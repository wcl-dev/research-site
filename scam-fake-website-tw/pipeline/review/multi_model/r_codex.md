# Review of scam-fake-website-tw insight_v1 — Codex

**Reviewed on**: 2026-05-21  
**Draft**: projects/scam-fake-website-tw/pipeline/draft/insight_v1.md  
**Sources consulted**: accepted.jsonl (43 records), extracts/ (20 deep-reads), brief.md

## Verdict
- Finding 1: ⚠️ needs tightening
- Finding 2: ⚠️ needs tightening
- Finding 3: ⚠️ needs tightening
- Finding 4: ❌ has gap
- Finding 5: ✅ solid
- Finding 6: ❌ has gap
- Finding 7: ❌ has gap
- Finding 8: ⚠️ needs tightening

Overall: 🟡 needs revision pass

## Per-finding review

### Finding 1 — 為何沒有單一官方「假網站佔比」數字
**Status**: ⚠️  
**L1 citations**: 引用密度整體足夠；未發現 rejected cid 或 invented cid。強證據段 c025/c043/c027 合格。30.52% 只靠 c047 摘要層，draft 有註明，OK。  
**L2 fidelity**: 主結論忠實。c027 extract：「『網路詐騙』這一格佔 89%，但它把假網站、社群假廣告、真平台假賣場、純 LINE 群組全部混在一起。」draft 對應句吻合。  
**L3 counter-evidence**: 有清楚說 30.52% 不是案件占比、1.33% 是 supply-side under-count，沒有隱藏反證。  
**L4 overlooked sources**: c048 是 Whoscall 二手回溯來源，未被正文用來加固 c047；若保留 30.52%，建議同時引用 c048 或在 Source index 說明為何不用。  
**L5 confidence calibration**: Finding confidence「高」略偏高，因本 finding 同時承載 c046/c047 摘要層數字；「無單一官方數字」可高，但「多分母骨架」整段宜拆成高/中。  
**L8 concept-fidelity**: 第三段 scope 標 `{conceptual:A}` 不夠準。Whoscall「網路釣魚網站」可能偏 A，但 c042「詐騙網站下架」是 A∪B/C supply-side，不是 A。屬 scope_overreach。  
**Suggested revision**: 將第三段 scope 改為 `{conceptual:C/A∪B; methodological:empirical-quantitative∩supply-side}`，並把 confidence 拆成「C 軸高、30.52%/1.33% 中」。

### Finding 2 — A 型冒名規模與最常被冒名對象
**Status**: ⚠️  
**L1 citations**: 無 rejected cid；每段有 citation。  
**L2 fidelity**: c023 對 1,466/1,068/393 支撐充分。c042 支撐「元大銀行 5,041 居首」，但 extract 明說其下架對象是粉專/貼文/廣告/LINE 帳號，draft 有 caveat，忠實。  
**L3 counter-evidence**: 有承認 moda 冒名清單不是假冒網域本身，處理誠實。  
**L4 overlooked sources**: c057（財政部假冒網站）只在對照表出現，未進 Finding 2；c058（金管會金融冒名警示）完全未用。若 Finding title 要講「政府／金融／物流／名人」，這兩個是明顯可用但漏掉的 A 型官方補強。  
**L5 confidence calibration**: Confidence「中」合理；三段分別是官方下界、業界偵測量、社群下架清單，無共同分母。  
**L8 concept-fidelity**: 大致 OK；但「最常被冒名對象」容易被讀成全 A 型排名，實際只是 moda 社群下架管道與 Watchmen 類別清單。  
**Suggested revision**: 標題或首句改成「A 型 proxy 與管道別被冒名對象」，避免暗示全台排名。

### Finding 3 — B 型非冒名型詐騙網站規模
**Status**: ⚠️  
**L1 citations**: 引用充分；無 rejected cid。  
**L2 fidelity**: c024 對站次與通報件數支撐準確。c031 extract 對 HOT、亦莊國際、buysemu 支撐 B 型；draft 未把灰色的「麥格理」硬歸 B，這點合格。  
**L3 counter-evidence**: 有承認站次≠獨立站數、純 LINE 群組會稀釋，誠實。  
**L4 overlooked sources**: c033 是 B 型「投資平台網頁」法院佐證，未用；可不必加，因 c030/c031/c032 已足夠。  
**L5 confidence calibration**: 第一段標【強證據】不符合 reviewer 規則：它主要只靠 c024 單一 qs=5 來源。即使來源強，High/強證據要求 ≥3 sources incl. qs≥4。第三段結構限制有 c023/c024/c022 三源，才可強。  
**L8 concept-fidelity**: B scope 合格；第三段雖標 B，但實際是 C 軸方法論（無共同分母），建議加 C。  
**Suggested revision**: 將第一段 tier 從【強證據】降為【爭議中】或補上 c030/c031/c032 作為同段支撐。

### Finding 4 — 假網站在詐騙流程中的角色與生命週期
**Status**: ❌  
**L1 citations**: 基本有 citation；c049 是摘要層且無一手 extract，draft 有標 contested，OK。  
**L2 fidelity**: 有一處 overreach。draft：「此鏈由三個獨立來源交叉確認：……c051。」c051 extract 實際說：「誘導參與假投資」且 caveat 明說「此段未明說最後一定有假投資網站」。  
Draft claim vs extract divergence:  
- Draft:「FB／社群假投資廣告 → 點連結加 LINE → … → 假投資網站註冊」由 c051 交叉確認。  
- Extract c051:「誘導參與假投資」；extract caveat：「未明說最後一定有假投資網站」。  
c030/c031 支撐網站鏈，c051 只支撐社群→LINE→假投資導流，不支撐「網站註冊」。  
**L3 counter-evidence**: 有提「並非所有詐騙都經假網站」，但仍把 c051 用得過滿。  
**L4 overlooked sources**: c059（內政部高額財損趨勢，FB→LINE→詐騙網站 funnel）是更直接的官方 funnel 補強，未用；雖摘要層，但可與 c031 互相支撐。  
**L5 confidence calibration**: Finding confidence「中」合理；但第一段「三個獨立來源交叉確認」需改成「兩個法院來源確認網站，c051 確認前端導流」。  
**L8 concept-fidelity**: A∩B scope 大致 OK；c049 的 61.1%「假冒品牌」偏 A，不應支撐 A∩B 生命週期整體。  
**Suggested revision**: 把 c051 的角色降格為「確認社群/LINE 前端導流」，不要說它確認假網站註冊。

### Finding 5 — 供給端攔阻成效
**Status**: ✅  
**L1 citations**: 引用密度高；無 rejected cid。強證據段有 c029/c037/c022/c040/c042 等 qs≥4 來源。  
**L2 fidelity**: 數字與 extract 對齊。c037：「2025 全年共停止解析 79,039 個網域」；c022：「48,575 列」；c042：「詐騙網站下架 1,621」。draft 忠實且有 supply-side caveat。  
**L3 counter-evidence**: 正確強調不可把攔阻量當受害佔比。  
**L4 overlooked sources**: c038/c039 可補 RPZ 機制背景，但 c037/c029 已足夠；非 cherry-pick。  
**L5 confidence calibration**: 高合理。唯一小點：c061 的 2,822 實源自 c037，不是獨立第二來源；draft 沒有把它當獨立趨勢來源，問題不大。  
**L8 concept-fidelity**: A∩B supply-side 合格；最後 PhishingCheck 段標 A 合格。  
**Suggested revision**: none — finding holds；只需註明 c061 的 2,822 與 c037 同源，不是獨立驗證。

### Finding 6 — 2023–2026 趨勢
**Status**: ❌  
**L1 citations**: 有 citation，但「2021–2022 年約千餘」基期沒有被 c037 extract 直接支撐。  
**L2 fidelity**: 主要問題在 TWNIC 長期基期。  
Draft claim vs extract divergence:  
- Draft:「TWNIC RPZ 攔阻量級由 2021–2022 年約千餘躍升至 2025 年約 8 萬 [c037]。」  
- Extract c037 caveat:「此頁無年對年比較表；2021-2024 基期數字來自 brief reconnaissance 的 deep-research，非本頁。」  
因此 c037 只支撐 2025 年 79,039，不支撐 2021–2022 基期。  
**L3 counter-evidence**: 有承認 2025 回落可能是資料集汰換，誠實。  
**L4 overlooked sources**: c028/c045 是趨勢旁證但非假網站專屬，不加可接受；真正缺的是可引用的 2021–2024 RPZ 基期來源。  
**L5 confidence calibration**: 第一段標【強證據】過高。B 型與 A 型序列強，但 TWNIC「兩個量級成長」目前部分無 citation；整體應維持中。  
**L8 concept-fidelity**: A∩B + supply-side 混在同一趨勢句，容易把偵測/攔阻趨勢讀成詐騙佔比趨勢；需更明確分層。  
**Suggested revision**: 刪除或另尋來源支撐「2021–2022 約千餘」，否則改成「2025 RPZ 攔阻量達 79,039；缺可深讀年對年基期」。

### Finding 7 — 需求端稀釋反證
**Status**: ❌  
**L1 citations**: Finding 本體有 c034/c032/c051/c031；無 rejected cid。  
**L2 fidelity**: 最大錯誤出現在 TL;DR 與 What we don’t know，而非 Finding 7 本段：draft 說「冒名社群貼文也只有約三分之一導向假網站」。c051 extract 只說「3 種導流網址類別」，沒有說三類等量或第（二）類占三分之一。  
Draft claim vs extract divergence:  
- Draft:「冒名社群貼文僅約三分之一導向假網站。」  
- Extract c051:「歸納出 3 種導流網址類別……只有第（二）類是假網站。」  
「三類」不能推成「約三分之一」。這是定量 overreach。  
**L3 counter-evidence**: Finding 7 本身就是 counter-framing，且最後有承認 c034 不是「零假網站」，處理方向正確。  
**L4 overlooked sources**: c035（真平台雅虎奇摩購物盜刷）可補 counter，但 c034/c032 已足夠。  
**L5 confidence calibration**: Confidence「低」合理；但 TL;DR 用 unsupported「三分之一」會讓低證據變成定量結論。  
**L8 concept-fidelity**: c051 是 A 型社群冒名貼文，不是所有 A 型冒名，也不是全部詐騙；draft Finding 7 本體有說清楚，TL;DR 沒有。  
**Suggested revision**: 全文刪除「約三分之一」，改成「三類導流終點中只有一類是假網站，比例未提供」。

### Finding 8 — 資料缺口與替代估計法
**Status**: ⚠️  
**L1 citations**: 前兩段引用足夠；第三段「調查局無公開量化資料」沒有 accepted cid 支撐，且 c060 在 rejected.jsonl，draft 沒有引用 c060，避免了 hard error，但該句可驗證性不足。  
**L2 fidelity**: c025/c043/c027/c023/c024/c022 對「缺媒介別交叉表、無單源覆蓋 A∪B」支撐充分。Scam Tracker c052 是摘要層替代估計工具，draft 有註明。  
**L3 counter-evidence**: 無 accepted source 反駁資料缺口；但「調查局缺席」應明確說是 pipeline search result，不是 source finding。  
**L4 overlooked sources**: c026、c028、c038、c039、c053 都是背景/路由，未用可接受；c048 可作 Whoscall替代估計支撐。  
**L5 confidence calibration**: Overall 中合理；第一段【強證據】合理，第三段【推測】合理但應從正文 finding 改到 gap note。  
**L8 concept-fidelity**: C scope 合格；第二段同時談 A/B，標 C 可接受，因主張是方法論缺口。  
**Suggested revision**: 將「調查局無公開量化資料」移到 What we don’t know，並標「pipeline 未找到，非 accepted source 證明」。

## Structural issues

- L6 brief-question coverage: Q1–Q7 都有覆蓋。最弱的是 Q6：趨勢段部分基期未被可引用 extract 支撐；Q3 有 B 型規模但仍沒有「假投資/網購中多少比例實際透過獨立假網站」的 demand-side 估計，只能明確列為缺口。
- L7 missed gaps: What we don’t know 大體誠實，也有承認 c049/c046 access_blocked / JS-only。缺一個明確 gap：c051 的三類導流沒有比例，不能推「三分之一」。另需補「c037 不支撐 2021–2024 RPZ 基期」這個 citation gap。
- Source integrity: Draft 正文與 source index 未發現 rejected cid；c001/c003/c004/c008/c009/c021 只在 Source index/Dr3 註記出現，未作台灣 empirics，符合 brief。accepted records 43、extract deep-reads 20，counts 正確。

## Summary recommendations

1. 立刻刪除「約三分之一導向假網站」；c051 只支撐「三類導流之一」，不支撐比例。
2. 修正 Finding 6 的 TWNIC 長期趨勢：c037 只支撐 2025，不支撐 2021–2022 基期；找來源或降格。
3. 降低單一來源段落的 tier：Finding 3 第一段、Finding 6 第一段不應標【強證據】。
4. 修正 Finding 4 對 c051 的使用：它支撐社群→LINE 導流，不支撐必然進入假網站註冊。
5. 補強或改寫 A 型「最常被冒名對象」語氣，避免把 moda 社群下架排名誤讀為全台 A 型排名。