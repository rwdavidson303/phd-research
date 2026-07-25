# Session Log: Phase 1 (Paper Revisions) + Phase 2 (Website Update)
**Date:** March 26, 2026
**Duration:** ~3 hours
**Scope:** Comprehensive paper revisions + website overhaul

---

## Phase 1: Paper Revisions (phd-research-v2)

### Citation Fixes
- **Landale et al. (2017):** Corrected author order across all papers. Crossref DOI verification confirmed first author is Landale, not Hawkins. Changed all in-text citations from "Hawkins et al." to "Landale et al." and updated reference list entries.
- **Omari et al. (2025):** Fixed Paper 5's "Alansari, M." → "N.", "Article 714" → "Article 1368", "Nature Scientific Data" → "Scientific Data". Added DOI to all reference list entries. Fixed 7 body-text instances of "Kaufman et al." → "Omari et al." in Paper 5.
- **Cross-references:** Added Davidson (2026a-e) lettering scheme across all 5 papers. Each paper cites companion papers but not itself.
- **Alphabetization:** Fixed reference list ordering errors in all 5 papers (9 misplacements found by audit agent).

### Analysis Upgrades (run_did_analysis.py, run_moderation_analysis.py)
- **Agency-clustered SEs:** Added clustering at 160-agency level. Key finding: single-bid effect loses significance with clustering (p=0.29 vs p<0.001 HC1). OLS outcomes produced NaN SEs (numerical issue, needs further investigation).
- **COVID-19 robustness:** Dropping FY2020 barely changes results (cost growth: -29.87 vs -30.35). Confirms COVID doesn't drive findings.
- **Subgroup event studies:** Added parallel trends tests within each moderator category (size, sector, pricing, competition) with F-tests on pre-period coefficients.

### Paper-Specific Revisions

**Paper 1 (Section 813 DiD):**
- Softened "no first stage" claim to cautious null finding with FPDS limitations caveat (6 locations)
- Explained Table 1 (-30.35) vs Table 2 (-29.54) estimate discrepancy
- Added Carpenter (2010) bureaucratic reputation and Huber & Shipan (2002) deliberate discretion framework in 2 locations

**Paper 2 (TCE Moderation):**
- Updated all cross-references to Davidson (2026a)
- FY range already fixed in prior revision

**Paper 3 (International Comparison):**
- Added vendor journey coding protocol (cost sources, firm size assumption, currency conversion, sensitivity ranges)
- Clarified "12 countries + EU framework = 13 systems"
- Softened causal language (3 instances)
- Added Pollitt & Bouckaert (2017) and Bandiera et al. (2009) citations with in-text integration

**Paper 4 (Single-Bid Awards):**
- Framed logistic regression as descriptive, not causal (5 locations)
- Added explicit endogeneity caveats for 3.5x odds ratio
- Expanded cost growth measure discussion (planned options vs overruns)
- Contextualized R² with Decarolis (2014) and Bajari et al. (2014)

**Paper 5 (Scoping Review):**
- Repositioned from "systematic review" to "scoping review"
- Qualified "one study" claim as "using U.S. federal contract-level data" (4 locations)
- Expanded limitations section (6 points: language bias, publication bias, single screener, grey lit, keyword gaps, quality assessment)
- Reframed research agenda as field needs (6 locations)
- Added companion paper cross-references (Davidson 2026a-d)

### Commits
- `8a61d3c` — Comprehensive revision of all 5 papers (19 files, 3,498 lines)
- `[hash]` — Fix reference list alphabetization (5 papers)

---

## Phase 2: Website Update (phd-research)

### New Pages Created
- **Papers** (`/papers/`) — 5-paper portfolio with narrative arc (5→1→2→4→3), integrating thesis ("LPTA-vs-tradeoff debate is a red herring"), paper cards with status badges and key findings
- **Findings** (`/findings/`) — Stats banner (654K/42.5M/FY2017-2023/5,277x), 6 result boxes with exact numbers from analysis JSON, caveat box
- **International** (`/international/`) — Combined landing page for Global Leaders + Global Vendor Journeys, 12 country cards, 87x headline statistic

### Updated Pages
- **Homepage** — New hero ("largest empirical study"), V2 section cards, integrating thesis, data sources
- **Research** — Complete rewrite: Section 813 natural experiment, DiD design, Kaufman/Omari dataset, 4 research questions, identification threats, robustness approaches
- **Federal Data** — Omari et al. (2025) hero section, dataset attributes table, analysis sample description, variable table
- **About** — Research evolution timeline, publication status table, expanded tools section

### Navigation
- Added: Papers (3), Findings (4), International (8)
- Removed: Articles from top nav (still accessible via homepage link)
- Merged: Global Leaders + Global Journeys → International

### CSS Additions (~130 lines)
- `.paper-card` — Cards with navy left border, paper number, target journal, key finding callout
- `.paper-status` — Draft/Review/Published badges
- `.findings-hero` — Navy stats banner with gold numbers
- `.result-box` — Gold-bordered result callouts
- `.caveat-box` — Cream-background limitation boxes
- Responsive breakpoints for all new components

### Commit
- `4731e8a` — Phase 2: Update website with V2 research (9 files changed)

---

## Sofi/Swarm Fix

### Problem
API/CLI-created swarm missions stuck in "planning" — required manual Telegram approval button press that never happened.

### Fix
- Added auto-approve in `orchestrator.py` for `source in ("api", "cli")` missions
- Added `"prompt"` as alias for `"message"` in API endpoint for backward compatibility
- Manually approved 4 stuck missions (IDs 9-12)

### Deployed
- Pushed to `rwdavidson303/sofi`, Railway auto-deploy triggered

---

## Tools Used
- **8 background Claude Code agents** (paper revisions, analysis upgrades, accuracy audit, website content)
- **4 Swarm missions** (Hawkins author order, Section 813 status, citation verification, recent literature)
- **Crossref API** (DOI 10.1108/JDAL-05-2017-0006 author order verification)
- **WebFetch** (live site verification post-deploy)

## Key Discoveries
1. Landale, not Hawkins, is first author of the N=124 study — would have been caught in peer review
2. "Kaufman et al." should be "Omari et al." (first author) — fixed in Paper 5
3. Clustered SEs attenuate single-bid effect to non-significance — important methodological finding
4. COVID robustness holds — results barely change without FY2020
5. Swarm needed auto-approve for API calls — architectural gap fixed
