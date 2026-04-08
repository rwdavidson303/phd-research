# When Does Method Matter? Source Selection Decision-Making and Contract Outcomes in Federal Procurement

## A DBA Research Proposal (Revised)

**Richard Davidson**
**Indiana University, Kelley School of Business**
**DBA Program**
**March 2026**

---

## Abstract

Public procurement increasingly involves complex, technology-intensive systems whose performance affects citizen welfare, service continuity, and taxpayer value. This proposal investigates a central question in procurement policy: when and why does the source selection method -- lowest price technically acceptable (LPTA) versus best-value tradeoff -- matter for contract outcomes, and when does it not?

The study builds on a completed large-scale quantitative pilot (N = 15,477 federal contract awards; 3,869 primary comparison sample) that produced a striking pattern of results: no significant main effects of source selection method on cost growth (p = .377) or contract modifications (p = .449), but a highly significant complexity moderation finding (p = .003) showing that method matters for smaller procurements but not larger ones. These findings challenge the prevailing policy assumption -- embedded in NDAA Section 813 and OFPP guidance -- that tradeoff evaluation consistently produces superior outcomes.

The null main effects cannot be explained by archival data alone. They demand qualitative investigation into the mechanisms, contextual factors, and practitioner reasoning that shape both the choice of method and the downstream dynamics of contracts. This dissertation employs a qualitative multiple-case study of five federal agency procurement offices, incorporating semi-structured interviews with 30-40 participants from both the government and vendor sides of the procurement relationship. The study integrates transaction cost economics, public value theory, institutional theory, and Kelman's process quality thesis to explain how organizational factors, workforce competence, and institutional norms determine whether formal source selection method matters for outcomes.

This revised proposal reflects a methodological pivot from the originally planned mixed-methods design. The quantitative analysis, completed prior to program enrollment, serves as the empirical foundation for qualitative inquiry -- a sequential explanatory design where quantitative findings inform the design, sampling, and research questions of the qualitative study.

---

## 1. Introduction

### 1.1 The Policy Puzzle

The United States federal government obligates over $700 billion annually in contracts with private-sector firms, funding systems ranging from veterans' disability claims processing to cybersecurity infrastructure to cloud computing platforms. The method by which the government selects contractors is one of the most consequential design choices in the procurement process. Under the Federal Acquisition Regulation (FAR), agencies may award contracts using either Lowest Price Technically Acceptable (LPTA) evaluation, where price is decisive among proposals meeting minimum acceptability thresholds, or best-value tradeoff evaluation, where agencies weigh price against non-price factors such as technical merit, past performance, and management approach (FAR 15.101-1, 15.101-2).

Congress, oversight bodies, and procurement reformers have increasingly argued that LPTA is overused and produces inferior outcomes. The 2017 National Defense Authorization Act (NDAA), Section 813, restricted LPTA use for DoD acquisitions in knowledge-based services, cybersecurity, and life-cycle cost-sensitive procurements. The Office of Federal Procurement Policy (OFPP) has issued guidance encouraging best-value approaches for complex acquisitions. These policy interventions rest on an empirical assumption: that tradeoff evaluation produces measurably better contract outcomes than LPTA.

This assumption has never been rigorously tested at scale. Until now.

### 1.2 What the Data Actually Show

Prior to entering the Kelley DBA program, I conducted the largest-sample quasi-experimental analysis of source selection method effects on federal contract outcomes to date. Using 15,477 competitive service and IT contract awards from USAspending.gov (FY2024 Q2), I tested whether Quality-Evaluating (QE) procurement design produces superior outcomes compared to Negotiated Fixed-Price (NFP) design, employing OLS regression, negative binomial GLM, logistic regression, and propensity score matching (1,093 matched pairs).

The results were unexpected:

| Hypothesis | Outcome | Result | p-value | Effect Size |
|-----------|---------|--------|---------|-------------|
| H1: Cost Growth | QE reduces cost growth vs. NFP | Not supported -- null | .377 | d = 0.02 |
| H2: Modifications | QE reduces contract modifications | Not supported -- null | .449 | IRR = 0.967 |
| H6: Competition | QE reduces single-bid rates | Not supported (marginal) | .085 | OR = 0.752 |
| H8: Complexity Moderation | Award size moderates method effect | **Supported** | **.003** | Crossover at ~$2M |

The complexity moderation finding (H8) is the study's most significant contribution. The interaction model revealed a crossover pattern: below approximately $2 million in award value, QE design was associated with lower cost growth (consistent with theory). Above $2 million, the effect reversed -- QE was associated with higher cost growth. This reversal is theoretically puzzling: transaction cost economics predicts that the tradeoff advantage should *increase* with complexity, not disappear.

Six additional hypotheses from the original proposal were untestable because they required data that archival procurement databases do not contain: practitioner decision rationale (H3), protest system effects (H4), oversight layer impacts (H5), competition mediation (H7), protest dual effects (H9), and standardized guidance effects (H10). These untestable hypotheses are precisely the ones that require qualitative investigation.

### 1.3 The Qualitative Imperative

The quantitative pilot established **what** happens at the aggregate level: source selection method alone does not predict contract cost performance. But it cannot explain **why**. The path from "what" to "why" requires direct engagement with the people who make and experience these decisions -- the contracting officers who choose between LPTA and tradeoff, the program managers who live with the consequences, and the vendors who invest millions in proposals only to compete against evaluation criteria they may or may not believe are meaningful.

Five specific interpretations from the quantitative findings demand qualitative investigation:

1. **The quality floor hypothesis:** Federal procurement already screens for contractor quality through mechanisms other than source selection -- responsibility determinations, past performance databases, security clearances, capability demonstrations. These mechanisms may reduce the marginal contribution of evaluation method, compressing the outcome difference between LPTA and tradeoff.

2. **The institutional isomorphism hypothesis:** Federal agencies adopt similar governance practices, oversight structures, and contract administration routines regardless of formal evaluation method. The institutional environment homogenizes outcomes even when the formal method differs.

3. **The crossover puzzle:** Why does the tradeoff advantage reverse above approximately $2 million? Possible explanations include organizational/political complexity (more stakeholders, more oversight), evaluation resource constraints (tradeoff evaluations become less rigorous at scale), or differential scope evolution dynamics.

4. **The scope evolution distinction:** Cost growth in tradeoff contracts may reflect legitimate scope evolution (the government got more value) rather than performance failure. Only practitioners can distinguish between these.

5. **The Kelman hypothesis:** The quality of the procurement *process* -- the skill, judgment, and effort of the acquisition workforce -- is more consequential than the formal evaluation method. This is fundamentally a question about human behavior and organizational practice.

These are "how" and "why" questions within a real-world context -- precisely the domain where case study research excels (Yin, 2018).

### 1.4 Purpose of This Study

This qualitative case study investigates the mechanisms, contextual factors, and practitioner reasoning that shape source selection decisions and their consequences in federal procurement. It examines the question from both sides of the procurement relationship -- government and vendor -- to build a comprehensive understanding of how source selection method interacts with organizational, institutional, and market factors to produce contract outcomes.

The study addresses the central puzzle surfaced by the quantitative evidence: if source selection method does not determine aggregate outcomes, what does? And under what conditions does method choice genuinely matter?

---

## 2. Researcher Positionality and Practical Motivation

I have spent more than twenty-five years working with government procurement, including roles inside government and on the vendor side, where I have led proposal strategy and written or managed more than twenty major technology RFP responses. I have seen procurements slowed by protests, appeals, oversight reviews, and post-award negotiations. I have watched LPTA awards produce excellent outcomes when the requirements were clear and the market was competitive. I have also watched LPTA awards produce costly failures when the government specified minimum acceptability thresholds that were too low for the actual mission need.

These experiences are not offered as evidence. Rather, they provide the practitioner lens that sharpens this study's research questions. The dual perspective -- having worked on both sides of the procurement transaction -- gives me access to participants and credibility with both audiences that purely academic researchers often lack. Vendors will speak candidly with someone who understands proposal economics; contracting officers will engage with someone who understands the constraints they face.

The completed quantitative analysis adds a further dimension to my positionality. I approached this topic expecting to find that best-value tradeoff produces better outcomes -- that was my working hypothesis based on twenty-five years of practice. The data did not confirm that expectation. That unexpected finding is what makes the qualitative inquiry essential: not to prove what I already believed, but to understand what I did not.

---

## 3. Research Questions

### Overarching Research Question

**When and why does source selection method matter for federal contract outcomes, and what system-level factors determine whether the method choice is consequential?**

### Specific Research Questions

**RQ1: Decision Drivers.** What factors drive the choice between LPTA and tradeoff source selection in practice? How much of that decision reflects genuine professional judgment versus institutional default, regulatory risk aversion, or organizational culture?

*Derived from: untested H3 (solicitation quality as mediator) and H10 (standardized guidance effects)*

**RQ2: The Crossover Puzzle.** Why does procurement complexity moderate the source selection method effect, and why does the advantage reverse for larger procurements? What mechanisms explain the crossover interaction observed at approximately $2 million in the quantitative data?

*Derived from: H8 finding (p = .003)*

**RQ3: Post-Award Dynamics.** How do post-award contract dynamics differ between LPTA and tradeoff contracts in practice? Why did the quantitative analysis find no aggregate difference in cost growth or modification intensity? Are there qualitative differences (relationship quality, scope management, dispute resolution) that archival data cannot capture?

*Derived from: null H1 (cost growth) and H2 (modifications)*

**RQ4: Organizational and Workforce Factors.** What role do workforce competence, organizational culture, leadership attention, and institutional norms play in determining whether source selection method matters for contract outcomes?

*Derived from: Kelman hypothesis (1990, 2005); untested H5 (oversight effects)*

**RQ5: The Vendor Perspective.** How do vendors experience and respond to LPTA versus tradeoff procurement? How do bid/no-bid decisions, pricing strategy, proposal investment, solution quality, and post-award behavior differ based on the evaluation method? Do vendor responses amplify or attenuate the government's method choice?

*Derived from: untested H7 (competition mediation); V2.2 original scope*

**RQ6: System-Level Determinants.** What system-level factors -- requirements quality, market conditions, contract structure, program management practices, oversight intensity -- matter more than source selection method for contract outcomes? How do these factors interact with method choice?

*Derived from: the core finding of the quantitative pilot -- that method alone does not predict outcomes*

---

## 4. Theoretical Framework

### 4.1 Transaction Cost Economics (Revised Application)

Transaction cost economics (Williamson, 1985, 1996) predicts that as asset specificity and uncertainty increase, market-based governance mechanisms (such as LPTA price competition) become less efficient and relational governance mechanisms (such as tradeoff evaluation with negotiation) become preferable. Applied to procurement, TCE predicts that tradeoff evaluation should produce better outcomes for complex, uncertain procurements.

The quantitative pilot partially confirmed this prediction: the complexity moderation finding (H8, p = .003) shows that method choice matters differentially by procurement size, consistent with TCE's conditional logic. However, the crossover reversal above approximately $2 million challenges TCE's monotonic prediction that tradeoff advantages should *increase* with complexity. This suggests that additional factors -- organizational complexity, evaluation resource constraints, or political dynamics -- intervene at higher procurement values, creating governance costs that offset the theoretical benefits of tradeoff evaluation.

This study uses TCE as a sensitizing framework rather than a hypothesis-generating engine: it guides attention to asset specificity, uncertainty, and governance alignment, while remaining open to evidence that the theory's predictions require modification in the federal procurement context.

### 4.2 Public Value Theory (Broadened Application)

Public value theory (Moore, 1995; Benington & Moore, 2011) argues that public managers should create value that is substantively important, democratically legitimate, and operationally feasible. In procurement, public value extends beyond cost minimization to include service quality, reliability, equity, innovation, and responsiveness.

The quantitative pilot's reliance on cost growth and modification intensity as outcome measures captures only the cost dimension of public value. The null findings may simply mean that LPTA and tradeoff contracts produce equivalent cost trajectories -- while differing substantially in quality, service continuity, or stakeholder satisfaction. Without CPARS (Contractor Performance Assessment Reporting System) data, which is not publicly available, the quantitative study cannot adjudicate this possibility.

The qualitative study addresses this limitation directly by asking practitioners about the full range of outcomes they observe -- not just cost, but quality, timeliness, relationship quality, user satisfaction, and long-term mission impact. It treats public value as a multidimensional construct that practitioners assess holistically, even when administrative data systems disaggregate it into narrow indicators.

### 4.3 Institutional Theory (New Addition)

Institutional theory (DiMaggio & Powell, 1983; Scott, 2014) offers a compelling explanation for the null main effects that TCE and public value theory struggle to account for. If federal agencies face similar regulatory environments (the FAR), similar oversight structures (IGs, GAO, congressional committees), similar workforce training (FAI certification, DAU courses), and similar professional norms (NCMA standards, acquisition career paths), then institutional isomorphism may compress outcome differences regardless of formal evaluation method.

Three mechanisms of institutional isomorphism may be operating:

- **Coercive isomorphism:** FAR requirements, OFPP guidance, and statutory mandates impose uniform procedures on all agencies, reducing the operational distinction between LPTA and tradeoff in practice.

- **Mimetic isomorphism:** Agencies facing uncertainty (how to handle a complex procurement) may model their approach on peer agencies, converging on similar practices regardless of formal method.

- **Normative isomorphism:** Professional training (FAI, DAU, NCMA) instills similar values and decision frameworks across the acquisition workforce, leading contracting officers to apply similar judgment regardless of whether the formal process is LPTA or tradeoff.

If institutional isomorphism is a significant factor, it would explain why source selection method choice produces little aggregate outcome difference -- the institutional environment normalizes behavior regardless of formal design. This is a potentially important theoretical contribution that has not been explored in the procurement literature.

### 4.4 Kelman's Process Quality Thesis (Elevated)

Steven Kelman (1990, 2005) has argued that federal procurement reform should focus on empowering skilled professionals to exercise judgment rather than constraining them with rigid procedural rules. Extended to source selection, this thesis predicts that the quality of the procurement *process* -- the competence and judgment of the contracting officer, the clarity and completeness of the requirements, the rigor of the market research, the quality of the evaluation panel, and the attentiveness of post-award contract management -- matters more than the formal evaluation mechanism.

If Kelman's thesis is correct, the null findings in the quantitative pilot reflect not the irrelevance of procurement design but the primacy of execution quality. A well-run LPTA procurement by a competent contracting officer with clear requirements may produce better outcomes than a poorly run tradeoff evaluation by an overworked, undertrained workforce operating under time pressure.

This is the most practically important theoretical proposition in the study, because it redirects policy attention from "which method?" to "what conditions enable good procurement regardless of method?" The qualitative study tests this proposition directly through RQ4 and RQ6.

### 4.5 Incomplete Contract Theory (Retained)

Incomplete contract theory (Hart & Moore, 1988; Bajari & Tadelis, 2001) predicts that for projects that cannot be fully specified in advance, negotiated/relational mechanisms will outperform competitive auctions. Bajari et al. (2009) found empirical support for this prediction in construction procurement.

This framework remains relevant for explaining the complexity moderation finding and for guiding investigation of post-award renegotiation dynamics (RQ3). However, the crossover reversal suggests that the relationship between contract incompleteness and governance mechanism is more complex in the federal context than in the private-sector construction settings where the theory was developed.

### 4.6 Revised Conceptual Model

The revised conceptual model (Figure 1) positions source selection method as one element within a broader procurement system, rather than as the primary independent variable driving outcomes. The key theoretical shift from the original proposal (V2.2) is the addition of system-level factors and institutional context as co-equal determinants of outcomes.

```
                    ┌─────────────────────────────┐
                    │    INSTITUTIONAL CONTEXT     │
                    │  FAR/regulatory environment  │
                    │  Oversight structure (IGs,   │
                    │  GAO, congressional)         │
                    │  Professional norms (FAI,    │
                    │  DAU, NCMA)                  │
                    └──────────────┬──────────────┘
                                   │
    ┌──────────────────┐          │          ┌──────────────────────┐
    │  SOURCE SELECTION │          │          │    PUBLIC VALUE       │
    │  METHOD CHOICE    ├──────────┼──────────►   OUTCOMES           │
    │                   │          │          │                      │
    │  LPTA vs.         │          │          │  - Cost performance  │
    │  Best-Value       │          │          │  - Quality/service   │
    │  Tradeoff         │          │          │  - Timeliness        │
    └────────┬─────────┘          │          │  - Relationship      │
             │                     │          │  - User satisfaction │
             │                     │          │  - Mission impact    │
             │                     │          └──────────────────────┘
             │                     │                    ▲
             │    ┌────────────────┴───────────────┐    │
             └────►  SYSTEM-LEVEL FACTORS           ├────┘
                  │                                 │
                  │  - Workforce competence (RQ4)   │
                  │  - Requirements quality (RQ6)   │
                  │  - Organizational culture (RQ4) │
                  │  - Contract management (RQ6)    │
                  │  - Market conditions (RQ5)      │
                  │  - Vendor behavior (RQ5)        │
                  │  - Procurement complexity (RQ2) │
                  └─────────────────────────────────┘
```

*Figure 1. Revised conceptual model: Source selection method as one element within a broader procurement system.*

---

## 5. Quantitative Pilot Findings: The Empirical Foundation

This section summarizes the completed quantitative analysis that provides the empirical foundation for the qualitative study. Full methodological details, statistical tables, and robustness checks are available in the companion manuscript prepared for journal submission.

### 5.1 Study Parameters

- **Sample:** 15,477 competitive service and IT contract awards above $250,000, extracted from USAspending.gov for FY2024 Q2
- **Primary comparison:** Quality-Evaluating design (n = 1,379) vs. Negotiated Fixed-Price design (n = 2,490); full sample including task orders (n = 15,477)
- **Methods:** OLS regression with agency and NAICS fixed effects; negative binomial GLM; logistic regression; propensity score matching (1,093 matched pairs)
- **Theoretical grounding:** Transaction cost economics, public value theory, auction theory, incomplete contract theory

### 5.2 Key Findings

**H1: Cost Growth (Not Supported).** The OLS main effect of tradeoff evaluation on cost growth was not statistically significant (b = 0.413, p = .377, 95% CI [-0.503, 1.330]). After regression adjustment, the effect size was negligible (d = 0.02). This null finding was robust across all specifications: full sample, PSM matched sample, large-agency subsample, NAICS-specific subsamples, outlier-excluded analyses, and alternative operationalizations.

**H2: Modification Intensity (Not Supported).** The negative binomial model found no significant effect of tradeoff evaluation on contract modification count (b = -0.034, IRR = 0.967, p = .449, 95% CI [0.884, 1.057]). QE contracts had 3.3% fewer modifications, but this difference was not statistically significant.

**H6: Single-Bid Competition (Not Supported, Marginal).** Tradeoff evaluation was associated with 24.8% lower odds of single-bid outcomes (OR = 0.752, p = .085), in the theoretically predicted direction but not reaching conventional significance at alpha = .05. This is the most promising archival finding for further investigation -- it suggests tradeoff evaluation may attract more competition.

**H8: Complexity Moderation (Supported).** The interaction between tradeoff evaluation and log award amount was statistically significant (b = 0.619, p = .003, 95% CI [0.210, 1.028]). The crossover point occurs at approximately $2 million in award value. Below this threshold, tradeoff evaluation is associated with lower cost growth. Above this threshold, the relationship reverses. This crossover pattern was robust across specifications.

### 5.3 What the Data Cannot Tell Us

The quantitative analysis identifies patterns but cannot explain mechanisms. Specifically:

- It cannot distinguish between legitimate scope evolution and contractor failure as drivers of cost growth
- It cannot measure quality outcomes (CPARS data is not publicly available)
- It cannot capture the decision rationale of contracting officers who chose between LPTA and tradeoff
- It cannot assess requirements quality, evaluation rigor, or post-award management practices
- It cannot determine whether vendor behavior (pricing strategy, proposal investment, bid/no-bid decisions) differs systematically by method
- It cannot explain why the complexity moderation effect reverses rather than strengthening

These gaps define the qualitative study's research questions and data collection priorities.

---

## 6. Literature Review

### 6.1 Source Selection Method and Contract Outcomes

The empirical literature on source selection method effects is surprisingly thin and largely confined to defense acquisition. Osman, Hill, and Baker (2017) found that LPTA contracts exhibited higher cost growth and schedule delays in a Naval Postgraduate School analysis. Watson (2015) found that tradeoff awards received higher CPARS performance ratings. Baker (2016) found that tradeoff was associated with lower cost growth for complex services, with the effect moderated by complexity. These studies, while informative, relied on single-agency or single-service samples with limited generalizability.

The present quantitative pilot is the first large-sample, cross-agency test of these relationships using federal-wide data. Its null main effects and significant complexity moderation contribute new evidence that challenges the findings of these smaller studies, or at minimum suggests their results may not generalize across the federal procurement system.

### 6.2 Qualitative Research on Procurement Decision-Making

Qualitative procurement research has explored practitioner decision-making, but not systematically in the context of source selection method choice. Rendon (2009) developed a procurement process maturity model through case studies of military procurement organizations. Patrucco, Luzzini, and Ronchi (2017) examined how public procurement competence affects performance through a multiple-case study of European public organizations. Prier and McCue (2009) traced the evolution of best-value procurement concepts through policy analysis and stakeholder interviews.

No published qualitative study has directly investigated how contracting officers choose between LPTA and tradeoff, what factors shape that decision, and how the choice reverberates through post-award contract dynamics. This gap is particularly striking given the policy significance of the question and the volume of practitioner commentary on the topic.

### 6.3 The Vendor Perspective in Procurement Research

Most procurement scholarship takes the buyer (government) perspective. The vendor experience -- how firms interpret evaluation criteria, make bid/no-bid decisions, invest in proposal quality, adjust pricing strategy, and manage post-award relationships -- remains largely unstudied in the public procurement context. Patrucco, Moretto, Trabucchi, and Golini (2023) call for greater attention to supplier perspectives in public procurement research. The present study addresses this gap by including vendor participants as an embedded unit of analysis within each case.

### 6.4 Institutional Context and Procurement Outcomes

The role of institutional context in shaping procurement outcomes has received growing attention. Calvo, Cui, and Serpa (2019) found that additional oversight can increase delays and cost overruns in public projects, while being more beneficial under specific conditions such as higher contractor experience. This finding resonates with the null effects observed in the present pilot study -- the institutional governance infrastructure of federal procurement (oversight, auditing, contract administration) may serve as a quality floor that reduces the marginal contribution of source selection method.

Kelman (1990, 2005) has been the most influential voice arguing that the quality of the procurement workforce and the discretion afforded to skilled professionals matters more than the procedural rules governing the process. This thesis has been debated but not empirically tested in the specific context of source selection method choice.

---

## 7. Research Method

### 7.1 Research Design: Qualitative Multiple-Case Study

This study employs a qualitative multiple-case study design following Yin (2018) and informed by Eisenhardt (1989) and Stake (1995). The case study is the appropriate method because:

1. The research questions are "how" and "why" questions about a contemporary phenomenon (Yin, 2018)
2. The investigator has no control over the events being studied
3. The phenomenon cannot be meaningfully separated from its organizational and institutional context
4. The quantitative pilot has identified specific patterns that require contextual explanation (sequential explanatory design; Creswell & Creswell, 2018)
5. The theory is in an intermediate state of development where quantitative tests of existing frameworks produce unexpected results, calling for qualitative investigation to refine or reconceptualize mechanisms (Edmondson & McManus, 2007)

The sequential explanatory logic is central to the study's design. The quantitative pilot identified the empirical patterns. The qualitative study investigates the mechanisms behind those patterns. This is not abandoning quantitative rigor for qualitative convenience -- it is building on quantitative evidence with the method best suited to answer the questions that evidence has raised.

### 7.2 Why Case Study Over Alternative Methods

**Why not grounded theory?** Grounded theory (Charmaz, 2014) is most appropriate when existing theory is absent or insufficiently developed. Source selection has well-developed theoretical frameworks (TCE, public value, auction theory); the problem is that their predictions are not confirmed empirically. The research need is to explain why theory fails, not to build theory from scratch.

**Why not phenomenology?** Phenomenology (Moustakas, 1994) examines lived experience and its meaning. While practitioner experience is important, the study's interest extends beyond subjective meaning to organizational mechanisms, institutional dynamics, and behavioral patterns that operate across individuals.

**Why not ethnography?** Ethnographic immersion in procurement offices would provide rich data but is impractical given the multi-agency, multi-site design and the study's focus on cross-case comparison rather than deep cultural description of a single setting.

**Why multiple cases rather than single case?** A single case could provide depth but not the comparative leverage needed to investigate how different organizational contexts produce different outcomes. The five-case design enables replication logic (Yin, 2018) and systematic comparison across agencies that differ on key theoretical dimensions.

### 7.3 Case Selection

Cases are selected using maximum variation sampling (Patton, 2015) across four dimensions that the quantitative analysis and theoretical framework identify as potentially important:

| Dimension | Variation Sought | Rationale |
|-----------|-----------------|-----------|
| Agency type | DoD vs. civilian | Different regulatory environments, cultures, workforce |
| Primary method used | LPTA-heavy vs. tradeoff-heavy vs. mixed | Captures full range of practice |
| Procurement complexity | Low-moderate to high | Tests the crossover finding qualitatively |
| Mission domain | Logistics, IT, health, security | Controls for sector-specific dynamics |

**Proposed Cases:**

**Case 1: Defense Logistics Agency (DLA)**
- *Profile:* DoD's largest procurement agency; processes millions of contract actions annually across commodities, services, and support
- *Selection rationale:* High-volume, mixed-method agency that uses both LPTA and tradeoff depending on commodity type; spans the complexity spectrum
- *Theoretical leverage:* Tests institutional isomorphism (do uniform DoD procedures homogenize outcomes?) and the complexity boundary (at what point does DLA shift from LPTA to tradeoff?)

**Case 2: Air Force or Navy Acquisition Office**
- *Profile:* Service-branch acquisition for complex IT, weapon system support, or professional services
- *Selection rationale:* Tradeoff-heavy environment post-NDAA Section 813 restrictions; high-complexity services
- *Theoretical leverage:* Tests TCE predictions in a high-complexity setting; examines the crossover puzzle (why doesn't tradeoff help more at higher complexity?)

**Case 3: General Services Administration (GSA) Federal Acquisition Service**
- *Profile:* Government-wide contracting vehicles; Alliant 2, OASIS+, Schedule contracts
- *Selection rationale:* LPTA-heavy, efficiency-driven culture; the government's "marketplace" agency
- *Theoretical leverage:* Tests whether a well-run LPTA process produces outcomes comparable to tradeoff (Kelman's process quality thesis)

**Case 4: Department of Veterans Affairs or Department of Health and Human Services**
- *Profile:* Mission-critical healthcare IT, benefits administration, public health systems
- *Selection rationale:* Moderate-to-high complexity; civilian agency with different culture than DoD; high public visibility
- *Theoretical leverage:* Tests public value theory (how do procurement decisions affect service delivery to citizens?) and institutional differences (civilian vs. DoD)

**Case 5: Department of Homeland Security (CISA or CBP)**
- *Profile:* Cybersecurity, border technology, emergency management systems
- *Selection rationale:* High complexity, rapidly evolving technology, high political salience
- *Theoretical leverage:* Tests the upper boundary of the complexity moderation finding; examines whether political and organizational complexity (as opposed to technical complexity alone) drives the crossover effect

### 7.4 Participants and Recruitment

**Government participants (4-5 per case, 20-25 total):**
- Contracting officers who make source selection method recommendations
- Source selection authorities who approve method decisions
- Program managers who define requirements and live with outcomes
- Contracting officer's representatives (CORs) who manage post-award performance
- Senior acquisition leaders (heads of contracting activities, chief procurement officers)

**Vendor participants (2-3 per case, 10-15 total):**
- Capture managers who make bid/no-bid recommendations
- Proposal directors who manage proposal development
- Program managers who execute contracts post-award
- Business development executives who assess market opportunities

**Total: 30-40 semi-structured interviews**

**Recruitment strategy:**
- Professional networks: NCMA (National Contract Management Association), FAI (Federal Acquisition Institute), DAU (Defense Acquisition University)
- Personal professional network (25 years of government and vendor relationships)
- Snowball sampling from initial participants
- Agency-level outreach through public affairs and academic liaison offices
- NCMA and IRSPM conference networking
- LinkedIn professional groups (Government Contracting, Federal Acquisition)

### 7.5 Data Collection

**Semi-Structured Interviews (Primary Data)**

Each interview will be 60-90 minutes, conducted via secure video conference or in person during Kelley immersion trips to Bloomington. Interviews will be audio-recorded with participant consent and professionally transcribed.

**Interview Protocol Outline:**

*Part A: Opening and Context (10 minutes)*
- Professional background and role
- Types of procurements typically handled
- Approximate mix of LPTA vs. tradeoff in their portfolio

*Part B: Source Selection Decision-Making (20 minutes)* [RQ1]
- Walk me through how you/your office decides between LPTA and tradeoff for a new procurement
- What factors weigh most heavily in that decision?
- Tell me about a time the method choice was debated or contested
- How much of the decision is driven by regulation vs. professional judgment vs. organizational culture?

*Part C: Post-Award Dynamics (15 minutes)* [RQ3]
- How does contract management differ between LPTA and tradeoff contracts?
- Do you observe differences in contractor performance, relationship quality, or scope management?
- Tell me about a contract that performed well/poorly -- what role did the source selection method play?

*Part D: Complexity and the Crossover (10 minutes)* [RQ2]
- [Share the crossover finding] Does this pattern make sense based on your experience?
- Why might tradeoff evaluation help for smaller procurements but not larger ones?
- What changes about procurements as they get larger that might affect this?

*Part E: Organizational and Workforce Factors (10 minutes)* [RQ4]
- How does the skill and experience of the contracting officer affect outcomes?
- What does your organization do well/poorly in procurement?
- If you could change one thing about how your office handles source selection, what would it be?

*Part F: Vendor Perspective (for vendor participants)* [RQ5]
- How does the evaluation method affect your bid/no-bid decision?
- How do you price differently under LPTA vs. tradeoff?
- How does your proposal investment differ?
- How does the post-award relationship differ?

*Part G: System Factors and Closing (10 minutes)* [RQ6]
- What matters more for contract outcomes -- the evaluation method or the quality of the overall process?
- What system-level factors have the biggest impact on whether a procurement succeeds or fails?
- Is there anything else about source selection that I should be asking about?

**Document Analysis (Secondary Data)**

For each case, the study will collect and analyze:
- Publicly available solicitations (FedBizOpps/SAM.gov) from the case agency
- Source selection decision documents (where accessible via FOIA or participant sharing)
- Agency-level procurement policy and guidance
- GAO bid protest decisions involving the agency
- Agency performance reports and strategic plans related to acquisition

**Archival Data Integration (Supplementary)**

The 15,477-record quantitative dataset provides agency-level descriptive statistics for each case: distribution of LPTA vs. tradeoff awards, average award sizes, cost growth distributions, modification patterns, competition levels, and NAICS/PSC composition. These quantitative profiles provide empirical context for each case and enable systematic comparison between what the archival data show and what practitioners describe.

### 7.6 Analysis Approach

**Within-Case Analysis**

Each case will be analyzed as a standalone unit, producing a detailed case narrative (30-50 pages per case) that describes:
- The agency's procurement environment and organizational context
- How source selection decisions are made in practice
- Post-award dynamics observed by participants
- The role of workforce, culture, and institutional factors
- Vendor experience and behavior
- How the case's patterns relate to the quantitative data

**Cross-Case Analysis**

Following Yin (2018) and Miles, Huberman, and Saldana (2020), cross-case analysis will use:
- **Pattern matching:** Compare observed patterns across cases to theoretical propositions
- **Explanation building:** Iteratively develop causal explanations for the quantitative findings
- **Cross-case displays:** Matrices comparing themes, codes, and patterns across all five cases
- **Rival explanations:** Systematically evaluate competing theoretical explanations

**Coding Strategy (Three Cycles)**

Following Saldana (2021):

*First Cycle: Initial/Open Coding*
- Line-by-line coding of interview transcripts
- In-vivo codes (participant language), descriptive codes, and process codes
- No code imposed from theory -- let the data speak first

*Second Cycle: Focused Coding*
- Identify the most frequent and significant codes from Cycle 1
- Group codes into categories aligned with the research questions
- Begin mapping codes to the theoretical framework

*Third Cycle: Theoretical Coding*
- Map focused codes to theoretical propositions (TCE, public value, institutional theory, Kelman)
- Build cross-case propositions explaining the quantitative findings
- Identify emergent themes not captured by existing theory

**Coding Architecture**

| Code Group | Codes | Research Question Link |
|-----------|-------|----------------------|
| **1. Decision Factors** | Regulatory guidance; Agency culture/norms; Protest risk perception; Administrative burden; Complexity assessment; Workforce experience; Leadership direction; Time pressure; Budget constraints | RQ1, RQ2 |
| **2. Post-Award Dynamics** | Contract management quality; Modification drivers; Contractor relationship; Scope evolution; Performance issues; Communication patterns; Trust; Adaptability | RQ3 |
| **3. Theoretical Constructs** | TCE: Asset specificity; TCE: Uncertainty; TCE: Frequency; Public Value: Substantive; Public Value: Legitimacy; Institutional isomorphism: Coercive; Institutional isomorphism: Mimetic; Institutional isomorphism: Normative; Kelman: Process quality | All RQs |
| **4. Organizational Factors** | Workforce competence; Training/development; Organizational learning; Agency risk tolerance; Process compliance vs. outcomes focus; Institutional memory | RQ4 |
| **5. Contextual Factors** | Agency type (civilian vs. DoD); Procurement size/complexity; Market conditions; Political environment; Oversight intensity; Technology maturity | RQ2, RQ6 |
| **6. Market/Competition & Vendor Behavior** | Firm participation decisions; Bid/no-bid factors; Proposal investment; Pricing strategy; Competitive landscape; Incumbent advantage; Small business dynamics; Post-award vendor behavior | RQ5, RQ6 |
| **7. Emergent** | Reserved for codes arising inductively | TBD |

**Integration of Quantitative and Qualitative Evidence**

The final analysis stage integrates the qualitative findings with the quantitative patterns, identifying:
- **Convergence:** Where qualitative evidence supports and explains quantitative patterns (e.g., practitioners describe the complexity crossover in terms consistent with the statistical finding)
- **Divergence:** Where qualitative evidence contradicts or complicates quantitative patterns (e.g., practitioners perceive method effects that the data do not capture)
- **Extension:** Where qualitative evidence reveals dynamics that quantitative data cannot measure (e.g., relationship quality, evaluation rigor, requirements evolution)

---

## 8. Validity and Trustworthiness

Following Lincoln and Guba (1985) and Yin (2018), the study addresses four dimensions of research quality:

### 8.1 Credibility (Internal Validity)
- **Triangulation:** Multiple data sources per case (government interviews + vendor interviews + documents + archival data)
- **Member checking:** Share case narratives with key participants for accuracy verification
- **Prolonged engagement:** Multiple interview rounds if needed to clarify or deepen understanding
- **Peer debriefing:** Regular discussion with dissertation committee and qualitative methods advisor
- **Negative case analysis:** Actively seek and report evidence that contradicts emerging patterns

### 8.2 Transferability (External Validity)
- **Thick description:** Provide sufficient contextual detail for readers to assess applicability to other procurement settings (state/local government, international, private sector)
- **Maximum variation sampling:** Case selection strategy captures a broad range of conditions, enhancing the breadth of potential transferability
- **Explicit boundary conditions:** Clearly state the federal procurement context and its institutional features to help readers calibrate transferability

### 8.3 Dependability (Reliability)
- **Case study protocol:** Detailed, written protocol followed consistently across all cases
- **Case study database:** Complete archive of interview recordings, transcripts, documents, codes, and memos in QDAS (ATLAS.ti or NVivo)
- **Audit trail:** Documented coding decisions, analytic memos, and methodological memos throughout the study
- **Chain of evidence:** Traceable links from research questions to data collection to analysis to conclusions

### 8.4 Confirmability (Objectivity)
- **Reflexivity journal:** Ongoing documentation of researcher assumptions, biases, and their potential influence on interpretation
- **Positionality disclosure:** Transparent reporting of practitioner background and how it shapes the research lens
- **Multiple theoretical lenses:** Application of competing theoretical frameworks (TCE, institutional theory, Kelman) prevents premature theoretical closure
- **Raw data access:** Committee members will have access to anonymized transcripts and coding

---

## 9. Ethics, IRB, and Feasibility

### 9.1 IRB Considerations

The study involves human subjects (interviews with federal employees and private-sector professionals) and will require IRB approval from Indiana University. Key considerations:

- **Federal employee participants:** Federal employees participating in interviews about their professional roles are generally low-risk, but the study will ensure that no participant is identifiable from published findings and that no sensitive procurement information (source selection details for active acquisitions, contractor proprietary information, classified or controlled unclassified information) is collected or reported.

- **Informed consent:** All participants will provide written informed consent. Consent forms will specify: voluntary participation, right to withdraw, audio recording procedures, data security measures, confidentiality protections, and anticipated use of data.

- **Anonymization:** All participants will be assigned pseudonyms. Agency names will be used (with consent) for case identification, but individual participants will not be linked to specific quotations without explicit permission.

- **Data security:** Interview recordings and transcripts will be stored on encrypted local storage (not cloud). Access limited to the researcher and dissertation committee.

### 9.2 Agency Access and Feasibility

Access to federal procurement professionals is the study's primary feasibility challenge. The strategy employs multiple, complementary access pathways:

1. **Professional networks:** Twenty-five years of government and vendor-side experience provides a foundation of professional relationships across multiple agencies, including at senior levels.

2. **Professional associations:** Active engagement with NCMA (National Contract Management Association), attendance at NCMA World Congress and regional events, and participation in FAI and DAU educational programs.

3. **Academic partnerships:** Indiana University's programs attract students and alumni who work in federal procurement and public administration.

4. **Snowball sampling:** Initial participants will be asked to recommend colleagues who may be willing to participate.

5. **Vendor-side access:** Personal professional network on the vendor side (proposal managers, capture professionals, program managers) provides direct access to the vendor perspective.

6. **Conference presentations:** Presenting preliminary findings at NCMA, APPAM, or IRSPM conferences generates visibility and participant interest.

### 9.3 Timeline Considerations

The study is designed to be completable within the Kelley program timeline. The ARP sequence (Years 1-2) produces pilot cases that feed directly into the dissertation (Year 3). Data collection for the remaining cases (Winter 2029) requires approximately 3 months of active interviewing, which is feasible given remote interview capabilities and the researcher's professional travel schedule.

---

## 10. Timeline and Program Alignment

### 10.1 Pre-Enrollment (Spring-Summer 2026)

| Activity | Timing |
|----------|--------|
| Qualitative software proficiency (ATLAS.ti/NVivo) | April-June 2026 |
| Submit quantitative paper to JPART or JOPP | Spring 2026 |
| Begin IRB pre-planning | Summer 2026 |
| Refine interview protocol | Summer 2026 |

### 10.2 Year 1 (Fall 2026 - Summer 2027)

| Kelley Milestone | Research Activity |
|-------------|-------------------|
| Fall 2026: Core methods courses (BUS 6000, 6001, 6002) | Learn qualitative methods formally; refine case study design based on coursework |
| Winter 2027: Research design, quantitative methods (BUS 6003, 6005) | Deepen analytical framework; present quant findings in class |
| Spring 2027: Leadership and ethics seminars (MGMT 6300, 6301) | Apply organizational theory to procurement context |
| **ARP I (Summer 2027):** BUS 6500 | Systematic literature review of qualitative procurement research; refined research questions |

### 10.3 Year 2 (Fall 2027 - Summer 2028)

| Kelley Milestone | Research Activity |
|-------------|-------------------|
| **ARP II (Fall 2027):** BUS 6501 | Finalize case study protocol; obtain IRB approval; begin recruitment; conduct 2-3 practice interviews |
| **ARP III (Winter 2028):** BUS 6502 | Conduct 2 pilot cases (Cases 1-2); transcribe and code; within-case analysis |
| **ARP IV (Spring 2028):** BUS 6503 | Write ARP paper (dual-case study); present findings; submit to target journal |
| Comprehensive Exams (Summer 2028) | Integrate quantitative and qualitative methods knowledge; demonstrate theoretical mastery |

### 10.4 Year 3: Dissertation (Fall 2028 - Spring 2029)

| Milestone | Activity | Timing |
|----------|---------|--------|
| Dissertation Proposal Defense | Present full 5-case design with 2 pilot cases completed; committee approval | October-November 2028 |
| Remaining Data Collection | Conduct Cases 3-5 (15-21 interviews) | December 2028 - February 2029 |
| Cross-Case Analysis | Analyze all 5 cases; integrate with quantitative pilot | February-March 2029 |
| Chapter Drafting | Write dissertation chapters 4-5 (results, discussion) | March-April 2029 |
| Member Checking | Share case narratives with participants | April 2029 |
| Final Revisions | Incorporate committee feedback | April-May 2029 |
| Final Defense | Oral defense of completed dissertation | May-June 2029 |

---

## 11. Limitations

Several limitations of the proposed study should be acknowledged:

1. **Selection bias in participation:** Procurement professionals who agree to be interviewed may differ systematically from those who decline. Participants may be more reflective, more reform-oriented, or more critical of current practice than the broader acquisition workforce. Snowball sampling and recruitment through multiple channels (professional associations, agency outreach, personal networks) will mitigate but not eliminate this concern.

2. **Recall and rationalization bias:** Participants describing past procurement decisions may retrospectively rationalize their choices or reconstruct decision processes in ways that are more coherent than the actual experience. The interview protocol includes probes for specific examples and concrete details to anchor responses in actual events.

3. **Federal-only scope:** The study examines only federal procurement under the FAR. Findings may not generalize to state and local procurement (which operate under different statutory frameworks) or international systems (EU public procurement directives, WTO Agreement on Government Procurement).

4. **Cross-sectional design:** Although the case study includes historical perspective from participants, it captures a snapshot of current practice rather than tracking changes over time. Longitudinal follow-up studies could examine how practice evolves in response to policy changes.

5. **Five cases from a universe of 58+ agencies:** While maximum variation sampling provides analytical generalization, the study cannot represent the full diversity of federal procurement practice. Agencies with unique characteristics (e.g., intelligence community procurement) are excluded.

6. **Vendor access challenges:** Vendors may be reluctant to discuss pricing strategy, competitive intelligence, or negative experiences with government clients. The researcher's vendor-side background and the study's academic context may mitigate this concern, but some vendor-side dynamics may remain opaque.

---

## 12. Expected Contributions

### 12.1 Theoretical Contributions

1. **Explains the aggregate null:** Provides the first systematic qualitative investigation of why source selection method alone does not predict contract outcomes at the federal level, addressing a gap that the quantitative literature cannot close.

2. **Tests institutional theory in procurement:** Introduces institutional isomorphism as an explanation for the null findings, extending institutional theory into a new empirical domain.

3. **Tests Kelman's process quality thesis empirically:** Provides the first direct test of whether workforce competence and process quality are more important than formal evaluation method for procurement outcomes.

4. **Explains the crossover puzzle:** Investigates the mechanisms behind the complexity moderation reversal (p = .003), potentially refining TCE's predictions for public-sector contexts.

5. **Integrates the vendor perspective:** Provides the first multi-case study that systematically examines both government and vendor perspectives on source selection method effects.

### 12.2 Practical Contributions

1. **Actionable guidance for contracting officers:** Identifies the conditions under which method choice genuinely matters, enabling practitioners to allocate evaluation resources more effectively.

2. **Workforce development implications:** If the Kelman thesis is supported, the study provides evidence-based rationale for investing in workforce competence rather than procedural reform.

3. **Policy reform evidence:** Informs the ongoing debate about LPTA restrictions (NDAA Section 813) with practitioner-level evidence about how these restrictions affect practice.

4. **Procurement system design:** Identifies system-level factors (requirements quality, contract management, market conditions) that policymakers should prioritize alongside or instead of source selection method reform.

---

## 13. Conclusion

Government procurement is not a simple price-shopping exercise. It is a public decision that determines whether agencies deliver reliable services, protect taxpayer dollars over the full contract life, and sustain credibility with both vendors and citizens.

This proposal starts from an empirical finding that surprised even the researcher: source selection method alone does not predict aggregate contract cost outcomes. Rather than dismissing this finding or seeking to explain it away, this dissertation investigates it directly -- through the eyes and experiences of the people who make and live with these decisions on both sides of the procurement relationship.

The path from lowest price to highest public value, it turns out, does not run primarily through the source selection method. It runs through the entire procurement system -- the quality of requirements, the competence of the workforce, the rigor of evaluation, the attentiveness of post-award management, and the institutional environment in which all of these occur. This dissertation seeks to map that fuller path.

---

## References

Asian Development Bank. (2018). *Value for money: Guidance note on procurement*. Asian Development Bank.

Bajari, P., McMillan, R., & Tadelis, S. (2009). Auctions versus negotiations in procurement: An empirical analysis. *Journal of Law, Economics, & Organization*, *25*(2), 372-399.

Bajari, P., & Tadelis, S. (2001). Incentives versus transaction costs: A theory of procurement contracts. *RAND Journal of Economics*, *32*(3), 387-407.

Baker, J. T. (2016). *LPTA versus tradeoff: Analysis of contract source selection strategies and performance outcomes* (Master's thesis). Naval Postgraduate School.

Ban, R. W. (2015). *Lowest price technically acceptable vs. tradeoff in Air Force acquisitions* (Master's thesis). Naval Postgraduate School.

Benington, J., & Moore, M. H. (Eds.). (2011). *Public value: Theory and practice*. Palgrave Macmillan.

Calvo, E., Cui, R., & Serpa, J. C. (2019). Oversight and efficiency in public projects: A regression discontinuity analysis. *Management Science*, *65*(12), 5651-5675.

Charmaz, K. (2014). *Constructing grounded theory* (2nd ed.). SAGE.

Congressional Research Service. (2024). *Lowest price technically acceptable contracts* (IF100968).

Creswell, J. W., & Creswell, J. D. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, *48*(2), 147-160.

Edmondson, A. C., & McManus, S. E. (2007). Methodological fit in management field research. *Academy of Management Review*, *32*(4), 1155-1179.

Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review*, *14*(4), 532-550.

Fazekas, M., & Blum, J. R. (2021). *Improving public procurement outcomes: Review of tools and the state of evidence*. World Bank Open Knowledge Repository.

Federal Acquisition Regulation. (n.d.). Part 15: Contracting by negotiation (SS 15.101-1, 15.101-2). Acquisition.gov.

Hart, O., & Moore, J. (1988). Incomplete contracts and renegotiation. *Econometrica*, *56*(4), 755-785.

Iossa, E. (2019). *Competition for-the-market: Tackling the incumbency advantage* (OECD Global Forum on Competition). Organisation for Economic Co-operation and Development.

Johansson, T., & Lahtinen, H. (2012). Requirement specification in government IT procurement. *Procedia Technology*, *5*, 369-377.

Jung, H., Kosmopoulou, G., Lamarche, C., & Sicotte, R. (2013). Strategic bidding and contract renegotiation (Working paper).

Kelman, S. (1990). *Procurement and public management: The fear of discretion and the quality of government performance*. American Enterprise Institute.

Kelman, S. (2005). *Unleashing change: A study of organizational renewal in government*. Brookings Institution Press.

Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic inquiry*. SAGE.

Malacina, I., Karttunen, E., Salminen, J., & Toppinen, A. (2022). Capturing the value creation in public procurement: A systematic literature review. *Journal of Purchasing and Supply Management*, *28*(1), 100724.

Miles, M. B., Huberman, A. M., & Saldana, J. (2020). *Qualitative data analysis: A methods sourcebook* (4th ed.). SAGE.

Moore, M. H. (1995). *Creating public value: Strategic management in government*. Harvard University Press.

Moustakas, C. (1994). *Phenomenological research methods*. SAGE.

Office of Federal Procurement Policy. (2021). *Procurement administrative lead time (PALT): A common definition and strategies for improvement* (Memorandum).

Organisation for Economic Co-operation and Development. (2009). *Guidelines for fighting bid rigging in public procurement*. OECD.

Organisation for Economic Co-operation and Development. (2019). *Public value in public service transformation*. OECD Observatory of Public Sector Innovation.

Osman, J., Hill, D. W., & Baker, J. T. (2017). *Contract source selection: An analysis of lowest price technically acceptable and tradeoff strategies* (Symposium briefing). Naval Postgraduate School.

Patrucco, A. S., Luzzini, D., & Ronchi, S. (2017). Evaluating the effectiveness of public procurement performance management systems in local governments. *Local Government Studies*, *43*(5), 739-761.

Patrucco, A. S., Moretto, A., Trabucchi, D., & Golini, R. (2023). Public procurement and supply management: New perspectives and research directions. *Public Administration Review*, *83*(5), 1087-1107.

Patton, M. Q. (2015). *Qualitative research and evaluation methods* (4th ed.). SAGE.

Prier, E., & McCue, C. P. (2009). The implications of a muddled definition of public procurement. *Journal of Public Procurement*, *9*(3-4), 326-370.

Rendon, R. G. (2009). Procurement process maturity: Key to performance measurement. *Journal of Public Procurement*, *8*(2), 200-214.

Saldana, J. (2021). *The coding manual for qualitative researchers* (4th ed.). SAGE.

Scott, W. R. (2014). *Institutions and organizations: Ideas, interests, and identities* (4th ed.). SAGE.

Stake, R. E. (1995). *The art of case study research*. SAGE.

U.S. Government Accountability Office. (2025). *Annual report on bid protests*. U.S. Government Accountability Office.

Watson, K. (2015). *LPTA versus tradeoff: How procurement strategies impact quality of contractor performance* (Master's thesis). Naval Postgraduate School.

Williamson, O. E. (1985). *The economic institutions of capitalism*. Free Press.

Williamson, O. E. (1996). *The mechanisms of governance*. Oxford University Press.

Yin, R. K. (2018). *Case study research and applications: Design and methods* (6th ed.). SAGE.
