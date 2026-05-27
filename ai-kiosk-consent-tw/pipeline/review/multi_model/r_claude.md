# Review of ai-kiosk-consent-tw insight_v1 — Claude (schema-aware reviewer, v1 review pass)

**Reviewed on**: 2026-05-27
**Draft**: projects/ai-kiosk-consent-tw/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (92 records), extracts/ (27 deep-reads), rejected.jsonl (15 records), brief.md, brief_expanded.yaml, themes.jsonl (9 themes)
**Reviewer role**: 多模型分工中的 schema-aware reviewer — L6 / L7 / L8 + Dr1/Dr2 合約裁決 weight 最重。本次為 v1 全力 adversarial pass,無先前 reviewer baseline。

## Verdict

- **F1 (Q1a 雙端規模)**: ✅ solid — 雙端展開 + B/C firewall 嚴謹,**唯 [speculative] tier 用法存疑(見 L5)**
- **F2 (Q1b 雙 showcase)**: ⚠️ needs tightening — Confidence 自評 "high" 與 [strong] 標記偏高,t01 themes tier_counts 是 3 strong / 2 contested / 1 spec,但 F2 整段標 strong + high
- **F3 (Q2+Q7 wording vacuum)**: ✅ solid — 五源 cross-confirmed 是最紮實的 finding
- **F4 (Q4 法律 + 憲法 spine)**: ⚠️ needs tightening — 釋字 603 / 111 憲判 13 援引嚴謹但 **transferability 跳得太快**,scope_caveat 在 c097/c098 extract 已明示卻未被 finding 自身複述(見 L2 + L7)
- **F5 (Q4+Q7 vendor internal-split)**: ✅ solid — partial_counter_framing 處理 Dr7 合規,caveat-tier 標記正確
- **F6 (D 軸三層對照表)**: ⚠️ needs tightening — 對照表本身 strong,但 c044 CyberLink SDK 行銷頁與 c045 CyberLink insights 兩者 framing 一致性、SDK vs 終端的法律責任分配在勾選表結論未清楚
- **F7 (Q3+Q6 四重結構性零)**: ❌ has gap — **「3,058 件/年隱形池下界 proxy」是 Drafter 推論,inference 內含比例完全未證**(見 L2 + L5);此外 c079 行政院消保會全國申訴統計 + c095 高雄高等行政法院 profiling 判決兩源 accepted but uncited 嚴重削弱「四重零」claim 的窮盡性
- **F8 (Q5 國際對照)**: ⚠️ needs tightening — Home Depot c073 案性質 caveat (B 區 identification 而非 A 區 inference) extract 已明示,finding 未承載;c070 EC Feb 2025 guidelines 是 AI Act Art. 5 商業界線的官方權威解析卻完全未引

**F-level tally**: 3 ✅ / 4 ⚠️ / 1 ❌ / 0 🚨

**Overall**: 🟡 publishable with edits — 整體架構 (A/B/C firewall、Dr2 scope tag coverage、Dr7 caveat-tier 處理) 合約合規且論證骨幹紮實,但 F4 跳躍式法律 transferability、F7 inference-proxy 推論、F8 Home Depot scope mismatch 三點是 publication-blocker 等級的修整需求。F4 + F7 同時涉及「Drafter 拿 c098 / c105 的力道做超出 extract scope_caveat 的推論」此一同型 failure mode,屬系統性 tightening 需求而非孤立修補。

---

## Per-finding analysis

### F1 (Q1a 雙端規模 — 保守下界 vs vendor-claimed 上界)

**L1 Citation density**: ✅ 每個 factual claim 都有 cite;[strong] 雙月 + 金色三麥 由 c032 + c041 直接背書 (≥2 strong sources)。
**L2 Claim-vs-source fidelity**: ✅
- 「雙月 WiXtar 將消費者精細分類,並由 AI 影像生成技術塑造的虛擬人物進行個性化推薦 [c032]」逐字符合 c032 Passage 1。
- 「金色三麥 已導入 AI 人臉辨識導購系統,根據顧客表情與特徵推薦酒款 [c041]」逐字符合 c041 Passage 1。
- 「WiXtar 30+ 品牌、超過 1000 台 AI Kiosk [c033]」逐字符合 c033 Passage 1。
- 「inference 啟用比例 vendor 未揭露」三層黑箱論證 = c033 extract scope_caveat (b) 直接搬移,**忠實處理**。
**L3 Counter-evidence honesty**: ✅ 雙端展開正是對 vendor 自報的 hedge;CyberLink c044 摘要層列為 counter-evidence 但明示 "依摘要層 sourcing,未經 deep-read 一手驗證" — Dr7 sourcing tier 標記合規。
**L4 Overlooked sources**: ⚠️ accepted.jsonl 內 c034-c036、c039-c040、c043、c048(其他 vendor 相關)未進入清單;不算 cherry-picking blocker,但若 F1 想 surface「保守下界 2 brand 已具名 + n brand 由其他來源指認」雙重防線可加強。
**L5 Confidence calibration**: ⚠️ **B/C callout 段 (第 4 段) 標 [speculative]** — 此處 tier 用法存疑:c049 銓幻元、c046 拍檔、c047 Berry AI 是 primary vendor doc + Dr1 spec 規定 [speculative] = 單源或未解爭議;但 B/C firewall callout 三者都是「明確證實 B/C 而非 A」的事實主張,應為 [contested] 或 [strong](方向相反)而非 speculative。建議改 tier 標籤或 reframe 為「per ontology B/C 定義,以下三者 do-not-count-toward-A:c049 [strong 為 B] / c046 [strong 為 C] / c047 [strong 為 C]」。
**L6 Brief-question coverage**: ✅ Q1a 完整覆蓋,雙端展開符合 brief §8 第 1 條「列出至少 N 家」。
**L7 Gaps / unknowns**: ✅ 「30+ 品牌名單」「inference 啟用比例」「4 種劇本分類規則」三層黑箱在 What we don't know 已 surfaced。
**L8 Concept-fidelity**: ✅ 段 1-3 標 `{conceptual:A}` 與 themes t02 (evidence_scope conceptual {A:4}) subset = OK;段 4 標 `{conceptual:B,C}` 與 themes t04 (conceptual {C:2, B:1}) subset = OK。

**判決**: ✅ solid。唯一可動處為 L5 tier 用法。

---

### F2 (Q1b 雙 showcase)

**L1 Citation density**: ✅
**L2 Claim-vs-source fidelity**: ⚠️
- 「藉由雲端運算,將資料完整回傳台灣總部 [c032]」逐字 = c032 Passage 2,正確。
- 「外籍遊客語音通過 OpenAI / 微軟 API 跨境傳輸 [c033]」 — c033 Passage 2 原文是「透過 OpenAI 及微軟的 AI 技術,外籍遊客只要對著 Kiosk 提出需求……自動轉譯成客人讀得懂的語言」 — 此處 wording 隱含跨境傳輸但 c033 並未明文寫「跨境傳輸」;Drafter 推論 OpenAI/Azure 為境外 = 跨境屬合理推論,但屬 inference 而非 verbatim,**應加 hedge**(「推論為跨境傳輸 — vendor 未明文說明資料是否經境外節點」)。
- 表格 t₁「即時臉部畫面進入 RAM / 推論管線」屬 Drafter 機制推論;c032/c033 並未明文寫 RAM/inference pipeline 細節。**建議標 [speculative-mechanism inference]** 或加 hedge。
**L3 Counter-evidence honesty**: ✅ 桌面觀察 AI 「規劃推出」狀態保留為 [contested-planned],Dr1 合規。
**L4 Overlooked sources**: ⚠️ accepted 中 c034-c040 同一 cluster 的 vendor / 媒體 source 應為 F2 第一手底料,但 F2 只引 c032/c033/c041/c042 四源(+ c038 在 F3 提到)。對 brief §Expected output「兩個 use-case 詳細 showcase」HARD requirement,F2 已達 t01 theme 6 source 中 4 source — 可接受但非 exhaustive。
**L5 Confidence calibration**: ⚠️ F2 結尾「Confidence: high — 兩個 case 皆有 ≥3 源 cross-confirmed」與 themes t01 tier_counts (strong: 3 / contested: 2 / speculative: 1) 不完全一致;showcase A 標 [strong] OK,showcase B「拍照玩 AI 調酒師 → 推算性格特質」由 c042 Marie Claire (qs=3 lifestyle 媒體) 為主源,搭配 c041 / c038,整體應為 medium-high 而非 high。
**L6 Brief-question coverage**: ✅ Q1b 完整對應 brief §8 第 2 條「2 個 use-case 詳細 showcase」。
**L7 Gaps / unknowns**: ✅ 「留存政策黑箱」在 What we don't know 已 surfaced。
**L8 Concept-fidelity**: ✅ Showcase A/B 段標 `{conceptual:A}` 與 t01 conceptual {A:6} subset = OK;表格後 [contested] 段標 `{conceptual:A∩D}` 在 themes 內無單獨 A∩D 列(但 brief research_focus 就是 A∩D)— **此 tag 屬語意上的 inference 合成,L8 lint 可能 flag 為「conceptual 軸不在 evidence_scope_distribution.conceptual」**。建議改為 `{conceptual:A; concept_axis:D}` 或在 brief_expanded ontology 中正式聲明 A∩D 為合法 conceptual scope value。

**判決**: ⚠️ needs tightening。Showcase A「跨境傳輸」+ Showcase B「high」confidence 自評兩處需 hedge。

---

### F3 (Q2 + Q7 — wording vacuum 五源 cross-confirmed)

**L1 Citation density**: ✅ 五源逐一具名 (c032/c041/c037/c042/c038)。
**L2 Claim-vs-source fidelity**: ✅
- 五源 0 字 wording 主張 = c032 Passage 3 / c041 Passage 3 / c042 Passage 2 三處 extract 已明示確認;c037 / c038 雖無 extract,但 c041 extract 結構說明「c032 + c041 + c033 + c038 + c039 + c040 + c042 + c043 八篇 0 wording」覆蓋。
- CyberLink c045 wording 反例「需透過用戶『知情同意』」逐字 = c045 Passage 1。
**L3 Counter-evidence honesty**: ✅ CyberLink 反例本身就是 self-counter,Drafter 主動 framing 為 counter-evidence。
**L4 Overlooked sources**: 無明顯遺漏。
**L5 Confidence calibration**: ✅ Confidence high 合理(5 源 cross-confirmed + 1 反例)。
**L6 Brief-question coverage**: ✅ Q2 + Q7 雙覆蓋。
**L7 Gaps / unknowns**: ✅ 「framing 傳染路徑」在 What we don't know 中 surfaced。
**L8 Concept-fidelity**: ✅ `{conceptual:A}` (段 1) → themes t05 conceptual {A:5} subset OK;`{conceptual:A∩D}` (段 2、3) 同 F2 議題:`A∩D` 不在 themes 個別 conceptual key 中,但屬 brief research_focus 合法值。

**判決**: ✅ solid。

---

### F4 (Q4 — 個資法 + 憲法 spine)

**L1 Citation density**: ✅ 4 strong 源 + 2 contested 源。
**L2 Claim-vs-source fidelity**: ⚠️ **這是 F4 最關鍵的 weakness**:
- 「§6 是 closed list,不含『等』字」— 對應 c054 Passage 1「病歷、醫療、基因、性生活、健康檢查及犯罪前科」,**正確**(條文確實無「等」)。
- 釋字 603 五動詞「是否揭露／在何種範圍內／於何時／以何種方式／向何人」逐字 = c097 Passage 1,**忠實**。
- 「**舉重以明輕**」適用釋字 603 比例原則論證至餐飲 inference — c097 Passage 4 確實有「身分證防偽…損益失衡、手段過當」原文,Drafter 推導「商業目的舉重以明輕」**是合理但屬論證跳板**;**c097 自己的 scope_caveat 明示「原因案件是強制蒐集 vs 私人商業行為,有 state action vs horizontal effect 差距」與「釋字 603 完全未觸及 inference vs identification 二分」兩條 caveat — F4 沒有複述這兩條 caveat,把這個跳板呈現得比 extract 願意承載的更強**。建議 F4 在 [strong] 段內加 hedge 句:「釋字 603 原因案件為強制蒐集 (state action),餐飲 kiosk 為私部門商業行為,doctrine 適用上有 horizontal effect 中介;但本研究援引其資訊隱私權定義 + 比例原則邏輯,屬通說可承載之 transferable scope」。
- 111 憲判 13【35】「無還原識別之方法難易…仍屬個資」逐字 = c098 Passage 1,**忠實**;但「即使 kiosk 在邊緣即時刪除原始影像,只要該影像在處理過程中仍可被還原識別 (實際上多數 edge inference 系統都會在 RAM/cache 短暫留存原始畫面)」這段 — **「實際上多數 edge inference 系統都會」是 Drafter 的技術事實主張,沒有 cite**;F4 此處夾帶一個 mechanism inference (RAM/cache 短暫留存) 作為 [strong] 段內論據。需 cite 或標 [speculative-mechanism]。
- 111 憲判 13 對個資法欠缺撤回機制違憲 → 「實作層更是完全空白 — 法律端 + 實作端兩端皆 broken」**這是強論點但本身合理**,c098 Passage 5 直接支撐。
**L3 Counter-evidence honesty**: ✅ 國發會「健保資料非用於識別」framing 被駁回的「同構先例」援引極為精彩,c098 extract structural section 確實記載此交鋒。
**L4 Overlooked sources**: ⚠️ **c057 / c058 / c060 三家律所對 2025 修法的並行分析、c088 個資法施行細則 primary doc、c061 PDPC 施行細則修正案及子法草案、c062 律所對人臉辨識規範解析、c065 極憲焦點對刷臉的憲法分析**,皆 accepted but uncited — 用 c055 fblaw 單源支撐「修法核心為 PDPC 組織建構而非 §6 inference 灰區填補」這個 [contested] 主張,**單源 contested 可接受**,但若加入 c057-c060 跨律所 cross-confirmation,可從 contested 升為 strong;此外 c061 對 PDPC 施行細則動態的揭露對 [contested] 段「修法為未來 PDPC 函釋 / 子法建立法源」可直接 instantiate。
**L5 Confidence calibration**: ⚠️ F4 結尾 Confidence: high,4 strong + 2 contested。整體 Confidence high 合理,但其中 [strong] 段第 4 段(111 憲判 13 對 inference framing 的炸藥級反駁)夾帶 unverified mechanism inference (RAM/cache),嚴格說應在那一句處降為 [contested-mechanism]。
**L6 Brief-question coverage**: ✅ Q4 完整。
**L7 Gaps / unknowns**: ⚠️ 「edge inference 系統實際是否在 RAM/cache 短暫留存原始畫面」是 Drafter 自己引入的技術主張,卻沒在 What we don't know 列為 gap;若 Reviewer 認為此屬「需技術驗證的關鍵 mechanism claim」,應 surface 為 gap。
**L8 Concept-fidelity**: ✅ 段標 `{conceptual:A∩D}` 與 t07 conceptual {A:4, D:6} subset OK。

**判決**: ⚠️ needs tightening。L2 (釋字 603 scope_caveat 未複述 + RAM/cache mechanism 主張無 cite) 是最關鍵的修整點。

---

### F5 (Q4 + Q7 — vendor internal-split)

**L1 Citation density**: ✅
**L2 Claim-vs-source fidelity**: ✅
- CyberLink 三層 wording (告知 / 同意 / 撤回) 逐字 = c045 Passage 1 + Passage 2,**全部忠實**。
- 對照 c032 / c037 / c041 三源 zero wording — c032 Passage 3 + c041 Passage 3 extract 已確認;c037 無 extract,以摘要層 sourcing 處理但本身為 vendor 一手頁,可接受。
**L3 Counter-evidence honesty**: ✅ CyberLink SDK vs kiosk 部署終端的法律責任分配 caveat 主動寫進 counter-evidence — Dr7 合規。
**L4 Overlooked sources**: ✅ 此 finding 的 vendor internal split 五源 (c044 + c045 + c032 + c037 + c041) 已涵蓋 t08 theme 4 extract refs。
**L5 Confidence calibration**: ✅ Confidence medium + 主動拒絕升 [strong] (Dr7 partial_counter_framing caveat-tier 處理) — 合約合規的典範。
**L6 Brief-question coverage**: ✅
**L7 Gaps / unknowns**: ✅ 「CyberLink vendor framing 在後 EU AI Act 環境的更新」surfaced。
**L8 Concept-fidelity**: ⚠️ 段 1 標 `{conceptual:A∩D; temporal:2023-2026}` 與 t08 conceptual {A:4, D:1} — temporal 範圍 2023-2026 略超 t08 evidence_scope temporal {2024+:1, 2026:1, 2025:1, 2023:1};subset 嚴格說 OK(2023-2026 覆蓋所有 evidence temporal 點),但這是 superset framing 邊緣,Reviewer 提示 Drafter 改寫為「2023 (c045) → 2026 (c037)」逐源 anchor 更精準。

**判決**: ✅ solid。Dr7 partial_counter_framing 處理是全 draft 最教科書式的合規範例。

---

### F6 (D 軸三層對照表)

**L1 Citation density**: ✅ 表格每 cell 都有 source。
**L2 Claim-vs-source fidelity**: ✅ CyberLink 三層 ✓ 對應 c045 Passage 1 + 2,**忠實**;雙月 / 金色三麥 0 wording 對應 c032 / c041 / c033 / c038 / c042 五源 cross-confirmed。
**L3 Counter-evidence honesty**: ✅ CyberLink 為 SDK 供應商 vs kiosk 終端的法律責任 caveat 在 counter-evidence 段提及。
**L4 Overlooked sources**: ⚠️ **c044 (CyberLink FaceMe SDK 產品頁) 在表格中未獨立佔列** — 對照表只有 c045 (CyberLink insights blog) 一列;若兩源 framing 一致可拼接,但若 c044 是純 SDK marketing 而 c045 是 thought leadership 文章,framing 上是否一致應 surface — c044 在 F1 「Counter-evidence」段被標為「依摘要層 sourcing,未經 deep-read 一手驗證」,意味 c044 wording 是否與 c045 同一致確認仍 unknown。F6 對照表未 surface c044 的 D 軸 wording 是否同 c045 一致。
**L5 Confidence calibration**: ✅ Confidence medium 合理,Drafter 主動 surface「勾選對照本身是 Drafter 對比個資法 §8 的中介判斷」屬合約合規。
**L6 Brief-question coverage**: ✅ brief §Expected output HARD requirement「同意機制三層對照表」滿足。
**L7 Gaps / unknowns**: ✅
**L8 Concept-fidelity**: ✅ `{conceptual:A∩D; temporal:2023-2026}` 與 t08 / t05 subset OK。

**判決**: ⚠️ needs tightening — c044 與 c045 一致性確認 + SDK vs 終端法律責任分配在勾選表結論可更明確。

---

### F7 (Q3 + Q6 — 四重結構性零)

**L1 Citation density**: ✅ 每重零各有 source。
**L2 Claim-vs-source fidelity**: ❌ **這是 draft 最大的單一 weakness**:
- 「新北 services_others 2,235 件 + 桃園「其他」823 件 = 3,058 件/年隱形池下界 proxy」— 計算正確:c105 Passage 2 確認新北 113 年 services_others_quantity = 2,235 件、c106 Passage 1 確認桃園 113 年「其他」= 823 件,sum 為 3,058。**但 Drafter 把這個 sum framing 為「A∩D 灰區隱形池下界 proxy」是 over-claim**:c105/c106 extract 都明確標 caveat「『結構性零』不等於『實質零』 — 不能直接結論『無 biometric 投訴』,只能結論『schema 不能辨識 biometric 投訴』」+「『其他』buckets 中可能含 biometric 相關投訴但無法獨立辨識」+「桃園與新北 schema 結構不對齊,Drafter 不應 naive 加總跨縣市『其他』bucket 數字」。**Drafter 不僅做了 caveat 警告過的 cross-locality 加總,還把該 sum framing 為「inference 隱形池下界 proxy」**,等於主張該 3,058 件中有非零比例屬 A∩D 投訴。Extract 沒有任何 row-level evidence 支持此 inference;c105 Passage 2 only 是「成長 4-5 倍 → 新類型 consumer complaint 出現」概念性主張,**不能反向推導 inference 投訴存在於 residual bucket**。

  **修正建議**: 改為「residual buckets 113 年新北 2,235 件 + 桃園 823 件,若 inference 投訴存在皆 absorbed 進此 opaque pool — 但 bucket 內 inference 比例完全 unknown,此 3,058 不能作為 inference 投訴量下界,只能作為『若有 inference 投訴 = invisible 的容量上界 proxy』」。3,058 是 invisible-ceiling 而非 inference-floor。

- 「司法零 35 件」— c096 accepted 記錄確認 20+15=35 件全文檢索,verdict 為「人臉辨識 + 生物特徵全部判決中 0 件餐飲 inference」;Drafter 已標「依摘要層 sourcing,未經 deep-read 一手驗證」— Dr1 合規。但 **F7「司法零」claim 未檢視 c095 高雄高等行政法院 114 年度簡字第 216 號判決**,該判決 abstract 明示「自動化資料處理、特徵分析、行為定位、強制身份核實、資訊過濾和大規模監視等對兒童造成的風險」 — **這是台灣行政法院唯一一個直接論述 profiling/特徵分析監控風險的判決**,即便場景不是餐飲 inference,作為「司法零」claim 的 boundary case 應在 F7 surface 為「邊界判例」,不是直接視為 zero。建議加註:「司法零僅限餐飲 inference 場景;高雄高等行政法院 114 年簡 216 雖屬兒少領域,已論述 profiling/特徵分析監控風險 — 顯示行政法院已有 doctrine 萌芽 [c095]」。

**L3 Counter-evidence honesty**: ✅ 「實際無問題故無投訴」另類解釋主動 surface 為 counter — 然後給出 TAHR + 國際比較 + vendor vacuum 三方匯流的反駁。處理良好。
**L4 Overlooked sources**: ❌ **c079 行政院消費者保護會全國申訴統計** + **c080 行政院消保會線上申訴系統** 都在 accepted、both why_relevant 直接寫「Q6: 全國消費者申訴統計 — Drafter 查『生物特徵類』申訴是否列項」與「『渠道存在但申訴量為零』論證」 — Drafter 只用 c105/c106 縣市層 dataset,**對全國層的官方統計 source 完全 silent**。F7 「申訴 schema 零」是核心 finding,缺全國層佐證屬重大 cherry-picking 風險;若全國消保會 schema 也無 biometric category,反而是 F7 最有力的證據 — 缺此 source 削弱 F7 claim 的窮盡性。
另 **c095 高雄高等行政法院 profiling 判決** — 同上 L2 已分析。
**L5 Confidence calibration**: ⚠️ Confidence medium 合理(schema-design 跨縣市 confirmation + 司法摘要層 + framing 兩源 + NGO 立場),但「3,058 件/年隱形池下界 proxy」這個量化 claim 在現有證據下應為 [speculative] 而非 [contested]。
**L6 Brief-question coverage**: ✅ Q3 + Q6 合併處理為 operator-confirmed 設計,**verified F7 同時涵蓋兩問**:Q3「人工替代是否可用」由 (1) 司法零 + (4) NGO 量化零承接(雖然 Q3 「人工替代退出成本」具體實況未直接量化處理,F7 對映度較低 — 但 Q3 在 F8 Home Depot 部分間接以「no staffed checkout alternatives」對照,跨 F 處理);Q6「執法現況」由四重零完整承接。**non-blocker,但 Q3 處理略單薄。**
**L7 Gaps / unknowns**: ✅ 台中 row-level + 全國 schema gap 部分 surface,**但全國消保會 c079/c080 access status 未在 What we don't know 提及**;若 Drafter 嘗試過但無資料,應主動承認。
**L8 Concept-fidelity**: ✅ `{conceptual:A∩D; temporal:2011-2025}` 與 t06 conceptual {D:6, A:5}、temporal 含 2011-2025 subset OK。雙重結構性原因段標 `{conceptual:A∩D; geographic:TW,US-IL}` 與 t06 geographic 不含 US-IL(僅 TW/TW-NPT/TW-TYC/TW-TCH)— **此段 conceptual 在 t06 內 OK,但 geographic US-IL 是 BIPA 比較段,屬 t09 evidence_scope geographic {EU:4, US-IL:1, SG:1};F7 段在 t06 主題下引入 t09 evidence 的 geographic scope = cross-theme scope blending**,L8 lint 嚴格說可能 flag。建議拆段或明示「此段引入 Q5 國際比較 t09 source [c073]」。

**判決**: ❌ has gap。「3,058 inference proxy」over-claim + c079 全國申訴 cherry-picking + c095 邊界判例 omission 三點是 F7 publication-blocker 等級修整需求。

---

### F8 (Q5 國際對照)

**L1 Citation density**: ✅
**L2 Claim-vs-source fidelity**: ⚠️
- 「Art. 5(1)(f) emotion recognition 禁令僅及於職場 + 教育機構,商業餐飲場合完全不在禁止範圍 [c067]」逐字符合 c067 Passage 1 + scope_caveat,**Drafter 主動防範常見誤讀,極為精彩**。
- 「Art. 5(1)(g) biometric categorisation 禁令只禁 6 類敏感屬性 [c067]」逐字符合 c067 Passage 2,正確。
- **Home Depot c073 案 finding 框架為「Q5 最接近台灣餐飲 kiosk 的單一國際先例」** — 但 c073 extract scope_caveat 明示「Home Depot 案件性質為『loss prevention surveillance』(防盜識別),與 brief A 區『demographic inference 用於推薦』非完全同類:Home Depot 可能更接近 B 區身分比對 (identification for 黑名單) 而非 A 區 demographic categorisation」 + structural section「Home Depot 案技術屬性被報導為『computer vision for loss prevention』(防盜識別),可能更接近 B 區 identification」。**F8 完全沒有複述此 scope_caveat**,直接把 Home Depot 框架為「最接近台灣餐飲 kiosk 的單一國際先例」。「最接近」屬實 (BIPA 同款保護涵蓋 A/B),但「無 caveat 援引」會讓讀者誤以為 Home Depot 屬 A 區 demographic inference 案。建議加 hedge:「Home Depot 案技術屬性可能更接近 B 區 identification (loss prevention),但訴狀的『無告示 + 無同意 + 無人工替代』邏輯對 A 區 inference 直接適用 — 援引的是其告知層失敗結構而非 case categorisation 一致性」。
**L3 Counter-evidence honesty**: ✅ 「EU AI Act 對餐飲 inference 場景的覆蓋有限是必須誠實告知讀者的」主動寫進 counter-evidence — 處理良好。
**L4 Overlooked sources**: ⚠️ **c070 EC Feb 2025 prohibited AI practices guidelines** — 這是 European Commission 對 AI Act Art. 5 的官方執行指引,直接針對「商業空間 / 教育 / 工作場所界線」(c070 why_relevant 字面),accepted but uncited。F8 對 Art. 5 商業/職場界線的論述基於 c067 條文本身,**缺 c070 官方解釋是嚴重 cherry-picking** — c070 是 Art. 5 邊界爭議的權威解析,若 F8 想 strong-tier 主張「emotion recognition 禁令僅及於職場/教育」,c070 是必引 source。
**c071 / c072 BIPA litigation trend** 兩源也未引,對 F8 BIPA enforcement infrastructure 論述可加強(僅 c073 單案略單薄)。
**c075 CCPA primary doc + c074 CCPA biometric guide** 兩源未引,F8 第 1 段「BIPA / CCPA / SG PDPA / EU AI Act」對照 framing 但實際只引 c067 + c073 + c076 + c077,CCPA 段 0 source。
**L5 Confidence calibration**: ⚠️ Confidence medium 合理。
**L6 Brief-question coverage**: ✅ Q5 涵蓋。
**L7 Gaps / unknowns**: ✅
**L8 Concept-fidelity**: ✅ 各段 geographic 標籤 (EU / US-IL / SG) 與 t09 evidence_scope {EU:4, US-IL:1, SG:1} subset OK。

**判決**: ⚠️ needs tightening — Home Depot scope mismatch 援引 + c070 EC guidelines 缺引兩點是修整需求。

---

## Cross-cutting concerns

### Tier-tagging 一致性 (Dr1)
**良好實踐**: F1 雙端展開、F5 partial_counter_framing 處理、F8 EU AI Act 主動防誤讀,皆 Dr1/Dr7 合規典範。
**問題**:
- F1 第 4 段 B/C callout 標 [speculative] 但內容為「明確證實 B/C」strong claim — tier 誤用。
- F4 第 4 段 [strong] 內夾帶「實際上多數 edge inference 系統都會在 RAM/cache 短暫留存原始畫面」的無 cite mechanism inference — strong-tier 段內不應夾 speculative claim。
- F7 「3,058 件/年隱形池下界 proxy」標 [contested] 但實際應為 [speculative]。

### L8 scope tagging coverage
**Coverage**: 8 個 Finding 都帶 `**{conceptual:...; temporal:...; geographic:...}**` 風格 inline scope tag(以 HTML comment `<!-- ... -->` 形式,而非 Dr2 推薦的可見 markdown bold)。**這是 Dr2 contract 形式上一個邊界爭議**:lint 的 `check_scope_tag_coverage` 應 verify presence 但 HTML comment 形式是否被認 recognised 取決於 lint script regex 設計。若 mechanical lint 只認 `**{...}**` visible bold pattern,**本 draft 全 8 個 Finding 都將被 lint fail**;但 HTML comment 形式對讀者也是 invisible — Drafter 是否刻意選用此 form 以避免報告本文「噪音」,但這同時違反 Dr2 spec「the tag for every paragraph」可見性意圖。**建議 operator 介面層確認 lint 認哪一形式**;若 lint 只認 visible bold,draft 需重寫所有 scope tag 為 visible 形式。
**Conceptual A∩D 合法性**: F2 / F3 / F4 / F5 / F6 / F7 多處 conceptual scope 標為 `A∩D`,但 brief_expanded.yaml 的 ontology 只定義 A / B / C / D 四個單值,**A∩D 是 research_focus 而非 conceptual key**。L8 lint `check_claim_scope_in_themes` 嚴格說可能 flag — 因為 themes evidence_scope_distribution.conceptual 只有 {A:n, D:m} 兩個獨立 key,沒有 A∩D 合成 key。**Reviewer 判斷**: 此屬語意合理 (A∩D = brief research_focus) 但 schema 不對齊;建議 Drafter 改寫為 `{conceptual:A,D}` (multi-value list 形式) 與 themes 結構對齊。

### TL;DR vs Findings consistency
- TL;DR 第 1 點「30+ 餐飲品牌、超過 1000 台 AI Kiosk」與 F1 「30+ 品牌、1000+ kiosk」一致;TL;DR 主動加 hedge「inference 啟用比例 vendor 未揭露」與 F1 主結論一致。
- TL;DR 第 3 點「3,058 件/年隱形池 lower-bound proxy」**直接 inherit F7 的 over-claim** — TL;DR 把 inference proxy 寫進 ⚡核心結論,若 F7 修整,TL;DR 必須連動修整。
- TL;DR 第 4 點 CyberLink internal-split + 三源 zero wording 與 F3 + F5 一致。
- TL;DR 第 5 點 2025/11/11 修法 vs 111 憲判 13 三個月落後 — 數字推導 (2022-08-12 + 3 年 = 2025-08-12;2025-11-11 公布 = 落後 3 個月) 正確。

### Source-pool integrity self-check (per prompt §"Source-pool integrity self-reminder")
- 引用 cids: c032, c033, c037, c038, c041, c042, c044, c045, c046, c047, c049, c053, c054, c055, c059, c067, c073, c076, c077, c081, c082, c096, c097, c098, c105, c106, c107 — **全 27 cids 都在 accepted.jsonl (92 records) 中**,**無一在 rejected.jsonl (15 records) 中**;cid 形式無捏造。
- 「Sources consulted: accepted.jsonl (92 records), extracts/ (27 deep-reads), themes.jsonl (9 themes)」與實檔計數一致。

### Brief failure-condition self-check
brief §Failure conditions 6 條 (倫理通論 / A-B 混為一談 / inference 不算蒐集 hand-wave / 無對照表 / GDPR 直接當台灣結論 / 沒分 supply-side vs demand-side):
1. **倫理通論**: ❌ 不發生 — F1-F8 全為具體 case 與 doc 援引。
2. **A-B 混為一談**: ❌ 不發生 — F1 第 4 段明確 firewall,Context 段亦 firewall。
3. **inference 不算蒐集 hand-wave**: ❌ 不發生 — F4 完整法律拆解。
4. **無對照表**: ❌ 不發生 — F6 對照表存在。
5. **GDPR 直接當台灣結論**: ❌ 不發生 — F8 主動防範。
6. **沒分 supply-side vs demand-side**: ⚠️ **partial** — F1 處理 supply-side (vendor 部署數),F2 處理 demand-side 部分 (showcase 個別消費者體驗),但 F7 demand-side 結構性 invisibility (申訴 schema 零) 試圖補上 demand-side 缺口時 over-claim 為 inference proxy — **這個 supply/demand 分離意圖好,但 F7 執行不嚴謹**。

---

## Overall verdict

🟡 **publishable with edits**

整體 architecture 合約合規且論證骨幹紮實,Dr1 tier-tagging、Dr2 scope tagging、Dr7 partial_counter_framing 處理多數 finding 為合約典範;A/B/C firewall 嚴格、釋字 603 + 111 憲判 13 憲法 spine 援引精彩、CyberLink internal-split partial counter rescue 是教科書範例。

但有 **3 個 publication-blocker 等級修整** 與多個 tightening 需求:

### 必修 (block publication)
1. **F7 「3,058 件/年隱形池下界 proxy」over-claim 重寫** — 改為「invisible-ceiling 而非 inference-floor」;TL;DR 第 3 點連動修整。
2. **F7 加 c079 行政院消保會全國申訴統計 + c080 線上申訴系統 source** 或在 What we don't know 明確承認「全國層 schema access status / 結論未取得」。
3. **F4 「edge inference 系統 RAM/cache 短暫留存原始畫面」mechanism inference** 需 cite 或標 [speculative-mechanism];避免在 [strong] 段內夾 unverified claim。

### 建議修整 (improve to fully 🟢)
4. **F4 釋字 603 transferability** 在 [strong] 段內加 state-action vs horizontal-effect hedge (c097 extract scope_caveat 已明示)。
5. **F8 Home Depot c073** 加 B vs A 區 scope_caveat hedge (c073 extract scope_caveat 已明示)。
6. **F8 加 c070 EC Feb 2025 prohibited AI practices guidelines** 作為 Art. 5 商業/職場界線權威解析。
7. **F1 第 4 段 tier** 由 [speculative] 改為 [strong 為 B] / [strong 為 C]。
8. **F2 Showcase A 「跨境傳輸」claim** 加「推論為跨境,vendor 未明文確認」hedge;表格 t₁「RAM / 推論管線」標 [speculative-mechanism]。
9. **F2 / F3 / F4 / F5 / F6 / F7 scope tag conceptual:A∩D** 改為 `conceptual:A,D` 與 themes evidence_scope_distribution 結構對齊。
10. **L8 scope tag form** (HTML comment vs visible bold) 確認 Drafter 是否與 Dr2 spec 對齊,或調 lint。

### 不需修整 (已合約典範)
- F1 雙端展開、F3 五源 cross-confirmed、F5 partial_counter_framing 處理、F8 EU AI Act 主動防誤讀、Counter-framing engagement 段、What we don't know 段、政策建議段 — 全 Dr1/Dr2/Dr7 合規典範,不要動。

**載重提示給 meta-merger**: 本 reviewer (Claude) 對 L6/L7/L8 weight 高,L4 overlooked sources 提了 4 個 (c057-c060/c070/c079-c080/c095/c088),其中 c079/c080 + c095 是 F7 真正影響結論可信度的關鍵 omission,c070 是 F8 真正影響結論可信度的關鍵 omission;c057-c060 + c088 屬於可加強但不修整也不違反 brief 的 polish 需求。Codex / Gemini 兩位 reviewer 若有對 L2 釋字 603 transferability 或 F7 3,058 proxy 給出獨立判斷,可作為本 reviewer L2/L5 判斷的 cross-validation。
