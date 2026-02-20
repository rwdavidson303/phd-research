#!/usr/bin/env python3
"""
Data Processing Pipeline for PhD Dissertation

Loads raw USAspending transaction-level CSV files, aggregates to award level,
classifies source selection method, applies sampling criteria, and constructs
all analysis variables.

Input:  data/raw/usaspending/*.csv (transaction-level)
Output: data/processed/awards_analysis.csv (award-level, analysis-ready)

Usage:
    python clean_and_process.py
    python clean_and_process.py --raw-dir /path/to/csvs
"""

import argparse
import glob
import os
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw" / "usaspending"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# NAICS codes for service/IT procurement (dissertation focus)
SERVICE_IT_NAICS_PREFIXES = ["5411", "5415", "5416", "5418", "5182", "5112", "5611", "5612"]

# Simplified acquisition threshold
SAT = 250000

# Source selection codes of interest
VALID_SOURCE_SELECTION = ["LPTA", "TO"]  # Lowest Price Technically Acceptable, Tradeoff


def find_csv_files(raw_dir):
    """Find all CSV files in the raw data directory."""
    csv_files = sorted(Path(raw_dir).rglob("*.csv"))
    csv_files = [f for f in csv_files if "manifest" not in f.name.lower()]
    print(f"Found {len(csv_files)} CSV file(s) in {raw_dir}")
    for f in csv_files:
        size_mb = f.stat().st_size / 1e6
        print(f"  {f.name} ({size_mb:.1f} MB)")
    return csv_files


def load_raw_data(csv_files):
    """Load and concatenate all transaction-level CSV files."""
    dfs = []
    for f in csv_files:
        print(f"Loading {f.name}...")
        try:
            df = pd.read_csv(f, low_memory=False, dtype=str)
            dfs.append(df)
            print(f"  Loaded {len(df):,} rows, {len(df.columns)} columns")
        except Exception as e:
            print(f"  ERROR loading {f.name}: {e}")

    if not dfs:
        print("ERROR: No data loaded. Check that CSV files exist in the raw directory.")
        sys.exit(1)

    data = pd.concat(dfs, ignore_index=True)
    print(f"\nTotal transactions loaded: {len(data):,}")
    print(f"Columns: {len(data.columns)}")
    return data


def identify_columns(df):
    """Identify key column names (they vary across download formats)."""
    cols = {c.lower().strip(): c for c in df.columns}

    # Map expected fields to actual column names
    field_map = {}

    # Source selection process
    for candidate in ['source_selection_process', 'evaluated_preference',
                      'source_selection_process_description']:
        for k, v in cols.items():
            if candidate in k:
                field_map['source_selection'] = v
                break
        if 'source_selection' in field_map:
            break

    # Award identifiers
    for candidate in ['award_id_piid', 'piid', 'contract_award_unique_key',
                      'award_id_fain', 'unique_award_key']:
        for k, v in cols.items():
            if candidate in k:
                field_map['award_id'] = v
                break
        if 'award_id' in field_map:
            break

    # Agency
    for candidate in ['awarding_agency_name', 'awarding_agency',
                      'awarding_toptier_agency_name']:
        for k, v in cols.items():
            if candidate in k:
                field_map['agency'] = v
                break
        if 'agency' in field_map:
            break

    # Sub-agency
    for candidate in ['awarding_sub_agency_name', 'awarding_subtier_agency_name']:
        for k, v in cols.items():
            if candidate in k:
                field_map['sub_agency'] = v
                break
        if 'sub_agency' in field_map:
            break

    # Amounts
    for label, candidates in {
        'obligation': ['federal_action_obligation', 'total_dollars_obligated',
                       'federal_action_obligation_amount'],
        'base_value': ['base_and_exercised_options_value',
                       'base_exercised_options_val'],
        'total_value': ['base_and_all_options_value',
                        'base_all_options_value'],
        'current_value': ['current_total_value_of_award',
                          'current_total_value_award'],
    }.items():
        for candidate in candidates:
            for k, v in cols.items():
                if candidate in k:
                    field_map[label] = v
                    break
            if label in field_map:
                break

    # Competition
    for candidate in ['number_of_offers_received', 'number_of_offers']:
        for k, v in cols.items():
            if candidate in k:
                field_map['num_offers'] = v
                break
        if 'num_offers' in field_map:
            break

    for candidate in ['extent_competed', 'extent_competed_description']:
        for k, v in cols.items():
            if candidate in k:
                field_map['extent_competed'] = v
                break
        if 'extent_competed' in field_map:
            break

    # Contract characteristics
    for label, candidates in {
        'naics': ['naics_code', 'naics'],
        'psc': ['product_or_service_code', 'product_service_code', 'psc_code'],
        'contract_type': ['type_of_contract_pricing',
                          'type_of_contract_pricing_description'],
        'award_type': ['contract_award_type', 'award_type',
                       'contract_award_type_description'],
        'set_aside': ['type_set_aside', 'type_of_set_aside',
                      'type_set_aside_description'],
        'action_date': ['action_date', 'date_signed'],
        'start_date': ['period_of_performance_start_date',
                       'period_of_perf_start_date'],
        'end_date': ['period_of_performance_current_end_date',
                     'period_of_perf_current_end_date'],
        'modification_number': ['modification_number', 'mod_number'],
        'recipient': ['recipient_name', 'vendor_name',
                      'recipient_dba_name'],
        'action_type': ['action_type', 'action_type_description',
                        'contract_action_type'],
    }.items():
        for candidate in candidates:
            for k, v in cols.items():
                if candidate in k:
                    field_map[label] = v
                    break
            if label in field_map:
                break

    print(f"\nColumn mapping ({len(field_map)} fields identified):")
    for label, col in sorted(field_map.items()):
        print(f"  {label:25s} -> {col}")

    # Report missing
    expected = ['award_id', 'agency', 'source_selection', 'obligation',
                'num_offers', 'extent_competed', 'naics', 'contract_type',
                'action_date', 'modification_number']
    missing = [f for f in expected if f not in field_map]
    if missing:
        print(f"\n  WARNING: Missing fields: {missing}")

    return field_map


def aggregate_to_award_level(df, field_map):
    """Aggregate transaction-level data to unique award-level records."""
    award_id_col = field_map.get('award_id')
    agency_col = field_map.get('agency')

    if not award_id_col:
        print("ERROR: Cannot identify award ID column")
        sys.exit(1)

    # Create a composite key
    if agency_col:
        df['_award_key'] = df[award_id_col].astype(str) + '|' + df[agency_col].astype(str)
    else:
        df['_award_key'] = df[award_id_col].astype(str)

    print(f"\nAggregating {len(df):,} transactions to award level...")
    print(f"  Unique award keys: {df['_award_key'].nunique():,}")

    # Build aggregation dict
    agg_dict = {}

    # Take first value for categorical fields (from the original award action)
    categorical_fields = ['agency', 'sub_agency', 'source_selection',
                          'extent_competed', 'naics', 'psc', 'contract_type',
                          'award_type', 'set_aside', 'recipient', 'start_date']
    for label in categorical_fields:
        if label in field_map:
            agg_dict[field_map[label]] = 'first'

    # Sum for obligation amounts
    if 'obligation' in field_map:
        agg_dict[field_map['obligation']] = lambda x: pd.to_numeric(x, errors='coerce').sum()

    # Take max for cumulative value fields
    for label in ['base_value', 'total_value', 'current_value']:
        if label in field_map:
            agg_dict[field_map[label]] = lambda x: pd.to_numeric(x, errors='coerce').max()

    # Take max for offers received
    if 'num_offers' in field_map:
        agg_dict[field_map['num_offers']] = lambda x: pd.to_numeric(x, errors='coerce').max()

    # Count modifications
    if 'modification_number' in field_map:
        agg_dict[field_map['modification_number']] = 'count'

    # Take last end date
    if 'end_date' in field_map:
        agg_dict[field_map['end_date']] = 'last'

    # Take first action date as award date
    if 'action_date' in field_map:
        agg_dict[field_map['action_date']] = 'first'

    # Sort by action date so 'first' captures the original award
    if 'action_date' in field_map:
        df = df.sort_values(field_map['action_date'])

    awards = df.groupby('_award_key').agg(agg_dict).reset_index()

    # Rename modification count
    if 'modification_number' in field_map:
        mod_col = field_map['modification_number']
        awards = awards.rename(columns={mod_col: 'modification_count'})

    print(f"  Award-level records: {len(awards):,}")
    return awards


def apply_sample_criteria(df, field_map):
    """Apply the dissertation's sampling criteria."""
    n_start = len(df)
    print(f"\n=== Applying Sampling Criteria ===")
    print(f"Starting records: {n_start:,}")

    # 1. Above simplified acquisition threshold
    if 'total_value' in field_map:
        val_col = field_map['total_value']
    elif 'obligation' in field_map:
        val_col = field_map['obligation']
    else:
        val_col = None

    if val_col and val_col in df.columns:
        df[val_col] = pd.to_numeric(df[val_col], errors='coerce')
        mask = df[val_col] >= SAT
        n_before = len(df)
        df = df[mask]
        print(f"  Above SAT (${SAT:,}): {n_before:,} -> {len(df):,} ({n_before - len(df):,} removed)")

    # 2. Competitive procurements only
    if 'extent_competed' in field_map:
        ec_col = field_map['extent_competed']
        if ec_col in df.columns:
            competitive_values = df[ec_col].str.lower().str.contains(
                'full and open|full & open|competed', na=False)
            n_before = len(df)
            df = df[competitive_values]
            print(f"  Competitive only: {n_before:,} -> {len(df):,} ({n_before - len(df):,} removed)")

    # 3. Service/IT NAICS codes
    if 'naics' in field_map:
        naics_col = field_map['naics']
        if naics_col in df.columns:
            naics_mask = df[naics_col].astype(str).str[:4].isin(SERVICE_IT_NAICS_PREFIXES)
            n_before = len(df)
            df = df[naics_mask]
            print(f"  Service/IT NAICS: {n_before:,} -> {len(df):,} ({n_before - len(df):,} removed)")

    # 4. Valid source selection method
    if 'source_selection' in field_map:
        ss_col = field_map['source_selection']
        if ss_col in df.columns:
            # Map various codes to standardized values
            ss_map = {
                'LPTA': 'LPTA', 'lpta': 'LPTA',
                'LOWEST PRICE TECHNICALLY ACCEPTABLE': 'LPTA',
                'TO': 'TO', 'to': 'TO',
                'TRADEOFF': 'TO', 'tradeoff': 'TO',
                'TRADE OFF': 'TO', 'TRADE-OFF': 'TO',
                'BEST VALUE': 'TO',
            }
            df['source_selection_std'] = df[ss_col].str.strip().str.upper().map(
                lambda x: ss_map.get(x, x) if pd.notna(x) else np.nan
            )

            n_before = len(df)
            df = df[df['source_selection_std'].isin(VALID_SOURCE_SELECTION)]
            print(f"  Valid source selection: {n_before:,} -> {len(df):,} ({n_before - len(df):,} removed)")

            print(f"\n  Source selection distribution:")
            print(df['source_selection_std'].value_counts().to_string())

    print(f"\nFinal sample: {len(df):,} awards ({len(df)/n_start*100:.1f}% of starting data)")
    return df


def construct_variables(df, field_map):
    """Construct all analysis variables."""
    print(f"\n=== Constructing Analysis Variables ===")

    # 1. Treatment indicator (binary)
    if 'source_selection_std' in df.columns:
        df['tradeoff'] = (df['source_selection_std'] == 'TO').astype(int)
        print(f"  tradeoff: {df['tradeoff'].mean():.3f} (proportion best-value)")

    # 2. Cost growth
    for val_label in ['total_value', 'current_value']:
        if val_label in field_map and field_map[val_label] in df.columns:
            df[field_map[val_label]] = pd.to_numeric(df[field_map[val_label]], errors='coerce')

    if 'base_value' in field_map and field_map['base_value'] in df.columns:
        df[field_map['base_value']] = pd.to_numeric(df[field_map['base_value']], errors='coerce')

    base_col = field_map.get('base_value')
    total_col = field_map.get('total_value') or field_map.get('current_value')

    if base_col and total_col and base_col in df.columns and total_col in df.columns:
        base = df[base_col]
        total = df[total_col]
        # Cost growth = (total - base) / base, only where base > 0
        valid = (base > 0) & base.notna() & total.notna()
        df.loc[valid, 'cost_growth'] = (total[valid] - base[valid]) / base[valid]
        # Winsorize at 1st/99th percentile
        if 'cost_growth' in df.columns:
            p01 = df['cost_growth'].quantile(0.01)
            p99 = df['cost_growth'].quantile(0.99)
            df['cost_growth_winsorized'] = df['cost_growth'].clip(p01, p99)
            print(f"  cost_growth: mean={df['cost_growth'].mean():.4f}, "
                  f"median={df['cost_growth'].median():.4f}, "
                  f"winsorized range=[{p01:.4f}, {p99:.4f}]")

    # 3. Modification intensity (already computed during aggregation)
    if 'modification_count' in df.columns:
        df['modification_count'] = pd.to_numeric(df['modification_count'], errors='coerce')
        print(f"  modification_count: mean={df['modification_count'].mean():.2f}, "
              f"median={df['modification_count'].median():.0f}")

    # 4. Competition variables
    if 'num_offers' in field_map and field_map['num_offers'] in df.columns:
        df['num_offers'] = pd.to_numeric(df[field_map['num_offers']], errors='coerce')
        df['single_bid'] = (df['num_offers'] == 1).astype(int)
        print(f"  num_offers: mean={df['num_offers'].mean():.2f}, "
              f"single_bid rate={df['single_bid'].mean():.3f}")

    # 5. Log award amount
    if 'obligation' in field_map and field_map['obligation'] in df.columns:
        amt = pd.to_numeric(df[field_map['obligation']], errors='coerce')
        df['log_award_amount'] = np.log(amt.clip(lower=1))
        print(f"  log_award_amount: mean={df['log_award_amount'].mean():.2f}")
    elif total_col and total_col in df.columns:
        amt = pd.to_numeric(df[total_col], errors='coerce')
        df['log_award_amount'] = np.log(amt.clip(lower=1))

    # 6. NAICS 2-digit sector
    if 'naics' in field_map and field_map['naics'] in df.columns:
        df['naics_2digit'] = df[field_map['naics']].astype(str).str[:2]
        print(f"  naics_2digit categories: {df['naics_2digit'].nunique()}")

    # 7. Contract type categories
    if 'contract_type' in field_map and field_map['contract_type'] in df.columns:
        ct_col = field_map['contract_type']
        # Simplify contract types
        df['contract_type_simple'] = df[ct_col].str.upper().str.strip()
        # Map to broad categories
        type_map = {}
        for val in df['contract_type_simple'].dropna().unique():
            if 'FIRM' in val or 'FFP' in val or 'FIXED' in val:
                type_map[val] = 'FFP'
            elif 'COST' in val:
                type_map[val] = 'COST_TYPE'
            elif 'TIME' in val or 'T&M' in val or 'LABOR' in val:
                type_map[val] = 'TM_LH'
            else:
                type_map[val] = 'OTHER'
        df['contract_type_cat'] = df['contract_type_simple'].map(type_map)
        print(f"  contract_type_cat distribution:")
        print(f"    {df['contract_type_cat'].value_counts().to_string()}")

    # 8. Fiscal year
    if 'action_date' in field_map and field_map['action_date'] in df.columns:
        df['action_date_parsed'] = pd.to_datetime(df[field_map['action_date']], errors='coerce')
        df['fiscal_year'] = df['action_date_parsed'].apply(
            lambda x: x.year + 1 if pd.notna(x) and x.month >= 10 else (x.year if pd.notna(x) else np.nan)
        )
        print(f"  fiscal_year distribution:")
        print(f"    {df['fiscal_year'].value_counts().sort_index().to_string()}")

    # 9. IDV indicator
    if 'award_type' in field_map and field_map['award_type'] in df.columns:
        df['is_idv'] = df[field_map['award_type']].str.upper().str.contains(
            'IDV|INDEFINITE', na=False).astype(int)
        print(f"  is_idv: {df['is_idv'].mean():.3f}")

    # 10. Agency name (standardized)
    if 'agency' in field_map and field_map['agency'] in df.columns:
        df['agency_name'] = df[field_map['agency']].str.strip()
        print(f"  Unique agencies: {df['agency_name'].nunique()}")

    return df


def save_output(df, output_path):
    """Save the analysis-ready dataset."""
    # Select analysis columns
    analysis_cols = [
        '_award_key', 'tradeoff', 'source_selection_std',
        'cost_growth', 'cost_growth_winsorized', 'modification_count',
        'num_offers', 'single_bid', 'log_award_amount',
        'naics_2digit', 'contract_type_cat', 'fiscal_year',
        'is_idv', 'agency_name',
    ]

    # Keep only columns that exist
    available = [c for c in analysis_cols if c in df.columns]
    output = df[available].copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_path, index=False)
    size_mb = output_path.stat().st_size / 1e6
    print(f"\n=== Output Saved ===")
    print(f"File: {output_path}")
    print(f"Records: {len(output):,}")
    print(f"Columns: {len(output.columns)}")
    print(f"Size: {size_mb:.1f} MB")

    # Summary statistics
    print(f"\n=== Summary Statistics ===")
    if 'tradeoff' in output.columns:
        n_lpta = (output['tradeoff'] == 0).sum()
        n_to = (output['tradeoff'] == 1).sum()
        print(f"LPTA awards: {n_lpta:,} ({n_lpta/len(output)*100:.1f}%)")
        print(f"Tradeoff awards: {n_to:,} ({n_to/len(output)*100:.1f}%)")

    for col in ['cost_growth_winsorized', 'modification_count', 'num_offers']:
        if col in output.columns:
            print(f"\n{col}:")
            print(output[col].describe().to_string())

    return output


def main():
    parser = argparse.ArgumentParser(description="Process USAspending data for analysis")
    parser.add_argument("--raw-dir", type=str, default=str(RAW_DIR),
                       help="Directory containing raw CSV files")
    parser.add_argument("--output", type=str,
                       default=str(PROCESSED_DIR / "awards_analysis.csv"),
                       help="Output file path")
    args = parser.parse_args()

    print("=" * 60)
    print("PhD Dissertation Data Processing Pipeline")
    print("=" * 60)

    # Step 1: Find and load data
    csv_files = find_csv_files(args.raw_dir)
    if not csv_files:
        print("No CSV files found. Run download_archive.py first.")
        sys.exit(1)

    df = load_raw_data(csv_files)

    # Step 2: Identify column names
    field_map = identify_columns(df)

    # Step 3: Aggregate to award level
    awards = aggregate_to_award_level(df, field_map)

    # Step 4: Apply sampling criteria
    sample = apply_sample_criteria(awards, field_map)

    # Step 5: Construct variables
    analysis = construct_variables(sample, field_map)

    # Step 6: Save output
    output_path = Path(args.output)
    save_output(analysis, output_path)

    print("\nDone!")


if __name__ == "__main__":
    main()
