---
title: "Key Findings"
description: "Principal findings from the analysis of 654,307 federal contract awards"
weight: 4
---

<div class="findings-hero">
<div class="findings-stat"><div class="findings-stat-number">654,307</div><div class="findings-stat-label">Awards Analyzed</div></div>
<div class="findings-stat"><div class="findings-stat-number">42.5M</div><div class="findings-stat-label">FPDS Transactions</div></div>
<div class="findings-stat"><div class="findings-stat-number">FY2017-2023</div><div class="findings-stat-label">Time Period</div></div>
<div class="findings-stat"><div class="findings-stat-number">5,277x</div><div class="findings-stat-label">Larger Than Prior Research</div></div>
</div>

---

## 1. The Evidence Gap

Prior to this research, only one peer-reviewed empirical study had directly compared LPTA and tradeoff outcomes using U.S. federal contract-level data: Landale et al. (2017), with a sample of just 124 contracts. A scoping review of 87 relevant works across procurement economics, public administration, auction theory, and defense acquisition confirmed that procurement policy affecting hundreds of billions of dollars annually rested on an evidence base that would be considered wholly inadequate in any adjacent policy domain.

<div class="result-box">
<strong>This research:</strong> N = 654,307 competitively awarded contracts -- 5,277 times larger than the only prior study. Drawn from the Omari et al. (2025) comprehensive FPDS dataset covering 42.5 million transactions.
</div>

---

## 2. Section 813 Effect on Contract Outcomes

A difference-in-differences design exploiting NDAA Section 813 as a natural experiment yields the following baseline estimates:

<div class="result-box">
<strong>Cost Growth:</strong> DoD contracts experienced a 30.35-percentage-point reduction in cost growth relative to civilian contracts after policy implementation (p < .001, N = 654,307). However, pre-trend F-tests reject parallel trends for cost growth -- DoD was already converging toward civilian cost levels before Section 813 took effect. Five correction approaches yield a preferred range of <strong>13 to 21 percentage points</strong>.
</div>

<div class="result-box">
<strong>Modifications:</strong> DoD contracts experienced 0.55 fewer modifications per award relative to civilian contracts post-treatment (p < .001, N = 654,307).
</div>

<div class="result-box">
<strong>Missing Mechanism:</strong> No evidence that DoD's source selection composition diverged from civilian agencies in the post-treatment period. DoD's post-period LPTA usage rate (39.8%) remained comparable to civilian agencies (38.8%), and tradeoff adoption was actually lower in DoD (16.4%) than in civilian agencies (19.0%). The policy effect appears real but did not operate through its intended mechanism.
</div>

---

## 3. Transaction Cost Moderation

Transaction cost economics correctly predicts when evaluation method matters most. Interaction models within the DiD framework show:

<div class="result-box">
<strong>Contract Size:</strong> The policy effect on cost growth is 48.15 percentage points for small contracts (below median) versus 27.14 percentage points for large contracts (above median) -- nearly twice as large for smaller awards where governance design is more consequential.
</div>

<div class="result-box">
<strong>Industry Sector:</strong> The effect is concentrated in restricted professional and scientific service categories (NAICS 51, 54) where asset specificity is highest: 40.56 percentage points versus 34.63 for unrestricted categories (NAICS 56).
</div>

<div class="result-box">
<strong>Pricing Structure:</strong> The effect is substantially larger for cost-reimbursement contracts than firm-fixed-price, consistent with TCE predictions about uncertainty and behavioral risk.
</div>

---

## 4. The Competition Paradox

<div class="result-box">
<strong>Prevalence:</strong> 41% of ostensibly competitive federal service and IT awards received only one offer -- classified as "competitive" under FAR despite having no actual price or quality competition.
</div>

<div class="result-box">
<strong>Descriptive Association:</strong> Contracts evaluated using tradeoff criteria are 3.5 times more likely to receive a single bid than LPTA awards. However, this association should not be interpreted causally -- source selection method is endogenous to contract characteristics that independently affect competition.
</div>

<div class="result-box">
<strong>DiD Evidence:</strong> Restricting LPTA in DoD slightly increased single-bid probability (logit coefficient = 0.051, p < .001 with robust SEs). With agency-clustered standard errors, the effect becomes non-significant (p = 0.288), suggesting the result is driven by within-agency correlation.
</div>

---

## 5. International Comparison

<div class="result-box">
<strong>Entry Cost Differential:</strong> An 87-fold differential in qualification costs between the most restrictive system (United States: $6,800-$516,000) and the least restrictive (Chile: $425-$5,800). Brazil's reverse auction model produces per-bid costs 160-270 times lower than the US.
</div>

<div class="result-box">
<strong>Digital Infrastructure:</strong> Every system achieving qualification costs below $15,000 operates a full end-to-end digital procurement platform. Digital infrastructure shows the strongest association with low barriers.
</div>

<div class="result-box">
<strong>Best-Value Correlation:</strong> Best-value evaluation mandates correlate with simpler entry requirements internationally -- suggesting barrier reduction may be more consequential than evaluation method reform.
</div>

---

## 6. COVID Robustness

<div class="result-box">
<strong>Stability:</strong> Dropping FY2020 entirely barely changes the main results. Cost growth DiD estimate: -29.87 (excluding FY2020) versus -30.35 (full sample). Modification count: -0.553 versus -0.555. The core findings are not driven by COVID-era contracting anomalies.
</div>

---

<div class="caveat-box">
<h4>Important Caveats</h4>
<ul>
<li>Parallel trends violation detected -- pre-treatment trends were already converging</li>
<li>Agency-clustered standard errors attenuate some results (single-bid effect becomes non-significant)</li>
<li>Source selection mechanism unclear -- no detectable first-stage compliance shift</li>
<li>Cost growth measure includes planned option exercises, not just overruns</li>
<li>CPARS performance data legally inaccessible -- using FPDS proxy measures</li>
</ul>
</div>
