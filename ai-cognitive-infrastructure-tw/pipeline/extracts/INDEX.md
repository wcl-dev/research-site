# Segmenter index — ai-cognitive-infrastructure-tw

Deep-read budget: 24 / Prioritized: 24 (of 43 accepted)

研究焦點:**四連結因果鏈的證據審計**(L1 價格→採用 / L2 AI 為資訊入口 / L3 穩定框架 / L4a 同質化 · L4b 個人信念位移 · L4c 社會層聚合)。深讀以兩個 LOAD-BEARING 精度點為核心:**(1) Waight c002 的 EXACT scope 用語**(相關性 + continued-pretraining 因果,且不作 user-belief 主張),**(2) L4b 說服 RCT 的 BOUNDEDNESS**(c023-c031,證明 bounded 個人層 capability,未證 single-dominant-model 的 L4c 人口層位移)。所有 extract 嚴守 L3/L4 邊界與 market-data containment。

## 關鍵發現(供 Drafter)

- **Waight c002 scope 已逐字鎖定**(PubMed PMID 42129566 全文 abstract + 作者 project site):「This result is correlational」逐字確認;因果僅在 model-output 層(continued-pretraining Llama-2-13b + 6,400 docs → ~80% pro-gov,後者數字來自 project site 非 abstract);"persuasive potential" 僅作背景引用(refs 1-10)與結尾前瞻推論("shaping LLM output"),**非 Waight 自身測得結果**。Drafter 可逐字背書 Waight = strict L3。
- **L4b→L4c 斷點已用逐字 bound 封住**:Hackenburg c026「current frontier models are barely more persuasive than models smaller in size by an order of magnitude or more」+ Chen/Kalla/Le c027「LLMs do not currently pose a substantially greater threat to democratic societies through mass persuasion than existing human-driven methods」「their real-world impact is constrained by scale」。**c027 是最高 over-read 風險**(title 含 "democratic societies" 但 data 為個人層、結論為 bounded)——Passage 2 已備好用來中和標題。
- **L3→L4b on-chain joint 已逐字取得(c028 RESCUED)**:Shu/Karell PNAS Nexus(N=1,912,US-pop-proportional,GPT-4o vs Wikipedia,兩事件 SGS/TWLF,三框架)——**latent(預設、未指示)框架**即可移動個人意見(default d=0.14;liberal d=0.28;conservative d=−0.13)。這是「stable model framing(L3)→ 個人意見位移(L4b)」最乾淨的一手 joint。**但仍嚴守 L4b**:effect 小、conservative 臂僅在「本來就保守」子群顯著、作者自陳僅兩事件且 latent bias 因模型而異——三項皆 REINFORCE L4b→L4c 斷點。與 c027 同等 over-read 處理。原因 Co4「no open PDF」為誤判(PNAS Nexus 為 OA + PMC 全文),已 RESTORE 至 qs=4。
- **L3 killer mechanism(c001 abliteration)逐字取得**:同一模型 abliterated 版本主動產生台灣主流史學語彙→框架是 post-training/RLHF,非 corpus absence。與 c018(「root causes ... likely embedded within the LLM's alignment processes」)、c043(「All tested models, regardless of their origin, exhibit remarkably similar patterns」)三點獨立收斂於「alignment-sourced, not corpus/intent-sourced」。
- **L3 對稱測試已備**:Buyl c003(US 模型內部分歧 + 中國模型 internal/domestic 分裂,雙向)+ Samokhodskyi c004(西方模型 "false balance"/"bothsidesism" 逐字:「They manufacture doubt where evidence is clear」)——guard directional artifact。
- **市場數據 snapshot 三筆 as-of 2026-06-08 已成 clean quotable**(c010 價差 ~51-460x / c011 下載量 Qwen+DeepSeek / c012 token-share 1.2%→~13%,含 window guard)。Containment:僅證 L1。
- **L4a disconfirming(c035 Elon / c036 Pew)**:concentration AND diversity 並存;ChatGPT 主導但多模型分散。c035 的「多模型」結論為 overlapping % 推論,非逐字陳述(已標)。
- **L4c indirect-only(c032 framework / c033 simulation / c034 analogy)逐字確認 empty cell**:c032「defines this emerging area ... lays out a program of research」、c033 為 LLM-agent 模擬(連模擬都需 prompt-induce confirmation bias 才像人)。empty cell 即是發現。
- **§6 anti-alarmism 三錨**:c042(framing 為 RLHF/HHH sociotechnical artifact)+ c043(framing mutable/data-attributable)+ c044(「integration ... alongside conventional methodologies」——LLM output≠population opinion,直擊 L4c 推論)。
- **L2 guard(c014 Reuters DNR)逐字**:chat-LLM 新聞使用 7%(under-25 15%/India 18%)vs AI Overviews 4%,兩機制明確分離。
- **c041 FDD 經 Wayback 深讀**:LLM 引用 state-aligned propaganda 占 57% 回應(~180 題 × 3 衝突含 Taiwan-China)——intermediation channel(FW/L2-L3 bridge);含 paywall-asymmetry 結構性解釋(§6-adjacent)。

## Deep-read (depth 1 — must;兩 load-bearing 精度點 + 各鏈 anchor)

### L3 — 最強鏈 + 對稱測試 + killer mechanism
- **c001** [conceptual: L3]: repo-internal 一手 abliteration 證據——同模型去對齊後產生台灣主流史學語彙→框架是 post-training/RLHF 非 corpus 缺漏。L3 killer mechanism。逐字取自 insight_v3.md §4.2/4.3。
- **c002** [conceptual: L3 | LOAD-BEARING]: Waight Nature 2026。EXACT scope 逐字鎖定(PubMed 全文 abstract):correlational cross-national audit + continued-pretraining 因果僅在 output 層 + 不作 user-belief 主張。access=partial(paywall,scope 由 2 一手源確認)。
- **c003** [conceptual: L3]: Buyl「LLMs reflect ideology of creators」——19 模型對稱,US 模型內部 + 中國模型 internal/domestic 雙向分歧。directional-artifact guard。
- **c004** [conceptual: L3]: Samokhodskyi/ELN——cross-lingual + 西方模型 "false balance" 逐字。think-tank qs=4。

### L4a — 同質化 anchor + LLM-specific 經驗 + disconfirming
- **c017** [conceptual: L4a]: Kleinberg & Raghavan monoculture anchor。SCOPE NOTE 載重:對象為 hiring/lending 決策系統,非 LLM info-output;延伸到 LLM 是 open question。
- **c018** [conceptual: L4a]: Generative Monoculture——LLM-specific output-diversity narrowing 經驗示範;root cause「embedded within ... alignment processes」(與 c001/c043 收斂)。
- **c035** [conceptual: L4a]: Elon survey——多模型使用 disconfirming(% overlap 推論,已標非逐字)。
- **c036** [conceptual: L4a]: Pew teens——population-rep,concentration+diversity 並存。authoritative。

### L4b — bounded capability(斷點 bound)+ L3→L4b on-chain joint
- **c023** [conceptual: L4b]: Costello/Pennycook/Rand Science——N=2,190,~20% reduction,durable 2mo。逐字 via Wayback。方向=debunking(需與 c031 配對)。
- **c024** [conceptual: L4b]: Salvi Nat Hum Behav——81.7% higher odds WITH personalization;WITHOUT 為 non-significant(p=0.31)。conditional bound。逐字 via arXiv。
- **c026** [conceptual: L4b | LOAD-BEARING bound]: Hackenburg PNAS——log scaling law,frontier「barely more persuasive」。封 L4b→L4c inflation。逐字 via arXiv。
- **c027** [conceptual: L4b | 最高 over-read 風險]: Chen/Kalla/Le N=10,417——title「democratic societies」但 data 個人層、結論 bounded(「not ... a substantially greater threat ... than ... human-driven methods」)。逐字 via Cambridge。
- **c028** [conceptual: L3,L4b | MOST ON-CHAIN L4b · RESCUED]: Shu/Karell PNAS Nexus N=1,912(US-pop-proportional,GPT-4o vs Wikipedia,SGS/TWLF 兩事件,三框架)——**latent(預設、未指示)框架即移動個人意見**(default d=0.14 P<0.05;liberal d=0.28 P<0.001 across all groups;conservative d=−0.13 P<0.05 但僅本就保守者顯著)。L3→L4b 最乾淨一手 joint。**仍 STRICT L4b**:小 effect + conservative 子群限定 + 作者自陳僅兩事件/latent bias 因模型而異 → 三項皆 REINFORCE L4b→L4c 斷點。逐字 via PMC OA 全文(PMC12954675)。qs=4 RESTORED(Co4「no open PDF」為誤判)。
- **c031** [conceptual: L4b]: LLM convince conspiracies——valence symmetry(N=2,724,「as effective at increasing ... as decreasing」)。逐字 via arXiv。

### L4c — indirect-only(empty cell 三證)
- **c032** [conceptual: L4c | FRAMEWORK ONLY]: Carley social cybersecurity——「defines this emerging area」。逐字。
- **c033** [conceptual: L4c | SIMULATION ONLY]: Chuang LLM-agent opinion dynamics——模擬非真人。逐字 via ACL Anthology。

### L1 — primary market snapshot(containment,as-of 2026-06-08)
- **c010** [conceptual: L1]: OpenRouter live pricing——價差 ~51-460x。primary API。
- **c011** [conceptual: L1]: HuggingFace downloads——Qwen+DeepSeek 主導。primary API。
- **c012** [conceptual: L1]: OpenRouter State of AI 2025——token-share 1.2%→~13%(含 window guard)。

### L2 — AI 資訊入口(含 mandatory guard)
- **c014** [conceptual: L2]: Reuters DNR 2025——chat-LLM 7% vs AI Overviews 4%,兩機制分離逐字。strongest L2。

### FW / §6 — intermediation + anti-alarmism
- **c041** [conceptual: FW,L2,L3]: FDD propaganda-in-citations——57% 回應引 state-aligned(含 Taiwan-China)。deep-read via Wayback 2026-03-15。qs=3。
- **c042** [conceptual: CE,L3]: RLHF sociotechnical limits——framing 為 alignment artifact 非 intent。§6 核心。逐字。
- **c043** [conceptual: CE,L4a]: LLMs & Cultural Values——framing mutable/data-attributable + cross-origin convergence。逐字 via arXiv。
- **c044** [conceptual: CE,L4c]: Qu & Wang——LLM output≠population opinion「alongside conventional methodologies」。直擊 L4c 推論。逐字。

## Fast-skip — snippet-layer usable (Dr3 secondary evidence)

以下 accepted 記錄含具實質內容摘要(具名 entity / 數字 / 可引主張),Drafter 在 Dr3 規則下可作 secondary evidence(cap 至 contested tier,須註明依摘要層 sourcing 未經 deep-read 一手驗證)。多數為各鏈已被 depth-1 anchor 充分覆蓋後的 corroborating 記錄,故 fast-skip。

### L3 對稱測試補充(已由 c001-c004 覆蓋)
- c005: (`access_status: ok`, `snippet_status: usable`) — https://arxiv.org/abs/2503.23688 — Guey 11-model 雙語 dual-framing US-China benchmark;摘要含「US-origin→pro-US, China-origin→pro-China」對稱 mapping。Drafter 可引摘要作 L3 對稱第三證(c003/c004 已為主錨)。
- c006: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.3390/socsci12030148 — Rozado「Political Biases of ChatGPT」;摘要含「systematic left-leaning bias across a battery of instruments」具體可引,Drafter 在 L3 西方模型 lean 可引摘要(2023 foundational)。
- c007: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.18653/v1/2023.acl-long.656 — Feng et al. ACL「pretraining data→model→downstream」;摘要載「training-data political slant propagates to predictions」——L3 training→output 通道,Waight c002 後來因果確認的前身。Drafter 可引摘要作 L3 機制前置。

### L1 因果臂 + 採用驅動文獻
- c008: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.70777/si.v2i1.11097 — DeepSeek R1 open-weight frontier event;摘要載「fraction of frontier cost yet competitive despite US GPU export bans」——L1 price-vs-capability 文獻臂(non-snapshot)。Drafter 可引摘要。
- c009: (`access_status: ok`, `snippet_status: usable`) — https://arxiv.org/abs/2605.02821 — hosted open-weight API 為「provider-specific, time-varying service object」;摘要點明「same model, many prices/behaviors」——銳化 L1 causal-identification 問題。Drafter 可引摘要。

### L4a 同質化補充(已由 c017/c018 覆蓋)
- c019: (`access_status: ok`, `snippet_status: usable`) — https://arxiv.org/abs/2211.13972 — Bommasani et al.「Picking on the Same Person」outcome homogenization 經驗測試;SCOPE 同 c017(決策系統非 info-output)。Drafter 可引摘要作 c017→經驗橋。
- c020: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.1007/s10676-025-09845-2 — Rudko「ChatGPT incredible at being average」;摘要載 LLM output「highly uniform, average」homogenization——L4a response-level。qs=3 conceptual。Drafter 可引摘要。
- c022: (`access_status: ok`, `snippet_status: usable`) — https://arxiv.org/abs/2604.09502 — Strategic Algorithmic Monoculture(AI-agent coordination games, 2026);摘要區分 primary/strategic monoculture。SCOPE:AI-agent 非人類資訊消費,延伸 partial。Drafter 可引摘要作 L4a 最新層。

### L4b 補充(已由 c023-c031 覆蓋)
- c025: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.1073/pnas.2412815122 — Argyle et al. PNAS「Testing theories of political persuasion using AI」;摘要載 human-subject attitude-change 機制測量——L4b 個人層 corroboration。Drafter 可引摘要。
- c029: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.18653/v1/2024.acl-long.858「Earth is Flat because...」;摘要點明 persuasion 測於 MODEL 非人類——L4b 方法論邊界 marker(model-as-subject vs scarcer human-as-subject)。Drafter 引摘要時須標 model-as-subject。
- c030: (`access_status: ok`, `snippet_status: usable`) — https://www.nature.com/articles/s41467-025-61345-5 — Nat Comms「LLM messages persuade humans on policy issues」;摘要為 human-subject attitude shift——L4b capability corroboration。Drafter 可引摘要。

### L4c analogy(label-only)+ FW frameworks
- c034: (`access_status: ss_landing_no_open_pdf`, `snippet_status: usable`) — semanticscholar slug(2024 Pakistani elections agenda-setting);摘要為 social-media population-scale agenda-setting——**ANALOGY ONLY**,brief handling_protocol 載重:Drafter 須標 analogy,**絕不**作 LLM L4c 直接證據。open PDF 未確認(qs=2)。
- c037: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.1002/poi3.437 — Pohle et al.「Unthinking Digital Sovereignty」;摘要為 digital sovereignty 批判系譜——FW anchor + anti-overclaim caution。Drafter 可引摘要 ground 借用標籤。
- c040: (`access_status: ok`, `snippet_status: usable`) — https://doi.org/10.30574/wjarr.2025.27.2.2845 — Abiade「Algorithmic Sovereignty」;摘要連結 foreign AI infra→security dependency(Global South)——FW conditional-policy anchor。qs=3 lower-profile venue,corroborate。Drafter 可引摘要。

## Fast-skip — no usable evidence (excluded from primary evidence pool)

### ss_landing_no_open_pdf 降階(qs=2,open PDF 未確認;摘要過薄或為次要)
- c021: (`access_status: ss_landing_no_open_pdf`, `snippet_status: thin`) — https://www.semanticscholar.org/paper/1beb1905... — Bias Amplification / model-collapse;摘要為機制描述但 open PDF 未確認、為 L4a 遞迴訓練次要機制,c018/c020 已覆蓋 homogenization 主軸。qs=2。
- c038: (`access_status: ss_landing_no_open_pdf`, `snippet_status: thin`) — https://www.semanticscholar.org/paper/798faf0d... — Brcic「cognitive sovereignty」;single-author conceptual preprint,open PDF 未確認。FW 概念錨,c037/c040 已 ground sovereignty 標籤。qs=2。
- c039: (`access_status: ss_landing_no_open_pdf`, `snippet_status: thin`) — https://www.semanticscholar.org/paper/db716b91... — Li「Digital Platform Gatekeeper Obligation」;S2 確認 isOpenAccess=false。FW DMA-gatekeeper 錨,secondary-tier。qs=2。

### 媒體 restatement(primary 已優先)
- c015: (`access_status: ok`, `snippet_status: usable`) — https://searchengineland.com/news-publishers-search-referrals-drop-report-467408 — Search Engine Land 轉述 Chartbeat;摘要含「Google organic traffic down 33% global/38% US Nov24-Nov25;publishers project -43% over 3yr」具數字。**注意**:c014 Reuters extract 已澄清 -43%/-33% 應歸 Chartbeat(c015)非 Reuters。Drafter 可引摘要作 L2 referral-decline trend,但須標 trade-press restatement + L2 guard(可能 AI-Overviews 驅動非 chat-LLM substitution)。**列此處因 qs=3 + 為 primary(Chartbeat)的 restatement**,Drafter 引用時優先標 Chartbeat 為 primary。
- c016: (`access_status: ok`, `snippet_status: thin`) — https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-... — Reuters「Generative AI and news 2025」attitudinal;摘要泛(comfort levels/usage by market/age 無具體數字),c014 已為 L2 主錨。Drafter 如需 attitudinal 細節可請 operator 深讀此 companion report。

## Operator overrides needed

- ✅ **c028 (Shu/Karell latent historical-narrative framing→opinion) — RESCUED 2026-06-08**:先前的 operator override 候選已解決。原 `ss_landing_no_open_pdf` / `thin` 降階為誤判——PNAS Nexus 為開放取用且 PMC 有免費全文(PMC12954675)。已深讀並寫入 `extracts/c028.md`,RESTORE 至 qs=4,移入 L4b depth-1。它是 L3→L4b 最 on-chain 的一手 joint(latent framing → 個人意見)。
- **c002 Waight 全文(paywall)** — scope 已由 PubMed 全文 abstract(逐字)+ 作者 project site 充分鎖定,Drafter 可精確 L3 引用。唯 continued-pretraining 的精確 in-text 句(Llama-2-13b / 6,400 docs / ~80%)中,abstract 僅有「additional pretraining ... generates more positive answers」,具體數字來自 project site。若 Drafter 需 Nature 內文逐字句,請 operator 取全文。
- **市場 snapshot c010/c011/c012(live API)** — 本 session 未重抓(live API 會變、重抓會破壞 dated containment)。2026-06-08 為 Collector 捕獲之 citable 記錄。若需更新 snapshot,operator 可重抓並另立 as-of 日期,勿覆蓋 2026-06-08 數字。
- **OpenRouter rankings 頁 + Artificial Analysis pricing 頁** — Collector 標 js_only(無 API 路徑);pricing 已由 OpenRouter JSON API(c010)覆蓋。若 operator 需 Artificial Analysis 的 tens-of-X 表作交叉驗證,需 API key 或 non-JS endpoint。
