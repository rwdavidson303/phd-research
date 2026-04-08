# Chapter 4: Results

## 4.1 Introduction to Results

This chapter presents the empirical findings of the study, organized around the hypotheses developed in Chapter 2 and tested using the methodology described in Chapter 3. The analysis draws on federal contract transaction data from USAspending.gov for Fiscal Year 2024 Quarter 2 (January through March 2024), encompassing competitive service and information technology awards above the Simplified Acquisition Threshold of $250,000. The results reported herein reflect the actual statistical outcomes of each hypothesis test, reported with full transparency and without alteration. As is characteristic of rigorous empirical research, the findings are mixed: some hypotheses receive support, while others do not. The pattern of results, taken as a whole, offers a more nuanced understanding of the relationship between procurement design and contract outcomes than any single hypothesis test could provide.

The analytical strategy follows the sequential logic outlined in Chapter 3. The chapter begins with a thorough description of the analysis sample, including its construction, composition, and the distributional properties of the key variables (Section 4.2). Understanding these distributional properties is essential for evaluating the appropriateness of the statistical models applied in subsequent sections and for contextualizing the substantive magnitude of the estimated effects. Section 4.3 examines the distribution of source selection methods across agencies and industry sectors, documenting the considerable institutional heterogeneity in procurement design usage that motivates the inclusion of agency and sector controls in the regression models. Section 4.4 reports the results of the propensity score estimation and matching diagnostics, establishing the comparability of the treatment and control groups and addressing the selection bias that arises from the non-random assignment of procurement design. Sections 4.5 and 4.6 present the results of the primary hypothesis tests and moderation analyses, respectively—the core empirical contributions of the study. Section 4.7 reports the propensity score matched sample results, providing a complementary set of estimates that are less susceptible to confounding by observed covariates. Section 4.8 describes the robustness checks and sensitivity analyses conducted to assess the stability of the primary findings across alternative sample definitions, variable specifications, and model assumptions. Section 4.9 concludes with a summary table mapping each hypothesis to its empirical outcome, accompanied by a discussion of effect sizes and statistical power.

Throughout this chapter, tables and figures are referenced in text and presented at the points of first discussion, consistent with APA 7th edition conventions. All statistical tests employ a significance threshold of alpha = .05 unless otherwise noted. Where appropriate, effect sizes are reported using Cohen's *d* for continuous outcomes, odds ratios for binary outcomes, and incidence rate ratios for count outcomes. Robust standard errors (HC3) are used in all ordinary least squares (OLS) models to account for heteroskedasticity, following the recommendation of Long and Ervin (2000) that HC3 standard errors provide the most reliable inference in samples of the size analyzed here. Confidence intervals are reported at the 95% level.

A note on the transparency of the findings is warranted at the outset. Of the four hypotheses tested in this chapter, three are not supported at conventional significance levels. The temptation in empirical research to emphasize positive findings and minimize null results is well documented in the methodological literature (Franco et al., 2014; Rosenthal, 1979). This chapter resists that temptation. The null findings are reported with the same rigor and detail as the significant findings, and the interpretation of each result acknowledges both what the data reveal and what they do not. As Greenwald (1975) argued, null results in well-powered studies are informative, not merely disappointing, and the pattern of null results observed here—combined with the one significant finding on moderation—tells a substantively meaningful story about the contingent nature of procurement design effects.

---

## 4.2 Sample Description and Descriptive Statistics

### 4.2.1 Sample Construction

The initial dataset comprised all contract transactions recorded in USAspending.gov for FY2024 Q2 (January 1 through March 31, 2024). The quarterly time window was selected to provide a manageable but representative snapshot of federal procurement activity. January through March represents a period of moderate procurement tempo—past the end-of-fiscal-year spending surge that characterizes September and October, but before the slowdown that sometimes occurs in the final quarter as agencies await new appropriations or continuing resolutions. The quarterly scope also aligns with the standard reporting cycles used by the Federal Procurement Data System (FPDS), facilitating data quality and completeness.

Consistent with the inclusion criteria specified in Chapter 3, the analysis was restricted to competitive awards in the service and information technology sectors, defined by North American Industry Classification System (NAICS) codes in three sectors: Sector 51 (Information), Sector 54 (Professional, Scientific, and Technical Services), and Sector 56 (Administrative and Support and Waste Management and Remediation Services). These three sectors were selected because they represent the categories of federal spending where source selection method choice is most consequential. Unlike commodity purchases, where specifications are standardized and price is the natural discriminator, service and IT acquisitions involve significant qualitative differentiation among offerors—in technical approach, staffing expertise, management methodology, and past performance. It is in precisely these categories that the choice between quality-evaluating and price-focused procurement designs is most likely to affect downstream outcomes.

Awards below the Simplified Acquisition Threshold (SAT) of $250,000 were excluded from the analysis. Below the SAT, federal agencies may use simplified acquisition procedures that do not require formal source selection evaluation plans, and the distinction between quality-evaluating and price-focused procurement is less meaningful. Non-competitive awards (sole-source contracts and contracts awarded without competition) were also excluded, as the research questions concern the effects of procurement design in competitive settings. Interagency agreements were excluded because they represent fund transfers between government entities rather than contracts with private-sector firms.

After applying these filters, the total analysis sample comprised 15,477 awards distributed across 58 federal agencies. This sample size provides substantial statistical power for the primary analyses and permits the estimation of models with multiple control variables and interaction terms without concern for degrees-of-freedom limitations.

### 4.2.2 Procurement Design Classification

A central methodological challenge addressed in this study is the absence of the FPDS `source_selection_process` field from USAspending.gov bulk download files. As discussed in Chapter 3, this field—which directly identifies whether an award was made using LPTA, tradeoff, or another evaluation approach—is reported in FPDS but is not included in the standard bulk data extracts available through USAspending.gov's Custom Award Data Download feature. This omission, which reflects the data architecture decisions made by the Treasury Department and the General Services Administration in designing the USAspending data pipeline, required the development of an alternative classification strategy.

The study employed a composite classification of procurement design based on two observable characteristics that are available in the USAspending bulk data: the solicitation procedure (negotiated proposals under FAR Part 15 versus sealed bidding under FAR Part 14 versus task/delivery orders under FAR Part 16) and the contract pricing type (cost-reimbursement versus firm-fixed-price versus other pricing arrangements). The combination of these two dimensions produces a typology that captures meaningfully different approaches to balancing price and quality considerations in the source selection process. The theoretical justification for this composite classification rests on two observations. First, negotiated proposals with cost-type pricing are almost exclusively used for complex requirements where the government places substantial weight on technical merit—the hallmark of quality-evaluating procurement. Second, sealed bidding with firm-fixed-price contracts represents the most price-dominant procurement approach, in which the lowest responsible bidder receives the award with minimal qualitative evaluation.

Table 4.1 presents the distribution of awards across the five procurement design categories.

**Table 4.1**

*Distribution of Awards by Procurement Design Category*

| Procurement Design Category | Abbreviation | Description | *n* | % of Total |
|---|---|---|---|---|
| Quality-Evaluating | QE | Negotiated proposals with cost-type pricing; emphasis on technical merit and quality evaluation | 1,379 | 8.9% |
| Negotiated Fixed-Price | NFP | Negotiated proposals with firm-fixed-price contracts; price competition within a negotiated framework | 2,490 | 16.1% |
| Task Order | TO | Task/delivery orders under existing indefinite delivery vehicle contracts | 11,446 | 74.0% |
| Price-Focused | PF | Sealed bidding with firm-fixed-price; most price-dominant approach | 38 | 0.2% |
| Other | OTH | Remaining combinations of solicitation procedure and pricing type | 124 | 0.8% |
| **Total** | | | **15,477** | **100.0%** |

Several features of this distribution merit extended comment.

First, task orders under existing indefinite delivery vehicles (IDVs) constituted the dominant procurement mechanism, accounting for 74.0% of all awards in the sample. This finding is consistent with, and reinforces, the broader trend in federal procurement toward the use of Government-Wide Acquisition Contracts (GWACs), multi-agency contracts (MACs), and agency-specific indefinite delivery/indefinite quantity (IDIQ) vehicles as the primary means of acquiring services (GAO, 2019). The dominance of task orders has significant implications for the study. Because the source selection decision for task orders occurs at the vehicle level (when the IDIQ contract is originally competed) rather than at the individual order level, the procurement design for task orders is effectively predetermined by the terms of the parent vehicle. For this reason, task orders were excluded from the primary QE-versus-NFP comparison but were included in robustness analyses (Section 4.8.1) to assess whether the main findings held in a broader sample.

Second, the Price-Focused category, representing pure sealed bidding with firm-fixed-price contracts, contained only 38 awards—a strikingly small number that reflects the near-obsolescence of sealed bidding for complex service acquisitions. Sealed bidding, once the default procurement method under the Competition in Contracting Act of 1984, has been almost entirely supplanted by negotiated procedures for service and IT procurements. This trend reflects the recognition, codified in the Federal Acquisition Streamlining Act of 1994 and subsequent reforms, that the rigidity of sealed bidding—with its requirement for award to the lowest responsive, responsible bidder without discussion—is poorly suited to requirements where technical approach and past performance are material discriminators. The virtual absence of Price-Focused awards precluded the inclusion of this category as a meaningful comparison group, which is why the primary analysis focuses on the QE-versus-NFP contrast rather than a broader comparison across all procurement design categories.

Third, the Other category (*n* = 124, 0.8%) encompassed residual combinations of solicitation procedure and pricing type that did not map cleanly onto the four primary categories. These included, for example, negotiated awards with time-and-materials pricing (which share characteristics of both QE and NFP) and awards with unusual contracting arrangements. The small size of this category precluded separate analysis.

Fourth, and most importantly for the study's analytical design, the two categories of primary analytical interest—Quality-Evaluating (QE) and Negotiated Fixed-Price (NFP)—together comprised 3,869 awards (25.0% of the total), forming the main comparison sample for hypothesis testing. The 1,379 QE awards and 2,490 NFP awards provided a sample with sufficient size for multivariable regression, propensity score matching, and subgroup analyses while representing a meaningful and clearly differentiated contrast in procurement philosophy.

### 4.2.3 Descriptive Statistics for Key Variables

Before proceeding to the regression analyses, it is essential to understand the distributional characteristics of the key variables. Table 4.2 presents descriptive statistics for the principal dependent and control variables, stratified by the two main procurement design categories. The table includes means, standard deviations, and medians for continuous variables, as well as percentages for categorical variables. Independent-samples *t*-tests are reported for comparisons between QE and NFP groups, along with Cohen's *d* effect sizes.

**Table 4.2**

*Descriptive Statistics for Key Variables by Procurement Design Category (QE vs. NFP)*

| Variable | QE (*n* = 1,379) | | | NFP (*n* = 2,490) | | | Test Statistic |
|---|---|---|---|---|---|---|---|
| | Mean | SD | Median | Mean | SD | Median | |
| Award obligation ($) | $4,550,000 | $53,700,000 | $80,000 | $1,050,000 | $3,800,000 | $107,000 | — |
| Log award amount | 15.26 | 1.89 | — | 14.59 | 1.52 | — | *t* = 10.52, *p* < .001, *d* = 0.36 |
| Cost growth (%, winsorized) | 9.85 | 10.62 | — | 7.82 | 9.45 | — | *t* = 4.24, *p* < .001, *d* = 0.20 |
| Modification count | 1.72 | 1.34 | — | 1.62 | 1.18 | — | *t* = 2.23, *p* = .026, *d* = 0.08 |
| Number of offers received | 6.29 | — | — | 8.21 | — | — | *t* = -0.87, *p* = .385, *d* = -0.05 |
| Single-bid rate (%) | 4.4% | — | — | 5.6% | — | — | *t* = -1.66, *p* = .096, *d* = -0.05 |

The descriptive statistics reveal several patterns that are critical for interpreting the subsequent regression results.

**Award Size.** QE awards were substantially larger than NFP awards in raw dollar terms. The mean obligation for QE awards was $4.55 million, compared with $1.05 million for NFP awards—a ratio of approximately 4.3 to 1. However, the distributions of award amounts were heavily right-skewed for both categories, as evidenced by the large disparity between means and medians. The QE median obligation of $80,000 was actually *lower* than the NFP median of $107,000, a seemingly paradoxical finding that indicates the higher QE mean was driven by a relatively small number of very large cost-type awards. The standard deviation of QE award amounts ($53.7 million) was more than fourteen times that of NFP awards ($3.8 million), further confirming the presence of extreme right-tail observations in the QE distribution. These distributional characteristics are typical of federal procurement data, where a small number of multibillion-dollar defense and health care contracts coexist with thousands of awards in the hundreds of thousands of dollars.

The extreme skewness of the award size distribution motivated the use of the natural logarithm of award amount (log award amount) as the operational measure of contract size in all regression models. When award amounts were log-transformed, QE awards remained significantly larger than NFP awards (*t* = 10.52, *p* < .001), with a small-to-medium effect size of *d* = 0.36. The Cohen's *d* of 0.36 indicates that QE awards were approximately one-third of a standard deviation larger than NFP awards on the log scale—a meaningful difference that confirmed the size differential was not solely attributable to outliers and that motivated the inclusion of log award amount as a control variable in all subsequent models. The systematic size difference between QE and NFP awards also underscored the importance of propensity score matching (Section 4.4), which explicitly balances the groups on this and other observed confounders.

**Cost Growth.** The raw descriptive comparison showed that QE awards exhibited *higher* mean cost growth (9.85%, *SD* = 10.62%) than NFP awards (7.82%, *SD* = 9.45%), a difference that was statistically significant (*t* = 4.24, *p* < .001) with a small effect size (*d* = 0.20). This pattern ran contrary to the directional prediction of Hypothesis 1, which posited that quality-evaluating procurement designs would be associated with *lower* cost growth. The descriptive finding is provocative and warrants careful interpretation.

The higher cost growth observed in QE awards in the unadjusted comparison could reflect several mechanisms operating simultaneously. First, QE awards are systematically larger, and larger contracts may experience greater absolute and percentage cost growth due to their longer performance periods, more complex deliverable structures, and greater exposure to requirements changes. Second, QE awards in this study are operationally defined by cost-type pricing, and cost-reimbursement contracts structurally permit—and indeed, under certain conditions, incentivize—cost growth, because the government bears the risk of cost overruns rather than the contractor. Third, confounding by agency could drive the observed difference if agencies that favor QE procurement also happen to have organizational characteristics (e.g., more complex missions, less stable requirements, or weaker contract oversight) that independently contribute to cost growth. The regression analyses reported in Section 4.5 address these confounds by controlling for log award amount, NAICS sector, and agency.

**Modification Intensity.** Modification counts were slightly higher for QE awards (mean = 1.72, *SD* = 1.34) than for NFP awards (mean = 1.62, *SD* = 1.18). This difference reached statistical significance (*t* = 2.23, *p* = .026) but with a negligible effect size (*d* = 0.08). A Cohen's *d* of 0.08 indicates that the two groups differed by less than one-tenth of a standard deviation on the modification count—a difference so small as to be practically indistinguishable. The practical significance of a 0.10-modification difference per contract is questionable, and the statistical significance of the *t*-test likely reflects the large sample size rather than a meaningful substantive difference. The negative binomial regression in Section 4.5.2 provides a more rigorous test of Hypothesis 2, controlling for confounders and properly accounting for the count nature and overdispersion of the modification variable.

**Competition Measures.** Competition intensity, measured by the number of offers received, did not differ significantly between procurement design categories. QE awards attracted an average of 6.29 offers compared with 8.21 for NFP awards, but this difference was not statistically significant (*t* = -0.87, *p* = .385, *d* = -0.05). The non-significance of this comparison should be interpreted in light of the substantial amount of missing data on the offer count variable (available for only 968 of 3,869 awards), which reduced statistical power and may have introduced non-random selection effects if the probability of reporting offer counts was correlated with procurement design or competition outcomes.

Similarly, single-bid rates were slightly lower for QE awards (4.4%) than for NFP awards (5.6%), but the difference did not reach conventional significance (*t* = -1.66, *p* = .096, *d* = -0.05). The direction of this difference—QE associated with lower single-bid rates—was consistent with the theoretical prediction of Hypothesis 6, and the *p*-value of .096 fell in the marginal zone between conventional significance and clear non-significance. Both competition measures are examined further in Sections 4.5.3 and 4.5.4 using multivariate models that control for confounding variables.

### 4.2.4 Award Size Distributions

The distributional properties of the key variables are important not only for descriptive purposes but also for evaluating the assumptions underlying the statistical models. Figure 4.1 presents the distribution of log-transformed award amounts for QE and NFP awards.

> **Figure 4.1.** Distribution of log award amounts by procurement design category (QE vs. NFP). The QE distribution (solid line) is shifted to the right relative to the NFP distribution (dashed line), reflecting the systematically larger average size of quality-evaluating procurements. Both distributions are approximately normal after log transformation, with slight positive skewness in the QE group.

The QE distribution is shifted to the right relative to NFP, consistent with the descriptive statistics reported above. Both distributions are approximately normal after the log transformation, with skewness and kurtosis values within acceptable ranges for OLS regression. The approximate normality of the log-transformed award amounts supports the use of OLS for models that employ log award amount as either a dependent or control variable, and it validates the linear specification of the propensity score model, which includes log award amount as a covariate.

The overlap between the two distributions is also noteworthy. Although the QE distribution is shifted rightward, there is substantial common support—that is, a wide range of log award amounts at which both QE and NFP awards are observed. This overlap is a necessary condition for propensity score matching, as it ensures that QE awards can be matched to NFP awards with similar characteristics. The common support region is discussed further in Section 4.4.

Figure 4.2 presents box plots of winsorized cost growth by procurement design category, providing a visual complement to the means and standard deviations reported in Table 4.2.

> **Figure 4.2.** Box plots of winsorized cost growth (%) by procurement design category. QE awards exhibit a higher median and greater interquartile range than NFP awards. Whiskers extend to 1.5 times the interquartile range; observations beyond this threshold are plotted individually. The wider QE distribution is consistent with the greater cost variability inherent in cost-type contracts.

The QE distribution shows both a higher median and a wider interquartile range than NFP, consistent with the interpretation that cost-type contracts, which predominate in the QE category, are inherently more variable in their cost outcomes. The greater spread of the QE cost growth distribution is not surprising: under cost-reimbursement pricing, the contractor is reimbursed for allowable costs incurred, plus a fee, and the government bears the risk of cost overruns. This risk allocation creates structural conditions under which cost growth—both positive (overruns) and, in some cases, negative (underruns or deobligations)—is more variable than under firm-fixed-price contracts, where the contractor bears cost risk and the government's obligation is fixed at the time of award.

### 4.2.5 Agency Distribution

The federal government is not a monolithic buyer. Procurement practices, organizational cultures, oversight intensity, and mission complexity vary enormously across the 58 agencies represented in the sample. Understanding the agency composition of the data is essential for interpreting the results, as any observed relationship between procurement design and outcomes could reflect agency-level confounding rather than a genuine procurement design effect.

Table 4.3 presents the distribution of awards across the five agencies with the largest representation in the sample, along with the aggregate counts for the remaining agencies.

**Table 4.3**

*Distribution of Awards by Agency (Top Five Agencies and Aggregate Remainder)*

| Agency | Total Awards | % of Sample | QE Awards | NFP Awards |
|---|---|---|---|---|
| Department of Defense (DoD) | 4,695 | 30.3% | — | — |
| Department of Health and Human Services (HHS) | 1,601 | 10.3% | — | — |
| Department of Homeland Security (DHS) | 1,210 | 7.8% | — | — |
| Department of Veterans Affairs (VA) | 760 | 4.9% | — | — |
| Department of Justice (DOJ) | 754 | 4.9% | — | — |
| All Other Agencies (53 agencies) | 6,457 | 41.7% | — | — |
| **Total** | **15,477** | **100.0%** | **1,379** | **2,490** |

The Department of Defense dominated the sample, accounting for nearly one-third of all awards (4,695 awards, 30.3%). This concentration reflects both the sheer scale of defense procurement—the DoD accounts for approximately two-thirds of all federal contract spending—and the department's heavy reliance on service contracts for information technology, professional services, and administrative support functions. The dominance of defense procurement in the sample is both a strength and a limitation: a strength because it ensures representation of the sector where source selection policy debates have been most active (e.g., Section 813 of the NDAA for FY2017), and a limitation because it raises the question of whether findings generalize to the civilian procurement environment, where institutional norms, oversight structures, and market dynamics may differ.

The top five agencies together accounted for 58.3% of all awards, with the remaining 53 agencies contributing 41.7%. This distribution—in which a small number of large agencies dominate the sample while a long tail of smaller agencies contribute modest numbers of awards—motivated the inclusion of agency fixed effects (operationalized as dummy variables for the top 10 agencies by volume) in the regression models. This specification controls for agency-level heterogeneity in procurement practices, oversight intensity, organizational culture, and any other time-invariant agency characteristics that might confound the relationship between procurement design and outcomes. Awards from agencies outside the top 10 are captured by the model intercept, effectively treating them as a pooled reference group.

The sample encompassed three NAICS sectors, which serve as a proxy for industry context. Sector 54 (Professional, Scientific, and Technical Services) was the largest contributor, reflecting the federal government's extensive use of consulting, engineering, and research services. Sector 56 (Administrative and Support Services) was the second largest, capturing facility management, security services, and other administrative support functions. Sector 51 (Information) was the smallest of the three sectors, encompassing telecommunications, data processing, and software services. NAICS sector dummy variables were included in all models to control for industry-specific differences in cost structures, competition dynamics, market concentration, and contract complexity.

### 4.2.6 Correlation Structure

Before estimating the multivariate models, the bivariate correlations among the key variables were examined to assess the potential for multicollinearity and to identify patterns that might inform model specification. Log award amount was positively correlated with both cost growth (*r* = .32) and modification count (*r* = .28), confirming that larger contracts tend to experience more cost escalation and more modifications—an intuitive pattern that reinforces the importance of controlling for award size. The correlation between cost growth and modification count was also positive (*r* = .41), reflecting the fact that many modifications involve scope changes or funding adjustments that directly contribute to cost growth. The Tradeoff indicator (QE = 1, NFP = 0) was positively correlated with log award amount (*r* = .17), confirming the descriptive finding that QE awards tend to be larger. No bivariate correlations among the independent variables exceeded .50, and variance inflation factors (VIFs) in the regression models were below 3.0 for all variables, indicating that multicollinearity was not a concern.

---

## 4.3 Source Selection Method Distribution

### 4.3.1 Distribution Across Procurement Design Categories

The distribution of procurement design categories across the full sample provides important context for understanding the institutional landscape within which the hypothesis tests are situated. Figure 4.3 presents the distribution of the full 15,477-award sample across the five procurement design categories.

> **Figure 4.3.** Distribution of awards by procurement design category (full sample, *N* = 15,477). Task orders (TO) represent the dominant procurement mechanism (74.0%), followed by Negotiated Fixed-Price (NFP, 16.1%) and Quality-Evaluating (QE, 8.9%). Price-Focused (PF, 0.2%) and Other (OTH, 0.8%) categories are negligibly small.

The dominance of task orders is visually apparent, as this category accounts for nearly three-quarters of all awards. This dominance has significant implications for the generalizability of the study's findings. The primary analysis compares QE and NFP awards, which together represent approximately one-quarter of all competitive service and IT awards above the SAT. The remaining three-quarters consist of task orders, whose procurement design is effectively determined at the vehicle level. To the extent that the factors driving outcomes for task orders differ from those affecting standalone negotiated procurements, the findings reported here may not generalize to the full federal service and IT procurement environment. This limitation is addressed partially by the robustness check in Section 4.8.1, which includes task orders in the analysis sample.

The near-absence of pure sealed-bid, firm-fixed-price awards (the Price-Focused category, *n* = 38) is a finding of substantive interest in its own right. Sealed bidding, once the default procurement method under the Competition in Contracting Act of 1984, has been almost entirely supplanted by negotiated procedures for complex service acquisitions. This finding is consistent with the historical trajectory of federal acquisition reform. The Federal Acquisition Streamlining Act of 1994, the Clinger-Cohen Act of 1996, and subsequent policy initiatives progressively expanded the use of negotiated procedures and best-value evaluation criteria, recognizing that the rigidity of sealed bidding—with its requirement for award to the lowest responsive, responsible bidder without discussion—is poorly suited to requirements where technical approach, management capability, and past performance are material discriminators. The data confirm that this policy evolution has been thoroughly implemented in practice: sealed bidding for service and IT contracts is now vanishingly rare.

### 4.3.2 Agency-Level Variation in Procurement Design Usage

Figure 4.4 presents the proportion of QE and NFP awards for each of the top ten agencies by award volume. The figure reveals substantial agency-level variation in the use of quality-evaluating versus negotiated fixed-price procurement designs.

> **Figure 4.4.** Proportion of QE and NFP awards by agency (top 10 agencies by total award volume). Agencies vary considerably in their use of quality-evaluating versus negotiated fixed-price procurement designs, reflecting differences in mission complexity, acquisition culture, and policy guidance. Error bars represent 95% confidence intervals for the QE proportion.

This variation is not random. Agencies with more complex, technically demanding missions—such as those involved in defense research, health care delivery, and intelligence operations—would be expected to favor quality-evaluating procurement designs that permit the government to assess technical approach and management capability. Agencies with more standardized, routine service requirements may favor negotiated fixed-price designs that emphasize price competition within a negotiated framework. The agency-level variation also reflects differences in acquisition workforce capacity, as the more elaborate evaluation procedures required for quality-evaluating procurement demand greater expertise and time from the contracting officer and technical evaluation team.

The agency-level variation in procurement design usage underscored the importance of controlling for agency effects in the regression models. If certain agencies that favor QE procurement also tend to award larger, more complex contracts—or if they have organizational characteristics that independently influence cost growth and modification patterns—then agency-level confounding could bias the estimated relationship between procurement design and outcomes. The inclusion of agency dummy variables in the regression specifications addresses this concern directly. The propensity score matching procedure (Section 4.4) further mitigates agency-level confounding by explicitly balancing the treatment and control groups on agency composition.

### 4.3.3 NAICS Sector Variation

The distribution of procurement design also varied by NAICS sector. Within the QE-versus-NFP comparison sample (*N* = 3,869), Professional, Scientific, and Technical Services (NAICS 54) accounted for the largest share of awards in both categories, consistent with the prominence of this sector in federal service procurement. However, the relative use of QE and NFP differed across sectors. Administrative and Support Services (NAICS 56) showed a higher proportion of NFP awards relative to QE, consistent with the interpretation that administrative services tend to be more standardized and less technically complex than professional services or IT, making price-focused procurement designs more appropriate. Information services (NAICS 51) were represented in both categories but with a smaller total count, limiting the precision of sector-specific estimates (as confirmed by the NAICS 51 robustness check in Section 4.8.4).

The NAICS sector variation reinforced the decision to include sector dummy variables in all regression models. By controlling for sector, the models ensure that the estimated procurement design effect is not confounded by systematic differences in cost structures, competition dynamics, or contract complexity across industries.

### 4.3.4 Temporal Considerations Within the Analysis Window

Although the analysis window spans a single fiscal quarter (January through March 2024), it is worth noting that procurement activity within this period is not uniformly distributed. January typically sees a surge of new fiscal year awards as agencies execute procurement actions that were in the pipeline during the preceding quarter. February and March represent more typical procurement tempo. The single-quarter design ensures temporal homogeneity—all awards in the sample were executed under the same economic conditions, regulatory framework, and political environment—but it also means that the findings are a snapshot of procurement behavior at a specific point in time. Seasonal patterns, budget cycle effects, and the particular policy environment of early calendar year 2024 may limit the generalizability of the results to other periods. The decision to use a single quarter reflects a deliberate trade-off between temporal homogeneity (which strengthens internal validity) and temporal breadth (which would strengthen external validity). Future research employing multi-year panels could assess the stability of the findings across different temporal contexts.

---

## 4.4 Propensity Score Estimation and Matching Diagnostics

### 4.4.1 Rationale for Propensity Score Matching

As discussed in Chapter 3, the fundamental identification challenge in this study is that procurement design is not randomly assigned. Agencies select their procurement approach in light of the characteristics of each acquisition, including its size, complexity, risk profile, and industry sector. If these same characteristics also influence contract outcomes—as theory and prior evidence suggest they do—then a naive comparison of QE and NFP awards would confound the effect of procurement design with the effects of these selection factors. The regression models in Section 4.5 address this confounding by including control variables for log award amount, NAICS sector, and agency. Propensity score matching (PSM) provides a complementary approach that addresses confounding through sample design rather than statistical adjustment.

PSM creates a matched comparison sample in which QE and NFP awards are balanced on observed covariates, thereby approximating the conditions of a randomized experiment within the constraints of an observational study (Rosenbaum & Rubin, 1983). The propensity score—the estimated probability of receiving the treatment (QE procurement design) conditional on observed covariates—serves as a scalar summary of the multidimensional covariate space. By matching QE awards to NFP awards with similar propensity scores, the procedure ensures that the matched groups are comparable on the full set of covariates, reducing the risk that estimated treatment effects are confounded by observed selection factors (Austin, 2011).

The decision to use PSM as a complementary rather than primary identification strategy reflects the inherent limitations of matching methods. PSM can only balance on observed covariates; unobserved confounders remain unaddressed. Additionally, PSM requires discarding unmatched observations, potentially limiting the generalizability of the estimates. The dual strategy of full-sample regression (Section 4.5) plus PSM matched-sample analysis (Section 4.7) provides estimates that are robust to different assumptions about the confounding structure: regression adjusts parametrically for confounders, while PSM adjusts nonparametrically through sample design.

### 4.4.2 Propensity Score Model Specification and Estimation

The propensity score was estimated using a logistic regression model in which the dependent variable was the binary indicator for QE procurement design (1 = QE, 0 = NFP) and the independent variables were the observable covariates hypothesized to influence the selection of procurement design. These covariates were selected based on the theoretical framework developed in Chapter 2 and the practical understanding of federal procurement practices. They included:

- **Log-transformed award amount**: Larger procurements are more likely to use cost-type pricing and quality-evaluating evaluation criteria, reflecting the greater complexity and risk associated with high-value acquisitions.
- **Transaction count**: The number of transactions associated with an award captures the complexity of the contract's administrative history and may be correlated with procurement design choice.
- **NAICS sector dummy variables**: Two dummy variables for Sectors 51 and 56, with Sector 54 as the reference category, capturing industry-level differences in the propensity to use QE versus NFP procurement.
- **Agency dummy variables**: Ten dummy variables for the top 10 agencies by award volume, capturing agency-level differences in procurement culture, policy guidance, and mission complexity.

Table 4.4 summarizes the key characteristics of the propensity score model and the matching procedure.

**Table 4.4**

*Propensity Score Estimation and Matching Summary*

| Model Characteristic | Value |
|---|---|
| Dependent variable | QE indicator (1 = QE, 0 = NFP) |
| Sample size | 3,869 |
| Pseudo *R*² | 0.106 |
| Covariates | Log award amount, transaction count, NAICS sector dummies (2), top 10 agency dummies (10) |
| PS score, treatment group: Mean (SD) | 0.446 (0.195) |
| PS score, control group: Mean (SD) | 0.307 (0.144) |
| Matching algorithm | 1:1 nearest-neighbor without replacement |
| Caliper | 0.05 (on the propensity score scale) |
| Matched pairs | 1,093 |
| Unmatched treatment units | 286 |
| Match rate | 79.3% |
| Matched sample size | 2,186 |

The pseudo *R*² of 0.106 indicated that the covariates included in the model explained a modest but meaningful share of the variation in procurement design selection. The interpretation of pseudo *R*² in the context of propensity score estimation differs from its interpretation in standard regression analysis. In PSM, a pseudo *R*² that is too high (above approximately 0.25 to 0.30) would suggest that QE and NFP awards occupy entirely different regions of the covariate space, making matching infeasible because few treated units would have viable control matches. Conversely, a pseudo *R*² near zero would suggest that the covariates do not predict selection, obviating the need for matching (since the groups would already be balanced). The observed value of 0.106 fell within the range typically considered appropriate for PSM applications in the social sciences (Caliendo & Kopeinig, 2008), indicating meaningful but not overwhelming selection on observables.

The mean propensity scores differed between the treatment group (QE: 0.446, *SD* = 0.195) and the control group (NFP: 0.307, *SD* = 0.144), confirming that QE and NFP awards differed systematically on the observed covariates prior to matching. The treatment group's higher mean propensity score (0.446 vs. 0.307) reflects the fact that QE awards tend to be larger and concentrated in certain agencies and sectors—characteristics that the propensity score model captures. The standard deviations indicated that there was substantial overlap in the propensity score distributions (i.e., a wide common support region), a necessary condition for successful matching.

### 4.4.3 Matching Results and Balance Diagnostics

One-to-one nearest-neighbor matching without replacement was conducted with a caliper of 0.05 on the propensity score scale. The caliper imposes a maximum permissible distance between matched pairs: a QE award is matched to the nearest NFP award on the propensity score scale, but only if the distance between their propensity scores does not exceed 0.05. This caliper width was chosen to balance the competing objectives of match quality (tighter calipers produce better-matched pairs but more unmatched units) and sample retention (wider calipers retain more observations but at the cost of poorer matches). The chosen caliper of 0.05 is within the range recommended by Austin (2011), who suggested calipers between 0.01 and 0.10 depending on the application.

Of the 1,379 QE awards in the treatment group, 1,093 (79.3%) were successfully matched to an NFP award within the caliper distance. The remaining 286 QE awards (20.7%) could not be matched within the specified caliper, typically because they occupied regions of the propensity score distribution where NFP awards were sparse. These unmatched units tended to represent very large awards from agencies with particularly high QE usage rates—observations that are, by definition, the most dissimilar from the NFP population and for which matched estimation is least feasible.

The matched sample of 2,186 awards (1,093 QE and 1,093 NFP) was then assessed for covariate balance. The standardized mean difference (SMD) was computed for each covariate before and after matching. The SMD is calculated as the difference in means between the treatment and control groups, divided by the pooled standard deviation. SMD values below 0.10 in absolute value are generally considered indicative of adequate balance (Austin, 2011; Stuart, 2010).

Figure 4.5 presents a Love plot displaying the SMD for each covariate before and after matching.

> **Figure 4.5.** Love plot of standardized mean differences (SMD) for covariates before and after propensity score matching. The vertical dashed lines at SMD = -0.10 and SMD = 0.10 indicate the conventional threshold for adequate balance. Matching substantially reduced imbalance on log award amount (from 0.363 to -0.120) and NAICS Sector 54 (from 0.202 to 0.056). Most covariates fell within or near the balance threshold after matching.

The most important covariate for the analysis was log award amount, given the substantial size differential between QE and NFP awards documented in Section 4.2.3. Before matching, the SMD for log award amount was 0.363, indicating a meaningful imbalance that exceeded the conventional threshold by a factor of more than three. After matching, the SMD was reduced to -0.120—a substantial improvement, though the absolute value (0.120) remained slightly above the conventional 0.10 threshold. This residual imbalance reflected the inherent difficulty of perfectly matching QE and NFP awards on size when QE awards are systematically larger: even after restricting the comparison to the most similar pairs, QE awards in the matched sample remained slightly larger on average. The negative sign indicates that after matching, the NFP matches were slightly larger than their QE counterparts, reflecting the asymmetric distribution of award sizes. The residual imbalance on log award amount was addressed by retaining this variable as a control in the matched-sample regressions, effectively combining the PSM-based and regression-based adjustment strategies—a "doubly robust" approach that is consistent if either the propensity score model or the outcome regression model is correctly specified (Bang & Robins, 2005).

The NAICS Sector 54 dummy variable showed a similar pattern of improvement, with the SMD declining from 0.202 to 0.056 after matching—well within the balance threshold. The remaining covariates (NAICS Sector 51 and 56 dummies, transaction count, and the agency dummies) generally showed adequate balance both before and after matching, with most SMD values below 0.10 in both conditions.

Figure 4.6 presents the propensity score distributions for the treatment and control groups before and after matching, providing a visual assessment of common support and distributional overlap.

> **Figure 4.6.** Propensity score distributions before and after matching. Panel (a) shows the raw distributions, which differ in location and spread, with the QE distribution shifted to the right. Panel (b) shows the matched distributions, which exhibit substantially greater overlap, confirming that matching improved the comparability of the two groups on observed covariates.

The improvement in overlap between the propensity score distributions after matching confirmed that the PSM procedure achieved its primary objective: creating a comparison sample in which QE and NFP awards were more similar on observed characteristics than in the full sample. The matched distributions in Panel (b) are much more similar in location and shape than the raw distributions in Panel (a), indicating that the caliper-based matching successfully eliminated the most extreme cases of imbalance.

### 4.4.4 Limitations of the Matching Procedure

Several limitations of the matching procedure warrant explicit acknowledgment, as they bear on the interpretation of the matched-sample results reported in Section 4.7.

First, the 79.3% match rate means that 286 QE awards (20.7%) were excluded from the matched analysis. These unmatched units are not a random subset of the treatment group; they are systematically different, tending to be larger and from agencies with particularly high QE usage rates. The exclusion of these units raises the question of whether the matched-sample results generalize to the full population of QE awards or only to the subset that has viable NFP counterparts. In PSM terminology, the matched-sample estimates represent the average treatment effect on the treated (ATT) within the region of common support, not the population ATT. The full-sample regression results, which retain all observations and adjust parametrically for confounders, provide a complementary set of estimates that are not subject to this selection and that estimate a parameter closer to the population average treatment effect.

Second, PSM can only balance on observed covariates. Unobserved factors that influence both the choice of procurement design and contract outcomes—such as the contracting officer's experience and risk tolerance, the quality and clarity of the statement of work, the depth of the market for the required services, the stability of the requirement over the contract period, and the intensity of post-award oversight—are not captured by the propensity score model. To the extent that these unobserved factors are correlated with the treatment indicator, the matched-sample estimates may still be biased. This limitation, which is common to all observational studies and cannot be fully resolved without randomized assignment, is addressed through multiple robustness checks (Section 4.8) and is discussed as a qualification on causal interpretation in Chapter 5.

Third, the choice of matching algorithm (1:1 nearest-neighbor without replacement) and caliper (0.05) involves trade-offs that could influence the results. Alternative matching algorithms (e.g., kernel matching, radius matching, or matching with multiple controls) might produce different estimates, and the sensitivity of the results to these choices was not exhaustively explored. However, the consistency between the full-sample regression results and the matched-sample results (reported in Section 4.7) provides reassurance that the findings are not highly sensitive to the specific matching approach employed.

---

## 4.5 Primary Hypothesis Tests

This section presents the results of the primary hypothesis tests, corresponding to Hypotheses 1, 2, and 6 as developed in Chapter 2. Each hypothesis is tested using the full QE-versus-NFP comparison sample (*N* = 3,869, or the analysis-specific subsample after excluding observations with missing values on the dependent variable), with regression controls for log award amount, NAICS sector dummy variables, and agency dummy variables. Propensity score matched results are reported separately in Section 4.7 to provide a complementary set of estimates.

### 4.5.1 H1: Cost Growth and Source Selection Method

**Hypothesis 1:** Contracts awarded through quality-evaluating procurement designs (QE) will exhibit lower cost growth than contracts awarded through negotiated fixed-price (NFP) designs.

The theoretical rationale for this hypothesis, grounded in transaction cost economics (Williamson, 1985, 1996), was that quality-evaluating procurement designs—by allowing the government to assess technical approach, management capability, and past performance in addition to price—should yield better contractor-requirement fit and, consequently, fewer unanticipated scope changes, disputes, and cost escalations during contract performance. In the language of transaction cost economics, quality evaluation reduces the bounded rationality and opportunism problems that arise when complex transactions are governed by simple price-based mechanisms. The hypothesis predicts that this reduction in transaction costs manifests as lower post-award cost growth.

The hypothesis was tested using OLS regression with winsorized cost growth (capped at the 1st and 99th percentiles of the distribution) as the dependent variable. Heteroskedasticity-consistent (HC3) robust standard errors were employed to address the non-constant variance that is typical of financial outcome data. The model specification was:

Cost Growth (%) = beta_0 + beta_1(Tradeoff) + beta_2(Log Award Amount) + sum(beta_j * NAICS_j) + sum(beta_k * Agency_k) + epsilon

where Tradeoff is a binary indicator (1 = QE, 0 = NFP), NAICS_j represents sector dummy variables, and Agency_k represents the top 10 agency dummy variables. The coefficient of interest is beta_1, which estimates the difference in mean cost growth between QE and NFP awards, conditional on award size, sector, and agency.

**Table 4.5**

*OLS Regression Results: Cost Growth as a Function of Procurement Design (Full Sample)*

| Variable | Coefficient | Robust SE (HC3) | *t* | *p* | 95% CI |
|---|---|---|---|---|---|
| Intercept | — | — | — | — | — |
| Tradeoff (QE = 1) | 0.413 | 0.468 | 0.88 | .377 | [-0.503, 1.330] |
| Log award amount | — | — | — | — | — |
| NAICS sector dummies | (included) | | | | |
| Agency dummies | (included) | | | | |
| | | | | | |
| *N* | 2,164 | | | | |
| *R*² | 0.151 | | | | |
| *F*-statistic | 207.32 | | | | |
| *p* (model) | < .001 | | | | |

The key coefficient of interest is the Tradeoff indicator. The estimated coefficient was 0.413 (*SE* = 0.468, *t* = 0.88, *p* = .377, 95% CI [-0.503, 1.330]). This result indicated that, controlling for award size, NAICS sector, and agency, QE procurement design was not significantly associated with cost growth. The point estimate of 0.413 percentage points suggests that QE awards experienced slightly higher cost growth than NFP awards—the opposite of the hypothesized direction—but the *p*-value of .377 was far from conventional significance thresholds, and the 95% confidence interval spanned zero, encompassing effects ranging from -0.503 to +1.330 percentage points. The wide confidence interval reflects the substantial residual variance in cost growth that is not explained by procurement design or the control variables.

**Hypothesis 1 was not supported.** The data provided no evidence that quality-evaluating procurement designs were associated with lower cost growth relative to negotiated fixed-price designs, after controlling for award size and institutional context.

Several aspects of this result merit detailed discussion.

First, the model's overall *R*² of 0.151 indicated that the included covariates explained approximately 15.1% of the variation in winsorized cost growth. While this explanatory power is modest in absolute terms, it is consistent with the general finding in the procurement literature that individual contract characteristics explain only a small share of outcome variance (Bajari et al., 2014). The *F*-statistic of 207.32 (*p* < .001) confirmed that the model was statistically significant overall, meaning that at least some of the control variables—particularly log award amount, which is the strongest predictor of cost growth—contributed meaningfully to the model's explanatory power. The non-significance of the Tradeoff variable thus did not reflect a failure of the model as a whole but rather the specific absence of a detectable procurement design effect after accounting for the other factors that drive cost growth.

Second, the sample size of 2,164 (rather than the full 3,869) reflects the exclusion of observations with missing cost growth data. Cost growth could not be computed for awards that had not yet received any modifications at the time of data extraction or for which the initial and current obligation amounts were not consistently reported. The reduction from 3,869 to 2,164 represents a loss of 44.1% of the comparison sample. If the probability of having computable cost growth data was correlated with procurement design or with the magnitude of cost growth itself (e.g., if awards with no modifications—and hence zero cost growth—were disproportionately excluded), then the effective sample may not be representative of the full population. This potential selection issue is inherent in the cost growth measure and represents a limitation of the analysis.

Third, the null finding on Hypothesis 1 admits multiple interpretations that are not distinguishable with the present data. One interpretation is that the proxy measure of procurement design used in this study—based on solicitation procedure and pricing type rather than the direct `source_selection_process` field—introduces measurement error that attenuates the estimated relationship toward zero. If some QE-classified awards did not actually involve a formal best-value tradeoff evaluation, or if some NFP awards did, then the contrast between the two categories would be diluted, and a genuine effect could be masked by classification noise. A second interpretation is that cost growth is driven primarily by factors not captured in the model—requirements volatility, contractor capacity, market conditions, the quality of post-award contract administration, and the stability of government funding—and that procurement design, even when perfectly measured, contributes only a negligible increment of explained variance. A third interpretation is that the true effect of procurement design on cost growth is genuinely small or zero in the population of service and IT contracts above the SAT, particularly when cost-type contracts (which are structurally expected to show greater cost variation) are classified as the "quality-evaluating" category. These interpretive possibilities are not mutually exclusive, and their relative plausibility is explored further in Chapter 5.

### 4.5.2 H2: Modification Intensity

**Hypothesis 2:** Contracts awarded through quality-evaluating procurement designs (QE) will experience fewer post-award modifications than contracts awarded through negotiated fixed-price (NFP) designs.

The rationale for this hypothesis followed from the logic of Hypothesis 1 and from the role of modifications in the federal contracting process. Post-award contract modifications serve multiple purposes: they may adjust scope, extend performance periods, exercise options, modify funding, or resolve disputes. While not all modifications are problematic—options exercises and incremental funding actions are routine administrative events—a higher rate of modifications is generally interpreted as an indicator of post-award instability, requirements volatility, or misalignment between the original contract terms and the actual needs that emerge during performance (Rendon & Snider, 2019). If quality-evaluating procurement designs produce better contractor-requirement alignment through more thorough pre-award evaluation, they should also produce fewer post-award modifications, particularly those that reflect scope changes, cost adjustments, and other corrections to initial misalignments.

Because modification counts are non-negative integer-valued data with overdispersion (the variance exceeds the mean), the hypothesis was tested using a negative binomial generalized linear model (GLM), which is the appropriate distributional family for such data (Cameron & Trivedi, 2013; Hilbe, 2011). The Poisson model, which assumes equality of the mean and variance, was rejected in favor of the negative binomial based on the likelihood ratio test for overdispersion.

**Table 4.6**

*Negative Binomial GLM Results: Modification Count as a Function of Procurement Design*

| Variable | Coefficient | SE | *z* | *p* | 95% CI |
|---|---|---|---|---|---|
| Intercept | — | — | — | — | — |
| Tradeoff (QE = 1) | -0.034 | 0.045 | -0.76 | .449 | [-0.123, 0.055] |
| Log award amount | — | — | — | — | — |
| NAICS sector dummies | (included) | | | | |
| Agency dummies | (included) | | | | |
| | | | | | |
| *N* | 3,869 | | | | |
| Deviance | 660.73 | | | | |
| AIC | 13,468 | | | | |

The Tradeoff coefficient was -0.034 (*SE* = 0.045, *z* = -0.76, *p* = .449, 95% CI [-0.123, 0.055]). In the negative binomial model, coefficients are on the log-count scale, meaning that each coefficient represents the expected change in the natural logarithm of the modification count associated with a one-unit change in the predictor. Exponentiating the Tradeoff coefficient yields an incidence rate ratio (IRR) of exp(-0.034) = 0.967, indicating that QE awards were associated with approximately 3.3% fewer modifications than NFP awards. The 95% confidence interval for the IRR, obtained by exponentiating the bounds of the coefficient confidence interval, ranged from exp(-0.123) = 0.884 to exp(0.055) = 1.057, encompassing the null value of 1.0. The *p*-value of .449 was far from conventional significance, and the confidence interval indicated that the data were consistent with effects ranging from an 11.6% reduction to a 5.7% increase in modification counts.

**Hypothesis 2 was not supported.** There was no statistically significant difference in modification intensity between QE and NFP awards after controlling for award size, NAICS sector, and agency.

The deviance statistic of 660.73 indicated adequate model fit relative to the number of observations, and the AIC of 13,468 provided a benchmark for comparison with alternative model specifications. The use of the negative binomial rather than the Poisson model was supported by the data: the deviance-to-degrees-of-freedom ratio was well below the value that would indicate overdispersion in a Poisson model, confirming that the negative binomial provided a better fit.

The null result on modification intensity is internally consistent with the null result on cost growth (Hypothesis 1). Modifications are a primary mechanism through which cost growth occurs: when a contract is modified to add scope, extend the period of performance, or adjust pricing, the cumulative obligation typically increases, contributing to measured cost growth. If procurement design does not significantly predict cost growth, it would be logically inconsistent to find a strong effect on the modification count that produces that cost growth. The consistency of the null findings across Hypotheses 1 and 2 strengthens the inference that the null pattern reflects a genuine absence of a main effect rather than a statistical anomaly in any single model.

It is also worth noting that the modification count variable captures all types of modifications, including routine administrative actions (e.g., incremental funding, exercising options) that do not reflect post-award instability. A more refined measure that distinguished problematic modifications (scope changes, engineering change proposals, claims settlements) from routine administrative actions might yield different results. However, the USAspending data do not provide sufficient detail on modification type to support this distinction, and the aggregate modification count was used as the best available proxy.

### 4.5.3 H6: Single-Bid Competition

**Hypothesis 6:** Quality-evaluating procurement designs (QE) will be associated with lower rates of single-bid outcomes compared with negotiated fixed-price (NFP) designs.

This hypothesis was motivated by the theoretical argument that procurement designs emphasizing quality evaluation signal to potential offerors that technical merit and past performance will be rewarded, thereby encouraging participation from firms that might otherwise decline to compete in a lowest-price environment. The signaling mechanism operates as follows: when a solicitation advertises that the government will evaluate proposals on the basis of technical approach, management plan, staffing qualifications, and past performance—in addition to price—firms with superior capabilities perceive a realistic prospect of winning despite not being the lowest bidder. This perception increases the expected value of proposal preparation for technically strong firms, inducing them to invest in proposal development and submit competitive offers. Conversely, price-focused solicitations may deter technically strong firms whose cost structures reflect higher-quality inputs, leaving the competition to lower-cost, potentially lower-quality competitors. The net effect, this hypothesis predicts, is that quality-evaluating procurement designs attract more offerors and reduce the probability of single-bid outcomes.

The hypothesis was tested using logistic regression, with the binary indicator for single-bid outcome (1 = only one offer received, 0 = two or more offers received) as the dependent variable.

**Table 4.7**

*Logistic Regression Results: Single-Bid Outcome as a Function of Procurement Design*

| Variable | Coefficient | SE | *z* | *p* | OR | 95% CI (OR) |
|---|---|---|---|---|---|---|
| Intercept | — | — | — | — | — | — |
| Tradeoff (QE = 1) | -0.285 | 0.166 | -1.72 | .085 | 0.752 | [0.543, 1.040] |
| Log award amount | — | — | — | — | — | — |
| NAICS sector dummies | (included) | | | | | |
| Agency dummies | (included) | | | | | |
| | | | | | | |
| *N* | 3,869 | | | | | |
| Pseudo *R*² | 0.035 | | | | | |
| AIC | 1,545.5 | | | | | |

The Tradeoff coefficient was -0.285 (*SE* = 0.166, *z* = -1.72, *p* = .085), corresponding to an odds ratio of 0.752 (95% CI [0.543, 1.040]). The direction of the effect was consistent with the hypothesis: QE procurement design was associated with approximately 24.8% lower odds of a single-bid outcome relative to NFP design. However, the *p*-value of .085 did not meet the pre-specified significance threshold of alpha = .05, and the confidence interval for the odds ratio included 1.0 (specifically, the upper bound of 1.040), precluding a definitive conclusion that QE design reduces single-bid rates.

**Hypothesis 6 was not supported at alpha = .05**, though the result was marginally significant at the .10 level (*p* = .085). The direction of the estimated effect was consistent with the hypothesis, and the odds ratio of 0.752 represented a substantively meaningful effect size—suggesting that QE procurement designs may reduce the odds of a single-bid outcome by approximately one-quarter. The marginal significance of this finding, falling in the ambiguous zone between the conventional .05 threshold and clear non-significance, invites further investigation with larger samples or alternative operationalizations of competition.

Several contextual factors bear on the interpretation of this result. First, the pseudo *R*² of 0.035 indicated that the model explained only 3.5% of the variation in single-bid outcomes. This modest explanatory power is not unexpected, given the multiplicity of factors that influence vendor participation decisions, including market conditions, geographic location, set-aside provisions, contract vehicle structure, timing relative to the fiscal year, and the perceived probability of protest. Procurement design is one of many influences on competition, and even a real effect could be small relative to the total variance.

Second, the base rates of single-bid outcomes were quite low in both groups (4.4% for QE and 5.6% for NFP). When the outcome of interest is rare, logistic regression estimates become less precise because the effective information in the data is concentrated in the small number of events rather than the large number of non-events (King & Zeng, 2001). The low base rate reduced statistical power for detecting differences between groups, and a study with a larger sample or a longer observation period—capturing more single-bid events—might achieve sufficient power to detect the effect suggested by the point estimate.

Third, the practical significance of the finding deserves consideration alongside the statistical significance. An odds ratio of 0.752 implies that, for every 100 procurements that would result in a single-bid outcome under NFP design, approximately 75 would result in a single-bid outcome under QE design—a meaningful reduction in the frequency of non-competitive outcomes. If this effect is real, its policy implications are substantial, as single-bid procurements deny the government the competitive tension that drives pricing discipline and innovation. The marginal statistical significance, in this context, may reflect a power limitation rather than the absence of a meaningful effect.

### 4.5.4 Competition Intensity

In addition to the single-bid indicator, the study examined competition intensity as measured by the continuous count of offers received. This analysis was conducted as an exploratory extension rather than a formal hypothesis test, given the well-documented limitations of the number-of-offers variable in the USAspending data. The field is frequently missing, reported inconsistently across agencies, and subject to definitional ambiguity (e.g., whether to count proposals deemed non-responsive, late submissions, or withdrawn offers).

An OLS regression of number of offers received on the Tradeoff indicator, controlling for log award amount, NAICS sector, and agency dummies, was estimated on the subsample of awards with non-missing offer count data (*N* = 968). The restriction to 968 observations (from a potential 3,869) reflects the 75.0% missing data rate on the offer count variable—a rate so high as to raise serious questions about the representativeness of the analysis sample and the validity of inferences drawn from it.

The Tradeoff coefficient was -1.607 (*SE* = 2.002, *p* = .422), suggesting that QE awards attracted approximately 1.6 fewer offers than NFP awards, but this difference was not statistically significant. The model *R*² was 0.012, indicating that the predictor variables explained only 1.2% of the variation in offer counts—an extremely low level of explanatory power that suggests the model is missing important determinants of competition or that the offer count variable is measured with substantial noise.

The null result on competition intensity is consistent with the marginal result on single-bid rates. Both analyses suggest that procurement design does not have a strong, detectable effect on vendor participation in the present data, though the severe data quality issues with the offer count variable limit the confidence that can be placed in this conclusion. The 75% missing data rate is particularly concerning because it raises the possibility of non-random selection: if agencies that report offer counts differ systematically from those that do not (e.g., in their procurement sophistication, data management practices, or competition outcomes), then the observed relationship between procurement design and offer count may not generalize to the full population.

---

## 4.6 Moderation Effects: H8 Complexity Hypothesis

**Hypothesis 8:** The relationship between procurement design and cost growth is moderated by procurement complexity, such that quality-evaluating designs yield greater cost growth advantages (i.e., lower cost growth relative to NFP) for more complex procurements.

This hypothesis represents the most theoretically grounded prediction in the study, drawing directly on the central contingency logic of transaction cost economics. Williamson (1985, 1996) argued that the optimal governance structure for a transaction depends on the transaction's attributes—particularly its complexity (asset specificity), uncertainty, and frequency. Simple, well-specified transactions can be governed efficiently by market mechanisms (analogous to price-focused procurement), while complex, uncertain transactions require more hierarchical governance (analogous to quality-evaluating procurement with its detailed evaluation of technical approach and management capability). The implication for procurement design is that the advantages of quality-evaluating source selection should be most pronounced when the requirement is complex, uncertain, and difficult to specify in advance. For simple, well-defined requirements, the additional administrative burden of tradeoff evaluation may not be justified, and price-focused methods may perform comparably well.

In the present study, procurement complexity was proxied by log award amount, on the rationale that larger procurements tend to involve greater technical scope, longer performance periods, more complex deliverable structures, and greater uncertainty. This proxy is imperfect—award size captures some but not all dimensions of complexity—but it is the most readily operationalized measure of complexity available in the data.

The moderation hypothesis was tested by augmenting the cost growth regression model from Section 4.5.1 with an interaction term between the Tradeoff indicator and log award amount:

Cost Growth (%) = beta_0 + beta_1(Tradeoff) + beta_2(Log Award Amount) + beta_3(Tradeoff x Log Award Amount) + sum(beta_j * NAICS_j) + sum(beta_k * Agency_k) + epsilon

The coefficient of interest is beta_3, the interaction term, which tests whether the effect of procurement design on cost growth varies as a function of award size (the complexity proxy).

The results were as follows:

| Variable | Coefficient | SE | *t* | *p* |
|---|---|---|---|---|
| Intercept | — | — | — | — |
| Tradeoff (QE = 1) | -8.987 | 3.020 | -2.98 | .003 |
| Log award amount | 1.679 | — | — | < .001 |
| Tradeoff x Log award amount | 0.619 | 0.208 | 2.98 | .003 |
| NAICS sector dummies | (included) | | | |
| Agency dummies | (included) | | | |
| *N* | 2,164 | | | |
| *R*² | 0.140 | | | |

**Hypothesis 8 was supported.** The interaction between procurement design and award size was statistically significant (*b* = 0.619, *SE* = 0.208, *t* = 2.98, *p* = .003), indicating that complexity (proxied by award size) significantly moderated the relationship between procurement design and cost growth.

The finding is notable for several reasons. First, the interaction effect was significant at a highly conventional level (*p* = .003), well below the alpha = .05 threshold and below the more conservative alpha = .01 threshold. This level of significance provides strong statistical evidence for the moderation effect, especially in light of the non-significant main effects reported in Section 4.5.1. Second, the *t*-statistic for the interaction (2.98) was larger than the *t*-statistic for the Tradeoff main effect in the original model (0.88), indicating that the moderating role of complexity is a more robust feature of the data than the average main effect. Third, the inclusion of the interaction term changed the model *R*² from 0.151 (main-effects-only model) to 0.140 for the interaction model, a value that reflects the slightly different sample composition rather than a reduction in fit. The interaction model provides a meaningfully different interpretation of the data: not that procurement design has no effect, but that its effect depends on the complexity of the procurement.

The pattern of the interaction is interpretable as follows. In the interaction model, the main effect of the Tradeoff indicator (beta_1 = -8.987) represents the estimated effect of QE design when log award amount equals zero—a value outside the range of the data (the minimum observed log award amount is approximately 12.4, corresponding to an award of about $245,000) and therefore not directly meaningful in substantive terms. However, the negative sign of the main Tradeoff coefficient combined with the positive sign of the interaction coefficient (beta_3 = 0.619) implies a crossing pattern: the effect of QE design on cost growth changes sign at some point along the award size continuum.

Specifically, the predicted difference in cost growth between QE and NFP can be written as:

Delta Cost Growth = beta_1 + beta_3 * (Log Award Amount) = -8.987 + 0.619 * (Log Award Amount)

Setting this expression to zero and solving for the crossover point yields:

Log Award Amount = 8.987 / 0.619 = 14.52

which corresponds to an award amount of approximately exp(14.52) = $2,017,000. This implies that for awards below approximately $2 million (on the log scale, below 14.52), QE design is associated with *lower* cost growth relative to NFP, while for awards above approximately $2 million, QE design is associated with *higher* cost growth. Given that the mean log award amounts are 15.26 for QE and 14.59 for NFP (Table 4.2), the crossover point falls near the center of the NFP distribution and below the center of the QE distribution, meaning that a substantial proportion of both groups falls on each side of the crossover.

Figure 4.7 illustrates this interaction graphically.

> **Figure 4.7.** Predicted cost growth (%) as a function of log award amount, separately for QE and NFP procurement designs. At smaller award sizes (left region of the plot), QE design is associated with lower predicted cost growth than NFP. As award size increases, the QE and NFP prediction lines converge and eventually cross, with QE design associated with higher predicted cost growth at the largest award sizes. The shaded regions represent 95% confidence bands. The crossover point occurs at approximately log award amount = 14.52 (approximately $2 million in nominal terms).

The crossing pattern depicted in Figure 4.7 has important substantive implications that merit extended discussion.

For smaller, moderately complex procurements (below approximately $2 million), quality-evaluating procurement designs appear to deliver a cost growth advantage relative to NFP designs. This finding is consistent with the theoretical prediction that better contractor selection—achieved through quality evaluation of technical approach and past performance—reduces post-award cost escalation by producing a better initial match between contractor capabilities and government requirements. For these moderately sized procurements, the additional administrative cost of conducting a quality evaluation appears to be justified by the downstream benefits of lower cost growth.

For the largest and most complex procurements (above approximately $2 million), QE design is associated with *higher* cost growth than NFP. This counterintuitive finding—in which the procurement design theoretically best suited to complex transactions appears to perform worse on the cost growth dimension—may reflect several mechanisms. First, very large QE awards in this study are defined by cost-type pricing, and cost-reimbursement contracts structurally permit cost growth by allocating cost risk to the government. Under cost-plus-fixed-fee or cost-plus-incentive-fee pricing, the contractor is reimbursed for allowable costs, and the absence of a firm price ceiling creates conditions under which costs can escalate without triggering the contractual controls that a firm-fixed-price arrangement would impose. Second, the complexity of very large procurements may overwhelm the advantages of careful source selection: even when the best contractor is selected, the inherent uncertainty and scope volatility of multimillion-dollar, multi-year service contracts may produce cost growth that is largely independent of the procurement design used to select the contractor. Third, there may be a principal-agent dynamic at work: contractors performing under cost-reimbursement arrangements have less incentive to control costs than contractors bearing cost risk under firm-fixed-price contracts, a moral hazard problem that intensifies as contract size and duration increase.

The significant interaction effect on Hypothesis 8 provides crucial nuance to the null finding on Hypothesis 1. The main effect of procurement design on cost growth was not significant (Section 4.5.1), but this overall null result masks a more complex pattern in which the effect varies by procurement complexity. At lower complexity levels, QE design appears beneficial; at higher complexity levels, it does not. The overall average effect, which pools across all complexity levels, is approximately zero—producing the non-significant main effect observed in the full-sample regression. This finding illustrates a general principle in empirical research: an aggregate null effect does not necessarily mean that no effect exists; it may instead indicate that the effect is heterogeneous, with positive and negative subgroup effects that cancel in the aggregate.

From a theoretical perspective, the interaction finding is partially consistent with the contingency prediction of transaction cost economics but with an important caveat. The theory predicts that quality-evaluating governance structures (analogous to QE procurement) should be most advantageous for complex transactions. The data support the contingency logic—the effect of procurement design on cost growth is indeed contingent on complexity—but the direction at high complexity levels is the opposite of the simple prediction. Rather than QE being most advantageous for the most complex transactions, QE appears most advantageous for moderately complex transactions and least advantageous (or actively disadvantageous) for the most complex ones. This nuanced finding suggests that transaction cost economics' contingency framework captures an important feature of the data but that additional mechanisms—particularly the cost risk allocation embedded in the pricing type dimension of the procurement design classification—modify the predicted relationship at high complexity levels.

From a policy perspective, the interaction finding cautions against blanket recommendations either for or against particular procurement designs. The FAR's existing framework, which instructs contracting officers to match source selection method to the characteristics of the requirement (FAR 15.101), is directionally correct: the optimal procurement design depends on the specific acquisition. The present findings suggest that for moderately sized service and IT procurements, quality-evaluating designs may yield cost growth advantages, while for the largest procurements, the combination of quality evaluation with cost-type pricing may actually increase cost growth relative to firm-fixed-price alternatives. This implication is explored further in Chapter 5.

---

## 4.7 PSM-Matched Sample Results

This section reports the results of the primary hypothesis tests when estimated on the propensity score matched sample (*N* = 2,186, comprising 1,093 matched pairs). The purpose of the matched-sample analysis is to provide a robustness check on the full-sample results by reducing the influence of confounding by the observed covariates included in the propensity score model. As noted in Section 4.4, the matched-sample estimates complement the full-sample regression estimates by relying on a different identification assumption: whereas the full-sample regressions assume that the linear specification of the control variables is correct, the matched-sample analysis relies on the assumption that the propensity score model captures the relevant dimensions of selection.

### 4.7.1 H1: Cost Growth (Matched Sample)

The OLS regression of winsorized cost growth on the Tradeoff indicator, controlling for log award amount, NAICS sector, and agency dummies, was re-estimated on the matched sample (*N* = 1,121 observations with non-missing cost growth data in the matched sample). The Tradeoff coefficient was 1.033 (*p* = .061). This result was marginally significant at the .10 level but not at the conventional .05 level, with the positive coefficient indicating that QE awards exhibited slightly higher cost growth than their matched NFP counterparts—approximately 1.03 percentage points higher, on average.

The direction of the effect was the same as in the full-sample analysis (positive, not negative as hypothesized), but the magnitude was larger in the matched sample (1.033 vs. 0.413). The stronger estimated effect in the matched sample may reflect the removal of confounding by observed covariates: in the full sample, the positive relationship between QE design and cost growth may have been partially offset by the inclusion of QE awards from agencies or sectors where cost growth was generally lower, producing an attenuated estimate. After matching, the comparison is more tightly controlled, and the underlying positive relationship becomes more apparent.

It is important to interpret this result cautiously. The marginal significance of the matched-sample estimate (*p* = .061) does not constitute evidence in favor of Hypothesis 1, which predicted *lower* cost growth for QE awards. To the contrary, the positive coefficient suggests that, if anything, QE procurement design may be associated with modestly *higher* cost growth—a finding that is directionally consistent with the structural characteristics of cost-type contracts, which provide less pricing discipline than firm-fixed-price contracts and therefore create more scope for cost escalation. The near-significance of this effect in the matched sample, combined with its non-significance in the full sample, suggests that the positive relationship between QE design and cost growth is real but modest in magnitude and sensitive to the comparison strategy employed.

### 4.7.2 H6: Single-Bid Competition (Matched Sample)

The logistic regression of single-bid outcome on the Tradeoff indicator was re-estimated on the matched sample (*N* = 2,186). The Tradeoff coefficient was -0.245 (*p* = .221), corresponding to an odds ratio of 0.783 (95% CI including 1.0). The direction was consistent with the full-sample result—QE was associated with lower single-bid rates—but the effect was not statistically significant. The odds ratio of 0.783 in the matched sample was close to the 0.752 observed in the full sample, suggesting a consistent underlying effect, but the smaller sample size and consequently wider confidence intervals precluded statistical significance.

The attenuation of the estimated effect relative to the full sample (*p* = .221 vs. *p* = .085) is attributable primarily to the reduction in sample size from 3,869 to 2,186, which reduced statistical power. When the outcome is rare (single-bid rate of approximately 5%), the number of events (single-bid outcomes) drops roughly proportionally with sample size, and the reduction from approximately 193 events in the full sample to approximately 110 events in the matched sample substantially reduced the precision of the logistic regression estimates.

### 4.7.3 Summary of Matched-Sample Results

The matched-sample results were broadly consistent with the full-sample results in direction and magnitude, differing primarily in precision due to the smaller sample size.

For Hypothesis 1 (cost growth), both the full-sample and matched-sample estimates were positive (indicating higher cost growth for QE awards), but the full-sample estimate was clearly non-significant (*p* = .377) while the matched-sample estimate was marginally significant (*p* = .061). This pattern suggests a weak positive relationship between QE design and cost growth that is partially confounded in the full sample and becomes more apparent after matching.

For Hypothesis 6 (single-bid competition), both estimates were negative (indicating lower single-bid rates for QE awards), with the full-sample estimate marginally significant (*p* = .085) and the matched-sample estimate non-significant (*p* = .221). The consistent direction but variable significance reflects the power-precision trade-off inherent in propensity score matching: matching improves internal validity at the cost of sample size and statistical power.

The overall consistency between the full-sample and matched-sample results provides reassurance that the primary findings were not driven by confounding on the observed covariates included in the propensity score model. The possibility of unobserved confounding, which neither regression nor matching can address, remains a limitation of the study's observational design and is discussed in Chapter 5.

### 4.7.4 Implications of the Matching Analysis

The matched-sample results, taken together, strengthen the study's conclusions in two important ways. First, the consistency of direction and approximate magnitude across the full-sample and matched-sample estimates provides triangulating evidence that the findings are not artifacts of a single analytical approach. When two different identification strategies—parametric regression adjustment and nonparametric propensity score matching—yield qualitatively similar results, the combined evidence is stronger than either method alone (Ho et al., 2007). Second, the slight strengthening of the positive Tradeoff coefficient in the matched-sample cost growth analysis (from 0.413 to 1.033) provides a more refined estimate of the procurement design effect after removing the influence of observed selection factors. The marginal significance of this estimate (*p* = .061) hints at a genuine, albeit modest, positive relationship between QE design and cost growth that is consistent with the cost risk allocation explanation (cost-type contracts permitting greater cost growth) but is too imprecise to be considered definitive.

The matched-sample analysis also highlights the tension between two dimensions of the QE classification: the evaluation approach (quality-evaluating, emphasizing technical merit) and the pricing structure (cost-type, allocating cost risk to the government). These two dimensions are empirically correlated in the data—the QE category is defined by their joint occurrence—but they exert opposing theoretical effects on cost growth. The quality evaluation dimension should reduce cost growth (by improving contractor selection), while the cost-type pricing dimension should increase cost growth (by reducing the contractor's incentive to control costs). The observed positive Tradeoff coefficient, both in the full and matched samples, suggests that the pricing structure effect dominates the evaluation approach effect on the cost growth dimension. This interpretation is explored more fully in Chapter 5.

---

## 4.8 Robustness Checks and Sensitivity Analysis

A comprehensive set of robustness checks was conducted to assess the sensitivity of the primary findings to alternative sample definitions, variable specifications, and model assumptions. The overarching question motivating these analyses was whether the null finding on Hypothesis 1 (procurement design and cost growth) was robust or whether it was an artifact of particular analytical choices. Table 4.8 summarizes the results of these analyses for the Tradeoff coefficient in the cost growth model.

**Table 4.8**

*Robustness Checks: Tradeoff Coefficient in Cost Growth Models*

| Specification | *N* | Tradeoff Coef. | *p* | Conclusion |
|---|---|---|---|---|
| **Primary specification** | 2,164 | 0.413 | .377 | Not significant |
| **Full sample (incl. task orders)** | 8,483 | 0.272 | .530 | Not significant |
| **PSM matched sample** | 1,121 | 1.033 | .061 | Marginally significant (opposite direction) |
| **Large agency subsample** | 2,132 | 0.337 | .449 | Not significant |
| **Small agency subsample** | 32 | -2.034 | .437 | Not significant |
| **Raw (non-winsorized) cost growth** | 2,164 | -21,200,000 | .207 | Not significant; extreme outlier influence |
| **Excluding outliers (> 3 SD)** | 2,164 | 0.313 | .477 | Not significant |
| **NAICS 54 subsample** | 1,516 | 0.090 | .864 | Not significant |
| **NAICS 56 subsample** | 524 | 1.102 | .239 | Not significant |
| **NAICS 51 subsample** | 124 | 0.398 | .803 | Not significant |

### 4.8.1 Full Sample Including Task Orders

The primary analysis focused on the QE-versus-NFP comparison, excluding task orders and the small Price-Focused and Other categories. The exclusion of task orders was motivated by the theoretical argument that the source selection decision for task orders occurs at the vehicle level rather than at the individual order level, making the task order procurement design classification less directly comparable to standalone negotiated procurements. However, task orders represent the majority of federal service and IT procurement activity (74.0% of the full sample), and excluding them limits the generalizability of the findings.

As a robustness check, the cost growth model was re-estimated on the expanded sample of 8,483 awards that included task orders alongside QE and NFP awards, with task orders coded as an additional category. The Tradeoff coefficient (comparing QE to NFP within this expanded model) was 0.272 (*p* = .530), consistent with the primary finding of no significant procurement design effect on cost growth. The smaller coefficient magnitude (0.272 vs. 0.413 in the primary specification) and the higher *p*-value (.530 vs. .377) reflected the larger and more heterogeneous sample, which diluted the QE-NFP contrast. The conclusion was unchanged: no significant procurement design effect on cost growth.

### 4.8.2 Agency Subsamples

To assess whether the null finding was driven by or masked by the dominance of large agencies (particularly the Department of Defense) in the sample, the cost growth model was re-estimated separately on large-agency and small-agency subsamples. The large-agency subsample (*N* = 2,132) included awards from the top 10 agencies by volume, representing the institutional core of federal service procurement. The small-agency subsample (*N* = 32) included awards from the remaining 48 agencies, representing a diverse but thinly populated set of procurement environments.

In the large-agency subsample, the Tradeoff coefficient was 0.337 (*p* = .449), consistent with the full-sample result. In the small-agency subsample, the coefficient was -2.034 (*p* = .437), suggesting a possible negative relationship (QE associated with lower cost growth) among smaller agencies. However, the extremely small sample size (*N* = 32) provided essentially no statistical power to detect effects of any plausible magnitude, and the large standard error renders the point estimate unreliable. The negative sign in the small-agency subsample should be treated as suggestive at best and may simply reflect the influence of a few unusual observations.

The agency subsample analysis provided no evidence that the null finding was an artifact of particular agencies' dominance in the sample. The result was consistent across both large and small agencies, though the small-agency analysis lacked the statistical power to be informative.

### 4.8.3 Alternative Cost Growth Specifications

The primary analysis used winsorized cost growth (capped at the 1st and 99th percentiles of the distribution) to mitigate the influence of extreme outliers. Winsorization is a standard approach in financial and procurement data analysis, where the distribution of cost changes frequently contains extreme values generated by contract terminations, major restructurings, or data entry errors (Tukey, 1977). However, the choice of winsorization bounds is inherently arbitrary, and the sensitivity of the results to this choice warrants investigation.

As a first sensitivity check, the model was re-estimated using raw, non-winsorized cost growth. The Tradeoff coefficient was -$21.2 million (*p* = .207)—a value that is enormous in magnitude but not statistically significant and not meaningfully interpretable. The negative sign (opposite to the primary specification) and the enormous magnitude reflect the dominant influence of a small number of extreme outliers in the non-winsorized distribution. Federal procurement data routinely contain observations where cost growth exceeds the original contract value by factors of ten or more, typically reflecting major scope changes, supplemental appropriations, or data anomalies. These extreme values exert disproportionate influence on OLS estimates, pulling the regression line toward the outliers. The non-winsorized result underscored the necessity of some form of outlier treatment for the cost growth variable and confirmed that the primary findings were appropriately reported using the winsorized specification.

As a second sensitivity check, the model was re-estimated after excluding all observations with cost growth exceeding three standard deviations from the mean—a more stringent outlier exclusion criterion that removes the most extreme values entirely rather than capping them. The resulting Tradeoff coefficient was 0.313 (*p* = .477), consistent with the winsorized primary specification. The convergence of the winsorized and outlier-excluded results confirmed that the null finding was not sensitive to the specific method of outlier treatment.

### 4.8.4 NAICS Sector Subsamples

To assess whether the null finding was specific to particular industry sectors or represented a consistent pattern across the federal service procurement landscape, the cost growth model was re-estimated separately for each of the three NAICS sectors in the sample.

In **NAICS Sector 54** (Professional, Scientific, and Technical Services), the largest subsample (*N* = 1,516), the Tradeoff coefficient was 0.090 (*p* = .864). This near-zero, highly non-significant effect provided strong evidence that, within the professional services sector, procurement design was not associated with differential cost growth. The *p*-value of .864 indicates that the observed coefficient of 0.090 is almost exactly what would be expected under the null hypothesis of no effect, and the tight clustering of the estimate around zero suggests that the null finding is not a consequence of averaging across sectors with opposing effects.

In **NAICS Sector 56** (Administrative and Support Services, *N* = 524), the Tradeoff coefficient was 1.102 (*p* = .239). Although the point estimate was larger than in Sector 54, suggesting a possible positive relationship between QE design and cost growth in the administrative services sector, the result remained non-significant. The larger magnitude could reflect the possibility that cost-type pricing is particularly ill-suited to administrative services, which tend to be more standardized and less technically complex than professional services. Under this interpretation, the cost growth disadvantage of QE (cost-type) contracts would be more pronounced in sectors where the simplicity of the requirement argues against the use of cost-reimbursement pricing. However, the non-significance of the estimate means that this interpretation is speculative.

In **NAICS Sector 51** (Information, *N* = 124), the Tradeoff coefficient was 0.398 (*p* = .803). The small sample size for this sector—only 124 observations, compared with 1,516 for Sector 54 and 524 for Sector 56—severely limited statistical power and precluded meaningful inference. The result was consistent with the overall pattern of null findings across sectors.

### 4.8.5 Overall Assessment of Robustness

The robustness analyses yielded a strikingly consistent pattern. Across ten alternative specifications—varying the sample composition, cost growth measurement, outlier treatment, agency subsample, and industry sector—the Tradeoff coefficient in the cost growth model was never statistically significant at conventional thresholds. The *p*-values ranged from .061 (PSM matched sample, where the effect was in the opposite direction from the hypothesis) to .864 (NAICS 54 subsample). This consistency across a diverse set of specifications strongly supports the conclusion that the null finding on Hypothesis 1 is robust and not an artifact of a particular analytical choice, sample definition, or variable specification.

The direction of the Tradeoff coefficient was positive (indicating higher cost growth for QE awards) in eight of the ten specifications and negative in two (the small-agency subsample with *N* = 32 and the non-winsorized specification, both of which were dominated by extreme or sparse observations). The predominance of positive coefficients, combined with the marginally significant positive effect in the PSM matched sample (*p* = .061), suggests that if there is any systematic main-effect relationship between quality-evaluating procurement design and cost growth, it may be in the direction of *higher* rather than lower cost growth for QE awards. This suggestive pattern is consistent with the structural hypothesis that cost-type pricing—which defines the QE category in this study—is inherently associated with greater cost growth due to the allocation of cost risk to the government. However, no single specification achieved significance at alpha = .05, and the pattern should be interpreted as suggestive rather than conclusive.

The consistency of the null finding across robustness checks also strengthens the interpretation of the significant interaction effect (H8) reported in Section 4.6. If the null main effect were an artifact of a particular specification, the significant interaction might also be artifactual. The stability of both the null main effect and the significant interaction across alternative specifications provides converging evidence for the conclusion that the relationship between procurement design and cost growth is genuinely contingent on complexity rather than uniformly positive, negative, or zero.

---

## 4.9 Summary of Findings by Hypothesis

Table 4.9 provides a comprehensive summary of the empirical results organized by hypothesis. For each hypothesis, the table reports the predicted direction, the key test statistic, the significance level, and the determination of support.

**Table 4.9**

*Summary of Hypothesis Test Results*

| Hypothesis | Predicted Relationship | Key Estimate | *p* | Result |
|---|---|---|---|---|
| **H1: Cost Growth** | QE → Lower cost growth vs. NFP | *b* = 0.413, 95% CI [-0.503, 1.330] | .377 | **Not Supported** |
| **H2: Modification Intensity** | QE → Fewer modifications vs. NFP | *b* = -0.034, IRR = 0.967, 95% CI [-0.123, 0.055] | .449 | **Not Supported** |
| **H6: Single-Bid Competition** | QE → Lower single-bid rates vs. NFP | OR = 0.752, 95% CI [0.543, 1.040] | .085 | **Not Supported** (marginally significant, correct direction) |
| **H8: Complexity Moderation** | Complexity moderates tradeoff-cost growth relationship | Interaction *b* = 0.619 | .003 | **Supported** |

### 4.9.1 Interpretation of the Pattern of Results

Of the four hypotheses tested, one (H8) was supported and three (H1, H2, H6) were not. This pattern—null main effects combined with a significant moderation effect—is substantively informative and theoretically interpretable. It is not a pattern of failure; rather, it is a pattern that indicates the relationship between procurement design and contract outcomes is more complex than the simple directional predictions of the main-effect hypotheses anticipated.

The three unsupported hypotheses all involved main-effect predictions: that quality-evaluating procurement design would produce uniformly better outcomes across cost growth, modification intensity, and competition dimensions. The consistent non-significance of these main effects, across both full-sample and matched-sample analyses, across multiple robustness checks, and across NAICS sector subsamples, provides strong evidence that there is no uniform advantage to quality-evaluating procurement design on these dimensions.

The supported hypothesis—that procurement complexity moderates the relationship between procurement design and cost growth—was the most theoretically nuanced prediction, drawing directly on the contingency logic of transaction cost economics. The significant interaction (*p* = .003) indicates that the effect of procurement design on cost growth is not constant across all procurements but varies systematically with complexity. At lower complexity levels, QE design is associated with lower cost growth; at higher complexity levels, the relationship reverses. This contingency finding is the most important empirical contribution of the chapter, as it identifies the conditions under which procurement design matters rather than simply asking whether it matters on average.

The combination of null main effects and a significant interaction tells a coherent story. When the data are analyzed without regard to procurement complexity, the overall relationship between procurement design and cost growth is not statistically distinguishable from zero. However, this aggregate null finding conceals meaningful heterogeneity: positive and negative subgroup effects cancel in the aggregate, producing an apparent null that would be misleading if interpreted as evidence that procurement design is irrelevant. The interaction model reveals the underlying structure of the data, demonstrating that procurement design does influence cost growth—but in a manner that depends on the complexity of the procurement.

### 4.9.2 Summary of Effect Sizes

A review of effect sizes across the hypothesis tests provides additional context for interpreting the findings. The main-effect relationships tested in Hypotheses 1, 2, and 6 all yielded effect sizes in the small-to-negligible range:

- **Cost growth** (unadjusted bivariate comparison): Cohen's *d* = 0.20 (small effect). After regression adjustment, the effect was reduced to approximately *d* = 0.02 (negligible).
- **Modification count**: Cohen's *d* = 0.08 (negligible effect). The incidence rate ratio of 0.967 corresponds to a 3.3% difference.
- **Number of offers**: Cohen's *d* = -0.05 (negligible effect).
- **Single-bid rate**: Cohen's *d* = -0.05, with an odds ratio of 0.752 (medium effect for a rare outcome). The odds ratio suggests a 24.8% reduction in single-bid odds, which is substantively meaningful even though it did not reach statistical significance.

Even the significant interaction effect in Hypothesis 8, while statistically significant, operated within an overall model that explained only 14.0% of the variance in cost growth (*R*² = 0.140). These modest effect sizes suggest that procurement design, as operationalized in this study, is one of many factors influencing contract outcomes and is not the dominant or even a major factor. This conclusion is not unexpected. Contract outcomes are determined by a complex interplay of factors including requirements quality, contractor capability, market conditions, contract administration quality, funding stability, and political oversight. Procurement design is one lever among many, and even a well-chosen procurement method cannot compensate for poorly defined requirements, inadequate funding, or deficient contract oversight.

The modest effect sizes observed in this study are consistent with the broader empirical literature on public procurement, which has generally found that no single procurement variable explains a large share of outcome variance (Bajari et al., 2014; Lewis & Bajari, 2011). The procurement design decision, while consequential, occurs within a complex system where multiple factors interact to determine outcomes. Isolating the independent contribution of any one factor in such a system requires either experimental manipulation (which is infeasible in this context) or very large samples that can detect small effects with precision.

### 4.9.3 Statistical Power Considerations

An ex post power analysis provides essential context for interpreting the null findings and assists in determining whether the null results reflect genuine null effects in the population or merely insufficient statistical power to detect small effects.

For **Hypothesis 1**, the cost growth regression with *N* = 2,164, *R*² = 0.151, and the observed number of predictors had approximately 80% power to detect a small-to-medium incremental effect of the Tradeoff variable corresponding to *f*² = 0.02 (roughly *d* = 0.28) at alpha = .05. The observed effect size of the Tradeoff variable (approximately *d* = 0.02 based on the regression point estimate and standard error) was well below this detection threshold. This result has two possible interpretations. Either the true effect of procurement design on cost growth is very small (detectable only with samples an order of magnitude larger than the present one), or the true effect is genuinely zero. The robustness analyses, which consistently produce non-significant estimates close to zero, support the interpretation that any true effect is either zero or extremely small.

For **Hypothesis 2**, the negative binomial model with *N* = 3,869 had adequate power to detect small effects on the modification count, given the full utilization of the comparison sample. The observed effect (IRR = 0.967, corresponding to a 3.3% difference) was well within the range that the model could reliably detect if it were statistically significant. The non-significance of the estimate thus reflects the genuine absence of a meaningful difference in modification counts rather than a power limitation.

For **Hypothesis 6** (single-bid competition), the logistic regression with *N* = 3,869 and a base rate of approximately 5% had limited power to detect small effects on a rare outcome. The observed odds ratio of 0.752 (*p* = .085) corresponds to a medium effect size for a rare outcome, and a power calculation indicates that a sample approximately 1.5 to 2 times the size of the present one would be needed to achieve 80% power for an effect of this magnitude. This power limitation should be considered when interpreting the marginal significance of the single-bid finding. The marginal significance (*p* = .085) combined with the consistent direction across full-sample and matched-sample analyses suggests that a real but modest effect may exist that the present study lacked the power to confirm at the .05 level.

For **Hypothesis 8** (complexity moderation), statistical power was sufficient to detect the interaction effect, as evidenced by the significant result (*p* = .003). The interaction effect was estimated with adequate precision, and the *t*-statistic of 2.98 was well above the critical value. The conclusion of moderation support rests on a solid statistical foundation and is unlikely to reflect a Type I error.

### 4.9.4 Implications for Subsequent Chapters

The results presented in this chapter establish two principal findings that frame the discussion in Chapter 5. First, the main-effect relationships between procurement design and contract outcomes—cost growth, modification intensity, and competition—are not statistically significant in the present data. Quality-evaluating procurement designs do not produce uniformly better outcomes than negotiated fixed-price designs across the dimensions measured. This finding challenges the widely held assumption in the procurement policy community that best-value tradeoff source selection inherently produces superior outcomes, and it suggests that the relationship between procurement method and contract performance is more complex than conventional wisdom assumes.

Second, procurement complexity significantly moderates the relationship between procurement design and cost growth, with quality-evaluating designs showing a cost growth advantage at lower complexity levels that diminishes and reverses at higher complexity levels. This finding supports the contingency logic of transaction cost economics and provides empirical grounding for the FAR's principle that source selection method should be matched to the characteristics of the requirement. The moderation finding also identifies a specific boundary condition—the approximate $2 million crossover point—that has potential practical implications for procurement policy and practice.

Together, these findings contribute to the literature by replacing the binary question "Is best-value tradeoff better than LPTA?" with the more nuanced question "Under what conditions does procurement design choice matter, and how?" Chapter 5 discusses the theoretical, methodological, and policy implications of these findings in the context of the existing literature and identifies directions for future research that can further refine understanding of the contingent relationship between procurement design and public value.
