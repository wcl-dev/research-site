# Off-diagonal analysis — join-petition-typology-tw

**v1 · 2026-06-18** · 對應 [brief.md](../brief.md) Q3–Q4 · 資料 [coding/coded.jsonl](../coding/coded.jsonl)（1,076 件）

## 方法
- **設計**：case-control 樣本（全部 162 成案 + 214 高附議對照 + 700 分層隨機長尾 = 1,076）。成案在樣本中被過取樣約 12×（樣本內 15% vs 母體 1.26%）。
- **編碼**：1,064 件由 45 個 sonnet agent 依 [codebook.md](../coding/codebook.md) v1.1 編碼；12 件人工補編。校準驗證：20 件中對得上的 11 件，form 一致 91%、motive 一致 91%（含「民粹重刑→motive0」等硬規則機器全中）。
- **模型**：logistic regression（純 python GD，無 SE/p-value）。**case-control 設計保留 odds ratio 不偏**，但截距與絕對機率不可解讀為母體率。

## 主結果 — odds ratio

`crossed ~ form_score + motive + constituency + org_assoc + org_ngo + ai_essay`（n=1,076）

| 變項 | OR/單位 | 方向 | 解讀 |
|---|---:|:--:|---|
| **org_backing = ngo** | **10.9×** | ▲▲▲ | **組織後盾＝萬能鑰匙** |
| **org_backing = assoc** | **7.2×** | ▲▲▲ | 職業/產業協會領銜 |
| form_score | 2.0× | ▲ | 審議品質**有**獨立效果，但次要 |
| constituency | 1.4× | ▲ | 潛在群體規模，溫和 |
| **motive（工具型 0→2）** | **0.55×** | ▼ | **控制 form 後為負**：同等品質下越問題解決取向越不易成案 |
| ai_essay | 1.3× | · | 可忽略 |
| media_window | 0.74× | · | **null**（見下）。納入後其他係數全不動 → 核心發現穩健 |

**media_window（事件時機）為 null**：依 `data/events_timeline.yaml`（15 個重大社會事件，topic+提送日落在事件後 8 週內）編碼，105/1,076 件命中。window=1 成案率 12.4% 反略低於 window=0 的 15.3%（OR 0.74）。**這是粗測量的稀釋**：時間線月精度、只比 topic 不比關鍵字，「剴剴案後 8 週任何兒少提案都算命中」把大量無關提案算進去。pilot 觀察到的「剴剴案→兒虐提案叢發成案」是顯著個案 pattern，但在此粗測量下不構成強的母體層效果。**關鍵：納入 media_window 後 form(1.99)/motive(0.55)/org(7–11×) 係數全不變，核心發現對其穩健。** v2 可改關鍵字級事件比對收窄。

## Off-diagonal 結構（樣本內次數，讀關聯不讀絕對率）

```
                 died   crossed
form_hi(2-3)      533     129
form_lo(0-1)      381      33
  ─────────────────────────
org_backed         22      35     ← 61.4% 成案
no_org            892     127     ← ~13% (樣本內)
```

**最致命對照**：
- **高 form × 無組織後盾**：607 件，成案 96（樣本內 15.8%，母體真實率約 1–2%）。← 認真寫、沒人撐 = 死。
- **有組織後盾（任何 form）**：57 件，成案 35（**61.4%**）。← 有人催票 = 過半成案。

## 三點發現

1. **組織動員是主變項**（OR 7–11×），量級壓過其他所有變項。`assoc`（全教總、職業/產業協會）與 `ngo`（倡議基金會聯署）把成案機率拉高近一個數量級。
2. **審議品質（form_score）次要但非零**（OR ~2×/單位）。這**修正了 pilot 的過度宣稱**（pilot 在 48 件上說品質幾乎無關）——品質有獨立效果，只是絕大多數高品質提案沒有組織後盾仍然石沉（607 件高 form 無組織，母體真實成案率約個位數%）。
3. **工具型動機是輕微負債**（OR 0.55，控制 form 後）。同等文本品質下，**越是情緒/表達框架越能動員、越是冷靜問題解決越容易被忽略**。這是「平台獎勵動員強度、非政策 merit」最銳利的量化版本——也呼應原文 IPSR 的 expressive↔instrumental 軸：在 Join 的門檻機制下，expressive 端在動員上佔優。

→ **「許願池」成見的裁決**：半對半錯。錯在「提案都很爛」——大量 form=3、問題導向的認真提案存在；對在「沒用」——但**沒用的原因不是品質差，是門檻機制把無組織後盾的認真提案系統性篩掉，並對情緒/動員框架加分**。

## 穩健性附錄（v2，回應 review）

**Stage-1 org OR 隨對照組組成劇變 → 改以 IPW 加權母體估計為準：**

| 規格 | org_assoc | org_ngo | form | motive |
|---|---:|---:|---:|---:|
| full 未加權 | 7.2× | 10.9× | 1.97 | 0.56 |
| 僅 cases+高附議對照 | 2.8× | 4.3× | 1.53 | 0.56 |
| 僅 cases+長尾 | 20.5× | 26.8× | 2.18 | 0.55 |
| **full IPW 加權（母體估計）** | **17.8×** | **19.7×** | 1.98 | 0.57 |

→ org 的「7–11×」是對照組混合的產物；**母體加權估計 ~18–20×（效果更大）**。form(1.5–2.2)/motive(~0.56) 跨組穩定。
加權母體率：**高form·無組織 1.41% vs 組織後盾 22.2%**（overall 1.26% sanity 對上）→ 取代未加權的 607/15.8% 與 57/61.4%。

**motive 0.56 是 suppression（非 finding）**：motive 單獨 OR **1.25**（正）、去 form 後 1.05、加 form 才 0.56；crude 跨門檻 motive=2 **16.9% > ** motive=0 12.1%。form×motive 格：form=3 有 **411/422** 是 motive=2，負係數其實建在 form=3·motive=0 的 **7 件**上。r(form,motive)=0.70。→ 報告為「net of form 的條件殘差對比」，非「工具型動機是負債」。

## Q5 — 回應層：兩階段門（capstone）

162 件成案的官方機關回應全抓到（`analysis/responses.jsonl`，100% 有回應、中位數 2,294 字）；160 件由 workflow 分類 substantive/partial/boilerplate（`analysis/crossers_with_response.jsonl`）。**此層為全體成案母體，回應率＝真實率，無 case-control 加權問題。**

整體：**boilerplate 47%(75) / partial 33%(53) / substantive 20%(32)**；committed 42%。**跨過門檻 ≠ 換到行動——近半成案拿罐頭。**

回應品質 by 輸入端編碼（substantive%）：

| 輸入端 | substantive% | committed% |
|---|---:|---:|
| motive=0（表達型） | **4%** (1/28) | 32% |
| motive=2（工具型） | **24%** (27/114) | 45% |
| form_score=0 | 8% | 31% |
| form_score=3 | **26%** (25/95) | 49% |
| 組織後盾成案 (assoc+ngo) | 15% | 35% |
| 個人·高form·工具型成案 | **27%** (22/82) | 48% |
| 表達型動機成案 (motive=0) | **4%** | 32% |

**核心發現 — 兩道門、選擇標準相反：**
- **Gate 1（跨 5000 附議＝被聽見）**：靠**動員**（org_backing OR 7–11×，§主結果），審議品質次要，工具型動機甚至是負債（OR 0.55）。
- **Gate 2（成案後換到實質回應＝被行動）**：靠**審議品質**（form 8%→26%、工具型 motive 4%→24% 單調遞增），**動員幫不上忙**（組織後盾成案 substantive 僅 15% < 個人高品質 27%；ngo 更只 8%）。

→ **平台在入口獎勵動員、在回應獎勵品質，兩標準錯位。** 最具審議品質、最能換到實質回應的提案（motive=2、form=3），**恰恰是最不容易擠過 Gate 1 的那些**（Stage 1 motive OR 0.55），除非自帶組織後盾。這是 IPSR 原文（無結果資料）做不到的延伸：expressive↔instrumental 軸在兩道門預測**相反**的結果。組織動員型成案常推單一議題/民粹訴求被機關以罐頭擋下；冷靜的工具型提案一旦擠過門檻則較能換到實質回應。

## 限制與下一步
- **無 SE/p-value**：純 python GD 只給點估計；org_backing 效果量級巨大顯然穩健，form(2×)/motive(0.55×) 需正式推論（裝 statsmodels 重跑加信賴區間）。
- **org_backing 偵測未獨立驗證**：僅 57 件被判有組織後盾；雖在校準 91% 一致內，仍建議抽查這 57 件的署名是否真有協會/NGO 領銜。
- ✅ **media_window 已納入**（`data/events_timeline.yaml`，15 事件），結果 null（見主結果表注）；v2 可改關鍵字級比對收窄低 recall 問題。
- **motive 負 OR 含共線性**：motive 與 form 正相關，此為「控制 form 後的殘差效果」，解讀須謹慎。
- ✅ 回應層（Q5）已完成（見上節）。2 件分類漏回（160/162）、部分 cell 偏小（motive=0 n=28）；motive(4%→24%)/form(8%→26%) 梯度仍清楚。org_backing 偵測那 57 件仍建議抽查署名。
