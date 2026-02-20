# Appendices

---

## Appendix A: Variable Codebook

This appendix provides a complete codebook for all variables used in the empirical analysis. Each entry specifies the variable name as coded in the analytic dataset, the corresponding FPDS/USAspending field name(s), a definition, the measurement type, and the data source.

### A.1 Independent Variable

| Variable Name | FPDS/USAspending Field | Definition | Measurement Type | Source |
|:---|:---|:---|:---|:---|
| `tradeoff` | `solicitation_procedures` (mapped from `source_selection_process`) | Binary indicator for best-value tradeoff source selection. Coded 1 if the contract was awarded using tradeoff evaluation (TO); coded 0 if the contract was awarded using lowest-price technically acceptable (LPTA) evaluation. | Binary (0/1) | FPDS-NG via USAspending.gov |

### A.2 Procurement Design Classification

The `procurement_design` variable is a composite classification constructed from two FPDS fields: `solicitation_procedures` and `type_of_contract_pricing`. This variable captures the joint distribution of how the government selected the contractor and how the contract prices performance, providing a more granular characterization of the procurement approach than either field alone.

| Variable Name | FPDS/USAspending Fields | Definition | Measurement Type | Source |
|:---|:---|:---|:---|:---|
| `procurement_design` | `solicitation_procedures` + `type_of_contract_pricing` | Composite classification of procurement approach based on solicitation procedure and contract pricing type. See classification rules below. | Categorical (5 levels) | FPDS-NG via USAspending.gov |

**Classification Rules for `procurement_design`:**

| Category | Label | Solicitation Procedures Code | Contract Pricing Type | Description |
|:---|:---|:---|:---|:---|
| 1 | `QUALITY_EVALUATING` | NP (Negotiated Proposal) | Cost-type pricing (cost-plus-fixed-fee, cost-plus-incentive-fee, cost-plus-award-fee, cost-no-fee) | Negotiated procurements using cost-reimbursement contracts. These represent the highest-discretion acquisitions, where the government evaluates both technical approach and cost/pricing methodology, and the contractor shares cost risk with the government. Typically used for R&D, complex IT development, and high-uncertainty professional services. |
| 2 | `NEGOTIATED_FFP` | NP (Negotiated Proposal) | Firm-fixed-price (J) or Fixed-price with economic price adjustment (A) | Negotiated procurements using firm-fixed-price contracts. The government evaluates proposals on price and non-price factors, but the contractor bears full cost risk. Common for well-defined professional services and IT support. |
| 3 | `TASK_ORDER` | SMA (Subject to Multiple Award) or SSS (Set Aside Sources Sought) | Any pricing type | Task orders issued under multiple-award indefinite-delivery/indefinite-quantity (IDIQ) contracts or orders set aside under pre-competed vehicles. Competition at the task-order level may differ from competition at the parent contract level. |
| 4 | `PRICE_FOCUSED` | SB (Sealed Bidding) or SAP (Simplified Acquisition Procedures) | Firm-fixed-price (J) or Fixed-price with economic price adjustment (A) | Procurements conducted through sealed bidding or simplified procedures with firm-fixed-price contracts. Award is determined primarily or exclusively by price. Represents the lowest-discretion procurement approach. |
| 5 | `OTHER` | All other combinations | All other combinations | Residual category for procurement approaches that do not fit the four primary classifications. Includes unusual combinations of solicitation procedures and pricing types, as well as records with missing or ambiguous coding. Excluded from primary analyses; included in sensitivity checks. |

### A.3 Dependent Variables

| Variable Name | FPDS/USAspending Field(s) | Definition | Measurement Type | Source |
|:---|:---|:---|:---|:---|
| `cost_growth` | `base_and_all_options_value` (current), `base_exercised_options_value` (initial) | Ratio of the change in contract value to the initial base value: (current_total_value - base_exercised_options_value) / base_exercised_options_value. A value of 0.0 indicates no cost growth; a value of 0.25 indicates 25% growth. | Continuous | FPDS-NG via USAspending.gov |
| `cost_growth_w` | Derived from `cost_growth` | Winsorized cost growth. The `cost_growth` variable is winsorized at the 1st and 99th percentiles of the sample distribution. Values below the 1st percentile are set to the 1st percentile value; values above the 99th percentile are set to the 99th percentile value. This transformation reduces the influence of extreme outliers on regression estimates while preserving the rank order and relative magnitude of observations. | Continuous (winsorized) | Derived |
| `transaction_count` | Count of records per `award_id_piid` | Count of unique transaction records (contract actions) associated with each award. Includes the initial award action and all subsequent modifications, funding actions, option exercises, and administrative changes. Serves as a proxy for post-award administrative burden and contract instability. | Count (non-negative integer) | FPDS-NG via USAspending.gov |
| `mod_count` | Count of records with `modification_number` > 0 per `award_id_piid` | Count of contract modifications (excluding the initial award action). Differs from `transaction_count` by excluding the base award record. | Count (non-negative integer) | FPDS-NG via USAspending.gov |
| `number_of_offers_received` | `number_of_offers_received` | Number of proposals or bids submitted by offerors in response to the solicitation. Self-reported by the contracting officer at the time of award. Serves as the primary measure of competition intensity. | Count (positive integer) | FPDS-NG via USAspending.gov |
| `single_bid` | Derived from `number_of_offers_received` | Binary indicator equal to 1 if `number_of_offers_received` = 1 (only one offer was submitted); equal to 0 if two or more offers were received. Identifies procurements that failed to generate effective competition despite being formally competitive. | Binary (0/1) | Derived |

### A.4 Control Variables

| Variable Name | FPDS/USAspending Field(s) | Definition | Measurement Type | Source |
|:---|:---|:---|:---|:---|
| `log_award_amount` | `base_exercised_options_value` (initial action) | Natural logarithm of the initial base award value (federal action obligation at the time of the initial award). Controls for contract size, which is correlated with both source selection method and outcomes. The log transformation addresses the severe right skew of contract dollar values. | Continuous | Derived from FPDS-NG |
| `award_amount` | `base_exercised_options_value` (initial action) | Initial base award value in dollars. Used for descriptive statistics and as the untransformed analog of `log_award_amount`. | Continuous (dollars) | FPDS-NG via USAspending.gov |
| `contract_type` | `type_of_contract_pricing` | Categorical classification of the contract pricing arrangement. Grouped into four categories: FFP (firm-fixed-price, codes J and A), CPFF (cost-plus-fixed-fee, code T), T&M (time-and-materials, code Z, and labor-hour, code 1), and Other (all remaining pricing types including cost-plus-incentive-fee, cost-plus-award-fee, fixed-price-incentive, and fixed-price-level-of-effort). | Categorical (4 levels) | FPDS-NG via USAspending.gov |
| `naics_sector` | `naics_code` | Categorical classification based on the 3-digit NAICS code prefix. Four categories: IT Services (NAICS 518xxx and 511xxx), Consulting (NAICS 5416xx and 5417xx), Other Professional (remaining NAICS 541xxx), Administrative Support (NAICS 561xxx). | Categorical (4 levels) | Derived from FPDS-NG |
| `naics_code` | `naics_code` | Full 6-digit North American Industry Classification System code identifying the product or service category of the contract. Used in fixed effects specifications and as a granular complexity proxy. | Categorical | FPDS-NG via USAspending.gov |
| `psc_code` | `product_or_service_code` | Product or Service Code identifying the type of supply or service. Used as an alternative classification to NAICS for robustness checks. | Categorical | FPDS-NG via USAspending.gov |
| `idv_indicator` | `idv_type`, `award_id_parent_award_piid` | Binary indicator equal to 1 if the award is a task order or delivery order issued under an indefinite-delivery vehicle (IDIQ, GWAC, BPA, or BOA); equal to 0 if the award is a standalone (definitive) contract. Determined by the presence of a non-null `award_id_parent_award_piid` or a non-null `idv_type` field. | Binary (0/1) | Derived from FPDS-NG |
| `agency_code` | `awarding_agency_code` | Numeric code identifying the federal agency that awarded the contract. Used to construct agency fixed effects that absorb time-invariant agency-specific factors (culture, workforce quality, mission complexity, risk tolerance). | Categorical | FPDS-NG via USAspending.gov |
| `agency_name` | `awarding_agency_name` | Name of the awarding agency. Used for labeling and descriptive reporting. | Text | FPDS-NG via USAspending.gov |
| `sub_agency_code` | `awarding_sub_agency_code` | Numeric code identifying the sub-agency or bureau that awarded the contract. Used for more granular fixed effects in robustness checks. | Categorical | FPDS-NG via USAspending.gov |
| `fiscal_year` | Derived from `action_date` | Federal fiscal year of the initial award action. Federal fiscal years run from October 1 through September 30 (e.g., FY2024 runs from October 1, 2023, through September 30, 2024). Used to construct fiscal year fixed effects. | Categorical (ordinal) | Derived from FPDS-NG |
| `set_aside_type` | `type_of_set_aside` | Categorical classification of the socioeconomic set-aside status of the procurement. Categories: Unrestricted (no set-aside), Small Business (general SB set-aside), 8(a) (8(a) Business Development Program), HUBZone (Historically Underutilized Business Zone), SDVOSB (Service-Disabled Veteran-Owned Small Business), WOSB (Women-Owned Small Business), Other (all remaining set-aside types). | Categorical (7 levels) | FPDS-NG via USAspending.gov |
| `contract_duration_months` | `period_of_performance_start_date`, `period_of_performance_current_end_date` | Duration of the contract period of performance in months, calculated as the difference between the current period of performance end date and the period of performance start date. Used as an exposure offset in negative binomial models for modification count and as a control variable in OLS models. | Continuous (months) | Derived from FPDS-NG |
| `dod_indicator` | `awarding_agency_code` | Binary indicator equal to 1 if the awarding agency is a Department of Defense component (Army, Navy, Air Force, or other defense agency); equal to 0 for civilian agencies. Used in subsample analyses comparing DoD and civilian procurement. | Binary (0/1) | Derived from FPDS-NG |

### A.5 Moderating Variables

| Variable Name | FPDS/USAspending Field(s) | Definition | Measurement Type | Source |
|:---|:---|:---|:---|:---|
| `complexity_proxy` | Derived from `naics_sector` and `contract_type` | Ordinal measure of procurement complexity. Constructed by crossing NAICS sector with contract type: IT Services + cost-type = highest complexity; Administrative Support + FFP = lowest complexity. Used to test interaction effects with source selection method. | Ordinal (3 levels: low, medium, high) | Derived |
| `agency_procurement_volume` | Aggregated from `federal_action_obligation` | Total dollar value of the agency's annual competitive procurement obligations in the study NAICS sectors. Serves as a proxy for agency procurement capacity and expertise. Agencies with higher procurement volume are expected to have more experienced acquisition workforces. | Continuous (dollars, logged) | Derived from FPDS-NG |

### A.6 Propensity Score and Matching Variables

| Variable Name | Definition | Measurement Type | Source |
|:---|:---|:---|:---|
| `pscore` | Estimated propensity score: the predicted probability of receiving tradeoff source selection, conditional on observed covariates. Estimated via logistic regression with covariates: `log_award_amount`, `naics_sector`, `agency_code`, `fiscal_year`, `contract_type`, `idv_indicator`, `set_aside_type`. | Continuous (0, 1) | Derived |
| `pscore_logit` | Logit transformation of the propensity score: ln(pscore / (1 - pscore)). Used for caliper matching on the logit scale. | Continuous | Derived |
| `matched` | Binary indicator equal to 1 if the observation is included in the propensity-score-matched sample; equal to 0 if excluded due to lack of a suitable match within the caliper. | Binary (0/1) | Derived |
| `match_id` | Identifier linking each treated (tradeoff) observation to its matched control (LPTA) observation in the nearest-neighbor matched sample. | Integer | Derived |

---

## Appendix B: Full Regression Tables

This appendix reproduces all regression output with complete coefficient estimates, standard errors, confidence intervals, and model diagnostics. Tables are organized by dependent variable.

*Note: Tables in this appendix will be populated with results from the empirical analysis. The structure and specifications are presented below; coefficient estimates, standard errors, and diagnostics will be inserted upon completion of the data analysis.*

### Table B.1: Cost Growth (OLS with Agency and Fiscal Year Fixed Effects)

**Dependent Variable:** `cost_growth_w` (winsorized at 1st/99th percentile)

| Variable | Coefficient | Robust SE | 95% CI Lower | 95% CI Upper | *p*-value |
|:---|:---:|:---:|:---:|:---:|:---:|
| Tradeoff (1 = TO, 0 = LPTA) | -- | -- | -- | -- | -- |
| Log(Award Amount) | -- | -- | -- | -- | -- |
| Contract Type: CPFF (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: T&M (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: Other (ref: FFP) | -- | -- | -- | -- | -- |
| IDV Indicator | -- | -- | -- | -- | -- |
| Set-Aside: Small Business (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: 8(a) (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: HUBZone (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: SDVOSB (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: WOSB (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: Other (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Agency Fixed Effects | Included | | | | |
| Fiscal Year Fixed Effects | Included | | | | |
| Constant | -- | -- | -- | -- | -- |
| *N* | -- | | | | |
| *R*-squared | -- | | | | |
| Adjusted *R*-squared | -- | | | | |
| *F*-statistic | -- | | | | |
| RMSE | -- | | | | |

*Standard errors clustered at the agency-NAICS level.*

### Table B.2: Cost Growth (OLS on PSM-Matched Sample)

**Dependent Variable:** `cost_growth_w` (winsorized at 1st/99th percentile)

*Specification: Same covariates as Table B.1, estimated on the propensity-score-matched sample. ATT is the primary estimand.*

| Variable | ATT Estimate | Robust SE | 95% CI Lower | 95% CI Upper | *p*-value |
|:---|:---:|:---:|:---:|:---:|:---:|
| Tradeoff (ATT) | -- | -- | -- | -- | -- |
| *N* (matched pairs) | -- | | | | |
| Caliper | 0.2 SD | | | | |
| Matching ratio | 1:1 | | | | |

### Table B.3: Modification Intensity (Negative Binomial Regression)

**Dependent Variable:** `mod_count` (count of post-award modifications)

**Exposure Offset:** `contract_duration_months`

| Variable | Coefficient | SE | IRR | 95% CI (IRR) | *p*-value |
|:---|:---:|:---:|:---:|:---:|:---:|
| Tradeoff (1 = TO, 0 = LPTA) | -- | -- | -- | -- | -- |
| Log(Award Amount) | -- | -- | -- | -- | -- |
| Contract Type: CPFF (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: T&M (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: Other (ref: FFP) | -- | -- | -- | -- | -- |
| IDV Indicator | -- | -- | -- | -- | -- |
| Set-Aside: Small Business (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: 8(a) (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: HUBZone (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: SDVOSB (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: WOSB (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Set-Aside: Other (ref: Unrestricted) | -- | -- | -- | -- | -- |
| Agency Fixed Effects | Included | | | | |
| Fiscal Year Fixed Effects | Included | | | | |
| Constant | -- | -- | -- | -- | -- |
| *N* | -- | | | | |
| Log-likelihood | -- | | | | |
| Overdispersion (alpha) | -- | | | | |
| LR test vs. Poisson (*p*) | -- | | | | |
| AIC | -- | | | | |
| BIC | -- | | | | |

*IRR = Incidence Rate Ratio. Standard errors clustered at the agency-NAICS level.*

### Table B.4: Competition Intensity (Negative Binomial Regression)

**Dependent Variable:** `number_of_offers_received`

| Variable | Coefficient | SE | IRR | 95% CI (IRR) | *p*-value |
|:---|:---:|:---:|:---:|:---:|:---:|
| Tradeoff (1 = TO, 0 = LPTA) | -- | -- | -- | -- | -- |
| Log(Award Amount) | -- | -- | -- | -- | -- |
| Contract Type: CPFF (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: T&M (ref: FFP) | -- | -- | -- | -- | -- |
| Contract Type: Other (ref: FFP) | -- | -- | -- | -- | -- |
| IDV Indicator | -- | -- | -- | -- | -- |
| Set-Aside controls | Included | | | | |
| Agency Fixed Effects | Included | | | | |
| Fiscal Year Fixed Effects | Included | | | | |
| Constant | -- | -- | -- | -- | -- |
| *N* | -- | | | | |
| Log-likelihood | -- | | | | |
| Overdispersion (alpha) | -- | | | | |
| AIC | -- | | | | |

### Table B.5: Single-Bid Outcome (Logistic Regression)

**Dependent Variable:** `single_bid` (1 = one offer received; 0 = multiple offers)

| Variable | Coefficient | SE | OR | 95% CI (OR) | *p*-value | AME |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Tradeoff (1 = TO, 0 = LPTA) | -- | -- | -- | -- | -- | -- |
| Log(Award Amount) | -- | -- | -- | -- | -- | -- |
| Contract Type: CPFF (ref: FFP) | -- | -- | -- | -- | -- | -- |
| Contract Type: T&M (ref: FFP) | -- | -- | -- | -- | -- | -- |
| Contract Type: Other (ref: FFP) | -- | -- | -- | -- | -- | -- |
| IDV Indicator | -- | -- | -- | -- | -- | -- |
| Set-Aside controls | Included | | | | | |
| Agency Fixed Effects | Included | | | | | |
| Fiscal Year Fixed Effects | Included | | | | | |
| Constant | -- | -- | -- | -- | -- | |
| *N* | -- | | | | | |
| Pseudo *R*-squared | -- | | | | | |
| Log-likelihood | -- | | | | | |
| AIC | -- | | | | | |
| Hosmer-Lemeshow *p* | -- | | | | | |

*OR = Odds Ratio. AME = Average Marginal Effect.*

### Table B.6: Moderation --- Tradeoff x NAICS Sector Interaction (Cost Growth)

**Dependent Variable:** `cost_growth_w`

| Variable | Coefficient | Robust SE | *p*-value |
|:---|:---:|:---:|:---:|
| Tradeoff | -- | -- | -- |
| NAICS: IT Services (ref: Admin Support) | -- | -- | -- |
| NAICS: Consulting (ref: Admin Support) | -- | -- | -- |
| NAICS: Other Professional (ref: Admin Support) | -- | -- | -- |
| Tradeoff x IT Services | -- | -- | -- |
| Tradeoff x Consulting | -- | -- | -- |
| Tradeoff x Other Professional | -- | -- | -- |
| Controls | Included | | |
| Agency and Year FE | Included | | |
| *N* | -- | | |
| *R*-squared | -- | | |
| Wald test: joint significance of interactions (*p*) | -- | | |

### Table B.7: Moderation --- Tradeoff x Contract Type Interaction (Cost Growth)

**Dependent Variable:** `cost_growth_w`

| Variable | Coefficient | Robust SE | *p*-value |
|:---|:---:|:---:|:---:|
| Tradeoff | -- | -- | -- |
| Contract Type: CPFF (ref: FFP) | -- | -- | -- |
| Contract Type: T&M (ref: FFP) | -- | -- | -- |
| Tradeoff x CPFF | -- | -- | -- |
| Tradeoff x T&M | -- | -- | -- |
| Controls | Included | | |
| Agency and Year FE | Included | | |
| *N* | -- | | |
| *R*-squared | -- | | |
| Wald test: joint significance of interactions (*p*) | -- | | |

### Table B.8: Difference-in-Differences Estimates

**Dependent Variable:** `cost_growth_w`

| Variable | Coefficient | Robust SE | *p*-value |
|:---|:---:|:---:|:---:|
| Post x Treat (DiD estimand) | -- | -- | -- |
| Post | -- | -- | -- |
| Treat | -- | -- | -- |
| Controls | Included | | |
| Agency-Category FE | Included | | |
| Fiscal Year FE | Included | | |
| *N* | -- | | |
| *R*-squared | -- | | |
| Pre-trend test (*p*) | -- | | |

---

## Appendix C: Propensity Score Balance Diagnostics

This appendix reports diagnostics for the propensity score matching procedure described in Chapter 3, Section 3.5.3. Balance diagnostics assess whether the matching procedure successfully equalized the distribution of observed covariates between the treated (tradeoff) and control (LPTA) groups, which is a necessary condition for the validity of the propensity score matching estimator.

### C.1 Balance Table

*Note: Values will be populated upon completion of the propensity score estimation and matching procedure.*

| Covariate | Mean (Tradeoff) Before | Mean (LPTA) Before | SMD Before | Mean (Tradeoff) After | Mean (LPTA) After | SMD After | Variance Ratio (After) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Log(Award Amount) | -- | -- | -- | -- | -- | -- | -- |
| FFP (proportion) | -- | -- | -- | -- | -- | -- | -- |
| CPFF (proportion) | -- | -- | -- | -- | -- | -- | -- |
| T&M (proportion) | -- | -- | -- | -- | -- | -- | -- |
| IDV Indicator (proportion) | -- | -- | -- | -- | -- | -- | -- |
| NAICS: IT Services (proportion) | -- | -- | -- | -- | -- | -- | -- |
| NAICS: Consulting (proportion) | -- | -- | -- | -- | -- | -- | -- |
| NAICS: Other Professional (proportion) | -- | -- | -- | -- | -- | -- | -- |
| NAICS: Admin Support (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: Unrestricted (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: Small Business (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: 8(a) (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: HUBZone (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: SDVOSB (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Set-Aside: WOSB (proportion) | -- | -- | -- | -- | -- | -- | -- |
| DoD (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2020 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2021 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2022 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2023 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2024 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| FY2025 (proportion) | -- | -- | -- | -- | -- | -- | -- |
| Contract Duration (months) | -- | -- | -- | -- | -- | -- | -- |

### C.2 Interpretation Guide

**Standardized Mean Difference (SMD):** The difference in means between treatment and control groups, divided by the pooled standard deviation. Following the thresholds established by Rosenbaum and Rubin (1985) and widely adopted in the causal inference literature:

- SMD < 0.10: Acceptable balance (negligible imbalance)
- SMD 0.10--0.25: Marginal balance (potential concern; sensitivity analysis warranted)
- SMD > 0.25: Unacceptable balance (re-specification of propensity score model required)

**Variance Ratio:** The ratio of the variance in the treatment group to the variance in the control group, computed for continuous covariates. Following Rubin (2001):

- Variance ratio between 0.50 and 2.00: Acceptable
- Variance ratio outside this range: Indicates remaining distributional imbalance

### C.3 Love Plot

*[Figure C.1: Love plot (dot plot of standardized mean differences before and after matching for all covariates) will be inserted upon completion of the analysis.]*

The love plot displays the absolute standardized mean difference for each covariate, with open circles indicating the before-matching value and filled circles indicating the after-matching value. The vertical dashed line at SMD = 0.10 marks the conventional threshold for acceptable balance. Successful matching is indicated by all filled circles falling to the left of the threshold line.

### C.4 Propensity Score Distribution

*[Figure C.2: Histograms and/or kernel density plots of the propensity score distribution in the tradeoff and LPTA groups, before and after matching, will be inserted upon completion of the analysis.]*

The propensity score distribution plots illustrate the region of common support---the range of propensity scores where both treated and control observations exist. Observations outside the region of common support are excluded from the matched sample. The overlap of the distributions after matching should be substantially improved relative to the unmatched distributions.

### C.5 Sensitivity Analysis: Rosenbaum Bounds

| Outcome Variable | Critical Gamma | Interpretation |
|:---|:---:|:---|
| `cost_growth_w` | -- | An unobserved confounder would need to change the odds of tradeoff assignment by a factor of [Gamma] to explain away the estimated treatment effect. |
| `mod_count` | -- | [Same interpretation] |
| `number_of_offers_received` | -- | [Same interpretation] |
| `single_bid` | -- | [Same interpretation] |

**Interpretation of Critical Gamma:** Gamma = 1.0 indicates no hidden bias. Gamma = 2.0 means an unmeasured confounder would need to double the odds of receiving the treatment to explain the result. Values above 2.0 are generally considered robust to hidden bias in the social sciences.

---

## Appendix D: Robustness Check Results

This appendix presents the complete results of the robustness and sensitivity analyses described in Chapter 3, Section 3.8. Each table reports the coefficient on the tradeoff indicator (or the relevant treatment effect estimate) under alternative specifications, alongside the primary specification for comparison.

*Note: All coefficient estimates, standard errors, and diagnostics will be populated upon completion of the data analysis.*

### Table D.1: Sensitivity to Cost Growth Operationalization

| Specification | Tradeoff Coefficient | SE | *p*-value | *N* |
|:---|:---:|:---:|:---:|:---:|
| **Primary: base_and_all_options cost growth, winsorized 1/99** | -- | -- | -- | -- |
| Alternative 1: total_dollars_obligated cost growth, winsorized 1/99 | -- | -- | -- | -- |
| Alternative 2: base_and_all_options cost growth, winsorized 5/95 | -- | -- | -- | -- |
| Alternative 3: base_and_all_options cost growth, winsorized 0.5/99.5 | -- | -- | -- | -- |
| Alternative 4: Trimmed (extreme 2% dropped) | -- | -- | -- | -- |
| Alternative 5: Binary (cost growth > 10%) | -- | -- | -- | -- |
| Alternative 6: Binary (cost growth > 20%) | -- | -- | -- | -- |

### Table D.2: Sensitivity to Competition Intensity Operationalization

| Specification | Tradeoff Coefficient | SE | *p*-value | *N* |
|:---|:---:|:---:|:---:|:---:|
| **Primary: Negative binomial, raw count** | -- | -- | -- | -- |
| Alternative 1: OLS, ln(offers + 1) | -- | -- | -- | -- |
| Alternative 2: Ordered logit (1, 2--3, 4--5, 6+) | -- | -- | -- | -- |
| Alternative 3: Binary (3+ offers = robust competition) | -- | -- | -- | -- |

### Table D.3: Sensitivity to Matching Specification

| Matching Method | ATT (Cost Growth) | SE | *p* | Matched Pairs |
|:---|:---:|:---:|:---:|:---:|
| **Primary: 1:1 NN, caliper = 0.2 SD, no replacement** | -- | -- | -- | -- |
| Alternative 1: 1:3 NN, caliper = 0.2 SD | -- | -- | -- | -- |
| Alternative 2: 1:5 NN, caliper = 0.2 SD | -- | -- | -- | -- |
| Alternative 3: 1:1 NN, with replacement | -- | -- | -- | -- |
| Alternative 4: Kernel matching | -- | -- | -- | -- |
| Alternative 5: Mahalanobis distance matching | -- | -- | -- | -- |
| Alternative 6: 1:1 NN, caliper = 0.1 SD | -- | -- | -- | -- |
| Alternative 7: 1:1 NN, caliper = 0.5 SD | -- | -- | -- | -- |

### Table D.4: Sensitivity to Fixed Effects Specification

| Fixed Effects | Tradeoff (Cost Growth) | SE | *p* | *R*-sq |
|:---|:---:|:---:|:---:|:---:|
| **Primary: Agency + FY** | -- | -- | -- | -- |
| Alternative 1: Agency x FY | -- | -- | -- | -- |
| Alternative 2: Agency + NAICS (4-digit) + FY | -- | -- | -- | -- |
| Alternative 3: Agency x NAICS (3-digit) | -- | -- | -- | -- |
| Alternative 4: Sub-Agency + FY | -- | -- | -- | -- |

### Table D.5: Sensitivity to Standard Error Clustering

| Clustering Level | Tradeoff (Cost Growth) | SE | *p* |
|:---|:---:|:---:|:---:|
| **Primary: Agency-NAICS** | -- | -- | -- |
| Alternative 1: Agency only | -- | -- | -- |
| Alternative 2: NAICS only | -- | -- | -- |
| Alternative 3: Two-way (Agency + FY) | -- | -- | -- |
| Alternative 4: HC3 (heteroskedasticity-consistent) | -- | -- | -- |

### Table D.6: Placebo Tests

| Placebo Specification | Tradeoff Coefficient | SE | *p*-value | *N* |
|:---|:---:|:---:|:---:|:---:|
| Commodity supply contracts (NAICS 31--33) | -- | -- | -- | -- |
| Pre-treatment period (DiD, pre-policy years only) | -- | -- | -- | -- |

### Table D.7: Subsample Replication

| Subsample | Tradeoff (Cost Growth) | SE | *p* | *N* |
|:---|:---:|:---:|:---:|:---:|
| **Full sample** | -- | -- | -- | -- |
| DoD only | -- | -- | -- | -- |
| Civilian agencies only | -- | -- | -- | -- |
| IT Services (NAICS 511/518) only | -- | -- | -- | -- |
| Consulting (NAICS 5416/5417) only | -- | -- | -- | -- |
| Large contracts (above median value) | -- | -- | -- | -- |
| Small contracts (below median value) | -- | -- | -- | -- |
| FY2020--FY2022 | -- | -- | -- | -- |
| FY2023--FY2025 | -- | -- | -- | -- |

### Table D.8: Quantile Regression Results (Cost Growth)

| Quantile | Tradeoff Coefficient | SE | *p*-value |
|:---|:---:|:---:|:---:|
| 25th percentile | -- | -- | -- |
| 50th percentile (median) | -- | -- | -- |
| 75th percentile | -- | -- | -- |

### Table D.9: High-Leverage Observation Analysis

| Specification | Tradeoff (Cost Growth) | SE | *p* | *N* |
|:---|:---:|:---:|:---:|:---:|
| **Full sample** | -- | -- | -- | -- |
| Excluding Cook's D > 4/N | -- | -- | -- | -- |

### Table D.10: Cross-Strategy Comparison Summary

| Identification Strategy | Tradeoff Effect (Cost Growth) | SE | *p* | Sign Consistent? |
|:---|:---:|:---:|:---:|:---:|
| Full-sample OLS with FE | -- | -- | -- | -- |
| PSM (1:1 NN) | -- | -- | -- | -- |
| DiD | -- | -- | -- | -- |
| Multi-level model | -- | -- | -- | -- |

---

## Appendix E: Acronym List

| Acronym | Full Term |
|:---|:---|
| ADB | Asian Development Bank |
| APA | American Psychological Association |
| ATE | Average Treatment Effect |
| ATT | Average Treatment Effect on the Treated |
| BPA | Blanket Purchase Agreement |
| BOA | Basic Ordering Agreement |
| CICA | Competition in Contracting Act |
| COFC | Court of Federal Claims |
| COTR | Contracting Officer's Technical Representative |
| CPARS | Contractor Performance Assessment Reporting System |
| CPFF | Cost-Plus-Fixed-Fee |
| CRS | Congressional Research Service |
| CSV | Comma-Separated Values |
| DATA Act | Digital Accountability and Transparency Act |
| DAU | Defense Acquisition University |
| DCAA | Defense Contract Audit Agency |
| DFARS | Defense Federal Acquisition Regulation Supplement |
| DiD | Difference-in-Differences |
| DoD | Department of Defense |
| DPC | Data Procedures Committee |
| DPAP | Defense Procurement and Acquisition Policy |
| EBRD | European Bank for Reconstruction and Development |
| ETL | Extract, Transform, Load |
| FAR | Federal Acquisition Regulation |
| FARA | Federal Acquisition Reform Act |
| FASA | Federal Acquisition Streamlining Act |
| FDR | False Discovery Rate |
| FFATA | Federal Funding Accountability and Transparency Act |
| FFP | Firm-Fixed-Price |
| FOIA | Freedom of Information Act |
| FPDS | Federal Procurement Data System |
| FPDS-NG | Federal Procurement Data System--Next Generation |
| FY | Fiscal Year |
| GAO | Government Accountability Office |
| GLM | Generalized Linear Model |
| GWAC | Government-Wide Acquisition Contract |
| HC3 | Heteroskedasticity-Consistent (type 3) standard errors |
| HHS | Department of Health and Human Services |
| HUBZone | Historically Underutilized Business Zone |
| IDIQ | Indefinite-Delivery/Indefinite-Quantity |
| IDV | Indefinite Delivery Vehicle |
| IPV | Independent Private Values |
| IRB | Institutional Review Board |
| IRR | Incidence Rate Ratio |
| IT | Information Technology |
| LPTA | Lowest Price Technically Acceptable |
| LR | Likelihood Ratio |
| MEAT | Most Economically Advantageous Tender |
| NAICS | North American Industry Classification System |
| NB | Negative Binomial |
| NDAA | National Defense Authorization Act |
| NDIA | National Defense Industrial Association |
| NFP | Negotiated Fixed Price |
| NIGP | National Institute of Governmental Purchasing |
| NASPO | National Association of State Procurement Officials |
| OLS | Ordinary Least Squares |
| OECD | Organisation for Economic Co-operation and Development |
| OR | Odds Ratio |
| PALT | Procurement Administrative Lead Time |
| PII | Personally Identifiable Information |
| PPIRS | Past Performance Information Retrieval System |
| PSC | Product or Service Code |
| PSM | Propensity Score Matching |
| QE | Quasi-Experimental |
| R&D | Research and Development |
| RFP | Request for Proposals |
| RMSE | Root Mean Square Error |
| SAT | Simplified Acquisition Threshold |
| SB | Sealed Bidding |
| SD | Standard Deviation |
| SDVOSB | Service-Disabled Veteran-Owned Small Business |
| SE | Standard Error |
| SMD | Standardized Mean Difference |
| SSA | Source Selection Authority |
| TCE | Transaction Cost Economics |
| T&M | Time and Materials |
| TO | Tradeoff (source selection process code) |
| TWFE | Two-Way Fixed Effects |
| UEI | Unique Entity Identifier |
| VfM | Value for Money |
| WOSB | Women-Owned Small Business |

---

## Appendix F: Data Processing Pipeline Description

This appendix describes the extract-transform-load (ETL) pipeline used to convert raw USAspending.gov bulk download files into the analysis-ready dataset used in the empirical analysis. The pipeline is implemented in Python and is designed for reproducibility, with all processing steps documented in version-controlled scripts.

### F.1 Extract Phase

**Source:** USAspending.gov Custom Award Data Download (bulk CSV files)

**Download Parameters:**
- Award types: Contracts and IDVs
- Fiscal years: FY2020 through FY2025
- Agencies: All executive branch agencies
- File format: Comma-separated values (CSV)
- Granularity: Transaction-level (one row per contract action)

**Process:**
1. Bulk download files are retrieved using the `download_awards.py` script located at `data/usaspending/download_awards.py`. The script automates requests to the USAspending.gov Custom Award Data Download API, specifying fiscal year and agency parameters.
2. Each fiscal year generates one or more CSV files, each containing up to 500,000 records. Files are stored in the `data/usaspending/raw/` directory, organized by fiscal year.
3. Supplementary data pulls using the USAspending.gov RESTful API are executed for specific data elements not included in the standard bulk download format (e.g., detailed subaward data, if used in sensitivity analyses).
4. GAO bid protest statistics are collected manually from the annual reports posted on gao.gov and stored in `data/gao/protest_statistics.csv`.

**Data Volume:** Approximately 2--5 million transaction records per fiscal year across all agencies and award types, prior to filtering. The study's NAICS sector restrictions and competition filters reduce the working dataset to approximately 500,000--1,000,000 relevant transactions, which aggregate to approximately 80,000--150,000 unique contract awards.

### F.2 Transform Phase

The transformation pipeline is organized into sequential stages, each implemented as a Python function within the analysis scripts. All transformations are logged and auditable.

**Stage 1: Deduplication and Quality Checks**
- Remove exact duplicate records (identical across all fields), which may arise from overlapping bulk download batches.
- Flag and investigate records with internally inconsistent data (e.g., award dates that precede solicitation dates, negative dollar values, non-numeric entries in numeric fields).
- Validate the `source_selection_process` field: identify records with null, blank, or unexpected values. Records with null or blank source selection process are flagged for exclusion from the primary analysis and retention for sensitivity checks.

**Stage 2: Filtering**
- Apply inclusion criteria (Chapter 3, Section 3.3.2):
  - Retain only records with `base_and_all_options_value` > $250,000 (above SAT).
  - Retain only records with `extent_competed` in {Full and Open Competition, Full and Open after Exclusion of Sources}.
  - Retain only records with `naics_code` in the 511xxx, 518xxx, 541xxx, or 561xxx families.
  - Retain only records with `source_selection_process` in {LPTA, TO} for the primary analysis.
- Apply exclusion criteria:
  - Exclude sole-source awards.
  - Exclude awards below the SAT.
  - Exclude records with `source_selection_process` = "O" or null from the primary sample; retain in a separate file for robustness checks.

**Stage 3: Aggregation from Transaction to Award Level**
- Group transaction records by `award_id_piid` (and `award_id_parent_award_piid` for task orders).
- For each award group:
  - Identify the initial award action (earliest `action_date` with `modification_number` = 0 or the lowest modification number).
  - Extract the source selection method, number of offers received, agency, NAICS code, PSC code, set-aside type, and initial financial values from the initial action record.
  - Compute the total transaction count and modification count.
  - Extract the current (most recent) financial values: `total_dollars_obligated`, `base_and_all_options_value`, `base_exercised_options_value`.
  - Extract the current period of performance end date from the most recent action record.
  - Compute contract duration in months.

**Stage 4: Variable Construction**
- Compute `cost_growth` = (current `base_and_all_options_value` - initial `base_exercised_options_value`) / initial `base_exercised_options_value`.
- Compute `cost_growth_w` by winsorizing `cost_growth` at the 1st and 99th percentiles of the sample distribution.
- Compute `log_award_amount` = ln(initial `base_exercised_options_value`).
- Construct `single_bid` = 1 if `number_of_offers_received` = 1, 0 otherwise.
- Construct `idv_indicator` from the presence of a parent award identifier.
- Construct `naics_sector` by mapping 6-digit NAICS codes to the four-category classification.
- Construct `contract_type` by mapping `type_of_contract_pricing` codes to the four-category classification.
- Construct `set_aside_type` by mapping detailed set-aside codes to the seven-category classification.
- Derive `fiscal_year` from `action_date`.
- Construct `dod_indicator` from `awarding_agency_code`.
- Construct the `procurement_design` composite variable from `solicitation_procedures` and `type_of_contract_pricing`.

**Stage 5: Propensity Score Estimation**
- Estimate the propensity score via logistic regression.
- Perform nearest-neighbor matching.
- Compute balance diagnostics.
- Generate the matched sample indicator variable.

### F.3 Load Phase

**Output Files:**
- `data/usaspending/processed/analysis_dataset.csv`: The award-level analysis dataset containing all variables described in Appendix A.
- `data/usaspending/processed/matched_sample.csv`: The propensity-score-matched sample with match identifiers and weights.
- `data/usaspending/processed/excluded_other.csv`: Awards with `source_selection_process` = "O" or null, retained for sensitivity analyses.
- `data/usaspending/processed/codebook.csv`: Machine-readable version of the variable codebook.

**Reproducibility:**
- All ETL scripts are maintained in the project repository under `analysis/scripts/`.
- Analysis notebooks are stored in `analysis/notebooks/`.
- Intermediate files are stored in `data/usaspending/intermediate/` for debugging and audit purposes.
- Python package versions are recorded in `requirements.txt`.
- Random seeds for matching procedures are set and documented to ensure exact reproducibility.

### F.4 Pipeline Diagram

```
USAspending.gov              GAO Annual Reports
Bulk CSV Downloads            (Manual Collection)
       |                            |
       v                            v
  data/usaspending/raw/       data/gao/
       |                            |
       v                            |
  Stage 1: Dedup & QC              |
       |                            |
       v                            |
  Stage 2: Filter                   |
  (NAICS, SAT, Competition,        |
   Source Selection)                |
       |                            |
       v                            |
  Stage 3: Aggregate                |
  (Transaction -> Award)           |
       |                            |
       v                            |
  Stage 4: Variable                 |
  Construction                     |
       |                            |
       v                            |
  Stage 5: PSM                      |
       |                            |
       v                            v
  analysis_dataset.csv       protest_statistics.csv
  matched_sample.csv
       |
       v
  Jupyter Notebooks
  (analysis/notebooks/)
       |
       v
  Results Tables & Figures
  (analysis/output/)
```

---

## Appendix G: Sampling Criteria and Sample Construction

This appendix provides a detailed listing of all inclusion and exclusion criteria applied to construct the analytic sample, with estimated or actual observation counts at each step. The purpose is to provide full transparency about the data reduction process and to enable readers to assess whether the final sample is representative of the target population.

### G.1 Sampling Flowchart

*Note: Counts will be updated with actual figures upon completion of data processing. Estimated ranges are provided below based on preliminary data exploration.*

| Step | Criterion | Records Remaining (Estimated) | Records Excluded (Estimated) | Exclusion Rate |
|:---|:---|:---:|:---:|:---:|
| 0 | **Starting population:** All contract transactions in FPDS-NG, FY2020--FY2025 | ~15,000,000--20,000,000 | -- | -- |
| 1 | Restrict to executive branch agencies reporting to FPDS | ~14,500,000--19,500,000 | ~500,000 | ~3% |
| 2 | Restrict to prime contract awards and modifications (exclude grants, loans, direct payments, other assistance) | ~8,000,000--12,000,000 | ~6,500,000 | ~40% |
| 3 | Restrict to NAICS codes 511xxx, 518xxx, 541xxx, 561xxx | ~2,000,000--3,500,000 | ~6,000,000--8,500,000 | ~70% |
| 4 | Restrict to competitive procurements (`extent_competed` = Full and Open Competition or Full and Open after Exclusion of Sources) | ~1,200,000--2,100,000 | ~800,000--1,400,000 | ~40% |
| 5 | Restrict to awards with `base_and_all_options_value` > $250,000 (above SAT) | ~600,000--1,200,000 | ~600,000--900,000 | ~50% |
| 6 | Restrict to `source_selection_process` = LPTA or TO (exclude "Other" and null) | ~450,000--900,000 | ~150,000--300,000 | ~25% |
| 7 | Aggregate from transaction level to award level (group by `award_id_piid`) | ~80,000--150,000 unique awards | -- | -- |
| 8 | Drop awards with missing key variables (missing `number_of_offers_received`, missing initial financial values, missing NAICS code) | ~75,000--145,000 | ~5,000 | ~3--5% |
| 9 | **Final analytic sample** | **~75,000--145,000** | | |

### G.2 Detailed Criteria Descriptions

**Step 1: Executive Branch Agencies**
Federal procurement data in FPDS-NG cover executive branch agencies. Legislative branch entities (e.g., Library of Congress, Government Publishing Office) and judicial branch entities report procurement data through separate systems and are excluded.

**Step 2: Prime Contract Awards**
USAspending.gov contains data on multiple federal spending categories: contracts, grants, loans, direct payments, insurance, and other assistance. Only contract awards (prime contracts and task/delivery orders) are relevant to this study. Subawards, grants, and non-contract obligations are excluded.

**Step 3: NAICS Sector Restriction**
The study focuses on four NAICS code families that represent the professional services and information technology domains where the LPTA-versus-tradeoff decision is most consequential:
- **511xxx** -- Software Publishers (including custom computer programming)
- **518xxx** -- Data Processing, Hosting, and Related Services (including cloud computing)
- **541xxx** -- Professional, Scientific, and Technical Services (including management consulting [5416], scientific consulting [5417], computer systems design [5415], R&D [5417], engineering [5413], accounting [5412], and legal services [5411])
- **561xxx** -- Administrative and Support Services (including facilities support [5612], office administrative services [5611], document preparation [5614], and staffing services [5613])

**Step 4: Competitive Procurements Only**
Source selection method is a concept that applies only to competitive procurements. Sole-source awards (where only one offeror is solicited or considered) are excluded because the choice between LPTA and tradeoff is not relevant when there is no competition. Awards under limited competition, follow-on contracts, or other non-full-and-open categories are also excluded to ensure a clean comparison of evaluation methods under competitive conditions.

**Step 5: Above Simplified Acquisition Threshold (SAT)**
Awards below $250,000 are subject to simplified acquisition procedures (FAR Part 13) that do not require formal source selection evaluation. The distinction between LPTA and tradeoff is less meaningful for these smaller acquisitions, and data quality for the source selection process field is likely lower. The $250,000 threshold reflects the current SAT as established by the 2018 NDAA.

**Step 6: Source Selection Process Filter**
Only awards coded as LPTA or TO (Tradeoff) in the `source_selection_process` field are included in the primary analysis. Awards coded as "O" (Other) represent a heterogeneous residual category that may include legitimate alternative evaluation methods, miscoded entries, or data quality gaps. Awards with null or blank source selection process values likely reflect non-reporting. Both categories are excluded from the primary sample to minimize measurement error but are retained for sensitivity analyses that assess whether their inclusion changes the results.

**Step 7: Transaction-to-Award Aggregation**
Multiple transaction records sharing the same `award_id_piid` are consolidated into a single award-level observation using the aggregation rules specified in Chapter 3, Section 3.3.4. This step transforms the dataset from the transaction level (multiple rows per contract) to the award level (one row per contract).

**Step 8: Missing Data Exclusion**
Awards missing critical variables are excluded. The most common sources of missing data are:
- `number_of_offers_received`: Occasionally unreported, particularly for task orders issued under pre-competed vehicles.
- Initial financial values: Rare, but some records have null or zero values for `base_exercised_options_value` at the initial award, which prevents computation of cost growth.
- `naics_code`: Very rare; virtually all contract actions include a NAICS code.

Missing data rates are reported for each variable. If the overall rate of exclusion due to missing data exceeds 5%, multiple imputation is considered as a sensitivity analysis.

### G.3 Sample Composition

*Note: Actual composition statistics will be inserted upon completion of data processing.*

**By Source Selection Method:**
- Tradeoff (TO): Estimated ~40--55% of sample
- LPTA: Estimated ~45--60% of sample

**By NAICS Sector:**
- IT Services (511, 518): Estimated ~20--30%
- Management and Technical Consulting (5416, 5417): Estimated ~15--25%
- Other Professional Services (remaining 541): Estimated ~25--35%
- Administrative Support (561): Estimated ~15--20%

**By Agency (top 5 by volume):**
- Department of Defense (all components): Estimated ~35--45%
- Department of Health and Human Services: Estimated ~8--12%
- Department of Homeland Security: Estimated ~6--10%
- Department of Veterans Affairs: Estimated ~5--8%
- General Services Administration: Estimated ~4--7%

**By Fiscal Year:**
- FY2020: Estimated ~14--18%
- FY2021: Estimated ~15--18%
- FY2022: Estimated ~16--18%
- FY2023: Estimated ~16--18%
- FY2024: Estimated ~16--18%
- FY2025: Estimated ~14--18%

**By Contract Type:**
- Firm-Fixed-Price: Estimated ~50--65%
- Cost-Plus-Fixed-Fee: Estimated ~15--25%
- Time-and-Materials / Labor-Hour: Estimated ~10--15%
- Other: Estimated ~5--10%

**By IDV Status:**
- Standalone (definitive) contracts: Estimated ~30--40%
- Task/delivery orders under IDVs: Estimated ~60--70%

### G.4 Comparison of Included and Excluded Observations

To assess potential selection effects from the filtering process, descriptive statistics for key variables are compared between the final analytic sample and the excluded observations (from Steps 3--6). Systematic differences between included and excluded observations are noted and discussed in the limitations section (Chapter 5) as potential threats to external validity.

| Variable | Included Sample (Mean/Proportion) | Excluded Sample (Mean/Proportion) | Difference |
|:---|:---:|:---:|:---:|
| Award Amount ($) | -- | -- | -- |
| Number of Offers | -- | -- | -- |
| DoD (proportion) | -- | -- | -- |
| FFP (proportion) | -- | -- | -- |
| FY Distribution | -- | -- | -- |
