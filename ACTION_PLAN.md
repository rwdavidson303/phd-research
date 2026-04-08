# PhD Research Action Plan
## "From Lowest Price to Highest Public Value"
### Richard Davidson — Indiana University, Kelley School of Business
### Generated: March 24, 2026

---

## Executive Summary

This action plan synthesizes findings from a comprehensive research sprint using both the Sofi swarm (6 parallel worker agents) and Claude Code analysis agents. The core finding is that while the conceptual framework is strong, the empirical execution needs a fundamental reset to produce publishable, defensible research.

**Key discoveries:**
1. FPDS has a `source_selection_process` field (LPTA/TO) available from ~FY2020 onward
2. **A 100-million-record academic FPDS dataset exists on Figshare** (Omari, Alansari, Libgober & Kaufman, 2025, Nature Scientific Data) — 470 variables, Parquet format, 1979-2023
3. No published study has used NDAA Section 813 as a natural experiment — major contribution opportunity
4. The empirical literature is nearly empty (only Hawkins et al. 2017, N=124)
5. CPARS performance data is legally inaccessible — must use FPDS proxy measures
6. Current dataset has critical quality issues: single quarter, proxy treatment variable, 44.8% missing DV

---

## Current State Assessment

### What's Strong
- Excellent theoretical framework (public value theory, TCE, principal-agent, auction theory)
- Extensive literature review (300+ references, well-structured)
- Policy-relevant research question with Congressional interest
- Practitioner credibility (DoD + state/local procurement experience, both sides)
- Research infrastructure (website, automated article search, data pipeline)
- International comparison data (26 vendor journey documents, 12 countries)

### Critical Issues Requiring Action
1. **Data**: Single quarter (FY2024 Q2), only ~2,222 usable observations with cost_growth data
2. **Treatment Variable**: USAspending doesn't include `source_selection_process` — current classification is an imputed proxy from solicitation procedures + pricing type
3. **Results**: All main hypotheses null (p > 0.05 except H8 moderation), some effects in wrong direction
4. **Identification**: No causal identification strategy (PSM pseudo-R² = 0.106, 21% unmatched)
5. **Outcomes**: No actual performance data (CPARS legally unavailable); only cost growth and modification counts

---

## THE GAME-CHANGING DATASET

### Omari, Alansari, Libgober & Kaufman (2025)
**"A Comprehensive Dataset of United States Federal Procurement, 1979-2023"**
- **Published:** Nature Scientific Data (August 2025)
- **DOI:** https://doi.org/10.1038/s41597-025-05714-1
- **Figshare:** https://springernature.figshare.com/articles/dataset/A_Comprehensive_Data_Set_of_US_Federal_Procurement_1979-2023/28057043
- **GitHub:** https://github.com/aaronrkaufman/FPDS_replication
- **Size:** 99,057,002 rows × 470 variables, 75+ GB in Parquet format
- **Coverage:** 1979-2023 (45 years of federal procurement)
- **Variable dictionary:** JSON format with definitions, types, valid values, and availability over time
- **License:** Open access for academic use
- **Access tools:** R `arrow` library or Python `dask`/`pyarrow`

### Critical Question: Does It Include `source_selection_process`?
The FPDS `source_selection_process` field was mandated by DPC Memorandum dated May 21, 2020. The field has values:
- **LPTA** — Lowest Price Technically Acceptable
- **TO** — Tradeoff (Best-Value)
- **O** — Other

Since the dataset includes 470 of FPDS's 1,000+ variables and covers through 2023, it likely includes this field for FY2020-FY2023 records. **VERIFY THIS IMMEDIATELY by downloading the variable dictionary JSON.**

### If It Includes `source_selection_process`:
This single dataset transforms the entire dissertation:
- **From 3,869 records → potentially 500,000+ classified LPTA/TO records (FY2020-2023)**
- **Direct treatment variable** instead of proxy classification
- **Multi-year data** enabling time-series analysis and the Section 813 DiD design
- **470 control variables** for robust matching and regression
- **Published, peer-reviewed data source** — bulletproof for committee review

---

## Phase 1: Data Foundation (Weeks 1-2)

### Priority 1A: Download and Evaluate the Kaufman et al. Dataset
1. Download the variable dictionary JSON from the Figshare page
2. Search for `source_selection_process` in the variable list
3. If present: download the Parquet shards for FY2017-2023 (for Section 813 analysis)
4. Install `pyarrow` and `dask` for Python access
5. Filter to service/IT NAICS codes and examine `source_selection_process` coverage

### Priority 1B: Alternative FPDS Access (if needed)
- Install `fpds` Python library (dherincx92/GitHub) for ATOM feed queries
- Register for SAM.gov API access (1-4 weeks approval)
- Retry USAspending bulk downloads for FY2020-FY2024

### Deliverable: Analysis-ready dataset with verified LPTA/Tradeoff classification, 4+ years, 50K+ records

---

## Phase 2: The Section 813 Natural Experiment (Weeks 3-6)

### Why This Is Your Strongest Play
**No published academic study has used NDAA Section 813 as a natural experiment.** This is confirmed by the swarm's competing research analysis — the field is wide open.

### Design: Difference-in-Differences

**Treatment group:** DoD contracts in restricted categories (IT, cybersecurity, knowledge-based services)
**Control group 1:** DoD contracts in unrestricted categories (commodities, simple supplies)
**Control group 2:** Civilian agency contracts (not restricted until FY2019 Section 880)

### Key Timeline
| Date | Event |
|------|-------|
| Dec 23, 2016 | Section 813 enacted (FY2017 NDAA) — DoD LPTA restrictions |
| Dec 12, 2017 | Section 822 enacted (FY2018 NDAA) — reinforcement |
| Aug 13, 2018 | Section 880 enacted (FY2019 NDAA) — government-wide extension |
| Oct 2019 | Final DFARS rule implementing Section 813 |

### Section 813 Criteria (all 6 must be met to use LPTA):
1. Minimum requirements clearly identified
2. Little/no value in exceeding minimum technical requirements
3. Little/no subjective evaluation needed
4. High confidence reviewing non-lowest bidders wouldn't reveal additional value
5. Little/no additional innovation from alternative source selection
6. Goods are expendable, nontechnical, or have short shelf life

### Reframed Hypotheses

**H1 (First Stage):** DoD LPTA usage in restricted categories declined significantly after Section 813 relative to civilian agencies.

**H2 (Main Effect):** Cost growth in affected DoD contract categories declined after Section 813 relative to control groups.

**H3 (Mechanism):** Competition intensity (number of offers) increased in affected categories after Section 813.

**H4 (Heterogeneity):** The effect is larger for complex, high-value contracts than for routine, low-value contracts.

**H5 (Implementation):** The effect appears at regulatory implementation (Oct 2019) rather than statutory enactment (Dec 2016), consistent with GAO's finding of delayed compliance.

### Complications to Address
- **33-month implementation lag** — use both statutory and regulatory dates as robustness checks
- **"Maximum extent practicable" language** — soft restriction, not hard mandate
- **Anticipation effects** — LPTA usage was already declining before Section 813
- **Multiple concurrent provisions** — use falsification tests on untargeted categories

---

## Phase 3: Publication Strategy (Months 2-12)

### Paper 1: The Section 813 Natural Experiment
**Target:** Journal of Public Procurement (primary) → JPART (ambitious)
**Title:** "The Policy Shock That Didn't Shock: Evaluating Congressional LPTA Restrictions on Federal Procurement Outcomes"
**Timeline:** Months 2-6

### Paper 2: Transaction Cost Moderation
**Target:** JPART
**Title:** "Transaction Costs as Moderators of Procurement Design: When Does Source Selection Method Matter?"
**Leverage:** Current H8 moderation finding as seed
**Timeline:** Months 5-8

### Paper 3: International Comparison (QUICK WIN — data already exists)
**Target:** IJPA or Journal of Public Policy
**Title:** "Comparing Procurement Entry Barriers Across 12 Countries"
**Leverage:** 26 vendor journey documents, 87x cost differential finding
**Timeline:** Months 1-3

### Paper 4: Competition Dynamics
**Target:** Public Performance & Management Review
**Title:** "Single-Bid Awards in Federal IT Procurement: Prevalence, Predictors, and Consequences"
**Timeline:** Months 6-10

### Paper 5: Systematic Literature Review (QUICK WIN — lit review already done)
**Target:** Journal of Public Procurement
**Title:** "The Source Selection Evidence Gap: A Systematic Review and Research Agenda"
**Timeline:** Months 1-4

### Journal Details

| Journal | Acceptance Rate | Review Model | Key Requirement |
|---------|----------------|-------------|-----------------|
| Journal of Public Procurement | Moderate | Double-blind | Procurement-specific empirical work |
| JPART | 10-15% | Double-blind | Strong theory + rigorous methods |
| PAR | 9% | Double-blind | Broad PA significance, ≤8,000 words |
| IJPA | Moderate | Peer review | Comparative/international angle |
| J. Defense Analytics & Logistics | Moderate | Peer review | DoD-specific findings |

---

## Phase 4: PhD Program Preparation (Months 6-12)

### IU Kelley Faculty (from swarm research)
- Research faculty who publish in PA journals, procurement, quantitative methods
- Attend IU Kelley seminars or events before enrollment
- Identify 2-3 potential advisors and read their recent publications

### Professional Network Building
- Join National Contract Management Association (NCMA)
- Attend NCMA World Congress
- Connect with procurement researchers (Rendon, Hawkins, Kelman)
- Reach out to the Kaufman et al. dataset authors — potential collaboration

### Skills Development
- Python data science (pandas, pyarrow, statsmodels) — enough to run own analyses
- Causal inference methods (DiD, event studies, synthetic control)
- Academic writing for journals (distinct from practitioner writing)

---

## Immediate Next Steps (This Week)

- [ ] Download Kaufman et al. variable dictionary from Figshare
- [ ] Check if `source_selection_process` is among the 470 variables
- [ ] Install `pyarrow` and `dask` for Python Parquet access
- [ ] Download FY2017-2023 Parquet shards (if source_selection_process present)
- [ ] Begin writing Paper 3 (international comparison) from existing material
- [ ] Begin writing Paper 5 (systematic lit review) from existing lit review chapter

---

## CPARS Alternative: Performance Proxy Measures

Since CPARS is legally protected (FAR 3.104, FOIA-exempt), use these FPDS-derived proxies:

| Proxy Metric | Source | Measurement | Validity |
|-------------|--------|-------------|----------|
| Cost growth | FPDS | (Final obligations – Initial value) / Initial value | Moderate-Good |
| Modification intensity | FPDS | Modifications per $M or per year | Moderate |
| Schedule adherence | FPDS | Actual vs. planned completion date | Moderate |
| Terminations for default | FAPIIS/SAM.gov | Binary indicator | Very Good (extremes) |
| Option exercise rates | FPDS | Whether option years were exercised | Moderate |
| Recompetition success | FPDS (matching) | Incumbent retention rate | Moderate-Good |
| Bid protests | GAO decisions | Protests filed and sustained rates | Moderate |

**Recommended composite:** Cost Performance Index + Modification Intensity + Schedule Adherence + Adverse Action Indicator

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Kaufman dataset doesn't include source_selection_process | FPDS ATOM feed + `fpds` library as backup |
| source_selection_process sparsely populated pre-FY2021 | Focus on FY2021-2023; use pre-2020 data with proxy classification as robustness check |
| Section 813 effects confounded by concurrent policies | Staggered DID; falsification tests on unrestricted categories; event study |
| Null results persist with better data | Frame as "context matters more than method" (Paper 2 moderation) |
| Advisor at IU doesn't support this direction | Methods are generalizable; work stands independently |

---

## Budget

| Item | Estimated Cost |
|------|---------------|
| Kaufman dataset | Free (open access) |
| FPDS ATOM feed | Free |
| SAM.gov API | Free |
| Python tools | Free (open source) |
| NCMA membership | ~$200/year |
| Journal OA fees | $0-3,000/article |
| **Total** | **$200-3,200** |
