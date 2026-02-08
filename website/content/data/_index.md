---
title: "Federal Procurement Data"
description: "USAspending, FPDS, GAO protest data, and analysis"
weight: 3
---

## Federal Procurement Data Hub

This section tracks and analyzes federal procurement data relevant to the dissertation.

### Data Sources

| Source | Description | Update Frequency |
|--------|-------------|-----------------|
| [USAspending.gov](https://www.usaspending.gov) | Contract award records with source selection process codes | Automated downloads |
| [FPDS](https://www.fpds.gov) | Federal Procurement Data System - detailed contract data | Linked via USAspending |
| [GAO Bid Protests](https://www.gao.gov/legal/bid-protests) | Annual protest statistics and decision dockets | Annual + ongoing |
| CPARS | Contractor Performance Assessment Reporting System | Access pending |

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
