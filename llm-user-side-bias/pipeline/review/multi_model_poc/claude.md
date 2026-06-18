# Review of llm-user-side-bias insight_v2.md（Claude，multi-model PoC）

**Reviewed on**: 2026-05-18
**Draft**: `pipeline/draft/insight_v2.md`
**Sources consulted**: accepted.jsonl（32 條紀錄）、extracts/（17 份深讀 + INDEX.md）、brief.md、synthesize/themes.jsonl、既有 review/review.md（v1 基線審查）
**評審者立場**: 對抗式（assume drafter over-confident），但因 v2 已套用 v1 review 的修正，本次重點是「修正是否徹底」與「殘留弱點」。
**注**: 本文採 v2 的章節編號（一–五），而非標準 Drafter 的 Finding 1/2/...。每節獨立套用 L1–L7；L8 在末尾依條件處理。

---

## 整體裁決（Verdict）

按章節給出單行狀態（v2 沒有採用標準 Findings 切分，因此以章節 + TL;DR 列示）：

- TL;DR：⚠️ 需細部緊縮（一處措辭仍與證據範疇有張力）
- 一、文獻地圖：✅ 大致紮實（v1 OC1/OC2 統計修正已落地）；單點殘留⚠️
- 二、理論錨點 — 框架一（資訊主權）：✅ v1 OC3 修正到位；無新增缺陷
- 二、理論錨點 — 框架二（知識不平等）：✅ v1 OC4/OC5 修正到位
- 三、貢獻陳述：✅ 立論精準，未超出證據
- 四、論述路徑：⚠️ v1 Russia/China 機制修正到位，但 c037 用法仍隱含未盡的概念差（西方左右政治 vs. 國族／地緣政治維度）
- 五、缺口清單：⚠️ 缺口列舉與 themes.jsonl 中 t04 cluster 的實際 accepted 條目數不一致（漏列 c044 等 Q2 epistemic 周邊文獻可用性）

**整體**: 🟢 可以送印（minor edits）— 修正基本到位，殘留為**措辭層級**而非事實層級錯誤。最關鍵的兩個微缺陷是：(1) TL;DR + Section 一「從未延伸至國族身份場景」的措辭與 c011 用 nationality 作為變項存在輕微張力；(2) c037 援引未顯示「PoliTune 測的是西方左右光譜，而非國族／地緣政治維度」此一概念差。皆為單句修補。

---

## 章節審查

### 一、文獻地圖（Literature positioning）

**狀態**: ⚠️ 需細部緊縮

**L1（引用密度）**:
- 全節事實聲明均有 `[cNNN]` 引用，無孤兒事實聲明。
- 已引用 cid 中無一出現在 rejected.jsonl（rejected: c010, c014, c016, c018, c027, c028, c034, c036, c038, c040, c042, c043, c045）— 通過硬性檢查。
- TL;DR 第一條「相同主題、相同語言，不同使用者身份得到不同答案」這一核心 niche claim 引 `[c012, c011, pilot]`，三來源含 c012 (qs=5)、c011 (qs=4)、pilot — 高信心宣稱滿足 ≥3 來源含 qs≥4 的條件。✅

**L2（聲明 vs. 來源忠實度）**:
- 「百川 60.23%、DeepSeek 約 36%、非中國模型 0%」[c001] — 與 c001 extract Passage 1 verbatim 一致。✅
- 「96 個主題類別中 68.75% 達到百分之百拒答率，且跨語言一致——英語拒答率（100%）等於甚至略高於中文（99.57%）」[c003] — 對應 c003 extract Passage 5 verbatim：「66 out of 96 categories (68.75%) result in a 100% censorship rate.」與「Chinese 99.57%; … English 100.00%.」。v1 OC1/OC2 已完整修正。✅
- 「17 個測試模型中有 15 個出現語言偏差，所有 6 個中國源模型全數「不及格」」[c005] — 與 c005 extract verbatim 一致。✅
- 「DeepSeek R1 的思維鏈中找到逐字重複的中共黨國宣傳文字」+「台灣自古以來就是中國領土不可分割的一部分」— 對應 c003 Passage 3：「Taiwan has always been an inalienable part of China's sacred territory since ancient times」。Drafter 把該句歸給 c005 + 引在 c005 段落，但實際 c005 extract Passage 3 也確有相同句的英文翻譯。雙重來源都有支撐，不算違規，但**嚴格說此 verbatim 中文句的原始抓取點是 c003 Figure 2**；可建議在引註後加「亦見 c003」以加強。⚠️（小）
- 「Guey 等人（2025）以 19,712 個雙語提示測試 11 個模型」[c007] — 與 INDEX.md 中 c007 描述「11 LLMs, 19,712 prompts」一致。✅
- 「Zhou & Zhang（2024）在 Nature Scientific Reports 以 qs=5 的同行評審標準記錄了 GPT 雙語模型中的系統性政治框架差異」[c008] — c008 extract Passage 1–4 verbatim 支撐。**但 v2 在正文中把 qs 視為「同行評審標準」是 pipeline 內部分級，不是 Nature SR 的審稿術語**；對外部讀者語意可能造成混淆。此備忘錄為內部使用，OK；對外公開時建議改為「同行評審期刊」即可。⚠️（措辭，極小）

**L3（反證誠實度）**:
- v2 在文末 Section 一加了：「c008 與 c005 記錄的「語言作為觸發器」機制（模型依提問語言給出不同內容）在概念上與先導研究的「宣告身份作為觸發器」… 有所區別」— 充分坦承並交叉到「缺口六」。✅
- 但**仍未明確指出 c011 (Amiri-Margavi 2026) 已將 nationality 作為測試變項**（雖在 career-advice 任務上）。draft 一律把 c011 與 c012/c013 並列為「全部在美國中心的人口統計或意識形態身份框架內操作」 — c011 extract caveat 明說 nationality 是三個身份變項之一。「全部」字眼在嚴格意義上把 c011 也歸入美國中心，與 c011 abstract 標示「varying identity attributes along age, gender, **and nationality**」有張力。⚠️
  - Draft 原文（Section 一）：「但**這些研究全部在美國中心的人口統計或意識形態身份框架內操作**，從未測試中國源模型上的國族身份×地緣政治敏感主題組合」
  - c011 extract caveat verbatim：「Nationality is one of three identity variables tested — but specific nationality-level findings not detailed in accessible abstract.」
  - 兩者語意衝突的範圍：v2 強調的 niche（**中國源模型 × 國族身份 × 地緣政治主題**）在 c011 缺乏「中國源模型」和「地緣政治主題」這兩項之下仍成立，但「從未測試國族身份」這個前提語句太強。

**L4（被忽略的可用來源）**:
- t01 cluster 中所有 extracted 來源（c002, c011, c012, c013）已全數引用；t04 cluster（c029, c033）也全引。✅
- t03 cluster 中 c022 (qs=4 「Operationalizes information sovereignty threats in concrete LLM deployment practices」) 雖在 INDEX 因 access_blocked SKIP，但其 abstract-level 訊息可以用以強化 Section 二，draft 未提及 — 屬可接受的選擇，因為 v1 review 並未要求補入。
- 不額外加分（避免 over-weighting L4）。

**L5（信心校準）**:
- Section 末段「中國源模型系統性審查的背景前提」高信心 — 由 c001, c003, c004, c005, c007 五來源含多個 qs≥4/5 支撐，符合 ≥3 來源含 qs≥4 的「高」門檻。✅

**L6（brief 問題涵蓋）**: brief Priority 1（empty niche）由 Section 一充分對應。✅

**L7（"What we don't know" vs 實際缺口）**: 缺口六已加入語言觸發 vs. 身份觸發的理論區分（v1 ST6 對應）— 處理到位。✅

**建議單行修補**:
- 將「但這些研究全部在美國中心的人口統計或意識形態身份框架內操作」改為「但這些研究的身份變項聚焦於人口統計或意識形態，c011 雖將 nationality 作為變項但任務為職涯建議，**從未在中國源模型 × 國族身份 × 地緣政治敏感主題的組合上同時測試**。」

---

### 二、理論錨點 — 框架一（資訊主權 informational sovereignty）

**狀態**: ✅ 紮實

**L1**: 全節事實聲明均有引用。c021 已正確標示「全文不可及，以下依摘要引用」。✅

**L2**:
- v1 OC3 critical issue（c021 三概念括弧定義）已**完全移除**。v2 改為「與資料主權有所區分」單一摘要可確認的區別，並加註解說明「論文是否進一步區分數位主權及其具體定義，有待全文確認」。對照 c021 extract「Drafter MUST NOT cite specific passages from this paper beyond the abstract」的紅線 — v2 不再越線。✅
- c023 三支柱（立法/技術/文化）— 與 c023 extract Passage 2 verbatim 一致。✅
- c023「能夠識別與政治敏感話題相關的隱性暗示或隱喻」— 對應 c023 Passage 3：「capable of identifying not only explicit violations, but hidden hints or metaphors related to politically sensitive topics」 — 中文是準確的意譯。✅
- c041「每年超過 15 億美元的宣傳投入」+「四個「國家重點實驗室」」— v1 已 VERIFIED，v2 沿用。✅
- c037 PoliTune「政治意識形態對齊可以透過參數高效微調（PEFT）以極低成本嵌入模型」— c037 Passage 1+2 verbatim 支撐「PEFT enables efficient ideological alignment」。✅
- **但**：c037 extract caveat 明確指出「Paper uses Western political dimensions (left-right ideology) not geopolitical/national dimensions — Drafter must make the inferential extension explicit」。v2 在此段加了「c037 的研究確立了「如何做到」的技術可行性，而非直接證明中國開發者使用了這套特定技術」— 處理了「中國開發者是否真的使用」的問題，但**未處理 PoliTune 測的是西方左右光譜、不是地緣政治／國族維度**這一概念維度落差。維度不同等於把工具從 A 領域推論到 B 領域，需另一層 caveat。⚠️
- c023 三支柱 → 先導研究合規/合宜映射 — v2 已加入「此為本研究的詮釋性論點，而非 c023 直接針對 LLM 的陳述」（對應 v1 ST3）。✅

**L3**: v1 review SL1（c021 access blocked）— v2 充分標示 ✅。可靠的反證來源未發現。

**L4**: c022（qs=4，operationalizes information sovereignty threats in concrete LLM deployment practices）摘要可用但未引用。屬可接受（INDEX SKIP；非 critical）。

**L5**: 信心分佈表 c021/「資訊主權」標「中」、註明「取得 c021 全文後升至高」— 校準合理。✅

**L6**: brief Priority 2（theoretical framework — informational sovereignty）覆蓋。✅

**L7**: 缺口二（c021 全文不可及）誠實列出。✅

**建議單行修補**:
- 在 c037 段落末尾加：「另須注意，PoliTune 操作的是西方左右光譜的政治對齊，本研究將其推論至國族／地緣政治維度屬類比延伸而非直接證據。」

---

### 二、理論錨點 — 框架二（知識不平等 epistemic injustice）

**狀態**: ✅ 紮實

**L1**: 全節引用密度合適。

**L2**:
- v1 OC4 critical issue（c029 杜撰引言「特別在多語境下，知識不平等從資訊取用差異中浮現」）已**完全移除**。v2 改為「Kay、Kasirzadeh 與 Mohamed（AAAI AIES 2024）識別了生成式演算法知識不平等的四個維度，其中「存取不平等」（access injustice）在多語言脈絡中尤其相關 [c029]」— 對應 c029 Passage 2、3 verbatim。✅
- v1 OC5（c033 epistemicide 延伸）— v2 加入限制語：「此概念原指去殖民學術脈絡中的普遍知識壓制；本研究將其延伸至國族身份觸發的歷史知識存取場景，是作者的詮釋性延伸，而非 c033 的直接論點」。對應 c033 extract caveat「Hermeneutical erasure concept focuses on suppression of non-Western epistemologies broadly — the pilot's case is more specific」。✅
- c020 Bang「內容/風格區分框架」用以詮釋「合規」vs.「合宜」— 對應 c020 在 INDEX/themes 中的定位（「lexical polarity as style bias signal」）。✅

**L3**: 無明顯反證遺漏。

**L4**: 此處可挑剔的是：theme t04 的 evidence_scope_distribution 顯示僅有 algorithmic_discrimination cluster 兩個來源（c029, c033），確實只有兩篇 — 但 **accepted.jsonl 中 Q2/epistemic 標籤** 另有 c030, c031, c032, c044（全因 access_blocked 被 SKIP，未生成 extract）。draft Section 五「缺口三」說「t04「知識不平等」主題僅有兩篇文獻」— 嚴格意義下與 themes.jsonl 一致，但**未說明 accepted 集中其實存在 4 篇周邊 Q2 epistemic 文獻只是 deep-read 被跳過**。對重新跑 pipeline 的 operator 來說這是一個有用的資訊。⚠️（屬 Section 五的小修補）

**L5**: 「知識不平等」標「中」信心 — 校準合理（兩篇 commentary 來源，無量化實證）。✅

**L6**: brief Priority 2（epistemic injustice）覆蓋。✅

**L7**: 缺口三（兩篇均為理論性）誠實列出。

---

### 三、貢獻陳述（Contribution Statement）

**狀態**: ✅ 立論精準

**L1**: 此章節為合成性陳述，引用 c009、c001、c003 等回顧主張，密度適當。
**L2**: 「Yadav 等人（2025）提供了「安全行為 vs. 審查行為」的概念區分工具」[c009] — 對應 c009 Passage 1 + 3 verbatim 支撐。✅
**L3**: 無反證遺漏。
**L4**: v1 OS4 已修正（c009 整合至 Section 二與三）。✅
**L5**: 未做信心宣稱（合成貢獻語句）— 無校準爭議。
**L6**: brief 三個 Priority 在此章節做收束陳述。
**L7**: 不涉及缺口列舉。

**單行建議**: 無 — 此章節已乾淨收束。

---

### 四、論述路徑（Argument Path）

**狀態**: ⚠️ 需細部緊縮

**L1**: 各步驟均有引用。

**L2**:
- 步驟二「96 個主題類別中 68.75% 達到百分之百拒答率 [c003]」— v1 OC1 critical 修正落地。✅
- 步驟二「審計研究確認模型「知道答案但刻意不輸出」[c004, c015]」— c004 Passage 3（CoT 機制）+ c015（獨立 elicitation 收斂佐證）。✅
- 步驟三「Atlantic Council… 每年超過 15 億美元的話語投射體系 [c041]」— c041 verbatim ✅
- 步驟三「「俄羅斯正在以類似目標、不同機制（訓練資料投毒，而非對齊微調）滲透 AI 資訊生態」的平行案例 [c035]」— v1 review L3 critical 修正落地，正確區分機制。✅
- 步驟四 c029/c033 — 已在 Section 二建立，回扣使用 OK。✅
- 步驟五「Freedom House 72 國記錄 [c039，注：全文不可及，以摘要層引用]」— v1 SL2 邊界內，且 v2 顯式加註，誠實。✅

**L3**: c037 段落（Section 二）已處理「設計可行 ≠ 中國開發者使用」；Section 四不需重複，但需注意 PoliTune 維度落差（已於 Section 二建議補入）。

**L4**: 步驟三 Gary King 標 `[anchor: gary_king]` — 為未在 accepted 集的錨論文。v2 維持「歷史比較作為開放問題」的描述（與 brief 一致），未過度宣稱。✅

**L5**: 此章節為敘事結構建議，未做信心分級，無校準爭議。

**L6**: 此章節對應 brief Priority 3（validation）的論述操作化，覆蓋。

**L7**: c039、anchor literature 的限制已標。✅

**建議單行修補**: 已在 Section 二中提到 PoliTune 維度落差的修補；Section 四無新獨立修補。

---

### 五、缺口清單（What we don't know）

**狀態**: ⚠️ 細項可加

**L1**: 缺口列舉本身不需高密度引用，引用密度恰當。

**L2**: 缺口陳述本身為對 pipeline 內部狀態的回顧，無 source-fidelity 風險。

**L3**: 無反證遺漏。

**L4 / L7 — 主要缺漏**:
- 缺口三說「t04 「知識不平等」主題僅有兩篇文獻」 — 與 themes.jsonl 一致，但**accepted.jsonl 中另有 4 個 access_blocked 的 Q2 epistemic 群來源（c030, c031, c032, c044）**，operator 若取得任一者全文，可顯著加強知識不平等框架的實證／法規面（c044 即「Human rights law framing of state/corporate AI deployment obligations」）。建議在缺口三加一句說明「accepted 集中尚有 4 篇 epistemic 群來源因 access_blocked 而未 deep-read，operator 取得全文後可補入」。⚠️（小）
- INDEX.md「Operator overrides needed」中第 3 項「c006 (Urman & Makhortykh 2024)」被標為「Notable qs=4 skip… directly parallel design to the pilot」 — v1 review ST2 已點過。v2 Section 五未列出 c006 作為待補來源。⚠️（與「empty niche」negative existence claim 直接相關，建議加入缺口列舉）

**L5**: 缺口分級隱含於信心分佈表，校準合理。

**L6**: 缺口列舉涵蓋三個 brief Priority 的不確定性。

**單行建議**:
- 在缺口三末尾加：「accepted 集中尚有 c030/c031/c032/c044 等 4 篇 Q2 epistemic 群來源因 access_blocked 而未 deep-read；operator 取得任一者全文可補強框架。」
- 新增缺口七：「c006（Urman & Makhortykh 2024 Telematics and Informatics）的跨語言 ChatGPT/Gemini Russia 主題守門研究與先導研究設計直接平行，但 Springer 付費牆封鎖；operator 取得後可作為「empty niche」negative existence claim 的最後檢驗。」

---

### TL;DR — 高層審查（L1–L7 概覽）

**狀態**: ⚠️ 一處措辭

- L1：5 個 bullet 均有引用，且 niche claim 三來源含 qs≥5（c012）— 高信心門檻達標。
- L2：「Gemini IP 驅動詞彙差異（單點觀測，尚待確認）」— v1 OC2 補入。✅；「相同主題、相同語言，不同使用者身份得到不同答案」對應 brief.md 與 pilot 內部設計，符合。
- L3：bullet 3「支撐這一機制的學術先例存在，但從未延伸至地緣政治或國族身份場景」 — 嚴格說 c011 已將 nationality 列為變項（但於 career advice 任務）。「從未延伸至地緣政治」成立；「從未延伸至**國族身份**場景」需要更精確的措辭。⚠️ 與 Section 一 L3 同源缺陷。
- L5：bullet 5「大規模實證研究已充分確立「中國源模型表現出系統性親中立場」這一背景前提」高信心 — 五來源含 qs=5 多篇，校準合理。✅

**單行建議**:
- bullet 3 改為「支撐這一機制的學術先例存在（含已將 nationality 作為變項的 c011），但從未在中國源模型 × 國族身份 × 地緣政治敏感主題的組合上同時測試 [c012, c013, c011]」。

---

## L8 — 概念忠實度（Conceptual Fidelity）

**條件檢查**: themes.jsonl **帶有** `evidence_scope_distribution`（5 個 themes 全數標註，例如 t02 `conceptual: {existing_llm_bias_studies:7, geopolitical_frameworks:2, identity_trigger_gap:1}, geographic: {CN:4, US:4, TW:2}` 等）— 因此 L8 啟動條件滿足。

**但 Drafter 採用了 Dr1 格式（research positioning memo，章節一–五）**，並未使用 Dr2 的 `**{<scope>}**` 段落標籤契約。state.yaml `draft.notes` 明確記載：

> "Standard Dr1/Dr2 tier-tagging and scope-tagging were not applied — the document type (positioning memo) uses sections 一-五 rather than the standard Findings/Confidence/Counter-evidence structure."

依 reviewer.md L8 規格：
> "For paragraphs WITHOUT a scope tag when one is expected (theme has evidence_scope_distribution but Drafter omitted), flag as `missing_scope_tag`"

機械上，整份 v2 都應該觸發 `missing_scope_tag`。但這是 **document-type 層級的決策**（operator 接受了 positioning-memo 格式），不是 Drafter 違規。因此本 reviewer 採取**語義版 L8**：抽樣抽查 v2 段落的 implicit scope 是否與對應 theme 的 evidence_scope_distribution 一致。

### 語義版抽樣（L8 lite）

- **Section 一 vs. t02**: t02 evidence_scope_distribution `geographic: {CN:4, US:4, TW:2}`。Section 一論述聚焦於中國源 LLM + 中英雙語 + 台灣，與 theme 證據範疇一致（CN+US+TW）。**無 scope overreach**。✅
- **Section 二框架一 vs. t03**: t03 evidence_scope_distribution `geographic: {CN:3, global:2}, conceptual: {geopolitical_frameworks:5}`。Section 二論述明確聚焦 CN（三支柱）+ 一段對俄羅斯（global）。範疇相符。**無 overreach**。✅
- **Section 二框架二 vs. t04**: t04 evidence_scope_distribution `conceptual: {algorithmic_discrimination:2}, methodological: {commentary:2}`。Section 二 framework 2 將理論延伸至台灣 228 場景，並**明確標示**為「作者的詮釋性延伸，而非 c033 的直接論點」— Drafter 自己提示了延伸。屬於受控的 scope extension。⚠️（mild — 但已自我標示）
- **Section 三 vs. t01 + t02 + t05**: 貢獻陳述是合成性，跨 themes 引用。t01 evidence_scope `conceptual: {identity_trigger_gap:4}` 與貢獻陳述中「將兩者交叉」的論述一致。**無 overreach**。✅
- **Section 四 vs. t05 + cross-cluster**: 採用 t05 的 cross-cluster 證據（geographic: CN, US, TW, global），與第五步「普世性與在地性」收束一致。**無 overreach**。✅

**L8 結論**: 雖然 v2 未採 Dr2 段落 scope-tagging 契約（`missing_scope_tag` 機械上觸發），但**語義版 scope 對應整體一致**，且唯一一處 conceptual scope 延伸（c033 epistemicide → 台灣 228）已自我標示。**未發現 `concept_fidelity_violation` 或硬性 `scope_overreach`**。

唯一語義邊緣案例：c037（PoliTune）evidence_scope `conceptual: {geopolitical_frameworks}` 但 c037 extract caveat 寫「Western political dimensions (left-right ideology) not geopolitical/national dimensions」 — 嚴格說 c037 自身的 conceptual scope 應為「演算法／意識形態對齊技術可行性」而非「geopolitical_frameworks」。這是 **Synthesizer 層級**的 evidence_scope 標籤可能偏鬆，而非 Drafter 的違規；但 Drafter 在 Section 二把 c037 用作「政策選擇可行性」的證據時，可加一句註記維度落差（已在前面建議）。

---

## 結構性議題（跨章節）

- **L6 brief-question 全覆蓋**: brief 三個 Priority（empty niche、theoretical framework、validation）全部由 v2 涵蓋。✅
- **L7 "What we don't know" 額外缺口**:
  - c006 Urman & Makhortykh 2024 跨語言守門研究 — v1 review ST2 已點過，v2 缺口列舉未納入。
  - c030/c031/c032/c044 等 Q2 epistemic 群 access_blocked 來源 — v2 未在缺口列舉中提及其潛在補強價值。
- **access_blocked 對信心的影響**: c021、c039 已在信心分佈表中標「中」並提出「取得全文後升至高」的條件 — 處理到位。✅
- **anchor literature**: Waight 2026、Samokhodskyi 2026、Gary King 仍未在 accepted 集中。v2 已用 `[anchor:]` 顯式標示且在缺口一充分坦承。✅
- **Pilot status caveat**: TL;DR 與 Section 一已加「30 格實驗，未發表、未同行評審，結果屬假說生成性質」 — v1 ST1 處理到位。✅

---

## 摘要建議（Summary Recommendations，按優先順序）

1. **（最高優先）措辭緊縮 — Section 一 + TL;DR 「美國中心 / 從未延伸至國族身份」**: c011 已將 nationality 作為變項；建議改為「c011 雖將 nationality 作為變項但任務為職涯建議，從未在中國源模型 × 國族身份 × 地緣政治敏感主題的組合上同時測試」。維護 niche claim 的同時更精準對應證據。
2. **（中度優先）Section 二 c037 增補維度落差 caveat**: 在 PoliTune 段落末尾加一句「另須注意，PoliTune 操作的是西方左右光譜的政治對齊，本研究將其推論至國族／地緣政治維度屬類比延伸而非直接證據」。
3. **（低優先）Section 五缺口列舉補充**:
   - 缺口三末尾加註 c030/c031/c032/c044 等 access_blocked Q2 epistemic 群來源可作為補強候選。
   - 新增缺口七：c006 Urman & Makhortykh 2024 為跨語言 ChatGPT/Gemini Russia 主題守門研究，設計與先導研究直接平行，operator 取得後可進一步檢驗 empty niche claim。
4. **（極低優先）措辭微調**: TL;DR/Section 一引述「Nature Scientific Reports 以 qs=5 的同行評審標準」— qs=5 為 pipeline 內部分級而非期刊用語；對外公開時改為「同行評審期刊」即可。

---

## 重跑 Drafter 的指引（如需）

若 operator 決定再跑一次 Drafter：

- **Critical 議題回饋**: 無 critical（v1 的 OC1/OC3/OC4/OC5 已全數修正落地）。
- **Substantive 議題回饋**: 上述建議 1 與 2（措辭緊縮 c011 nationality 變項地位、c037 維度落差）。
- **可優先 deep-read 的來源**: c006 Urman & Makhortykh 2024（若 operator 取得 Springer 全文）— 為當前 niche claim 的最後檢驗來源。
- **brief 問題是否需重述**: 否 — brief 本身無問題；殘留缺陷源於執行措辭而非 brief 設計。

---

*本 review 為 multi-model PoC 一環，未更新 state.yaml 與 handoff_log.jsonl，亦不覆蓋既有 review/review.md。輸出僅寫於本檔案。*
