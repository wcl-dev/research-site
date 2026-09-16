#!/usr/bin/env python3
"""CASE-2026-004 sweep extractor.

Reads one or more archived Keyword-mode runs, verifies each row actually carries a
link to the searched domain (decode the l.threads.com shim first — see
crawl-tool-quirks.md §7), groups by registry cluster (the `label` column of the
input CSV travels through the tool as `case_name`), and writes:

  analysis/sweep_hits.csv      one row per verified (post, domain)
  analysis/sweep_accounts.csv  one row per (cluster, account)
  analysis/sweep_summary.json  per-cluster domain hit counts, zero-hit domains,
                               tag inventory, overlap with CASE-002/003 accounts

Usage:
  sweep_extract.py [--prefix sweep_b1] [--input inputs/keywords_b1_confirmed_tw.csv] data/raw/<run_id>/keyword_result_*.csv [...]

  --prefix  輸出檔名前綴（預設 sweep；四批各用 sweep_b1..b4 免得互相覆蓋）
  --input   這輪實際搜的關鍵字檔；「searched／zero_hit」只算這份，網域→群對照仍用全部 keywords_*.csv
"""
from __future__ import annotations
import csv, json, re, sys, collections
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

import pandas as pd

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
INPUTS = CASE / 'inputs'
URL_RE = re.compile(r"https?://[^\s\"'<）)】\]]+")
TEXT_COLS = ('text', 'share_link', 'share_text', 'Quote_text', 'Quote_link')


def decode_meta_shim(url: str) -> str:
    if 'l.threads.com' not in url:
        return url
    q = parse_qs(urlparse(url).query).get('u')
    return unquote(q[0]) if q else url


def load_keywords() -> dict[str, str]:
    """domain -> cluster id, from every inputs/keywords_*.csv."""
    out = {}
    for p in sorted(INPUTS.glob('keywords_*.csv')):
        with p.open(encoding='utf-8-sig') as fh:
            for r in csv.DictReader(fh):
                out[r['keywords'].strip().lower()] = r['label'].strip()
    return out


def prior_accounts() -> dict[str, str]:
    """handle -> prior case id, for overlap reporting."""
    out = {}
    p2 = CASE.parent / 'CASE-2026-002-picread-content-farm' / 'analysis' / 'picread-family-registry.md'
    if p2.exists():
        for m in re.finditer(r'^\| `([^`]+)` \|', p2.read_text(encoding='utf-8'), re.M):
            out.setdefault(m.group(1), 'CASE-2026-002')
    p3 = CASE.parent / 'CASE-2026-003-alpha-dsawjk-content-farm' / 'analysis' / 'alpha_r1_accounts.csv'
    if p3.exists():
        for r in csv.DictReader(p3.open(encoding='utf-8')):
            out.setdefault(r['account'], 'CASE-2026-003')
    return out


def host_of(u: str) -> str:
    h = (urlparse(u).hostname or '').lower()
    return h[4:] if h.startswith('www.') else h


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--prefix', default='sweep')
    ap.add_argument('--input', type=Path)
    ap.add_argument('files', nargs='+')
    args = ap.parse_args(argv)
    argv = args.files
    dom2cl = load_keywords()
    searched_set = None
    if args.input:
        with args.input.open(encoding='utf-8-sig') as fh:
            searched_set = {r['keywords'].strip().lower() for r in csv.DictReader(fh)}
    prior = prior_accounts()
    frames = []
    for f in argv:
        df = pd.read_csv(f).fillna('')
        df['__src'] = Path(f).parent.name
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    # drop checkpoint/temp duplicates (§8) — caller should pass final files only, but be safe
    df = df.drop_duplicates(subset=['link']) if 'link' in df else df

    hits = []
    for _, r in df.iterrows():
        blob = ' '.join(decode_meta_shim(str(r[c])) for c in TEXT_COLS if c in df)
        urls = URL_RE.findall(blob)
        # bare "domain.tld/path…" in text (Threads truncates links) also counts
        for m in re.finditer(r'(?<![\w./])((?:[a-z0-9-]+\.)+[a-z]{2,})/[^\s…]*', blob, re.I):
            urls.append('https://' + m.group(0))
        seen = set()
        for u in urls:
            h = host_of(u)
            cl = None
            for d, c in dom2cl.items():
                if h == d or h.endswith('.' + d):
                    cl = c; dom = d; break
            if cl is None or (dom, r['link']) in seen:
                continue
            seen.add((dom, r['link']))
            frag = u.split('#', 1)[1] if '#' in u else ''
            uid = ''
            m = re.search(r'[?&]uid=(\d+)', u) or re.search(r'[?&]utm_term=(\d+)', u)
            if m: uid = m.group(1)
            hits.append(dict(run=r['__src'], cluster=cl, domain=dom, account=r['account'], date=str(r['date'])[:10],
                             link=r['link'], url=u.split('#')[0][:200], fragment=frag[:40], uid=uid,
                             likes=r.get('like', ''), keyword=r.get('key', ''), case_name=r.get('case_name', ''),
                             flag=r.get('match_flag', ''), text=str(r.get('text', ''))[:160].replace('\n', ' ')))
    H = pd.DataFrame(hits)
    (HERE / f'{args.prefix}_hits.csv').write_text('') if H.empty else H.to_csv(HERE / f'{args.prefix}_hits.csv', index=False)

    summary = {'rows_raw': int(len(df)), 'verified_hits': int(len(H)), 'input': str(args.input or ''), 'clusters': {}}
    acc_rows = []
    if not H.empty:
        for cl, g in H.groupby('cluster'):
            dom_hits = g.groupby('domain').size().sort_values(ascending=False).to_dict()
            searched = [d for d, c in dom2cl.items() if c == cl and (searched_set is None or d in searched_set)]
            zero = [d for d in searched if d not in dom_hits]
            tags = collections.Counter(f for f in g['fragment'] if f and not f.startswith('google_vignette'))
            uids = collections.Counter(u for u in g['uid'] if u)
            acc = g.groupby('account').agg(posts=('link', 'nunique'), domains=('domain', 'nunique'),
                                           first=('date', 'min'), last=('date', 'max'),
                                           tags=('fragment', lambda s: ','.join(sorted({x for x in s if x and not x.startswith('google_vignette')}))),
                                           uids=('uid', lambda s: ','.join(sorted({x for x in s if x}))),
                                           domain_list=('domain', lambda s: ','.join(sorted(set(s)))))
            for a, r in acc.iterrows():
                acc_rows.append(dict(cluster=cl, account=a, posts=int(r['posts']), domains=int(r['domains']), first=r['first'], last=r['last'],
                                     tags=r['tags'], uids=r['uids'], domain_list=r['domain_list'], prior_case=prior.get(a, '')))
            summary['clusters'][cl] = dict(searched=len(searched), domains_hit=dom_hits, zero_hit=zero,
                                           posts=int(len(g)), accounts=int(acc.shape[0]),
                                           accounts_ge2=int((acc.posts >= 2).sum()), accounts_ge5=int((acc.posts >= 5).sum()),
                                           tags=dict(tags.most_common(15)), uids=dict(uids.most_common(15)),
                                           overlap_prior={a: prior[a] for a in acc.index if a in prior})
    pd.DataFrame(acc_rows).to_csv(HERE / f'{args.prefix}_accounts.csv', index=False)
    (HERE / f'{args.prefix}_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding='utf-8')

    # console digest
    print(f"rows {summary['rows_raw']} | verified hits {summary['verified_hits']}")
    for cl, s in sorted(summary['clusters'].items(), key=lambda kv: -kv[1]['posts']):
        print(f"{cl:30s} searched={s['searched']:3d} hit_domains={len(s['domains_hit']):3d} posts={s['posts']:4d} accounts={s['accounts']:4d} (>=2:{s['accounts_ge2']}, >=5:{s['accounts_ge5']}) prior_overlap={len(s['overlap_prior'])} tags={list(s['tags'])[:4]} uids={list(s['uids'])[:4]}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
