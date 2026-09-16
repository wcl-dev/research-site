#!/usr/bin/env python3
"""CASE-2026-004 第二層核實：Account 模式發文史 → 每帳號判定。

輸入一個或多個已封存的 Account 模式 run（data/raw/<run_id>/），只看輸入檔列出的帳號
自己發的列（串內別人的回覆會混在 account_posts 裡，要濾掉），把每篇貼文的連結解開
l.threads.com 轉址殼（quirks §7）與文字裡被截斷的裸網域，對照 registry.yaml 的網域清單，算出：

  posts            該帳號自己的列數（貼文＋自回覆）
  farm_posts       帶 registry 網域連結的列數（連結卡片或文字裸網域皆算）
  card_posts       只算 share_link／Quote_link 連結卡片命中的列數（＝2026-09-07 R2 首版判定的口徑，留作對照）
  ratio            farm_posts / posts；判定用篇數不用比例
                   ★Threads 會把文字裡的連結截成「vivi01.com/watch…」且工具常抓不到卡片（share_link 空），
                   只認 https:// 會漏掉一半以上（R2 首版就是這樣漏了 [帳號已隱去] 的 68 篇）；
                   一篇農場文常是「原文 1 / 2」＋「2 / 2 帶連結」兩列，兩列都帶網域時各算一列，滿載帳號 ratio 會接近 1.0
  clusters         各群篇數
  top_domains      農場網域篇數（前 6）
  tags / uids      α 的 #threads<N>、γ 的 ?uid=、β/family-01 的 utm_term=N
  self_reply_2of2  文字含「2 / 2」的列數（分享工具注入的自回覆標記；與 reply_to 是否為自己無關）
  non_registry_top 非 registry 的外連網域（前 4；不含 threads.com）
  joined / location / followers / following  來自 accounts_*.csv
  serp_tag         原候選名單上的 tag（第一層來自哪一群），由 --serp-tags 指定的輸入檔查
  verdict          ≥5 篇或 ≥20% → 散布者（發文史核實）；1–4 篇且 <20% → 偶發轉貼；0 → 發文史無農場連結

用法：
  account_verdicts.py --run data/raw/2026-09-07_14-05-04 --input inputs/accounts_serp_candidates_r2b.csv \
      --serp-tags inputs/accounts_serp_candidates_r2.csv --out analysis/serp_candidates_r2b_verdicts.csv
"""
from __future__ import annotations
import argparse, collections, csv, re, sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

import pandas as pd
import yaml

HERE = Path(__file__).resolve().parent
CASE = HERE.parent
REGISTRY = Path.home() / 'kwara-farm-registry' / 'registry.yaml'
URL_RE = re.compile(r"https?://[^\s\"'<）)】\]]+")
BARE_RE = re.compile(r'(?<![\w./@])((?:[a-z0-9-]+\.)+[a-z]{2,})/[^\s…]*', re.I)
TEXT_COLS = ('text', 'share_link', 'share_text', 'Quote_text', 'Quote_link')
SKIP_HOSTS = {'threads.com', 'threads.net', 'l.threads.com'}


def decode_meta_shim(url: str) -> str:
    if 'l.threads.com' not in url:
        return url
    q = parse_qs(urlparse(url).query).get('u')
    return unquote(q[0]) if q else url


def host_of(u: str) -> str:
    h = (urlparse(u).hostname or '').lower()
    return h[4:] if h.startswith('www.') else h


def load_domain_map() -> dict[str, str]:
    """domain -> cluster id：registry.yaml 為主，inputs/keywords_*.csv 補（兩者應一致）。"""
    out: dict[str, str] = {}
    reg = yaml.safe_load(REGISTRY.read_text(encoding='utf-8'))
    for c in reg['clusters']:
        for d in c['domains']:
            name = d['name'] if isinstance(d, dict) else d
            out.setdefault(name.strip().lower(), c['id'])
    for p in sorted((CASE / 'inputs').glob('keywords_*.csv')):
        with p.open(encoding='utf-8-sig') as fh:
            for r in csv.DictReader(fh):
                k = r['keywords'].strip().lower()
                if '/' in k or ' ' in k or '.' not in k:
                    continue  # ref-groups 的集團名條目不是網域
                out.setdefault(k, r['label'].strip())
    return out


def match_cluster(host: str, dom2cl: dict[str, str]):
    for d, c in dom2cl.items():
        if host == d or host.endswith('.' + d):
            return d, c
    return None, None


def links_of(row: pd.Series, cols) -> list[str]:
    blob = ' '.join(decode_meta_shim(str(row[c])) for c in cols)
    urls = URL_RE.findall(blob)
    urls += ['https://' + m.group(0) for m in BARE_RE.finditer(blob)]
    return urls


def verdict_of(farm: int, ratio: float) -> str:
    if farm >= 5 or (farm and ratio >= 0.2):
        return '散布者（發文史核實）'
    if farm:
        return '偶發轉貼（發文史 <5 篇且 <20%）'
    return '發文史無農場連結（Google 命中可能為舊文或誤配）'


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--run', action='append', required=True, type=Path, help='data/raw/<run_id>（可重複）')
    ap.add_argument('--input', required=True, type=Path, help='跑這輪用的 inputs/accounts_*.csv（只判定其中帳號）')
    ap.add_argument('--serp-tags', type=Path, help='含 serp_candidate_*|群 標籤的候選名單，用來填 serp_tag')
    ap.add_argument('--out', required=True, type=Path)
    a = ap.parse_args(argv)

    dom2cl = load_domain_map()
    accounts = [r['account_name'].strip() for r in csv.DictReader(a.input.open(encoding='utf-8-sig'))]
    serp_tag = {}
    for p in [a.serp_tags, a.input]:
        if p and p.exists():
            for r in csv.DictReader(p.open(encoding='utf-8-sig')):
                serp_tag.setdefault(r['account_name'].strip(), r.get('tag', ''))

    posts, meta = [], {}
    for run in a.run:
        run = run if run.is_absolute() else CASE / run
        for f in sorted(run.glob('account_posts_*.csv')):
            if '_temp' in f.stem:
                continue
            df = pd.read_csv(f).fillna('')
            df['__run'] = run.name
            posts.append(df)
        for f in sorted(run.glob('accounts_*.csv')):
            if '_temp' in f.stem:
                continue
            for _, r in pd.read_csv(f).fillna('').iterrows():
                meta[str(r['account_name']).strip()] = r
    if not posts:
        sys.exit('no account_posts_*.csv found in the given runs')
    P = pd.concat(posts, ignore_index=True)
    P = P.drop_duplicates(subset=['link'])
    cols = [c for c in TEXT_COLS if c in P.columns]

    rows = []
    for acc in accounts:
        g = P[P['account'] == acc]
        m = meta.get(acc)
        base = dict(account=acc, posts=int(len(g)), farm_posts=0, card_posts=0, ratio=0.0, clusters='', top_domains='', tags='', uids='',
                    self_reply_2of2=int(g['text'].astype(str).str.contains(r'2\s*/\s*2').sum()) if len(g) else 0, non_registry_top='',
                    joined=(m['joined_raw'] if m is not None else ''), location=(m['based_in_raw'] if m is not None else ''),
                    followers=(m['followers_count'] if m is not None else ''), following=(m['following_count'] if m is not None else ''),
                    first=(str(g['date'].min())[:10] if len(g) else ''), last=(str(g['date'].max())[:10] if len(g) else ''),
                    serp_tag=serp_tag.get(acc, ''), verdict='')
        if not len(g):
            base['verdict'] = '未回傳（工具無資料）'
            rows.append(base)
            continue
        cl_c, dom_c, tag_c, uid_c, ext_c = (collections.Counter() for _ in range(5))
        farm = card = 0
        for _, r in g.iterrows():
            hit_doms, hit_cls, ext = set(), set(), set()
            cards = [decode_meta_shim(str(r[c])) for c in ('share_link', 'Quote_link') if c in cols and str(r[c])]
            if any(match_cluster(host_of(u), dom2cl)[1] for u in cards):
                card += 1
            for u in links_of(r, cols):
                h = host_of(u)
                if not h or h in SKIP_HOSTS:
                    continue
                d, c = match_cluster(h, dom2cl)
                if c:
                    hit_doms.add(d); hit_cls.add(c)
                    frag = u.split('#', 1)[1] if '#' in u else ''
                    if frag and not frag.startswith('google_vignette'):
                        tag_c['#' + frag.lstrip('#')[:30]] += 1
                    mm = re.search(r'[?&](uid|utm_term)=(\d+)', u)
                    if mm:
                        uid_c[f'{mm.group(1)}={mm.group(2)}'] += 1
                else:
                    ext.add(h)
            if hit_doms:
                farm += 1
                for d in hit_doms: dom_c[d] += 1
                for c in hit_cls: cl_c[c] += 1
            for h in ext: ext_c[h] += 1
        ratio = round(farm / len(g), 2)
        base.update(farm_posts=farm, card_posts=card, ratio=ratio,
                    clusters=','.join(f'{k}:{v}' for k, v in cl_c.most_common()),
                    top_domains=','.join(f'{k}:{v}' for k, v in dom_c.most_common(6)),
                    tags=','.join(f'{k}×{v}' for k, v in tag_c.most_common(6)),
                    uids=','.join(f'{k}×{v}' for k, v in uid_c.most_common(6)),
                    non_registry_top=','.join(f'{k}:{v}' for k, v in ext_c.most_common(4)),
                    verdict=verdict_of(farm, ratio))
        rows.append(base)

    out = pd.DataFrame(rows).sort_values(['farm_posts', 'posts'], ascending=[False, False])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(a.out, index=False)
    print(f'{len(out)} accounts → {a.out}')
    print(out['verdict'].value_counts().to_string())
    print(out[['account', 'posts', 'farm_posts', 'card_posts', 'ratio', 'clusters', 'tags', 'uids', 'self_reply_2of2', 'verdict']].to_string(index=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
