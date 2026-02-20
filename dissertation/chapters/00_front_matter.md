# Front Matter

---

## Title Page

&nbsp;

**FROM LOWEST PRICE TO HIGHEST PUBLIC VALUE:**
**AN EMPIRICAL TEST OF BEST-VALUE SOURCE SELECTION IN GOVERNMENT RFPs**

&nbsp;

A Dissertation Presented to
the Faculty of the Daniels College of Business
University of Denver

&nbsp;

In Partial Fulfillment
of the Requirements for the Degree of
Doctor of Philosophy

&nbsp;

Richard W. Davidson

[Month] 2026

&nbsp;

Advisor: [Committee Chair Name TBD]

---

## Abstract

Federal procurement policy has long debated the relative merits of lowest-price technically acceptable (LPTA) and best-value tradeoff (BVT) source selection methods, yet empirical evidence on their differential post-award outcomes remains limited. This dissertation examines whether quality-evaluating (best-value tradeoff) source selection in federal procurement produces superior public value outcomes compared to price-focused (LPTA) approaches. Drawing on public value theory, transaction cost economics, and principal-agent theory, the study develops and tests a conceptual model linking procurement design choices to measurable contract performance indicators.

The research employs a quasi-experimental archival design, analyzing 15,477 competitive service and information technology contract awards exceeding $250,000 from USAspending.gov for fiscal year 2024. Procurement design is operationalized as a binary treatment variable distinguishing quality-evaluating awards from price-focused awards. Outcome variables include cost growth (percentage change from initial to current award value), modification intensity (count of contract modifications), and competition level (single-bid indicator). Analytical methods include ordinary least squares regression, negative binomial generalized linear modeling, logistic regression, and propensity score matching to address selection bias inherent in observational procurement data.

Results reveal three principal findings. First, no statistically significant main effect of procurement design on cost growth was detected (H1 not supported, *p* = 0.377), nor on modification intensity (H2 not supported, *p* = 0.449). Second, a marginally significant reduction in single-bid rates was observed under quality-evaluating design (OR = 0.752, *p* = 0.085), suggesting that evaluation criteria emphasizing technical merit may modestly enhance competitive participation. Third, award complexity significantly moderates the procurement design-performance relationship (H8 supported, interaction *p* = 0.003), with quality-evaluating design demonstrating benefits primarily for smaller, less complex procurements.

These findings indicate that source selection method alone may be insufficient to drive post-award contract outcomes. Contract management capacity, requirements definition quality, and oversight intensity may exert greater influence on performance than the initial evaluation framework. The complexity moderation finding suggests that procurement policy should adopt context-sensitive, rather than one-size-fits-all, approaches to source selection method prescription.

*Keywords:* public procurement, source selection, best value, LPTA, public value, federal contracting, propensity score matching

---

## Acknowledgments

I wish to express my sincere gratitude to the faculty and staff of the Daniels College of Business at the University of Denver, whose commitment to rigorous scholarship and practitioner-relevant research shaped this work at every stage. I am especially grateful to [Committee Chair Name TBD], my dissertation committee chair, and to the members of my committee for their sustained guidance, intellectual challenge, and generous investment of time throughout this process.

I owe a considerable debt to the federal acquisition community -- the contracting officers, program managers, and policy professionals whose daily work inspired this research. Over more than 25 years in government contracting, I have been privileged to observe the complexities of public procurement firsthand, and it is the dedication and professionalism of this community that motivated my inquiry into how procurement design choices affect public value.

I am grateful to the Executive PhD cohort at Daniels College of Business for the camaraderie, candid feedback, and shared resolve that sustained us through the demands of doctoral study alongside professional careers. The intellectual companionship of fellow scholar-practitioners enriched this dissertation in ways that transcend any single citation.

Finally, and most importantly, I thank my family for their unwavering patience, encouragement, and sacrifice. The pursuit of a doctoral degree while maintaining professional obligations exacts a toll that extends well beyond the scholar, and I am profoundly grateful for the support that made this achievement possible.

---

## Table of Contents

| Section | Page |
|---|---|
| Abstract | ii |
| Acknowledgments | iv |
| Table of Contents | v |
| List of Tables | vii |
| List of Figures | viii |
| | |
| **Chapter 1: Introduction** | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.1 Background and Context | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.2 Statement of the Problem | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.3 Purpose of the Study | 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.4 Research Questions and Hypotheses | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.5 Significance of the Study | 10 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.6 Definitions of Key Terms | 12 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.7 Scope and Delimitations | 14 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.8 Organization of the Dissertation | 15 |
| | |
| **Chapter 2: Literature Review and Hypotheses** | 16 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.1 Theoretical Foundations | 16 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.1 Public Value Theory | 17 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.2 Transaction Cost Economics | 20 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.3 Principal-Agent Theory | 23 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2 Federal Procurement Policy and Source Selection | 26 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.1 Regulatory Framework | 26 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.2 LPTA vs. Best-Value Tradeoff | 29 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2.3 Legislative and Policy Evolution | 32 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.3 Empirical Evidence on Procurement Outcomes | 35 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.1 Cost Growth and Contract Modifications | 35 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.2 Competition and Market Participation | 38 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3 Performance Quality and Satisfaction | 41 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.4 Moderating and Contextual Factors | 43 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.5 Conceptual Model and Hypotheses | 46 |
| | |
| **Chapter 3: Methodology** | 50 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.1 Research Design | 50 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.2 Data Sources and Population | 52 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3 Sample Selection and Inclusion Criteria | 54 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.4 Variable Operationalization | 56 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.1 Independent Variable: Procurement Design | 56 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.2 Dependent Variables | 58 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.3 Control Variables | 60 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.4.4 Moderating Variables | 62 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.5 Analytical Methods | 63 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.1 OLS Regression | 63 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.2 Negative Binomial GLM | 64 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.3 Logistic Regression | 65 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.5.4 Propensity Score Matching | 66 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.6 Assumptions and Diagnostics | 68 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.7 Ethical Considerations | 70 |
| | |
| **Chapter 4: Results** | 71 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.1 Sample Description | 71 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.2 Descriptive Statistics | 73 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.3 Propensity Score Matching Results | 76 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.4 Hypothesis Tests | 79 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.1 Cost Growth (H1) | 79 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.2 Modification Intensity (H2) | 81 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.3 Single-Bid Indicator (H6) | 83 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.4.4 Moderation by Award Complexity (H8) | 85 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.5 Robustness Checks | 87 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6 Summary of Findings | 89 |
| | |
| **Chapter 5: Discussion and Conclusions** | 91 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1 Summary of Results | 91 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.2 Interpretation of Findings | 93 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.3 Theoretical Implications | 97 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4 Practical and Policy Implications | 100 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.5 Limitations | 103 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.6 Directions for Future Research | 105 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.7 Conclusion | 107 |
| | |
| **References** | 109 |
| | |
| **Appendices** | |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix A: Variable Definitions and Data Dictionary | 125 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix B: USAspending.gov Data Fields and Extraction Protocol | 128 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix C: Procurement Design Classification Criteria | 131 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix D: Propensity Score Model Specification | 133 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix E: Additional Robustness Check Results | 135 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix F: Sensitivity Analyses | 138 |
| &nbsp;&nbsp;&nbsp;&nbsp;Appendix G: IRB Determination Letter | 141 |

---

## List of Tables

| Table | Title | Page |
|---|---|---|
| Table 4.1 | Sample Composition by Procurement Design Category | 72 |
| Table 4.2 | Descriptive Statistics for Key Variables | 74 |
| Table 4.3 | Treatment vs. Control Group Comparison | 75 |
| Table 4.4 | Propensity Score Matching Balance Diagnostics | 77 |
| Table 4.5 | OLS Regression Results for Cost Growth (H1) | 80 |
| Table 4.6 | Negative Binomial GLM Results for Modification Intensity (H2) | 82 |
| Table 4.7 | Logistic Regression Results for Single-Bid Indicator (H6) | 84 |
| Table 4.8 | Robustness Check Results | 88 |
| Table 4.9 | Summary of Hypothesis Test Results | 90 |

---

## List of Figures

| Figure | Title | Page |
|---|---|---|
| Figure 2.1 | Conceptual Model | 47 |
| Figure 4.1 | Distribution of Awards by Procurement Design Category | 71 |
| Figure 4.2 | Distribution of Award Amounts by Procurement Design | 73 |
| Figure 4.3 | Cost Growth Distribution by Procurement Design | 79 |
| Figure 4.4 | Single-Bid Rate by Procurement Design Category | 83 |
| Figure 4.5 | Distribution of Number of Offers Received | 84 |
| Figure 4.6 | Propensity Score Distribution Before and After Matching | 76 |
| Figure 4.7 | Covariate Balance Before and After Matching | 78 |
| Figure 4.8 | Marginal Effect of Quality-Evaluating Design by Award Size | 86 |

---
