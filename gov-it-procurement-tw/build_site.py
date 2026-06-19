#!/usr/bin/env python3
"""build_site.py — 把政府 IT 採購市場結構研究組成 5 篇獨立 research-site HTML。
共用 CSS/JS（Template B「hardcore mono」皮膚，對齊姊妹報告）寫一次，組裝 5 篇 body。
register：白話、理性中立、學術保守（降行銷/張力/口語）。
輸出到 site/：index(導讀) + lock-in + geography + ownership + award-method。
"""
from pathlib import Path

OUT = Path(__file__).parent / "site"

STYLE = r"""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --c-paper:#fbfaf6; --c-paper-card:#f5f3ec; --c-paper-sink:#efece4;
  --c-ink:#333; --c-ink-soft:#555; --c-ink-faint:#888; --c-watermark:#aaa;
  --c-rule:#cfc9b9; --c-rule-soft:#dfd9c5;
  --c-navy:#1B4A66; --c-jade:#2B7458; --c-clay:#B5402B;
  --role-primary:var(--c-navy); --role-method:var(--c-jade); --role-emphasis:var(--c-clay);
  --ff-display:'IBM Plex Mono','PingFang TC','Microsoft JhengHei','Noto Sans TC',ui-monospace,'SF Mono',Menlo,monospace;
  --ff-serif:'IBM Plex Mono','PingFang TC','Microsoft JhengHei','Noto Sans TC',ui-monospace,'SF Mono',Menlo,monospace;
  --ff-mono:'IBM Plex Mono',ui-monospace,'SF Mono',Menlo,monospace;
  --maxw-prose:720px; --maxw-content:920px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--c-paper);color:var(--c-ink);font-family:var(--ff-serif);
  font-weight:400;font-size:15.5px;line-height:1.65;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
body::before{content:"";position:fixed;inset:0;z-index:9999;pointer-events:none;opacity:.18;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E")}
a{color:inherit}
::selection{background:var(--c-paper-card)}
.rv{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
.progress{position:fixed;top:0;left:0;height:2px;width:0;background:var(--role-emphasis);z-index:200;transition:width .12s linear}
.badge{position:fixed;top:18px;right:24px;z-index:100;font-size:14px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--c-ink);opacity:0;transition:opacity .25s;padding:8px 14px;background:var(--c-paper);border:1px solid var(--c-rule)}
.badge.show{opacity:.85}
.badge b{color:var(--role-emphasis);font-weight:700;margin-right:8px}
.series{max-width:var(--maxw-content);margin:0 auto;padding:30px 48px 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.series .sl{font-family:var(--ff-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--c-ink-faint);margin-right:6px;font-weight:600}
.series a{font-family:var(--ff-mono);font-size:12.5px;letter-spacing:.04em;color:var(--c-ink-soft);padding:7px 12px;border:1px solid var(--c-rule);background:var(--c-paper);text-decoration:none;transition:background .12s,border-color .12s,color .12s}
.series a:hover{background:var(--c-paper-card);border-color:var(--c-ink-faint)}
.series a.cur{background:var(--c-ink);color:var(--c-paper);border-color:var(--c-ink)}
.series a .sx{color:var(--c-ink-faint);margin-right:6px}
.series a.cur .sx{color:var(--c-paper-sink)}
.inline-toc{max-width:var(--maxw-content);margin:0 auto;padding:24px 48px 0;display:flex;flex-wrap:wrap;gap:8px}
.inline-toc a{font-family:var(--ff-mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--c-ink-soft);padding:7px 12px;border:1px solid var(--c-rule);background:var(--c-paper);text-decoration:none;transition:background .12s,border-color .12s,color .12s}
.inline-toc a:hover{background:var(--c-ink);color:var(--c-paper);border-color:var(--c-ink)}
.inline-toc .ix{color:var(--c-ink-faint);margin-right:6px}
main{display:block}
.wrap{max-width:var(--maxw-content);margin:0 auto;padding:0 48px}
section{padding:90px 0;border-bottom:1px solid var(--c-rule)}
section:last-of-type{border-bottom:none}
.hero{border-bottom:4px double var(--c-rule);background:linear-gradient(180deg,var(--c-paper-card),transparent 72%)}
.hero-inner{max-width:var(--maxw-content);margin:0 auto;padding:70px 48px 56px}
.hero-kicker{font-family:var(--ff-mono);font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--role-emphasis);font-weight:600;display:flex;align-items:center;gap:14px;margin-bottom:28px}
.hero-kicker::after{content:"";flex:1;height:1px;background:var(--c-rule)}
h1.hero-title{font-family:var(--ff-display);font-weight:600;font-size:clamp(26px,3.8vw,44px);line-height:1.3;letter-spacing:-.006em;margin-bottom:26px}
.hero-scope{font-family:var(--ff-display);font-weight:500;color:var(--c-ink);font-size:clamp(17px,2vw,20px);line-height:1.55;margin:-4px 0 30px;padding-left:16px;border-left:4px solid var(--role-primary)}
.hero-stand{font-size:17.5px;line-height:1.82;color:var(--c-ink-soft);max-width:var(--maxw-prose);margin-bottom:34px}
.hero-stand b{color:var(--c-ink);font-weight:700}
.hero-foot{margin-top:30px;font-size:14.5px;color:var(--c-ink-soft);display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.hero-foot .dot{width:7px;height:7px;border-radius:50%;background:var(--role-emphasis);display:inline-block;flex:none}
.sec-head{margin-bottom:48px}
.sec-num{font-family:var(--ff-mono);font-size:14px;font-weight:600;letter-spacing:.14em;color:var(--c-ink-faint);display:block;margin-bottom:16px}
h2.sec-title{font-family:var(--ff-display);font-weight:600;color:var(--c-watermark);font-size:clamp(23px,3vw,33px);line-height:1.32;letter-spacing:-.004em}
.sec-lead{font-size:17.5px;color:var(--c-ink-soft);margin-top:20px;max-width:var(--maxw-prose);line-height:1.78}
.sub-h{font-family:var(--ff-display);font-size:22px;font-weight:600;color:var(--c-ink);margin:0 0 24px;padding-bottom:14px;border-bottom:2px solid var(--c-rule);line-height:1.4}
.block{margin-top:56px}
.cap{font-family:var(--ff-mono);font-size:13.5px;color:var(--c-ink-soft);margin-bottom:18px;font-weight:500;letter-spacing:.01em}
.prose p{margin-bottom:22px;max-width:var(--maxw-prose)}
.prose p:last-child{margin-bottom:0}
.prose b{color:var(--c-ink);font-weight:700}
.prose .em{font-weight:700;background:var(--c-paper-sink);padding:1px 5px;border-radius:3px}
.tldr-list{display:flex;flex-direction:column;gap:14px}
.tldr{display:flex;gap:26px;padding:30px 32px;background:var(--c-paper-card);border:1px solid var(--c-rule);border-radius:12px;align-items:flex-start}
.tldr .num{font-family:var(--ff-display);font-size:44px;font-weight:600;line-height:.9;color:var(--role-primary);flex:none;width:48px}
.tldr .body p{font-size:17.5px;line-height:1.82}
.tldr .body b{font-weight:700;color:var(--c-ink)}
.find{background:var(--c-paper-card);border:1px solid var(--c-rule);border-radius:16px;padding:38px 40px;margin-bottom:24px}
.find-top{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap;margin-bottom:20px}
.find-no{font-family:var(--ff-mono);font-size:14px;font-weight:600;letter-spacing:.08em;color:var(--c-paper-card);background:var(--c-ink);padding:7px 12px;border-radius:6px;flex:none}
.find h3{font-family:var(--ff-display);font-size:22px;font-weight:600;line-height:1.44;flex:1;min-width:260px}
.find-sum{font-size:17.5px;line-height:1.84;color:var(--c-ink-soft)}
.find-sum b{color:var(--c-ink);font-weight:700}
.find-sum .em{font-weight:700;background:var(--c-paper-sink);padding:1px 5px;border-radius:3px}
.find-key{margin-top:24px;padding:22px 26px;background:var(--c-paper-sink);border-radius:11px;font-size:16.5px;line-height:1.74}
.find-key .kl{font-family:var(--ff-mono);font-size:13px;letter-spacing:.08em;color:var(--role-emphasis);font-weight:600;display:block;margin-bottom:6px}
.find-key b{font-weight:700;color:var(--c-ink)}
.find .block{margin-top:32px}
.find-more{display:inline-block;margin-top:24px;font-family:var(--ff-mono);font-size:13.5px;font-weight:600;letter-spacing:.04em;color:var(--role-primary);text-decoration:none;border-bottom:2px solid var(--role-primary);padding-bottom:2px}
.find-more:hover{color:var(--role-emphasis);border-color:var(--role-emphasis)}
footer{background:var(--c-ink);color:var(--c-ink-faint);padding:46px 28px;font-size:14.5px;line-height:1.85}
footer .ft-inner{max-width:var(--maxw-content);margin:0 auto}
footer b{color:var(--c-paper-card);font-weight:700}
footer a{color:var(--c-paper-card);border-bottom:1px solid rgba(255,255,255,.25);text-decoration:none}
.src-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.src{background:var(--c-paper-card);border:1px solid var(--c-rule);border-radius:11px;padding:22px 24px;font-size:15px;line-height:1.7;color:var(--c-ink-soft)}
.src .src-k{font-family:var(--ff-mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--role-primary);font-weight:600;display:block;margin-bottom:8px}
.src b{color:var(--c-ink);font-weight:700}
.hero-numbers{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin:36px 0 8px;border:1px solid var(--c-rule);border-radius:14px;overflow:hidden;background:var(--c-paper-card)}
.hn-cell{padding:28px 26px}
.hn-cell+.hn-cell{border-left:1px solid var(--c-rule)}
.hn-big{font-family:var(--ff-display);font-size:30px;font-weight:600;line-height:1.12;color:var(--role-primary);margin-bottom:10px}
.hn-big .unit{font-size:17px;color:var(--c-ink-soft);font-weight:500;margin-left:4px}
.hn-lbl{font-family:var(--ff-mono);font-size:11.5px;color:var(--c-ink-faint);letter-spacing:.12em;text-transform:uppercase;font-weight:600;margin-bottom:6px}
.hn-sub{font-size:14px;color:var(--c-ink-soft);line-height:1.6}
.schema{background:var(--c-paper-card);border:2px solid var(--role-primary);border-radius:14px;padding:30px 34px;margin-top:10px}
.schema-h{font-family:var(--ff-display);font-size:21px;font-weight:600;color:var(--role-primary);margin-bottom:6px}
.schema-sub{font-family:var(--ff-mono);font-size:13px;color:var(--c-ink-faint);letter-spacing:.06em;margin-bottom:22px}
.schema-row{display:grid;grid-template-columns:120px 150px 1fr;gap:18px;padding:16px 0;align-items:start;border-top:1px solid var(--c-rule-soft)}
.schema-row:first-child{border-top:none;padding-top:0}
.schema-code{font-family:var(--ff-mono);font-size:13px;font-weight:700;color:#fff;background:var(--role-primary);padding:5px 10px;border-radius:5px;text-align:center;height:fit-content;letter-spacing:.04em;white-space:nowrap}
.schema-name{font-family:var(--ff-display);font-size:16px;font-weight:600;color:var(--c-ink);line-height:1.4;padding-top:3px}
.schema-def{font-size:15px;line-height:1.7;color:var(--c-ink-soft);padding-top:3px}
.schema-def b{color:var(--c-ink);font-weight:700}
.schema-foot{margin-top:22px;padding-top:20px;border-top:1px solid var(--c-rule);font-size:15px;line-height:1.74;color:var(--c-ink-soft)}
.schema-foot b{color:var(--role-primary);font-weight:700}
.spectrum{margin-top:18px}
.sp-row{display:grid;grid-template-columns:210px 1fr 168px;gap:14px;align-items:center;padding:10px 0}
.sp-row+.sp-row{border-top:1px dotted var(--c-rule)}
.sp-name{font-size:15px;color:var(--c-ink)}
.sp-track{height:24px;background:var(--c-paper-sink);border-radius:4px;position:relative;overflow:hidden}
.sp-fill{height:100%;background:var(--role-emphasis);border-radius:4px;transition:width 1.1s cubic-bezier(.2,.7,.2,1)}
.sp-fill.alt{background:var(--role-primary)}
.sp-val{font-family:var(--ff-mono);font-size:13px;color:var(--c-ink-soft);text-align:right;white-space:nowrap}
.sp-val b{font-family:var(--ff-display);font-size:16px;color:var(--c-ink);font-weight:700;margin-right:6px}
.chains{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.chain{border:1px solid var(--c-rule);border-radius:16px;overflow:hidden;background:var(--c-paper-card)}
.chain-top{padding:24px 26px}
.chain.A .chain-top{background:var(--role-primary)}
.chain.B .chain-top{background:var(--role-method)}
.chain-top *{color:#fff}
.chain-tag{font-family:var(--ff-mono);font-size:13px;letter-spacing:.1em;opacity:.82;text-transform:uppercase}
.chain-name{font-family:var(--ff-display);font-size:21px;font-weight:600;margin-top:7px}
.chain-sub{font-size:14px;opacity:.9;margin-top:8px;line-height:1.6}
.chain-rows{padding:6px 26px 22px}
.crow{padding:16px 0}
.crow+.crow{border-top:1px solid var(--c-rule)}
.crow .lbl{font-size:13.5px;color:var(--c-ink-faint);margin-bottom:7px}
.crow .val{font-size:16px;line-height:1.62}
.crow .val b{font-weight:700;color:var(--c-ink)}
.verify{width:100%;border-collapse:collapse;font-size:15px;margin-top:14px}
.verify th,.verify td{border-bottom:1px solid var(--c-rule);padding:14px 14px;vertical-align:top;text-align:left}
.verify th{font-family:var(--ff-mono);font-size:12px;color:var(--c-ink-faint);letter-spacing:.06em;text-transform:uppercase;font-weight:600;background:var(--c-paper-sink)}
.verify .vid{font-family:var(--ff-display);font-weight:700;color:var(--role-primary)}
.verify .ok{color:var(--role-method);font-weight:700;white-space:nowrap}
.verify .upd{color:var(--role-emphasis);font-weight:700;white-space:nowrap}
.flagship{margin-top:16px;padding:30px 28px;background:var(--c-ink);border-radius:16px;color:var(--c-paper-card)}
.flag-lab{font-family:var(--ff-mono);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--c-paper-sink);opacity:.7;margin-bottom:8px;font-weight:600}
.flag-h{font-family:var(--ff-display);font-size:22px;font-weight:600;color:#fff;margin-bottom:20px;line-height:1.4}
.flag-tbl{width:100%;border-collapse:collapse;font-size:15px;color:var(--c-paper-card)}
.flag-tbl th,.flag-tbl td{padding:13px 10px;text-align:right;border-bottom:1px solid rgba(255,255,255,.1)}
.flag-tbl th{font-family:var(--ff-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--c-paper-sink);opacity:.75;font-weight:600;background:rgba(255,255,255,.04)}
.flag-tbl th:first-child,.flag-tbl td:first-child{text-align:left;font-family:var(--ff-display);font-size:15px;font-weight:500;color:#fff;padding-left:14px}
.flag-tbl tr.total td{font-weight:700;color:#fff;background:rgba(255,255,255,.05);border-bottom:none}
.flag-tbl .dom{background:var(--role-emphasis);color:#fff;font-weight:700;border-radius:4px}
.flag-note{font-size:14px;color:var(--c-paper-sink);opacity:.82;margin-top:18px;line-height:1.7}
.flag-note b{color:#fff;font-weight:700}
.gaps{list-style:none}
.gaps li{position:relative;padding:18px 22px 18px 56px;margin-bottom:12px;background:var(--c-paper-card);border:1px solid var(--c-rule);border-radius:11px;font-size:16px;line-height:1.76;color:var(--c-ink-soft)}
.gaps li::before{content:"!";position:absolute;left:20px;top:18px;font-family:var(--ff-display);font-weight:700;font-size:19px;color:var(--role-emphasis);width:26px;height:26px;border:2px solid var(--role-emphasis);border-radius:50%;text-align:center;line-height:23px}
.gaps li b{color:var(--c-ink);font-weight:700}
@media(max-width:1040px){.hero-numbers{grid-template-columns:1fr}.hn-cell+.hn-cell{border-left:none;border-top:1px solid var(--c-rule)}.chains{grid-template-columns:1fr}}
@media(max-width:600px){
  body{font-size:14.5px}.badge{display:none}
  .series,.inline-toc{padding-left:24px;padding-right:24px}
  .wrap,.hero-inner{padding-left:24px;padding-right:24px}
  section{padding:60px 0}.hero-inner{padding-top:48px}
  .find{padding:26px 22px}.tldr{padding:22px;gap:16px}.tldr .num{font-size:36px;width:40px}
  .schema{padding:22px 18px}.schema-row{grid-template-columns:1fr;gap:8px}.schema-code{width:fit-content}
  .src-grid{grid-template-columns:1fr}.sp-row{grid-template-columns:120px 1fr 96px;gap:10px}
  .verify th,.verify td{padding:10px 8px;font-size:13.5px}
  .flagship{padding:22px 16px}.flag-tbl{font-size:13px}.flag-tbl th,.flag-tbl td{padding:10px 6px}
  footer{padding:34px 24px}
}
</style>"""

SCRIPT = r"""<script>
(function(){
  const progress=document.getElementById('progress'),badge=document.getElementById('badge');
  const bn=document.getElementById('badgenum'),bnm=document.getElementById('badgename');
  const secs=Array.from(document.querySelectorAll('section[data-num]'));
  function up(){
    const dh=document.documentElement.scrollHeight-window.innerHeight;
    const pct=dh>0?Math.min(100,(window.scrollY/dh)*100):0;
    if(progress)progress.style.width=pct+'%';
    const y=window.scrollY+120;let a=secs[0];
    for(const s of secs){if(s.offsetTop<=y)a=s;}
    if(a&&bn){bn.textContent=a.dataset.num;bnm.textContent=a.dataset.name||'';
      if(window.scrollY>240)badge.classList.add('show');else badge.classList.remove('show');}
  }
  window.addEventListener('scroll',up,{passive:true});up();
})();
(function(){
  const els=document.querySelectorAll('.rv');
  if(!els.length||!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in'));return;}
  const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:0.12,rootMargin:'0px 0px -8% 0px'});
  els.forEach(e=>io.observe(e));
})();
</script>"""

SERIES = [("","導讀","overview"),("lock-in/","供應商鎖定","lock-in"),
          ("geography/","地理集中","geography"),("ownership/","供給端集團","ownership"),
          ("award-method/","決標原則","award-method")]

def series_nav(cur, prefix):
    items=[]
    for i,(path,label,key) in enumerate(SERIES,1):
        href=(prefix+path) or "./"
        c=" cur" if key==cur else ""
        items.append(f'<a class="{c.strip()}" href="{href}"><span class="sx">{i:02d}</span>{label}</a>')
    return ('<nav class="series" aria-label="本專題">\n  <span class="sl">本專題 · 政府資訊採購</span>\n  '
            + "\n  ".join(items) + "\n</nav>")

def page(dest_rel, title, desc, prefix, cur, hero, toc, body, foot_line):
    badge='<div class="progress" id="progress"></div>\n<div class="badge" id="badge"><b id="badgenum">01</b><span id="badgename"></span></div>'
    html=f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — weichen's Research</title>
<meta name="description" content="{desc}">
{STYLE}
</head>
<body>
{badge}
<main>
{hero}
{series_nav(cur, prefix)}
{toc}
{body}
</main>
<footer><div class="ft-inner">
{foot_line}<br>
資料：政府電子採購網半月公開資料 · 廠商集團以商工登記董監事還原 · 2026 / 06<br>
定位：在公開資料範圍內描述市場結構，標示值得查核之處，不認定個案違法<br>
研究儲存庫 · <a href="https://github.com/wcl-dev/research-site">github.com/wcl-dev/research-site</a> · <a href="{prefix}../">回 weichen's Research 首頁</a>
</div></footer>
{SCRIPT}
</body>
</html>"""
    p=OUT/dest_rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    return len(html)

def hero(kicker,title,scope,stand,cells,foot):
    hn="".join(f'<div class="hn-cell"><div class="hn-lbl">{l}</div><div class="hn-big">{b}</div><div class="hn-sub">{s}</div></div>' for l,b,s in cells)
    return f"""<header class="hero"><div class="hero-inner">
<div class="hero-kicker">{kicker}</div>
<h1 class="hero-title">{title}</h1>
<p class="hero-scope">{scope}</p>
<p class="hero-stand">{stand}</p>
<div class="hero-numbers">{hn}</div>
<div class="hero-foot"><span class="dot"></span><span>{foot}</span></div>
</div></header>"""

def toc(items):
    a="".join(f'<a href="#{i}"><span class="ix">§{n:02d}</span>{lab}</a>' for n,(i,lab) in enumerate(items,1))
    return f'<nav class="inline-toc" aria-label="目次">{a}</nav>'

def sec(num,sid,name,title,lead,inner):
    return f"""<section id="{sid}" data-num="{num:02d}" data-name="{name}"><div class="wrap">
<header class="sec-head rv"><span class="sec-num">{num:02d}</span><h2 class="sec-title">{title}</h2>{f'<p class="sec-lead">{lead}</p>' if lead else ''}</header>
{inner}
</div></section>"""

# 共用：守線 find-key、來源段
DISCIPLINE = ('<div class="find-key rv" style="margin-top:36px"><span class="kl">用語界線</span>'
  '<b>限制性招標、廠商集中、重複得標，在本研究中均作為結構訊號，而非違法證據。</b>'
  '《政府採購法》第 22 條對限制性招標列有合法事由（獨家、後續擴充、相容、緊急）。'
  '本研究在公開資料範圍內描述結構，不對個案作違法認定。</div>')

def sources(extra):
    return f"""<div class="src-grid">
<div class="src"><span class="src-k">主要資料 · 採購</span><b>政府電子採購網半月公開資料</b>（行政院公共工程委員會）。決標公告約 8.6 萬筆，經 twinkle-hub 正規化彙整；本研究取其資訊類 13,339 筆，2015–2026。授權：政府網站資料開放宣告，須註明出處。</div>
<div class="src"><span class="src-k">廠商集團 · 商工登記</span>公司董監事「所代表法人」席次，原始來源經濟部商業發展署，經歐噴資料庫（data.openfun.tw）／g0v 整理；用以還原控制集團、並以財政部稅籍行業代號標記非資訊類廠商。</div>
{extra}
<div class="src"><span class="src-k">再現材料</span>母體定義、集團歸戶證據、集中度與清洗計算（JSON／Python）公開於 randomfindings 專案目錄，可逐步重跑。</div>
</div>"""

# ════════════════════════════════════════════════════════════════════
# 篇 1 · 導讀（index）
# ════════════════════════════════════════════════════════════════════
ov_hero=hero(
  "政府採購開放資料 · 資訊類市場結構 · 專題導讀",
  "政府資訊採購的市場結構：四個面向",
  "以政府電子採購網 2015–2026 約 1.3 萬筆資訊類決標公告，從供應商鎖定、廠商地理分布、供給端集團組成、決標原則四個面向，描述政府採購資訊服務的市場結構。",
  "本專題分為一篇導讀與四篇分論。整體而言，在此資料範圍內，資訊類採購較一般政府採購更倚賴限制性招標、得標廠商在地理上集中於台北、供給端在還原控制集團後較帳面更為集中；而「採購偏向低價」這一常見推論不被資料支持。本篇說明母體與方法，並概述四個面向與其相互關係。",
  [("母體","13,339<span class='unit'>件</span>","2015–2026 資訊類決標；清除非資訊類後乾淨名目約 3,050 億"),
   ("限制性招標","37<span class='unit'>%</span>","資訊類限制性招標合計佔比（全體政府採購約 22%）"),
   ("開源相關標題","0<span class='unit'>筆</span>","16 萬筆招標／決標標題，含「開源／公共程式」者")],
  "資料：政府電子採購網半月公開資料 · 廠商集團以商工登記董監事還原 · 訊號非定罪")

ov_toc=toc([("scope","母體與方法"),("threads","四個面向"),("synthesis","綜述"),("sources","資料來源")])

ov_threads=""
TH=[("01","供應商鎖定","lock-in/","以「限制性招標（未經公開評選）」的比率與機關—廠商長年配對，檢視鎖定。資訊類無公開競爭採購約佔公告金額以上案件的五分之一，且 2018–2025 由約 17% 升至約 22%。"),
    ("02","地理集中","geography/","由廠商登記地址解析縣市。台北市登記廠商取得資訊類決標金額約七成；買方機關不在台北時，其資訊支出仍有約 72% 金額由台北廠商承作。"),
    ("03","供給端集團組成","ownership/","以商工登記董監事資料還原控制集團。帳面數千家廠商中，部分為同一集團的不同名子公司；還原後集中度較帳面提高，但長尾仍由逾四千家獨立廠商構成。"),
    ("04","決標原則","award-method/","以決標原則檢視「採購偏向低價」一說。低價標集中於硬體（商品化，屬合理），客製服務多採比品質選商；此說在資料中不成立。")]
for no,nm,href,summ in TH:
    ov_threads+=f"""<div class="find rv"><div class="find-top"><span class="find-no">面向 {no}</span><h3>{nm}</h3></div>
<div class="find-sum"><p>{summ}</p></div>
<a class="find-more" href="{href}">閱讀本面向分論 →</a></div>
"""

ov_body = (
 sec(1,"scope","母體與方法","母體與方法：什麼算「資訊採購」，以及兩道清洗",
   "本專題是「政府採購人格類型學」的資訊類延伸，沿用相同資料源與「訊號非定罪」的用語界線。",
   '<div class="prose rv"><p>政府每年以公帑採購資訊系統與服務，這些系統承載稅務、健保、郵政、戶政、交通等核心業務的日常運作。本研究的資訊類母體（13,339 件、清洗後名目約 3,050 億）即是觀察這個市場結構的窗口。</p>'
   '<p>本研究的「資訊類母體」定義為：標的屬<b>財物或勞務</b>（排除工程類，以剔除捷運號誌、鐵路電氣化等系統工程）、且標案名稱命中資訊關鍵字（系統／軟體／資訊／資通／雲端／資安／網路／程式等）。得到 <b>13,339 件</b>資訊類決標，橫跨 2015–2026。資料採半月公開資料，各年份收錄密度不一，故跨年趨勢僅就「未經公開評選」這一十一年用字一致的欄位進行，並條件化於「公告金額以上」母體。</p></div>'
   '<div class="block rv"><div class="sub-h">清洗一：以行業代號剔除非資訊類</div><div class="prose">'
   '<p>「系統」一詞會誤含重電、環保、醫療設備（例如中欣行屬環境檢測、台灣世曦屬土木工程顧問）。本研究以商工登記的財政部稅籍<b>行業代號</b>判定大額廠商是否屬資訊類：前 30 大金額廠商中，約 <b>738 億（佔帳面 19.5%）為非資訊類</b>。因此金額型陳述採清洗後的乾淨值約 <b>3,050 億</b>；件數型陳述不受影響（污染僅集中於少數大案）。</p></div></div>'
   '<div class="block rv"><div class="sub-h">清洗二：以董監事資料還原控制集團</div><div class="prose">'
   '<p>帳面上有數千家廠商，其中部分為同一集團的不同名子公司。本研究以公司董監事「所代表法人」的席次，將廠商歸戶至實際控制集團（例如資拓宏宇董事會 10 席中，中華電信占 5 席）。此還原為「供給端集團組成」一篇的核心。</p></div></div>'
   + DISCIPLINE)
 + sec(2,"threads","四個面向","四個面向","以下四篇分論，各自說明該面向的資料、方法與發現。",
   '<div class="rv">'+ov_threads+'</div>')
 + sec(3,"synthesis","綜述","綜述：市場結構與數位轉型、開源的關係",None,
   '<div class="prose rv">'
   '<p>四個面向指向一致的結構：得標廠商在地理上集中於台北、個別機關傾向由既有廠商承作、供給端存在一個規模明顯領先的供應集團（中華電信集團，由交通部為最大股東），而決標原則的差異主要反映標的性質而非單純壓低價格。這個結構與兩個常被討論的問題相關。</p>'
   '<p>其一，<b>開源／公共程式在採購標題層未見出現</b>。16 萬筆招標與決標標題中，含「開源／開放原始碼／公共程式／自由軟體」者為零（此為標題層觀察，不代表規格書零要求）。在既有廠商與專屬技術形成較高轉換成本的結構下，開源方案（任何人皆可維護、可降低轉換成本）較難取得切入點。</p>'
   '<p>其二，採購結構在主管機關自身亦可見。政府將相當部分資訊業務委由自家捐助法人承作——工業技術研究院（91 案，跨 24 機關）、資訊工業策進會（70 案，跨 15 機關）；數位發展部自身金額最大的兩個承作對象，亦為資策會（24 案、16.7 億）與工研院。此處非評價法人是否適任，而是指出此一路徑未經公開競爭。</p>'
   '<p>綜合而言，在此資料範圍內，資訊採購的競爭限制主要不在「全國市佔由少數廠商把持」，而在<b>地理集中、機關層級的承作延續、以及大型標案的集中</b>。若以降低轉換成本（開放標準、可攜架構、原始碼交付）與降低進入門檻（在地化、模組化）為方向，較有機會擴大競爭。詳細證據見四篇分論。</p>'
   '</div>')
 + sec(4,"sources","資料來源","資料來源與再現材料",None, sources("")))

page("index.html",
  "政府資訊採購的市場結構：四個面向",
  "以政府電子採購網 2015–2026 約 1.3 萬筆資訊類決標公告，從供應商鎖定、地理分布、供給端集團組成、決標原則四個面向描述政府資訊採購的市場結構。專題導讀。",
  "", "overview", ov_hero, ov_toc, ov_body,
  "<b>政府資訊採購的市場結構：四個面向</b>（專題導讀）")

print("✓ index.html (導讀)")

# ════════════════════════════════════════════════════════════════════
# 篇 2 · 供應商鎖定（D）
# ════════════════════════════════════════════════════════════════════
d_hero=hero(
  "政府資訊採購市場結構 · 面向一",
  "資訊採購中的供應商鎖定：無競爭採購與長年配對",
  "以「限制性招標（未經公開評選）」的比率，以及機關與廠商的長年配對關係，檢視資訊採購中供應商延續承作的程度。",
  "在公告金額以上的資訊類採購中，無公開競爭、直接議價的案件約佔五分之一，且 2018–2025 年呈緩升。在機關層級，部分機關長年由同一廠商承作。本文區分兩種長年配對：一種持續以單一來源直接議價，另一種雖每次公開競爭、仍由既有廠商持續得標；兩者治理意義不同，但均使既有廠商不易被替換。",
  [("無公開競爭採購","約 1/5","公告金額以上資訊類採購中，未經公開評選之佔比"),
   ("趨勢","17→22<span class='unit'>%</span>","2018→2025，未經公開評選佔比緩升"),
   ("對照全體","約 1.4<span class='unit'>×</span>","資訊類未經公開評選佔比相對全政府同口徑")],
  "資料：政府電子採購網 · 招標方式以原始值判讀（欄名易誤導）· 訊號非定罪")
d_toc=toc([("method","方法"),("rate","無公競爭採購"),("pairs","兩種長年配對"),("case","逐年重複的單一來源採購"),("limits","限制"),("sources","資料來源")])
d_body=(
 sec(1,"method","方法","方法：以招標方式衡量競爭開放程度","招標方式（procurement_type）以欄位實際值判讀，而非欄名。",
   '<div class="prose rv">'
   '<p>「限制性招標（未經公開評選或公開徵求）」指機關不經公開競爭，直接洽特定廠商議價，是供應商延續承作最直接的訊號。此標籤十一年間用字一致，適合觀察跨年變化。為使各年可比，本文將分母條件化於「<b>公告金額以上</b>」的資訊類採購（排除「公開取得報價單」等小額方式，其在 2022 年因收錄範圍變動而大量出現）。</p>'
   '<p>在機關—廠商配對層面，本文以「未經公開評選件數 / 總件數」作為單一來源比例，量度某一配對中無公開競爭的程度；數值高者表示該機關對該廠商的採購多以直接議價進行。</p>'
   '</div>')
 + sec(2,"rate","無公競爭採購","無公開競爭採購的比率高於全政府，並呈緩升",None,
   '<div class="find rv"><div class="find-top"><span class="find-no">發現一</span><h3>每五件公告金額以上的資訊採購，約有一件未經公開競爭</h3></div>'
   '<div class="find-sum"><p>在公告金額以上的資訊類採購中，未經公開評選之佔比於 2015 年約 20%，2018 年一度降至約 17%，其後回升，2023–2025 年約 22%。對照全政府同口徑（約 14%），資訊類整體高出約 1.4 倍。</p></div>'
   '<div class="block"><div class="cap">未經公開評選佔「公告金額以上資訊類決標」之比率（逐年）</div><div class="spectrum">'
   '<div class="sp-row rv"><div class="sp-name">2015</div><div class="sp-track"><div class="sp-fill" style="width:19.6%"></div></div><div class="sp-val"><b>19.6%</b>93 / 474</div></div>'
   '<div class="sp-row rv"><div class="sp-name">2018</div><div class="sp-track"><div class="sp-fill" style="width:16.9%"></div></div><div class="sp-val"><b>16.9%</b>125 / 740</div></div>'
   '<div class="sp-row rv"><div class="sp-name">2021</div><div class="sp-track"><div class="sp-fill" style="width:19.6%"></div></div><div class="sp-val"><b>19.6%</b>163 / 833</div></div>'
   '<div class="sp-row rv"><div class="sp-name">2023</div><div class="sp-track"><div class="sp-fill" style="width:22.9%"></div></div><div class="sp-val"><b>22.9%</b>176 / 768</div></div>'
   '<div class="sp-row rv"><div class="sp-name">2025</div><div class="sp-track"><div class="sp-fill" style="width:22.4%"></div></div><div class="sp-val"><b>22.4%</b>189 / 843</div></div>'
   '</div></div>'
   '<div class="find-key"><span class="kl">說明</span>未經公開評選有合法事由（如原廠專屬、後續擴充），故此比率為值得查核的結構指標，而非違法比率。資訊類高於全政府，與資訊系統建置後維護、擴充多須由原建置者承作的特性一致。</div></div>'
   '<div class="find rv"><div class="find-top"><span class="find-no">發現二</span><h3>資訊支出較多用於維持既有系統，而非建置新系統</h3></div>'
   '<div class="find-sum"><p>在標題明確標示用途的案件中，「維持既有」（維護、維運、授權、擴充、升級）的件數約為「建置新系統」（建置、開發、導入）的 <b>3.5 倍</b>（4,278 件 vs 1,219 件）。在未經公開評選的資訊案中，約 <b>45%</b> 的標題即明示為既有系統的維護、授權或擴充（728 / 1,612）。</p></div>'
   '<div class="find-key"><span class="kl">與轉型的關係</span>採購結構偏向維持既有系統，是「數位轉型不易前進」可在資料中觀察到的一個面向：相當部分的資訊預算用於延續既有系統的運轉，而延續既有系統多須由原建置者承作，兩者相互強化。（其餘約六成案件標題用語較一般，如採購、服務、委託，未必能據以判斷新舊。）</div></div>')
 + sec(3,"pairs","兩種長年配對","機關層級的兩種長年配對","同樣是「多年由同一廠商承作」，其競爭性質可分為兩類；同一區分亦見於各機關的直接議價結構。",
   '<div class="chains rv">'
   '<article class="chain A"><div class="chain-top"><div class="chain-tag">類型一</div><div class="chain-name">持續單一來源</div><div class="chain-sub">多年承作，且多數以直接議價進行</div></div>'
   '<div class="chain-rows">'
   '<div class="crow"><div class="lbl">範例</div><div class="val">中華郵政 × IBM（25 件 / 9 年；單一來源比 <b>100%</b>）</div></div>'
   '<div class="crow"><div class="lbl">其他</div><div class="val">中華郵政 × 駿永 82%、× 細達 95%；智財局 × 碩睿 100%</div></div>'
   '<div class="crow"><div class="lbl">對應特性</div><div class="val">核心系統綁定特定技術，後續授權與維護多須由同一廠商承作</div></div>'
   '<div class="crow"><div class="lbl">合法事由</div><div class="val">原廠專屬、後續擴充常屬法律允許之單一來源採購</div></div>'
   '</div></article>'
   '<article class="chain B"><div class="chain-top"><div class="chain-tag">類型二</div><div class="chain-name">重複競標、既有廠商持續得標</div><div class="chain-sub">多年承作，但多數經公開競爭</div></div>'
   '<div class="chain-rows">'
   '<div class="crow"><div class="lbl">範例</div><div class="val">健保署 × 資拓宏宇（49 件 / 10 年；單一來源比 <b>6%</b>）</div></div>'
   '<div class="crow"><div class="lbl">其他</div><div class="val">警政署 × 精誠科技整合 0%、主計總處 × 晶茂 0%</div></div>'
   '<div class="crow"><div class="lbl">對應特性</div><div class="val">程序合規、公開競爭，既有廠商因轉換成本與領域知識持續得標</div></div>'
   '<div class="crow"><div class="lbl">判讀</div><div class="val">較難以本資料指為問題，但同樣使既有廠商不易被替換</div></div>'
   '</div></article>'
   '</div>'
   '<div class="find-key rv" style="margin-top:30px"><span class="kl">說明</span>兩類配對的治理意義不同：類型一無公開競爭，類型二保有競爭程序。但兩者皆指向「既有廠商延續承作」的結構，這也是新進廠商、在地中小廠與開源方案較難切入的層級。</div>'
   '<div class="block rv"><div class="flagship"><div class="flag-lab">未經公開評選資訊採購 · 件數最多的機關（2015–2026）</div><div class="flag-h">直接議價的資訊採購，集中於少數機關</div>'
   '<table class="flag-tbl"><thead><tr><th>機關</th><th>直接議價件數</th><th>不同廠商數</th><th>金額</th></tr></thead><tbody>'
   '<tr><td>中華郵政</td><td>328</td><td>73</td><td>111.5 億</td></tr>'
   '<tr><td>中央研究院</td><td>166</td><td>110</td><td>31.2 億</td></tr>'
   '<tr><td>台灣中油</td><td>73</td><td>34</td><td>25.0 億</td></tr>'
   '<tr><td>交通部臺鐵</td><td>26</td><td class="dom">11</td><td>29.5 億</td></tr>'
   '<tr><td>飛航服務總臺</td><td>26</td><td class="dom">10</td><td>16.6 億</td></tr>'
   '<tr><td>經濟部智慧財產局</td><td>18</td><td class="dom">6</td><td>1.3 億</td></tr>'
   '</tbody></table>'
   '<p class="flag-note"><b>兩種型態並存：</b>中央研究院直接議價件數雖多，但分散於 110 家廠商（多為各自獨家的科研儀器與系統），接近前述「程序上未公開競爭、但廠商分散」一類；臺鐵、飛航服務總臺、智財局等則由極少數廠商承作（11、10、6 家），屬集中於少數既有廠商一類。兩者均有合法事由，差別在競爭是否集中。</p></div></div>')
 + sec(4,"case","逐年重複的單一來源採購","逐年重複的單一來源採購：以中華郵政的大型主機為例","此例說明系統建置後，後續支出如何長期集中於原廠。",
   '<div class="prose rv" style="margin-bottom:28px"><p>中華郵政的資訊採購分散於約七至八家廠商，其中多數配對的單一來源比偏高。以其 IBM z/OS 大型主機相關採購為例，2015 年起每年大致固定為三筆，且均以未經公開評選方式辦理。</p></div>'
   '<div class="flagship rv"><div class="flag-lab">中華郵政 · IBM 大型主機相關採購（2015 年起）</div><div class="flag-h">系統建置後，後續授權、維護逐年由原廠承作</div>'
   '<table class="flag-tbl"><thead><tr><th>逐年大致固定的品項</th><th>典型金額</th><th>招標方式</th></tr></thead><tbody>'
   '<tr><td>電腦軟體授權使用及 IBM z/OS 暨子系統程式技術支援</td><td>約 3.0–3.5 億 / 年</td><td class="dom">未經公開評選</td></tr>'
   '<tr><td>IBM 主機及週邊設備硬軟體維護服務</td><td>約 6,000 萬 / 年</td><td class="dom">未經公開評選</td></tr>'
   '<tr><td>資金運用管理系統應用軟體增修暨維護</td><td>約 1,500 萬 / 年</td><td class="dom">未經公開評選</td></tr>'
   '<tr class="total"><td>2015 一次性：汰換及擴充雙中心 IBM 大型主機設備</td><td>2.53 億</td><td>未經公開評選</td></tr>'
   '</tbody></table>'
   '<p class="flag-note"><b>說明：</b>核心金融系統建置於 IBM z/OS 主機，後續授權、技術支援與硬體維護多須由原廠承作，形成每年約 3.6 億、九年累計約 33.8 億的單一來源採購。z/OS 為原廠專屬技術，此處限制性招標有合法事由；本例呈現的是建置選擇所帶來的長期轉換成本，而非違法。若核心系統採開放標準或可攜架構，後續採購較有空間引入競爭。</p></div>')
 + sec(5,"limits","限制","限制",None,
   '<ul class="gaps rv">'
   '<li><b>訊號非弊端。</b>未經公開評選、長年配對均有合法事由（採購法 §22）；個案是否適當，需另查投標家數等本資料未含的欄位。</li>'
   '<li><b>跨年趨勢僅就用字一致的欄位。</b>各年收錄密度不一，故趨勢限於「未經公開評選」此一標籤，並條件化於公告金額以上母體；不宜外推為絕對件數變化。</li>'
   '<li><b>配對以名稱聚合。</b>同一廠商的中英文或分公司寫法可能分散；本文已就主要配對人工核對，細部統計仍以統一編號歸戶為宜。</li>'
   '</ul>')
 + sec(6,"sources","資料來源","資料來源",None, sources(
   '<div class="src"><span class="src-k">姊妹研究</span>本文為「政府資訊採購的市場結構」專題之面向一，與導讀及其他三篇分論共用母體與用語界線。</div>')))
page("lock-in/index.html",
  "資訊採購中的供應商鎖定：無競爭採購與長年配對",
  "以限制性招標（未經公開評選）比率與機關—廠商長年配對，檢視政府資訊採購中的供應商延續承作。公告金額以上資訊採購約五分之一未經公開競爭，並呈緩升。",
  "../","lock-in", d_hero, d_toc, d_body,
  "<b>資訊採購中的供應商鎖定</b>（面向一 / 共四篇）")
print("✓ lock-in/index.html")

# ════════════════════════════════════════════════════════════════════
# 篇 3 · 地理集中（B）
# ════════════════════════════════════════════════════════════════════
b_hero=hero(
  "政府資訊採購市場結構 · 面向二",
  "資訊採購的地理集中：得標廠商的縣市分布",
  "由得標廠商的登記地址解析縣市，檢視政府資訊採購在供給端的地理分布，以及非台北機關的採購流向。",
  "在此資料範圍內，台北市登記廠商取得資訊類決標金額約七成。即使買方機關不在台北，其資訊支出仍有約七成金額由台北廠商承作，且台北廠商承作的平均單案金額明顯較在地廠商為高，顯示規模較大的標案多由台北廠商承作。須說明，廠商登記地非履約地，大型廠商總部多設於台北。",
  [("台北廠商 · 金額","70.3<span class='unit'>%</span>","資訊類決標金額由台北市登記廠商取得（可解析子集）"),
   ("北北合計 · 金額","83.9<span class='unit'>%</span>","台北＋新北登記廠商取得之金額佔比"),
   ("非台北機關 · 外流","71.8<span class='unit'>%</span>","非台北機關之資訊支出，由台北廠商承作之金額比")],
  "資料：政府電子採購網 · 廠商縣市由登記地址解析 · 登記地非履約地")
b_toc=toc([("method","方法"),("share","廠商縣市分布"),("flow","非台北機關的流向"),("limits","限制"),("sources","資料來源")])
b_body=(
 sec(1,"method","方法","方法：由登記地址解析廠商縣市","政府採購資料含廠商與機關地址，可比較供需兩端的地理分布。",
   '<div class="prose rv">'
   '<p>本文由得標廠商的登記地址解析其所在縣市，計算資訊類決標的件數與金額在各縣市的分布；並以機關地址判定買方所在縣市，進一步觀察「非台北機關」的採購流向。可解析的地址佔多數，少數格式不一者列為無法解析，不影響整體分布。</p>'
   '<p>須先說明一項界線：<b>廠商登記地非履約地</b>。大型資訊廠商總部多設於台北，登記於台北不等於工作於台北。因此本文的陳述限於「得標廠商登記地之集中」，不外推為人力或履約地之集中。</p>'
   '</div>')
 + sec(2,"share","廠商縣市分布","得標廠商集中於台北，且金額較件數更集中",None,
   '<div class="find rv"><div class="find-top"><span class="find-no">發現一</span><h3>台北市登記廠商取得資訊類決標金額約七成</h3></div>'
   '<div class="block" style="margin-top:6px"><div class="cap">資訊類決標之得標廠商登記縣市（可解析子集）</div><div class="spectrum">'
   '<div class="sp-row rv"><div class="sp-name">臺北市（金額）</div><div class="sp-track"><div class="sp-fill" style="width:70.3%"></div></div><div class="sp-val"><b>70.3%</b>金額</div></div>'
   '<div class="sp-row rv"><div class="sp-name">臺北市（件數）</div><div class="sp-track"><div class="sp-fill alt" style="width:53.8%"></div></div><div class="sp-val"><b>53.8%</b>件數</div></div>'
   '<div class="sp-row rv"><div class="sp-name">臺北＋新北（金額）</div><div class="sp-track"><div class="sp-fill" style="width:83.9%"></div></div><div class="sp-val"><b>83.9%</b>金額</div></div>'
   '</div></div>'
   '<div class="find-key"><span class="kl">說明</span>台北市登記廠商取得的件數逾半、金額約七成；金額佔比高於件數佔比，顯示規模較大的標案更集中。此為可解析子集的下界——少數登記於非台北的大額為被誤含的非資訊類工程，移除後台北佔比將略升。</div>'
   '<div class="block"><div class="cap">得標廠商登記縣市（前 7，可解析子集）</div>'
   '<table class="verify"><thead><tr><th>廠商登記縣市</th><th>件數</th><th>金額佔比</th></tr></thead><tbody>'
   '<tr><td class="vid">臺北市</td><td>6,865</td><td>70.3%</td></tr>'
   '<tr><td class="vid">新北市</td><td>2,205</td><td>13.5%</td></tr>'
   '<tr><td class="vid">臺中市</td><td>1,050</td><td>4.3%</td></tr>'
   '<tr><td class="vid">高雄市</td><td>947</td><td>3.6%</td></tr>'
   '<tr><td class="vid">桃園市</td><td>437</td><td>1.9%</td></tr>'
   '<tr><td class="vid">新竹縣</td><td>304</td><td>1.8%</td></tr>'
   '<tr><td class="vid">臺南市</td><td>344</td><td>0.8%</td></tr>'
   '</tbody></table>'
   '<div class="cap" style="margin-top:14px">金額佔比為占可解析縣市總額之比例；其餘縣市合計約 3.8%。</div></div></div>')
 + sec(3,"flow","非台北機關的流向","非台北機關的資訊支出，多數金額由台北廠商承作",None,
   '<div class="find rv"><div class="find-top"><span class="find-no">發現二</span><h3>規模較大的標案，多由台北廠商承作</h3></div>'
   '<div class="find-sum"><p>僅就<b>買方機關不在台北</b>的資訊類決標而言，由台北廠商承作者佔<b>件數 37.5%、金額 71.8%</b>。台北廠商承作這些案件的平均單案金額約 <b>3,340 萬</b>，在地廠商（如臺中約 530 萬、高雄約 760 萬）則明顯較低。</p></div>'
   '<div class="find-key"><span class="kl">判讀</span>件數上，非台北機關仍有相當比例由在地廠商承作；金額上則多數流向台北廠商。兩者並列指向：<b>小型標案傾向在地承作，規模較大的標案則多由台北廠商承作</b>。在公開資料範圍內，這呈現資訊服務供給能量在地理上的不均；地方機關進行較大規模的資訊建置時，多須向台北廠商採購。</div>'
   '<div class="prose rv" style="margin-top:28px"><p>對照之下，<b>買方機關遍布全台</b>——各縣市政府、鄉鎮機關、地方學校醫院皆有資訊採購，買方端的地理分布遠較賣方端分散。供需兩端的落差，即是「數位城鄉」的具體樣態：需求在各地，供給能量集中於首都。</p></div>'
   '<div class="find-key rv" style="margin-top:24px"><span class="kl">一個具體例子</span>臺東縣境內機關的資訊類決標，金額約 <b>72% 由台北廠商承作</b>（約 2,650 萬）；在地臺東廠商雖得標 7 件，金額僅約 395 萬。比例與全國型態一致：在地廠商承接零星小案，較大的標案由台北廠商承作。</div></div>')
 + sec(4,"limits","限制","限制",None,
   '<ul class="gaps rv">'
   '<li><b>登記地非履約地。</b>本文陳述限於得標廠商登記縣市之集中，不外推為人力或履約地集中；大型廠商總部多設台北。</li>'
   '<li><b>金額受非資訊類影響。</b>少數登記於非台北的大額為被「系統」一詞誤含的工程／環保案；其方向使台北佔比偏低，故文中七成為保守下界。</li>'
   '<li><b>地址解析有少數無法判讀。</b>格式不一者列為無法解析，未計入縣市分布；其比例不影響整體結論。</li>'
   '</ul>')
 + sec(5,"sources","資料來源","資料來源",None, sources(
   '<div class="src"><span class="src-k">姊妹研究</span>本文為「政府資訊採購的市場結構」專題之面向二，與導讀及其他三篇分論共用母體與用語界線。</div>')))
page("geography/index.html",
  "資訊採購的地理集中：得標廠商的縣市分布",
  "由廠商登記地址解析縣市，檢視政府資訊採購的地理分布。台北市登記廠商取得資訊類決標金額約七成；非台北機關的資訊支出亦多數金額由台北廠商承作。",
  "../","geography", b_hero, b_toc, b_body,
  "<b>資訊採購的地理集中</b>（面向二 / 共四篇）")
print("✓ geography/index.html")

# ════════════════════════════════════════════════════════════════════
# 篇 4 · 供給端集團組成（A）
# ════════════════════════════════════════════════════════════════════
a_hero=hero(
  "政府資訊採購市場結構 · 面向三",
  "資訊採購的供給端組成：以董監事資料還原控制集團",
  "帳面上有數千家廠商承作政府資訊採購。本文以商工登記董監事資料，將廠商還原至實際控制集團，檢視市場集中度是否被子公司的不同命名所低估。",
  "以公司董監事「所代表法人」的席次還原控制集團後，部分看似獨立的中型廠商實為集團子公司，市場集中度較帳面為高。但即使完全還原，前 14 大集團合計亦僅佔件數約 17%、金額約 22%，其餘逾八成件數由四千餘家獨立廠商構成。供給端可描述為「一個規模明顯領先的供應集團＋十餘個集團骨幹＋為數眾多的獨立廠商」的雙層結構；該領先集團為中華電信集團，其最大股東為交通部。",
  [("還原 14 大集團","17.3<span class='unit'>%</span>","還原控制集團後，前 14 大集團合計件數佔比（金額 22.2%）"),
   ("獨立廠商","4,424<span class='unit'>家</span>","其餘約 82.9% 件數由獨立廠商承作"),
   ("最大供應集團","中華電信系","件數 5.3% / 金額 8.5%，明顯領先；交通部為最大股東")],
  "資料：商工登記董監事所代表法人席次（經濟部商業發展署／g0v／歐噴整理）")
a_toc=toc([("method","方法"),("rollup","集團還原"),("largest","最大供應集團"),("reading","如何判讀集中度"),("foundation","法人承包"),("limits","限制"),("sources","資料來源")])
a_body=(
 sec(1,"method","方法","方法：以董監事「所代表法人」還原控制關係","公司名稱無法看出隸屬；董事會席次的法人代表可較客觀地判定控制關係。",
   '<div class="prose rv">'
   '<p>台灣資訊服務廠商常以不同名稱的子公司分別承作標案，僅看名稱難以判斷是否同屬一集團，且名稱相近不必然同集團。本文採用商工登記的公司董監事資料：每位董事、監察人若由法人指派，其「所代表法人」即顯示於登記中。當某一法人在某公司董事會占有多數或關鍵席次，即可判定其控制關係。例如資拓宏宇董事會 10 席中，中華電信占 5 席。</p>'
   '<p>除逐家查核外，本文亦以「某法人在哪些公司占有董監席位」的反向查詢，找出以不同名稱承作的集團成員，再與廠商名單比對。此法同時排除名稱相近但無控制關係者（例如凌網、凌誠與凌群並無母子關係；華電聯網與中華電信並無持股關係）。</p>'
   '</div>'
   '<div class="find-key rv" style="margin-top:30px"><span class="kl">怎麼讀董事會</span>以資拓宏宇為例：其董事會 10 席中，<b>5 席由中華電信指派的法人代表擔任</b>，即可判定中華電信為控制方——即使公司名稱不含「中華電信」。本研究即以此種「法人占席」關係，將不同名稱的子公司歸戶至同一集團。</div>')
 + sec(2,"rollup","集團還原","還原控制集團後，集中度較帳面為高",None,
   '<div class="schema rv"><div class="schema-h">集團還原（董監事席次為據）</div><div class="schema-sub">帳面件數 → 還原控制集團後件數 · 商工登記董監事所代表法人</div>'
   '<div class="schema-row"><div class="schema-code">405 → 707</div><div class="schema-name">中華電信系 <span style="color:var(--role-emphasis)">+75%</span></div><div class="schema-def">含資拓宏宇（中華電信占董事會 <b>5/10 席</b>）、中華系統整合（<b>6/6 席</b>）、中華資安國際（3/7 席）、是方電訊。</div></div>'
   '<div class="schema-row"><div class="schema-code">98 → 215</div><div class="schema-name">宏碁系 <span style="color:var(--role-emphasis)">+119%</span></div><div class="schema-def">含安碁資訊（宏碁占 3/7 席）、宏碁雲架構（安碁占 4/4 席）。資安子公司之名稱不顯示其隸屬。</div></div>'
   '<div class="schema-row"><div class="schema-code">235 → 394</div><div class="schema-name">精誠系 <span style="color:var(--role-emphasis)">+68%</span></div><div class="schema-def">含康和資訊（精誠占 4/4 席）、泰鋒電腦、藍新資訊。另：駿永屬驊宏資通、國眾屬大眾投控、三商電腦屬三商投控，名稱均不顯示其隸屬。</div></div>'
   '<div class="schema-foot"><b>但長尾為實：</b>即使完全還原，前 14 大集團合計亦僅佔 <b>17.3% 件數 / 22.2% 金額</b>，其餘 <b>82.9% 件數由 4,424 家獨立廠商</b>承作（平均 2.5 件／家）。前 4 大集團合計約 11%、前 8 大約 14%（件數），尚不構成由少數集團把持的全國市場。</div></div>'
   '<div class="block rv"><div class="cap">還原控制集團後 · 前 14 大集團（資訊類決標，2015–2026）</div>'
   '<table class="verify"><thead><tr><th>集團</th><th>件數</th><th>金額</th><th>含括實體（例）</th></tr></thead><tbody>'
   '<tr><td class="vid">中華電信系</td><td>707</td><td>321 億</td><td>中華電信、資拓宏宇、中華系統整合、中華資安</td></tr>'
   '<tr><td class="vid">精誠系</td><td>394</td><td>77 億</td><td>精誠資訊、科技整合、軟體服務、康和資訊</td></tr>'
   '<tr><td class="vid">宏碁系</td><td>215</td><td>54 億</td><td>宏碁資訊、安碁資訊、宏碁雲架構</td></tr>'
   '<tr><td class="vid">叡揚資訊</td><td>149</td><td>21 億</td><td>（獨立）</td></tr>'
   '<tr><td class="vid">凌群電腦</td><td>122</td><td>41 億</td><td>（獨立）</td></tr>'
   '<tr><td class="vid">聯華神通系</td><td>108</td><td>34 億</td><td>神通資訊、資通電腦</td></tr>'
   '<tr><td class="vid">關貿網路</td><td>102</td><td>15 億</td><td>（財政部官股）</td></tr>'
   '<tr><td class="vid">工研院</td><td>91</td><td>35 億</td><td>（政府捐助法人）</td></tr>'
   '<tr><td class="vid">敦陽系</td><td>86</td><td>15 億</td><td>敦陽科技、敦陽資訊</td></tr>'
   '<tr><td class="vid">大眾投控</td><td>81</td><td>24 億</td><td>國眾電腦</td></tr>'
   '<tr><td class="vid">遠傳系</td><td>79</td><td>58 億</td><td>遠傳系統整合、數聯資安</td></tr>'
   '<tr><td class="vid">資策會</td><td>70</td><td>34 億</td><td>（政府捐助法人）</td></tr>'
   '<tr><td class="vid">三商投控</td><td>68</td><td>110 億</td><td>三商電腦（含大型主機）</td></tr>'
   '<tr><td class="vid">驊宏資通</td><td>40</td><td>3.5 億</td><td>駿永資訊</td></tr>'
   '</tbody></table>'
   '<div class="cap" style="margin-top:14px">其餘 11,060 件（約 83% 件數）由約 4,424 家獨立廠商承作；金額型集中度高於件數，反映大型標案更集中。</div></div>'
   '<div class="prose rv" style="margin-top:30px"><p>以帳面廠商家數衡量競爭，會因子公司分別命名而低估集中度（中華電信系由 405 件增為 707 件、宏碁系由 98 件增為 215 件）。但還原後集中度的提高約為三至四成，市場仍存在為數眾多的獨立廠商；因此較準確的描述是「集中度被部分低估」，而非「市場由少數集團隱藏式把持」。</p></div>')
 + sec(3,"largest","最大供應集團","規模明顯領先的供應集團為中華電信集團",None,
   '<div class="find rv"><div class="find-top"><span class="find-no">發現</span><h3>最大的單一供應集團，最大股東為交通部</h3></div>'
   '<div class="find-sum"><p>還原後，中華電信集團為規模明顯領先的供應集團，單一集團佔資訊類決標<b>件數 5.3% / 金額 8.5%</b>，居首且與其後集團有明顯差距；而中華電信由<b>交通部為最大股東（董事會 8/13 席）</b>。其承作對象包含多項核心系統——財政部財政資訊中心（約 64 億）、健保署、中華郵政、臺鐵票務、台電、公路監理、航港、氣象等。各機關的單一來源比不一（如公路總局較高、健保署多為公開競爭）。</p></div>'
   '<div class="block"><div class="cap">中華電信系承作的主要機關（資訊類決標）</div>'
   '<table class="verify"><thead><tr><th>機關</th><th>件數</th><th>金額</th><th>承載的系統（例）</th></tr></thead><tbody>'
   '<tr><td class="vid">財政部財政資訊中心</td><td>16</td><td>64 億</td><td>稅務資訊系統</td></tr>'
   '<tr><td class="vid">衛福部中央健保署</td><td>71</td><td>37 億</td><td>健保資訊系統</td></tr>'
   '<tr><td class="vid">中華郵政</td><td>43</td><td>27 億</td><td>郵務／金融資訊</td></tr>'
   '<tr><td class="vid">交通部臺鐵</td><td>15</td><td>20 億</td><td>票務系統維運</td></tr>'
   '<tr><td class="vid">交通部公路總局</td><td>18</td><td>12 億</td><td>公路監理委外</td></tr>'
   '<tr><td class="vid">交通部航港局</td><td>23</td><td>8 億</td><td>航港資訊</td></tr>'
   '</tbody></table></div>'
   '<div class="find-key"><span class="kl">說明</span>政府資訊採購最大的單一供應方，是一個由政府為最大股東的集團，且其承載的多為稅務、健保、郵政、交通等核心系統。各機關的單一來源比不一（如公路總局較高、健保署多為公開競爭）；本文呈現的是供給端的結構事實，不就個案作評價。</div></div>')
 + sec(4,"reading","如何判讀集中度","如何判讀此處的集中度","集中度的高低取決於以哪一層（實體或集團）、哪一維（件數或金額）衡量。",
   '<div class="prose rv">'
   '<p>「政府資訊採購是否被少數廠商寡占」沒有單一答案，取決於衡量方式。以帳面實體、件數衡量，集中度低（前 8 大約 11%）；以還原集團、金額衡量，集中度較高（前 8 大約 19%），且大型標案更集中。兩者並非矛盾，而是反映同一市場的不同切面：商品化的硬體採購分散於眾多廠商，規模較大的系統建置與服務則集中於少數集團。</p>'
   '<p>因此本文的結論是雙層結構：<b>一個規模明顯領先的供應集團、十餘個集團骨幹、以及為數眾多的獨立廠商</b>。競爭限制主要不在「全國市佔」，而在大型標案的集中與機關層級的承作延續（後者見面向一）。</p>'
   '</div>')
 + sec(5,"foundation","法人承包","另一條供給管道：政府捐助法人","除商業廠商外，政府亦將相當部分資訊業務委由自家捐助法人承作。",
   '<div class="prose rv"><p>工業技術研究院（91 案，跨 24 個機關）與資訊工業策進會（70 案，跨 15 個機關）是資訊採購的承作大戶。其主要委託來源為經濟部體系與數位發展部——經濟部工業局（43 案、約 27 億）、數位發展部數位產業署（25 案、約 21 億）、經濟部產業發展署等。</p>'
   '<p>值得一提的是，<b>數位發展部自身</b>金額最大的兩個資訊承作對象，正是資策會與工研院。委由捐助法人承作多以政策性計畫名義進行，未必經一般公開競爭。此處非評價法人是否適任，而是指出：在商業廠商的市場之外，還有一條「委由自家法人」的供給管道，同樣不經開放競爭。對「為何開放競爭、開源或新進廠商不易擴大」而言，這是供給端結構的一部分。</p></div>')
 + sec(6,"limits","限制","限制",None,
   '<ul class="gaps rv">'
   '<li><b>還原僅涵蓋可識別的 14 個最大集團。</b>長尾四千餘家中可能仍有未捕捉的中小型集團，故實際集中度可能再略高；「長尾為實」的量級結論不變。</li>'
   '<li><b>控制關係以董事會法人席次近似。</b>本文以「最大股東＋董事會多數席次」判定控制，非精確持股百分比；持股顯著但未過半者，另以集團聯屬標示而非歸入控制。</li>'
   '<li><b>登記資料非即時。</b>商工登記為登記資料，反映登記時點之董監結構，可能與最新狀況有時間差。</li>'
   '</ul>')
 + sec(7,"sources","資料來源","資料來源",None, sources(
   '<div class="src"><span class="src-k">姊妹研究</span>本文為「政府資訊採購的市場結構」專題之面向三，與導讀及其他三篇分論共用母體與用語界線。</div>')))
page("ownership/index.html",
  "資訊採購的供給端組成：以董監事資料還原控制集團",
  "以商工登記董監事資料還原政府資訊採購廠商的控制集團。子公司分別命名使集中度被部分低估；還原後前 14 大集團佔件數約 17%，最大供應集團為中華電信集團（最大股東為交通部）。",
  "../","ownership", a_hero, a_toc, a_body,
  "<b>資訊採購的供給端組成</b>（面向三 / 共四篇）")
print("✓ ownership/index.html")

# ════════════════════════════════════════════════════════════════════
# 篇 5 · 決標原則（C）
# ════════════════════════════════════════════════════════════════════
c_hero=hero(
  "政府資訊採購市場結構 · 面向四",
  "資訊採購的決標原則：價格標與最有利標的分布",
  "以決標原則（價格標或最有利標）區分標的，檢視「政府資訊採購偏向低價、因而品質不佳」這一常見推論是否成立。",
  "在此資料範圍內，資訊類採購的低價標主要集中於硬體採購（標的商品化，採最低標屬合理），而客製化服務多採比品質的「準用最有利標」。資訊類採用最低標的比例並不高於全政府；最嚴格的「最有利標」則與全政府同樣稀少。因此「資訊採購偏向低價」之說，在資料中不成立；真正值得關注的競爭限制在其他面向（見面向一至三）。",
  [("硬體（財物）· 最低標","82<span class='unit'>%</span>","財物類資訊採購採最低標之比例"),
   ("服務（勞務）· 比品質","54<span class='unit'>%</span>","勞務類採「準用最有利標」（比品質）之比例"),
   ("最有利標","3.3<span class='unit'>%</span>","資訊類採最嚴格之最有利標比例（全政府約 2.9%）")],
  "資料：政府電子採購網 · 決標原則以欄位實際值判讀 · 與全政府基準對照")
c_toc=toc([("method","方法"),("split","標的與決標原則"),("reading","常見推論的對照"),("limits","限制"),("sources","資料來源")])
c_body=(
 sec(1,"method","方法","方法：以標的拆分決標原則，並與全政府對照","決標原則須區分標的，且須與全政府基準比較，方能判讀。",
   '<div class="prose rv">'
   '<p>決標原則（award_way）以欄位實際值判讀，分為比價格的「最低標」與比品質的「最有利標」系（含最有利標、準用最有利標、參考最有利標精神）。判讀「資訊採購是否偏向低價」時，須注意兩點：其一，標的不同，適合的決標原則不同——規格明確的硬體採最低標屬合理，難以價格衡量的客製服務才需比品質；其二，須與全政府基準比較，否則無從判斷資訊類是否「特別」偏向低價。本文因此以「標的 × 決標原則」交叉，並對照全政府同口徑。</p>'
   '</div>')
 + sec(2,"split","標的與決標原則","硬體採最低標、服務比品質，與標的性質一致",None,
   '<div class="chains rv">'
   '<article class="chain A"><div class="chain-top"><div class="chain-tag">財物</div><div class="chain-name">硬體：以最低標為主</div><div class="chain-sub">規格明確、商品化</div></div>'
   '<div class="chain-rows">'
   '<div class="crow"><div class="lbl">最低標</div><div class="val"><b>82%</b>（規格明確，採比價屬合理）</div></div>'
   '<div class="crow"><div class="lbl">最有利標</div><div class="val">6.5%</div></div>'
   '<div class="crow"><div class="lbl">判讀</div><div class="val">硬體商品化，以價格決標與標的性質一致</div></div>'
   '</div></article>'
   '<article class="chain B"><div class="chain-top"><div class="chain-tag">勞務</div><div class="chain-name">服務：以比品質為主</div><div class="chain-sub">客製、難以價格衡量</div></div>'
   '<div class="chain-rows">'
   '<div class="crow"><div class="lbl">準用最有利標（比品質）</div><div class="val"><b>54%</b></div></div>'
   '<div class="crow"><div class="lbl">最低標</div><div class="val">28%</div></div>'
   '<div class="crow"><div class="lbl">判讀</div><div class="val">客製服務多採比品質選商，非一律比價</div></div>'
   '</div></article>'
   '</div>'
   '<div class="find-key rv" style="margin-top:30px"><span class="kl">說明</span>資訊類整體採最低標約 54%（全政府約 58%），並未高於全政府；而最嚴格的「最有利標」資訊類約 3.3%、全政府約 2.9%，同樣稀少。資訊服務的比品質選商，多以限制性招標下的「準用最有利標」進行，而非公開的最有利標。</div>'
   '<div class="block rv"><div class="sub-h">「最有利標」其實有三種，嚴謹度不同</div>'
   '<div class="prose"><p>「比品質」並非單一制度。資訊類的「比品質」多屬<b>準用最有利標</b>，而這幾乎全部發生在<b>限制性招標之內</b>（3,726 件全數為限制性）；真正公開、由評選委員會完整評分的<b>最有利標</b>僅 441 件（3.3%）。換言之，資訊服務的品質選商主要在限縮競爭的程序中進行，而非公開競爭——此與面向一（限制性招標佔比偏高）相互呼應。</p></div>'
   '<table class="verify"><thead><tr><th>決標方式</th><th>件數</th><th>是否在限制性招標內</th><th>均案金額</th></tr></thead><tbody>'
   '<tr><td class="vid">最有利標（公開、最嚴謹）</td><td>441</td><td>否（公開競爭）</td><td>約 1.3 億</td></tr>'
   '<tr><td class="vid">準用最有利標</td><td>3,726</td><td class="ok">是（100%）</td><td>約 3,700 萬</td></tr>'
   '<tr><td class="vid">參考最有利標精神</td><td>1,945</td><td>否（多為小額）</td><td>約 57 萬</td></tr>'
   '<tr><td class="vid">最低標</td><td>7,225</td><td>部分（約 22%）</td><td>約 2,500 萬</td></tr>'
   '</tbody></table>'
   '<div class="cap" style="margin-top:14px">最嚴謹的公開最有利標案件雖少，但平均金額最大（約 1.3 億）；準用最有利標次之（約 3,700 萬）。</div></div>')
 + sec(3,"reading","常見推論的對照","常見推論與資料的對照",None,
   '<table class="verify rv"><thead><tr><th style="width:230px">常見推論</th><th>資料中的對照</th><th style="width:96px">判定</th></tr></thead><tbody>'
   '<tr><td class="vid">資訊採購偏向低價，<br>因而品質不佳</td><td>低價標集中於商品化的硬體（財物類 82% 最低標，屬合理）；客製服務多採比品質（勞務類準用最有利標 54%）。資訊類採最低標之比例並不高於全政府。</td><td class="upd">不成立</td></tr>'
   '<tr><td class="vid">資訊採購已普遍<br>採用最有利標</td><td>最嚴格的最有利標僅佔 3.3%，與全政府 2.9% 同樣稀少；比品質多在限制性招標內進行（準用最有利標）。</td><td class="ok">部分為實</td></tr>'
   '</tbody></table>'
   '<div class="prose rv" style="margin-top:30px"><p>就「偏向低價」一說而言，資料不支持。決標原則的分布主要反映標的性質：硬體比價、服務比品質。需補充的一點是，資訊服務的「比品質」多發生於限制性招標之內（準用最有利標），而非公開的最有利標——此一現象與面向一（限制性招標佔比偏高）相互呼應。換言之，資訊採購較值得關注的結構限制在競爭開放程度與供給端集中，而非決標價格。</p></div>')
 + sec(4,"limits","限制","限制",None,
   '<ul class="gaps rv">'
   '<li><b>決標原則不等於最終品質。</b>本文比較的是決標方式的分布，不直接衡量交付系統的品質；「比品質選商」不保證結果良好，「比價」亦非必然品質差。</li>'
   '<li><b>標的分類以欄位為準。</b>財物／勞務依採購公告標的別，個案可能混合（如含建置與維護）；分類為近似。</li>'
   '<li><b>金額分布另受非資訊類影響。</b>本文以件數比例為主；涉及金額時，已就非資訊類污染另作清洗（見導讀）。</li>'
   '</ul>')
 + sec(5,"sources","資料來源","資料來源",None, sources(
   '<div class="src"><span class="src-k">姊妹研究</span>本文為「政府資訊採購的市場結構」專題之面向四，與導讀及其他三篇分論共用母體與用語界線。</div>')))
page("award-method/index.html",
  "資訊採購的決標原則：價格標與最有利標的分布",
  "以決標原則區分標的，檢視「政府資訊採購偏向低價」一說。低價標集中於商品化硬體，客製服務多採比品質；資訊類採最低標比例不高於全政府，此說不成立。",
  "../","award-method", c_hero, c_toc, c_body,
  "<b>資訊採購的決標原則</b>（面向四 / 共四篇）")
print("✓ award-method/index.html")

print("\n→ 5 篇已輸出至", OUT)
