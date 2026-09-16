# CASE-2026-004：registry 其餘各群網域 Threads 反搜

## 目的

擴增社群帳號清單（`~/kwara-farm-registry/evidence/social-accounts-2026-09-03/`）。CASE-2026-002（picread 群 18 域）與 CASE-2026-003（dsawjk 群 54 域）
之外，registry 其餘 276 域從未在 Threads 反搜過；dsawjk 群 也證明「沒看到」多半是「沒搜過」。本案一次搜完，每群的散布帳號層各自登錄。

歸因狀態維持 **not-attributed**。網域層權威在 registry；本案只維護 Threads 側帳號層。

## 輸入：四批（label 欄＝registry cluster id，爬蟲輸出的 `case_name` 會帶著它，分析時直接歸群）

| 檔案 | 群 | 關鍵字數 | 預估 | sha256 |
|---|---|---:|---|---|
| `inputs/keywords_b1_confirmed_tw.csv` | qsh-alpha, qsh-beta, qsh-gamma, family-01, looker-17 | 78 | 約 94 分鐘 | `e46d67a07ec34f87` |
| `inputs/keywords_b2_small_and_tw_cands.csv` | farm-eatmary, ezvivi, farm-enews, farm-twqiang, cand-docilepuppy, cand-happyshare, cand-singles, cand-ptt-network, cand-tw-cells, cand-qastack, cand-hk-farms | 68 | 約 82 分鐘 | `08e94110e37dcfa1` |
| `inputs/keywords_b3_alpha_cands.csv` | cand-qhd-adstxt, cand-anyelse-net, cand-cn-fanwen | 59 | 約 71 分鐘 | `defb4a70b22ac41d` |
| `inputs/keywords_b4_sea_and_refs.csv` | vietnam-adsense, thai-news01-hsupr, thai-wdwire, cand-thai-narrative-amplifiers, ref-active, ref-groups | 71 | 約 85 分鐘 | `a60f9ae4e50b26ba` |

## 執行（GUI，逐批）

Keyword 模式，設定與 CASE-2026-003 相同（GUI 沿用上次：Top 分頁、每關鍵字約 100 列、auth chrome）。一批跑完再貼下一批的路徑，
**每批各自一個 run_id**；跑完先叫 Claude 封存再跑下一批（quirks §9：重跑會沿用 run_id 並清空 temp）。別在批次中途休眠。

## 封存

```bash
python3 shared/scripts/archive_run.py \
  --source ~/Documents/"Local Crawl Tool"/output/keyword/<run_id> \
  --case-dir cases/CASE-2026-004-all-clusters-threads-sweep \
  --mode keyword --tier <batch 名> \
  --input-file inputs/keywords_<batch 名>.csv \
  --settings '{"keyword_tab": "Top（推斷）", "max_posts": "GUI 沿用", "auth_mode": "chrome"}'
```

## 分析（每批跑完即做，最後合併）

`analysis/sweep_extract.py`：兩層解碼 `share_link`，以 `case_name`（＝群 id）歸群，輸出每群的網域命中、帳號、`#片段` 標籤、
與 CASE-002／003 帳號的重疊。命中帳號寫回社群帳號 xlsx 的 Threads 分頁（增量追加，cluster 欄＝群 id）。

## 措辭

Threads Keyword 只是 Top 分頁樣本；0 命中只能寫「本次未見」。單篇無標籤帳號依慣例標「可能一般轉貼」。

## 搜尋引擎補充路徑（2026-09-05，Threads 爬蟲被 Meta 節流期間）

`shared/scripts/serp_site_search.py --backend serpapi`（SerpApi 免費 250 次/月）對 b1＋b3 共 137 域查 `site:threads.com "<域>"`：
106 域有命中、717 筆網址、**444 個帳號（412 個不在既有清單）**；結果 `analysis/serpapi_threads_b1b3_merged.csv`、原始 JSON
`data/raw/serpapi_threads_b1b3_2026-09-05/`。召回率測試（`analysis/serpapi_recall_test_threads.csv`）：每域 Google 只索引約 10 篇、
帳號與 Threads 內搜幾乎不重疊（12 帳號重疊 3）→ 補充而非替代。

**性質警語**：Google 索引命中只代表貼文文字或連結提到該網域，未驗證是否為散布行為（東森新聞 `[帳號已隱去]`、`meta.ai` 也在命中裡），
入帳號清單時角色一律標「搜尋引擎索引命中，待驗證」，待 Threads 節流解除後用 Account 模式或 Post 頁面核實。
臉書版（`--platform facebook.com`）對 b1 跑完：73/78 域命中、637 筆網址、**248 個實體（粉專 180、社團 68）**；解析後檔 `analysis/serpapi_facebook_b1_parsed.csv`。
★picread 群 有 41 個臉書社團在貼連結（先前影片線只知 3 個），社團是 picread 群 的主要臉書通路；looker-17 自家粉專（dailyder／BuzzHandCom／How01Com）跨十幾域出現＝站方自推。
Threads 444 帳號＋臉書 248 實體已增量追加進 `~/kwara-farm-registry/evidence/social-accounts-2026-09-03/` xlsx（1,270 筆）。SerpApi 本月剩約 30 次。
b2／b4 與其餘臉書批次改用 Serper（2,500 點）跑。

### SerpApi 命中的驗證分級（2026-09-05）

Google 索引命中不等於散布。三層驗證：

1. **摘要層（已做，零接觸）**：Google 回的標題／摘要若含 `網域/doc_…`、`/pic_…`、`/d/…` 等**完整文章連結**，代表貼文本身帶農場連結。
   Threads 674 篇中 410 篇（61%）含連結；405 帳號中 213 個至少 1 篇、64 個 ≥2 篇、38 個 ≥3 篇。臉書 245 實體中 132 個含連結。
   這些在 xlsx 的角色升為「散布者候選（Google 摘要含農場文章連結 N 篇）」；只提到網域而無連結者維持「待驗證」。
   限制：摘要會截斷，含連結是充分條件不是必要條件；摘要本身也可能來自回覆／引用。
2. **貼文層（Threads 節流解除後）**：對 ≥2 篇含連結的 64 個帳號跑 Account 模式（post_num 200），與 CASE-003 同一套流程：
   完整發文史裡的農場連結比例、`#threads<N>`／`?uid=` 標籤、註冊月、追蹤結構。臉書粉專用 Page Plugin／Post Plugin（不登入）核現名與貼文。
3. **排除層**：主流媒體與平台官方帳號（`[帳號已隱去]`、`meta.ai`、`[帳號已隱去]` 等）即使含連結也不算散布者，標「媒體引用」。

### Serper 補撈（2026-09-05，b2／b4 Threads；b2／b3／b4 臉書；第 1 頁 10 筆＋飽和域續翻第 2–3 頁）

Serper 拒絕 `num=100`，實際每頁 10 筆；第一段每域 1 點、第二段對第 1 頁滿 10 筆的域翻第 2–3 頁。ref-groups 的 7 個非網域條目（集團名）已由腳本跳過。
Threads b4／臉書 b4 第一段因非網域檔名炸掉，已從 raw JSON 重建（`--from-raw`），無額度損失。

| 平台 | 網址 | 命中域 | 實體 | 摘要含農場連結的實體 |
|---|---:|---:|---:|---:|
| Threads（b2＋b4） | 611 | 54 | 323 帳號 | 170 |
| 臉書（b2＋b3＋b4） | 3,864 | 167 | 1,704（粉專 1,450、社團 244） | 680 |

合併檔：`analysis/serper_threads_merged.csv`、`analysis/serper_facebook_all_parsed.csv`。已增量追加進盤點 xlsx（現 3,247 筆；CASE-004 來源
Threads 725、臉書 1,898）。摘要含連結者角色為「散布者候選」，其餘「待驗證」；主流媒體／官方帳號的排除（第三層）尚未做。
泰國敘事放大候選群（cand-thai-narrative-amplifiers）Threads 96 帳號、臉書 141 實體，是本輪社群層最活躍的候選群之一，值得優先核實。

### 第三層排除（2026-09-05，人工策展）

自動規則試過三條：(1) 帳號名含 news／媒體品牌——會誤殺農場自己的帳號（enews.tw、newsnews_forlife、ENews.Star），不能自動套；
(2) 只分享 ref-active／ref-groups 主流站——那些站本身是公開清單上的內容農場，分享也可能是散布，不排除；
(3) 跨 ≥3 群——dsawjk 群／picelse／luckyelse 群／秦皇島候選同生態系的真下線也會跨群，不能單獨用。
改為人工策展名單 `analysis/exclusions_2026-09-05.csv`：A 類 58 個確定的主流媒體／平台／政府帳號 → 角色「排除」；
B 類 38 個 registry 網域自有帳號（enews 系列、dailyder、freshhhnews、newspolar、malay.news…）→ 角色「站方官方帳號」。
套用後 CASE-004 來源：Threads 散布者候選 337／待驗證 363／排除 19；臉書 散布者候選 776／待驗證 1,066／排除 39。
規則一命中但未列入 A／B 者（[帳號已隱去]、[帳號已隱去]、[帳號已隱去]、aseantopnews 等）維持原角色，待人工核。

## 第二層：Account 模式核實 Google 索引候選（2026-09-05 準備，Threads 節流已解除）

輸入 `inputs/accounts_serp_candidates_r2.csv`：76 帳號＝摘要含農場連結 ≥2 篇或跨 ≥2 群，扣除第三層排除、站方官方、與 CASE-002/003 已抓過發文史者。
**配額紀律（quirks §10）**：前次同機兩天內 93 關鍵字＋49 帳號（post_num 200＋追蹤名單）即觸發節流。本輪建議 **post_num 100、不抓追蹤名單**，
一天只跑這一批；Keyword 四批（276 域）之後每天一批。跑前先用無登入瀏覽器開 `/@leealy796` 確認渲染。

| 設定 | 值 |
|---|---|
| mode | Account |
| post_num | 100 |
| crawl_followers / crawl_following | false / false |
| skip_if_over | 1000 |

封存：`archive_run.py --mode account --tier serp_candidates_r2 --input-file inputs/accounts_serp_candidates_r2.csv --settings '{"post_num":100,"crawl_followers":false,"crawl_following":false}'`。
分析：對每帳號算「發文史中農場連結比例」「跨群網域」「#threads／uid 標籤」「註冊月」，≥20% 或 ≥5 篇農場連結者升為「散布者（發文史核實）」，
否則降為「偶發轉貼」。結果寫回 xlsx（role／registered／location／followers／following）。

### 第二層結果（2026-09-07，Account 模式 post_num 100，run `2026-09-07_09-44-01` ＋補跑 `2026-09-07_14-05-04`）

判定由 `analysis/account_verdicts.py` 產生（`serp_candidates_r2_verdicts.csv`、`serp_candidates_r2b_verdicts.csv`），
寫回盤點表用 `~/kwara-farm-registry/evidence/social-accounts-2026-09-03/apply_threads_verdicts.py`。

**★首版判定（2026-09-07 上午的臨時程式碼）漏算了一半以上的農場連結，已於同日重算訂正。** 原因：Threads 把文字裡的連結截成
「vivi01.com/watch…」，工具常抓不到連結卡片（`share_link` 空），只認 `https://` 開頭的網址就漏掉。重算後 6 個帳號判定翻轉：
[帳號已隱去]（family-01 vivi01.com 2→70 篇）、[帳號已隱去]（cand-anyelse-net okazu.cc 0→13 篇，全是「okazu.cc/… 2 / 2」自回覆）、
[帳號已隱去]（farm-eatmary 1→6）、[帳號已隱去]（qsh-beta 1→5）升為散布者；[帳號已隱去]、[帳號已隱去] 從「無」改「偶發」。
判定檔保留 `card_posts` 欄＝舊口徑，方便對照。

R2 76 候選：62 有回傳、57 有自發貼文；未回傳 14 個中 3 個是香港媒體（[帳號已隱去]、[帳號已隱去]、[帳號已隱去] → 第三層 A 類排除）、
[帳號已隱去] 無登入探測回登入牆（私人或已刪除）、其餘 10 個補跑（R2b，10/10 回傳，hia3473112025 仍無貼文資料）。

| 判定 | R2（57） | R2b 補跑（10） | 規則 |
|---|---:|---:|---|
| 散布者（發文史核實） | 36 | 6 | 農場連結 ≥5 篇或 ≥20% |
| 偶發轉貼 | 8 | 0 | 1–4 篇且 <20% |
| 發文史無農場連結 | 13 | 3 | Google 命中為舊文或誤配；含 [帳號已隱去]（馬來西亞 The Star，應歸媒體排除） |
| 未回傳 | — | 1 | 工具無資料 |

- **比例怎麼讀**：一篇農場文常是「原文 1 / 2」＋「2 / 2 帶連結」兩列，只算連結卡片時滿載帳號比例約 0.5，連文字裸網域一起算則接近 1.0。判定門檻用篇數，別被比例誤導。
- **新增 dsawjk 群 標籤**：#threads5168（cheungna3 ×30）、#threads2067（yaping3121 ×50）、#threads2994、#threads3214、#threads5043、#threads1822、#threads2771、#threads323——一標籤一帳號再確認；dsawjk 群 散布帳號 2024-08～09 註冊批次再現（8＋7）。
  R2b 的 ivanovivanebe（50 篇 dsawjk 群、2024-09 註冊、香港）、[帳號已隱去]、[帳號已隱去]（各 7 篇 dsawjk 群）沒有 #threads 標籤，屬手貼或另一套工具。
- **picelse／luckyelse 群／family-01 共用 `utm_term=N` 分潤寫法**：girlsnews747→picelse `utm_term=1883`、news.xinwen→picelse `utm_term=9223`、tvbzuixinzixun→vodsilo.cc `utm_term=576`、tvbfanssharingnews1712→vivi01 `utm_term=36`。
  ★R2b 的 **youtubenews747 也用 `utm_term=1883`（55 篇）＝與 girlsnews747 同一分潤編號**，兩帳號（名字同款 *news747）是同一操作者的兩個出口；[帳號已隱去] 推 picelse／luckyelse 群 17 篇（`utm_term=8478`）。
  ★`utm_term=576` 與 picread 群 的 uid 576 只是數字撞名（picread 群 用 `?uid=`），**不是** picread 群↔family-01 連結；但 picelse／luckyelse 群 與 family-01 影片站共用同一套編號系統，與兩群共用私有 CDN 的既有觀察一致。
- picread 群：turnerhugheshughes→hknews.pro `?uid=12742`（新 uid）。越南向：[帳號已隱去] 71 篇推 cand-thai-narrative-amplifiers 的 vietnaminsiders。
- cand-anyelse-net：hedy.pater 只有 16 篇貼文但 5 篇帶 okazu.cc；加上 [帳號已隱去] 的 13 篇，okazu.cc 有兩個專職散布帳號。
- 結果已寫回 xlsx（role／registered／location／followers／join_keys／linked_domains／notes；三個香港媒體與 4 個站方帳號套第三層排除）。

## Keyword 反搜第一批 b1（confirmed_tw 78 域；run `2026-09-05_13-23-41`，實跑 2026-09-07 晚～09-08 00:50）

run_id 沿用 09-05 被節流那次的目錄（quirks §9）。78 個關鍵字全部跑完：57 個有回傳列、21 個 Threads 搜尋零結果（工具不寫零結果列，
缺的關鍵字散在輸入順序各處，非中途節流）。工具回傳 9,429 列，其中 `match_flag=0`（不含該網域的貼文）9,147 列由 `sweep_extract.py` 自行驗連結後剔除。
輸出：`analysis/sweep_b1_hits.csv`（2,146 篇驗過連結）、`sweep_b1_accounts.csv`（246 帳號）、`sweep_b1_summary.json`。
`sweep_extract.py` 本批起加 `--prefix`（四批輸出不互覆）與 `--input`（零命中只算本批實搜的網域）。

| 群 | 搜的域 | 有命中的域 | 驗過連結的篇數 | 帳號 | ≥2 篇 | ≥5 篇 | 與 CASE-002/003 重疊 |
|---|---:|---:|---:|---:|---:|---:|---:|
| qsh-alpha | 23 | 12 | 1273 | 83 | 61 | 47 | 28 |
| family-01 | 11 | 6 | 573 | 57 | 22 | 12 | 0 |
| qsh-beta | 3 | 2 | 230 | 47 | 30 | 12 | 3 |
| looker-17 | 23 | 7 | 37 | 35 | 2 | 0 | 2 |
| qsh-gamma | 17 | 3 | 18 | 15 | 2 | 0 | 1 |
| cand-docilepuppy | 1 | 1 | 15 | 9 | 3 | 1 | 4 |

- **有命中 31 域、零命中 47 域**。零命中：family-01：cklive.net, coolgirl01.com, fav543.com, restcookie.com, tmmlove.com；looker-17：lookerpets.com, how543.com, itislooker.com, 17readthis.com, buzzhand.com, look543.com, omg4fun.com, how01.com, lookingforward.info, omgnews.cc, funtoday.news, happyday543.com, lookernew.com, omg543.com, read543.com, starfocus.news；qsh-alpha：666.44finefood.com, aigo7.com, co-47.com, designiwe.com, dreamwe1.com, jkingtimes.com, lovey-puppys.com, pets-dote.com, pets-naivety.com, with-summer.com, zavideo.successs-experience.com；qsh-beta：tvsilo.com；qsh-gamma：coms.pub, justshare.live, cklive.live, videowatch.fun, vidonline.org, kanwatch.site, gogovideo.net, share-video.cc, vidlah.com, ytttube.com, eeurl.press, photoshare.pro, funshare.pro, ppoo.club。
  ★零命中不等於沒人貼——designiwe.com 在 R2 發文史裡 cheungna3 貼了 10 篇，Keyword 搜尋就是搜不到；Threads 搜尋召回本來就差（CASE-003 已知），
  Google 索引那層（第一層）與發文史（第二層）是必要的補充。
- **dsawjk 群 依舊最大**：1,273 篇／83 帳號／47 個 ≥5 篇；`#threads` 標籤再現（threads7374＝zyy71687 ×98、threads1700＝shaoqianglee、threads11044、threads745）。
  dsawjk 群 帳號有明顯的「同日開跑」批次：2026-08-11 起（jbn03297、arrietlinor3235、dunaykin.igor、qhw39489）、2026-06-13/14 起（srb02145、016c5276757、yiqsj2025）、2025-01-18 起（violet374546、avyvq1）。
- **family-01 影片站**：vodsilo.cc 254 篇幾乎全是 tvbzuixinzixun（R2 已核實）；`utm_term` 再現 1883（phpnews747／girlsnews747／chinesenews747 三個 *news747 帳號共用）、576、3863、8901。
- **picelse／luckyelse 群**：luckyelse／picelse 230 篇、47 帳號，uid 8842、1127、8427、9510、8752（haha123zx ×79）。
- **itigeryou.com（registry 內雙列：qsh-alpha via kwara case 17 ＋ cand-docilepuppy）**：9 個帳號共 15 篇，全帶 `#threads` 標籤
  （leealy796 #threads9656 ×5、dison26475 #threads14074、threads7482、threads4397），4 個帳號與 CASE-003 dsawjk 群 帳號重疊——社群層再確證它走 dsawjk 群 的散布工具；已回寫 registry note。
- looker-17／picread 群 在 Threads 幾乎沒有聲量（37／18 篇、無 ≥5 篇帳號），與兩群主攻臉書的既有觀察一致。looker-17 的 fragment（`m274d7qncj199cshcz` 等）不是 #threads 格式，是站方自己的錨點。
- 已入盤點表（build_accounts.py 新增 E5 段）：新增 159 個 Threads 帳號；既有 SERP 命中的帳號若被 Keyword 驗到連結，角色依「只升不降」規則升級
  （搜尋引擎索引 ＜ Google 摘要含連結 ＜ Keyword 逐篇驗連結 ＜ Account 發文史核實／人工排除）。

### 第二層名單（b1 → Account 模式）

≥2 篇的 115 帳號扣掉已抓過發文史的 30（CASE-002/003/004 R2）→ 85 個，依篇數拆兩天：
`inputs/accounts_kw_b1_r3a.csv`（45 個，篇數最多）與 `accounts_kw_b1_r3b.csv`（40 個）。設定同 R2（Account、post_num 100、不抓追蹤名單、skip_if_over 1000）。
跑完：`archive_run.py --mode account --tier kw_b1_r3a …`，`account_verdicts.py --run … --input inputs/accounts_kw_b1_r3a.csv --out analysis/kw_b1_r3a_verdicts.csv`，
`apply_threads_verdicts.py --verdicts … --label 'b1 R3a'`。

## Keyword 反搜第二批 b2（small_and_tw_cands 68 域、11 個小群；run `2026-09-08_22-07-45`，2026-09-08 22:07–23:12）

同日已跑 b1 78 域，再跑 68 域未觸發節流（單日 146 關鍵字，比 quirks §10 的估計寬）。68 個關鍵字全跑完：31 有回傳、37 零結果。
輸出 `analysis/sweep_b2_hits.csv`（993 篇驗過連結）、`sweep_b2_accounts.csv`（197 帳號）、`sweep_b2_summary.json`。

| 群 | 搜的域 | 有命中的域 | 驗過連結的篇數 | 帳號 | ≥2 篇 | ≥5 篇 |
|---|---:|---:|---:|---:|---:|---:|
| farm-eatmary | 2 | 2 | 337 | 30 | 5 | 4 |
| cand-singles | 11 | 6 | 306 | 25 | 6 | 3 |
| farm-enews | 3 | 3 | 260 | 125 | 13 | 1 |
| farm-twqiang | 5 | 1 | 63 | 1 | 1 | 1 |
| cand-docilepuppy | 22 | 1 | 15 | 9 | 3 | 1 |
| cand-ptt-network | 7 | 2 | 7 | 3 | 1 | 1 |
| cand-happyshare | 2 | 1 | 2 | 1 | 1 | 0 |

零命中：cand-docilepuppy 21 域（docilepuppy.com, channel2025.com, friend-color.com, knowledgekhabar.com…）；cand-happyshare 1 域（happyshare101.com）；cand-ptt-network 5 域（pttcareers.com, pttconsumer.com, pttdigits.com, pttfoodtravel.com…）；cand-singles 5 域（dailytin24.com, newsentertai.com, newstoday123.com, 74novel.com…）；farm-twqiang 4 域（bpic.lawtw.com, bodhi.lawtw.com, human.lawtw.com, whlwell.com）。cand-qastack 六個語言站、cand-ptt-network 七個 ptt* 站、lawtw 三個子域全部零結果。

- **聲量集中在站方自己的帳號**：chinesehotnews→chinanewscenter.com 254 篇（cand-singles；內容是中國政治流言，與其他商業農場性質不同）、
  eatmary2020 166 篇＋kikinote123 67 篇（farm-eatmary）、enews.tw 官方 119 篇。這些都已在第三層 B 類（站方）。真正的下線只有：
  [帳號已隱去] 72 篇 kikinote（R2 已核實）、[帳號已隱去] 63 篇全推 twqiang 的 co2 子站（2024-12～2025-02，碳議題）、[帳號已隱去] 19 篇 janeeyrego.com（男性保健品，貼文帶「2 / 2」自回覆＝dsawjk 群/picelse／luckyelse 群 同款分享工具寫法）。
- **enews.tw 的 `?uid=` 不是 picread 群 的分潤編號**：uid=108 被 11 個不同帳號共用、410 被 5 個共用、站方自己用 310/990/3100，且網址常帶臉書分享參數 `sfnsn=mo`，
  是站方端的來源／版位參數，不是每個分享者一個。與 picread 群 的 uid 值（uid 對照表 158 列）無撞號。★盤點表的 uid 對照分頁原本把所有 `uid=` 標成 picread 群 分潤編號，本批改依網域所屬群標示。
- **dsawjk 群 帳號跨群貼 enews.tw**：CASE-003 的 [帳號已隱去]、[帳號已隱去] 各貼 2–4 篇 enews.tw／life.tw，屬個別轉貼（篇數少、走臉書分享），不是 dsawjk 群 工具管道。
- itigeryou.com 與 b1 重複搜到（兩批關鍵字檔都有），結果相同（9 帳號 15 篇、#threads 標籤），入表時同帳號不重複計。
- farm-enews 的 125 個帳號絕大多數 1 篇（一般讀者轉貼），只有站方 ≥5 篇。ref-active／looker-17 各 1–2 篇是別群關鍵字撈到的順帶命中。
- 入盤點表：新增 173 個 Threads 帳號（1,127→1,300）。

### 第二層名單（b2）

≥2 篇 31 帳號，扣除已抓發文史 2、站方／排除 5、已在 b1 r3 名單 3 → `inputs/accounts_kw_b2_r3.csv` 21 個。
篇數 ≥5 的只有 [帳號已隱去]、[帳號已隱去]、[帳號已隱去]、[帳號已隱去]、[帳號已隱去]；其餘 2–4 篇。依「先跑完四批 Keyword 再決定 Account 核實範圍」的原則暫緩。

## Keyword 反搜第四批 b4（sea_and_refs；實搜 `keywords_b4_domains_only.csv` 64 域；run `2026-09-08_23-23-23`，2026-09-08 23:23–09-09 00:28）

原 b4 檔的 7 個 ref-groups 集團名條目（「coco01 集團」等）不是網域，Threads 會當文字搜、回來的貼文無網域可驗，故去掉後跑 64 域。
同日累計 b1＋b2＋b4 共 210 個關鍵字，未觸發節流（quirks §10 的「兩天 100」是保守估計，實測單日 210 仍可）。
64 域：33 有回傳、31 零結果。輸出 `analysis/sweep_b4_*`：858 篇驗過連結、188 帳號。

| 群 | 搜的域 | 有命中的域 | 驗過連結的篇數 | 帳號 | ≥2 篇 | ≥5 篇 |
|---|---:|---:|---:|---:|---:|---:|
| cand-thai-narrative-amplifiers | 11 | 7 | 588 | 26 | 7 | 3 |
| ref-active | 13 | 5 | 173 | 128 | 16 | 4 |
| vietnam-adsense | 8 | 4 | 96 | 33 | 8 | 3 |
| thai-news01-hsupr | 28 | 1 | 1 | 1 | 0 | 0 |

- **泰國 news01/HSU 網絡不在 Threads 上**：28 域只有 newsbeat.asia 1 篇。這個網絡的散布層在臉書與 PR 稿站，Threads 反搜對它無效，社群層要從 f-research/thai 既有的臉書線索接。
- **越南向兩個專職帳號**：[帳號已隱去]→vietnaminsiders.com 298 篇（R2 已核實，2026-04 起每日）、[帳號已隱去]→enewspolar.com 254 篇（2023-07～2024-10，尼泊爾名）。
  vietnam-adsense 的 thebustednews.com 76 篇由 [帳號已隱去]（39）等印度名帳號推，帶 `#goog_rewarded`（AdSense 獎勵廣告的錨點）。這些是英語圈／南亞受眾的變現站，與台灣受眾無關。
- **ref-active 的 kknews.cc 163 篇散在 128 個帳號**，多為一般讀者轉貼（≥5 篇只有 [帳號已隱去] 12、[帳號已隱去] 11、[帳號已隱去] 7、teeprnews 5），沒有散布網絡。
- 與 b1/b2 重疊只有 [帳號已隱去]、[帳號已隱去] 兩個。
- 入盤點表後 Threads 分頁見 build_accounts 輸出。

### 第二層名單（b4）

≥2 篇 31 帳號扣除已抓發文史與站方 → `inputs/accounts_kw_b4_r3.csv`。越南／南亞向帳號與台灣受眾無關，優先度最低。

## 四批總結（2026-09-09）

b3（59 個 dsawjk 群 候選域）未跑：b1 的 dsawjk 群 帳號已有 28 個與 CASE-003 重疊、47 個 ≥5 篇，再搜 dsawjk 群 候選域預期撈到同一批人，留到需要時再補。
四批實搜 210 域（b1 78＋b2 68＋b4 64）：驗過連結 3,997 篇、去重後帳號約 600。各群在 Threads 的社群層答案：

| 群 | Threads 上的散布層 |
|---|---|
| qsh-alpha | 最大：83 帳號、47 個 ≥5 篇、#threads 分享工具、同日開跑批次 |
| family-01／qsh-beta | 中：影片站專職帳號（tvbzuixinzixun 254 篇）＋ *news747 系列共用 utm_term=1883 |
| farm-eatmary／farm-enews／cand-singles | 站方自營帳號撐聲量，下線零星 |
| looker-17／qsh-gamma／farm-twqiang | 幾乎沒有（picread 群 用 uid 分潤但在 Threads 找不到帳號） |
| thai-news01-hsupr | 完全沒有 |
| vietnam-adsense／cand-thai-narrative-amplifiers | 有專職帳號但受眾非台灣 |
| cand-docilepuppy／ptt-network／qastack／hk-farms 等小群 | 零 |

## 受眾研究（2026-09-09，Link 模式；run `2026-09-09_11-01-10`）

目的：回答「什麼樣的路人和農場帳號互動」。樣本 `inputs/links_audience_v2.csv` 244 篇依盤點表「行為類型」分層；
實際回傳 242 篇（enews.tw 19,600 讚那篇讓工具掛住三小時，排除；[帳號已隱去] 一篇未回傳）。
輸出 `analysis/audience_v2_replies.csv`（路人回覆逐則）、`audience_v2_summary.json`。

**★讚名單拉不到（quirks §12）**：`link_behaviors` 只有引用 61 筆，Likes／Reposts 零；8 月 CASE-001 同模式抓到數千筆。受眾只能從回覆與引用看。

| 分層 | 貼文 | 有回覆的貼文 | 路人回覆 | 回覆者 | 每篇回覆 |
|---|---:|---:|---:|---:|---:|
| 偶發轉貼 | 113 | 77 | 283 | 243 | 2.5 |
| 專職轉貼 | 37 | 20 | 109 | 101 | 2.95 |
| 工具化對照 | 42 | 8 | 66 | 63 | 1.57 |
| 站方自營 | 50 | 44 | 291 | 278 | 5.82 |

回覆語言（規則：粵語詞／簡體字／純表情）：

| 分層 | 繁體中文 | 簡體 | 粵語 | 純表情或符號 |
|---|---:|---:|---:|---:|
| 偶發轉貼 | 243 | 6 | 6 | 28 |
| 專職轉貼 | 33 | 2 | 1 | 73 |
| 工具化對照 | 51 | 1 | 2 | 12 |
| 站方自營 | 245 | 28 | 4 | 14 |

- **路人幾乎都是路過的**：683 個回覆者裡只有 13 個回過 ≥2 篇、2 個跨分層，沒有「粉絲」結構。農場的 Threads 受眾靠演算法丟給不同的人，不是養出來的社群。
- **工具化帳號不是零互動，但最低**：42 篇只有 8 篇有回覆，每篇 1.57 則；站方自營每篇 5.82 則最高，專職轉貼 2.95、偶發 2.50。分工的圖成立：工具帳號種連結，站方與專職帳號才有人理。
- **專職轉貼的回覆七成是純表情**（73/109），多在 TVB 影片站帳號（tvbzuixinzixun）底下，是粉絲式的祈福／愛心，不是對內容的討論。
- **站方自營的簡體回覆 28 則**幾乎全在 chinesehotnews（中國政治流言）底下，受眾含簡體中文使用者；其餘站方（enews、eatmary）是台灣繁體。
- 農場帳號自己的回覆 182 則＝「2 / 2」注入，已排除。meta.ai（Meta 的 AI 帳號）在兩個分層底下自動回覆，分析時要濾掉。
- 下一步：對回覆者跑 Account 模式取所在地／註冊月／簡介，樣本 `inputs/accounts_audience_all.csv`（v2 四分層各 25＋試點 90，去重後 190 個；post_num 30 即可）。

**操作紀錄**：Stop 後工具的 `.running` 旗標與程序殘留，再 Run 回「Already running」；結束 app 與其 Playwright 子程序、刪 `Documents/Local Crawl Tool/.running` 後才能跑。
補跑沿用同 run_id 並把兩段合併成 final（與 Keyword 模式 §9 清空 temp 的行為不同）。

### 第四步：回覆者輪廓（2026-09-09，Account 模式 run `2026-09-09_16-50-03`）

輸入 `inputs/accounts_audience_all.csv` 190 個回覆者（v2 四分層各 25＋試點六群 90），post_num 30、抓追蹤名單、skip_if_over 2000。
132 個成功；第 133 個起 58 個全部「Target page has been closed」＝筆電合上休眠讓工具的瀏覽器關閉（quirks §13），
不是 Meta 節流；補跑檔 `inputs/accounts_audience_all_rerun.csv`。以下數字以成功的 132 個為準，每分層 22～30 人，只能看傾向。
輸出 `analysis/audience_following_summary.json`（聚合表，不含個人清單）。

| 分層（回覆者所回的貼文類型） | 所在地（前三） | 註冊年 2024／2025／2026 | 追蹤中位數 | 貼文中位數 |
|---|---|---|---:|---:|
| 偶發轉貼 | 台灣 22、香港 1 | 12／7／2 | 414 | 299 |
| 專職轉貼 | 台灣 11、中國 1、香港 1 | 12／6／3 | 104 | 142 |
| 工具化對照 | 台灣 15、香港 8 | 16／5／0 | 129 | 115 |
| 站方自營 | 台灣 6、香港 6、中國 4、美國 2 | 10／8／8 | 39 | 41 |

- **沒有人回頭追蹤農場**：123 個有追蹤名單的回覆者裡，只有 1 個追蹤了任何站方／工具／專職帳號（[帳號已隱去]）。和第三步「路過型」一致：農場在 Threads 沒有粉絲。
- **台灣回覆者的追蹤名單偏政治參與、且偏綠**：整體最常被追蹤的是蔡英文（10）、陳水扁（6）、八炯（6）、明居正（5）、沈伯洋（4）、賴清德（4）、黃國昌（3）、陳柏惟（3）、陳其邁（3）、吳崢（3）；
  偶發轉貼分層尤其明顯（蔡英文 7、陳水扁 5、沈伯洋 4）。也就是說，在 enews／eatmary 這類台灣農場貼文下留言的，很多是關心政治、反中立場的一般使用者，
  農場內容的來源（陸源、商業套利）和它在 Threads 上碰到的受眾立場並不一致。★這是 22～30 人的小樣本，只能當假設，補跑完再看。
- **站方自營分層的回覆者像新開的空帳號**：追蹤中位數 20、貼文中位數 41、2026 年註冊 8 個，追蹤名單裡多是 Threads 預設推薦的 Meta 官方帳號（Meta Newsroom、Instagram 等）；
  所在地散在台灣、香港、中國、美國。這一層多是 chinesehotnews（中國政治流言）底下的回覆者，要留意是否為人頭帳號，但目前證據只到「新帳號」。
- **工具化對照的回覆者三分之一在香港**，追蹤的是香港藝人（Error、古天樂、林夕）：工具帳號推的 TVB 影片站內容吸到的是港人，不是台灣人。
- 專職轉貼分層混雜：追蹤 Meta AI、阿滴、7-ELEVEn、momo 購物，是一般消費型使用者。

**方法紀錄**：追蹤名單 JSON 的欄位是 `display_name`＋`href`（`/@handle`）；聚合時以 handle 計數。這批是一般民眾，表只出聚合、不列個人追蹤清單。

### 第四步（完整版，2026-09-10）：189 個回覆者的輪廓（run `2026-09-09_16-50-03` ＋補跑 `2026-09-10_09-31-37`）

補跑 58 個全部回傳，合計 189 人（試點六群的 90 人依其所回貼文的帳號類型併入四分層）。聚合表在 `analysis/audience_repliers_profile.json`；不列個人。

| 回覆者所回的貼文類型 | 人數 | 所在地：台灣／香港／中國／其他 | 註冊年 2024／2025／2026 | 追蹤者中位 | 追蹤中位 | 貼文中位 | 有簡介 |
|---|---:|---|---|---:|---:|---:|---:|
| 偶發轉貼 | 44 | 36／2／0／6 | 23／13／2 | 125 | 209 | 164 | 73% |
| 專職轉貼 | 40 | 22／3／1／14（巴西 5） | 17／9／8 | 84 | 75 | 131 | 52% |
| 工具化對照 | 47 | 27／14／0／6 | 26／9／0 | 61 | 97 | 132 | 47% |
| 站方自營 | 58 | 27／8／6／17（美 4、Not shared 3） | 27／13／8 | 62 | 52 | 42 | 52% |

**使用習慣**（最近 30 篇）：四層幾乎一樣，回覆占一半（45–47%），晚上 18–23 時最活躍（30–39%），深夜 10–14%；沒有哪一層是「白天上班時間才用」或「全是回覆型」的。
自發貼文的題材桶命中率都低（政治 4–7%、美食旅遊 3–6%），代表多數人貼的是日常瑣事，不是議題帳號。

**語言**：偶發轉貼層 91% 繁體；工具化對照層粵語 10%（港人）；站方自營層簡體 8%、粵語 8%；專職轉貼層非中文或純表情 20%。

**追蹤名單**（173 人有名單）：
- 追蹤任一農場帳號（站方／工具／專職）的只有 1 人。農場在 Threads 沒有粉絲，四層皆然。
- **偶發轉貼層是政治參與度最高的一群**：每人平均追蹤 0.9 個政治人物或政黨、0.6 個媒體或知識帳號；最常被追蹤的是蔡英文 7、陳水扁 6、沈伯洋 4、清流君 3、泛科學 3。名單長度中位數 59，是四層裡最會用 Threads 的。
- **站方自營層像新開的帳號**：名單中位數 20、貼文中位數 42、2026 年註冊 8 人、所在地最分散（含中國 6、美國 4）；最常追蹤苗博雅、蔡康永、明居正、八炯、黃暐瀚、陳水扁各 3。這層主要是 chinesehotnews（中國政治流言）與 enews 底下的回覆者。
- **工具化對照層**：30% 在香港，追蹤港星與日語學習 App；台灣的部分追蹤民進黨、王定宇、明居正、吳崢。
- **專職轉貼層**：追蹤 Meta AI、7-ELEVEn、Lidl（德國）；政治方面八炯 3、黃國昌 3、國民黨 2、翁曉玲 2，是四層裡唯一藍白名單和綠名單並存的。

**對「什麼樣的台灣人吃這套」的初步回答**：在台灣農場貼文下留言的路人，多數是一般的、晚上滑 Threads 的繁體使用者，
沒有粉絲關係、沒有回頭；有政治傾向者偏綠與反中（尤其偶發轉貼層），與農場內容的陸源背景不一致。
農場在 Threads 的觸及靠的是演算法把單篇貼文丟給不特定的人，不是養出來的受眾。★樣本每層 40～58 人，追蹤名單分類用關鍵字，只能當傾向。

**拿不到的**：年齡、性別、真實地點、是否同一人多帳號。工具沒有回傳 IG 連動欄位（`crawl_ig_header` 未開）。

### 第五步：路人是在對抗還是附和？（2026-09-10，回覆態度）

問題：在偶發轉貼帳號（分享過 1–4 次農場連結的一般人）的貼文下留言的路人，是在澄清農場的假資訊，還是順著內容？
資料：`data/raw/2026-09-09_11-01-10` 的 64 篇偶發轉貼母文與其下 283 則路人回覆，對照站方自營層 291 則。
方法：先用寬鬆關鍵字分四類（質疑／附和／提問／其他），發現「質疑」多是在罵新聞人物（騙錢的女生）不是質疑農場，
改用只針對「來源或真偽」的字眼（假新聞、農場、舊聞、幾年前、查證、出處、AI 生成、亂寫、造謠、真的假的、小編、寫錯…）重算，命中的全部人工讀過。
逐則結果在 `analysis/audience_v2_reply_stance.csv`（寬鬆版四類，僅供瀏覽）。

| 分層 | 路人回覆 | 針對來源／真偽 | 比例 |
|---|---:|---:|---:|
| 偶發轉貼 | 283 | 6 | 2.1% |
| 站方自營 | 291 | 9 | 3.1% |
| 專職轉貼 | 109 | 0 | 0% |
| 工具化對照 | 66 | 0 | 0% |

- **分享的人不是在澄清**：64 篇母文只有 1 篇是批評性分享（「又一個釣魚文加小粉紅亂搞」），24 篇加了自己的話但都是順著內容（「懂就轉發」「終於有人寫出我的心聲」），7 篇純標題加連結。他們把農場文當一般新聞轉。
- **回覆的人也不是在對抗**：283 則裡只有 6 則指出來源或真偽有問題（「這新聞不是好幾年前的事了嗎」「這個是中國內容農場文」「新聞寫錯了，真實資訊要看官方的」「AI 引用維基百科然後說內容農場是新聞」等）。
  其餘九成八是對故事裡的人與事的反應：罵騙錢的女生、罵政黨、祈福、表情符號。**內容穿透了，但穿透的是一群沒有把它當農場的路人。**
- **站方自營層質疑比例略高（3.1%）**，集中在 chinesehotnews（中國政治流言）底下的簡體使用者（「造謠」「假消息」「赌5万人民币这是假消息」），是反駁內容，不是識別農場。
- 所以第四步的「偶發轉貼層政治參與最高、偏綠」要這樣讀：這群人關心政治、會用 Threads，但在農場文下的行為和一般路人一樣，被故事帶著走，不是在做事實查核。
  這也解釋農場為何不需要粉絲：每篇文只要碰到願意對故事有反應的人就夠了。
- ★分類靠關鍵字加人工讀 15 則，樣本小；寫報告只能說「零星」，不能報比例。

## Keyword 反搜第三批 b3（dsawjk 群 模板候選三群 59 域；run `2026-09-10_11-11-19`，2026-09-10 11:11–12:25）

59 域：36 有回傳、23 零結果（cand-cn-fanwen 六個中國範文站全零）。輸出 `analysis/sweep_b3_*`：657 篇驗過連結、80 帳號。
**L0 至此 340／340 個 registry 真網域全部反搜過**（CASE-002 picread 群 18＋CASE-003 dsawjk 群 54＋CASE-004 b1/b2/b4 209＋b3 59；7 個 ref-groups 集團名條目不是網域）。

| 群 | 搜的域 | 有命中的域 | 驗過連結的篇數 | 帳號 | ≥2 篇 | ≥5 篇 |
|---|---:|---:|---:|---:|---:|---:|
| cand-anyelse-net | 31 | 10 | 436 | 42 | 21 | 15 |
| cand-qhd-adstxt | 22 | 7 | 220 | 37 | 19 | 7 |

- **兩群都帶 dsawjk 群 的 `#threads` 標籤**：leealy796 #threads9656（貼 anyelse 系）、linlinwen5 #threads2264、[帳號已隱去] #threads1530（qhd-adstxt 系）等 9 個標籤。
  這兩群在 registry 是「共用 dsawjk 群 ads.txt 模板但抓不到追蹤碼」的 C 級候選，社群層現在證實它們的散布走 dsawjk 群 的分享工具，和 itigeryou.com 同一種再確證；已回寫 registry note。
- **三個同日開跑批次**：2025-05-13～05-20（[帳號已隱去]、chikatengsen、shaoqianglee、[帳號已隱去]、[帳號已隱去]、[帳號已隱去] 六帳號各 15–20 篇）、
  2026-01-14～02-04（inzwg2025、nny3086222025、hia3473112025 各 38–57 篇）、2026-01-20～01-30（kjmjunga2、huying904、minilovenovel、chen95244822 各 37–39 篇）。
  同一週開、同一週停、篇數相近＝批次投放，是 dsawjk 群 散布層的典型作法。hia3473112025 在 R2b 兩次 Account 模式都未回傳，這裡 38 篇。
- 專職帳號 ory315844 推 15lovingclub.com 83 篇（2025-06 起持續到現在）。
- 與 b1/b2/b4 重疊 8 個帳號。入盤點表後見 build_accounts 輸出。

### 第二層名單合併（r3）

b3 ≥2 篇者扣除已抓發文史與已列名單 → `inputs/accounts_kw_b3_r3.csv`；與 b1 r3a/r3b、b2 r3、b4 r3 合併去重、扣已抓發文史者，依篇數拆成 `inputs/accounts_r3_session{N}.csv`（每檔 ≤120，quirks §13 休眠風險）。
設定同 R2：Account、post_num 100、追蹤名單關、skip_if_over 1000。跑完 `account_verdicts.py` → `apply_threads_verdicts.py`。

## 第二層核實 R3（r3 合併名單；session1 2026-09-10，run `2026-09-10_13-39-30`）

輸入 `inputs/accounts_r3_session1.csv`：五份 r3 名單合併去重後篇數 ≥5 的 82 帳號，82/82 回傳。判定 `analysis/r3_session1_verdicts.csv`，已寫回盤點表。

| 判定 | 帳號數 |
|---|---:|
| 散布者（發文史核實） | 60 |
| 偶發轉貼 | 7 |
| 發文史無農場連結 | 15 |

- **`utm_term=1883` 現在有 6 個帳號共用**：girlsnews747、youtubenews747（R2）＋ tiktoknews747、phpnews747、chinesenews747、fbnews747（本輪），全推 picelse／luckyelse（picelse／luckyelse 群）並夾幾篇 family-01。同一分潤碼、同一命名法（平台名＋news747）、2024-07～11 註冊＝同一操作者的六個出口。
- **`utm_term=8842` 是馬來西亞的 picelse／luckyelse 群 分潤位**：yangji8500（2024-07）、kennyng5291、kkme124412026（皆 2026-02 註冊、所在地馬來西亞），各 54–57 篇。加上 haha123zx（馬來西亞，100 篇 luckyelse），picelse／luckyelse 群 的散布層有一條馬來西亞線。
- **b3 的批次帳號核實**：chen95244822（qhd-adstxt 95 篇）、inzwg2025（anyelse 90 篇，所在地中國）、huying904、nny3086222025、minilovenovel 都是 50 篇以上的專職出口，2/2 自回覆 50 上下＝工具注入。
- 註冊月集中在 2024-07～10（48/82），所在地香港 27、台灣 25、馬來西亞 10、中國 6：dsawjk 群／picelse／luckyelse 群 的散布帳號多半自述在香港與馬來西亞，台灣只占三成。
- 15 個「無農場連結」多是 ref-active（kknews、teepr）的一般讀者或 Google 舊文誤配。

session2（81 帳號，2–5 篇）待跑。

### R3 session2（2026-09-10 17:22–18:50，run `2026-09-10_17-22-58`）

輸入 `inputs/accounts_r3_session2.csv`：篇數 2–5 的 81 帳號。18:48 筆電合蓋，工具把剩餘 12 個標 error 後寫出 final（quirks §13）；69 有資料，12 個另存 `inputs/accounts_r3_session2_rerun.csv`。
判定 `analysis/r3_session2_verdicts.csv`，已寫回盤點表。

| 判定 | 帳號數 |
|---|---:|
| 散布者（發文史核實） | 28 |
| 偶發轉貼 | 13 |
| 發文史無農場連結 | 27 |
| 未回傳（待補跑） | 12 |

Keyword 只搜到 2–5 篇的帳號，翻完發文史有四成是 50 篇以上的專職出口（yetta30422 dsawjk 群 78 篇、hui1181_2／hui1.181 family-01 各 70 篇、erliusanjiu dsawjk 群 60 篇…），
說明 Threads 搜尋對單一帳號的召回很低，第二層 Account 模式不能省。

- **picelse／luckyelse 群↔picread 群 共用散布者**：ericcheww（馬來西亞，2025-01）與 shixiaoqi6554（馬來西亞，2025-11）同時貼 picelse／luckyelse 群 的 `utm_term=8427` 連結與 picread 群 的 `uid=12853／1143／12690` 連結。
  先前判定 `utm_term=576` 與 picread 群 uid 576 只是撞名，仍成立；但這兩個帳號是**同一人同時領 picelse／luckyelse 群 與 picread 群 兩套分潤**，是 picelse／luckyelse 群 與 picread 群 在散布層的第一個帳號級橋。
- **picelse／luckyelse 群 馬來西亞線再擴**：`utm_term=8842` 加 kpopbreaking2026、kaobeiahxi101（2026-02）、jedsonzieyyh（2026-08）；`utm_term=9510` 是一組 `lp000000NN2026` 命名的帳號（2026-05～06 註冊，馬來西亞，各 11–17 篇）；`utm_term=8600` ooooe113、`utm_term=8901` anime_thenews_。
  加上 fararrinews747（`utm_term=1883`，第 7 個 *news747）。picelse／luckyelse 群 的散布層以馬來西亞帳號為主體，命名有規律、註冊成批。
- dsawjk 群：dison26475 #threads14074 ×43、ha0lqz2025 #threads7950 ×30、jza00060 #threads744（帶 `#gw` 前綴變體）；2024-08 註冊批次再現（11 個）。
- 所在地台灣 20、馬來西亞 15、香港 11、中國 5；27 個「無農場連結」多為 ref-active 一般讀者。

### L2 收尾（2026-09-11）：session3 與 CASE-003 R2 重算

- session3（run `2026-09-11_10-07-51`）：CASE-003 dsawjk 群 R1 只用 Keyword 抓到、從未跑過 Account 的 21 帳號 → 10 散布者／3 偶發／8 無。
- CASE-003 R2 的三個 Account run（2026-09-04）共 49 帳號，當時只回填屬性沒寫判定，這次用 `account_verdicts.py` 重算 → 32 散布者／6 偶發／11 無，角色升到證據層級 3。
- **L2 邊界達成**：盤點表 Threads 分頁裡「驗過連結 ≥5 篇或帶工具痕跡（工具化／專職）」的帳號全部跑過 Account 模式，剩餘未核實數為 0。
  目前層級分布：3 層 296、2 層 585（1–4 篇，依規則停在此）、1 層 235、0 層 353；行為類型：工具化散布 201、專職轉貼 27、站方 11、偶發 817＋核實無 71。
- R3 三個 session 加補跑合計 184 帳號：98 散布者、27 偶發、59 無（含 CASE-003 重算則 130 散布者）。

## L3 全量（2026-09-14）：1,106 篇有互動農場母文的留言區

母體：L1 驗過連結的母文中有任何互動者 1,114 篇（`analysis/audience_full_population.csv`），排除讚 19,600 那篇，1,106 篇回傳（8 篇未回傳，多為 tvbzuixinzixun 已刪文）。
五個 run：v2 `2026-09-09_11-01-10` ＋ session1–4（`2026-09-11_10-39-05`、`2026-09-11_13-47-19`、`2026-09-13_14-40-34`、`2026-09-14_09-10-34`）。
逐則回覆在 `analysis/audience_full_replies.csv`，彙總 `audience_full_summary.json`。**這是母體不是樣本，數字不需再談抽樣偏差。**

回覆 1,397 則：農場帳號自回覆 457（「2/2」注入）、meta.ai 4、**路人回覆 936 則、833 人**。

| 發文帳號類型 | 爬到的貼文 | 有回覆的貼文 | 路人回覆 | 回覆者 | 每篇回覆 |
|---|---:|---:|---:|---:|---:|
| 偶發轉貼 | 229 | 91（40%） | 318 | 277 | 1.39 |
| 專職轉貼 | 288 | 19（7%） | 102 | 97 | 0.35 |
| 工具化散布 | 245 | 55（22%） | 133 | 120 | 0.54 |
| 站方自營 | 344 | 108（31%） | 383 | 340 | 1.11 |

| 群（前 8） | 貼文 | 路人回覆 | 回覆者 | 每篇回覆 |
|---|---:|---:|---:|---:|
| cand-singles | 210 | 237 | 198 | 1.13 |
| farm-enews | 109 | 151 | 144 | 1.39 |
| family-01 | 288 | 121 | 109 | 0.42 |
| farm-eatmary | 106 | 96 | 86 | 0.91 |
| cand-qhd-adstxt | 32 | 92 | 86 | 2.88 |
| looker-17 | 15 | 76 | 74 | 5.07 |
| ref-active | 57 | 66 | 48 | 1.16 |
| qsh-alpha | 42 | 41 | 39 | 0.98 |

- **路人是路過的，全量確認**：833 人裡回過 ≥2 篇的 23 人、≥3 篇 9 人；跨帳號類型 1 人、跨群 1 人、對兩個以上農場帳號回覆 2 人。最多的 [帳號已隱去] 回了 12 篇，全在同一個帳號底下。
- **每篇回覆量的排序和抽樣時不同**：抽樣時站方每篇 5.8 則是因為挑了互動最高的前 15 篇；全量是偶發轉貼 1.39、站方 1.11、工具化 0.54、專職 0.35。
  專職轉貼帳號的貼文 288 篇只有 19 篇有人回，而且 92% 的回覆是純表情（TVB 影片站帳號底下的粉絲愛心），沒有文字對話。
- **工具化帳號不是零互動**：245 篇有 55 篇有人回（22%），每篇 0.54 則。它們的貼文確實有人看到並反應，只是量低於站方與偶發。
- **語言**：偶發層 86% 繁體；站方層簡體 10%（chinesehotnews 底下）；工具化層粵語 8%（TVB 影片站內容的港人）。
- **針對來源或真偽的回覆**：站方層 3.4%（13 則，多在 chinesehotnews 的中國政治流言底下）、偶發層 1.6%、工具化 0.8%、專職 0。整體不到 2%。
- 引用 95 筆；讚與轉發名單仍為零（quirks §12）。
- 各群每篇回覆最高的是 looker-17（5.07，[帳號已隱去] 藝人貼文）與 cand-qhd-adstxt（2.88）；泰國敘事放大器候選 148 篇只有 10 則回覆（0.07），越南向 0.18，這些群在 Threads 沒有華語受眾。

### L4 抽樣設計（2026-09-14）

母體：833 個路人回覆者。抽樣：有中文文字回覆者中，依發文帳號類型每層隨機抽 75（`random.seed(20260914)`），加上所有回過 ≥2 篇者。
專職轉貼層有中文文字的回覆者只有 8 人（其餘純表情），該層全取。共 250 人（隨機 233＋跨篇 17），其中 82 人先前已跑過 Account 模式不重爬，
剩 168 人拆成 `inputs/accounts_audience_random_session1.csv`、`session2.csv`（各 84），Account 模式 post_num 30、開追蹤名單、skip_if_over 2000。
名單與分層在 `analysis/audience_random_sample.csv`。★一般民眾，只出聚合輪廓不點名。

## L4（2026-09-14）：隨機樣本 250 人的輪廓，與活躍者版並排

L4 樣本：有中文文字回覆者每層隨機 75（專職層僅 8）＋回過 ≥2 篇者 17，共 250 人；先前抓過的 82 人沿用，新抓 168 人（run `2026-09-14_10-42-42`、`_12-55-35`、`_14-04-32`；
第一個 run 在第 28 個帳號時瀏覽器關閉，補跑後齊）。聚合在 `analysis/audience_random_profile.json`；活躍者版（189 人，挑字多的）在 `audience_repliers_profile.json`。

| 分層（所回貼文的帳號類型） | 人數 | 所在地前三 | 註冊 2024／25／26 | 追蹤者中位 | 追蹤中位 | 貼文中位 | 有追蹤名單 |
|---|---:|---|---|---:|---:|---:|---:|
| 偶發轉貼 | 75 | 台灣 51、香港 6、新加坡 2 | 35／17／7 | 85 | 162 | 156 | 68 |
| 工具化散布 | 75 | 香港 37、台灣 22、日本 5 | 46／20／0 | 71 | 79 | 141 | 69 |
| 站方自營 | 75 | 台灣 34、香港 10、中國 9 | 29／22／9 | 40 | 56 | 94 | 71 |
| 專職轉貼 | 8 | 台灣 5、香港 2 | 5／1／0 | 182 | 368 | 51 | 8 |
| 回過 ≥2 篇 | 17 | 台灣 7、美國 2、香港 2 | 7／3／2 | 37 | 50 | 2,300 | 16 |

**隨機版與活躍者版一致的結論**
- 沒有粉絲關係：232 份追蹤名單裡追蹤任一農場帳號的 6 人（專職層 3、工具化 2、跨篇 1），2.6%；活躍者版是 1/173。
- 使用習慣四層相同：回覆占約半（43–48%），晚間 18–23 時最活躍，自發貼文以日常為主（各題材命中 1–7%）。
- 偶發轉貼層是政治參與最高的一群：每人平均追蹤 0.63 個政治人物或政黨、0.24 個政治評論者，最常追蹤蔡英文 9、沈伯洋 6、賴清德 4、明居正 4；名單長度中位 64。
- 站方自營層像新帳號：名單中位 20、貼文中位 94、2026 年註冊 9 人、所在地最分散（中國 9）。

**隨機版才看得到的**
- **工具化散布層的受眾一半在香港**（37/75），追蹤的是古天樂、李施嬅、朱晨麗這些港星和 TVB 藝人；註冊集中 2024 年（46）。工具帳號推的 TVB 影片站內容，在 Threads 碰到的是港人不是台灣人。
- **站方自營層的政治光譜和偶發層相反**：最常追蹤 Team Trump 4、蔣萬安 3、國民黨 3，蔡英文只有 2。這層主要是 chinesehotnews（中國政治流言）與 enews 底下的回覆者，偏藍白與親川普。
  活躍者版看到的是苗博雅、蔡康永、明居正（偏綠），隨機版翻過來，代表 chinesehotnews 底下的受眾光譜是混的，小樣本哪一邊都能抽到。★這一點寫報告時只能說「兩極都有」。
- **回過 ≥2 篇的 17 人貼文中位數 2,300**，是重度使用者，但名單短（中位 20）、不追政治，像是專門在留言區活動的帳號。
- 專職轉貼層 8 人追蹤名單偏購物與品牌（7-ELEVEn、蝦皮、Panda Palace 熊貓帳號），和該層貼文（TVB、熊貓影片）的粉絲屬性一致。

**對「什麼樣的台灣人吃這套」的最終回答（Threads 範圍）**：農場貼文在 Threads 碰到的是路過的一般使用者，不是粉絲；台灣人占六成，
另有三到五成是港人（工具化帳號推的 TVB 內容）與少數中國、東南亞使用者。有政治傾向者兩極都有：一般台灣分享者底下偏綠反中，
中國政治流言站方底下偏藍白親川普。多數回覆是對故事的情緒反應，指出來源有問題的不到 2%。年齡與性別無法取得。

**拿不到／未做**：讚與轉發名單（平台限制）、臉書受眾（登入牆）、年齡性別、同一人多帳號。

### 訂正（2026-09-16）：專職轉貼層的留言不是「92% 純表情」

L3 全量與 L4 段落寫專職轉貼層 102 則留言「92% 純表情」，是語言分類把非中文一律歸入「非中文／表情」造成的誤讀。重算：中文 8、外語文字 86、純表情 8；外語的 83 則是同一個巴西帳號 [帳號已隱去]（推巴西向農場網域）底下的葡萄牙文政治留言。
結論不變（該層華語留言者只有 8 人），但描述改為「幾乎沒有華語受眾」而非「粉絲式表情」。報告 v1.1 已依此改寫 persona 四；persona 五（回過 ≥2 篇的 17 人）12 人在 chinanewscenter 底下、追蹤者中位 36、無人追蹤該帳號，是否人頭無法判定。

### 訂正（2026-09-16）：留言者所在地不是「台灣六成、港人三到五成」

上面「最終回答」那句把不同層的比例疊在一起寫，兩個數字相加超過十成。依隨機樣本 250 人重算，有自述所在地的 227 人裡台灣 119 人（約一半）、香港 57 人（約四分之一）；港人集中在工具化帳號底下那一層（37／75，近半），偶發層與站方層的港人只占一成上下。報告 v1.3 已改為「台灣約一半、香港約四分之一，港人集中在工具化層」。

### 訂正（2026-09-16）：常客層「貼文中位數 2,300」不採用

17 人裡只有 5 人抓得到貼文數，中位數 2,300 是這 5 人的數字，不能代表 17 人。報告改用有 16 個值的追蹤者中位數 36（不到 50 人的 10 人、個位數 4 人）。
