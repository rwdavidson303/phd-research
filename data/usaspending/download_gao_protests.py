#!/usr/bin/env python3
"""
GAO Bid Protest Data Downloader

Downloads bid protest statistics and data from the U.S. Government
Accountability Office (GAO) for PhD research on procurement outcomes.

GAO publishes annual bid protest reports and maintains a searchable
docket of protest decisions.

Usage:
    python download_gao_protests.py
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

import requests

DATA_DIR = Path(__file__).parent.parent / "gao-protests"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# GAO protest report URLs (annual reports)
GAO_REPORTS = {
    "2025": "https://www.gao.gov/products/b-158766",
    "2024": "https://www.gao.gov/products/b-158766",
}

# GAO protest decisions search
GAO_DECISIONS_URL = "https://www.gao.gov/legal/bid-protests/search"


def download_gao_annual_reports():
    """Download GAO annual bid protest reports."""
    print("Downloading GAO Annual Bid Protest Reports")
    print("=" * 50)

    reports_dir = DATA_DIR / "annual_reports"
    reports_dir.mkdir(exist_ok=True)

    # Download the main bid protest page for links
    try:
        resp = requests.get(
            "https://www.gao.gov/legal/bid-protests/about",
            headers={"User-Agent": "PhD-Research-Bot/1.0 (academic research)"},
        )
        resp.raise_for_status()

        output_path = reports_dir / "gao_bid_protests_about.html"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(resp.text)
        print(f"  Saved: {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"  ERROR downloading GAO page: {e}")

    # Download annual report pages
    for year, url in GAO_REPORTS.items():
        try:
            resp = requests.get(
                url,
                headers={"User-Agent": "PhD-Research-Bot/1.0 (academic research)"},
            )
            resp.raise_for_status()
            output_path = reports_dir / f"gao_protest_report_{year}.html"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(resp.text)
            print(f"  Saved FY{year}: {output_path}")
        except requests.exceptions.RequestException as e:
            print(f"  ERROR downloading FY{year}: {e}")


def download_protest_statistics():
    """
    Download protest statistics from GAO.

    Note: GAO publishes summary statistics in their annual reports.
    Key metrics include:
    - Total protests filed
    - Protests sustained vs. denied
    - Cases dismissed
    - Effectiveness rate
    - Average processing time
    """
    print("\nGAO Protest Statistics")
    print("=" * 50)

    stats_dir = DATA_DIR / "statistics"
    stats_dir.mkdir(exist_ok=True)

    # Historical protest statistics (manually compiled from GAO reports)
    # These should be updated as new annual reports are published
    historical_stats = {
        "source": "GAO Annual Bid Protest Reports",
        "last_updated": datetime.now().isoformat(),
        "note": "Update annually from GAO Annual Report to Congress on Bid Protests",
        "data_fields": [
            "fiscal_year",
            "cases_filed",
            "cases_closed",
            "sustained",
            "denied",
            "dismissed",
            "effectiveness_rate_pct",
            "merit_decisions",
        ],
        "annual_data": [],
        "urls": {
            "gao_bid_protests": "https://www.gao.gov/legal/bid-protests",
            "annual_reports": "https://www.gao.gov/legal/bid-protests/annual-report",
            "search_decisions": "https://www.gao.gov/legal/bid-protests/search",
        },
    }

    output_path = stats_dir / "gao_protest_statistics.json"
    with open(output_path, "w") as f:
        json.dump(historical_stats, f, indent=2)
    print(f"  Statistics template saved: {output_path}")
    print("  NOTE: Populate with data from GAO annual reports")


def create_data_dictionary():
    """Create a data dictionary for protest-related variables."""
    data_dict = {
        "name": "GAO Bid Protest Data Dictionary",
        "description": "Variables for analyzing bid protest patterns and outcomes",
        "last_updated": datetime.now().isoformat(),
        "variables": [
            {
                "name": "protest_docket_number",
                "type": "string",
                "description": "GAO docket number (e.g., B-419XXX)",
            },
            {
                "name": "filing_date",
                "type": "date",
                "description": "Date protest was filed with GAO",
            },
            {
                "name": "decision_date",
                "type": "date",
                "description": "Date GAO issued decision",
            },
            {
                "name": "protester",
                "type": "string",
                "description": "Name of protesting entity",
            },
            {
                "name": "agency",
                "type": "string",
                "description": "Contracting agency",
            },
            {
                "name": "solicitation_number",
                "type": "string",
                "description": "Related solicitation/contract number",
            },
            {
                "name": "outcome",
                "type": "categorical",
                "values": ["sustained", "denied", "dismissed", "withdrawn"],
                "description": "Final disposition of the protest",
            },
            {
                "name": "processing_days",
                "type": "integer",
                "description": "Days from filing to decision",
            },
            {
                "name": "grounds",
                "type": "string",
                "description": "Basis for protest (evaluation errors, solicitation issues, etc.)",
            },
            {
                "name": "award_type",
                "type": "categorical",
                "values": ["LPTA", "tradeoff", "other"],
                "description": "Source selection method used in protested procurement",
            },
            {
                "name": "naics_code",
                "type": "string",
                "description": "NAICS code of the protested procurement",
            },
            {
                "name": "contract_value",
                "type": "float",
                "description": "Value of the protested contract",
            },
        ],
    }

    output_path = DATA_DIR / "protest_data_dictionary.json"
    with open(output_path, "w") as f:
        json.dump(data_dict, f, indent=2)
    print(f"  Data dictionary saved: {output_path}")


def main():
    print("GAO Bid Protest Data Downloader")
    print(f"Output directory: {DATA_DIR}")
    print()

    download_gao_annual_reports()
    download_protest_statistics()
    create_data_dictionary()

    print(f"\nDone. Files saved to: {DATA_DIR}")
    print("\nNext steps:")
    print("  1. Review downloaded GAO report pages for PDF links")
    print("  2. Populate statistics from annual reports")
    print("  3. Search GAO decisions database for relevant protests")
    print("  4. Link protest data to USAspending award records")


if __name__ == "__main__":
    main()
