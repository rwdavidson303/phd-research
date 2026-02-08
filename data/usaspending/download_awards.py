#!/usr/bin/env python3
"""
USAspending.gov Federal Procurement Data Downloader

Downloads contract award data from the USAspending.gov API for PhD research on
best-value source selection in government RFPs.

Data includes source selection process (LPTA vs tradeoff), contract type,
competition details, obligations, and key dates.

Usage:
    python download_awards.py                    # Download all categories, current FY
    python download_awards.py --fy 2024          # Specific fiscal year
    python download_awards.py --fy 2020-2025     # Range of fiscal years
    python download_awards.py --it-only          # IT & professional services only
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests
import pandas as pd

BASE_URL = "https://api.usaspending.gov/api/v2"
DATA_DIR = Path(__file__).parent
RAW_DIR = DATA_DIR.parent / "raw"
PROCESSED_DIR = DATA_DIR.parent / "processed"

# Contract award type codes (all procurement types)
CONTRACT_TYPES = ["A", "B", "C", "D"]  # Definitive contracts
IDV_TYPES = ["IDV_A", "IDV_B", "IDV_B_A", "IDV_B_B", "IDV_B_C", "IDV_C", "IDV_D", "IDV_E"]

# NAICS codes most relevant to the dissertation (IT & professional services)
IT_SERVICES_NAICS = [
    "541511",  # Custom Computer Programming Services
    "541512",  # Computer Systems Design Services
    "541513",  # Computer Facilities Management Services
    "541519",  # Other Computer Related Services
    "541611",  # Administrative Management Consulting
    "541612",  # Human Resources Consulting
    "541613",  # Marketing Consulting
    "541614",  # Process/Logistics Consulting
    "541618",  # Other Management Consulting
    "541620",  # Environmental Consulting
    "541690",  # Other Scientific/Technical Consulting
    "541715",  # R&D in Physical/Engineering/Life Sciences
    "518210",  # Data Processing/Hosting
    "511210",  # Software Publishers
    "561110",  # Office Administrative Services
    "561210",  # Facilities Support Services
]


def get_agencies():
    """Fetch list of all federal agencies for bulk download."""
    url = f"{BASE_URL}/bulk_download/list_agencies/"
    payload = {"type": "award_agencies"}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()


def request_bulk_download(fiscal_year, agency=None, award_types=None, date_range=None):
    """
    Request a bulk download of award data from USAspending.

    Returns the status URL and file URL for monitoring.
    """
    url = f"{BASE_URL}/bulk_download/awards/"

    if award_types is None:
        award_types = CONTRACT_TYPES + IDV_TYPES

    # Default date range: full fiscal year
    if date_range is None:
        start_date = f"{fiscal_year - 1}-10-01"
        end_date = f"{fiscal_year}-09-30"
    else:
        start_date, end_date = date_range

    filters = {
        "prime_award_types": award_types,
        "date_type": "action_date",
        "date_range": {
            "start_date": start_date,
            "end_date": end_date,
        },
    }

    if agency:
        filters["agencies"] = [
            {"type": "awarding", "tier": "toptier", "name": agency}
        ]

    payload = {
        "filters": filters,
        "file_format": "csv",
    }

    print(f"Requesting bulk download: FY{fiscal_year}")
    print(f"  Date range: {start_date} to {end_date}")
    if agency:
        print(f"  Agency: {agency}")
    print(f"  Award types: {award_types}")

    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    result = resp.json()

    print(f"  Status URL: {result.get('status_url', 'N/A')}")
    print(f"  File URL: {result.get('file_url', 'N/A')}")

    return result


def check_download_status(file_name):
    """Check the status of a bulk download request."""
    url = f"{BASE_URL}/bulk_download/status/"
    params = {"file_name": file_name}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


def wait_and_download(result, output_dir, max_wait=1800):
    """Wait for bulk download to complete, then download the file."""
    file_name = result.get("file_name", "")
    file_url = result.get("file_url", "")

    if not file_name:
        print("  No file_name in response, trying file_url directly...")
        if file_url:
            return download_file(file_url, output_dir)
        print("  ERROR: No file URL available")
        return None

    print(f"  Waiting for download generation: {file_name}")
    start_time = time.time()

    while time.time() - start_time < max_wait:
        status = check_download_status(file_name)
        state = status.get("status", "unknown")

        if state == "finished":
            download_url = status.get("file_url", file_url)
            print(f"  Download ready: {download_url}")
            return download_file(download_url, output_dir)
        elif state == "failed":
            print(f"  ERROR: Download failed - {status.get('message', 'unknown error')}")
            return None
        else:
            elapsed = int(time.time() - start_time)
            print(f"  Status: {state} (waiting {elapsed}s)...", end="\r")
            time.sleep(15)

    print(f"\n  TIMEOUT: Download did not complete within {max_wait}s")
    return None


def download_file(url, output_dir):
    """Download a file from URL to output directory."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = url.split("/")[-1]
    output_path = output_dir / filename

    print(f"  Downloading to: {output_path}")
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    total_size = int(resp.headers.get("content-length", 0))
    downloaded = 0

    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            if total_size > 0:
                pct = (downloaded / total_size) * 100
                print(f"  Downloaded: {downloaded:,} / {total_size:,} bytes ({pct:.1f}%)", end="\r")

    print(f"\n  Saved: {output_path} ({downloaded:,} bytes)")
    return output_path


def search_awards(filters, limit=100, page=1):
    """
    Search for specific awards using the spending_by_award endpoint.
    Useful for targeted queries.
    """
    url = f"{BASE_URL}/search/spending_by_award/"
    payload = {
        "filters": filters,
        "fields": [
            "Award ID",
            "Recipient Name",
            "Start Date",
            "End Date",
            "Award Amount",
            "Total Outlays",
            "Awarding Agency",
            "Awarding Sub Agency",
            "Contract Award Type",
            "NAICS Code",
            "PSC Code",
            "Place of Performance State Code",
        ],
        "limit": limit,
        "page": page,
        "sort": "Award Amount",
        "order": "desc",
        "subawards": False,
    }

    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()


def download_fiscal_year(fy, output_dir, it_only=False):
    """Download all contract data for a given fiscal year."""
    output_dir = Path(output_dir)

    print(f"\n{'='*60}")
    print(f"Downloading FY{fy} procurement data")
    print(f"{'='*60}")

    try:
        result = request_bulk_download(fy)
        filepath = wait_and_download(result, output_dir / f"FY{fy}")
        if filepath:
            print(f"  SUCCESS: FY{fy} data saved to {filepath}")
            return filepath
        else:
            print(f"  WARNING: FY{fy} download did not complete")
            return None
    except requests.exceptions.RequestException as e:
        print(f"  ERROR: API request failed for FY{fy}: {e}")
        return None


def parse_fy_range(fy_str):
    """Parse a fiscal year string like '2024' or '2020-2025'."""
    if "-" in fy_str:
        start, end = fy_str.split("-")
        return list(range(int(start), int(end) + 1))
    return [int(fy_str)]


def main():
    parser = argparse.ArgumentParser(
        description="Download federal procurement data from USAspending.gov"
    )
    parser.add_argument(
        "--fy",
        default=str(datetime.now().year),
        help="Fiscal year or range (e.g., 2024 or 2020-2025). Default: current year",
    )
    parser.add_argument(
        "--it-only",
        action="store_true",
        help="Download only IT and professional services categories",
    )
    parser.add_argument(
        "--output",
        default=str(RAW_DIR / "usaspending"),
        help="Output directory for downloaded files",
    )
    parser.add_argument(
        "--list-agencies",
        action="store_true",
        help="List available agencies and exit",
    )

    args = parser.parse_args()

    if args.list_agencies:
        print("Fetching agency list...")
        agencies = get_agencies()
        for agency_group in agencies.get("agencies", {}).values():
            for agency in agency_group:
                print(f"  {agency.get('name', 'Unknown')}")
        return

    fiscal_years = parse_fy_range(args.fy)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"USAspending Data Downloader")
    print(f"  Fiscal years: {fiscal_years}")
    print(f"  Output: {output_dir}")
    print(f"  IT/Services only: {args.it_only}")
    print()

    results = {}
    for fy in fiscal_years:
        filepath = download_fiscal_year(fy, output_dir, args.it_only)
        results[fy] = filepath

    # Summary
    print(f"\n{'='*60}")
    print("Download Summary")
    print(f"{'='*60}")
    for fy, path in results.items():
        status = "OK" if path else "FAILED"
        print(f"  FY{fy}: {status} - {path or 'N/A'}")

    # Save manifest
    manifest = {
        "download_date": datetime.now().isoformat(),
        "fiscal_years": fiscal_years,
        "it_only": args.it_only,
        "results": {str(fy): str(path) if path else None for fy, path in results.items()},
    }
    manifest_path = output_dir / "download_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest saved: {manifest_path}")


if __name__ == "__main__":
    main()
