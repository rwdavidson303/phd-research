---
title: "Source Selection Decision Tool"
description: "Interactive guide: When to use LPTA vs. best-value tradeoff evaluation"
---

This interactive decision tool helps federal contracting officers determine whether Lowest Price Technically Acceptable (LPTA) or best-value tradeoff source selection is appropriate for a given acquisition. It walks through the key regulatory considerations from FAR 15.101, DFARS 215.101-2-70, and NDAA Section 813, and provides a recommendation based on your answers. The tool is designed for GS-13 and GS-14 contracting officers and contracting officer representatives who are drafting source selection plans.

<div id="decision-tool-app">

<style>
  #decision-tool-app {
    --dt-navy: #1B2A4A;
    --dt-gold: #C9A84C;
    --dt-cream: #FAF8F5;
    --dt-white: #FFFFFF;
    --dt-green: #2E7D32;
    --dt-red: #B71C1C;
    --dt-neutral: #546E7A;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 720px;
    margin: 2rem auto;
  }

  #decision-tool-app *,
  #decision-tool-app *::before,
  #decision-tool-app *::after {
    box-sizing: border-box;
  }

  .dt-progress {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
    color: var(--dt-navy);
    opacity: 0.7;
  }

  .dt-progress-bar {
    flex: 1;
    height: 4px;
    background: #e0e0e0;
    border-radius: 2px;
    overflow: hidden;
  }

  .dt-progress-fill {
    height: 100%;
    background: var(--dt-gold);
    border-radius: 2px;
    transition: width 0.4s ease;
  }

  .dt-card {
    background: var(--dt-white);
    border: 2px solid var(--dt-navy);
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(27, 42, 74, 0.1);
    animation: dt-fade-in 0.35s ease;
  }

  @keyframes dt-fade-in {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .dt-card h3 {
    margin: 0 0 0.5rem 0;
    color: var(--dt-navy);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .dt-card p.dt-question {
    margin: 0 0 1.75rem 0;
    font-size: 1.1rem;
    line-height: 1.55;
    color: #222;
  }

  .dt-hint {
    margin: -1.25rem 0 1.75rem 0;
    font-size: 0.85rem;
    color: #666;
    font-style: italic;
    line-height: 1.45;
  }

  .dt-buttons {
    display: flex;
    gap: 1rem;
  }

  .dt-btn {
    flex: 1;
    padding: 0.85rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    border: 2px solid var(--dt-navy);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .dt-btn-yes {
    background: var(--dt-navy);
    color: var(--dt-white);
  }

  .dt-btn-yes:hover {
    background: #2a3d66;
    border-color: #2a3d66;
  }

  .dt-btn-no {
    background: var(--dt-white);
    color: var(--dt-navy);
  }

  .dt-btn-no:hover {
    background: var(--dt-cream);
  }

  /* Result cards */
  .dt-result {
    padding: 2rem;
    border-radius: 8px;
    animation: dt-fade-in 0.35s ease;
    margin-bottom: 1rem;
  }

  .dt-result h3 {
    margin: 0 0 0.75rem 0;
    font-size: 1.25rem;
  }

  .dt-result p {
    margin: 0;
    line-height: 1.55;
    font-size: 0.95rem;
  }

  .dt-result-lpta {
    background: #E8F5E9;
    border: 2px solid var(--dt-green);
    color: #1B5E20;
  }
  .dt-result-lpta h3 { color: var(--dt-green); }

  .dt-result-tradeoff {
    background: #FFF8E1;
    border: 2px solid var(--dt-gold);
    color: var(--dt-navy);
  }
  .dt-result-tradeoff h3 { color: var(--dt-navy); }

  .dt-result-restricted {
    background: #FFEBEE;
    border: 2px solid var(--dt-red);
    color: #4A0E0E;
  }
  .dt-result-restricted h3 { color: var(--dt-red); }

  .dt-result-either {
    background: #ECEFF1;
    border: 2px solid var(--dt-neutral);
    color: #263238;
  }
  .dt-result-either h3 { color: var(--dt-neutral); }

  .dt-start-over {
    display: inline-block;
    margin-top: 1.25rem;
    padding: 0.65rem 1.5rem;
    font-size: 0.9rem;
    font-weight: 600;
    background: var(--dt-navy);
    color: var(--dt-white);
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s ease;
  }

  .dt-start-over:hover {
    background: #2a3d66;
  }

  .dt-citation {
    font-size: 0.8rem;
    color: #888;
    margin-top: 0.75rem;
    line-height: 1.45;
  }

  .dt-disclaimer {
    margin-top: 2rem;
    padding: 1rem 1.25rem;
    background: var(--dt-cream);
    border-left: 4px solid var(--dt-gold);
    font-size: 0.82rem;
    color: #555;
    line-height: 1.5;
    border-radius: 0 4px 4px 0;
  }
</style>

<div id="dt-container"></div>

<script>
(function() {
  var container = document.getElementById('dt-container');

  var questions = [
    {
      id: 'q1',
      label: 'Question 1 of 6',
      text: 'Is this a Department of Defense (DoD) acquisition in IT services, cybersecurity, professional services, or knowledge-based services (NAICS 51 or 54)?',
      hint: 'Section 813 of the FY2016 NDAA restricts LPTA for these service categories within DoD.',
      yes: 'q2',
      no: 'q3',
      progress: 17
    },
    {
      id: 'q2',
      label: 'Question 2 of 6',
      text: 'Can you clearly define minimum requirements where exceeding them provides no additional value to the government?',
      hint: 'Even under Section 813 restrictions, LPTA may be permissible if minimum requirements are truly sufficient and quality above that threshold adds no value.',
      yes: 'result-lpta-813',
      no: 'result-restricted',
      progress: 33
    },
    {
      id: 'q3',
      label: 'Question 3 of 6',
      text: 'Is the requirement for a commercial commodity, expendable supply, or nontechnical item?',
      hint: 'FAR 15.101-2 indicates LPTA is appropriate when the government can clearly define minimum requirements in terms of performance or capability.',
      yes: 'result-lpta',
      no: 'q4',
      progress: 50
    },
    {
      id: 'q4',
      label: 'Question 4 of 6',
      text: 'Is past performance or technical capability important to successful contract execution?',
      hint: 'If quality of personnel, experience, or technical approach significantly affects outcomes, a tradeoff process can evaluate those factors alongside price.',
      yes: 'result-tradeoff',
      no: 'q5',
      progress: 67
    },
    {
      id: 'q5',
      label: 'Question 5 of 6',
      text: 'Is the estimated contract value above the simplified acquisition threshold ($350,000)?',
      hint: 'Higher-dollar acquisitions carry greater risk and typically benefit from evaluating quality factors, not just price.',
      yes: 'result-tradeoff-value',
      no: 'q6',
      progress: 83
    },
    {
      id: 'q6',
      label: 'Question 6 of 6',
      text: 'Is this a competitive environment with three or more expected offerors?',
      hint: 'Competition on quality factors is most effective when multiple firms can submit meaningfully different proposals.',
      yes: 'result-tradeoff-competition',
      no: 'result-either',
      progress: 100
    }
  ];

  var results = {
    'result-lpta': {
      cls: 'dt-result-lpta',
      title: 'LPTA Is Appropriate',
      body: 'For commercial commodities and nontechnical items, Lowest Price Technically Acceptable is generally the appropriate evaluation method. Ensure your solicitation clearly defines the minimum technical requirements that proposals must meet.',
      cite: 'FAR 15.101-2'
    },
    'result-lpta-813': {
      cls: 'dt-result-lpta',
      title: 'LPTA May Be Permissible',
      body: 'Although this is a DoD services acquisition subject to Section 813, LPTA may still be used if you can demonstrate that minimum requirements are clearly definable and exceeding them provides no added value. Document this determination thoroughly in your source selection plan.',
      cite: 'NDAA Section 813; DFARS 215.101-2-70'
    },
    'result-restricted': {
      cls: 'dt-result-restricted',
      title: 'LPTA Restricted by Section 813 \u2014 Use Tradeoff',
      body: 'This DoD services acquisition falls under NDAA Section 813 restrictions, and the requirements are not purely commodity-like. LPTA is not appropriate. Use a best-value tradeoff process that evaluates technical approach, past performance, and other quality factors alongside price.',
      cite: 'NDAA Section 813; DFARS 215.101-2-70'
    },
    'result-tradeoff': {
      cls: 'dt-result-tradeoff',
      title: 'Best-Value Tradeoff Recommended',
      body: 'When past performance and technical capability matter to contract success, a best-value tradeoff evaluation allows the government to select the proposal offering the greatest overall value\u2014not just the lowest price. Consider weighting technical and past performance factors appropriately.',
      cite: 'FAR 15.101-1'
    },
    'result-tradeoff-value': {
      cls: 'dt-result-tradeoff',
      title: 'Best-Value Tradeoff Recommended',
      body: 'For acquisitions above the simplified acquisition threshold, the additional cost and complexity of a tradeoff evaluation is generally warranted. Higher-value contracts carry greater performance risk, and evaluating quality factors helps the government make better award decisions.',
      cite: 'FAR 15.101-1'
    },
    'result-tradeoff-competition': {
      cls: 'dt-result-tradeoff',
      title: 'Best-Value Tradeoff Recommended',
      body: 'With multiple expected offerors, a tradeoff evaluation leverages competition on quality\u2014not just price. Research shows that best-value tradeoff yields the greatest performance benefits in competitive markets with three or more bidders.',
      cite: 'FAR 15.101-1'
    },
    'result-either': {
      cls: 'dt-result-either',
      title: 'Either Method May Be Appropriate',
      body: 'Based on your answers, this acquisition does not clearly favor one method over the other. For lower-value, nontechnical acquisitions with limited competition, LPTA can reduce evaluation burden. However, if there is any risk that a low-price award could result in poor performance, consider a tradeoff approach. Document your rationale in the source selection plan.',
      cite: 'FAR 15.101'
    }
  };

  function getQuestion(id) {
    for (var i = 0; i < questions.length; i++) {
      if (questions[i].id === id) return questions[i];
    }
    return null;
  }

  function renderQuestion(id) {
    var q = getQuestion(id);
    if (!q) return;

    container.innerHTML =
      '<div class="dt-progress">' +
        '<span>' + q.label + '</span>' +
        '<div class="dt-progress-bar"><div class="dt-progress-fill" style="width:' + q.progress + '%"></div></div>' +
      '</div>' +
      '<div class="dt-card">' +
        '<h3>Source Selection Decision</h3>' +
        '<p class="dt-question">' + q.text + '</p>' +
        '<p class="dt-hint">' + q.hint + '</p>' +
        '<div class="dt-buttons">' +
          '<button class="dt-btn dt-btn-yes">Yes</button>' +
          '<button class="dt-btn dt-btn-no">No</button>' +
        '</div>' +
      '</div>';
    container.querySelector('.dt-btn-yes').addEventListener('click', function() { window._dtAnswer(q.yes); });
    container.querySelector('.dt-btn-no').addEventListener('click', function() { window._dtAnswer(q.no); });
  }

  function renderResult(id) {
    var r = results[id];
    if (!r) return;

    container.innerHTML =
      '<div class="dt-progress">' +
        '<span>Recommendation</span>' +
        '<div class="dt-progress-bar"><div class="dt-progress-fill" style="width:100%"></div></div>' +
      '</div>' +
      '<div class="dt-result ' + r.cls + '">' +
        '<h3>' + r.title + '</h3>' +
        '<p>' + r.body + '</p>' +
        '<p class="dt-citation">Reference: ' + r.cite + '</p>' +
        '<button class="dt-start-over">Start Over</button>' +
      '</div>';
    container.querySelector('.dt-start-over').addEventListener('click', function() { window._dtStart(); });
  }

  window._dtAnswer = function(next) {
    if (next.indexOf('result') === 0) {
      renderResult(next);
    } else {
      renderQuestion(next);
    }
  };

  window._dtStart = function() {
    renderQuestion('q1');
  };

  window._dtStart();
})();
</script>

<div class="dt-disclaimer">
<strong>Disclaimer:</strong> This tool provides general guidance based on FAR 15.101, DFARS 215.101-2-70, and NDAA Section 813. It does not constitute legal advice. Contracting officers should consult their agency's source selection policies and legal counsel for specific acquisition decisions.
</div>

</div>

---

## The Evidence Behind This Tool

The decision logic in this tool is grounded in federal acquisition regulation, but the recommendation to favor best-value tradeoff for complex services is also supported by empirical research. In [Paper 1](/papers/paper1/), we use a difference-in-differences design to show that NDAA Section 813's restriction on LPTA in DoD services led to measurable improvements in contract outcomes, including reduced cost growth and fewer single-bid awards. [Paper 4](/papers/paper4/) examines the single-bid problem directly, finding that evaluation method choice is linked to competitive dynamics.

Perhaps most importantly, [Paper 2](/papers/paper2/) applies Transaction Cost Economics to show that evaluation method matters most for complex, smaller contracts in competitive markets. When the acquisition is technically complex, when contract values are moderate (not so large that other oversight mechanisms dominate), and when multiple firms are competing, best-value tradeoff delivers the greatest performance advantages over LPTA. These are precisely the conditions where contracting officers have the most discretion --- and where this decision tool can be most useful.
