# Session Log: Vendor Journey — Regulatory Burden Visual

**Date:** February 27, 2026
**Commits:** 9 (ed280a8 through 07e3707)

---

## Objective

Add a powerful visual to the Vendor Journey page showing the enormous regulatory burden federal contractors face — the sheer volume of FAR pages, directives, and agency supplements they must master before earning a dollar.

---

## What Was Done

### Attempt 1: Snake-Path Overview (Reverted)

Built a CSS-only winding 4-row × 7-column snake path showing all 28 vendor journey steps. Two issues:
1. **Goldmark rendering bug** — 4-space indentation after blank lines in Hugo markdown gets treated as code blocks, causing raw HTML to display as text. Fix: flatten all indentation to 0 spaces.
2. **User feedback** — "Just a snake version of the linear list below." Didn't add new information or emotional impact. Reverted entirely.

**Lesson:** Hugo/Goldmark rule — never use 4+ spaces of indentation after a blank line in HTML blocks within markdown files. Keep all embedded HTML at 0–2 spaces max.

### Attempt 2: Regulation Brick Wall (Replaced)

Built a CSS grid of 54 labeled bricks (navy = FAR core, red = DoD, gold = agency supplements) with a legend. User feedback: "Just a bunch of bricks, doesn't evoke emotion." Needed something that makes readers say "Wow."

### Attempt 3: Counter with Harry Potter Comparison (Final)

The winning design. A massive "2,000+" number dominates the section, flanked by satellite stats. Below: a devastating comparison that lands emotionally.

**Layout (top to bottom):**
- Section title: "The Regulatory Burden"
- Subtitle: "Before writing a single proposal, a contractor must master all of this"
- Hero row: `53 FAR Parts` ← **`2,000+` PAGES** → `30+ Agency Supplements`
- Second row: `~3,000 individual directives` | `+1,000 more pages for DoD (DFARS alone)`
- Comparison box (navy with gold borders):
  > The entire **Harry Potter** series is 4,224 pages.
  > The **FAR + DFARS** is comparable in length.
  > One is fiction. The other is *required reading* — before you earn $1.
- Citation footnote: acquisition.gov/FAR · acquisition.gov/DFARS · EO 14275

### Page Reordering

After the visual was finalized, reordered the page sections:
1. **The Regulatory Burden** (new section — leads the page)
2. **The Qualification Gauntlet** heading
3. **Stats banner** (28+ steps / $12K–$530K+ / 3–12 Months) — moved directly under the heading
4. Subtitle + intro paragraph
5. Timeline steps (unchanged)

### CSS Centering Fix

Gave satellite stats equal fixed widths (140px) so the center "2,000+" box sits symmetrically aligned with the Harry Potter comparison box below.

---

## Key Numbers (Verified)

| Metric | Value | Source |
|--------|-------|--------|
| FAR page count | 2,000+ | EO 14275, acquisition.gov |
| FAR directives | ~3,000 | EO 14275 |
| FAR parts | 53 | acquisition.gov |
| DFARS additional pages | ~1,000 | acquisition.gov/DFARS PDF |
| Agency supplements | 30+ | CRS Report R42826 |
| Harry Potter total pages | 4,224 | Published book data |

---

## Files Modified

- `website/content/vendor-journey/_index.md` — New regulatory burden HTML block + page reordering
- `website/static/css/custom.css` — `vj-regburden-*` styles (hero, satellites, comparison box, responsive, print)

---

## Lessons Learned

1. **Hugo/Goldmark HTML blocks:** Never indent 4+ spaces after a blank line — Goldmark interprets it as a code block. Flatten all embedded HTML to 0 indentation.
2. **Visual impact over data density:** A wall of 54 labeled bricks conveys information but not emotion. A single massive number with a relatable comparison (Harry Potter) lands harder than exhaustive detail.
3. **Iterate through user feedback:** Three attempts with different visual approaches. The user knows what "feels" right — ask for reactions early.
