---
title: "Federal Procurement Data"
description: "USAspending, FPDS, GAO protest data, and analysis"
weight: 3
---

### The Omari et al. (2025) FPDS Dataset

> Omari, S., Alansari, N., Libgober, B., & Kaufman, A. R. (2025). A comprehensive dataset of United States federal procurement, 1979-2023. *Scientific Data*, 12, Article 1368. [DOI: 10.1038/s41597-025-05714-1](https://doi.org/10.1038/s41597-025-05714-1)

This peer-reviewed dataset, published in *Scientific Data*, represents a transformative resource for procurement research:

| Attribute | Value |
|-----------|-------|
| Total records | 99,057,002 |
| Variables | 470 |
| Time span | FY1979-2023 |
| Format | Parquet (open access on Figshare) |
| Key field | `source_selection_process` (LPTA/TO/Other, FY2020+) |

### Our Analysis Sample

From this dataset, we constructed a sample of **654,307** competitively awarded service and IT contracts (NAICS 51, 54, 56) spanning FY2017-2023.

| Variable Type | Variables |
|---------------|-----------|
| Treatment | is_dod, is_restricted, post_813, treatment_did |
| Outcomes | cost_growth_winsorized, modification_count, single_bid, log_num_offers |
| Controls | log_base_amount, NAICS FE, fiscal year FE, pricing type FE |

---

## Federal Procurement Data Hub

This section tracks and analyzes federal procurement data relevant to the dissertation.

### Data Sources

| Source | Description | Update Frequency |
|--------|-------------|-----------------|
| [USAspending.gov](https://www.usaspending.gov) | Contract award records with source selection process codes | Automated downloads |
| [FPDS](https://www.fpds.gov) | Federal Procurement Data System - detailed contract data | Linked via USAspending |
| [GAO Bid Protests](https://www.gao.gov/legal/bid-protests) | Annual protest statistics and decision dockets | Annual + ongoing |
| [CPARS](https://www.cpars.gov/cparsweb/home) | Contractor Performance Assessment Reporting System | Access pending |

### Key Variables

- **Source Selection Process** - LPTA vs. tradeoff (from FPDS)
- **Contract Type** - Fixed-price, cost-reimbursement, T&M
- **NAICS/PSC Codes** - Industry and product/service classification
- **Competition Details** - Number of offers, competition type
- **Obligations** - Award amounts and modifications over time
- **Key Dates** - Solicitation, award, period of performance

### Analysis Pipeline

1. **Download** - Automated scripts pull data from USAspending API
2. **Clean** - Standardize variables, handle missing data
3. **Classify** - Tag awards by source selection method
4. **Analyze** - Quasi-experimental analysis (DiD, PSM)
5. **Visualize** - Charts, tables, and dashboards

### Getting Started

```bash
# Download current fiscal year data
python data/usaspending/download_awards.py --fy 2025

# Download multi-year panel
python data/usaspending/download_awards.py --fy 2020-2025

# Download GAO protest data
python data/usaspending/download_gao_protests.py
```

---

## GAO Bid Protest Statistics — FY2025

*Source: [GAO Annual Bid Protest Report to Congress for FY2025](https://www.gao.gov/products/gao-26-900695) (December 2025)*

| Metric | FY2025 | Trend |
|--------|--------|-------|
| Total cases filed | 1,688 | 6% decrease from FY2024 |
| Protests sustained | 53 | Lowest absolute number in 20+ years |
| Sustain rate | 14% | Consistent with recent years |
| Effectiveness rate | 52% | Over half of protestors received some relief |

**Top grounds for sustained protests:**
1. Unreasonable technical evaluations
2. Unreasonable cost/price evaluations
3. Unreasonable rejection of proposals

The dominance of technical evaluation errors as the primary sustain ground reinforces the argument that evaluation methodology and execution quality are critical determinants of procurement outcomes.

### Notable FY2025 Protest Decisions

**[The Mission Essential Group, LLC (B-422698.2)](https://www.gao.gov/products/b-422698.2) — January 8, 2025**
GAO sustained a pre-award protest challenging the Air Force's use of LPTA source selection for knowledge-based professional services in Europe and Africa. Key findings:
- The solicitation encouraged "unique approaches" and "deviations from staffing estimates" — incompatible with LPTA's premise
- The procurement was "predominantly for the acquisition of knowledge-based professional services," which DFARS says should "avoid, to the maximum extent practicable" LPTA
- GAO recommended the agency consider best-value tradeoff methodology

**[Enviremedial Services](https://www.governmentcontractslegalforum.com/2025/11/articles/bid-protest/august-2025-bid-protest-sustain-of-the-month-gao-sustains-protest-of-past-performance-evaluation-and-best-value-tradeoff-on-multiple-grounds/) — August 2025**
GAO sustained a protest reinforcing that agencies must consider the "relative merits" of offerors' past performance in best-value tradeoff analysis. Adjectival ratings serve only as "guides to intelligent decision-making" and cannot substitute for substantive qualitative analysis.

**[Procurement Integrity Decisions](https://www.governmentcontractslegalforum.com/2026/01/articles/bid-protest/december-2025-sustain-of-the-month-gao-leans-into-its-mandate-to-protect-the-integrity-of-the-procurement-process-in-two-decisions-rebuffing-agency-gamesmanship/) — December 2025**
Two decisions "rebuffing agency gamesmanship" — GAO stressed that agencies must provide adequate records for assessment of the reasonableness of their source selection actions.

---

## Regulatory Changes (2025)

### FAR Threshold Increases (Effective October 1, 2025)

| Threshold | Old | New |
|-----------|-----|-----|
| Simplified Acquisition Threshold | $250,000 | $350,000 |
| Micro-Purchase Threshold | $10,000 | $15,000 |

Higher thresholds mean more acquisitions can use simplified procedures, shifting the volume of procurements subject to formal Part 15 tradeoff analysis.

### FAR Overhaul (Executive Order 14275 — April 15, 2025)

The most comprehensive rewrite of federal procurement rules in 40+ years. The EO directs stripping the FAR back to statutory requirements and moving non-statutory guidance into Strategic Acquisition Guidance (SAG) "buying guides." Deviations have been issued for 38 FAR parts. See [Research Overview](/research/) for full analysis.
