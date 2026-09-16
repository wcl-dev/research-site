# content-farm-threads-tw

**內容農場在 Threads 的散布網絡與受眾**

分享者拿農場的分潤碼貼連結，演算法決定誰看到，路人留言後即離開；質疑來源的留言不到 2%。

成品：[index.html](./index.html)（[線上版](https://wcl-dev.github.io/research-site/content-farm-threads-tw/)）

---

## 這份研究在問什麼

1. 內容農場的連結在 Threads 上是誰在貼、怎麼貼：是一群互相配合的人，還是各自領分潤碼的帳號。
2. 這些貼文碰到什麼樣的人：農場在 Threads 有沒有固定受眾，留言的人是誰、追蹤誰、有沒有質疑來源。

## 主張的邊界

- 不主張任何群的操作者國籍、主機位置，或是否受國家指使。分潤碼證明的是同一套分潤系統，不是同一個人。
- 受眾結論只適用於 Threads；臉書留言區需登入，本研究全程不登入任何平台。
- 按讚與轉發名單自 2026 年 9 月起 Threads 不再回傳，留言者是會說話的少數。

## 個資規則（決定了這個資料夾放什麼）

- **具名**：只有行為類型為「工具化散布」與「站方自營」的 Threads 帳號（共 212 個），它們是公開帳號、有公開的散布行為。清單在成品的附錄 B。
- **不具名**：偶發轉貼帳號、專職轉貼帳號、所有留言的路人。凡列出這些帳號的檔案一律不放；工作紀錄裡出現的一律以「[帳號已隱去]」取代。
- **不放**：原始抓取資料（108 MB，含路人帳號與留言）、留言逐則資料、路人抽樣名單與追蹤名單、候選帳號輸入清單、搜尋引擎原始結果、跨平台帳號盤點表、農場網域清單的內部註記（網域本身見成品的附錄 A）。

## 研究軌（pipeline/）

| 路徑 | 內容 |
|---|---|
| `draft/draft.md` | 報告正文 v1.3；`revisions.md` 是修訂史；`build_html.py` 組出 index.html |
| `method/working-notes.md` | 案件工作紀錄（L0–L4 各層邊界、每一批抓取、訂正）；內部群代號已換成公開群名，非具名帳號已隱去 |
| `method/inputs-notes.md`、`method/crawl-tool-quirks.md` | 輸入檔說明；抓取工具的已知限制（節流、裸網域截斷、讚名單消失、闔上筆電中斷） |
| `method/case.yaml` | 案件中繼資料 |
| `inputs/keywords_*.csv` | 四批網域關鍵字（L0 反搜的輸入） |
| `analysis/sweep_extract.py`、`account_verdicts.py` | L1 貼文抽取與 L2 帳號判定的腳本 |
| `analysis/sweep_b*_summary.json` | 四批反搜的彙總 |
| `analysis/report_cluster_table.csv` | 25 個群的旗艦表資料 |
| `analysis/audience_*_summary.json`、`audience_random_profile.json`、`audience_repliers_profile.json`、`audience_following_summary.json` | L3 留言區與 L4 路人的聚合輪廓（只有聚合數字，沒有個別路人） |
| `analysis/named/verdicts_named.csv` | L2 發文史判定，只保留具名帳號的列（保留 172 列，移除 159 列） |
| `analysis/named/sweep_accounts_named.csv`、`sweep_hits_named.csv` | L1 反搜命中的帳號與貼文，只保留具名帳號（帳號 163 列／貼文 3018 列；移除 548／1636 列） |
| `raw-manifests/*.yaml` | 每一批原始抓取的封存清單（工具版本、檔名、SHA-256），原始檔本身不公開 |

## 工具

Threads Crawl Tool 1.9.x（Keyword／Account／Link 三種模式，不登入）、Facebook Page Plugin（零登入取粉專名稱與追蹤數）、SerpApi 與 Serper（Google 索引）。
