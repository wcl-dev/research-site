# Review of scam-fake-website-tw insight_v1 — Claude (Opus 4.7)

**Reviewed on**: 2026-05-21
**Draft**: projects/scam-fake-website-tw/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (43 records), extracts/ (20 deep-reads), brief.md, brief_expanded.yaml, synthesize/themes.jsonl (8 themes)

審查取向：對抗式。本份草稿在方法論紀律上明顯高於一般水準（A/B 拆開、supply/demand 嚴格分離、tier 標註、分母逐層說明都做到了），所以本審查把火力集中在三類弱點：(1) confidence 行的「qs≥4 計數」與實際 quality_score 不符；(2) 少數 L2 數字 fidelity 的細微誇大；(3) 一個被忽略且 load-bearing 的 secondary 來源（c048）未引。

## Verdict

- Finding 1：✅ solid（confidence 行有一處 qs 計數需修，見下）
- Finding 2：⚠️ needs tightening（c042 被當 qs≥4 計入；c058 官方佐證未引）
- Finding 3：✅ solid
- Finding 4：⚠️ needs tightening（96%/24h 外部數字載重過高；c059 官方 funnel 來源未引）
- Finding 5：⚠️ needs tightening（Confidence 行「4 個 qs≥4」實為 3 個；「96.5%」算術錯置）
- Finding 6：✅ solid
- Finding 7：✅ solid（反證處理誠實，counter-of-counter 也寫了）
- Finding 8：✅ solid

Overall：🟢 publishable with minor edits — 無 🚨、無 concept_fidelity_violation、無引用 rejected cid、無 orphan claim。所有 ⚠️ 都是「修 confidence 行的 qs 標示 + 補一個算術 + 補 1–2 個未引官方來源」等級的小修，不需要 re-Drafter。

---

## Per-finding review

### Finding 1 — 為何沒有單一官方「假網站佔比」數字：多分母方法論（Q1）

**Status**: ✅ solid（一處 confidence 行 qs 計數需修）

**L1 citations**：每個事實主張皆有 cite。c025/c043/c027/c044/c046/c047/c042 全部存在於 accepted.jsonl，無一在 rejected.jsonl。c046（165 儀表板 16.2 萬／893 億）已誠實標「依摘要層 sourcing，未經 deep-read 一手驗證」，且 c046 的確是 INDEX 列為 `snippet_status: usable` 的 secondary，標註正確。

**L2 fidelity**：逐句比對。
- 「桃園市警局 2019–2024 六年統計唯一的分類欄是『詐騙手法』」— c025 extract Passage 1 明言「資料集 6 個欄位中分類維度只有『詐騙手法』一欄」，吻合。
- 「2024 年全般刑案 614,800 件，詐欺占 32.14%」— c044 extract Passage 1「114 年全般刑案發生數 61.48 萬件，詐欺占 32.14%」，吻合。
- 「受理詐欺犯罪案件數 2024 年約 198,000 件 [c043]」— c043 extract「114 年詐欺犯罪計約 19.8 萬件」，吻合。**惟年份標示需注意**：c043/c044 extract 內 temporal range 寫「114年 (2024)」，但 114 年是 2025 曆年；extract 自己已採「114=2024」的換算。草稿沿用 extract 的「2024」，與 extract 一致，但若 meta-reviewer 採嚴格曆年口徑，這是 extract 層既有的標示，非草稿新增的錯誤 — 標記給 operator 知悉即可。
- Whoscall 30.52%／35.72%、moda 1,621/122,119=1.33% — 與 c047、c042 extract 完全吻合，且分母限制（「惡意連結」非詐騙案件、moda channel-specific under-count）都明確寫出，這段做得很好。

**L3 counter-evidence**：「Counter-evidence: 無 —— 沒有任何 accepted 來源宣稱存在一個官方的『假網站佔比』單一數字」。spot-check：accepted.jsonl 內無任何來源宣稱單一官方佔比，此陳述成立。

**L4 overlooked sources**：theme t01 的 extract_refs = c025/c027/c043/c044/c042/c047，草稿全數引用，另加 c046。**c048（TechNews 轉述 Whoscall）未引** — 見 Finding 1 第三段引 c047 時。c048 在 accepted（qs=3），其 why_relevant 明寫「traceable secondary recovery of the Whoscall malicious-link composition when the primary blog is JS-blocked」。c047 主頁 JS-only、未一手驗證，c048 正是「可回溯的二手」。草稿在此處（與 Finding 8）只引 c047 單源支撐 30.52%，未引 c048 作為可回溯背書 — 這是本草稿最實質的 L4 缺漏（詳見「結構問題」）。

**L5 confidence calibration**：宣告「高」。三段分屬【強證據】【爭議中】【爭議中】。Finding 整體核心結論「無單一官方數字、官方按手法分類」由 c025(qs=4)/c043(qs=5)/c027(qs=4) 三個獨立官方資料集證實，皆 qs≥4，符合 High 門檻（≥3 來源含 qs≥4）。**惟 Confidence 行末句「多分母骨架的每層分母都有 qs≥4 來源」需修**：第三層分母 165 儀表板 16.2 萬／893 億出自 c046，c046 quality_score=3（gate-capped，JS SPA）。草稿其實在正文已把這層標為「依摘要層 sourcing」並標【爭議中】tier，所以正文是誠實的；不一致的只是 Confidence 行那句「每層分母都有 qs≥4」的概括。屬一句話的修正。

**L8 concept-fidelity**：三段 scope tag 為 `{C}`、`{C}`、`{A}`。對照 theme t01 evidence_scope_distribution `conceptual: {C:5, A:2, B:1}`。`{C}` ⊆ 分布、`{A}` ⊆ 分布（A 有 2 筆）— 全部 subset，✅ 無 overreach、無 violation。geographic 皆 `TW`，t01 含 `TW:6, global:1`，subset OK。

**Suggested revision**：Confidence 行末句改為「多分母骨架前兩層（c044/c043）為 qs5，第三層 165 儀表板分母依 c046 摘要層、已標 contested」；正文第三段引 c047 處加引 c048 作可回溯二手。

### Finding 2 — A 型冒名規模與最常被冒名對象（Q2）

**Status**: ⚠️ needs tightening

**L1 citations**：c023/c050/c042/c031/c032/c057 全部存在於 accepted、無一在 rejected。c050 已標「原 iThome 頁 403，經 Wayback 2025-05-16 快照救回」，c042 已標「rescued 一手 PDF」，標註誠實。

**L2 fidelity**：
- 「moda 165027 累計 1,466 列…假冒類 1,068 列（72.9%）…393 列『偽冒電商一頁式詐騙』」— c023 extract Passage 1 數字完全吻合（1,068/1,466=72.9%、393 列）。
- 「Watchmen 2023 至 2024-04 偵測到『近萬個冒名詐騙網頁』…『逾 300 萬筆冒名電話／簡訊』」— c050 extract Passage 1 吻合，且「不同媒介不可加總」的 caveat 也照搬，good。
- 「最常被仿冒公眾人物前 10 名以元大銀行（5,041 件）居首…台積電居第 9」— c042 extract Passage 2：元大銀行 5,041 居首、台積電 954 居第 9，吻合。
- 「此清單的下架對象是社群平台上的粉專／廣告／帳號，不是假冒網域本身」— c042 extract Passage 2「Why it matters」明言此點，草稿忠實傳達，這是很好的反向誠實。
- 法院實例 BYBITPRO/dowappbybit.com、aliexptwapp.com 冒 AliExpress — c031 extract Passage 1 吻合；假冒富邦／樂天銀行釣魚站 — c032 extract Passage 2 吻合。

**L3 counter-evidence**：「A 型冒名的『下架計數主體』是社群假廣告而非假冒網域（c042），且冒名社群貼文僅約三分之一導向假網站（c051）」。誠實，且這正是 brief 要求的反面錨點。

**L4 overlooked sources**：theme t02 extract_refs = c023/c042/c050/c051/c031/c032，草稿全數引用 + c057。**c058（金管會防詐專區，A 型金融冒名）未引** — c058 在 accepted（qs=3），why_relevant「official FSC warnings on fake-investment impersonation of listed firms/figures — A-type financial impersonation corroboration」。Finding 2 大量談被冒名金融機構（元大、國泰世華、富邦），c058 是一個官方部會（金管會）對「冒名上市公司／名人」的佐證來源，正對題。不引不算 cherry-pick（c050 已涵蓋金融冒名清單），但補一個官方來源能把「金融冒名」從「業界偵測量」升級為「業界+官方雙背書」。屬 nice-to-have，非硬缺漏。

**L5 confidence calibration**：宣告「中」。三段 tier 為【爭議中】【爭議中】【推測】，theme t02 tier_counts `strong:1, contested:2, speculative:3`。A 型規模有兩個獨立 proxy（moda 1,466 為 qs5 一手；Watchmen「近萬」為 c050 qs3、Wayback 救援）。一個 qs5 + 一個 qs3-rescued，且兩者口徑不同 — 宣告「中」是恰當的，沒有 over-claim。✅ calibration 合理。

**L8 concept-fidelity**：三段 scope tag `{A}`、`{A}`、`{A}`。theme t02 evidence_scope_distribution `conceptual: {A:5, B:4, C:2}` — `{A}` ⊆ 分布，✅ subset OK。注意 t02 分布裡 B 有 4 筆，但 Finding 2 三段全標純 `{A}`；這是合理的，因為 Finding 2 只談 A 型，引用的證據（c023 實測≈100% A、c050 冒名報告、c042 冒名清單）確實都是 A-scoped — 沒有用 B 證據去支撐 A 主張。methodological tag `primary-doc`/`empirical-quantitative`/`primary-doc∩case-study` 皆在 t02 分布 `{primary-doc:2, empirical-quantitative:2, case-study:2}` 內，subset OK。

**Suggested revision**：第二段「被冒名對象橫跨六大類」一句後可加引 c058 作官方（金管會）佐證；非必須。

### Finding 3 — B 型非冒名型詐騙網站規模（Q3）

**Status**: ✅ solid

**L1 citations**：c024/c030/c031/c032/c022 全存在於 accepted、無 rejected。

**L2 fidelity**：
- 「站次 2021 年 64、2022 年 4,135、2023 年 11,391…2024 年 17,306，2025 年回落至 12,362；通報件數 2024 高峰 36,755、2025 降至 22,315」— c024 extract Passage 1 數字逐一吻合（64/4,135/11,391/17,306/12,362；件數 36,755/22,315）。
- 三份法院判決自創品牌站名 — c030 extract（zsdsd.com、impvcu.tw、highleve14dc.com、gmb2tw.com.tw、doublecoin.com 五個）、c031 extract（亦莊國際 yzgi.lat、HOT、buysemu.store）、c032 extract（信仲金融、安順、裕隆信貸假貸款站）全部吻合。
- 「沒有任一官方來源同時涵蓋 A∪B 全集且按冒名軸拆分」— c022 extract scope_caveat、c023 extract caveats 都明言此結構限制，草稿忠實。

**L3 counter-evidence**：「『站次』≠ 真實獨立假投資站數，因攻擊者一站多網域輪換」「部分假投資詐騙是純 LINE 群組喊單變體、無獨立網站」。c024 extract caveats 與 c051 extract Passage 3 都支持，誠實。

**L4 overlooked sources**：theme t03 extract_refs = c024/c030/c031/c032，草稿全數引用。**c033（高雄地院 114訴707，B 型法院佐證）未引** — c033 在 accepted（qs=3），INDEX 明說「c030/c031/c032 已充分覆蓋 B 型，深讀邊際效益低」。不引 c033 完全合理，非 cherry-pick。L4 ✅ clean。

**L5 confidence calibration**：宣告「中」。三段 tier【強證據】【爭議中】【強證據】，theme t03 tier_counts `strong:1, contested:3`。B 型規模有一個 qs5 官方逐週序列（c024）+ 3 份 qs4 法院判決一手背書。第一段【強證據】：c024 單一 qs5 來源 — 嚴格按 spec「High = ≥3 sources incl. qs≥4」，單一來源撐【強證據】是偏高的，但這一段的主張是「160055 資料集逐年站次」這個純資料事實（不是因果推論），單一白金資料集足以；草稿整體 Finding 宣告「中」已下修。可接受。⚠️ 微點：第一段 tier【強證據】若嚴格套 spec 應為【爭議中】（單源），但因是 qs5 一手資料集的純事實陳述，影響極小。

**L8 concept-fidelity**：三段 scope tag `{B}`、`{B}`、`{B}`。theme t03 evidence_scope_distribution `conceptual: {B:4, A:1}` — `{B}` ⊆ 分布，✅ subset OK。methodological `primary-doc`/`case-study`/`primary-doc` 在 t03 `{primary-doc:1, case-study:3}` 內，OK。

**Suggested revision**：none — finding holds。（可選：第一段 tier 由【強證據】下修為【爭議中】以對齊「單源」spec，但非必要。）

### Finding 4 — 假網站在詐騙流程中的角色與生命週期（Q4）

**Status**: ⚠️ needs tightening

**L1 citations**：c030/c031/c051/c049 全存在於 accepted、無 rejected。c049 已明標「依摘要層 sourcing，未經 deep-read 一手驗證；趨勢科技頁 403、Wayback 僅得 hub landing」。

**L2 fidelity**：
- 導流鏈「FB／社群假投資廣告 → 點連結加 LINE → 助教邀請 → 假投資網站註冊 → 偽造交易明細 → 儲值匯款」— c031 extract Passage 3（附表二明列「假網站交易明細畫面」）、c030 extract Passage 3（虛擬帳號/超商繳費代碼）、c051 extract Passage 3（FB假廣告→LINE群組→假投資）三來源交叉確認，吻合。
- 「新北地院 111金訴1726 直接認定假投資網站『投資群組隨時更換』」— c030 extract Passage 2 原文「（下稱詐騙群組，投資群組隨時更換）」，吻合。
- 「同一詐騙集團用 fswg.dowappbybit.com 與 gyte.dowappbybit.com 兩個近似網域打不同被害人」— c031 extract Passage 1 確有此兩網址（編號 2 與編號 8），吻合。
- **「96% 詐騙網站於 24 小時內消失、61.1% 民眾看過假冒品牌詐騙網站 [c049]」** — c049 是 INDEX 列 `access_status: 403`、Wayback 僅得 hub landing 的摘要層；數字實際來源是 brief reconnaissance 的 pre-interview deep-research。草稿已標「依摘要層 sourcing、未一手驗證、引用須標 contested」，這點誠實。⚠️ 但 fidelity 風險仍在：這兩個數字**目前在 accepted 證據池內沒有任何一手或可回溯二手背書**（不像 Whoscall 30.52% 至少有 c048 TechNews 可回溯）。c049 extract 自己的 caveat 寫「Wayback 快照僅得 hub landing（無內文）」— 即連 Wayback 都取不到這兩個數字的出處頁。草稿把它放在【爭議中】tier 已是正確處置，但「常被引用的外部數字」這個措辭略微淡化了「此數字在本 pipeline 內完全無法回溯到原文」的嚴重性。

**L3 counter-evidence**：「並非所有詐騙都經過假網站 —— 冒名社群貼文只有約三分之一導向假網站，網購／物流詐騙整類幾乎不用獨立假網站」。誠實，且與 Finding 7 呼應。

**L4 overlooked sources**：theme t04 extract_refs = c030/c031/c051/c023。草稿引 c030/c031/c051，未引 c023（但 c023 的快閃化在 Finding 6 已用，可接受）。**c059（內政部 FB→LINE→詐騙網站 funnel，qs=4）未引** — c059 在 accepted、why_relevant 明寫「official statement of the fake-investment funnel (FB ad→LINE group→fake site)」。Finding 4 的核心主張正是這條 funnel，目前由 c030/c031（法院）+ c051（NGO）三來源支撐，若加 c059 就多一個「官方部會聲明」層級的背書 — INDEX 也明說 c059 的 funnel「已由 c031、c051 雙重一手確認」。不引不致命（三來源已夠），但 c059 是 qs=4 的官方來源且直接對題，比 Finding 2 的 c058 更值得補。屬實質的 L4 小缺漏。

**L5 confidence calibration**：宣告「中」。導流鏈與快閃輪換有 3 個一手來源交叉，confidence 高；但 96%/24h 此一外部載重數字僅靠摘要層，整體下修為「中」。✅ 這個下修邏輯是對的、誠實。

**L8 concept-fidelity**：三段 scope tag `{A∩B}`、`{A∩B}`、`{A}`。theme t04 evidence_scope_distribution `conceptual: {B:3, A:3, C:1}`。`{A∩B}` 視為 {A,B} 子集 ⊆ {A,B,C}，✅ OK。第三段 `{A}`（96%/24h、61.1% 民眾看過假冒品牌站）⊆ 分布，OK — 且趨勢科技數字確實偏 A 型（「假冒品牌詐騙網站」），scope tag 正確。methodological `case-study∩empirical-quantitative` / `case-study` / `empirical-quantitative` 皆在 t04 `{case-study:2, empirical-quantitative:1, primary-doc:1}` 範圍內，OK。

**Suggested revision**：第三段「96%/24h」一句加引 c059 至 Finding 4 第一段 funnel 處作官方背書；並把「常被引用的外部數字」改為「一個本 pipeline 內無法回溯到原文、僅靠 pre-interview 摘要層的外部數字」以更精確地標示其薄弱程度。

### Finding 5 — 供給端攔阻成效（Q5，純 supply-side）

**Status**: ⚠️ needs tightening

**L1 citations**：c029/c037/c022/c042/c040/c061/c054 全存在於 accepted、無 rejected。c054 已標「依摘要層 sourcing」。

**L2 fidelity**：
- 「TWNIC 2025 全年 RPZ 停止解析 79,039 個網域（.tw 844／非 .tw 78,195）；網路釣魚 4,824 件、經認定違法濫用 76,930 件」— c037 extract Passage 1 逐一吻合。
- 「刑事局 4 個月停止解析 48,575 個…金融保險 76.2%／電子商務 17.8%」— c022 extract Passage 1 吻合。
- 「moda 累計（2024-09 至 2025-12）通報 508,193 則、下架 247,071 則」— c040 extract Passage 1 吻合。
- 「98.9% 被停止解析的網域為非 .tw」— c037 extract Structural content「98.9%（78,195/79,039）」，吻合。
- 「Meta 自報 2024-03 至 2025-12 移除約 780 萬則…Meta 已遭裁罰 4 次共 1,850 萬元」— c040 extract Passage 2 吻合。
- **⚠️ 算術錯置**：草稿第三段「下架總量 122,119 件中，『詐騙網站下架』僅 1,621 件（1.33%），**其餘 96.5% 是社群平台內容（Meta 117,845、LINE 1,438、Google 211、TikTok 15）**」。實算：Meta 117,845/122,119 = **96.5%（Meta 單獨）**；Meta+LINE+Google+TikTok 四者合計 = 119,509/122,119 = **97.86%**；扣掉「詐騙網站 1,621」後全部非網站內容 = 98.67%。草稿把「96.5%」這個**Meta 單獨**的比例，安在「Meta+LINE+Google+TikTok 四個平台」這個括號清單上 — 數字與清單不對應。c042 extract Passage 1「Why it matters」原文是精確的：「其餘 96.5% 是社群平台（Meta）」。草稿把「（Meta）」擴寫成四平台清單時遺漏了重算百分比。屬可量化的 fidelity slip，雖不影響「假網站只佔 1.33%」的主結論，但這是一份「以量化骨幹自居、嚴禁無分母 X%」的簡報，數字精度本身就是 deliverable，須修。

**L3 counter-evidence**：「無對立的攔阻量數據；但須強調的反向風險是把攔阻量誤讀為受害佔比」。誠實，且「供給端 vs 需求端落差」獨立一節把這個風險展開得很好。

**L4 overlooked sources**：theme t05 extract_refs = c022/c029/c037/c040/c041/c042/c061，草稿在 Finding 5 引用 c029/c037/c022/c042/c040/c061，未在本 Finding 引 c041（c041 移至 Finding 6 使用，合理）。L4 ✅ clean。

**L5 confidence calibration**：宣告「高」。⚠️ **Confidence 行有 qs 計數錯誤**：原文「攔阻量有 4 個 qs≥4 官方／基礎設施來源（c037/c022/c042/c040）」。實際 quality_score：c037=5、c022=5、c040=4 — 三個 qs≥4；但 **c042 quality_score=3**（accepted.jsonl 內 c042 qs=3，gate-capped；c042 extract 開頭也自標「Quality: qs=3 (gate-capped)」）。所以正確說法是「3 個 qs≥4 來源（c037/c022/c040）+ c042 為 rescued 一手 PDF、qs=3 gate-capped」。Finding 5 的證據其實非常厚實（c037/c022 兩個 qs5 + c029 qs5 法條 + c040 qs4），即使把 c042 移出 qs≥4 計數，宣告「高」依然成立（≥3 來源含 qs≥4 達標）。所以這是「修一個計數標示」而非「降 confidence tier」。但因 brief 要求 tier-tagged 且 multi-model fidelity_level: high，這個 qs 數字錯標必須修 — 它正是 reviewer 該抓的「confidence 行與實際 qs 不符」。

**L8 concept-fidelity**：四段 scope tag `{A∩B}`×3、`{A}`×1。theme t05 evidence_scope_distribution `conceptual: {A:7, B:6, C:2}`。`{A∩B}` ⊆ {A,B}、`{A}` ⊆ 分布，✅ 全部 subset。第四段標 `{A}`（PhishingCheck 釣魚通報）— c061 extract scope 明寫「PhishingCheck 偏 A 型冒名釣魚」，tag 正確。methodological 四段皆 `primary-doc`，t05 `{primary-doc:7}`，完全吻合。

**Suggested revision**：(1) Confidence 行改為「攔阻量有 3 個 qs≥4 來源（c037/c022/c040）+ c042 rescued 一手 PDF（qs=3 gate-capped），制度骨幹有 c029（qs5）」；(2) 第三段「其餘 96.5%」改為「其餘 98.67% 為非獨立網站內容，其中 Meta 單一平台即佔 96.5%」。

### Finding 6 — 2023–2026 趨勢（Q6，⚠ thin cell）

**Status**: ✅ solid

**L1 citations**：c024/c023/c037/c041/c042 全存在於 accepted、無 rejected。

**L2 fidelity**：
- 「moda 假冒電商網域『創建日期』逐年量 2022→2025 由 51 增至 214→517→588」— c023 extract Passage 3 吻合（51/214/517/588）。
- 「TWNIC RPZ 攔阻量級由 2021–2022 約千餘躍升至 2025 約 8 萬」— c037 extract Passage 2 引 brief reconnaissance 基期（2021–2022 攔阻 2,975）+ 本頁 79,039，「兩個量級成長」措辭吻合。
- 「moda 新聞稿稱金融投資及身分冒充類詐騙案件數較高峰期分別下降 97%／94%」— c041 extract Passage 2 吻合，且「基準期不明」caveat 照搬。
- 「金融投資類詐騙廣告掃描數自高峰 77,484 件/週降至期末約 4,650 件/週」— c042 extract Passage 3 吻合。
- 「160055 假投資博弈集 2026-01 起被 176455 取代」— c024 extract caveats 吻合。

**L3 counter-evidence**：「2025 回落可能是真實下降，也可能是資料集汰換造成的更新趨緩 —— 兩種解釋目前無法從 accepted 來源區分」。這是非常誠實的不確定性陳述，正是 brief「Q6 thin cell」應有的處置。

**L4 overlooked sources**：theme t07 extract_refs = c023/c024/c037/c041/c042，草稿全數引用。L4 ✅ clean。

**L5 confidence calibration**：宣告「中」。【強證據】+【推測】。三個縱貫序列（c024/c023/c037 皆 qs≥4，c023=5/c024=5/c037=5）方向一致，但 brief 已標 Q6 為最薄格、趨勢全靠資料列三角導出。宣告「中」恰當 — 沒有因為三個 qs5 來源就 over-claim 成「高」，誠實。✅

**L8 concept-fidelity**：兩段 scope tag `{A∩B}`、`{A∩B}`。theme t07 evidence_scope_distribution `conceptual: {B:5, A:4, C:1}` — `{A∩B}` ⊆ {A,B}，✅ subset OK。methodological 兩段 `primary-doc`，t07 `{primary-doc:5}`，吻合。

**Suggested revision**：none — finding holds。

### Finding 7 — 需求端稀釋反證：相當部分詐騙不經獨立假網站（Q4 caveat）

**Status**: ✅ solid

**L1 citations**：c034/c032/c051/c031 全存在於 accepted、無 rejected。c051 已標「原 iThome 頁 403，經 Wayback 2025-12-12 救回」。

**L2 fidelity**：
- 「臺中地院 114審金易10 判決 8 名被害人全部、無一例外經由真實平台上的假帳號／假冒客服受騙」— c034 extract Passage 1 列出附表 1–8 全為真平台假帳號/假客服路徑，吻合「全部、無一例外」。
- 「高雄地院 114訴432 同案 17 名被害人中，約 4–5 人屬真平台假賣家路徑」— c032 extract Passage 3 + scope_caveat「17 人中約 4-5 人無假網站」，吻合。
- 「數位信任協會把社群冒名貼文導流歸納為三類去處…只有第（二）類是假網站」— c051 extract Passage 2 三類導流網址，吻合，「只有第（二）類是假網站」措辭與 extract 一致。
- ⚠️ 微點：草稿 TL;DR 與 Finding 7 都用「冒名社群貼文只有約三分之一導向假網站」。c051 extract **並未給出「三分之一」這個數字** — extract Passage 2 只說「三類導流去處之一是假網站」，沒有量化成 1/3。「三分之一」是草稿從「三類去處之一」推導的近似（隱含三類等權）。草稿在 Finding 7 第三段把它定位為 caveat、在 What we don't know 也標「冒名社群貼文僅約三分之一導向假網站…這些是 caveat 級證據」，整體沒有當精確數字用；但「三分之一」嚴格說是 drafter 的推算而非 c051 原文。建議改為「三條導流去處之一」或明標「（粗估，假設三類等權）」。

**L3 counter-evidence**：本 Finding 本身就是 counter-framing；難得的是它還寫了 **counter-of-counter**：「反向亦不可過度外推 —— c034 屬網購／物流單一手法類別，不能推論到假投資類；且 c034 偵卷仍有『假新竹物流網站截圖』，嚴格說是『假網站為輔、假客服話術為主』」。c034 extract Structural content + caveats 確有「偵卷證物含假新竹物流網站頁面截圖」「嚴格說此案非零假網站」。這段把雙向誇大都堵住了，是全草稿處理得最謹慎的一段。✅

**L4 overlooked sources**：theme t06 extract_refs = c034/c032/c051，草稿全數引用 + c031（作對照）。theme t06 的 conflicts 欄明確記載 c034 vs c031 在「Q4 是否依賴獨立假網站」的張力，草稿 Finding 7 第三段正是把這個 conflict 顯式寫出並解釋為「按手法分流」，與 themes.jsonl 的 conflict 記錄完全對應。L4 ✅ clean。

**L5 confidence calibration**：宣告「低」。理由「反面證據雖載重，但量少（c034/c032/c051 三件）；它確證『不可外推單一比例』，但本身不足以給出『不用假網站的詐騙佔多少』的數字」。theme t06 tier_counts `contested:2, speculative:1`。宣告「低」恰當 — 草稿沒有因為 c034「8 人全部無假網站」這個強烈表述就把反證 over-claim 成主結論。✅ 誠實。

**L8 concept-fidelity**：三段 scope tag `{C}`、`{A}`、`{C}`。theme t06 evidence_scope_distribution `conceptual: {C:2, B:1, A:1}`。`{C}` ⊆ 分布、`{A}` ⊆ 分布（A 有 1 筆），✅ subset OK。第二段標 `{A}`（c051 社群冒名貼文導流）— c051 extract scope refs `[A, C]`，tag `{A}` 合理。methodological `case-study`/`empirical-quantitative`/`case-study` 在 t06 `{case-study:2, empirical-quantitative:1}` 內，OK。

**Suggested revision**：把「冒名社群貼文只有約三分之一導向假網站」（TL;DR、Finding 7、What we don't know 三處）改為「假網站僅是冒名貼文三條導流去處之一」，或保留「三分之一」但加「（假設三類等權的粗估）」。

### Finding 8 — 資料缺口與替代估計法（Q7，⚠ thin cell）

**Status**: ✅ solid

**L1 citations**：c025/c043/c027/c023/c024/c022/c052/c047 全存在於 accepted、無 rejected。c052 已標「依摘要層 sourcing」。

**L2 fidelity**：
- 「即使有『管道』維度的資料（嘉義市 c027）粒度也只到 channel（網路詐騙 89%）」— c027 extract Passage 1「網路詐騙 2,190（89.0%）」，吻合。
- 「165027 偏 A 型電商、160055 偏 B 型假投資、176455 是產業別非冒名軸」— c023/c024/c022 三個 extract 的 scope_caveat 一致支持，吻合。
- 「法務部調查局：本 pipeline 未找到任何調查局公開出版品或新聞稿含『假網站佔比』的量化內容（Gatekeeper 已標 must_include_skipped）」— 與 brief_expanded.yaml `法務部調查局 fetch_fallback: skip_with_flag` 對應。spot-check rejected.jsonl：c060「法務部調查局 — 最新消息」確在 rejected、c062「法務部調查局反詐騙法治教育電子書」亦在 rejected — 草稿說「未找到可引用的調查局量化資料」與 rejected 池一致，誠實。

**L3 counter-evidence**：「無 —— 此 Finding 的核心（資料缺口）本身就是發現；無 accepted 來源反駁『現行統計缺媒介別交叉表』」。spot-check：accepted 內無任何來源宣稱存在媒介別交叉表，成立。

**L4 overlooked sources**：theme t08 extract_refs = c027/c023/c025/c043，草稿全數引用 + c022/c024/c052/c047。L4 ✅ clean。

**L5 confidence calibration**：宣告「中」。【強證據】+【爭議中】+【推測】。「缺媒介別交叉表」「無單源覆蓋 A∪B」由多個 qs≥4 官方資料集證實（c025=4/c043=5/c027=4/c023=5）— 這部分達 High；但「有哪些替代估計法」一節證據薄（c052 為 qs3 摘要層），整體下修為「中」。✅ 下修邏輯誠實。

**L8 concept-fidelity**：三段 scope tag `{C}`×3。theme t08 evidence_scope_distribution `conceptual: {C:3, A:1, B:1}` — `{C}` ⊆ 分布，✅ subset OK。methodological `primary-doc`/`primary-doc∩empirical-quantitative`/`primary-doc` 在 t08 `{primary-doc:4}` 範圍內（empirical-quantitative 不在 t08 分布內，但第二段 tag 是 `primary-doc∩empirical-quantitative` 的交集 — 交集成分中 primary-doc 在分布內、empirical-quantitative 不在；嚴格說這是一個 `methodological` 維度的輕微 superset。考量第二段引用的 c023/c024/c022 確為 primary-doc 資料集、且引 c047 帶 empirical-quantitative 性質，標 `∩` 反映了混合來源，屬可接受的標示。提請 meta-reviewer 知悉，非須修。）

**Suggested revision**：none — finding holds（第二段 methodological tag 的 `empirical-quantitative` 成分技術上略超 t08 分布，但語意上反映 c047 的引入，可不修。）

---

## Structural issues

### L6 brief-question coverage

逐一對照 brief Q1–Q7：
- Q1（多分母方法論）→ Finding 1 ✅
- Q2（A 型冒名規模、最常被冒名對象）→ Finding 2 ✅
- Q3（B 型非冒名型規模）→ Finding 3 ✅
- Q4（媒介角色、生命週期、快閃化）→ Finding 4 + Finding 7（caveat）✅
- Q5（supply-side 攔阻成效）→ Finding 5 ✅
- Q6（2023–2026 趨勢）→ Finding 6 ✅
- Q7（資料缺口、替代估計法）→ Finding 8 ✅

七題全覆蓋，無結構性遺漏。brief success criteria 逐條檢核：(1) 給出至少 3 個不同分母的可引用區間 — 草稿 What we don't know 列出 4 個（全般刑案 32.14%／詐欺 19.8 萬件／惡意連結釣魚 30.52%／moda 下架 1.33%），每個標分母，✅；(2) A/B 分開測量並對照 — A 型 vs B 型對照表 ✅；(3) 媒介角色/生命週期/攔阻/趨勢全涵蓋 ✅；(4) 每個佔比 tier-tagged + supply/demand 明確分離 —「供給端 vs 需求端落差」獨立一節 ✅；(5) 資料缺口 + 替代估計法 — Finding 8 + 獨立「資料缺口」節 ✅。brief 失敗條件無一觸犯（無無分母 X%、無 A/B 混用、無攔阻量當受害佔比、無忽略真平台假賣場反證、無把國際數據當台灣結論）。

### L7 missed gaps

「What we don't know」7 條，逐一檢核皆為真實 gap、無虛列。已涵蓋的 access_blocked 來源（per INDEX.md）：c049 趨勢科技 403、c046 165 儀表板 JS-only、c047 Whoscall JS SPA、c043/c044 細頁 HTTP 400 — 草稿全部在 What we don't know 或正文 contested 標註中誠實承認。**唯一可補的 gap**：c050（Watchmen「近萬個冒名詐騣網頁」）與 c051（社群冒名貼文百分比）兩個 A 型業界數字皆經 Wayback 救援、非協會原報告全文（c050/c051 extract caveats 都明說「內容是 iThome 新聞報導，非協會原報告全文」）。草稿在引用處標了「經 Wayback 救回」，但 What we don't know 沒有像對 c049 那樣明列「協會兩份報告原文（含完整方法論與分母定義）未取得」這個 gap。Finding 2 的 A 型規模量級相當程度依賴這兩份 Wayback-rescued 的二手新聞稿 — 建議 What we don't know 補一條：「數位信任協會《2024 冒名詐騙報告書》《2025 社群冒名詐騙報告書》原報告全文未取得，A 型業界 proxy（近萬網頁、31%/17% 等百分比）的精確方法論與分母定義依 iThome 二手轉述」。

### 跨 Finding 的來源完整性與 cite 衛生小結

- 草稿所有 cite（c022–c061 區段）逐一比對 accepted.jsonl：**全部存在、無一引用 rejected.jsonl 的 20 個 cid（c002/c005/c006/c007/c010–c020/c055/c056/c060/c062/c063/c011）**。✅ 無硬錯誤。
- 國際學術 c001/c003/c004/c008/c009/c021 — 草稿 What we don't know 明確聲明「未引為台灣 empirics」，且 Source index 未列入。符合 brief「國際數據不作台灣結論」。✅
- **唯一實質 L4 缺漏：c048（TechNews 轉述 Whoscall，accepted、qs=3）未被引用。** c048 的 why_relevant 與 INDEX 都指明它是「c047 的可回溯二手」。草稿在 Finding 1 與 Finding 8 兩處引 c047（30.52%）時，c047 主頁 JS-only、未一手驗證，c048 是 pipeline 內唯一能讓這個載重數字「可回溯」的來源。不引 c048 使 30.52% 表面上像「單一未驗證來源」，實際上 pipeline 是有二手背書的 — 草稿反而把自己的證據說薄了。次要 L4：c059（qs=4 官方 funnel）、c058（qs=3 金管會 A 型佐證）未引，屬 nice-to-have。

## Summary recommendations

1. **修 Finding 5 Confidence 行的 qs 計數**（最高優先，因 multi-model fidelity_level: high 且 brief 要求 tier-tagged）：「4 個 qs≥4 來源（c037/c022/c042/c040）」應為「3 個 qs≥4（c037/c022/c040）+ c042 為 rescued 一手 PDF、qs=3 gate-capped」。同理修 Finding 1 Confidence 行末句「每層分母都有 qs≥4」（第三層 c046 為 qs3 摘要層）。confidence tier 本身（兩處皆「高」/Finding 1「高」）不需降 — 即使移出 c042/c046，仍達「≥3 來源含 qs≥4」門檻；只是行內的 qs 標示須與 accepted.jsonl 的實際 quality_score 一致。

2. **補引 c048 作為 c047（Whoscall 30.52%）的可回溯二手**（Finding 1 第三段、Finding 8 第二段、TL;DR 第二點）。c048 已在 accepted、其存在目的就是「JS-blocked 時可回溯」。同時建議 Finding 4 第一段 funnel 補引 c059（qs=4 官方部會 funnel 聲明）。

3. **修 Finding 5 第三段「96.5%」算術錯置**：「96.5%」是 Meta 單一平台佔比，不是「Meta+LINE+Google+TikTok 四平台」。改為「扣除詐騙網站 1,621（1.33%）後，98.67% 為非獨立網站內容，其中 Meta 單一平台即佔 96.5%」。並將「冒名社群貼文只有約三分之一導向假網站」（TL;DR／Finding 7／What we don't know 三處）改為「假網站僅是冒名貼文三條導流去處之一」或加註「（三類等權的粗估）」— c051 原文未給「1/3」此數字。

4. **（次要）What we don't know 補一條 gap**：數位信任協會兩份冒名詐騙報告原文未取得，A 型業界 proxy（近萬網頁、貸款 31%/投資 17% 等）依 iThome 二手 Wayback 轉述、精確方法論與分母定義不明 — 比照草稿對 c049 的處理標準。

---

**整體**：本草稿方法論紀律扎實（A/B 嚴格分拆、supply/demand 獨立成節、每個百分比附分母、tier 標註、conflict 顯式寫出、reverse-of-counter 也寫了），無 🚨、無 concept_fidelity_violation、無 scope_overreach、無引用 rejected cid、無 orphan claim。所有缺失集中在「confidence 行的 qs 計數與 accepted.jsonl 不符」「一處百分比算術錯置」「一個可回溯二手 c048 漏引」三類小修，皆可在一次 light edit pass 內完成，不需要 re-Drafter。建議 meta-merge verdict：🟢 publishable with minor edits。
