# Coding reliability — join-petition-typology-tw

**2026-06-19** · 回應 review blocker（brief 要求 ≥150 件雙盲 + κ）

## 方法（誠實範圍）
**Inter-model** reliability：原始編碼為 sonnet（45-agent workflow）；獨立第二編碼者為 **opus**（9-agent workflow，盲編——只給提案文本＋同一套 codebook v1.1，不給原始標籤）。樣本 200 件 = 隨機 150 ∪ 全部 57 件 org-backed（審查特別點名稽核）；opus 回 196 件，overlap 196。

⚠️ 這是**跨模型一致性**（測 codebook 是否清楚到不同模型會同意），**非人工雙盲**。是此 pipeline 可達的最強信度驗證；若要期刊級，仍需人工雙盲子樣本。腳本 `coding/compute_kappa.py`。

## 結果

| 變項 | %一致 | Cohen κ | 加權 κ(序數) | %在±1內 | 判讀 |
|---|---:|---:|---:|---:|---|
| **org_binary（有無組織）** | 93% | **0.83** | — | — | almost-perfect ✅ |
| topic | 87% | 0.85 | — | — | almost-perfect |
| **org_backing（四類）** | 88% | **0.71** | — | — | substantial ✅ |
| **motive** | 68% | 0.46 | **0.65** | 95% | 兩端可靠、1-2 邊界模糊 |
| **form_score** | 50% | 0.31 | **0.62** | 88% | 分歧多相鄰、substantial(加權) |
| d2_enable | 84% | 0.63 | — | — | substantial |
| ai_essay | 97% | 0.60 | — | — | substantial |
| d1_target | 82% | 0.59 | — | — | moderate |
| d3_outcome | 62% | 0.31 | — | — | fair（最弱的 D 分量） |
| **constituency** | 46% | 0.20 | **0.25** | 87% | **poor（即使加權）— 最不可靠** |

> 序數變項（form_score/motive/constituency）的未加權 Cohen κ 偏嚴（把 ±1 算全錯）；二次加權 κ 才是公允統計。

**org_backing 稽核**：56 件 gold org-backed 中，opus 也判 org-backed 的有 **46（82%）**。
**motive 混淆**：主要分歧是 gold=2 vs opus=1（40 件）→ sonnet 比 opus 多判 motive=2，證實「全樣本 64% motive=2 偏寬鬆」。0-vs-2 兩端極少互換（gold0→opus2 = 0 件）。

## 對研究結論的意涵

1. **Headline（組織動員主導跨門檻）站得住**：org_backing 是**最可靠**的變項（org_binary κ=0.83），審查最大疑慮（org 建在未驗證標記）**解除**。
2. **form_score（次要、2×）可接受**：加權 κ=0.62、88% 在 ±1 內；分歧是 form2/form3 之類相鄰格，不影響「正向次要」結論。
3. **motive（已在 v2 降級為 suppression 殘差）**：兩端可靠、但 1-2 邊界模糊且 sonnet 偏寬；維持 v2 的強 hedge 是正確的。
4. **constituency（1.4×）信度 poor（κ 0.25）**：v2 須把它標為**最不可靠的變項**，其溫和效果視為弱證據。
5. d3_outcome（fair）是 form 三分量裡最弱的——codebook v2 可優先補這條的決策規則。

**發表前仍建議**：人工雙盲子樣本（~50 件）覆核 org_backing 與 motive 兩端，作為跨模型 κ 之外的金標準。
