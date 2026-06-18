# Collection coverage — cognitive-disruption-tw

Candidates: 79  |  Tracks run: T1 (academic, halved per Co2), T3 (general web, doubled per Co2). T2 skipped (no project sources.yaml). T4 skipped (non-TW-public-data brief; the two TW Q8 case reports are already in hand).

Budget note: brief is `fidelity:high` + `horizon:emerging` → Co2 matrix halves Track 1 (ran 15 academic queries × `--limit 15` but hand-selected only the load-bearing conceptual anchors, discarding ML-detection survey noise) and doubles Track 3 (16 WebSearch query-clusters → 42 curated candidates). This redistribution is correct for a fast-moving threat-intel/policy argument brief where peer-reviewed weight lags the news cycle.

## Brief question × track  (cell = candidate count; combined-Q records counted in each Q)

| Brief Q | T1 academic | T2 curated | T3 web | T4 portal | total |
|---------|-------------|------------|--------|-----------|-------|
| Q1 動機合流 | 8 | – | 9 | – | 17 |
| Q2 共用 TTP | 6 | – | 5 | – | 11 |
| Q3 AI slop 規模 | 4 | – | 9 | – | 13 |
| Q4 認知破壞對位框架 | 12 | – | 5 | – | 17 |
| Q5 force multiplier 證據 | 2 | – | 5 | – | 7 |
| Q6 偵測盲區 | 3 | – | 3 | – | 6 |
| Q7 跨域接口 | 2 | – | 6 | – | 8 |
| Q8 在地案例 | 0 ⚠ | – | 2 | – | 2 |

## Concept ontology distribution

| concept | count | note |
|---------|-------|------|
| I (共用基礎設施) | 28 | research_focus 主軸,證據最厚——disinfo-for-hire / GAN 假頭像 / EEAS FIMI 基礎設施 / Meta+OpenAI+Google 威脅報告 |
| CD (認知破壞 harm model) | 19 | Wardle 資訊失序 / Roberts flooding / firehose / liar's dividend / AI slop——對位框架齊備 |
| FM (force multiplier) | 9 | 含 4 個 no_measurable_effect 反框架,逼 Drafter 逐環標記證據(brief 最弱一環) |
| XD (跨域整合) | 9 | IMS / DISARM-STIX / DISINFOX / CheckFirst 供應鏈 / NATO 偵測實驗——接口層完整 |
| P (政治攻擊舊框架) | 8 | Oxford computational propaganda 系作對照,非主軸 |
| S (詐騙獲利舊框架) | 6 | 詐騙中心 / 廣告變現 slop / engagement farming 反框架作對照 |

## Counter-framing coverage (operator priority #3 — 4 keys, all hit)

| key | records | 
|-----|---------|
| just_spam (slop 是演算法副產物非協同) | c016, c017 (Carrigan / Digital Content Next) |
| just_profit (純廣告變現) | c014 (404 Media slop 供應鏈) + S-cluster |
| no_measurable_effect (minimal effects) | c034 (Cato), c035 (Altay/Berriche/Acerbi), c036 (Adams et al.), c079 (SIO/CSET 量產≠影響) + c018 (Springer alarmist 下游害) |
| shared_vendor_not_actor (各自獨立非統一行為者) | c037 (SIO 重量輕質) + c023 (CIB 訊號碎裂、各群體不同戰術) |

## Language

| Language | count | note |
|----------|-------|------|
| EN | ~75 | 學術與威脅情報主體,符合 brief「en 為主」 |
| zh-TW topic | 4 | Doublethink Lab 兩篇(中文機構、英文發表)+ 兩案 answer-key(已在手,未重蒐) |

**C5 CJK 學術缺口（誠實標記）**：Track 1（OpenAlex + Semantic Scholar）對繁中學術索引極弱。本研究的台灣在地認知作戰學術(IORG / 事查中心研究)幾乎不在 T1 母體內——這是預期的覆蓋缺口,不是「無此研究」。已用英文翻譯變體跑 T1、並把在地實例權重移到 T3(Doublethink Lab)與已在手的兩案 answer-key。Drafter/Gatekeeper 勿將 T1 的繁中空白誤讀為證據不存在。

## Provider failure (honest flag)

- **Semantic Scholar TLS 憑證過期**：所有 T1 查詢的 S2 半邊回 `[SSL: CERTIFICATE_VERIFY_FAILED] certificate has expired`,故 T1 實際只有 OpenAlex 一個 provider 生效。q11(ABCDE taxonomy)因此 + OpenAlex 該 phrasing 零命中 → T1 完全 0;ABCDE/SCOTCH/BEND 框架文獻改由 T3 補(IMS/DISARM cluster)。

## Blind spots (every zero / near-zero cell)

- **Q8 × T1 = 0**：預期缺口,非缺漏。兩份台灣一手報告(FB 外連可疑站 / YouTube 養生網)是 operator 明示「已在手、僅作 Q8 實例、不重蒐」;T3 另補 Doublethink Lab 兩篇作兩案外的在地脈絡。Drafter 應直接引 answer-key `draft_v1.md` 的兩案,本 collect 不重複。
- **Q5 × T1 = 2(near-zero)**:force multiplier 受眾端鏈(信任基線下降→後續操作更易)在學術上本就薄——這正是 brief 標為「最弱一環」的原因。已用 T3 的 no_measurable_effect 反框架(c034-c037/c079)從反面逼近,但「養生受眾→極化頻道導流」這種具體 spillover 實證,文獻層仍是 gap。誠實標記:這條鏈缺直接實證是真實的證據狀態,非蒐集失敗。
- **Q6 × both = 3/3**:偵測盲區證據中等。CIB 偵測批判(c023)、GAN-collage 對抗工程(c025)、NATO 偵測實驗(c026)已覆蓋主要面向;反詐金流追蹤的盲區文獻較薄,但已由詐騙中心 cluster 與兩案 answer-key 間接補。
- **ABCDE/SCOTCH/BEND 具名框架**:T1 零命中(見 provider failure),T3 以 IMS+DISARM 涵蓋大部分跨域接口需求,但 Camille François ABCDE 與 Carley BEND 的原始出處未直接收進候選——Gatekeeper 若認為 Q7 需具名框架原典,可標 wanted_source 回補。

## Meta H1 2026 一手核對結果（operator priority #5）

已 WebFetch `transparency.meta.com/reports/integrity-reports-h1-2026/`(c001, access_status=ok):
- 一手數字確認:「In 2025, we took down 10.9 million accounts associated with scam centers in Southeast Asia and in the Middle East... grown in sophistication and industrialization.」
- 影響力操作:俄/伊/中三大來源,含一中國網絡 targeting Taiwan。
- **關鍵更正**:Meta 報告把詐騙中心與隱蔽影響力操作列為**分開的**執法優先項,**未明文宣稱兩者共用 tactics/infrastructure**。draft_v1 §4.5 的「同一套工業化身分偽造橫跨詐騙與影響力」是**本研究的詮釋,非 Meta 立場**——已在 c001 的 abstract 與 why_relevant 明確標記,Drafter 引用時不可把合流連結歸給 Meta。
