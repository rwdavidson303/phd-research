#!/usr/bin/env python3
"""
Full Statistical Analysis for PhD Dissertation
"From Lowest Price to Highest Public Value"

Runs all analyses on the processed awards_analysis.csv dataset:
1. Descriptive statistics and sample characterization
2. Propensity score estimation and matching
3. Primary hypothesis tests (OLS, logistic, negative binomial)
4. Moderation/interaction effects
5. Robustness checks

Outputs tables and figures to analysis/output/
"""

import json
import os
import sys
import warnings
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import mannwhitneyu, chi2_contingency, kruskal

warnings.filterwarnings('ignore')

# Paths
PROJECT = Path(__file__).parent.parent
DATA = PROJECT / 'data' / 'processed' / 'awards_analysis.csv'
TABLES = PROJECT / 'analysis' / 'output' / 'tables'
FIGURES = PROJECT / 'analysis' / 'output' / 'figures'
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# Results collector
RESULTS = {}

###############################################################################
# LOAD DATA
###############################################################################
print("=" * 70)
print("LOADING DATA")
print("=" * 70)

df = pd.read_csv(DATA)
print(f"Total awards: {len(df):,}")
print(f"Columns: {len(df.columns)}")

# Create binary treatment variable: QUALITY_EVALUATING vs PRICE_FOCUSED/NEGOTIATED_FFP
# Main comparison: awards with quality evaluation signals vs price-focused
df['quality_eval'] = (df['procurement_design'] == 'QUALITY_EVALUATING').astype(int)
df['price_focused_narrow'] = (df['procurement_design'] == 'PRICE_FOCUSED').astype(int)

# Broader treatment: non-task-order awards with quality signals vs price signals
# For main analysis, compare QUALITY_EVALUATING vs NEGOTIATED_FFP (closest comparison)
df_main = df[df['procurement_design'].isin(['QUALITY_EVALUATING', 'NEGOTIATED_FFP'])].copy()
df_main['tradeoff'] = (df_main['procurement_design'] == 'QUALITY_EVALUATING').astype(int)

# Also create full-sample version with TASK_ORDER
df_full = df[df['procurement_design'].isin(['QUALITY_EVALUATING', 'NEGOTIATED_FFP', 'TASK_ORDER'])].copy()
df_full['tradeoff'] = (df_full['procurement_design'] == 'QUALITY_EVALUATING').astype(int)

print(f"\nMain analysis sample (QE vs NFP): {len(df_main):,}")
print(f"  QUALITY_EVALUATING (tradeoff=1): {df_main['tradeoff'].sum():,}")
print(f"  NEGOTIATED_FFP (tradeoff=0): {(1 - df_main['tradeoff']).sum():,}")
print(f"\nFull sample (QE vs NFP vs TO): {len(df_full):,}")

RESULTS['sample'] = {
    'total_awards': len(df),
    'main_sample': len(df_main),
    'quality_evaluating': int(df_main['tradeoff'].sum()),
    'negotiated_ffp': int((1 - df_main['tradeoff']).sum()),
    'full_sample': len(df_full),
    'task_order': int((df_full['procurement_design'] == 'TASK_ORDER').sum()),
}

###############################################################################
# 1. DESCRIPTIVE STATISTICS
###############################################################################
print("\n" + "=" * 70)
print("1. DESCRIPTIVE STATISTICS")
print("=" * 70)

# Table 1: Sample composition by procurement design
print("\n--- Table 4.1: Sample Composition ---")
comp = df.groupby('procurement_design').agg(
    n=('contract_award_unique_key', 'count'),
    mean_obligation=('federal_action_obligation', 'mean'),
    median_obligation=('federal_action_obligation', 'median'),
    mean_offers=('number_of_offers_received', 'mean'),
    pct_single_bid=('single_bid', 'mean'),
    mean_transactions=('transaction_count', 'mean'),
).round(3)
comp['pct_of_total'] = (comp['n'] / comp['n'].sum() * 100).round(1)
print(comp.to_string())
comp.to_csv(TABLES / 'table_4_1_sample_composition.csv')

# Table 2: Descriptive statistics for key variables
print("\n--- Table 4.2: Descriptive Statistics ---")
desc_vars = ['federal_action_obligation', 'log_award_amount', 'cost_growth_w',
             'transaction_count', 'number_of_offers_received', 'single_bid']
desc_labels = ['Award Amount ($)', 'Log Award Amount', 'Cost Growth (%)',
               'Modification Count', 'Number of Offers', 'Single-Bid Rate']

desc_stats = []
for var, label in zip(desc_vars, desc_labels):
    s = df[var].dropna()
    desc_stats.append({
        'Variable': label,
        'N': len(s),
        'Mean': s.mean(),
        'SD': s.std(),
        'Median': s.median(),
        'Min': s.min(),
        'Max': s.max(),
        'Skewness': s.skew(),
    })
desc_df = pd.DataFrame(desc_stats)
print(desc_df.to_string(index=False))
desc_df.to_csv(TABLES / 'table_4_2_descriptive_statistics.csv', index=False)

# Table 3: Comparison by procurement design (QE vs NFP)
print("\n--- Table 4.3: Treatment vs Control Comparison ---")
for group_name, group_df in [('Main (QE vs NFP)', df_main), ('Full (QE vs NFP vs TO)', df_full)]:
    print(f"\n  {group_name}:")
    for var in ['federal_action_obligation', 'log_award_amount', 'cost_growth_w',
                'transaction_count', 'number_of_offers_received', 'single_bid']:
        treat = group_df[group_df['tradeoff'] == 1][var].dropna()
        ctrl = group_df[group_df['tradeoff'] == 0][var].dropna()
        if len(treat) > 5 and len(ctrl) > 5:
            t_stat, p_val = stats.ttest_ind(treat, ctrl, equal_var=False)
            print(f"    {var:35s}: QE={treat.mean():.3f} vs Other={ctrl.mean():.3f}  "
                  f"t={t_stat:.3f} p={p_val:.4f}")

# By-group comparison table
comparison_rows = []
for var, label in zip(desc_vars, desc_labels):
    treat = df_main[df_main['tradeoff'] == 1][var].dropna()
    ctrl = df_main[df_main['tradeoff'] == 0][var].dropna()
    if len(treat) > 5 and len(ctrl) > 5:
        t_stat, p_val = stats.ttest_ind(treat, ctrl, equal_var=False)
        d = (treat.mean() - ctrl.mean()) / np.sqrt((treat.std()**2 + ctrl.std()**2) / 2)
        comparison_rows.append({
            'Variable': label,
            'QE Mean': treat.mean(),
            'QE SD': treat.std(),
            'NFP Mean': ctrl.mean(),
            'NFP SD': ctrl.std(),
            't-statistic': t_stat,
            'p-value': p_val,
            "Cohen's d": d,
        })
comparison_df = pd.DataFrame(comparison_rows)
comparison_df.to_csv(TABLES / 'table_4_3_group_comparison.csv', index=False)
print(comparison_df.to_string(index=False))

# NAICS sector breakdown
print("\n--- NAICS Sector Distribution ---")
naics_dist = df.groupby(['naics_2digit', 'procurement_design']).size().unstack(fill_value=0)
print(naics_dist)
naics_dist.to_csv(TABLES / 'table_4_naics_distribution.csv')

# Agency breakdown
print("\n--- Top 15 Agencies ---")
agency_counts = df['awarding_agency_name'].value_counts().head(15)
print(agency_counts)
agency_counts.to_csv(TABLES / 'table_4_agency_distribution.csv')

RESULTS['descriptive'] = {
    'comparison': comparison_rows,
    'n_naics_sectors': len(df['naics_2digit'].unique()),
    'n_agencies': len(df['awarding_agency_name'].unique()),
    'top_agency': str(agency_counts.index[0]),
}

###############################################################################
# 2. FIGURES
###############################################################################
print("\n" + "=" * 70)
print("2. GENERATING FIGURES")
print("=" * 70)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'figure.dpi': 150,
})

# Figure 1: Procurement design distribution
fig, ax = plt.subplots(figsize=(10, 6))
design_counts = df['procurement_design'].value_counts()
bars = ax.barh(design_counts.index, design_counts.values, color=['#2c3e50', '#2980b9', '#27ae60', '#e67e22', '#c0392b'])
ax.set_xlabel('Number of Awards')
ax.set_title('Distribution of Awards by Procurement Design Category')
for bar, val in zip(bars, design_counts.values):
    ax.text(val + 50, bar.get_y() + bar.get_height()/2, f'{val:,} ({val/len(df)*100:.1f}%)',
            va='center', fontsize=10)
plt.tight_layout()
plt.savefig(FIGURES / 'fig_4_1_procurement_design_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved fig_4_1")

# Figure 2: Award amount distribution by design
fig, ax = plt.subplots(figsize=(10, 6))
for design in ['QUALITY_EVALUATING', 'NEGOTIATED_FFP', 'TASK_ORDER']:
    subset = df[df['procurement_design'] == design]['log_award_amount'].dropna()
    ax.hist(subset, bins=40, alpha=0.5, label=design, density=True)
ax.set_xlabel('Log Award Amount')
ax.set_ylabel('Density')
ax.set_title('Distribution of Award Amounts by Procurement Design')
ax.legend()
plt.tight_layout()
plt.savefig(FIGURES / 'fig_4_2_award_amount_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved fig_4_2")

# Figure 3: Cost growth by procurement design (box plot)
fig, ax = plt.subplots(figsize=(10, 6))
designs = ['QUALITY_EVALUATING', 'NEGOTIATED_FFP', 'TASK_ORDER']
data_for_box = [df[df['procurement_design'] == d]['cost_growth_w'].dropna() for d in designs]
bp = ax.boxplot(data_for_box, labels=designs, patch_artist=True,
                boxprops=dict(facecolor='lightblue'),
                medianprops=dict(color='red', linewidth=2))
ax.set_ylabel('Cost Growth (%, Winsorized)')
ax.set_title('Cost Growth Distribution by Procurement Design')
ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(FIGURES / 'fig_4_3_cost_growth_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved fig_4_3")

# Figure 4: Single-bid rate by procurement design
fig, ax = plt.subplots(figsize=(10, 6))
single_bid_rates = df.groupby('procurement_design')['single_bid'].mean() * 100
bars = ax.bar(single_bid_rates.index, single_bid_rates.values, color=['#2c3e50', '#2980b9', '#27ae60', '#e67e22', '#c0392b'])
ax.set_ylabel('Single-Bid Rate (%)')
ax.set_title('Single-Bid Rate by Procurement Design Category')
for bar, val in zip(bars, single_bid_rates.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f'{val:.1f}%', ha='center', fontsize=10)
plt.tight_layout()
plt.savefig(FIGURES / 'fig_4_4_single_bid_rate.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved fig_4_4")

# Figure 5: Number of offers distribution
fig, ax = plt.subplots(figsize=(10, 6))
offers = df['number_of_offers_received'].dropna().clip(upper=20)
ax.hist(offers, bins=20, edgecolor='black', alpha=0.7, color='#2980b9')
ax.set_xlabel('Number of Offers Received')
ax.set_ylabel('Count')
ax.set_title('Distribution of Number of Offers Received')
ax.axvline(x=offers.median(), color='red', linestyle='--', label=f'Median={offers.median():.0f}')
ax.legend()
plt.tight_layout()
plt.savefig(FIGURES / 'fig_4_5_offers_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("  Saved fig_4_5")

###############################################################################
# 3. PROPENSITY SCORE MATCHING
###############################################################################
print("\n" + "=" * 70)
print("3. PROPENSITY SCORE MATCHING")
print("=" * 70)

try:
    import statsmodels.api as sm
    from statsmodels.stats.weightstats import ttest_ind as sm_ttest

    # Prepare matching dataset (QE vs NFP, complete cases)
    match_vars = ['log_award_amount', 'single_bid', 'transaction_count']
    psm_df = df_main[['tradeoff', 'cost_growth_w', 'number_of_offers_received',
                       'transaction_count', 'single_bid', 'log_award_amount',
                       'naics_2digit', 'awarding_agency_name',
                       'procurement_design', 'federal_action_obligation']].copy()

    # Create NAICS dummies
    top_naics = psm_df['naics_2digit'].value_counts().head(5).index
    for n in top_naics:
        psm_df[f'naics_{n}'] = (psm_df['naics_2digit'] == n).astype(int)

    # Create top agency dummies
    top_agencies = psm_df['awarding_agency_name'].value_counts().head(10).index
    for a in top_agencies:
        psm_df[f'agency_{a[:20].replace(" ","_")}'] = (psm_df['awarding_agency_name'] == a).astype(int)

    # Propensity score covariates
    ps_covariates = ['log_award_amount', 'transaction_count']
    ps_covariates += [c for c in psm_df.columns if c.startswith('naics_')]
    ps_covariates += [c for c in psm_df.columns if c.startswith('agency_')]

    # Drop rows with missing covariates
    psm_complete = psm_df.dropna(subset=ps_covariates + ['tradeoff'])
    print(f"PSM complete cases: {len(psm_complete):,}")
    print(f"  Treatment (QE): {psm_complete['tradeoff'].sum():,}")
    print(f"  Control (NFP): {(1 - psm_complete['tradeoff']).sum():,}")

    # Estimate propensity scores
    X = sm.add_constant(psm_complete[ps_covariates].astype(float))
    y = psm_complete['tradeoff'].astype(float)

    logit = sm.Logit(y, X)
    logit_result = logit.fit(disp=0)
    print("\n--- Propensity Score Model ---")
    print(f"Pseudo R-squared: {logit_result.prsquared:.4f}")
    print(f"Log-Likelihood: {logit_result.llf:.1f}")
    print(f"AIC: {logit_result.aic:.1f}")

    psm_complete['pscore'] = logit_result.predict(X)

    # Summary of propensity scores by group
    for g, label in [(1, 'Treatment (QE)'), (0, 'Control (NFP)')]:
        ps = psm_complete[psm_complete['tradeoff'] == g]['pscore']
        print(f"  {label}: mean={ps.mean():.4f}, sd={ps.std():.4f}, "
              f"min={ps.min():.4f}, max={ps.max():.4f}")

    # Nearest-neighbor matching with caliper
    print("\n--- Nearest-Neighbor Matching (1:1, caliper=0.05) ---")
    treated = psm_complete[psm_complete['tradeoff'] == 1].copy()
    control = psm_complete[psm_complete['tradeoff'] == 0].copy()

    caliper = 0.05
    matched_pairs = []
    used_controls = set()

    for idx, row in treated.iterrows():
        ps_t = row['pscore']
        # Find nearest control within caliper
        available = control[~control.index.isin(used_controls)]
        distances = (available['pscore'] - ps_t).abs()
        within_caliper = distances[distances <= caliper]

        if len(within_caliper) > 0:
            best_match = within_caliper.idxmin()
            matched_pairs.append((idx, best_match))
            used_controls.add(best_match)

    print(f"Matched pairs: {len(matched_pairs):,}")
    print(f"Unmatched treated: {len(treated) - len(matched_pairs):,}")

    if matched_pairs:
        treated_idx = [p[0] for p in matched_pairs]
        control_idx = [p[1] for p in matched_pairs]
        matched_treated = psm_complete.loc[treated_idx]
        matched_control = psm_complete.loc[control_idx]
        matched_sample = pd.concat([matched_treated, matched_control])

        print(f"Matched sample size: {len(matched_sample):,}")

        # Balance diagnostics
        print("\n--- Balance Diagnostics (Standardized Mean Differences) ---")
        balance_rows = []
        for var in ['log_award_amount', 'transaction_count'] + [c for c in psm_complete.columns if c.startswith('naics_')][:5]:
            t_pre = psm_complete[psm_complete['tradeoff'] == 1][var].dropna()
            c_pre = psm_complete[psm_complete['tradeoff'] == 0][var].dropna()
            smd_pre = (t_pre.mean() - c_pre.mean()) / np.sqrt((t_pre.std()**2 + c_pre.std()**2) / 2)

            t_post = matched_treated[var].dropna()
            c_post = matched_control[var].dropna()
            smd_post = (t_post.mean() - c_post.mean()) / np.sqrt((t_post.std()**2 + c_post.std()**2) / 2) if len(t_post) > 0 and len(c_post) > 0 else np.nan

            balance_rows.append({
                'Variable': var,
                'SMD Before': smd_pre,
                'SMD After': smd_post,
                'Reduction (%)': (1 - abs(smd_post) / max(abs(smd_pre), 0.001)) * 100 if not np.isnan(smd_post) else np.nan,
            })
            print(f"  {var:30s}: Before={smd_pre:+.4f}  After={smd_post:+.4f}")

        balance_df = pd.DataFrame(balance_rows)
        balance_df.to_csv(TABLES / 'table_4_4_psm_balance.csv', index=False)

        RESULTS['psm'] = {
            'matched_pairs': len(matched_pairs),
            'unmatched': len(treated) - len(matched_pairs),
            'pseudo_r2': float(logit_result.prsquared),
            'balance': balance_rows,
        }

        # Figure: Propensity score distribution before/after matching
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Before matching
        axes[0].hist(psm_complete[psm_complete['tradeoff'] == 1]['pscore'], bins=30, alpha=0.5,
                     label='QE (Treatment)', density=True, color='#2980b9')
        axes[0].hist(psm_complete[psm_complete['tradeoff'] == 0]['pscore'], bins=30, alpha=0.5,
                     label='NFP (Control)', density=True, color='#e74c3c')
        axes[0].set_title('Before Matching')
        axes[0].set_xlabel('Propensity Score')
        axes[0].set_ylabel('Density')
        axes[0].legend()

        # After matching
        axes[1].hist(matched_treated['pscore'], bins=30, alpha=0.5,
                     label='QE (Treatment)', density=True, color='#2980b9')
        axes[1].hist(matched_control['pscore'], bins=30, alpha=0.5,
                     label='NFP (Control)', density=True, color='#e74c3c')
        axes[1].set_title('After Matching')
        axes[1].set_xlabel('Propensity Score')
        axes[1].legend()

        plt.suptitle('Propensity Score Distribution: Before and After Matching', fontsize=14)
        plt.tight_layout()
        plt.savefig(FIGURES / 'fig_4_6_psm_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("  Saved fig_4_6")

        # SMD balance plot
        fig, ax = plt.subplots(figsize=(8, 6))
        y_pos = range(len(balance_df))
        ax.scatter(balance_df['SMD Before'], y_pos, marker='o', color='red', label='Before Matching', s=80)
        ax.scatter(balance_df['SMD After'], y_pos, marker='s', color='blue', label='After Matching', s=80)
        ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
        ax.axvline(x=0.1, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=-0.1, color='gray', linestyle='--', alpha=0.5)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(balance_df['Variable'], fontsize=9)
        ax.set_xlabel('Standardized Mean Difference')
        ax.set_title('Covariate Balance: Before and After Matching')
        ax.legend()
        plt.tight_layout()
        plt.savefig(FIGURES / 'fig_4_7_balance_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("  Saved fig_4_7")

    else:
        matched_sample = None
        print("  WARNING: No matched pairs found")

except Exception as e:
    print(f"PSM Error: {e}")
    import traceback
    traceback.print_exc()
    matched_sample = None

###############################################################################
# 4. PRIMARY HYPOTHESIS TESTS
###############################################################################
print("\n" + "=" * 70)
print("4. PRIMARY HYPOTHESIS TESTS")
print("=" * 70)

try:
    import statsmodels.api as sm
    from statsmodels.genmod.generalized_linear_model import GLM
    from statsmodels.genmod.families import Gaussian, Poisson, Binomial
    import statsmodels.formula.api as smf

    # Prepare regression dataset
    reg_df = df_main.copy()

    # Create dummies for top NAICS sectors
    top_naics = reg_df['naics_2digit'].value_counts().head(4).index
    for n in top_naics:
        reg_df[f'naics_{n}'] = (reg_df['naics_2digit'] == n).astype(int)

    # Create dummies for top agencies
    top_agencies = reg_df['awarding_agency_name'].value_counts().head(8).index
    for a in top_agencies:
        safe_name = a[:20].replace(" ", "_").replace(",", "").replace(".", "")
        reg_df[f'agency_{safe_name}'] = (reg_df['awarding_agency_name'] == a).astype(int)

    naics_dummies = [c for c in reg_df.columns if c.startswith('naics_') and c != 'naics_2digit' and c != 'naics_4digit' and c != 'naics_code' and c != 'naics_description']
    agency_dummies = [c for c in reg_df.columns if c.startswith('agency_')]

    controls = ['log_award_amount'] + naics_dummies[:3] + agency_dummies[:5]

    regression_results = {}

    # H1: Cost growth ~ tradeoff + controls
    print("\n--- H1: Cost Growth (OLS) ---")
    h1_df = reg_df.dropna(subset=['cost_growth_w', 'tradeoff'] + controls)
    if len(h1_df) > 50:
        X = sm.add_constant(h1_df[['tradeoff'] + controls].astype(float))
        y = h1_df['cost_growth_w'].astype(float)
        ols = sm.OLS(y, X).fit(cov_type='HC3')
        print(f"  N = {int(ols.nobs):,}")
        print(f"  R-squared = {ols.rsquared:.4f}")
        print(f"  Tradeoff coef = {ols.params['tradeoff']:.4f} (SE={ols.bse['tradeoff']:.4f}, p={ols.pvalues['tradeoff']:.4f})")
        print(f"  F-statistic = {ols.fvalue:.2f} (p={ols.f_pvalue:.4f})")

        regression_results['H1_cost_growth'] = {
            'model': 'OLS',
            'dv': 'Cost Growth (Winsorized %)',
            'n': int(ols.nobs),
            'r_squared': float(ols.rsquared),
            'tradeoff_coef': float(ols.params['tradeoff']),
            'tradeoff_se': float(ols.bse['tradeoff']),
            'tradeoff_p': float(ols.pvalues['tradeoff']),
            'tradeoff_ci_low': float(ols.conf_int().loc['tradeoff', 0]),
            'tradeoff_ci_high': float(ols.conf_int().loc['tradeoff', 1]),
            'f_stat': float(ols.fvalue),
            'f_p': float(ols.f_pvalue),
        }

        # Save full table
        h1_table = pd.DataFrame({
            'Variable': ols.params.index,
            'Coefficient': ols.params.values,
            'Std Error': ols.bse.values,
            't-statistic': ols.tvalues.values,
            'p-value': ols.pvalues.values,
            'CI Lower': ols.conf_int()[0].values,
            'CI Upper': ols.conf_int()[1].values,
        })
        h1_table.to_csv(TABLES / 'table_4_5_h1_cost_growth_ols.csv', index=False)

    # H2: Modification intensity ~ tradeoff + controls (Negative Binomial)
    print("\n--- H2: Modification Intensity (Negative Binomial) ---")
    h2_df = reg_df.dropna(subset=['transaction_count', 'tradeoff'] + controls)
    if len(h2_df) > 50:
        X = sm.add_constant(h2_df[['tradeoff'] + controls].astype(float))
        y = h2_df['transaction_count'].astype(float)

        try:
            nb = sm.GLM(y, X, family=sm.families.NegativeBinomial()).fit()
            print(f"  N = {int(nb.nobs):,}")
            print(f"  Tradeoff coef = {nb.params['tradeoff']:.4f} (SE={nb.bse['tradeoff']:.4f}, p={nb.pvalues['tradeoff']:.4f})")
            print(f"  Deviance = {nb.deviance:.2f}")

            regression_results['H2_modifications'] = {
                'model': 'Negative Binomial GLM',
                'dv': 'Transaction Count',
                'n': int(nb.nobs),
                'tradeoff_coef': float(nb.params['tradeoff']),
                'tradeoff_se': float(nb.bse['tradeoff']),
                'tradeoff_p': float(nb.pvalues['tradeoff']),
                'tradeoff_ci_low': float(nb.conf_int().loc['tradeoff', 0]),
                'tradeoff_ci_high': float(nb.conf_int().loc['tradeoff', 1]),
                'deviance': float(nb.deviance),
                'aic': float(nb.aic),
            }

            h2_table = pd.DataFrame({
                'Variable': nb.params.index,
                'Coefficient': nb.params.values,
                'Std Error': nb.bse.values,
                'z-statistic': nb.tvalues.values,
                'p-value': nb.pvalues.values,
            })
            h2_table.to_csv(TABLES / 'table_4_6_h2_modifications_nb.csv', index=False)

        except Exception as e:
            print(f"  NB failed ({e}), falling back to Poisson")
            pois = sm.GLM(y, X, family=sm.families.Poisson()).fit()
            print(f"  N = {int(pois.nobs):,}")
            print(f"  Tradeoff coef = {pois.params['tradeoff']:.4f} (SE={pois.bse['tradeoff']:.4f}, p={pois.pvalues['tradeoff']:.4f})")

            regression_results['H2_modifications'] = {
                'model': 'Poisson GLM',
                'dv': 'Transaction Count',
                'n': int(pois.nobs),
                'tradeoff_coef': float(pois.params['tradeoff']),
                'tradeoff_se': float(pois.bse['tradeoff']),
                'tradeoff_p': float(pois.pvalues['tradeoff']),
                'deviance': float(pois.deviance),
            }

    # H6: Single-bid indicator ~ tradeoff + controls (Logistic)
    print("\n--- H6: Single-Bid Indicator (Logistic) ---")
    h6_df = reg_df.dropna(subset=['single_bid', 'tradeoff'] + controls)
    if len(h6_df) > 50:
        X = sm.add_constant(h6_df[['tradeoff'] + controls].astype(float))
        y = h6_df['single_bid'].astype(float)

        logit = sm.Logit(y, X).fit(disp=0)
        print(f"  N = {int(logit.nobs):,}")
        print(f"  Pseudo R-squared = {logit.prsquared:.4f}")
        print(f"  Tradeoff coef = {logit.params['tradeoff']:.4f} (SE={logit.bse['tradeoff']:.4f}, p={logit.pvalues['tradeoff']:.4f})")
        print(f"  Tradeoff OR = {np.exp(logit.params['tradeoff']):.4f}")

        regression_results['H6_single_bid'] = {
            'model': 'Logistic',
            'dv': 'Single-Bid Indicator',
            'n': int(logit.nobs),
            'pseudo_r2': float(logit.prsquared),
            'tradeoff_coef': float(logit.params['tradeoff']),
            'tradeoff_se': float(logit.bse['tradeoff']),
            'tradeoff_p': float(logit.pvalues['tradeoff']),
            'tradeoff_or': float(np.exp(logit.params['tradeoff'])),
            'tradeoff_or_ci_low': float(np.exp(logit.conf_int().loc['tradeoff', 0])),
            'tradeoff_or_ci_high': float(np.exp(logit.conf_int().loc['tradeoff', 1])),
            'aic': float(logit.aic),
        }

        h6_table = pd.DataFrame({
            'Variable': logit.params.index,
            'Coefficient': logit.params.values,
            'Std Error': logit.bse.values,
            'z-statistic': logit.tvalues.values,
            'p-value': logit.pvalues.values,
            'Odds Ratio': np.exp(logit.params.values),
        })
        h6_table.to_csv(TABLES / 'table_4_7_h6_single_bid_logit.csv', index=False)

    # Competition intensity (number of offers) ~ tradeoff + controls
    print("\n--- Competition Intensity (OLS) ---")
    comp_df = reg_df.dropna(subset=['number_of_offers_received', 'tradeoff'] + controls)
    if len(comp_df) > 50:
        X = sm.add_constant(comp_df[['tradeoff'] + controls].astype(float))
        y = comp_df['number_of_offers_received'].astype(float)
        ols_comp = sm.OLS(y, X).fit(cov_type='HC3')
        print(f"  N = {int(ols_comp.nobs):,}")
        print(f"  R-squared = {ols_comp.rsquared:.4f}")
        print(f"  Tradeoff coef = {ols_comp.params['tradeoff']:.4f} (SE={ols_comp.bse['tradeoff']:.4f}, p={ols_comp.pvalues['tradeoff']:.4f})")

        regression_results['competition_intensity'] = {
            'model': 'OLS',
            'dv': 'Number of Offers',
            'n': int(ols_comp.nobs),
            'r_squared': float(ols_comp.rsquared),
            'tradeoff_coef': float(ols_comp.params['tradeoff']),
            'tradeoff_se': float(ols_comp.bse['tradeoff']),
            'tradeoff_p': float(ols_comp.pvalues['tradeoff']),
        }

    ###########################################################################
    # 5. PSM-MATCHED SAMPLE REGRESSIONS
    ###########################################################################
    if matched_sample is not None and len(matched_sample) > 50:
        print("\n" + "=" * 70)
        print("5. PSM-MATCHED SAMPLE REGRESSIONS")
        print("=" * 70)

        psm_regression_results = {}

        # H1 on matched sample
        print("\n--- H1 (Matched): Cost Growth ---")
        h1m = matched_sample.dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
        if len(h1m) > 20:
            X = sm.add_constant(h1m[['tradeoff', 'log_award_amount']].astype(float))
            y = h1m['cost_growth_w'].astype(float)
            ols_m = sm.OLS(y, X).fit(cov_type='HC3')
            print(f"  N = {int(ols_m.nobs):,}")
            print(f"  Tradeoff coef = {ols_m.params['tradeoff']:.4f} (p={ols_m.pvalues['tradeoff']:.4f})")

            psm_regression_results['H1_matched'] = {
                'n': int(ols_m.nobs),
                'tradeoff_coef': float(ols_m.params['tradeoff']),
                'tradeoff_p': float(ols_m.pvalues['tradeoff']),
                'r_squared': float(ols_m.rsquared),
            }

        # H6 on matched sample
        print("\n--- H6 (Matched): Single-Bid ---")
        h6m = matched_sample.dropna(subset=['single_bid', 'tradeoff', 'log_award_amount'])
        if len(h6m) > 20:
            X = sm.add_constant(h6m[['tradeoff', 'log_award_amount']].astype(float))
            y = h6m['single_bid'].astype(float)
            logit_m = sm.Logit(y, X).fit(disp=0)
            print(f"  N = {int(logit_m.nobs):,}")
            print(f"  Tradeoff coef = {logit_m.params['tradeoff']:.4f} (p={logit_m.pvalues['tradeoff']:.4f})")
            print(f"  Tradeoff OR = {np.exp(logit_m.params['tradeoff']):.4f}")

            psm_regression_results['H6_matched'] = {
                'n': int(logit_m.nobs),
                'tradeoff_coef': float(logit_m.params['tradeoff']),
                'tradeoff_p': float(logit_m.pvalues['tradeoff']),
                'tradeoff_or': float(np.exp(logit_m.params['tradeoff'])),
            }

        regression_results['psm_matched'] = psm_regression_results

    ###########################################################################
    # 6. MODERATION / INTERACTION EFFECTS
    ###########################################################################
    print("\n" + "=" * 70)
    print("6. MODERATION EFFECTS")
    print("=" * 70)

    # H8: Complexity moderation (NAICS sector as proxy)
    print("\n--- H8: Complexity Moderation (Award Size x Tradeoff) ---")
    int_df = reg_df.dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
    int_df['tradeoff_x_size'] = int_df['tradeoff'] * int_df['log_award_amount']

    X = sm.add_constant(int_df[['tradeoff', 'log_award_amount', 'tradeoff_x_size']].astype(float))
    y = int_df['cost_growth_w'].astype(float)
    ols_int = sm.OLS(y, X).fit(cov_type='HC3')
    print(f"  N = {int(ols_int.nobs):,}")
    print(f"  Tradeoff coef = {ols_int.params['tradeoff']:.4f} (p={ols_int.pvalues['tradeoff']:.4f})")
    print(f"  Size coef = {ols_int.params['log_award_amount']:.4f} (p={ols_int.pvalues['log_award_amount']:.4f})")
    print(f"  Interaction coef = {ols_int.params['tradeoff_x_size']:.4f} (p={ols_int.pvalues['tradeoff_x_size']:.4f})")

    regression_results['H8_moderation'] = {
        'model': 'OLS with interaction',
        'n': int(ols_int.nobs),
        'tradeoff_coef': float(ols_int.params['tradeoff']),
        'tradeoff_p': float(ols_int.pvalues['tradeoff']),
        'size_coef': float(ols_int.params['log_award_amount']),
        'size_p': float(ols_int.pvalues['log_award_amount']),
        'interaction_coef': float(ols_int.params['tradeoff_x_size']),
        'interaction_p': float(ols_int.pvalues['tradeoff_x_size']),
        'r_squared': float(ols_int.rsquared),
    }

    # Marginal effects plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sizes = np.linspace(int_df['log_award_amount'].quantile(0.05),
                        int_df['log_award_amount'].quantile(0.95), 50)
    me_tradeoff = ols_int.params['tradeoff'] + ols_int.params['tradeoff_x_size'] * sizes
    se_tradeoff = np.sqrt(
        ols_int.cov_params().loc['tradeoff', 'tradeoff'] +
        2 * sizes * ols_int.cov_params().loc['tradeoff', 'tradeoff_x_size'] +
        sizes**2 * ols_int.cov_params().loc['tradeoff_x_size', 'tradeoff_x_size']
    )
    ax.plot(sizes, me_tradeoff, color='#2980b9', linewidth=2)
    ax.fill_between(sizes, me_tradeoff - 1.96*se_tradeoff, me_tradeoff + 1.96*se_tradeoff,
                    alpha=0.2, color='#2980b9')
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Log Award Amount')
    ax.set_ylabel('Marginal Effect of Quality-Evaluating Design')
    ax.set_title('Marginal Effect of Tradeoff on Cost Growth by Award Size')
    plt.tight_layout()
    plt.savefig(FIGURES / 'fig_4_8_marginal_effects.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved fig_4_8")

    ###########################################################################
    # 7. ROBUSTNESS CHECKS
    ###########################################################################
    print("\n" + "=" * 70)
    print("7. ROBUSTNESS CHECKS")
    print("=" * 70)

    robustness_results = {}

    # 7a: Include TASK_ORDER in the comparison
    print("\n--- 7a: Full Sample (including Task Orders) ---")
    full_reg = df_full.copy()
    full_reg['is_task_order'] = (full_reg['procurement_design'] == 'TASK_ORDER').astype(int)
    full_complete = full_reg.dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
    if len(full_complete) > 50:
        X = sm.add_constant(full_complete[['tradeoff', 'is_task_order', 'log_award_amount']].astype(float))
        y = full_complete['cost_growth_w'].astype(float)
        ols_full = sm.OLS(y, X).fit(cov_type='HC3')
        print(f"  N = {int(ols_full.nobs):,}")
        print(f"  Tradeoff coef = {ols_full.params['tradeoff']:.4f} (p={ols_full.pvalues['tradeoff']:.4f})")
        print(f"  Task Order coef = {ols_full.params['is_task_order']:.4f} (p={ols_full.pvalues['is_task_order']:.4f})")
        robustness_results['full_sample'] = {
            'n': int(ols_full.nobs),
            'tradeoff_coef': float(ols_full.params['tradeoff']),
            'tradeoff_p': float(ols_full.pvalues['tradeoff']),
        }

    # 7b: Subsample by agency size
    print("\n--- 7b: Subsample by Large vs Small Agency ---")
    agency_sizes = reg_df['awarding_agency_name'].value_counts()
    large_agencies = agency_sizes[agency_sizes >= agency_sizes.median()].index
    for label, mask in [('Large Agency', reg_df['awarding_agency_name'].isin(large_agencies)),
                        ('Small Agency', ~reg_df['awarding_agency_name'].isin(large_agencies))]:
        sub = reg_df[mask].dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
        if len(sub) > 30:
            X = sm.add_constant(sub[['tradeoff', 'log_award_amount']].astype(float))
            y = sub['cost_growth_w'].astype(float)
            ols_sub = sm.OLS(y, X).fit(cov_type='HC3')
            print(f"  {label}: N={int(ols_sub.nobs):,}, "
                  f"Tradeoff={ols_sub.params['tradeoff']:.4f} (p={ols_sub.pvalues['tradeoff']:.4f})")
            robustness_results[f'agency_{label.lower().replace(" ","_")}'] = {
                'n': int(ols_sub.nobs),
                'tradeoff_coef': float(ols_sub.params['tradeoff']),
                'tradeoff_p': float(ols_sub.pvalues['tradeoff']),
            }

    # 7c: Alternative outcome - raw cost growth (not winsorized)
    print("\n--- 7c: Raw Cost Growth (Not Winsorized) ---")
    h1_raw = reg_df.dropna(subset=['cost_growth', 'tradeoff', 'log_award_amount'])
    if len(h1_raw) > 50:
        X = sm.add_constant(h1_raw[['tradeoff', 'log_award_amount']].astype(float))
        y = h1_raw['cost_growth'].astype(float)
        ols_raw = sm.OLS(y, X).fit(cov_type='HC3')
        print(f"  N = {int(ols_raw.nobs):,}, Tradeoff = {ols_raw.params['tradeoff']:.4f} (p={ols_raw.pvalues['tradeoff']:.4f})")
        robustness_results['raw_cost_growth'] = {
            'n': int(ols_raw.nobs),
            'tradeoff_coef': float(ols_raw.params['tradeoff']),
            'tradeoff_p': float(ols_raw.pvalues['tradeoff']),
        }

    # 7d: Exclude outliers (cost_growth_w beyond 3 SD)
    print("\n--- 7d: Excluding Outliers (>3 SD) ---")
    cg_mean = reg_df['cost_growth_w'].mean()
    cg_std = reg_df['cost_growth_w'].std()
    no_outliers = reg_df[(reg_df['cost_growth_w'] >= cg_mean - 3*cg_std) &
                         (reg_df['cost_growth_w'] <= cg_mean + 3*cg_std)]
    no_outliers = no_outliers.dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
    if len(no_outliers) > 50:
        X = sm.add_constant(no_outliers[['tradeoff', 'log_award_amount']].astype(float))
        y = no_outliers['cost_growth_w'].astype(float)
        ols_no = sm.OLS(y, X).fit(cov_type='HC3')
        print(f"  N = {int(ols_no.nobs):,}, Tradeoff = {ols_no.params['tradeoff']:.4f} (p={ols_no.pvalues['tradeoff']:.4f})")
        robustness_results['no_outliers'] = {
            'n': int(ols_no.nobs),
            'tradeoff_coef': float(ols_no.params['tradeoff']),
            'tradeoff_p': float(ols_no.pvalues['tradeoff']),
        }

    # 7e: By NAICS sector
    print("\n--- 7e: By NAICS Sector ---")
    for sector in reg_df['naics_2digit'].value_counts().head(3).index:
        sub = reg_df[reg_df['naics_2digit'] == sector].dropna(subset=['cost_growth_w', 'tradeoff', 'log_award_amount'])
        if len(sub) > 30:
            X = sm.add_constant(sub[['tradeoff', 'log_award_amount']].astype(float))
            y = sub['cost_growth_w'].astype(float)
            ols_sec = sm.OLS(y, X).fit(cov_type='HC3')
            print(f"  NAICS {sector}: N={int(ols_sec.nobs):,}, "
                  f"Tradeoff={ols_sec.params['tradeoff']:.4f} (p={ols_sec.pvalues['tradeoff']:.4f})")
            robustness_results[f'naics_{sector}'] = {
                'n': int(ols_sec.nobs),
                'tradeoff_coef': float(ols_sec.params['tradeoff']),
                'tradeoff_p': float(ols_sec.pvalues['tradeoff']),
            }

    regression_results['robustness'] = robustness_results

    # Robustness comparison table
    robust_rows = []
    for key, vals in robustness_results.items():
        robust_rows.append({
            'Specification': key,
            'N': vals['n'],
            'Tradeoff Coefficient': vals['tradeoff_coef'],
            'p-value': vals['tradeoff_p'],
        })
    robust_df = pd.DataFrame(robust_rows)
    robust_df.to_csv(TABLES / 'table_4_8_robustness_checks.csv', index=False)
    print("\nRobustness Summary:")
    print(robust_df.to_string(index=False))

    RESULTS['regressions'] = regression_results

except Exception as e:
    print(f"Regression Error: {e}")
    import traceback
    traceback.print_exc()

###############################################################################
# 8. SUMMARY OF FINDINGS
###############################################################################
print("\n" + "=" * 70)
print("8. SUMMARY OF FINDINGS BY HYPOTHESIS")
print("=" * 70)

summary_rows = []
if 'regressions' in RESULTS:
    regs = RESULTS['regressions']

    if 'H1_cost_growth' in regs:
        r = regs['H1_cost_growth']
        supported = 'Supported' if r['tradeoff_p'] < 0.05 else 'Not Supported'
        direction = 'higher' if r['tradeoff_coef'] > 0 else 'lower'
        summary_rows.append({
            'Hypothesis': 'H1',
            'Description': 'Best-value tradeoff reduces cost growth',
            'Model': r['model'],
            'N': r['n'],
            'Coefficient': r['tradeoff_coef'],
            'p-value': r['tradeoff_p'],
            'Result': supported,
            'Note': f'QE design associated with {direction} cost growth',
        })

    if 'H2_modifications' in regs:
        r = regs['H2_modifications']
        supported = 'Supported' if r['tradeoff_p'] < 0.05 else 'Not Supported'
        summary_rows.append({
            'Hypothesis': 'H2',
            'Description': 'Best-value tradeoff reduces renegotiation',
            'Model': r['model'],
            'N': r['n'],
            'Coefficient': r['tradeoff_coef'],
            'p-value': r['tradeoff_p'],
            'Result': supported,
            'Note': '',
        })

    if 'H6_single_bid' in regs:
        r = regs['H6_single_bid']
        supported = 'Supported' if r['tradeoff_p'] < 0.05 else 'Not Supported'
        summary_rows.append({
            'Hypothesis': 'H6',
            'Description': 'Single-bid rates lower under tradeoff',
            'Model': r['model'],
            'N': r['n'],
            'Coefficient': r['tradeoff_coef'],
            'p-value': r['tradeoff_p'],
            'Result': supported,
            'Note': f'OR = {r.get("tradeoff_or", "N/A")}',
        })

    if 'H8_moderation' in regs:
        r = regs['H8_moderation']
        supported = 'Supported' if r['interaction_p'] < 0.05 else 'Not Supported'
        summary_rows.append({
            'Hypothesis': 'H8',
            'Description': 'Complexity moderates tradeoff effect',
            'Model': r['model'],
            'N': r['n'],
            'Coefficient': r['interaction_coef'],
            'p-value': r['interaction_p'],
            'Result': supported,
            'Note': 'Award size as complexity proxy',
        })

summary_df = pd.DataFrame(summary_rows)
if len(summary_df) > 0:
    summary_df.to_csv(TABLES / 'table_4_9_hypothesis_summary.csv', index=False)
    print(summary_df.to_string(index=False))

###############################################################################
# SAVE ALL RESULTS
###############################################################################
results_path = PROJECT / 'analysis' / 'output' / 'analysis_results.json'

# Convert numpy types for JSON serialization
def convert_types(obj):
    if isinstance(obj, (np.integer,)):
        return int(obj)
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_types(i) for i in obj]
    return obj

with open(results_path, 'w') as f:
    json.dump(convert_types(RESULTS), f, indent=2)

print(f"\n{'='*70}")
print(f"ANALYSIS COMPLETE")
print(f"{'='*70}")
print(f"Results saved to: {results_path}")
print(f"Tables saved to: {TABLES}")
print(f"Figures saved to: {FIGURES}")
