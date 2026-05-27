# Jargon map · audit trail

Pipeline jargon → publication 改寫決策對照表。共 8 個 cluster + 各 finding 重組原則。

## Cluster 1 · Concept ontology refs

| Pipeline | Publication | Note |
|---|---|---|
| A∩D 灰區 | 即時推測與同意機制的灰色地帶 / 這個灰區（後續） | 首次出現完整解釋 |
| A 區 / demographic inference | 即時推測 / demographic inference (首次補英文) | 整份統一用「即時推測」 |
| B 區 / identification | 身分比對 / 人臉登入會員 | 視 context |
| C 區 / PII data flow | 會員資料流 | 簡單 swap |
| D 軸 / consent axis | 告知／選擇／撤回三層同意機制 | 視 context |
| concept_target / claim_scope | (刪) | 不出現 |
| firewall (B/C 分軌) | 分開計算 / 不算進… | 簡單 swap |
| research_focus | 研究核心 | swap |

## Cluster 2 · Pipeline workflow refs

| Pipeline | Publication |
|---|---|
| F1 / F2 / F3 ... F8 | (刪) 改 noun-led 標題 |
| Q1a / Q1b / Q2 ... Q7 | (刪) |
| §6 (個資法) / §8 (個資法) | 個資法第 6 條 / 第 8 條（保留條文編號）|
| §8 (brief success criteria 結構) | (刪) |
| Dr1 / Dr2 / Dr3 / Dr7 | (刪) |
| Co1 / Co2 / Co5 | (刪) |
| Sy / G4 | (刪) |
| cNNN | inline attribution + 末尾 numbered 引用（見 cid-citation-map.md） |
| partial_counter_framing per Dr7 | 反例 / 對立論點 |
| caveat-tier rescue | 附條件保留 / 但書 |
| meta-reviewer / multi_model review / integrity_check | (刪 — 研究產製方式段一筆帶過) |
| accepted record / extracts | 採用的資料 / 深讀的資料 |
| pipeline_stage_added | (絕對不出現) |

## Cluster 3 · Statistical / methodological

| Pipeline | Publication |
|---|---|
| 保守下界 | 最少能確認的數量 / 至少… |
| vendor-claimed 上界 | 業者自己對外宣稱的最大數字 / 業者公開的範圍上限 |
| dual-bound / 雙端展開 | 兩端並列 / 從保守數字到業者宣稱數字之間 |
| cross-confirmed / N-源 cross-confirmed | 多重來源確認 / N 個來源都顯示 |
| invisibility-ceiling proxy | 容量上限 / 看不見的天花板 |
| lower-bound proxy | 保守下界 |
| quadruple structural zero / 四重結構性零 | 四個角度都看不到資料 / 四重結構性空白 |
| [strong] / [contested] / [speculative] / [speculative-mechanism] | (刪標記, 融入 prose hedge) |
| verbatim quote | 原文 / 字面引用 |
| parallel coverage | 平行佐證 / 對照確認 |
| Scope caveat | 需注意的範圍限制 / 但要說明的是 |
| state action vs horizontal effect | 國家強制蒐集 vs 套用到私部門需經水平效力 |
| categorically prohibited | 明文禁止 / 列入禁制清單 |
| publication-channel | 對外公開管道 / 發布管道 |
| modality layer / text + visual modality | 文字層 + 影像層 / 不同呈現方式 |
| 10-layer cross-confirmed wording vacuum | 跨 10 個對外管道、文字到畫面都沒人提到 |
| wording vacuum | 沒有任何文字提到 / 完全沉默 |
| framing | 說法 / 論述方式 / 立場 |
| defensive framing | 業者的辯護立場 |
| framing fluidity / internal split | 業者跨管道說法不一致 |
| dismantle / 結構性瓦解 / 「打掉」 | 大幅削弱 / 論證上無法成立（避免戰鬥語氣）|

## Cluster 4 · Process metadata (整段刪)

| Pipeline | Action |
|---|---|
| Project / Stage / Date metadata block | 整塊刪;改寫成 intro narrative |
| 「給 PDPC / 立委 / 消保處 / 消基會 / 媒體的政策報告」 | 完全刪 |
| review.mode / fidelity_level | 刪 |
| patch 1 / 2 / 3 / 3.1 / 4 修訂史 | 刪;研究產製方式段一句「歷經多輪人工 + agent 協作修訂」 |
| self_audit / integrity_check | 刪 |
| multi_model review (Claude + Codex + Gemini) | 研究產製方式段提「三模型平行審閱」 |
| accepted record (95) / extracts (28) / themes (9) | 研究產製方式段提數字, 不散在正文 |
| handoff_log / pipeline_stage_added | 絕對不出現 |

## Cluster 5 · English jargon 中譯

| Pipeline | Publication |
|---|---|
| inference (n.) | 即時推測 / 推測 / 推論（context-dependent）|
| edge inference | 裝置本機運算 |
| cloud upload | 上傳雲端 |
| opt-in / opt-out | 事前同意 / 事後退出 (首次解釋) |
| boilerplate | 制式樣板文 |
| narrative | 敘事 / 論述 |
| metadata | (刪 or 改「附帶資訊」)|
| caveat | 但書 |
| governance | 治理 (常見, OK) |
| enforcement | 執法 / 執行 |

## Cluster 6 · Acronym 首次 gloss

| First-use form |
|---|
| 個人資料保護委員會（PDPC）|
| 個人資料保護法（PDPA） |
| 歐盟人工智慧法案（EU AI Act） |
| 歐盟一般資料保護規則（GDPR）|
| 美國伊利諾州生物特徵資訊隱私法（Illinois BIPA）|
| 歐洲資料保護委員會（EDPB） |
| 台灣人權促進會（TAHR）|
| 軟體開發套件（SDK） |
| 視覺語言模型（VLM, Visual Language Model）|

## Section restructure 決策

- F-no 全部刪, 改 noun-led 標題
- TL;DR 從 5 個 dense cards 縮成 5 個 ≤3 句的 lay-reader 段
- 結構從 F1-F8 順序改成 Pattern A「發生什麼 / 為什麼 / 法律怎麼說 / 業者立場 / 為什麼沒人在告 / 國際對照 / 怎麼辦 / 限制」
- F6 同意對照表保留為 standalone section（讀者會引用的表）
- 政策建議段 4 個 stakeholder 結構保留, 但改成「對 X 的建議」(stakeholder label, 非 audience label)

## 改寫原則 (overall)

1. **數字保留** — 35 / 0 / 2235 / 823 / 3058 / 95 / 28 / 30+ / 1000+ 全部 inline 保留
2. **claim 保留** — 8 個 finding 的核心主張不動, 只改 wording
3. **限制保留** — Counter-evidence 跟 What we don't know 的 caveat 全部 inline 進對應 finding
4. **register 對齊混合 audience** — 媒體可引用、立委可拿來質詢、PDPC 不嫌淺
