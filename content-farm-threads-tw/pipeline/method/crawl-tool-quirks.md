# Threads Crawl Tool 1.9.2 已知行為與資料品質問題

實測記錄。每項都註明發現的 run，可重新查證。後續分析必須先讀本文件，
否則會把工具行為誤讀為資料現象。

## 1. Link 模式對回覆型 URL 回傳母文，不回傳該回覆自己的留言區

**發現於：** run `2026-08-12_18-00-29`（CASE-2026-001 Tier 1，24 篇目標）

輸入一則回覆的網址時，工具回傳的是該回覆所在討論串的母文與其他參與者，
**不是**這則回覆自己的留言與按讚名單。24 個目標中只有 5 個回傳了目標貼文本身，
其餘皆為回覆型貼文，回傳的是其 `Origina_link` 指向的母文。

**影響：** 若調查對象習慣以回覆形式散布內容，必須另外把母文列入爬取清單，
否則完全拿不到互動資料。`Thread_link` 欄位記錄該列是由哪個輸入連結收集而來，
是唯一可靠的歸屬鍵；`link == Thread_link` 才是目標貼文本身。

## 2. 高讚貼文的 `like` 欄位會被截斷

**發現於：** 比對 run `2026-08-12_15-46-12`（Keyword）與 `2026-08-12_18-00-29`（Link）中同一批貼文

| 貼文帳號 | Keyword run | Link run | 判定 |
|---|---:|---:|---|
| `taipeishihchung` | 115,000 | 11 | 截斷 |
| `ryanpualpual` | 74,000 | 7 | 截斷 |
| `tetracyclin747` | 19,600 | 1 | 截斷 |
| `dr.brain_` | 15,600 | 1 | 截斷 |

讚數未達萬級的貼文兩次一致（如 `[帳號已隱去]` 5,000 / 5,069）。
`comment`、`repost` 兩次皆一致，未見此問題。

**機制：** Link 模式讀到介面顯示的「N.M萬」時，取整數部分而未套用萬的乘數。
四筆全部符合：

| 真值 | 介面顯示 | Link run 輸出 | `int(真值/10000)` |
|---:|---:|---:|---:|
| 115,000 | 11.5萬 | 11 | 11 |
| 74,000 | 7.4萬 | 7 | 7 |
| 19,600 | 1.96萬 | 1 | 1 |
| 15,600 | 1.56萬 | 1 | 1 |

**適用範圍：** 僅讚數 ≥ 10,000 的貼文受影響。低於一萬者介面顯示完整數字，
不經萬進位換算，故正確（且比 Keyword 模式精確，如 5,069 vs 概數 5,000）。

**影響：** Link 模式輸出的 `like` 欄位在讚數破萬的貼文上不可用。
需要正確讚數時，改用 Keyword run 的值（概數但量級正確），
或以 `link_behaviors.csv` 實際收集到的 Likes 筆數為準。
不得直接以 Link run 的 `like` 計算互動率或排序。

不建議用「乘回 10000」修補：整數部分已丟失小數，1.96萬 與 1.05萬 都會還原成 1 萬。

## 3. 第一個連結無資料時整批中止

**發現於：** run `2026-08-12_18-14-35`（CASE-2026-001 Tier 1b，18 篇母文）

```
[1/18] https://www.threads.com/@acer861122/post/Db6gDjdE6z1
Error: No objects to concatenate
  runner.py line 902, in _run_link
  ValueError: No objects to concatenate
```

處理完第 1 個連結後立即崩潰，退出碼 1，輸出目錄為空，其餘 17 個連結未執行。
`_run_link` 在存檢查點時對累積結果呼叫 `pd.concat`，若此時清單為空即拋錯。

**影響：** 單一無效連結（貼文已刪除、私人帳號、版面異常）若排在第一位，
會讓整批爬取失敗且無任何產出。

`_run_link` 有兩處 concat，錯誤行號可判斷缺哪一種資料：

| 行號 | 缺少 |
|---|---|
| 901 | posts（該連結完全無回傳） |
| 902 | behaviors（有 posts 但無互動者名單） |

**因應：** Link 模式輸入檔的第一個連結必須選用**實測確認會回傳資料**者。
批次失敗時先檢查第一個連結，不要直接假設全部連結都無效。

**反直覺之處：互動數高不代表能直接爬取。**
`taipeishihchung/post/DbuWCjiiW_8`（11.5 萬讚、5,061 留言）作為直接目標時
完全無回傳，兩度導致整批失敗（run `18-14-35`、`18-19-11`）；
但同一篇貼文在 Tier 1 run 中以「母文」身分被連帶收集時卻有資料。
推測與超大型貼文的頁面結構或載入逾時有關。
選 lead 連結時應依實測結果，不可用讚數推測。

**後續驗證：放在非首位即可成功。** 同一個 `taipeishihchung` 連結放在 8 篇中的
最後一個（run `2026-08-12_18-21-32` 續跑），回傳 920 行 posts 和 900 行 behaviors，
資料完整。因此 crash 僅限於該連結位於第一位且無先前累積資料的情境。

CASE-2026-001 已驗證可作為 lead 的連結記錄在
`analysis/build_followup_targets.py` 的 `PROVEN_DIRECT_TARGETS`。

## 4. 輸出欄位與 Keyword 模式不同

Link 模式 `link_posts.csv` 為 20 欄，無 `keyword`、`key`、`match_flag`、`case_name`，
但多出 `views` 與 `Thread_link`。`link_behaviors.csv` 為 5 欄：
`account_link`、`account_name`、`account_type`、`quotes`、`Thread_link`，
其中 `account_type` 為 `Likes` / `Reposts` / `Quotes`。

`views` 僅在目標貼文本身的列上有值，母文與其他參與者列為空。

## 5. 認證方式

`auth_mode: chrome` 會複製 Chrome 使用者設定檔到 `/tmp/local-crawl-tool-chrome`
再以 CDP 模式啟動，沿用既有登入 cookie。不需輸入帳號密碼，
研究資料夾內也不會留下憑證。設定中的 `account`、`password` 欄位應保持空白。

## 6. 隨程式散布的明文權杖

`/Applications/Threads Crawl Tool.app/Contents/Resources/.github_token` 為明文檔案。
用途未查證，內容未讀取。若工具由外部提供，建議向提供者確認該權杖的權限範圍。

## 7. `share_link` 是 Meta 轉址包裝，真實網址藏在 `u=` 參數裡

**發現於：** 全語料掃描（CASE-2026-001，5 個 run 共 27,962 列，2026-08-19）

貼文帶外部連結時，`share_link` 存的不是目標網址，而是 Meta 的轉址包裝：

```text
https://l.threads.com/?u=<URL-encode 過的真實網址>&e=<每篇貼文獨立的簽章>
```

實測 243 列 `share_link` 非空當中，231 列是這種包裝，且**全部可用 `u=` 參數離線還原**，
不需要對外發出任何請求。

**影響一：直接對 `share_link` 做網域統計會得到「231 筆 `l.threads.com`」**，
真實流向完全看不見。還原後才看得到實際有 96 個不同的外部網域。

**影響二：`e=` 每篇貼文都不一樣。** 同一個目標網址出現在不同貼文時，wrapper 字串完全不同，
因此任何以「網址字串」為單位的去重都會失效——同一支 YouTube 影片會被算成 N 個不同網址。
**去重必須在還原之後做。**

離線還原：

```python
from urllib.parse import urlparse, parse_qs, unquote

def decode_meta_shim(url: str) -> str:
    if "l.threads.com" not in url:
        return url
    target = parse_qs(urlparse(url).query).get("u")
    return unquote(target[0]) if target else url
```

**外連本身極度稀疏：27,962 列裡只有 243 列（0.84%）帶外部連結。**
以外連為主軸的分析在這個平台先天資料量就小，設計研究問題前要先確認量體夠不夠。
貼文正文裡的裸 URL 另計，但更少（同一批語料實測僅 3 筆）。

## 8. checkpoint / temp 檔不是 final 的子集，且與 final 內容重疊

**發現於：** run `2026-08-13_14-57-47`（CASE-2026-001，目前唯一產生這類檔案的 run）

該目錄除了 final CSV，另有 `keyword_checkpoint_latest.csv`、`keyword_result_temp.csv`
（兩者內容**完全相同**）與 `keyword_result_temp.xlsx`。

| 檔案 | 列數 | 不重複 link |
|---|---:|---:|
| `keyword_result_20260813_145747.csv`（final） | 4,506 | 4,178 |
| `keyword_checkpoint_latest.csv` | 500 | 500 |
| `keyword_result_temp.csv` | 500 | 500 |

checkpoint 的 500 列全部屬於同一個關鍵字 `Keyword.CL-B_template`。final 中該關鍵字
也正好是 500 列，**但兩者只有 388 個 link 重疊**——也就是 final 的那 500 列
是「另一批」500 列，checkpoint 有 **112 篇貼文是 final 完全沒有的**。

**影響一：直接 `rglob("*.csv")` 掃 `data/raw/` 會多算 1,000 列。**
實測全語料 28,962 列，排除 checkpoint/temp 後為 27,962 列。任何未排除的統計
（貼文數、帳號數、比例）都會偏高，而且不會有任何錯誤徵兆。

**影響二：但單純排除也不是全對。** 排除後會少掉那 112 篇只存在於 checkpoint 的貼文。
若該次爬取的覆蓋完整性重要，需另外把這 112 筆併入處理，不能當成純粹的暫存垃圾。

**實務建議：** 分析預設排除檔名含 `checkpoint` 或 `temp` 者（避免重複計算），
但在 manifest 或分析註解中記錄有這類檔案存在，不要假設它們的內容已被 final 涵蓋。

**未解：** 各關鍵字的列數叢集在 500 附近（500 / 501 / 1,000 / 1,505），疑似每個
關鍵字有批次或上限機制，checkpoint 捕捉到的是同一關鍵字較早的一批。機制未查證，
但這表示**單一關鍵字的抓取結果可能被截斷**，設計覆蓋率相關的結論時要留意。

## 9. 中斷後重跑不會開新 run_id，且會清空前次的 temp／checkpoint

**發現於：** CASE-2026-003，run `2026-09-03_18-10-09`（2026-09-03 18:10 起跑，18:27 電腦休眠後停滯；
2026-09-04 09:25 以新輸入檔重新按 RUN）

重新執行時工具**沿用前一次的 run_id 目錄**（不以本次啟動時間建新目錄），並在第一個關鍵字寫入時
**覆寫** `keyword_result_temp.csv` 與 `keyword_checkpoint_latest.csv`——前次累積的 839 列（16 個關鍵字）
自活檔消失。最終檔 `keyword_result_20260903_181009.csv` 的檔名時間戳也是舊 run_id，不是實際完成時間；
final 產出後 temp／checkpoint 會被刪除。

**影響：** 中斷的 run 若未在重跑前封存 temp 檔，資料即永久遺失，且不會有任何錯誤徵兆。
manifest 若只看檔名時間戳，會把 2026-09-04 的爬取記成 2026-09-03。

**因應：** (1) 重跑前先用 `archive_run.py` 封存前次 run 目錄；(2) 第二次封存時 run_id 會撞名
（`archive_run.py` 拒絕覆寫），先把來源目錄複製並加後綴（如 `_r1b`）再封存；(3) manifest 的 `note`
明寫實際起訖時間。另觀察：休眠導致的停滯不會讓工具報錯，`.running` 旗標與程序都維持「執行中」。

## 10. Meta 端節流：連續大量 Keyword／Account 後，Threads 所有查詢回 GraphQL 1675012「處理此要求時發生問題，請稍後再試」

**發現於：** CASE-2026-004 第一批（run `2026-09-05_13-23-41`，2026-09-05 13:23）

前兩天累計：Keyword 模式 93 個關鍵字（每個約 100 列）＋ Account 模式 49 個帳號（post_num 200、含追蹤名單），
第三天第一個關鍵字即失敗。工具不報錯：寫出只有表頭的 checkpoint 後結束，`.running` 旗標殘留。

**實測到的事實（2026-09-05，使用者在咖啡廳網路）：** (a) 使用者本人 Chrome（登入）搜尋回 Something went wrong；
(b) 同機無登入乾淨瀏覽器開搜尋頁與公開帳號頁 `/@leealy796` 同樣錯；(c) 網路層全部 HTTP 200，錯誤來自 Meta GraphQL 回應
`1675012`（BarcelonaSearchResultsQuery）與帳號查詢回 null——**不是網路過濾**；(d) 從另一個 IP 抓帳號頁回正常登入牆；
(e) 狀態站當時無大範圍故障。**IP 與帳號兩個變因尚未分離**（咖啡廳共用 IP 本身可能被 Meta 節流，帳號亦可能被限）。

**影響：** 單一環境兩天內約 100 關鍵字＋50 帳號是實測到的上限。大型反搜（276 關鍵字）不能一次跑完。

**因應：** (1) 跑前先用無登入瀏覽器開任一公開帳號頁，能渲染再跑；(2) 分批跨日、每天 ≤80 關鍵字；(3) 換網路＋換帳號各試一次以分離變因；
(4) 不碰 Threads 的補充路徑：`shared/scripts/serp_site_search.py`（SerpApi 免費 250 次/月，或 Serper 2,500 次；`site:threads.com "<域>"`），召回受 Google 索引限制，只能補不能替代。

**第二個數據點（2026-09-11 15:44，CASE-2026-004 L3 session3）：** 前兩天累計 Keyword 59 域＋Account 196 帳號（post_num 100）＋Link 444 篇（含留言區捲動），
第三個 Link session 一篇都抓不到，工具噴 `ValueError: No objects to concatenate`（`_run_link` 對空結果 concat），使用者端看到 Threads 跳警示後卡住。
同時無登入乾淨瀏覽器開同一篇貼文正常渲染＝**被限的是登入 session，不是 IP**（與 09-05 的觀察互補，兩個變因這次分開了）。
單日上限估計：Link 模式約 400 篇加上其他模式後就到頂；Link 每篇要捲留言區，成本比 Keyword 一個關鍵字高。

## 11. 文字裡的連結被截成「網域/路徑…」且 `share_link` 常是空的：只認 `https://` 會漏掉一半以上

**發現於：** CASE-2026-004 第二層重算（2026-09-07）

Threads 顯示貼文時把文字內的網址截成 `vivi01.com/watch…`（無協定、路徑截斷、尾巴是省略號），工具原樣寫進 `text`；
同一列的 `share_link`（連結卡片）常是空的，尤其是「1 / 2」原文與部分「2 / 2」自回覆。首版判定只用 `https?://` 正則
從 `text`＋解碼後的 `share_link` 抓網址，結果 [帳號已隱去] 的 70 篇 vivi01.com 只算到 2 篇、[帳號已隱去] 的 13 篇 okazu.cc 算到 0。

**因應：** 網域比對要再加裸網域正則（`(?<![\w./@])((?:[a-z0-9-]+\.)+[a-z]{2,})/[^\s…]*`）並對照 registry 清單；
實作在 `cases/CASE-2026-004-…/analysis/account_verdicts.py`，同時保留 `card_posts`（只算卡片）做對照。
截斷的路徑無法還原文章 id，要拿標籤（`#threadsN`）或 uid 只能靠有卡片的列。

## 12. Link 模式現在拉不到按讚／轉發名單；Stop 後旗標殘留；補跑會與前段合併

**發現於：** CASE-2026-004 受眾研究（run `2026-09-09_09-13-14`、`2026-09-09_11-01-10`）

(a) `link_behaviors.csv` 只剩 `Quotes`，`Likes`／`Reposts` 全為零（44 篇試點與 242 篇正式樣本皆然）；2026-08-12 CASE-001 同模式同版本抓到 Likes 616～3,421 筆。
`activity_max_items` 是 `runner.EasyCrawlConfig` 的參數，GUI 沒有對應欄位。研判是 Threads 端改了讚名單可見性，非設定問題。受眾分析改以回覆與引用為準。
(b) 讚數破萬的貼文（enews.tw 19,600 讚）會讓 Link 模式掛住不報錯（三小時檢查點不動）；樣本要先排除讚 >5,000 者。
(c) 按 Stop 後 `Documents/Local Crawl Tool/.running` 旗標與 app／Playwright 子程序仍在，再 Run 回「Already running」；
要結束 `ThreadsCrawlTool` 與 `Threads Crawl Tool.app` 的所有程序並刪旗標檔才能再跑（GUI 是 app 開的網頁，app 本身無視窗）。
(d) 掛住後以剩餘清單補跑，Link 模式沿用同一 run_id，final 檔＝前段＋補跑合併（與 §9 Keyword 模式清空 temp 的行為不同）；仍應先手動保全 temp 檔再重跑。

## 13. 筆電休眠會讓 Account 模式的 Playwright 瀏覽器關閉，其餘帳號全部 error 但 final 檔照寫

**發現於：** CASE-2026-004 受眾回覆者 run `2026-09-09_16-50-03`（190 帳號，post_num 30、crawl_following、skip_if_over 2000）

第 1～132 個正常（含 123 份追蹤名單），第 133～190 個 `threads_status=error`、`threads_reason` 皆為
`Page.goto: Target page, context or browser has been closed`。使用者確認當時把筆電合上；與 §9 觀察到的「休眠導致停滯」同源，
差別是這次瀏覽器直接關閉、工具把剩餘帳號標 error 後仍寫出 final 檔並殘留 `.running` 旗標（§12(c)）。不是 Meta 節流。

**因應：** 長批次跑的時候別讓機器休眠；跑完檢查 `threads_status`，把 error 的帳號另存補跑檔（`accounts_*_rerun.csv`）；
Account 模式補跑會開新 run_id（與 Link 模式合併同 run_id 的行為不同），分析時把兩個 run 一起餵。
