# Post-patch addendum — ai-kiosk-consent-tw v1

**Date**: 2026-05-27
**Status**: Informational; does NOT supersede `review/review.md` (the canonical meta-merged review)

## Background

Stage 6a originally ran in **2-senior fallback** mode after Gemini MCP timed out 3× (210s provider-side, `totalCalls: 0` in get-usage-stats indicating the call never reached LLM). Root cause traced post-hoc: `ask-gemini-mcp@1.6.3` wrapper does not pass `--yolo` to underlying `gemini` CLI, so CLI hangs at approval prompt indefinitely. MCP server is alive (ping ✓) but the wrapper-to-CLI handoff fails silently.

**Workaround applied**: bypass MCP entirely; invoke `gemini -p --yolo` directly via Bash, pipe `_prompt.md` as primary instruction. Returned in ~5 minutes. Output cleaned (4 leading stderr lines stripped) and written to `multi_model/r_gemini.md`.

## Gemini verdict tally (post-patch)

Important: Gemini reviewed **v1 AFTER the 3 P0 hand-edits were applied** — so her assessment reflects the patched wording (F7 「capacity upper-bound proxy」, F4 「[speculative-mechanism] RAM/cache」 etc.), not the pre-patch wording that Claude+Codex reviewed.

- F1 ✅ · F2 ✅ · F3 ✅ · F4 ✅ · F5 ⚠️ · F6 ✅ · F7 ✅ · F8 ✅
- Tally: 7 ✅ / 1 ⚠️ / 0 ❌ / 0 🚨
- Overall: 🟢 publishable as-is (with note that F5 vendor-role-layer warrants minor potential refinement)

## Convergence analysis

| Finding | Claude (pre) | Codex (pre) | Gemini (post) | Interpretation |
|---|---|---|---|---|
| F1 | ✅ | ⚠️ | ✅ | Codex's wording concern remains valid but non-blocking |
| F2 | ⚠️ | ⚠️ | ✅ | Pre-patch artifact-flow over-claim flags; Gemini didn't catch (lenient bias) |
| F3 | ✅ | ✅ | ✅ | Unanimous strongest finding |
| F4 | ⚠️ | ❌ | **✅** | **Hand-edit patch validated** — Gemini's L7 ✅ explicitly cites the new [speculative-mechanism] tag and transferability scope_caveat as honest |
| F5 | ✅ | ⚠️ | **⚠️** | **Convergent residual** — independent Codex+Gemini catch on SDK upstream vs Kiosk integrator vs end-deployer responsibility-layer ambiguity. **Sole remaining ⚠️ for v2 / next-pass consideration.** |
| F6 | ⚠️ | ⚠️ | ✅ | Pre-patch absence-of-evidence overreach flag; Gemini didn't catch (lenient + not in her junior scope) |
| F7 | ❌ | ❌ | **✅** | **Hand-edit patch validated** — Gemini explicitly cites the new「capacity upper-bound proxy 而非投訴量下界」wording as closing the over-claim |
| F8 | ⚠️ | ⚠️ | ✅ | Home Depot scope_caveat + c070 cherry-pick still warranted per pre-patch senior consensus |

## Calibration notes (per multi-model spec §2)

Gemini's lenient verdict pattern (7✅/1⚠️ vs Claude 3✅/4⚠️/1❌ vs Codex 1✅/5⚠️/2❌) is **consistent with the documented bias** in `tools/insight-pipeline/backlog/multi-model-reviewer.md` §2:「verdict severity instability… lenient 偏向觀察」. Her ✅ verdicts on F4 / F7 do NOT override the senior reviewers' pre-patch ❌s under §8 stricter-wins; the senior ❌s correctly identified publication-blocker issues that the hand-edit patch then addressed.

The meaningful contribution of Gemini's post-patch pass:
1. **3-reviewer integrity completeness** — `integrity_check.py` now confirms all three reviewers achieved 0 hallucinated cid / 0 count_mismatch (the spec §4 source-pool-integrity self-reminder prefix worked as documented)
2. **Post-patch independent validation** of F4 + F7 remediation (Gemini wasn't briefed that a patch was applied; she independently judged the patched wording as ✅)
3. **F5 convergent residual** — independent confirmation of the sole remaining ⚠️ worth potential v2 attention (SDK supplier vs kiosk integrator vs end-deployer responsibility-layer split)

## What this does NOT change

- `review/review.md` canonical merged verdict (🟡 publishable with edits) — Gemini lenient ✅ doesn't override §8 stricter-wins
- state.yaml stays at `current_stage: done, status: done`
- No new hand-edits needed; F5 ⚠️ is contested-tier rhetorical refinement, not publication blocker

## Spec / tooling feedback (queued for `backlog/multi-model-reviewer.md`)

1. **MCP wrapper failure mode** — `ask-gemini-mcp@1.6.3` does not pass `--yolo` to gemini CLI, causing silent indefinite hang at approval prompt. Document the bypass-via-direct-CLI workaround in spec §9.5 (graceful degrade). Either pin a different MCP wrapper, fork `ask-gemini-mcp` with `--yolo`, or document Bash-bypass as official fallback.
2. **Post-patch re-review pattern** — when meta-reviewer recommends ship-with-patch and operator applies hand-edits, useful to re-run ONE reviewer (junior is sufficient) for independent post-patch validation. Should this be a documented optional Stage 6d in spec?
3. **`totalCalls: 0` as MCP health signal** — get-usage-stats showing 0 calls after multiple timeout attempts is a strong signal that MCP wrapper-to-LLM handoff is broken (not provider slowness). Add as diagnostic in operator runbook.
