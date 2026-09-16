四批關鍵字檔（2026-09-05），label＝registry cluster id。來源：registry.yaml 全部群扣除 CASE-002／003 已搜域。
`accounts_serp_candidates_r2.csv`：Google 索引命中中「摘要含農場連結 ≥2 篇」或「跨 ≥2 群」的 Threads 帳號（扣除第三層排除與已抓過發文史者），第二層 Account 模式輸入（2026-09-05）。
`accounts_serp_candidates_r2b.csv`：R2 第一次未回傳的 14 帳號中，扣除 3 個媒體（排除 A）與 1 個已私人／刪除（[帳號已隱去]）後的 10 個補跑（2026-09-07）。
- `accounts_kw_b1_r3a.csv`／`accounts_kw_b1_r3b.csv`（2026-09-08）：Keyword b1 驗過連結 ≥2 篇、未抓過發文史的 85 帳號，依篇數拆兩天跑 Account 模式；tag `kw_b1_r3|<群>`。
- `accounts_kw_b2_r3.csv`（2026-09-08）：Keyword b2 驗過連結 ≥2 篇、未抓過發文史且不在 b1 r3 名單的 21 帳號；tag `kw_b2_r3|<群>`。
- `keywords_b4_domains_only.csv`（2026-09-08）：b4 去掉 7 個 ref-groups 集團名條目後的 64 個網域，Threads Keyword 模式實際用這份；集團名條目改由人工或搜尋引擎處理。
- `accounts_kw_b4_r3.csv`（2026-09-09）：Keyword b4 驗過連結 ≥2 篇、未抓過發文史的 27 帳號；越南／南亞向為主，優先度最低。
- `links_audience_pilot.csv`（2026-09-09）：受眾試點，Link 模式輸入。台灣向 7 群各 ≤10 篇驗過連結的母文（讚數 10–3,000，留言優先，每群至少 6 個不同帳號），共 43 篇；第一筆為 eatmary2020 近期貼文（quirks §3）。樣本明細在 analysis/audience_pilot_sample.csv。
- `accounts_audience_repliers.csv`（2026-09-09）：受眾試點的回覆者分層抽樣（6 群各 ≤15 個，優先有中文文字的），90 個，Account 模式取所在地／註冊月／簡介；★這些是一般民眾，資料只放 farm-registry、只講輪廓不點名。
- ~~`links_audience_full.csv`~~（2026-09-09，作廢）：未分層的 563 篇全量，改用下面的 v2。
- `links_audience_v2.csv`（2026-09-09）：受眾研究正式樣本，Link 模式輸入，依盤點表「行為類型」分層：站方自營每帳號前 15 篇（51）、專職轉貼每帳號前 3 篇（38）、偶發轉貼有留言或 ≥10 讚者全取（113）、工具化散布最活躍 30 帳號各 2 篇當對照（42），共 244 篇（40 篇與試點重疊，補抓讚名單）。
  設定：activity_max_items 1000（讚 >1,000 的只有 5 篇）、comment_scroll_rounds 5。第一筆同試點。明細與分層標籤在 analysis/audience_v2_sample.csv。
- `links_audience_v2_remaining.csv`（2026-09-09）：v2 在第 193 篇（enews.tw 19,600 讚那篇）卡住三小時後保全暫存，剩下 50 篇＋第一筆 eatmary 驗證用；19,600 讚那篇排除（讚名單拉不完會掛住，quirks §2）。
- `accounts_audience_v2_repliers.csv`／`accounts_audience_all.csv`（2026-09-09）：受眾 v2 回覆者四分層各 25（100），與試點 90 合併去重為 190 個，Account 模式 post_num 30；一般民眾，只講輪廓不點名。
- `accounts_audience_all_rerun.csv`（2026-09-10）：上一輪第 133 個起瀏覽器關閉未回傳的 58 個回覆者（試點六群），設定同前。
- `accounts_kw_b3_r3.csv`、`accounts_r3_session1.csv`…（2026-09-10）：b3 第二層名單；r3 五份合併去重後依篇數拆成每檔 ≤120 的 session，供 Account 模式核實（post_num 100、追蹤名單關、skip_if_over 1000）。
- `accounts_r3_session2_rerun.csv`（2026-09-11）：session2 因合蓋未回傳的 12 個，設定同前。
- `accounts_r3_session3.csv`（2026-09-11）：盤點表裡證據層級 2、行為類型為工具化或專職、但從未跑過 Account 模式的帳號（多為 CASE-003 dsawjk 群 R1、CASE-002 picread 群），L2 邊界的最後一批；設定同前。
- `accounts_audience_random_session1.csv`／`session2.csv`（2026-09-14）：L4 分層隨機 300（實得 250，扣已抓 82 → 168）的 Account 模式輸入，各 84；post_num 30、crawl_following 開、skip_if_over 2000。
