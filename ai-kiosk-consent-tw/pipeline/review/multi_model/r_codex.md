# Review of ai-kiosk-consent-tw insight_v1 — Codex

**Reviewed on**: 2026-05-27
**Draft**: projects/ai-kiosk-consent-tw/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (92 records), extracts/ (27 deep-reads), brief.md, themes.jsonl (9 themes)

## Verdict
- F1: ⚠️ needs tightening
- F2: ⚠️ needs tightening
- F3: ✅ solid
- F4: ❌ has gap
- F5: ⚠️ needs tightening
- F6: ⚠️ needs tightening
- F7: ❌ has gap
- F8: ⚠️ needs tightening

## Per-finding analysis

### F1 Q1a — 雙端規模

**L1/L5 citation + tier**: 2-brand 下界用 c032/c041 支撐合理，但段首標 **[strong]** 容易外溢到「兩品牌皆一手確認」；c041 是 CIO Taiwan case-study，不是 vendor 一手。建議改成「2 brand confirmed by deep-read sources」而非「一手確認」。30+/1000+ 在 F1 正文已標 [contested]，符合 c033 caveat；但 TL;DR 與標題仍把「vendor-claimed 上界」放得太像規模上限，應加「非 A 區上界，只是 WiXtar kiosk fleet 上界」。

**L2 fidelity**: c033 extract 明確說「已在台灣 30 多間合作餐飲品牌旗下門市導入超過千台 AI Kiosk」，但同 extract caveat 也說「不能假設這 1000+ 台 kiosk 全做 demographic inference」。Draft 正文有守住；標題「A 區部署規模...上界 30+/1000+」仍略 over-claim，因為上界不是 A 區，而是 vendor fleet 中 A 子集未知。

**L3 counter-evidence**: c082 歷史錨點被正確分軌，未併入 2024+ kiosk 數；B/C firewall 也清楚。不過 c044 CyberLink fast-food age/gender detection 只在 Counter-evidence 提到且未在 Source index 的正文 tier 中細化，這是合理 omission，不構成 cherry-pick。

**L4 overlooked**: Q1a 相關但未用的 c034/c036/c040/c048/c085 可補旁證，但不是必須。更明顯缺口是 c038 access_status=partial，不應被用來強化技術細節；F1 沒用 c038，OK。

**L8 scope**: 段落 scope tag 大致正確。F1 第四段 `conceptual:B,C` 將 Berry AI「人計數營運分析」放入 C 可能過粗；theme t04 對 c047 記成 C/營運分析，但不是會員 PII C 的典型例。建議寫「B/C/ops contrast」避免把 ops analytics 硬塞入 C。

### F2 Q1b — 雙 showcase 時間軸

**L1/L2**: 最大問題是表格中的若干現場流程 claim 沒有直接來源。c032 支援「精細分類」「雲端回傳總部」，c033 支援 OpenAI/微軟和 4 劇本，c041/c042 支援金色三麥人臉導購/拍照推算。但「進店看到 kiosk + 攝影鏡頭，無告示、無同意提示」「站到機器前瞬間就被掃描」「即時臉部畫面進入 RAM/cache」「持續 inference + 推薦策略運算」多是合理推論，不是 extract 原文。應標 `inferred from public materials; no on-site audit`，不能放在 [strong] 時間軸中當已觀察事實。

**Hedge fading**: c041 對桌面觀察 AI 明確是「規劃推出」，draft 在表格有標，但下一段「雙 showcase 共同特徵：(i) 消費者站到機器前的瞬間就被掃描」對金色三麥不完全適用；c042 是「拍一張照片」的主動互動，非站到 kiosk 前自動掃描。這裡從「拍照互動」滑成「瞬間掃描」。

**L3**: Counter-evidence 只處理 planned status，未處理「公開報導 0 字提同意」不等於「店面現場 0 告示」的替代解釋。應把「無公開資料顯示告示/同意介面」與「現場無告示」分開。

**L5**: 整個 F2 Confidence high 過高。部署事實 high；consumer journey 的 artifact 流向 medium/contested；金色三麥留存/傳輸 unknown。

**L8**: `conceptual:A` tags OK，但共同特徵段是 A∩D。表格內含 OpenAI/微軟語音跨境資料流，已開始觸及 C/third-party processing，scope tag 未反映。

### F3 Q2/Q7 — wording vacuum

**L1/L2**: 五源 wording vacuum 由 c032/c037/c038/c041/c042 支撐，其中 c038 是 partial access，只能作 contested/secondary。Draft 把整段標 [strong] 稍微偏高；若保留 strong，應說「c032/c037/c041/c042 strong + c038 partial corroboration」。

**L2 fidelity**: c045 passage 確實支援 CyberLink 主動承認知情同意與撤回。Draft「不是 vendor 沒空寫、是 framing 性地不認為需要寫」是 mechanism inference，不是來源直接說法；可保留，但 tier 應是 contested interpretation，而非 strong factual claim。

**L3**: 有誠實處理 CyberLink 反例。仍需補一句「媒體報導 zero wording 不等於店內實作 zero」，避免把 publication vocabulary 等同現場法遵。

**L4**: D-axis 相關 c050/c052/c056 access_blocked、c060/c061/c066/c088/c089 未用。不是硬缺口，但 F3 若討論 §8 告知層，c052 js_only blocked 應在 gap 提醒中出現，避免看似已完整查核 PDPC §8 函釋。

**L8**: 第一段 tag `conceptual:A` 不足，因結論是告知層 vacuum，應為 `A∩D` 或至少 `A,D`。目前 scope tag 低估 D，不是 overreach，但不符合 paragraph-level audit。

### F4 Q4 — 法律/憲法 spine

**L1/L2**: 個資法 §6 closed list 與 §5/§8/§19-20 一般個資義務由 c053/c054 支撐。111 憲判 13 的「直接或間接識別」引用忠實。問題在 c097 釋字 603 的 transferability 被寫得太強。

**Major causal/legal overreach**: Draft 說「餐飲業 AI Kiosk 即時 demographic inference 沒有任何單一條法律對『為了即時 inference』明確授權，以釋字 603 標準衡量連起點門檻都未滿足」。釋字 603 是國家強制捺指紋、建立身分資料庫；extract caveat 明確提醒有 state action/private actor 與 identification/categorisation 差距。私部門個資法架構未必要求每一商業蒐集目的有「單一法律明確授權」，而是要求特定目的、告知、法定蒐集事由。這句應降為「釋字 603 提供比例原則與資訊自決的強類比；直接套用『法律明定目的』到私部門商業 inference 需經水平效力與個資法中介論證」。

**Hedge fading**: 「幾乎不可能站得住」「結構性瓦解」「直接打掉」語氣過強。111 憲判 13 確實打掉「仍可間接識別卻稱非個資」；但若 vendor 證明原始影像不留存、推論結果不可回溯且不連結個人，法律結果仍需 case-by-case。建議改成「大幅削弱」「不能僅憑不識別/不留存即豁免」。

**L3 counter-evidence**: Draft 有提業者 no-identification framing，但沒有完整處理「金色三麥拍照互動可能是消費者主動提供」與「私部門非強制」兩個反論。這是 F4 最大 gap。

**L4 overlooked**: c050/c051/c052/c056 PDPC js_only blocked 已在 What we don't know 提到；但 F4 正文沒有利用 c066「虹膜雖非特種但高識別」摘要層，這本可降低從憲法判決直接跳到餐飲 inference 的壓力。

**L5**: 法律條文/判決 existence strong；「inference framing 在現行法下站不住」應為 contested legal analysis，不宜 overall high。

**L8**: `A∩D` tags OK，但 c097/c098 原場景分別是 B-like identification/state biometric 與健保資料，paragraph 應標示 `source_scope: state/health/identification; application_scope: A∩D by analogy`，否則 L8 scope transfer 太隱形。

### F5 Q4/Q7 — vendor internal split

**L1/L2**: c045 確實支援 D 軸三層 wording；c032/c037/c041 支援 WiXtar/金色三麥公開材料 zero wording。Tier [contested] 合理。

**Overreach**: 「同樣賣 demographic inference SDK / kiosk」把 CyberLink SDK 與 WiXtar/星益欣 kiosk 整合商視為同類，需加 caveat。CyberLink c045 是 restaurant facial recognition marketing，不必然是同一產品責任層或同一部署端。Draft Counter-evidence 有提 SDK vs terminal，但正文「同類 vendor、同類技術」仍太平。

**L3**: CyberLink 是反例，不是 proof WiXtar/星益欣有義務在新聞稿揭露全部 §8 要素。它只證明「vendor 可以公開談知情同意」。建議把「直接打掉 defence」改為「削弱『業界不能寫/不會寫』defence」。

**L4**: 可加入 c044 CyberLink product page 作產品線旁證，但因 c044 是摘要層，非必要。

**L8**: `A∩D; TW; 2023-2026` 基本正確；但 CyberLink source temporal=2023，WiXtar thought leadership=2026，跨時比較應加「不同年份」 caveat。

### F6 D 軸三層對照表

**L1/L2**: 表格把「zero wording」與「無人工替代描述」都標 ✗。前者有來源支撐；後者只能說「公開資料未描述人工替代」，不能說「無人工替代」。這是從 absence of evidence 到 evidence of absence 的典型 overreach。

**Citation problem**: 表格 source 欄只是裸 cid 串，未用 `[cNNN]` 格式；若 integrity checker 只抓 cid 可能過，但正式 citation density 不如其他段。建議改成 `[c032, c033, c042]` 等。

**L5**: CyberLink 的 ✓ 應標「framing wording ✓」而非「實作 ✓」。Draft 第二段有 caveat「未提供 implementable 設計」，但表格視覺上仍容易讓讀者誤讀成 CyberLink 實作合格。

**L4**: 個資法 §8 本身應直接 cite c053，而非只 cite c098。F6 對照標準是 §8 五要素，缺 c053 是 citation gap。

**L8**: 整段 A∩D 正確。表格混合部署終端、中游廠商、上游 SDK 供應商，entity scope 不同；應新增「責任層級」欄，否則 vendor × 同意機制比較有 scope mismatch。

### F7 Q3+Q6 — 四重結構性零

**L1/L2**: 四重結構性零方向正確，但 3,058 件/年表述有重大校準問題。c105/c106 支援 residual buckets 無法辨識 biometric/inference；不支援「A∩D 灰區下界」。這 3,058 是「兩縣市 residual buckets 中可能容納此類投訴的 opaque capacity/proxy」，不是 lower-bound，也不是 inference 投訴數，更不是 unique cases。

**Specific F7 proxy issue**: Draft 寫「新北 services_others 2,235 + 桃園其他 823 = 3,058 件/年兩縣市相加，即為 A∩D 灰區『無 visibility 下界 proxy』」。這應改為「visibility-blind residual pool proxy」。原因：若真正 A∩D 投訴為 0，residual pool 仍是 3,058；因此它不是 lower bound for A∩D complaints。且 c105 另有 business_others 3,074；選 services_others 而排除 business_others 的理由未交代，會被質疑 cherry-picking。

**L2 fidelity**: c105 extract 自身有一處 Passage 1 文字把 113 年 residual 誤寫成 714+432=1,146（其實那是 103 年列），Passage 2 又給 113 年 2,235/3,074。Draft 採 Passage 2，但應註明以 full time-series analysis 為準，避免 extract 內部矛盾被讀者抓住。

**L3**: Draft 有「結構性零非實質零」 caveat，但結尾說「實質零假說站不住」太強。現有證據只能說「實質零不能被確認且有反向風險訊號」，不能說站不住；因為沒有 row-level complaints、沒有消費者調查、沒有現場觀察。

**L4**: Q6 可引用 c079/c080 作全國消保處 portal/statistics context，但 c105/c106/c107 已足夠。司法零 c096 是 accepted snippet，沒有 extract deep-read；draft 有標摘要層，OK。

**L5**: Finding tier [contested] 合理；但 TL;DR 把 3,058 件/年放在核心 bullets，容易被媒體誤讀成投訴量。必須在 TL;DR 同步修正。

**L8**: 段落 tag `temporal:2011-2025; geographic:TW` 是 superset。c105/c106 是 TW-NPT/TW-TYC，c107 只是 metadata；c096 是司法全國摘要。建議各子段落分別 tag，避免把兩縣市 schema 推成全台實證。

### F8 Q5 — 國際對照

**L1/L2**: EU AI Act 限制範圍的 caveat 做得好；c067 支撐「workplace/education」與敏感屬性清單。BIPA/Home Depot c073 作 contested 類比合理。

**Overreach**: 「GDPR Art. 9 + EDPB Opinion 11/2024 才是真正涵蓋商業 demographic inference 的 spine」過強。c077 是機場 FR、重點是 biometric identification/authentication passenger flow；extract caveat 明確說 airport scenario 非餐飲 inference，核心原則可轉用但不是直接涵蓋商業 demographic inference。建議改成「提供 biometric consent/withdrawal 的高標準參照」。

**L2 fidelity**: Draft 說 EDPB 要求「biometric template sole control 原則」，extract caveat 說這是 reduced intrusiveness design pattern，不是 mandatory standard。應降語氣。

**L4 overlooked**: themes t09 包含 c068/c069/c070/c072/c078 等補強 EU/BIPA enforcement trend。Draft 只用 c067/c073/c076/c077，足以回答 Q5，但若維持 [strong]，建議加 c068/c069 以支撐 AI Act 範圍解讀。

**L8**: International paragraphs geographic tags correct (EU/US-IL/SG)，但 conceptual `A∩D` 對 c077 機場 identification source 是 application scope，不是 source scope。應標註 transferability caveat。

## Cross-cutting concerns

**1. 「公開資料無提及」被多次寫成「現場沒有」**  
F2/F6/F7 都有這個問題。c032/c041/c042 等最強支撐是 publication wording vacuum，不是現場 audit。所有「無告示、無人工替代、站到前瞬間被掃描」應改成「公開資料未揭露；需現場查核」或降 tier。

**2. Causal language 太硬**  
「直接打掉」「結構性瓦解」「站不住」「幾乎不可能」應限縮到來源真正支持的子命題。c098 能打掉的是「仍可間接識別卻稱非個資」；不能自動處理所有 no-storage/no-identification implementations。

**3. Paragraph-level L8 scope tags 形式不一致**  
Findings 多數有 HTML scope tag，但 Context、TL;DR、Counter-framing、What we don't know、政策建議沒有。若 L8 要 paragraph-level audit，至少 TL;DR 每 bullet 或每 finding 的 summary bullet 要有 scope；否則 meta-review 很難確認 TL;DR 是否把 source scope 放大。

**4. Single-source/vendor self-claim handling mostly OK，但標題/TL;DR 還需同步**  
F1 正文有把 c033 30+/1000+ 標 contested；TL;DR 和 Finding title 仍可能讓讀者讀成 A 區上界。建議所有出現「30+/1000+」處都固定附「WiXtar fleet claim; inference-enabled subset unknown」。

**5. Rejected-source integrity OK**  
Draft 使用的 cids 皆存在於 accepted.jsonl；未見引用 rejected.jsonl 來源。

**6. Coverage OK**  
Q1a=F1、Q1b=F2、Q2=F3/F6、Q3=F7/F6、Q4=F4/F5、Q5=F8、Q6=F7、Q7=F3/F5/F6。Q3+Q6 合併為 F7 不構成 coverage gap，但 F7 的 Q3 opt-out 實作層仍偏弱，主要是 absence-of-public-info 而非 observed opt-out absence。

## Overall verdict

🟡 publishable with edits

不是推倒重寫；核心架構與 source discipline 大致可用。但發布前必須修三處：F4 降低釋字 603/111 憲判 13 對私部門餐飲 inference 的直接套用語氣；F7 把「3,058 件/年 lower-bound proxy」改成「兩縣市 residual-pool visibility proxy，非 A∩D 投訴量」；F2/F6 全面區分「公開資料未揭露」與「現場實際沒有」。
