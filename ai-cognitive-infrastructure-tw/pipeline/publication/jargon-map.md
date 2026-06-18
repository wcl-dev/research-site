# jargon transformation map (audit trail)

What internal pipeline term → what lay-reader term in `publication/draft.md`.

## Cluster 1 · chain-link ontology (the big one for this project)
| pipeline | publication |
|---|---|
| L1 | 第一環：價格與採用（「低價 → 採用」）|
| L2 | 第二環：AI 成為資訊入口 |
| L3 | 第三環：模型輸出的立場框架 |
| L4 (overall) | 第四環：框架會不會放大成社會層的認知 |
| L4a | 第四環第一步：輸出會不會同質化 |
| L4b | 第四環第二步：模型能不能改變個人信念 |
| L4c | 第四環第三步：放大成社會層級認知 |
| L4b→L4c break | 「從『能說服個人』到『重構社會認知』之間斷裂」|
| FW (frameworks cluster) | 折入「政策結論」與「資訊入口」段，不單獨命名 |
| CE (counter-evidence cluster) | 「為什麼這份報告不能被讀成反中警報」一節 |
| 載重連結 / load-bearing link | 「最脆弱的那一環」/「承重點」|
| containment | 「只能證明…，不能被偷渡成…」(改寫，不用術語) |
| directional artifact | 「方向性錯覺」|

## Cluster 2 · pipeline workflow refs
| pipeline | publication |
|---|---|
| Finding 1–6 / 主題 t01–t09 | noun-led 章節標題（刪 F-no 與 t-id）|
| cNNN cid | [1]–[30]（見 cid-citation-map.md）|
| 「依摘要層 sourcing，未經 deep-read 一手驗證」| 「(二手摘要)」/「(此筆為二手摘要，未取得原文逐一核對)」|
| partial_counter_framing (single_answer_not_systemic_effect) | 改寫為「缺席加上限」的白話解釋，刪術語 |
| brief / spec §6 | 「原始說法」/「本研究的自我設限」(不顯示 §6) |
| handling_protocol | 刪除（折入「僅作類比」的 inline 提醒）|

## Cluster 3 · tier-tags → prose hedges
| pipeline | publication |
|---|---|
| **[strong]** | 直述 + anchor-to-evidence 語氣（「資料顯示」「作者明文寫」「已被嚴謹證明」）|
| **[contested]** | inline hedge（「仍有爭議」「把握偏低」「兩者並陳，不選邊」）|
| **[speculative]** | 明文標注推測（「沒有任何直接證據」「是推測，不是證據」「刻意得出的發現」）|
| Confidence: high/medium/low | 改寫為每段末的引述塊「這一環的把握度：高／中等／偏低」|
| Counter-evidence: … | 折入正文 prose（保留實質，刪標籤）|

## Cluster 4 · process metadata (deleted)
- `Insight Draft v1` 標題後綴 → 刪
- 全部 `<!-- {conceptual:…; methodological:…} -->` scope 註解 → 刪
- qs=4/qs=5 quality score → 刪
- 主題 id（t01–t09）→ 刪

## Cluster 5 · English jargon → 中文
| pipeline | publication |
|---|---|
| abliteration | 「去對齊（abliteration，一種移除模型內建拒答與自我審查機制的技術）」首次解釋 |
| RLHF | 「以人類回饋微調模型（RLHF）」首次解釋 |
| framing (n.) | 「立場框架」/「說法」/「角度」(依 context 變化) |
| paywall-asymmetry | 「取得難易度的經濟學解釋」/「躲在付費牆後、封鎖爬蟲」|
| generative monoculture | 「生成式單一文化」|
| longitudinal | 「長期追蹤」|
| Observatory | 「觀測站」|
| RCT / 隨機實驗 | 「隨機實驗」|

## Cluster 6 · acronym gloss (first use)
- LLM → 「大型語言模型」(全文多用「模型」「語言模型」避免縮寫堆疊)
- RLHF → 首次「以人類回饋微調模型（RLHF）」
- abliteration → 首次括號解釋（見上）

## Notes / judgment calls
- **反-alarmism framing 提升到開頭 blockquote**：原 draft 的「不是指控」散在 Context；publication 把它提到題後第一段，因為這是對外稿最容易被斷章取義的點。
- **TL;DR 降低引註密度**：摘要段刪掉多數 [cNNN]，把完整引註留在正文，符合 lay-reader 摘要慣例。
- **第四環三步結構顯性化**：原 draft 用 L4a/b/c，publication 改成「第四環的三步」並加導言句，讓讀者看得到「為什麼要拆三步」。
- **c010/c012 價差與佔比數字保留精確值**（51–460×、1.2%→13%）：屬實質發現，不可軟化（skill 邊界：不改數字）。
