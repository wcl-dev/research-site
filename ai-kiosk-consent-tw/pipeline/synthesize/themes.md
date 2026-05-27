# Synthesizer themes — ai-kiosk-consent-tw

**Stage**: 4 (Synthesize) → 5 (Draft)
**Date**: 2026-05-27
**Input**: 27 deep-read extracts (extracts/) · brief_expanded.yaml keyword_expansions · brief.md Q1a/Q1b/Q2–Q7 · accepted.jsonl quality_score

研究焦點:**A∩D 灰區** — demographic inference 型部署 × 同意機制 axis 的交集。本階段把 27
個 deep-read extract 編成 9 個主題,使 Drafter 能按 Q1a/Q1b/Q2–Q7 寫 Findings,並把
operator-confirmed 的「Q3+Q6 四重結構性零」與「Q4 framing-對照 CyberLink internal-split」
escalate 為核心主題。

## 統計總覽

- **主題數**: 9(t01–t09)
- **theme_type 分布**: evidence_cluster ×4(t01/t02/t03/t05)、comparison_framework ×2(t04/t09)、
  narrative_anchor ×2(t06/t08)、regulatory_mechanism ×1(t07)
- **extract 覆蓋**: 27/27 全部指派至 ≥1 主題;unassigned = 0(遠低於 30% 門檻)
  - multi-assignment 合法:c032(t01/t02/t05/t08)、c037(t01/t02/t05/t08)、c041(t01/t02/t05/t08)、
    c055(t06/t07)、c059(t06/t07)、c081(t03/t06)、c082(t03/t06)
- **brief Q 覆蓋**: Q1a(t02/t03/t04)、Q1b(t01)、Q2(t05)、Q3(t06)、Q4(t07/t08)、Q5(t09)、
  Q6(t06)、Q7(t08) — **無 uncovered question**;Q6 與 Q3 合併於 t06 為 operator-confirmed 決策
- **partial_counter_framing**: t08(implied_consent,internal-contradiction rescue)
- **counter / primary balance**: counter=2 theme(t06/t08)/ primary=7 theme;extract 端 t06+t08=10、
  其餘=17,ratio ≈ 1:1.7 — 見下方說明
- **cluster_source 覆蓋**: key_actors(t01/t02/t03/t04)、synonyms(t05)、counter_framings(t06/t08)、
  technical_jargon(t07)、adjacent_concepts(t09)。**5 個 keyword_expansions cluster 全部命中**

## 載重設計原則

brief 失敗條件嚴格要求:(1) A vs B 分軌不混合、(2) Q1a 雙端展開不給單一數字、(3) 同意機制
三層對照表須有具體 wording 引用、(4) 「inference 不算蒐集」必須做完整法律拆解。本階段主題
結構為這些硬要求服務:

- **A vs B 分軌**:t02(A 量化)+ t03(A 歷史)專做 A 區規模,t04 把 B(智取櫃)/ C(POS) 廠商
  顯式 callout 為「do not count toward A」,Drafter 寫 Q1a 清單時不會把 B/C 算進 A。
- **Q1a 雙端展開**:t02 把 c032+c041 一手確認的 2 brand「保守下界」與 c033 引 WiXtar 自主張的
  「30+ 餐飲品牌、1000+ AI Kiosk」上界並列;Drafter 須兩端並列 + tier-tag 標 strong vs contested。
- **Q1a 歷史錨點 vs 當期分軌**:t03 把 TAHR 2014+ 零售 retail FR(7-11/全家/萊爾富/星巴克/屈臣氏)
  獨立成 theme,顯式說「retail 場景非 F&B kiosk、與 2024+ kiosk 部署分軌計算,不可合為單一數字」。
- **Q3+Q6 結構性零 ESCALATE 為核心 finding**:t06 整合四角度(司法零 c096 + 申訴 schema 零
  c105/c106 + 律所/行政院 framing 零 c055/c059 + NGO 量化零 c081/c082),operator-confirmed 是
  本研究最尖銳的單一發現。
- **Q4 framing-對照**:t08 以 CyberLink(c045)自家主動承認知情同意 vs WiXtar/星益欣(c032/c037/c041)
  thought leadership 完全沉默的 vendor internal-split 為 SHARPEST 對照證據,直接打掉「我們是
  vendor 不負責告知」defence。
- **Q4 法律 spine**:t07 把 §6 / §8 法律 + 釋字 603 / 111憲判13 憲法 spine 集成,Drafter 在 Q4 可
  直接引六源建構完整拆解。

## counter / primary balance 說明

`brief_type.intent = surveillance` — 依 Synthesizer 定義,surveillance brief 不強制 counter-framings
對稱拆分。但 brief 含 counter_framings cluster(9 短關鍵字 + counter_framing_keywords 4 keys),
Gatekeeper G4 已 flag balance 為 counter=1/primary=49 的 49:1 asymmetry,並明示「asymmetry 是
structural-from-topic 不是 coverage bug」 — 業者側對 implied_consent / no_storage / no_identification
全為 **OMISSION 而非陳述**(WiXtar/CIO 案例 0 字提同意,而非辯稱「不必同意」)。

本階段對此 topic-structural asymmetry 的處理:

- 建立 **t06**(四重結構性零)+ **t08**(CyberLink vs WiXtar internal-split)兩個 narrative_anchor 主題,
  讓 Drafter 能把「沉默本身就是 D 軸 wording vacuum 的證據」與「同類 vendor 不同 framing 決策」
  兩條反向錨點寫成 Finding。
- **t08 標 `partial_counter_framing.value=true`**,framing_id=`implied_consent`,reason 為「vendor-side
  internal contradiction across vendors — CyberLink 行銷文構成 implied_consent counter-framing 的
  mechanism-inference rescue」。Drafter 應把 t08 寫成 contested-tier framing 對照段(辯論式),
  不寫成主結論 Finding。
- 依步驟 3,surveillance intent 下**不**因 ratio 觸發 `balance_warning`(該規則僅對 comparative/exploratory
  intent 生效)。但本階段顯式建立兩個 counter / narrative-anchor theme(t06/t08)= 10 extracts,
  primary theme 17 extracts,extract 端 ratio ≈ 1:1.7,實際已較 G4 的 49:1 大幅改善。

---

## t01 — Q1b 雙 use-case showcase — 雙月 × WiXtar 與 金色三麥 × 星益欣

- **theme_type**: evidence_cluster
- **cluster_source**: key_actors
- **linked_brief_questions**: Q1b
- **extracts**: c032, c033, c037, c038, c041, c042
- **tier_counts**: strong 3 / contested 2 / speculative 1

兩個 §6b recon 已驗證的代表性 A 區 demographic inference 部署的一手 vendor / 媒體 wording bundle:
雙月食品社 × WiXtar 3-in-1 AI Kiosk「先判斷年齡、性別、語言 → 切換虛擬服務員」,以及金色三麥
× 星益欣「AI 餐酒實驗室」人臉辨識按表情/特徵推薦啤酒 + 桌面偵測。本主題彙整 vendor 一手新聞稿
+ 數位時代 / CIO Taiwan / TechNews / Marie Claire 多源報導,以供 Drafter 寫消費者使用情境完整時間軸
+ 可見 / 不可見動作 + 資料 artifact 流向(brief success criteria #2)。

## t02 — Q1a 量化部署測繪 — 保守下界 vs vendor-claimed 上界(雙端展開)

- **theme_type**: evidence_cluster
- **cluster_source**: key_actors
- **linked_brief_questions**: Q1a
- **extracts**: c032, c033, c037, c041
- **tier_counts**: strong 2 / contested 2

台灣餐飲業 A 區 demographic inference kiosk 部署規模的雙端量化:**保守下界**為 c032 雙月 + c041
金色三麥 = 2 brand 一手確認 inference;**vendor-claimed 上界**為 c033 BNext 引 WiXtar 自主張
「30+ 餐飲品牌、超過 1000 台 AI Kiosk」(inference 啟用比例 vendor 未公開,屬 contested tier);
c037 WiXtar 自家 thought leadership 把 VLM / inference 列為 2026 七大模組標配,作為「業界趨勢」
旁證。Drafter 須兩端並列、不可給單一數字;tier 標註:下界 strong、上界 contested 並註 vendor self-claim。

## t03 — Q1a 歷史錨點 — 2014+ 零售/超商 retail FR「搜集族群投放廣告」(與 2024+ F&B kiosk 分軌計算)

- **theme_type**: evidence_cluster
- **cluster_source**: key_actors
- **linked_brief_questions**: Q1a
- **extracts**: c081, c082
- **tier_counts**: contested 2

TAHR 一手記載至少 2014 年起 7-11/全家/萊爾富/星巴克/屈臣氏結帳櫃台上方已部署人臉辨識
「搜集客戶族群資料投放廣告」,技術型態屬 A 區 demographic inference(族群分類 → 廣告投放),
非 B 區身分比對。為 Q1a 提供 10+ 年「告知/同意機制長期缺席」的縱貫錨點。**但這是 retail/超商
場景而非 F&B kiosk** — Drafter 必須與 2024+ kiosk 部署數**分軌計算**,不可合為單一規模數字;
此分軌是 brief 失敗條件「把 A 跟 B 混為一談」的延伸要求(時代軸的混淆同樣會膨脹數字)。

## t04 — B/C contrast — 智取櫃身分比對 / 拍檔 POS / Berry 廚房分析(do not count toward A)

- **theme_type**: comparison_framework
- **cluster_source**: key_actors
- **linked_brief_questions**: Q1a
- **extracts**: c046, c047, c049
- **tier_counts**: speculative 3

作為 A 區純度 firewall 的對照背景。c049 銓幻元 MCS 智取櫃 99% 相似度比對既有資料庫(B 區
identification);c046 拍檔科技 30% 連鎖餐飲市占但功能為 POS + member 推薦(C 區);c047 Berry AI
廚房 inventory + 人計數 operations analytics(B 區但屬營運分析非身分比對)。Drafter 必須引這些
record 作為 callout,確保 Q1a 量化清單不把 B/C 廠商算進 A 區 inference 部署數;**此為 brief
失敗條件之一**(「把 A 跟 B 混為一談給出膨脹的部署數字」)。

## t05 — Q2 告知層 — A 區 vendor 頁/媒體報導全面 D 軸 wording vacuum

- **theme_type**: evidence_cluster
- **cluster_source**: synonyms
- **linked_brief_questions**: Q2
- **extracts**: c032, c037, c038, c041, c042
- **tier_counts**: strong 3 / contested 1 / speculative 1

inference 型部署在「告知」層的 vendor / 媒體 wording 實況:c032 雙月 WiXtar 一手新聞稿 0 字提
同意/告知/隱私;c041 CIO Taiwan 金色三麥詳細報導 0 字提;c037 WiXtar thought leadership 0 字提;
c042 Marie Claire 消費者體驗報導 0 字提;c038 TechNews 星益欣 × 金色三麥報導 0 字提。**五源
cross-confirmed** — vendor 在主動 framing 自家功能時連 boilerplate 隱私聲明都沒提,wording vacuum
本身就是 Q2 對個資法第 8 條(蒐集目的/項目/留存期限/傳輸對象/撤回機制)落差的最直接證據。

## t06 — Q3+Q6 灰區的結構性沉默 — 四重結構性零(operator-confirmed core finding ⚡)

- **theme_type**: narrative_anchor
- **cluster_source**: counter_framings
- **linked_brief_questions**: Q3, Q6
- **extracts**: c055, c059, c081, c082, c105, c106, c107
- **tier_counts**: contested 4 / speculative 3

⚡ **本研究最尖銳的單一發現**,operator-confirmed escalate as core theme。四個角度獨立確認 A∩D
灰區的結構性「不可見」:

1. **司法零** — c096(Q6 quantitative;Segmenter INDEX 中 fast-skip 但 Drafter 可摘要層引用):
   司法院 35 judgments 含人臉辨識/生物特徵,**0** 在餐飲 inference 場景。
2. **申訴 schema 零** — c105 新北市 12 年縱貫(103-114 年)18+ category + c106 桃園市(109-114 年)
   25 category,均無 biometric / 個資 / inference 獨立 column;只能歸入 "其他" residual buckets
   (新北 113 年 services_others 2,235 件、桃園 113 年 其他 823 件,各占 18-20%);c107 台中市
   row-level 因 DNS proxy failure 未取得,僅 schema metadata 層 corroborate。
3. **律所/行政院 framing 零** — c055 fblaw 律所對 2025/11/11 修法分析 + c059 行政院 PDPC 修法新聞,
   均未觸及 §6 inference 灰區;修法核心為 PDPC 組織建構,§6 特種個資定義未動。
4. **NGO 量化零** — c081/c082 TAHR 雖有立場(「匿名化即不算個資」業者 framing 應 push-back)
   但無具體投訴/案件量化數據。

Q3(退出層,消費者不能 opt-out)與 Q6(執法現況,零案例)合併處理 — operator-confirmed 決策。
**不是「沒有問題」,是「沒有資料」就是核心發現** — Drafter 應把此 theme 寫成「為何結構性零是
A∩D 灰區的最強證據」的 Finding,並把 schema-zero 的 residual bucket 「隱形池」量化(2,235 + 823
= 3,058 件/年 兩縣市相加)當作「無 visibility」的下界 proxy。

## t07 — Q4 法律屬性 — 個資法 §6 / §8 spine + 釋字 603 / 111憲判13 憲法 spine

- **theme_type**: regulatory_mechanism
- **cluster_source**: technical_jargon
- **linked_brief_questions**: Q4
- **extracts**: c053, c054, c055, c059, c097, c098
- **tier_counts**: strong 4 / contested 2

「inference 不算個資蒐集」業者 framing 法律拆解的 spine 證據。

**法律層**:c053 個資法本文(2025/11/11 修法後現行版本)、c054 §6 特種個資定義(**人臉/聲紋
未列入**)、c055 fblaw 律所對修法核心為 PDPC 組織建構而非 §6 inference 灰區的分析、c059 行政院
新聞與「建立 AI 全面應用時代資料治理」立法理由 + 6 年過渡期。

**憲法 spine**:c097 釋字 603(2005 指紋身分證案)— 資訊隱私權 + 比例原則中度審查 + 目的須法律
明定 + 組織程序防護;c098 111 憲判 13(個資法 §6 I 4)— 事後控制權 + 比例原則 + 「相關機關 3 年內
應修法」 → 2025/11/11 修法即為直接回應。

Drafter 在 Q4 可直接引此六源建構完整法律拆解:**(a)** §6 未把人臉列入特種個資不等於業者可主張
inference 不算蒐集;**(b)** 「高識別力的一般個資」邏輯仍受 §8 告知義務拘束;**(c)** 釋字 603 已確立
資訊隱私權對指紋此類生物特徵的保護 spine,demographic inference 為其延伸;**(d)** 111憲判13 + 修法
共同強化 PDPC 監管職權。

## t08 — Q4/Q7 framing-對照 SHARPEST — CyberLink 自家承認知情同意 vs WiXtar/星益欣完全沉默(vendor internal split)

- **theme_type**: narrative_anchor
- **cluster_source**: counter_framings
- **linked_brief_questions**: Q4, Q7
- **extracts**: c032, c037, c041, c045
- **tier_counts**: strong 3 / contested 1
- **partial_counter_framing**: `true` — framing_id `implied_consent`
  - reason: counter-framing rescue via internal contradiction across vendors — 業者側對
    implied_consent / no_storage / no_identification 全為 OMISSION 而非陳述(G4-flagged:
    counter=1/primary=49 為 topic-structural,業者用沉默而非辯論);CyberLink (c045) 在自家
    行銷文中主動承認知情同意,構成 vendor-side 內部矛盾,作為 implied_consent counter-framing
    的 mechanism-inference rescue。
- **conflicts**:
  - **c045 vs c032** on「Q4 — vendor 是否須告知/同意」:CyberLink FaceMe 自家行銷文主動承認
    「需知情同意 + 用戶有權刪除」;WiXtar 雙月 vendor 一手頁面 zero consent wording。同類 vendor、
    同 inference SDK 路徑、相反 framing 決策。
  - **c045 vs c041** on「Q7 — vendor 對個資法 §8 告知事項落差」:CyberLink 對告知/選擇/撤回
    三層皆有 wording;CIO Taiwan 金色三麥 × 星益欣詳細報導對三層皆無 wording。Drafter 應對照
    §8 應告知五要素逐項勾選兩 vendor 落差。

同類 vendor、同類技術、不同 framing 的內部對照。c045 CyberLink FaceMe 餐飲應用 marketing 主動
承認「人臉辨識屬個資、需用戶知情同意、用戶有權隨時取消/刪除」— 是台灣 vendor 自家行銷文中
對 D 軸三層完整承認的孤例。對照 c032 WiXtar 雙月案例頁 + c037 WiXtar 2026 餐飲 AI 趨勢攻略
+ c041 CIO Taiwan 金色三麥報導 — 三源 zero consent wording。**這證明「業界 wording vacuum
不是法遵不能寫,而是 vendor framing 選擇」**,直接打掉 WiXtar/星益欣潛在的「我們是 vendor
不負責告知」defence。Drafter 應把本主題寫成 contested-tier framing 對照段(辯論式)+ 同意機制
三層對照表(brief success criteria #3)。

## t09 — Q5 國際對照最低標準 — EU AI Act Art.5 + GDPR Art.9 + BIPA + SG PDPA

- **theme_type**: comparison_framework
- **cluster_source**: adjacent_concepts
- **linked_brief_questions**: Q5
- **extracts**: c067, c068, c069, c073, c076, c077
- **tier_counts**: strong 3 / contested 3

國際對 inference 型生物特徵在商業空間的最低標準:c067 EU AI Act Article 5 禁令原文(emotion
recognition 在 workplace/edu 全禁、biometric categorisation 條件禁);c068 EC AI Act Service Desk
對 Art.5 官方解析;c069 FPF Red Lines 對 emotion recognition 禁令範圍商業場合是否涵蓋的細部討論;
c073 Home Depot self-checkout BIPA 集體訴訟(Q5 最接近台灣餐飲 kiosk 的國際先例);c076 新加坡
PDPC biometric 指引(scope 排除 commercial inference、留待 future guidance 的同類監管機構漸進
路徑);c077 EDPB Opinion 11/2024 機場 FR(GDPR Art.9 explicit consent + biometric template sole
control 原則)。Drafter 在 Q5 用六源建構「最低標準對台灣 PDPC 籌備中政策的借鏡建議」段
(brief success criteria #4 + 政策建議)。

---

## Drafter 交接備註

1. **A vs B 分軌是硬要求**:t02(A 量化)+ t03(A 歷史)+ t04(B/C contrast)分屬不同主題,
   Drafter 須維持 A 區清單純度,引 t04 顯式 callout「智取櫃/拍檔/Berry 不算 A」。
2. **Q1a 雙端展開(operator-confirmed)**:t02 把保守下界(2 brand)+ vendor 上界(30+ brand、
   1000+ kiosk)兩端並列,tier-tag 標 strong vs contested,Drafter 不可只給單一數字;歷史錨點
   (t03)10+ 年 retail FR 與 2024+ F&B kiosk 分軌,不合為一個規模數。
3. **Q3+Q6 結構性零是核心 finding(operator-confirmed escalate)**:t06 寫成本研究主軸 Finding
   之一,強調「四重結構性零」+「申訴 schema 隱形池」(新北 services_others 2,235 + 桃園 其他 823
   = 3,058 件/年兩縣市相加 lower bound proxy);Q6 不獨立寫節,合併進 Q3 結構性零段。
4. **Q4 framing-對照 CyberLink internal-split**:t08 寫成 contested-tier framing 對照段(辯論式),
   同時用 c045 vendor self-admission 打掉「業界寫法是統一沉默」的論述;t08 與 t07 法律 spine
   配合,Drafter 在 Q4 同時做「法律分析」+「framing 對照」雙軸。
5. **同意機制三層對照表(brief success criteria #3)**:Drafter 從 t05(告知層 vendor wording vacuum)
   + t08(三層對照 c045 vs c032/c037/c041)兩主題合成業者 × 告知/選擇/撤回的勾選表。
6. **partial_counter_framing(t08)**:寫成 caveat / contested-tier 段落,不寫成主結論;
   cross-reference counter_framing_keywords 的 implied_consent。
7. **摘要層 sourcing**:c038 TechNews「八維智能/典通客層辨識」精確 wording 須回到 accepted snippet
   並標 contested(WebFetch 未確認原 wording);c050-052 PDPC 函釋全文未取得,但 c055/c059 律所
   + 行政院 parallel coverage 已足。
8. **c107 台中 row-level 缺失**:t06 已用 c105/c106 row-level + c107 metadata-level 三角化;Drafter
   若需 row-level confirm 可請 operator 救援,但已不阻塞 Q6 結構性零的結論。
