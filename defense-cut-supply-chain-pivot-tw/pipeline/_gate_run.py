#!/usr/bin/env python3
"""Gatekeeper run for defense-cut-supply-chain-pivot-tw.

Aggressive mode: target ~30-40% accept rate (~60-70 / 179).
Per-record decisions encoded below. Each decision must carry a gate_reason.

Output:
  pipeline/gate/accepted.jsonl
  pipeline/gate/rejected.jsonl
"""
import json
import os
from pathlib import Path
from collections import Counter

PIPE = Path(__file__).parent
CAND = PIPE / "collect" / "candidates.jsonl"
GATE = PIPE / "gate"
GATE.mkdir(exist_ok=True)

# ── Per-record decision table ────────────────────────────────────────────
# Format: id -> (verdict, quality_score_or_None, why_relevant_or_None, gate_reason)
# verdict: "accept" | "reject"
# For "accept", why_relevant follows "Q<N>: <specific contribution>" rule.
# For "reject", gate_reason names the rule.

D = {}

def A(qs, why, reason):
    return ("accept", qs, why, reason)

def R(reason):
    return ("reject", None, None, reason)

# ── Track 1 academic (c001–c129) — aggressive cull ──────────────────────
# Most are tangential to Taiwan defense supply chain. Accept only those
# that materially address: machine tool cross-strait relocation;
# long-arm jurisdiction / Entity List / export control; Taiwan defense
# industrial base; cross-strait industrial integration with defense angle;
# friend-shoring + Taiwan defense; New Southbound Policy (south-bound hedge).

D["c001"] = R("adjacent_not_material: HCI/making cultures ethnography, no defense supply chain content")
D["c002"] = R('adjacent_not_material: generic SCM-geopolitics lit review, no Taiwan defense content')
D["c003"] = A(3, "Q3: GVC + developmentalist framework grounded in Taiwan/Korea industrial-policy experience (baseline for state role in defense industrial base)", "Taiwan-grounded GVC theory")
D["c004"] = R("adjacent_not_material: smart port ICT, no defense or machine-tool content")
D["c005"] = R("adjacent_not_material: cloud computing environmental impact")
D["c006"] = A(4, "Q3/Q5: China CNC machine-tool catch-up + Middle Technology Trap under US export controls (direct counterpart industry to Taiwan工具機)", "China CNC industry geopolitics analysis")
D["c007"] = A(4, "Q3: BRI + Made-in-China 2025 impact on Taiwan machine tool industry (direct A-track baseline)", "Taiwan machine tool vs Made-in-China-2025")
D["c008"] = A(3, "Q3: Taiwan machine tool industrial upgrading via China interaction (A-track empirics, abstract empty but title direct)", "Taiwan machine tool x China upgrading")
D["c009"] = A(3, "Q3: Taiwan machine tool extra-regional innovation network in China (empirics on 2015 baseline)", "Taiwan machine tool extra-regional networks in China")
D["c010"] = A(3, "Q3: Taiwan + China cutting-tool industry status quo (component-level baseline for A-track)", "Taiwan/China cutting tool industry")
D["c011"] = R("adjacent_not_material: ML stock-crash prediction, no industry/defense content")
D["c012"] = R("adjacent_not_material: Taiwan machine tool trade-show marketing (deprioritised per brief — '工具機展覽會行銷文')")
D["c013"] = R("adjacent_not_material: Indonesia nickel/EV battery supply chain, no Taiwan defense link")
D["c014"] = R("adjacent_not_material: CNC geometric-error compensation (technical engineering, not industry/defense)")
D["c015"] = R('adjacent_not_material: chip-side US-Taiwan policy, no machine tool / defense industrial base material')
D["c016"] = R("adjacent_not_material: Taiwan green finance / renewable energy")
D["c017"] = A(4, "Q3: spatiotemporal evolution of Taiwanese IT/electronics investment in PRC 1991–2012 (historical baseline for cross-strait industrial relocation)", "Taiwan-funded IT/electronics value chain in PRC")
D["c018"] = R("adjacent_not_material: Pakistan stock investor behaviour biases")
D["c019"] = R("adjacent_not_material: Alice Amsden inductive method history of thought")
D["c020"] = R("adjacent_not_material: AI bibliometric review")
D["c021"] = R("duplicate_of:c010 (same paper, same DOI different URL)")
D["c022"] = A(3, "Q3: Taiwan machine tool export models + major exporting destinations (A-track external markets baseline)", "Taiwan machine tool export structure")
D["c023"] = R("adjacent_not_material: EU digital sovereignty stack model")
D["c024"] = R("adjacent_not_material: Ukraine agricultural export disruption CGE")
D["c025"] = R("adjacent_not_material: Ukraine biofuel energy security")
D["c026"] = R("adjacent_not_material: LLM schema induction for EV battery supply chain")
D["c027"] = R("adjacent_not_material: generic 2023 year-ahead international agenda review")
D["c028"] = R('adjacent_not_material: EU strategic autonomy, no Taiwan defense supply chain material')
D["c029"] = R("adjacent_not_material: Korea peninsula + Ukraine war security complex, no Taiwan supply chain")
D["c030"] = R("adjacent_not_material: AI bibliometric Industry 4.0/5.0")
D["c031"] = A(5, "Q1/Q3/Q5: cross-strait semiconductor flow to PLA — direct empirical mechanism for technology diffusion via Taiwan industrial relocation", "cross-strait defense-tech leakage to PLA")
D["c032"] = R("adjacent_not_material: Taiwan/Korea democratisation comparison, no supply chain")
D["c033"] = A(4, "Q5: chokepoint economies framework (Taiwan, Korea, Japan, NL) navigating US extraterritorial export controls — direct framing for BIS/EAR mechanism", "chokepoint economies + extraterritorial controls")
D["c034"] = R("duplicate_of:c006 (same paper, different URL/DOI variant)")
D["c035"] = R('adjacent_not_material: 2021 Taiwan country yearbook, low information density on supply chain')
D["c036"] = R("adjacent_not_material: 1952 China hydraulic engineering diplomacy history")
D["c037"] = R('adjacent_not_material: business security dilemma theoretical frame, Germany/NL case')
D["c038"] = R("adjacent_not_material: cross-strait marriage migration (brief excludes '兩岸投資 餐飲文創' — analogous)")
D["c039"] = R("adjacent_not_material: Taiwan environmental NGOs")
D["c040"] = A(4, "Q1/Q3: Taiwan indigenous defence industry history + external military assistance review (Q1 fact-base on national-team genealogy)", "Taiwan indigenous defence industry history")
D["c041"] = R("adjacent_not_material: EU semiconductor strategy, no Taiwan defense supply chain content")
D["c042"] = R('adjacent_not_material: cross-strait Industry 4.0 innovation policy abstraction')
D["c043"] = A(4, "Q4/counter-framing: Christensen 'mutually assured disruption' — argues against aggressive decoupling, key counter-framing for '西進是商業合理性' angle", "decoupling-skeptic counter-framing")
D["c044"] = R("adjacent_not_material: EU supply security in semiconductors/pharma/CRM, no Taiwan defense link")
D["c045"] = R("adjacent_not_material: generic lean inventory + geopolitical shocks regression")
D["c046"] = R("adjacent_not_material: South China Sea + supply chain speculation")
D["c047"] = R("adjacent_not_material: Eurasian transport routes + Ukraine war")
D["c048"] = R("adjacent_not_material: Indonesian armed forces RMA")
D["c049"] = R("adjacent_not_material: Ukraine war + Northeast Asia geopolitics overview")
D["c050"] = R('adjacent_not_material: 2022 Taiwan country yearbook, no supply chain content')
D["c051"] = R('adjacent_not_material: China grey-zone warfare context, no supply chain material')
D["c052"] = R("adjacent_not_material: Taiwan public opinion pro-American attitudes shift")
D["c053"] = R('adjacent_not_material: Taiwan banks x Japan semiconductor financing, financial integration not defense')
D["c054"] = R("adjacent_not_material: Taiwan semiconductor trade facilitation efficiency, no defense angle")
D["c055"] = R('adjacent_not_material: national identity x economy electorate-level, not industry-side')
D["c056"] = R("duplicate_of:c035 (same yearbook entry)")
D["c057"] = R("adjacent_not_material: Ukraine semiconductor industry prospects")
D["c058"] = R("adjacent_not_material: emerging electronics economy bibliometric")
D["c059"] = R('adjacent_not_material: rare-earth analogue, not Taiwan machine tool / drone material')
D["c060"] = A(3, "Q3: ROC-PRC economic/trade interdependence baseline (2018 stock-take of cross-strait industrial ties)", "ROC-PRC economic interdependence")
D["c061"] = R('adjacent_not_material: geopolitical risk methodology paper, no Taiwan supply chain content')
D["c062"] = R("adjacent_not_material: meteorology + asthma")
D["c063"] = R("adjacent_not_material: US Cold War nonproliferation grand strategy")
D["c064"] = R("adjacent_not_material: UK lithium onshoring + Brexit")
D["c065"] = R('adjacent_not_material: China-balancing theory, no Taiwan-specific empirical')
D["c066"] = R("adjacent_not_material: India AUKUS/Quad minilateralism")
D["c067"] = A(4, "Q1/Q6: Taiwan strategic importance to US/allies (defense posture context)", "Taiwan strategic importance to US/allies")
D["c068"] = R("adjacent_not_material: non-economic objectives in GVC theory")
D["c069"] = R('adjacent_not_material: economic security state-transformation Korea case theoretical')
D["c070"] = R("adjacent_not_material: generic China-Taiwan ambitions overview")
D["c071"] = R('adjacent_not_material: state infrastructure power Thailand analogue, not long-arm jurisdiction')
D["c072"] = R("adjacent_not_material: Bangladesh India geopolitics")
D["c073"] = R("adjacent_not_material: Zimbabwe Rhodesia alternate history")
D["c074"] = R("adjacent_not_material: video-game intellectual capital efficiency")
D["c075"] = R("adjacent_not_material: Asian FTA leadership overview")
D["c076"] = R("adjacent_not_material: Vietnam country note")
D["c077"] = R("adjacent_not_material: great-power competition measurement Africa/Asia")
D["c078"] = R("adjacent_not_material: India Act East policy with ASEAN")
D["c079"] = R("adjacent_not_material: Ukraine war Asia economic impact")
D["c080"] = R("adjacent_not_material: Silk Road BRI regional perspectives")
D["c081"] = R("adjacent_not_material: infrastructure conflict South/East China Sea anxieties")
D["c082"] = R("adjacent_not_material: Vietnam subnational governance + competitiveness")
D["c083"] = R("adjacent_not_material: China agricultural investment in ASEAN")
D["c084"] = R('adjacent_not_material: Germany chip dependency comparative, no Taiwan defense link')
D["c085"] = R('adjacent_not_material: generic semiconductor industrial policy theory')
D["c086"] = R('adjacent_not_material: Huawei decoupling case, not Taiwan defense / machine tool')
D["c087"] = R("adjacent_not_material: 3D printing + international security risks")
D["c088"] = R("adjacent_not_material: East Germany/Yugoslavia variegated state capitalism")
D["c089"] = R("adjacent_not_material: 'not trading with enemy' theoretical case")
D["c090"] = R('adjacent_not_material: US-China platform decoupling, not machine tool or defense industrial base')
D["c091"] = R("adjacent_not_material: RMB internationalisation 'financial war' theory")
D["c092"] = R("adjacent_not_material: India bank credit + working capital financing")
D["c093"] = R("adjacent_not_material: manufacturing cycle prediction SEM model")
D["c094"] = R('adjacent_not_material: US-China chip industry trade war, no Taiwan defense angle')
D["c095"] = R('adjacent_not_material: US emerging-tech export control theory, redundant with c103/c099/c114/c115')
D["c096"] = R("adjacent_not_material: India NSG entry history")
D["c097"] = R("adjacent_not_material: European private firm accounting")
D["c098"] = R("adjacent_not_material: Indonesia financial fraud detection ML")
D["c099"] = A(4, "Q5: October 2022 US export controls on China advanced chips (canonical Entity List/EAR mechanism case for Q5)", "October 2022 US export controls on China chips")
D["c100"] = R("adjacent_not_material: external auditor selection bank performance")
D["c101"] = R("adjacent_not_material: Russia Ukraine info war in Africa")
D["c102"] = R("adjacent_not_material: Indonesian textile Industry 4.0 case")
D["c103"] = A(5, "Q5: extraterritorial reach of US export-control law — direct legal mechanism for Q5 long-arm rhetoric (BIS/EAR/FDPR)", "US export-control extraterritorial reach legal analysis")
D["c104"] = R("adjacent_not_material: Brazil 5G deployment + US-China rivalry")
D["c105"] = R("adjacent_not_material: Indonesian music industry resistance")
D["c106"] = R("adjacent_not_material: GVC rents/power/governance theory")
D["c107"] = R("adjacent_not_material: China response to Ukraine war")
D["c108"] = R("adjacent_not_material: forced labour in global supply chains")
D["c109"] = A(4, "Q5: China weaponisation of trade-barrier investigations vs Taiwan (direct economic coercion mechanism)", "China economic coercion vs Taiwan via trade-barrier probes")
D["c110"] = R("adjacent_not_material: AI international governance")
D["c111"] = R("adjacent_not_material: US political text on China narrative")
D["c112"] = R("adjacent_not_material: Russia OFDI potential under sanctions")
D["c113"] = R('adjacent_not_material: comparative US sanctions China vs Russia, no Taiwan firm-level material')
D["c114"] = A(5, "Q5: PRC counter-long-arm-jurisdiction legal toolbox + foreign-related law expansion — direct China-side mechanism for 反外國制裁法", "PRC counter-long-arm-jurisdiction toolbox")
D["c115"] = A(5, "Q5: US long-arm jurisdiction + China countermeasures — direct dyad legal analysis for Q5 core mechanism", "US long-arm jurisdiction + China countermeasures")
D["c116"] = R("adjacent_not_material: generic China-US economic game dynamics")
D["c117"] = A(4, "Q5: China sanctions/countermeasures/unilateral restrictive measures policy (direct mechanism for PRC long-arm regime)", "China sanctions + unilateral restrictive measures policy")
D["c118"] = A(4, "Q4: NSP soft-power flagship programme (South-bound hedge baseline — empirics on Taiwan investment shift to ASEAN/India)", "Taiwan New Southbound Policy flagship programme")
D["c119"] = R("adjacent_not_material: India sovereignty consequences of Taiwan crisis")
D["c120"] = R("adjacent_not_material: national election outcomes + international relations")
D["c121"] = R("adjacent_not_material: Afghanistan 2016 country note")
D["c122"] = A(3, "Q4: NSP human resources cooperation + Vietnam case (south-bound hedge specific case)", "NSP HR cooperation Vietnam")
D["c123"] = A(3, "Q4: NSP cross-strait relations interaction (south-bound vs west-bound framing)", "NSP vs cross-strait relations")
D["c124"] = R("adjacent_not_material: India mobile manufacturing lessons")
D["c125"] = R("adjacent_not_material: ASEAN COVID agri-food measures")
D["c126"] = R("adjacent_not_material: Ethiopia/Vietnam SEZ comparison")
D["c127"] = R("adjacent_not_material: fuzzy prioritisation high-tech method")
D["c128"] = R("adjacent_not_material: SEA semiconductor foundry cost-saving")
D["c129"] = A(3, "Q4: Taiwan manufacturing expatriate willingness to Vietnam (south-bound hedge worker-mobility evidence)", "Taiwan manufacturing expatriate willingness to VN")

# ── Track 3 manual c130–c179 — high-priority retention ──────────────────
# Operator-curated; nearly all accept per high fidelity_level.

D["c130"] = A(4, "Q1: stock-market reaction to defense/drone budget cuts (seek_direct seed, real-time market signal)", "TechNews stock reaction to budget cut")
D["c131"] = A(4, "Q1: Yahoo News political-industry reaction to 3350億 drone cut (Taichung industry impact)", "Yahoo: Taichung industry impact of drone cut")
D["c132"] = A(5, "Q3/A: ChinaTimes 工具機十五五磁吸 — direct A-track west-bound pressure thesis evidence", "ChinaTimes machine tool 15-5 west-bound pressure")
D["c133"] = A(5, "Q2/B: CNA 鳳梨田起飛 — drone industry 21x export + 129億 production (B-track + counter-framing baseline)", "CNA drone industry growth")
D["c134"] = A(5, "Q1: 報導者 1.25兆拔河 deep-report (canonical Q1 source)", "報導者 1.25兆 deadlock deep report")
D["c135"] = A(4, "Q1: UDN 1.25兆預算整理包 (budget breakdown + political negotiation timeline)", "UDN 1.25兆 budget primer")
D["c136"] = A(4, "Q1/Q3: LTN academic warning — drone cut means soldiers pay in blood (security framing)", "LTN academic on drone cut security cost")
D["c137"] = A(4, "Q2/B: 新北 drone industry response to budget cut (industry-side cost evidence)", "New Taipei drone industry response")
D["c138"] = A(4, "Q1: nextapple 4700億 cut + MND no-second-budget statement (canonical fact-base)", "nextapple 4700億 cut + MND statement")
D["c139"] = A(5, "operator follow-up — manual retrieval required (MOPS portal for primary-source財報 for priority上市櫃 tickers)", "primary_doc: MOPS portal — operator todo")
D["c140"] = A(5, "Q1: 國防部 official publication 85301 (primary gov source on procurement)", "MND official publication primary source")
D["c141"] = A(5, "Q2/Q5: Atlantic Council Global Strategy to Secure UAS Supply Chains (canonical drone-supply-chain framework)", "Atlantic Council UAS supply chain strategy")
D["c142"] = A(5, "Q1/Q2: CNAS Hellscape report — canonical asymmetric drone defense thesis for Taiwan", "CNAS Hellscape Taiwan asymmetric defense")
D["c143"] = A(5, "Q2/Q5: CSIS drone supply-chain chokepoints (direct B-track chokepoint mapping)", "CSIS drone supply-chain chokepoints")
D["c144"] = A(4, "Q2/Q6: Diplomat US-Taiwan defense partnership 2.0 + UAV doctrine analysis", "Diplomat US-Taiwan UAV doctrine")
D["c145"] = A(5, "Q2/B: GTI Taiwan indigenous drone industry overview (canonical B-track廠商-level survey)", "GTI Taiwan drone industry overview")
D["c146"] = A(4, "Q2/Q5: AmCham 'rushing to localise drone supply chain' (industry-association non-red supply chain perspective)", "AmCham localising drone supply chain")
D["c147"] = A(4, "Q1/Q6: RAND deterring Taiwan invasion without war (strategic context for asymmetric procurement)", "RAND deterring Taiwan invasion")
D["c148"] = A(4, "Q2: RSIS Drones Over the Strait (cross-strait UAV reshaping analysis)", "RSIS Drones Over the Strait")
D["c149"] = A(4, "Q2/Q5: ArmyRecognition Taiwan drone production fixing China supply-chain risk (industry status)", "ArmyRecognition Taiwan drone localisation")
D["c150"] = A(5, "Q5: Haas Automation $2.5M sanctions settlement — concrete BIS Entity List enforcement precedent on machine tools", "Haas Automation BIS sanctions settlement")
D["c151"] = A(5, "Q5: Federal Register Sep 2025 Entity List additions/revisions — primary regulatory source", "primary_doc: Federal Register Entity List Sep 2025")
D["c152"] = A(4, "Q2/B: DSET surfaces Economist coverage of Taiwan non-red drone export (counter-framing balance)", "DSET re-Economist non-red drones")
D["c153"] = A(5, "Q2/Q6: DSET Drones for Democracy US-Taiwan strategic report (canonical non-red drone framing)", "DSET Drones for Democracy report")
D["c154"] = A(4, "Q2/Q6: FocusTaiwan EU non-red drone supply chain entry analysis", "FocusTaiwan EU non-red drone entry")
D["c155"] = A(4, "Q2: AsiaTimes Taiwan drone surge offsetting China edge", "AsiaTimes Taiwan drone surge")
D["c156"] = A(4, "Q1/Q2: defence-ua on Taiwan asymmetric-hell obstacles (Q1/Q2 cross-check, ground-truth obstacles)", "defence-ua Taiwan asymmetric obstacles")
D["c157"] = A(5, "Q2/E: TaipeiTimes drone export 21-fold + Poland leads non-red supply chain (canonical B-track + E-market evidence)", "TaipeiTimes drone export 21x Poland leads")
D["c158"] = A(5, "Q3/A: FFG corporate disclosure — 'pioneer of Taiwan machine tool industry in China' primary-source company self-narrative", "primary_doc: FFG corporate self-disclosure on China")
D["c159"] = A(5, "Q3/A: MOF July 2025 machinery export statistics (primary government data on machinery trade)", "MOF machinery export statistics 2025-07")
D["c160"] = R('brief_exclusion: 工具機展覽會行銷文 (TMTS industry event marketing, deprioritised per brief)')
D["c161"] = A(5, "Q2/B: Coretronic IR page — MND micro-recon drone contract (primary-source廠商 data)", "primary_doc: Coretronic MND contract")
D["c162"] = A(5, "Q2/B: Thunder Tiger SeaShark 600 USV + 1,300-vessel MND tender (primary-source廠商 data on無人艇)", "primary_doc: Thunder Tiger SeaShark + MND tender")
D["c163"] = A(5, "Q3/A: HIWIN Suzhou Industrial Park subsidiary disclosure (primary-source A-track west-bound exposure)", "primary_doc: HIWIN Suzhou subsidiary")
D["c164"] = A(5, "Q2/Q5: 新頭殼 NCSIST drones using PRC-made components whistleblower (concrete red-supply-chain leakage evidence)", "新頭殼 NCSIST 驟雲/銳鳶 PRC components")
D["c165"] = A(5, "Q5: 中國反外國制裁法及實施細則 PRC primary law text (direct long-arm legal source)", "PRC counter-sanctions law primary text")
D["c166"] = A(5, "Q5: MOEA strategic high-tech export control aligning to Wassenaar (Taiwan-side regulatory primary source)", "MOEA Wassenaar alignment update")
D["c167"] = A(5, "Q5: MOEA notice on US export control of 77 machine tools to Russia (direct machine-tool BIS-equivalent enforcement)", "MOEA 77 machine-tool export control to RU")
D["c168"] = A(4, "Q3/Q4: PwC Taiwan cross-strait supply chain relocation transfer-pricing analysis (practitioner perspective on west-bound legal/tax mechanism)", "PwC cross-strait relocation transfer pricing")
D["c169"] = A(4, "Q4: 新南向 — 台商 SEA investment 3-year overtaking China (south-bound hedge official evidence)", "新南向 SEA investment overtakes China")
D["c170"] = A(5, "Q2/E: LTN Ukraine-war-fuelled Taiwan drone exports 41.7x growth (canonical B-track scale evidence)", "LTN Ukraine war + Taiwan drone export 41.7x")
D["c171"] = A(4, "Q2/Q6: USTBC EVP on Taiwan non-red drone supply chain (industry-NGO advocacy framing)", "USTBC EVP Taiwan non-red drones")
D["c172"] = A(4, "Q2/E: TEDIBOA alliance — Taiwan drone international business opportunities (B-track market structure)", "TEDIBOA drone international alliance")
D["c173"] = A(5, "Q2/E/Q6: Guardian Ukraine seeks to push China out of drone supply chain via Taiwan partnership (canonical E-market + non-red framing)", "Guardian Ukraine-Taiwan drone partnership")
D["c174"] = A(5, "Q2/Q5: BusinessWeekly industry whistleblower — Taiwan UAV companies' rebranded-Chinese-product problem (concrete red-supply-chain leakage evidence)", "BusinessWeekly Taiwan UAV rebranded-PRC components")
D["c175"] = R('adjacent_not_material: industry-analyst blog commentary, no primary insight beyond c142/c176')
D["c176"] = A(4, "Q2: War on the Rocks Hellscape Taiwan porcupine drone defense (military-strategic framing)", "War on the Rocks Hellscape porcupine")
D["c177"] = A(4, "Q2/B: AIDC 漢翔 Shield AI partnership Sept 2025 (B-track specific廠商 partnership evidence)", "AIDC Shield AI partnership")
D["c178"] = A(3, "Q1: Threads @letsgolin civil-society reading of 國家無人機隊 + budget cut (seek_direct seed)", "Threads @letsgolin civil reading")
D["c179"] = A(4, "Q2/E: DSET FB on Le Parisien Taiwan non-red drone exports surpassing US (European perspective + Poland data)", "DSET Le Parisien Taiwan non-red drones")

# ── Verify coverage ──────────────────────────────────────────────────────
def load():
    with open(CAND) as f:
        return [json.loads(line) for line in f]

records = load()
ids = {r["id"] for r in records}
decision_ids = set(D.keys())
missing = ids - decision_ids
extra = decision_ids - ids
assert not missing, f"Missing decisions for: {sorted(missing)}"
assert not extra, f"Extra decisions for non-existent ids: {sorted(extra)}"

# ── Write output ──────────────────────────────────────────────────────────
accepted_path = GATE / "accepted.jsonl"
rejected_path = GATE / "rejected.jsonl"

accepted = []
rejected = []
reject_reasons = Counter()
qs_dist = Counter()

for r in records:
    verdict, qs, why, reason = D[r["id"]]
    if verdict == "accept":
        rec = dict(r)
        rec["verdict"] = "accept"
        rec["quality_score"] = qs
        rec["why_relevant"] = why
        rec["gate_reason"] = reason
        accepted.append(rec)
        qs_dist[qs] += 1
    else:
        rec = dict(r)
        rec["verdict"] = "reject"
        rec["gate_reason"] = reason
        rejected.append(rec)
        # extract reason head
        head = reason.split(":")[0].strip()
        reject_reasons[head] += 1

with open(accepted_path, "w") as f:
    for r in accepted:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(rejected_path, "w") as f:
    for r in rejected:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# ── G4 counter-framings balance check ─────────────────────────────────────
import yaml
with open(PIPE / "brief_expanded.yaml") as f:
    bx = yaml.safe_load(f)

ke = bx.get("keyword_expansions", {}) or {}
counter_terms = [t.lower() for t in (ke.get("counter_framings") or [])]
primary_terms = []
for cluster, vals in ke.items():
    if cluster == "counter_framings":
        continue
    if isinstance(vals, list):
        primary_terms.extend([str(v).lower() for v in vals])

counter_count = 0
primary_count = 0
per_framing = {ct: 0 for ct in counter_terms}

# For per-framing breakdown, use semantic keys rather than substring (the
# counter_framings here are full sentences). Map each framing to keywords.
framing_keys = {
    "外銷對沖（無人機整機外銷強勁可補內銷）": ["外銷", "21倍", "21-fold", "41.7", "non-red", "非紅", "poland", "波蘭", "drone export", "uav export"],
    "西進是商業合理性、不必過度國防化": ["business", "商業", "市場規模", "rational", "decoupling", "cost", "成本"],
    "中國市場規模 ≠ 中國長臂管轄": ["市場", "market size", "中國市場"],
    "工具機跟國防製造能力的連結是想像的": ["machine tool", "工具機", "civilian", "dual-use"],
    "南移東南亞才是 hedge 主軸": ["southbound", "新南向", "南向", "vietnam", "越南", "asean", "south-bound"],
    "藍白砍預算是程序問題而非實質": ["procedural", "程序", "預算 程序"],
}

per_framing_semantic = {k: 0 for k in framing_keys}

for r in accepted:
    text = (r.get("title", "") + " " + r.get("abstract_or_snippet", "") + " " + r.get("why_relevant", "")).lower()
    hit_primary = any(pt in text for pt in primary_terms if pt and len(pt) > 2)
    hit_counter = any(ct in text for ct in counter_terms if ct)
    if hit_counter:
        counter_count += 1
    if hit_primary:
        primary_count += 1
    for fk, keys in framing_keys.items():
        if any(k in text for k in keys):
            per_framing_semantic[fk] += 1

print("\n=== GATEKEEPER SUMMARY ===")
print(f"Total candidates: {len(records)}")
print(f"Accepted: {len(accepted)}  ({len(accepted)/len(records)*100:.1f}%)")
print(f"Rejected: {len(rejected)}  ({len(rejected)/len(records)*100:.1f}%)")
print()
print("Quality score distribution (accepted):")
for qs in sorted(qs_dist.keys(), reverse=True):
    print(f"  qs={qs}: {qs_dist[qs]}")
print()
print("Top rejection reasons:")
for reason, n in reject_reasons.most_common(10):
    print(f"  {n:3d}  {reason}")
print()
print(f"Balance: counter={counter_count} / primary={primary_count}")
print()
print("Per-framing accepted-set semantic coverage:")
for fk, n in per_framing_semantic.items():
    print(f"  {n:3d}  {fk[:60]}")

# Detect asymmetry
warn = []
if counter_count == 0:
    warn.append("counter_count==0")
if primary_count == 0:
    warn.append("primary_count==0")
elif counter_count > 0:
    if counter_count / primary_count > 3.0:
        warn.append(f"ratio counter/primary={counter_count/primary_count:.2f}>3.0")
    if primary_count / counter_count > 3.0:
        warn.append(f"ratio primary/counter={primary_count/counter_count:.2f}>3.0")
print()
if warn:
    print("BALANCE WARNING:", warn)
else:
    print("Balance OK.")

# Per-framing at-risk check
at_risk = [fk for fk, n in per_framing_semantic.items() if n == 0]
print(f"At-risk framings (zero coverage): {at_risk}")

print()
print(f"Wrote: {accepted_path}")
print(f"Wrote: {rejected_path}")
