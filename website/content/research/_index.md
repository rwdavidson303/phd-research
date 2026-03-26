---
title: "Research Design"
description: "Difference-in-differences analysis of NDAA Section 813 effects on federal procurement"
weight: 2
---

## From Lowest Price to Highest Public Value

An Empirical Test of Best-Value Source Selection in Government RFPs

### Abstract

Federal procurement policy affecting hundreds of billions annually has been shaped with minimal empirical evidence. This research exploits Section 813 of the National Defense Authorization Act for Fiscal Year 2017 — which restricted the Department of Defense's use of Lowest Price Technically Acceptable (LPTA) source selection — as a natural experiment. Using a difference-in-differences design applied to 654,307 competitively awarded service and IT contracts from the Omari et al. (2025) comprehensive FPDS dataset, we estimate the causal effect of LPTA restrictions on cost growth, contract modifications, competition, and single-bid rates.

### The Natural Experiment: NDAA Section 813

The LPTA restrictions rolled out across multiple legislative cycles, creating a staggered policy shock:

| Date | Event |
|------|-------|
| Dec 2016 | NDAA FY2017 enacted, Section 813 restricts DoD LPTA use |
| Dec 2017 | NDAA FY2018 reinforces restrictions (Section 822) |
| Aug 2018 | NDAA FY2019 extends restrictions government-wide (Section 880) |
| Oct 2019 | Final DFARS regulatory implementation |

Section 813 directed the Secretary of Defense to avoid, to the maximum extent practicable, using LPTA source selection when any of six criteria are present:

1. The contract requires the delivery of **knowledge-based professional services**
2. The contract requires the delivery of services that will be **performed by professional employees** with specific qualifications
3. The contract requires the delivery of services that require **specialized skill or expertise**
4. The contract will be awarded on the basis of **adequate price competition** from two or more responsible offerors
5. The requirement involves items that are **predominantly expendable** in nature, are nontechnical, or have a history of stable pricing
6. The solicitation requires offerors to provide solutions or approaches that are **difficult to compare** objectively

This policy change creates a natural experiment because it imposed binding constraints on DoD's choice of evaluation method for specific contract categories while leaving civilian agencies initially unaffected. The treatment is plausibly exogenous — driven by Congressional concern about contractor performance failures rather than by trends in the outcome variables themselves — enabling a credible difference-in-differences identification strategy.

### Research Questions

1. Does restricting LPTA reduce cost growth in affected contract categories?
2. Does the restriction reduce post-award contract modifications?
3. Does shifting to tradeoff evaluation affect the number of competing offerors?
4. How do transaction characteristics (complexity, size, pricing type) moderate the policy effect?

### Difference-in-Differences Design

The core identification strategy compares changes in outcomes between treated and control groups before and after the LPTA restriction took effect:

- **Treatment:** DoD contracts in restricted NAICS codes (51 = Information Technology, 54 = Professional Services)
- **Control 1:** DoD contracts in unrestricted NAICS codes (56 = Administrative Support Services)
- **Control 2:** Civilian agency contracts (not subject to Section 813)
- **Pre-period:** FY2017–2019 (before DFARS implementation)
- **Post-period:** FY2020–2023 (after regulatory implementation)

The estimating equation:

<div style="text-align: center; font-size: 1.1em; margin: 1.5em 0;">

Y<sub>it</sub> = β₀ + β₁(DoD<sub>i</sub>) + β₂(Post<sub>t</sub>) + β₃(DoD<sub>i</sub> × Post<sub>t</sub>) + γX<sub>it</sub> + ε<sub>it</sub>

</div>

Where **β₃** is the parameter of interest — the causal effect of LPTA restrictions on the outcome, net of common time trends and permanent group differences. **X** includes controls for log base award amount, NAICS fixed effects, fiscal year fixed effects, and pricing type fixed effects.

### Data: The Omari et al. (2025) FPDS Dataset

> Omari, S., Alansari, N., Libgober, B., & Kaufman, A. R. (2025). A comprehensive dataset of United States federal procurement, 1979–2023. *Scientific Data*, 12, Article 1368. [DOI: 10.1038/s41597-025-05714-1](https://doi.org/10.1038/s41597-025-05714-1)

This peer-reviewed dataset represents the most comprehensive publicly available record of federal contracting activity:

- **99 million rows** spanning 470 variables across FY1979–2023
- Published in *Scientific Data* (Nature) with open access via Figshare
- **Our analysis sample:** 654,307 competitively awarded service and IT contracts, FY2017–2023
- **Key variable:** `source_selection_process` — identifies LPTA, tradeoff, and other methods (available FY2020+)

### Outcome Variables

| Outcome | Measure | Description |
|---------|---------|-------------|
| Cost growth | Winsorized % | Percentage change from base award to current obligations, winsorized at 1st/99th percentiles |
| Modification count | Count | Number of post-award contract modifications |
| Single-bid | Binary (0/1) | Whether the contract received only one offer |
| Competition intensity | log(offers) | Natural log of the number of offers received |

### Identification Threats and Robustness

The primary threat to identification is a **parallel trends violation**: pre-treatment outcome trajectories for DoD and civilian contracts show convergence rather than parallel movement. We address this through five complementary robustness approaches:

1. **Trend-adjusted DiD** — includes group-specific linear time trends to account for differential pre-treatment trajectories
2. **Callaway & Sant'Anna (2021) estimator** — heterogeneity-robust estimator designed for staggered treatment adoption
3. **Goodman-Bacon (2021) decomposition** — decomposes the two-way fixed effects estimate into all constituent 2×2 DiD comparisons to diagnose problematic variation
4. **Inverse probability weighted DiD (IPW-DiD)** — reweights observations to improve covariate balance between treatment and control groups
5. **Temporal trimming** — restricts the sample to windows around the treatment date to reduce the influence of long-run divergent trends

Additional robustness checks include:

- **COVID-19 confound:** Excluding FY2020 to assess whether pandemic-era procurement disruptions drive results
- **Section 880 SUTVA concern:** The government-wide extension of LPTA restrictions in FY2019 potentially contaminates the civilian control group; we test sensitivity to alternative control group definitions

### Known Limitations

- **No pre-FY2020 source selection data:** The `source_selection_process` variable is only populated from FY2020 onward, so we cannot directly observe the first-stage policy effect (the shift from LPTA to tradeoff) in the pre-period
- **CPARS data legally inaccessible:** Contractor Performance Assessment Reporting System data would provide direct quality measures but is restricted to authorized government users
- **Cost growth includes planned options:** The cost growth measure captures all obligation changes including planned option exercises, not solely unplanned cost overruns
- **Parallel trends violation requires careful interpretation:** All causal estimates should be interpreted with the caveat that pre-treatment trends are not fully parallel

---

## Recent Policy Context

The procurement landscape has shifted dramatically since this research was designed. These developments provide both validation of the research thesis and important contextual factors.

### The FAR Overhaul (Executive Order 14275)

On **April 15, 2025**, President Trump signed [EO 14275](https://www.whitehouse.gov/briefings-statements/2025/04/white-house-announces-revolutionary-federal-procurement-overhaul/), "Restoring Common Sense to Federal Procurement," initiating the most comprehensive overhaul of the Federal Acquisition Regulation since its creation over 40 years ago. The EO directs stripping the FAR back to statutory requirements and moving non-statutory guidance into Strategic Acquisition Guidance (SAG) "buying guides." If source selection guidance moves out of the FAR, it could create more flexibility — or less uniformity — in how agencies implement best-value vs. LPTA decisions.

### FY 2026 NDAA: Statutory Shift from Lowest-Price to Best-Value

The **FY 2026 National Defense Authorization Act** (signed December 2025) contains provisions directly on point:

- **Section 812** amends the GSA Multiple Award Schedule Program definition of competitive procedures from those that "result in the **lowest overall cost** alternative" to those that "result in the **best value** to meet the needs of the United States" — a direct statutory codification of the shift this research studies.
- **Section 1801** directs the Secretary of Defense to issue guidance requiring resource decisions to "prioritize best value."
- **Section 1823** expands Commercial Solutions Openings (CSOs) beyond "innovative" commercial solutions to serve as a general commercial acquisition tool.

### DOGE and Federal Contracting Disruption

The Department of Government Efficiency (DOGE) was described as "[government contracting's biggest story of 2025](https://www.washingtontechnology.com/opinion/2025/12/doge-was-government-contractings-biggest-story-2025-and-its-not-close/410372/)." Contract reviews, pauses, and cancellations created significant uncertainty government-wide — a natural experiment in rapid, top-down procurement reform outside the traditional FAR rulemaking process.

### AI in Federal Procurement

**OMB Memorandum M-25-22** (effective for solicitations after September 30, 2025) imposes guardrails on AI procurement and urges agencies to maximize use of domestically developed AI. AI procurement is inherently ill-suited for LPTA given its complexity and risk — favoring best-value approaches.
