# Design refresh audit (Phase 2 of design-refresh-2026-05)

**Date:** 2026-05-26
**Scope:** 5 in-scope reports + pilot (legacy) + landing
**Tool:** `~/.claude/skills/generate-research-html/references/lint.py`

## TL;DR

The 5 in-scope reports are **already well aligned within their Template family**. The drift I worried about in Phase 0 (`--paper` cool vs warm) turned out to be by-design template differentiation, not accidental drift.

→ **Phase 3 turns out to be near no-op.** The one genuine cross-report divergence is `--mono` in Template B (defense-cut uses SF Mono, scam uses IBM Plex Mono). Fixing it is a visible visual change, not silent alignment — needs your OK.

## Lint findings (after lint.py improvements)

Two lint rules were fixed during this audit:
1. Google Fonts double-count (preconnect was being counted as a stylesheet) — fixed
2. Non-canon font list didn't include Template C's PingFang TC / Helvetica Neue — fixed

| Report | Errors | Warnings |
|---|---|---|
| sycophancy | 1 (inline `#fff` in inline `<code>`) | 1 (inline `font-size:18px` on a transition paragraph) |
| defense-cut | 0 | 1 (one inline `font-size`) |
| scam | 0 | 14 (inline `font-size` on prose + code spans) |
| advocacy | 0 | 1 |
| multiturn | 0 | 3 |
| pilot (legacy) | 1 (pilot-specific blue inline hex × 3) | 1 (Noto Sans TC — pilot only) |
| **landing (new)** | 0 | 0 |

### Interpretation

**The warnings are mostly intentional hand-tunings** done by [revise-research-html skill](../../.claude/skills/revise-research-html). For example:
- scam line 920: `<code style="font-family:var(--mono);background:var(--paper-sink);padding:1px 5px;border-radius:3px;font-size:14px">word1018.shop</code>` — this is inline code styling that uses token vars but inlines the chrome. Acceptable.
- sycophancy line 474: `<p style="margin-top:30px;...">下一頁是 192 段對話...</p>` — transition paragraph between sections. Acceptable.

These are not "drift" — they're authored micro-adjustments that don't recur and therefore don't belong in a class. The lint warns out of caution; review case-by-case agrees with the original choice.

### The one real cross-report divergence

```
defense-cut:  --mono: ui-monospace, 'SF Mono', Menlo, 'Noto Serif TC', monospace
scam:         --mono: 'IBM Plex Mono', 'Noto Serif TC', monospace
                      ^^^^^^^^^^^^^^^ also needs Google Fonts link to load
```

defense-cut falls back to system monospace because it doesn't import IBM Plex Mono. If we align defense-cut to scam's stack (the skill's canonical `--ff-mono`), the monospace labels throughout the sidebar / find cards / hero kickers will **visibly change** (system font → IBM Plex Mono). It's still acceptable typographically, but it is a visible change, not silent.

## Phase 3 decision

Three options:

| Option | Action | Visible change | Risk |
|---|---|---|---|
| **Skip** | Do nothing. Document the divergence. | None | None |
| **Align defense-cut `--mono`** | Add `IBM+Plex+Mono` to defense-cut's Google Fonts link + change `--mono` value | Subtle but visible across all mono labels | Low (typography only) |
| **Defer to v0.3** | Bundle with future broader visual unification work | None now | None |

My recommendation: **Skip** (or defer). The Template B reports already share `--paper`, `--paper-card`, `--ink`, font hierarchy, role colors. The mono difference is the only crack and it's not visually offensive — defense-cut's system mono renders perfectly readable. Forcing alignment buys little, costs a visible change to a published report.

## What Phase 1 (landing) accomplished

Re-check landing against the lint = **all checks pass**. The new landing:
- Uses skill's `--c-paper` / `--c-ink` namespace (lead-by-example for future migrations)
- Carries 3-family visual hints (left-border in family color + monospace tag)
- Resolves the orphan `#7a3e2a` brown that matched nothing
- Adds a tiny color-key legend at the bottom for reader orientation
- Pilot link gets `<span class="li-tag">早期版型</span>` to flag as legacy

## What's NOT in this audit

- Visual regression check (no browser-rendered comparison; you'll review by eye)
- Whether the new landing's family hints feel right typographically (subjective)
- Whether legacy pilot deserves a Template C rebuild (separate decision)

## Sequence going forward

1. ✅ Phase 1: Landing redesign — done
2. ✅ Phase 2: A audit — this document
3. ⏭ Phase 3: Skip (or your call: align `--mono`)
4. ✅ Phase 4: pilot legacy treatment — handled in Phase 1 landing
5. → Wrap-up: local commit on branch, summarize what to push

If you OK skipping Phase 3, ready to commit + summarize for push.
