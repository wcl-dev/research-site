#!/usr/bin/env python3
"""把 draft.md（v1.0：論點先行）組成 research-site Template B（linear chrome）的 index.html。

skill：~/.claude/skills/generate-research-html（palette: research-default；modules: hero-numbers, find-card, flagship-table,
verify-table, gaps-list）。三張圖（分工結構、persona 個人檔案卡、追蹤類別長條）與附錄的摺疊／篩選是 skill 沒有的模組，
在本檔自寫 CSS/JS/SVG，顏色全走 tokens。表格由資料檔生成。
"""
from pathlib import Path
import csv, re, html, yaml
from openpyxl import load_workbook

SK = Path.home() / '.claude/skills/generate-research-html'
HERE = Path(__file__).resolve().parent
CASE = HERE.parent
OUT = HERE / 'index.html'

def read(p): return Path(p).read_text(encoding='utf-8')
def css_of_module(name):
    t = read(SK / 'templates/template-b-sidebar/_modules' / f'{name}.html')
    m = re.search(r'<style>(.*?)</style>', t, re.S)
    return m.group(1) if m else ''
def e(s): return html.escape(str(s), quote=False)

# ---------------- data ----------------
EXT = {'qsh-alpha':'dsawjk 群','qsh-beta':'picelse／luckyelse 群','qsh-gamma':'picread 群','family-01':'vivi01 影片站群','looker-17':'looker 系群','farm-eatmary':'eatmary 群','ezvivi':'ezvivi 群','farm-enews':'ENews／LIFE 群','farm-twqiang':'twqiang 群','vietnam-adsense':'越南向 AdSense 群','thai-news01-hsupr':'泰國 news01／HSU 群','thai-wdwire':'泰國 wdwire 群','cand-thai-narrative-amplifiers':'東南亞敘事放大器候選群','cand-docilepuppy':'docilepuppy 系候選群','cand-happyshare':'happyshare 候選群','cand-singles':'單站候選群','cand-ptt-network':'ptt 系候選群','cand-tw-cells':'台灣小站候選群','cand-cn-fanwen':'中國範文站候選群','cand-qastack':'qastack 多語候選群','cand-hk-farms':'香港農場候選群','cand-qhd-adstxt':'ads.txt 模板候選群（qhd）','cand-anyelse-net':'anyelse 網候選群','ref-active':'參照群：仍在營運的老牌農場','ref-groups':'參照群：集團名條目'}
reg = yaml.safe_load(read(Path.home() / 'kwara-farm-registry/registry.yaml'))
clusters = {c['id']: c for c in reg['clusters']}
ct = list(csv.DictReader(open(CASE / 'analysis/report_cluster_table.csv', encoding='utf-8')))
wb = load_workbook(Path.home() / 'kwara-farm-registry/evidence/social-accounts-2026-09-03/社群帳號盤點_2026-09-03.xlsx', read_only=True)
rows = list(wb['Threads'].iter_rows(values_only=True)); hdr = [str(c).split('\n')[-1] for c in rows[0]]
ACC = [dict(zip(hdr, r)) for r in rows[1:]]
named = [d for d in ACC if d['behavior_type'] in ('工具化散布', '站方自營')]
def farm_n(d):
    m = re.search(r'農場連結 (\d+) 篇', str(d['role'] or '')); return int(m.group(1)) if m else int(d['evidence_count'] or 0)
named.sort(key=lambda d: (d['behavior_type'] != '站方自營', -farm_n(d)))
def cl_ext(s): return '、'.join(EXT.get(x.strip(), x.strip()) for x in str(s or '').replace('+', ',').split(',') if x.strip())

# ---------------- generated tables ----------------
def flagship_rows():
    out = []
    for r in ct:
        if r['cluster'] == 'ref-groups': continue
        tool = f"{r['tool']}／{r['ded']}／{r['site']}"
        tk = '有' if int(r['tier3_or_toolkeys']) > 0 or r['cluster'] == 'qsh-gamma' else '無'
        per = r['per_post'] if r['per_post'] not in ('', 'nan') else '無互動'
        dom = ' class="dom"' if r['cluster'] in ('qsh-alpha', 'family-01', 'qsh-beta', 'cand-anyelse-net', 'cand-qhd-adstxt') else ''
        out.append(f"<tr><td>{e(EXT[r['cluster']])}</td><td>{r['domains']}</td><td>{int(float(r['l1_posts'])):,}</td><td>{int(r['accounts'])}</td><td{dom}>{tool}</td><td>{tk}</td><td>{per}</td></tr>")
    return '\n'.join(out)
def appendix_a():
    return '\n'.join(f"<details class=\"apx\"><summary><b>{e(EXT[cid])}</b><span class=\"apx-n\">{len(c['domains'])} 域</span></summary><p class=\"apx-doms\">{'、'.join(e(d['name'] if isinstance(d, dict) else d) for d in c['domains'])}</p></details>" for cid, c in clusters.items())
def appendix_b():
    return '\n'.join(f"<tr><td>{e(EXT[cid])}</td><td class=\"mono\">{cid}</td><td>{e(c['label'])}</td><td class=\"r\">{len(c['domains'])}</td></tr>" for cid, c in clusters.items())
def appendix_c():
    return '\n'.join(f"<tr data-type=\"{d['behavior_type']}\"><td class=\"mono\">{e(d['handle'])}</td><td>{d['behavior_type']}</td><td>{e(cl_ext(d['cluster']))}</td><td class=\"r\">{str(d['evidence_tier'])[:1]}</td><td class=\"r\">{farm_n(d)}</td><td class=\"mono small\">{e(str(d['join_keys'] or '')[:40])}</td><td>{e(d['registered'] or '')}</td><td>{e(d['location'] or '')}</td></tr>" for d in named)

# ---------------- figures ----------------
def fig_division():
    """圖一：分工結構圖（SVG，顏色走 tokens；viewBox 留白避免文字溢出）"""
    boxes = [(30, ['工具化帳號'], '201 個', ['農場發的識別碼與分潤碼', '「2 / 2」注入']), (270, ['Threads 搜尋', '與演算法'], '', ['貼文丟給', '不特定的人']), (510, ['站方與專職帳號'], '38 個', ['承接互動', '有人設']), (750, ['路人'], '833 人', ['留言完就走', '回頭 23 人'])]
    s = ['<svg class="fig" viewBox="0 0 1000 300" role="img" aria-label="分工結構圖：工具化帳號種連結，演算法送貼文，站方與專職帳號承接互動，路人留言完就走">']
    for x, title, n, sub in boxes:
        s.append(f'<rect x="{x}" y="50" width="220" height="150" rx="12" class="fg-box"/>')
        for k, line in enumerate(title): s.append(f'<text x="{x+110}" y="{80 + k*20}" class="fg-t" text-anchor="middle">{e(line)}</text>')
        y = 80 + len(title)*20 + 8
        if n: s.append(f'<text x="{x+110}" y="{y+14}" class="fg-n" text-anchor="middle">{e(n)}</text>'); y += 30
        for k, line in enumerate(sub): s.append(f'<text x="{x+110}" y="{y+16 + k*18}" class="fg-s" text-anchor="middle">{e(line)}</text>')
    for x, lab in [(250, '種連結'), (490, '送貼文'), (730, '看到就回')]:
        s.append(f'<line x1="{x}" y1="125" x2="{x+12}" y2="125" class="fg-arrow"/><polygon points="{x+10},119 {x+20},125 {x+10},131" class="fg-head"/><text x="{x+10}" y="112" class="fg-s" text-anchor="middle">{e(lab)}</text>')
    s.append('<path d="M140 200 C 140 262, 620 262, 620 200" class="fg-loop"/><text x="380" y="285" class="fg-s fg-em" text-anchor="middle">帳號之間互相回覆 0 次、引用 1 次：共用的是碼，不是關係</text>')
    s.append('</svg>')
    return ''.join(s)

CATS = ['政治人物／政黨', '政治評論者', '媒體與知識', '藝人與網紅', '品牌與購物', 'Meta 官方']
FOLLOW = {'台灣讀者': [0.63, 0.24, 0.47, 0.32, 0.32, 0.13], '兩極讀者': [0.21, 0.10, 0.30, 0.03, 0.06, 0.03], 'TVB 劇迷': [0.09, 0.03, 0.17, 0.16, 0.14, 0.06], '專職帳號底下的讀者': [0.25, 0.00, 0.25, 0.25, 1.50, 0.25], '流言常客': [0.19, 0.06, 0.31, 0.00, 0.00, 0.19]}
FOLLOW_N = {'台灣讀者': 75, '兩極讀者': 75, 'TVB 劇迷': 75, '專職帳號底下的讀者': 8, '流言常客': 17}
def fig_follow():
    """圖三：五種人追蹤名單類別平均數（分組長條 SVG）"""
    names = list(FOLLOW); W, H, L, B = 920, 360, 40, 100; gw = (W - L - 20) / len(names); bw = gw / 8; mx = 1.6
    s = [f'<svg class="fig" viewBox="0 0 {W} {H}" role="img" aria-label="五種路人每人平均追蹤的帳號類別數">']
    for v in (0.5, 1.0, 1.5):
        y = H - B - v / mx * (H - B - 30); s.append(f'<line x1="{L}" y1="{y:.0f}" x2="{W-20}" y2="{y:.0f}" class="fg-grid"/><text x="{L-8}" y="{y+4:.0f}" class="fg-s" text-anchor="end">{v}</text>')
    s.append(f'<text x="{L}" y="18" class="fg-s">每人平均追蹤的該類帳號數</text>')
    for i, n in enumerate(names):
        x0 = L + i * gw + bw
        for j, v in enumerate(FOLLOW[n]):
            h = v / mx * (H - B - 30); x = x0 + j * bw
            s.append(f'<rect x="{x:.0f}" y="{H-B-h:.0f}" width="{bw-3:.0f}" height="{h:.0f}" class="fg-bar c{j}"><title>{e(n)}・{e(CATS[j])}：{v}</title></rect>')
        s.append(f'<text x="{x0 + 3*bw:.0f}" y="{H-B+22}" class="fg-t2" text-anchor="middle">{e(n)}</text><text x="{x0 + 3*bw:.0f}" y="{H-B+40}" class="fg-s" text-anchor="middle">{FOLLOW_N[n]} 人的平均</text>')
    lg = ''.join(f'<rect x="{L + (j%3)*220}" y="{H-34 + (j//3)*18}" width="12" height="12" class="fg-bar c{j}"/><text x="{L + (j%3)*220 + 18}" y="{H-24 + (j//3)*18}" class="fg-s">{e(CATS[j])}</text>' for j in range(6))
    s.append(lg + '</svg>')
    return ''.join(s)

def bubble(text, src): return f'<div class="bub"><span class="bub-av"></span><div><p>{e(text)}</p><span class="bub-src">{e(src if "，" in src else src + "貼文底下")}</span></div></div>'
def persona_card(n, name, meta, stats, bio, paras, av):
    st = ''.join(f'<div class="pstat"><b>{b}</b><span>{s}</span></div>' for b, s in stats)
    return f'''<article class="pcard rv"><div class="pc-head"><div class="pc-av {av}"></div><div><div class="pc-name">{n}、{name}</div><div class="pc-meta">{meta}</div></div></div><p class="pc-bio">{bio}</p><div class="pstats">{st}</div>{paras}</article>'''

PERSONAS = '\n'.join([
persona_card('一', '被題材帶走的台灣讀者', '在一般使用者偶發轉貼的貼文底下留言 · 隨機 75 人', [('51／75', '自述位於台灣'), ('64', '追蹤名單中位數'), ('0.63', '每人追蹤的政治人物數'), ('5／318', '提到來源的留言')],
 '這類讀者在一般使用者偶發轉貼的貼文底下留言。隨機抽取的 75 人中，有 51 人自述位於台灣，另有 6 人自述位於香港；其中 35 人在 2024 年註冊。他們的追蹤名單中位數為 64 個帳號，是五種類型中最長的一組；他們也最熟悉 Threads 的使用方式。他們的追蹤名單平均每人包含 0.63 個政治人物或政黨帳號，最常見的帳號是蔡英文、沈伯洋與賴清德；泛科學和 Netflix 台灣也經常出現在名單中。這類讀者在晚間 18 到 23 時最活躍。他們回應的是事件本身，而不是資訊來源：',
 bubble('太辛苦了，警察工作真的是包山又包海，工作時數過長，完全沒有基本的人權', 'ENews 群') + bubble('什麼？！剛才發現貝納頌也是味全的？！人啊！有什麼新發現真的要多發文 能救一個是一個！起碼救到我了！', 'eatmary 群') + bubble('只要我有錢 or 有勢力 or 倚老賣老 或者是藍白的大樁腳 只要我想…沒有什麼不可以！！', 'ENews 群') + '<p class="pc-note">少數讀者會注意資訊來源，但這類留言在該層 318 則留言中只有 5 則：</p>' + bubble('這新聞不是好幾年前的事了嗎？', 'looker 系群') + bubble('現在知識的定義已經變成 AI 引用維基百科然後說內容農場是新聞的時代了嗎', '參照群'), 'av1'),
persona_card('二', '中國政治流言的兩極讀者', '在 chinanewscenter 官方帳號底下留言 · 隨機 75 人', [('34／10／9', '自述台灣／香港／中國'), ('20', '追蹤名單中位數'), ('9／75', '2026 年才註冊'), ('3.4%', '質疑真偽的留言')],
 '這類讀者在 chinanewscenter 官方帳號底下留言，也是「農場官方帳號」這一層的主體。隨機抽取的 75 人中，有 34 人自述位於台灣、10 人自述位於香港、9 人自述位於中國、4 人自述位於美國；這一類型的所在地分布在五種類型中最為分散。其中有 9 人到 2026 年才註冊。他們的追蹤名單中位數只有 20 個帳號，許多人的追蹤名單只包含 Threads 預設推薦的 Meta 官方帳號。隨機樣本最常追蹤的帳號是 Team Trump、蔣萬安與國民黨。我們另外刻意挑選了留言較長的活躍留言者，而這組對照樣本最常追蹤的帳號是苗博雅與明居正。政治光譜兩端的讀者會在同一個留言區中彼此對話：',
 bubble('習近平主席是對的，必須抓張', '單站候選群') + bubble('停止改革開放，中共政權必死無疑', '單站候選群') + bubble('习在中国地位穩如泰山，請勿造謠。', '單站候選群') + '<p class="pc-note">在四層留言者中，這一層質疑資訊真偽的留言比例最高，但這些讀者質疑的是內容本身，而不是資訊來源：</p>' + bubble('李克強女兒不可能做這種無腦的事情來自取絕路的。造謠首先要能在邏輯上說的通。', '單站候選群') + bubble('很好奇那些相信这种讯息的都是一些什么人？', '單站候選群') + bubble('这是真的吗 meta.ai', '單站候選群') + '<p class="pc-note">最後一則留言是一名路人直接詢問 Meta 的 AI 這是不是真的，Meta AI 也確實回覆了。</p>', 'av2'),
persona_card('三', 'TVB 劇迷', '在工具化帳號底下留言 · 隨機 75 人', [('37／75', '自述位於香港'), ('46／75', '2024 年註冊'), ('20', '追蹤名單中位數'), ('0', '追蹤的政治人物')],
 '這類讀者在工具化帳號底下留言。隨機抽取的 75 人中，有 37 人自述位於香港，另有 22 人自述位於台灣；其中 46 人在 2024 年註冊。他們的追蹤名單中位數為 20 個帳號，名單中常見古天樂、李施嬅與朱晨麗等香港藝人，沒有政治人物。這類讀者有四分之一的留言只有表情符號，包含文字的留言則使用粵語：',
 bubble('「創世紀」葉孝勤 × 李碧珍呢螢幕夫妻，演活得精彩，令人印象留下深刻。粵語片年代至今都是名星世一，永遠懷念。雪妮姨＋驄叔 安心上路🌹 家人保重🙏', 'vivi01 影片站群') + bubble('吓，咁就瓜咗 因為個位置俾阿黃宗澤取代啊？', 'vivi01 影片站群') + bubble('南無阿彌陀佛，祝早日康復🙏🙏🙏', 'vivi01 影片站群') + '<p class="pc-note">工具化帳號透過分潤碼張貼 TVB 藝人新聞後，在 Threads 上觸及的主要是香港讀者，而不是台灣讀者。同一層中，少數來自台灣的留言出現在 dsawjk 群的山老鼠盜伐貼文底下：</p>' + bubble('殺人都不會判死刑了，何況只是當山老鼠', 'dsawjk 群') + bubble('當見證台灣歷史的生命只是變成一塊塊磚頭擺在案頭，那一份沉默台灣人承擔的起嗎？', 'dsawjk 群'), 'av3'),
persona_card('四', '專職轉貼帳號底下幾乎沒有讀者', '在專職轉貼帳號底下留言 · 留下華語文字的只有 8 人', [('288', '專職帳號的貼文'), ('19', '收到留言的貼文'), ('83／102', '一個巴西帳號底下的葡萄牙文'), ('8', '華語留言者')],
 '在專職轉貼帳號底下留言的人非常少。專職轉貼帳號發布的 288 篇貼文中，只有 19 篇收到留言；全部 102 則留言中，有 83 則是同一個巴西帳號（該帳號推廣面向巴西的農場網域，屬專職轉貼，依本文規則不具名）收到的葡萄牙文政治留言，與台灣無關。扣除這些留言後，資料中只剩下華語留言 8 則與純表情留言 8 則。這 8 名留下文字的讀者追蹤 7-ELEVEn、蝦皮與熊貓影片帳號，沒有追蹤政治人物。他們回應的是貼文內容，不是轉貼者：',
 bubble('這張照片的四妹好Q,好可愛😍❤️❤️❤️', 'vivi01 影片站群') + bubble('希望他身體健康平安快樂', 'vivi01 影片站群') + bubble('連結錯了？', 'anyelse 網候選群') + bubble('謝謝分享', 'anyelse 網候選群') + bubble('👍👍👍👍', 'vivi01 影片站群') + '<p class="pc-note">專職轉貼帳號雖然長期推送單一農場的內容，在 Threads 上卻幾乎得不到回應。這些帳號的功能，是在站方帳號之外增加一個散布出口，而不是經營受眾。</p>', 'av4'),
persona_card('五', '中國政治流言的常客', '回覆兩篇以上的 17 人 · 全部納入', [('12／17', '在 chinanewscenter 底下'), ('36', '追蹤者中位數'), ('0', '追蹤自己留言的農場帳號'), ('12', '單人最多回覆篇數')],
 '這類讀者是曾回覆兩篇以上貼文的 17 人。其中有 12 人只在 chinanewscenter 底下留言，另外 5 人則分別固定在 TVB 影片站帳號、eatmary 或一般使用者的轉貼底下留言。他們的追蹤者人數中位數為 36 人，其中 10 人的追蹤者不到 50 人；他們的追蹤名單中位數為 20 個帳號。沒有任何人追蹤自己留言的農場帳號。他們自述的所在地包括台灣 7 人、美國 2 人、香港 2 人，以及新加坡、俄羅斯、中國各 1 人。他們分布在政治立場的兩端，同一名留言者可能連續回覆十多篇貼文：',
 bubble('習近平主席是聰明滴，永遠給咱指明方向💖👍', '單站候選群，同一人回了 12 篇') + bubble('不幹掉習畜生就會被習畜生幹掉。', '單站候選群，同一人回了 5 篇') + bubble('老爸被带出会场后不久，儿子破格升副部长。这次升隔了三年算是常规。', '單站候選群') + bubble('這班時間帶如果能改成10點半出發一定爆滿', 'eatmary 群，同一人回了 3 篇') + '<p class="pc-note">現有資料無法判定這 17 人是否為人頭帳號。部分跡象支持人頭帳號的可能性：有些帳號的追蹤者只有個位數，有些在 2025 或 2026 年才註冊，有些只在單一帳號底下出現，也有帳號自述位於美國或俄羅斯，卻密集發表支持習近平的留言。另一些跡象則較接近真人使用行為：留言長短不一，內容包含反問、引用與錯字，顯示這些使用者可能把留言區當成論壇。另外還有 3 人是貼文數上萬的台灣重度使用者，只是剛好在兩篇貼文底下都留下留言。目前唯一能確定的是，這些常客是特定帳號的常客，而不是內容農場的常客。</p>', 'av5'),
])

# ---------------- style ----------------
STYLE = '\n'.join([read(SK / 'shared/brand-tokens.css'), read(SK / 'shared/base.css'), read(SK / 'templates/template-b-sidebar/template.css'),
                   *[css_of_module(m) for m in ('hero-numbers', 'verify-table', 'gaps-list', 'flagship-table')],
'''
.mini-tbl{width:100%; border-collapse:collapse; font-size:15px; margin-top:6px}
.mini-tbl th,.mini-tbl td{border-bottom:1px solid var(--c-rule-soft); padding:12px 12px; text-align:left; vertical-align:top}
.mini-tbl th{font-family:var(--ff-mono); font-size:12px; color:var(--c-ink-faint); letter-spacing:.08em; text-transform:uppercase; font-weight:600; background:var(--c-paper-sink)}
.mini-tbl td.r,.mini-tbl th.r{text-align:right; font-family:var(--ff-mono); font-weight:600}
.mini-tbl .hi{color:var(--role-emphasis); font-weight:700}
.tbl-scroll{overflow-x:auto}
.mono{font-family:var(--ff-mono)} .small{font-size:12.5px}
.lf p{max-width:var(--maxw-prose); font-size:17px; line-height:1.85; color:var(--c-ink-soft); margin-bottom:18px}
.lf p b{color:var(--c-ink)}
.lf ul{max-width:var(--maxw-prose); margin:0 0 22px 22px; color:var(--c-ink-soft); font-size:16.5px; line-height:1.8}
.lf li{margin-bottom:8px}
.lf .sub-h{margin-top:48px}
/* 論點 */
.thesis{max-width:var(--maxw-prose); font-family:var(--ff-display); font-size:clamp(20px,2.6vw,26px); line-height:1.6; color:var(--c-ink); font-weight:600; margin:0 0 26px; padding-left:18px; border-left:5px solid var(--role-emphasis)}
/* 洞察卡（沿用 find-card 但徽章用中文序號） */
.find-no.zh{font-size:15px; letter-spacing:.2em}
.find .so{margin-top:24px; padding:20px 24px; background:var(--c-paper-sink); border-radius:11px; font-size:17px; line-height:1.74}
.find .so .kl{font-family:var(--ff-mono); font-size:13px; letter-spacing:.08em; color:var(--role-emphasis); font-weight:600; display:block; margin-bottom:6px}
.find .find-sum p{margin-bottom:14px}
.find .find-sum p:last-child{margin-bottom:0}
/* figures */
.figwrap{margin:8px 0 40px; padding:22px 22px 14px; background:var(--c-paper-card); border:1px solid var(--c-rule); border-radius:14px; cursor:zoom-in}
@media(min-width:1180px){.figwrap,.flagship{width:var(--maxw-wide); margin-left:calc((var(--maxw-content) - var(--maxw-wide))/2)}}
@media(min-width:1400px){.figwrap,.flagship{width:1240px; margin-left:calc((var(--maxw-content) - 1240px)/2)}}
.figwrap.zoom{position:fixed; inset:0; z-index:300; width:auto; margin:0; border-radius:0; padding:40px 4vw; background:var(--c-paper); display:flex; flex-direction:column; justify-content:center; cursor:zoom-out; overflow:auto}
.figwrap.zoom .fig{max-height:80vh; width:auto; max-width:100%; margin:0 auto}
.figwrap .zoom-hint{font-family:var(--ff-mono); font-size:11.5px; color:var(--c-ink-faint); text-align:right; margin-top:6px}
.figwrap .cap{margin-bottom:12px}
.fig{width:100%; height:auto; display:block; font-family:var(--ff-mono)}
.fg-box{fill:var(--c-paper); stroke:var(--c-rule); stroke-width:1.5}
.fg-t{font-size:15px; font-weight:600; fill:var(--c-ink)}
.fg-t2{font-size:14px; font-weight:600; fill:var(--c-ink)}
.fg-n{font-size:22px; font-weight:700; fill:var(--role-primary)}
.fg-s{font-size:12px; fill:var(--c-ink-soft)}
.fg-em{fill:var(--role-emphasis); font-weight:600}
.fg-arrow{stroke:var(--c-ink-soft); stroke-width:2}
.fg-head{fill:var(--c-ink-soft)}
.fg-loop{fill:none; stroke:var(--role-emphasis); stroke-width:1.5; stroke-dasharray:5 5}
.fg-grid{stroke:var(--c-rule-soft); stroke-width:1}
.fg-bar.c0{fill:var(--role-primary)} .fg-bar.c1{fill:var(--role-emphasis)} .fg-bar.c2{fill:var(--role-method)}
.fg-bar.c3{fill:var(--c-ink-faint)} .fg-bar.c4{fill:var(--c-rule)} .fg-bar.c5{fill:var(--c-watermark)}
/* persona 個人檔案卡 */
.pcard{background:var(--c-paper); border:1px solid var(--c-rule); border-radius:18px; padding:30px 32px; margin-bottom:26px; box-shadow:0 1px 0 var(--c-rule-soft)}
.pc-head{display:flex; gap:18px; align-items:center; margin-bottom:14px}
.pc-av{width:64px; height:64px; border-radius:50%; flex:none; border:2px solid var(--c-paper-sink)}
.av1{background:radial-gradient(circle at 30% 30%, var(--role-primary), var(--c-paper-sink) 70%)}
.av2{background:conic-gradient(var(--role-emphasis) 0 50%, var(--role-primary) 50% 100%)}
.av3{background:repeating-linear-gradient(45deg, var(--role-method) 0 8px, var(--c-paper-sink) 8px 16px)}
.av4{background:radial-gradient(circle, var(--c-paper-sink) 0 30%, var(--role-emphasis) 32% 34%, var(--c-paper-sink) 36%)}
.av5{background:linear-gradient(180deg, var(--c-ink-faint), var(--c-paper-sink))}
.pc-name{font-family:var(--ff-display); font-size:22px; font-weight:700; color:var(--c-ink)}
.pc-meta{font-family:var(--ff-mono); font-size:12.5px; color:var(--c-ink-faint); margin-top:4px; line-height:1.6}
.pc-bio{font-size:16.5px; line-height:1.8; color:var(--c-ink-soft); margin:0 0 18px; max-width:var(--maxw-prose)}
.pstats{display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:0 0 18px}
.pstat{background:var(--c-paper-card); border:1px solid var(--c-rule-soft); border-radius:10px; padding:12px 14px}
.pstat b{display:block; font-family:var(--ff-display); font-size:22px; color:var(--role-primary); line-height:1.1}
.pstat span{font-size:12px; color:var(--c-ink-faint); font-family:var(--ff-mono)}
.bub{display:flex; gap:12px; margin:0 0 12px; align-items:flex-start}
.bub-av{width:28px; height:28px; border-radius:50%; background:var(--c-paper-sink); border:1px solid var(--c-rule); flex:none; margin-top:4px}
.bub>div{background:var(--c-paper-card); border:1px solid var(--c-rule-soft); border-radius:4px 16px 16px 16px; padding:12px 16px; max-width:640px}
.bub p{margin:0; font-size:15.5px; line-height:1.72; color:var(--c-ink)}
.bub-src{display:block; margin-top:6px; font-family:var(--ff-mono); font-size:11.5px; color:var(--c-ink-faint)}
.pc-note{font-size:15px; color:var(--c-ink-soft); margin:16px 0 10px}
@media(max-width:600px){.pcard{padding:22px 18px} .pstats{grid-template-columns:repeat(2,1fr)} .bub>div{max-width:100%}}
/* appendix */
.apx{border:1px solid var(--c-rule); border-radius:10px; background:var(--c-paper-card); margin-bottom:10px; padding:0 18px}
.apx summary{cursor:pointer; padding:14px 0; display:flex; justify-content:space-between; align-items:center; font-size:16px}
.apx .apx-n{font-family:var(--ff-mono); font-size:12.5px; color:var(--c-ink-faint)}
.apx-doms{font-family:var(--ff-mono); font-size:13px; line-height:1.9; color:var(--c-ink-soft); padding:0 0 16px; word-break:break-all}
.filter{display:flex; gap:10px; flex-wrap:wrap; margin:0 0 14px}
.filter input,.filter select{font-family:var(--ff-mono); font-size:14px; padding:9px 12px; border:1px solid var(--c-rule); background:var(--c-paper); color:var(--c-ink); border-radius:6px}
.filter input{flex:1; min-width:220px}
.filter .cnt{font-family:var(--ff-mono); font-size:13px; color:var(--c-ink-faint); align-self:center}
.src-grid{display:grid; grid-template-columns:1fr 1fr; gap:0 36px}
.src{padding:16px 0; border-bottom:1px solid var(--c-rule); font-size:15px; line-height:1.62; display:flex; gap:14px}
.src .sid{font-family:var(--ff-mono); font-size:12px; color:var(--role-emphasis); flex:none; font-weight:600; padding-top:3px; width:30px}
.src .sx b{font-weight:700; color:var(--c-ink)}
@media(max-width:1040px){.src-grid{grid-template-columns:1fr}}
'''])

SECTIONS = [('insights','01','三個洞察'),('persona','02','五種路人'),('farms','03','25 個群'),('method','04','我們怎麼知道的'),('appendix','05','附錄'),('sources','06','資料來源')]
TOC = '\n'.join(f'<a href="#{i}"><span class="ix">§{n}</span>{t}</a>' for i, n, t in SECTIONS)
def sec(i, n, t, lead, body):
    return f'''<section id="{i}" data-num="{n}" data-name="{t}"><div class="wrap"><header class="sec-head rv"><span class="sec-num">{n}</span><h2 class="sec-title">{t}</h2>{f'<p class="sec-lead">{lead}</p>' if lead else ''}</header>{body}</div></section>'''
def insight(zh, h, prose, so):
    return f'''<article class="find rv"><div class="find-top"><span class="find-no zh">{zh}</span><h3>{h}</h3></div><div class="find-sum">{prose}</div><div class="so"><span class="kl">因此</span>{so}</div></article>'''

# ---------------- content ----------------
insights = f'''<div class="lf"><p>內容農場的連結在 Threads 上到處出現，但張貼這些連結的帳號不是一群互相配合的人。農場會給分享者一組分潤碼，也就是放在連結裡、用來記錄分享者的代碼；誰的連結帶著這組碼，收益就算給誰。這些帳號各自貼文，彼此幾乎不互動。貼文會被誰看到，由演算法決定；看到的人留完言就離開，也幾乎沒有人追問文章來自哪裡。</p><p>我們反向搜尋了 25 個農場群與 340 個網域在 Threads 上的紀錄，找到 1,520 個帳號，並核實其中 296 個帳號的完整發文史。我們也完整擷取 1,106 篇有互動的農場貼文留言區，再從 833 個留言者中隨機抽取 250 人，分析這些留言者的身分輪廓。以下三項發現是這批資料最能支持的結論。</p></div>
<div class="figwrap rv" data-zoom><div class="cap">圖一 · 分工結構：分享者拿農場的分潤碼貼連結，演算法決定誰看到，路人留言後即離開</div>{fig_division()}<div class="zoom-hint">點圖放大</div></div>
{insight('一', '農場的帳本是分潤碼，不是帳號',
 '<p>picelse／luckyelse 群的連結尾端帶有分潤參數 <span class="mono">utm_term=</span>，參數中的數字是這家農場分潤系統所使用的分享者編號。只要連結帶有某個編號，系統就會把收益計入該名分享者。其中，<span class="mono">utm_term=1883</span> 這個編號串起 10 個帳號，當中有 7 個帳號以「某平台名加 news747」命名：girlsnews747、youtubenews747、tiktoknews747、phpnews747、chinesenews747、fararrinews747、fbnews747。這 7 個帳號共用同一個分享者編號與同一種命名方式，也都在 2024 年 7 到 11 月間註冊，並推送同一家農場的內容。這些跡象顯示，<b>它們不是七名各自運作的使用者，而是同一個分潤帳戶的七個出口。</b></p><p>相同模式也出現在其他群。同一家農場的另一個分享者編號 <span class="mono">utm_term=8842</span>，串起 8 個自述位於馬來西亞的帳號。dsawjk 群提供的分享工具，會在連結尾端加上「<span class="mono">#threads</span> 加數字」的識別碼；我們共發現 65 組識別碼，每個識別碼對應一個帳號，並且跨網域沿用。另有兩個群原本只因共用頁面模板而被列為候選群；這兩個群的貼文帶有同一套識別碼，因而證實其散布行為使用同一項工具。分潤碼也會跨群使用：ericcheww 和 shixiaoqi6554 這兩個帳號，同時張貼 picelse／luckyelse 群帶有 <span class="mono">utm_term=8427</span> 的連結，以及 picread 群帶有自身分潤參數 <span class="mono">uid=12853</span> 的連結；換言之，同一個帳號同時領取兩家農場的分潤。</p><p>這些散布帳號彼此沒有互動關係。在兩批共 13,097 列貼文中，散布帳號彼此回覆 <span class="em">0 次</span>，彼此引用 1 次。這些帳號共用的是工具與代碼，不是社群關係。</p>',
 '監測與處置若以帳號為單位，關閉一個帳號就只是關閉一個出口；<b>若以分潤碼為單位，才是關閉一個帳本。</b>')}
{insight('二', '農場沒有固定受眾，只有觸及',
 '<p>我們擷取了 1,106 篇有互動的農場貼文留言區，並找出共 833 名路人留言者。其中，只有 <span class="em">23 人</span>曾回覆兩篇以上的貼文，只有 9 人曾回覆三篇以上的貼文，也只有 1 人曾跨群留言。在可取得追蹤名單的 232 人中，只有 6 人追蹤任何一個農場帳號。</p><p>就這批資料而言，內容農場在 Threads 上沒有形成固定的粉絲群。演算法把每篇農場貼文分別推送給不同的使用者。一般使用者偶發轉貼的貼文，平均每篇有 1.39 則路人留言；農場官方帳號的貼文，平均每篇有 1.11 則；工具化帳號的貼文，平均每篇有 0.54 則；專職轉貼帳號的貼文，平均每篇有 0.35 則。專職轉貼層共有 102 則留言，其中 83 則是同一個巴西帳號收到的葡萄牙文留言，華語留言只有 8 則。</p><p>這項結果也解釋了散布帳號為何不需要經營人設，也不需要彼此拉抬：農場並未培養自己的受眾，而是由演算法為每篇貼文重新分配受眾。</p>',
 '研究者若以「社群」「粉絲」或「同溫層」的框架理解內容農場，<b>會找錯研究對象。</b>')}
{insight('三', '農場文章進入日常，但少有人把它當成農場內容',
 '<p>在 936 則路人留言中，指出來源或真偽有問題的留言比例如下：農場官方帳號底下為 3.4%，一般使用者轉貼底下為 1.6%，工具化帳號底下為 0.8%，專職轉貼底下為 0。<span class="em">整體比例不到 2%</span>。</p><p>其餘留言都是路人對故事本身的反應，例如責罵新聞中騙錢的女性、批評政黨、祈福或留下愛心。轉貼農場文章的一般使用者也不是為了澄清資訊：他們的 64 篇轉貼中，只有 1 篇屬於批評性分享，其餘貼文則寫著「懂就轉發」「終於有人寫出我的心聲」。</p><p>最直接反映這種狀況的一則留言，是一名路人直接詢問 Meta 的 AI：「这是真的吗 meta.ai」。Meta AI 確實回覆了這則提問。</p>',
 '內容農場的文章已經進入一般使用者的日常生活，媒體識讀卻在留言區中缺席。這項現象比「有人相信假新聞」更值得注意，因為<b>幾乎沒有人提出「這是不是新聞」這個問題。</b>')}'''

personas = f'''<div class="figwrap rv" data-zoom><div class="cap">圖二 · 五種路人平均每人追蹤多少個特定類型的帳號。縱軸代表每人的追蹤名單中，屬於該類型帳號數量的平均值：0.5 代表平均每兩人會有一人追蹤一個該類型帳號。本文依帳號名稱中的關鍵字判定類別，資料來自隨機樣本。長條高度是平均值，不是人數；各組人數標在組名底下，專職帳號底下的讀者只有 8 人，那組長條再高也只代表 8 個人。台灣讀者追蹤政治人物最多，TVB 劇迷追蹤藝人。</div>{fig_follow()}<div class="zoom-hint">點圖放大</div></div>
{PERSONAS}
<div class="lf" style="margin-top:36px"><p>綜合這五種類型，內容農場貼文在 Threads 上接觸到的並不是同一群人，而是五種彼此不重疊、分別受到不同題材吸引的路人。<b>沒有任何一種類型可以稱為「農場的受眾」；唯一近似常客的類型，長期停留在單一政治流言帳號，而不是整個農場。</b> 在隨機樣本中有自述所在地的留言者裡，台灣人約占一半，香港人約占四分之一；香港人集中在工具化帳號底下那一層，占該層近半。兩端政治傾向的讀者都有。</p></div>'''

farms = f'''<div class="lf"><p><b>如何閱讀這張表。</b>「驗過連結的貼文」是站內搜尋擷取後，逐篇解開連結並確認指向該群網域的貼文數。「Threads 帳號」是盤點表中標記為該群的帳號數，一個帳號張貼多個群的連結時會重複計入。「工具化／專職／站方」是三種散布帳號的數量：工具化帳號的連結帶有分享工具識別碼或分潤碼，或以「原文加 2 / 2 回覆」的固定格式發文；專職帳號張貼過 5 篇以上，但沒有工具痕跡；站方帳號是農場自己的官方帳號。「分享工具痕跡」表示該群的貼文中是否出現識別碼或分潤碼。「留言區每篇回覆」是該群貼文的留言區中，平均每篇的路人留言數。完整定義見 §04。</p></div>
<div class="flagship rv"><div class="flag-lab">§03 · 旗艦表</div><div class="flag-h">25 個農場群在 Threads 上的散布樣態與受眾</div>
<div class="tbl-scroll"><table class="flag-tbl"><thead><tr><th>群</th><th>網域</th><th>驗過連結的貼文</th><th>Threads 帳號</th><th>工具化／專職／站方</th><th>分享工具痕跡</th><th>留言區每篇回覆</th></tr></thead><tbody>{flagship_rows()}</tbody></table></div>
<p class="flag-note">群名以核心網域命名；完整網域清單列於附錄 A。帳號數是盤點表中標記為該群的 Threads 帳號數，一個帳號張貼多個群的連結時會重複計入。標色的五列是具有散布帳號網絡的群。</p></div>
<div class="lf" style="margin-top:44px"><ul>
<li><b>真正具有散布帳號網絡的只有五個群</b>：dsawjk、vivi01 影片站、picelse／luckyelse，以及 dsawjk 的兩個模板候選群 anyelse 與 qhd。這五個群的共同特徵，是貼文中帶有分享工具的痕跡。其餘 20 群有些主要依靠站方自營帳號發文（ENews、eatmary、chinanewscenter），有些只有一般使用者偶發轉貼，有些則未出現在 Threads 上。</li>
<li><b>東南亞向與越南向的群雖然有貼文，卻沒有華語受眾</b>：這些群分別有 588 篇與 96 篇驗過連結的貼文，留言區平均每篇分別有 0.07 則與 0.18 則回覆，而且所有回覆都不是華語。泰國 news01／HSU 群的 28 個網域中，只有 1 篇貼文命中。</li>
<li><b>參照群的 183 個帳號幾乎都是偶發轉貼者</b>：teepr、kknews 等老牌農場的連結是由一般使用者轉貼，並未形成散布網絡。參照群呈現的是「有農場但沒有操作」的對照情況。</li>
</ul></div>'''

method = '''<div class="lf">
<h3 class="sub-h">五層設計</h3>
<p>每一層的研究母體，都是上一層篩選或蒐集後的結果。我們為每一層設定明確邊界，說明資料蒐集到何處才算完整，也交代未處理邊界以外資料的理由。</p>
<div class="tbl-scroll"><table class="mini-tbl"><thead><tr><th>層</th><th>對象</th><th>邊界</th><th>實際涵蓋</th></tr></thead><tbody>
<tr><td>L0 網域</td><td>340 個農場網域</td><td>清單採用 2026-09-10 快照，所有網域皆反向搜尋</td><td class="r">340／340</td></tr>
<tr><td>L1 貼文</td><td>張貼這些網域連結的 Threads 貼文</td><td>站內搜尋每個網域最多 300 篇，另加 Google 索引前 10 筆；搜尋不到的貼文不在母體內</td><td class="r">逐篇驗證連結 5,202 篇</td></tr>
<tr><td>L2 帳號</td><td>張貼農場連結的帳號</td><td>完整擷取張貼驗過連結 5 篇以上或帶有自動化痕跡者的發文史；張貼 1 到 4 篇者只分析至貼文層</td><td class="r">1,520 個，296 個經核實</td></tr>
<tr><td>L3 留言區</td><td>這些貼文底下的互動</td><td>完整擷取 L1 母體中有任何互動的貼文</td><td class="r">1,106／1,114 篇</td></tr>
<tr><td>L4 路人</td><td>留言者</td><td>分層隨機抽樣有中文文字留言者，另納入所有回過兩篇以上貼文者</td><td class="r">250／833 人</td></tr>
</tbody></table></div>
<p style="margin-top:22px">證據層級代表我們對單一帳號查到的深度：0 代表只有搜尋引擎命中，1 代表摘要含有連結，2 代表逐篇驗證過連結，3 代表已核實完整發文史。我們在層級 3 才會把帳號判定為散布者，判定門檻是發文史中帶有農場連結的貼文達 5 篇以上，或占全部貼文的 20% 以上。我們依據可觀察的行為痕跡，把帳號分為四種類型：<b>站方自營</b>帳號的名稱與農場品牌相同；<b>工具化散布</b>帳號的連結帶有 <span class="mono">#threads</span> 識別碼、<span class="mono">utm_term=</span> 或 <span class="mono">uid=</span> 分潤碼 3 次以上，或使用「原文加 2 / 2 回覆帶連結」的固定格式注入；<b>專職轉貼</b>帳號張貼農場連結 5 篇以上，但沒有工具使用痕跡；<b>偶發轉貼</b>帳號則只張貼 1 到 4 篇。</p>
<p>我們以 Threads Crawl Tool 的三種模式擷取資料，全程未登入任何平台。我們透過 Facebook 公開的 Page Plugin，在未登入的狀態下取得臉書粉專名稱與追蹤數；Google 索引則透過 SerpApi 與 Serper 查詢。</p>
<h3 class="sub-h">預期與實際</h3>
<table class="verify rv"><thead><tr><th>開始前的假設</th><th style="width:44%">實際結果</th><th style="width:110px">判定</th></tr></thead><tbody>
<tr><td>農場靠一批散布帳號擴散，帳號之間存在組織痕跡</td><td>只出現在五個群；其餘群依靠站方帳號，或根本未出現</td><td class="upd">部分成立</td></tr>
<tr><td>散布帳號之間存在協作</td><td>散布帳號彼此回覆 0 次，共用的是代碼而不是關係</td><td class="upd">不成立</td></tr>
<tr><td>農場擁有固定受眾</td><td>833 人中只有 23 人曾回覆兩篇貼文</td><td class="upd">不成立</td></tr>
<tr><td>受眾會識別並質疑資訊</td><td>質疑來源的留言不到 2%</td><td class="upd">不成立</td></tr>
</tbody></table>
<h3 class="sub-h">抽樣與偏差</h3>
<p>L0 到 L3 的數字是研究母體，只有 L4 採取抽樣。我們依留言者所回貼文的帳號類型分為四層，原則上從每層有中文文字留言的人中隨機抽取 75 人；專職層只有 8 人留下文字，因此全部納入。我們再加入曾回覆兩篇以上貼文的 17 人，樣本合計 250 人，並使用固定亂數種子抽樣。另一組 189 人，是我們先前刻意選取留言字數較長者所建立的對照組。兩組結果一致的部分可信度較高；兩組結果不一致時，本文以隨機組為準。</p>
<p>L1 的貼文數受到 Threads 搜尋召回能力限制，因此只能視為下限。在搜尋結果中只出現 2 到 5 篇貼文的帳號，若進一步查完其發文史，會發現其中四成其實是張貼 50 篇以上的專職出口。340 個網域中，有 195 個沒有搜尋結果，但沒有搜尋結果不代表無人張貼。L3 完整涵蓋「有互動的貼文」，但不包括前期針對 dsawjk 群單獨調查的 565 篇，也不包括完全沒有互動的約一半貼文。L4 排除只留表情符號與非中文留言者。專職轉貼層的 102 則留言中，有 83 則是同一個巴西帳號收到的葡萄牙文留言，因此該層可用的華語留言者只有 8 人。</p>
<h3 class="sub-h">不能主張的</h3>
<ul class="gaps rv">
<li><b>本文不主張任何群的操作者國籍、主機位置，或是否受到國家指使。</b>分潤碼能證明的是「同一套分潤系統」，不能證明「同一個人」。</li>
<li><b>本文對受眾政治傾向的描述，只根據追蹤名單中的關鍵字分類。</b>每層樣本為 75 人，因此本文只能描述傾向；農場官方帳號底下的留言者，在兩種抽樣方式中都呈現政治光譜兩端，因此本文也只能描述為兩極。</li>
<li><b>我們無法取得按讚與轉發名單。</b>2026 年 8 月時，同一項工具仍能取得這些名單；從 9 月起，Threads 只回傳引用名單。按讚者是互動的主體，留言者只是願意發言的少數。</li>
<li><b>臉書的留言區在未登入時無法查看，而本研究不登入平台。</b>內容農場主要在臉書變現，因此本文的受眾結論僅適用於 Threads。</li>
<li><b>我們無法取得使用者的年齡、性別與真實地點。</b>本文所稱的所在地，都是使用者自述。</li>
</ul>
<h3 class="sub-h">個資與後續</h3>
<p>散布帳號是公開帳號，也有公開可見的散布行為，因此本文會具名，但具名範圍只限工具化散布與站方自營兩類帳號。本文一律不具名偶發轉貼帳號與留言路人，只呈現聚合後的輪廓。原始資料存放在未公開的本機倉庫中。</p>
<p>後續工作包括：監測工作應以識別碼與分潤碼為單位建立觀察名單；若要研究臉書受眾，研究者必須先決定是否接受使用需登入的研究帳號；研究者應回到臉書與公關稿網站，追查面向泰國與越南的群；研究者也應以更大的隨機樣本，確認 chinanewscenter 這類網站受眾的政治光譜。</p>
</div>'''

appendix = f'''<div class="lf">
<h3 class="sub-h" id="apx-a">附錄 A　網域清單（依群）</h3>
<p>清單為 2026-09-10 快照。候選群是依模板或廣告帳號重疊列入、尚未以追蹤碼確證同操作者的群；參照群不是調查對象，只作對照。點群名展開。</p>
{appendix_a()}
<h3 class="sub-h" id="apx-b">附錄 B　具名帳號清單</h3>
<p>只列行為類型為站方自營與工具化散布的 Threads 帳號，共 {len(named)} 個（站方 {sum(1 for d in named if d['behavior_type']=='站方自營')}、工具化 {sum(1 for d in named if d['behavior_type']=='工具化散布')}）。「農場貼文」在證據層級 3 是發文史 100 篇中帶農場連結的篇數，層級 2 是搜尋驗過連結的篇數。偶發轉貼帳號與留言者不列。</p>
<div class="filter"><input id="apx-q" type="search" placeholder="篩選帳號、群、分潤碼…" aria-label="篩選"><select id="apx-t" aria-label="類型"><option value="">全部類型</option><option>站方自營</option><option>工具化散布</option></select><span class="cnt" id="apx-cnt"></span></div>
<div class="tbl-scroll"><table class="mini-tbl" id="apx-tbl"><thead><tr><th>帳號</th><th>類型</th><th>群</th><th class="r">層級</th><th class="r">農場貼文</th><th>識別碼／分潤碼</th><th>註冊</th><th>自述所在地</th></tr></thead><tbody>{appendix_c()}</tbody></table></div>
</div>'''

sources = '''<div class="src-grid rv">
<div class="src"><span class="sid">[1]</span><div class="sx"><b>內容農場網域清單（registry）</b>，25 群 347 條目，2026-09-10 快照。本機倉庫，未公開。</div></div>
<div class="src"><span class="sid">[2]</span><div class="sx"><b>跨平台社群帳號盤點表</b>，3,784 筆，含證據層級、行為類型、識別碼與分潤碼欄位。本機倉庫，未公開。</div></div>
<div class="src"><span class="sid">[3]</span><div class="sx"><b>Threads Crawl Tool 1.9.x</b> 三種模式的原始輸出，2026-09-03 至 09-14，共 23 個抓取批次，逐批封存並附 SHA-256 清單。</div></div>
<div class="src"><span class="sid">[4]</span><div class="sx"><b>SerpApi 與 Serper</b> 的 <span class="mono">site:threads.com</span>、<span class="mono">site:facebook.com</span> 查詢結果，2026-09-05，原始 JSON 封存。</div></div>
<div class="src"><span class="sid">[5]</span><div class="sx"><b>Facebook Page Plugin</b> 零登入查詢，1,573 個粉專識別字，2026-09-09。</div></div>
<div class="src"><span class="sid">[6]</span><div class="sx"><b>分析腳本</b>：連結驗證與帳號判定、留言區彙整、路人輪廓聚合，隨案件倉庫保存，可重現。</div></div>
</div>'''

hero = '''<header class="hero"><div class="hero-inner">
<div class="hero-kicker">內容農場 · 社群層調查 · Threads · 2026 年 9 月</div>
<h1 class="hero-title">內容農場在 Threads 的<span class="cut">散布網絡與受眾</span></h1>
<p class="hero-stand"><b>內容農場的連結在 Threads 上到處出現，但張貼這些連結的帳號不是一群互相配合的人。</b> 農場會給分享者一組分潤碼，也就是放在連結裡、用來記錄分享者的代碼；誰的連結帶著這組碼，收益就算給誰。這些帳號各自貼文，彼此幾乎不互動。</p>
<div class="hero-numbers"><div class="hn-cell"><div class="hn-claim"><b>農場的帳本是分潤碼，不是帳號。</b>picelse 群的一個分享者編號由 10 個帳號共用，這些帳號之間從不互動。</div></div><div class="hn-cell"><div class="hn-claim"><b>農場沒有固定受眾，只有觸及。</b>833 名留言者中，只有 23 人曾回覆兩篇以上的貼文；每篇貼文觸及的都是不同的人。</div></div><div class="hn-cell"><div class="hn-claim"><b>農場文章進入日常，但少有人把它當成農場內容。</b>936 則留言中，質疑來源的不到 2%，其餘留言把它當成真實新聞在回應。</div></div></div>
<div class="hero-foot"><span class="dot"></span><span>340 個網域、1,520 個帳號、1,106 篇貼文的留言區、250 名隨機抽取的路人 · 研究方法見 §04</span></div>
</div></header>'''

page = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>內容農場在 Threads 的散布網絡與受眾</title>
<meta name="description" content="25 個農場群、340 個網域的社群層調查：分享者拿農場的分潤碼貼連結，演算法決定誰看到，路人留言後即離開。">
<meta property="og:type" content="article">
<meta property="og:title" content="內容農場在 Threads 的散布網絡與受眾">
<meta property="og:description" content="25 個農場群、340 個網域的社群層調查：分享者拿農場的分潤碼貼連結，演算法決定誰看到，路人留言後即離開。">
<meta property="og:url" content="https://wcl-dev.github.io/research-site/content-farm-threads-tw/">
<meta property="og:image" content="https://wcl-dev.github.io/research-site/content-farm-threads-tw/og.png?v=1">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{STYLE}
</style>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="badge" id="badge"><b id="badgenum">01</b><span id="badgename">三個洞察</span></div>
<div class="shell"><main>
{hero}
<nav class="inline-toc" aria-label="目次">{TOC}</nav>
{sec('insights','01','三個洞察','這批資料最能支持的三項結論，每項附一個關鍵數字和一句「因此」。',insights)}
{sec('persona','02','五種路人','以下五種人物輪廓，是根據隨機樣本 250 人的聚合數據與留言原文整理而成。抽樣方式是把 833 個留言者依其所回貼文的帳號類型分為四層，在有中文文字留言的人當中，每層隨機抽取 75 人；若該層樣本不足則全部納入，另外再納入所有回過兩篇以上貼文的 17 人。抽樣細節與偏差列於 §04。每個人物代表一種類型，而不是特定個人。本文引用留言時，只標示該則留言出現在哪一個群的貼文底下，不附上帳號，也不更動原文。',personas)}
{sec('farms','03','25 個群','25 個群在 Threads 上的散布樣態。讀者閱讀這張表時可以注意三點，列於表後。',farms)}
{sec('method','04','我們怎麼知道的','五層設計、證據層級、帳號類型、預期與實際、抽樣與偏差、不能主張的。',method)}
{sec('appendix','05','附錄','網域清單依群摺疊，具名帳號可篩選。',appendix)}
{sec('sources','06','資料來源','',sources)}
</main></div>
<footer><div class="ft-inner"><b>內容農場在 Threads 的散布網絡與受眾</b><br>
25 個農場群、340 個網域的社群層調查 · 2026 年 9 月<br>
立場：散布帳號具名、路人不具名；不主張操作者國籍或國家指使；受眾結論僅適用於 Threads。<br>
研究儲存庫 · <a href="https://github.com/wcl-dev/research-site">github.com/wcl-dev/research-site</a> · <a href="../">回 weichen's Research 首頁</a></div></footer>
<script>
(function(){{
  const progress=document.getElementById('progress'),badge=document.getElementById('badge'),badgeNum=document.getElementById('badgenum'),badgeName=document.getElementById('badgename');
  const sections=Array.from(document.querySelectorAll('section[data-num]'));
  function update(){{const docH=document.documentElement.scrollHeight-window.innerHeight;const pct=docH>0?Math.min(100,(window.scrollY/docH)*100):0;if(progress)progress.style.width=pct+'%';const y=window.scrollY+120;let active=sections[0];for(const s of sections){{if(s.offsetTop<=y)active=s;}}if(active&&badgeNum){{badgeNum.textContent=active.dataset.num;badgeName.textContent=active.dataset.name||'';if(window.scrollY>240)badge.classList.add('show');else badge.classList.remove('show');}}}}
  window.addEventListener('scroll',update,{{passive:true}});update();
}})();
{read(SK / 'shared/reveal.js')}
(function(){{
  document.querySelectorAll('.figwrap[data-zoom]').forEach(f=>{{f.addEventListener('click',()=>{{f.classList.toggle('zoom');document.body.style.overflow=f.classList.contains('zoom')?'hidden':'';}});}});
  document.addEventListener('keydown',e=>{{if(e.key==='Escape'){{document.querySelectorAll('.figwrap.zoom').forEach(f=>f.classList.remove('zoom'));document.body.style.overflow='';}}}});
}})();
(function(){{
  const q=document.getElementById('apx-q'),t=document.getElementById('apx-t'),tbl=document.getElementById('apx-tbl'),cnt=document.getElementById('apx-cnt');
  if(!q||!tbl)return;const rows=Array.from(tbl.tBodies[0].rows);
  function run(){{const s=q.value.trim().toLowerCase(),ty=t.value;let n=0;rows.forEach(r=>{{const ok=(!ty||r.dataset.type===ty)&&(!s||r.textContent.toLowerCase().includes(s));r.hidden=!ok;if(ok)n++;}});cnt.textContent=n+' / '+rows.length;}}
  q.addEventListener('input',run);t.addEventListener('change',run);run();
}})();
</script>
</body>
</html>'''
OUT.write_text(page, encoding='utf-8')
print('wrote', OUT, len(page))
