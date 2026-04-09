# Session Log — 2026-04-09: Site Maintenance, Security Audit & Bug Fixes

## Summary

Routine maintenance session covering navigation fixes, article database cleanup, security hardening, and UI improvements to the PhD research website.

---

## Changes Made

### 1. Added "Articles" to Navigation Menu
- **File:** `website/hugo.yaml`
- **Issue:** The Articles page (`/articles/`) existed but was missing from the site navigation bar
- **Fix:** Added `Articles` menu entry at weight 6, between Literature and Federal Data

### 2. Article Database — Duplicate Removal & Improved Deduplication
- **File:** `automation/update_articles_cloud.py`
- **Issue:** 18 duplicate articles in the database (451 total, 433 unique). Caused by the dedup logic only using MD5 of `title|authors` — OpenAlex sometimes returns slightly different author names for the same article (e.g., "Fang Qiu" vs "Fangjun Qiu")
- **Fix:** Added three layers of deduplication:
  1. DOI-based matching (catches same article with different author formatting)
  2. Normalized title matching (strips all punctuation/spaces for comparison)
  3. Runs dedup on existing database at startup, plus prevents new dupes during search
- **Result:** 451 → 431 articles (20 duplicates removed)

### 3. Restored Daily Digest Generation
- **Files:** `automation/update_articles_cloud.py`, `.github/workflows/update-articles.yml`
- **Issue:** Daily digest markdown files stopped being generated after Feb 25, 2026. The digest logic existed only in the legacy local script (`daily_article_search.py`), but the GitHub Action only runs the cloud script (`update_articles_cloud.py`)
- **Fix:** Added `generate_digest()` function to the cloud script; updated GitHub Action to commit digest files to `research/articles/digests/`
- **Result:** Digests will now be generated on every daily run

### 4. Reduced Page Header Font Sizes
- **File:** `website/layouts/_partials/site-header.html`
- **Issue:** Page titles were excessively large — `f-subheadline-l` class rendered at ~80px on large screens
- **Fix:** 
  - Title: `f-subheadline-l` (~80px) → `f2-l` (~36px)
  - Description: `f3-l` → `f5-l`
  - Reduced vertical padding (`pv4-l` → removed)

### 5. Security Fixes

#### Decision Tool XSS (Critical → Fixed)
- **File:** `website/content/decision-tool/_index.md`
- **Issue:** Inline `onclick` handlers used string concatenation, which is an XSS vector pattern
- **Fix:** Replaced all inline `onclick` attributes with `addEventListener` calls
- **Note:** Not actively exploitable (all values are hardcoded), but the pattern was unsafe

#### Markdown Table Injection (Medium → Fixed)
- **File:** `automation/update_articles_cloud.py`
- **Issue:** Article titles from OpenAlex API were embedded in markdown tables without sufficient escaping. Combined with Hugo's `unsafe: true` setting, a malicious title could potentially inject HTML/JS
- **Fix:** 
  - Added `sanitize_markdown()` function to escape `[]|` characters in titles
  - Restricted article link URLs to `https://doi.org/` and `https://openalex.org/` only

#### Remaining (Accepted Risk)
- Hugo `unsafe: true` in `hugo.yaml` — needed for inline HTML/JS in decision tool, vendor journey, and other pages. Low risk since all content is author-controlled.

---

## Site Health Check

All 14 pages verified as loading correctly with content:

| Page | Status |
|------|--------|
| Home | OK |
| Research | OK |
| Papers | OK |
| Findings | OK |
| Literature | OK |
| Articles | OK |
| Federal Data | OK |
| Vendor Journey | OK |
| International | OK |
| Briefs | OK |
| Decision Tool | OK |
| Tracker | OK |
| People | OK |
| About | OK |

---

## Commits

1. `c73ab0e` — Add Articles page to navigation menu
2. `bfd8601` — Fix article dedup and restore daily digest generation
3. `fb612f0` — Reduce page header font sizes and fix security issues
