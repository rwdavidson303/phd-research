#!/usr/bin/env python3
"""
USAspending.gov Bulk Download Script for PhD Dissertation

Downloads federal contract transaction data via the USAspending bulk download API.
Retrieves all FPDS fields including source_selection_process for FY2020-FY2025.

Downloads are requested in quarterly chunks to keep file sizes manageable.
The API generates ZIP files containing CSVs with all transaction-level fields.

Usage:
    python download_archive.py                  # Download all FY2020-FY2025
    python download_archive.py --fy 2024        # Single fiscal year
    python download_archive.py --fy 2023-2025   # Range of fiscal years
"""

import argparse
import json
import os
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path

import requests
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='urllib3')

BASE_URL = "https://api.usaspending.gov/api/v2"
RAW_DIR = Path(__file__).parent.parent / "raw" / "usaspending"

# NAICS codes for service/IT procurement (dissertation focus)
SERVICE_IT_NAICS = [
    "541511", "541512", "541513", "541519",  # Computer/IT services
    "541611", "541612", "541613", "541614", "541618",  # Management consulting
    "541620", "541690",  # Other consulting
    "541715",  # R&D
    "518210",  # Data processing/hosting
    "511210",  # Software publishers
    "561110", "561210",  # Administrative/facilities support
]

# Fiscal year quarters (Oct-Dec, Jan-Mar, Apr-Jun, Jul-Sep)
def get_fy_quarters(fy):
    """Return date ranges for each quarter of a fiscal year."""
    return [
        {"start_date": f"{fy-1}-10-01", "end_date": f"{fy-1}-12-31", "label": f"FY{fy}Q1"},
        {"start_date": f"{fy}-01-01", "end_date": f"{fy}-03-31", "label": f"FY{fy}Q2"},
        {"start_date": f"{fy}-04-01", "end_date": f"{fy}-06-30", "label": f"FY{fy}Q3"},
        {"start_date": f"{fy}-07-01", "end_date": f"{fy}-09-30", "label": f"FY{fy}Q4"},
    ]


def request_download(start_date, end_date):
    """Request a bulk download from USAspending API."""
    url = f"{BASE_URL}/bulk_download/awards/"
    payload = {
        "filters": {
            "prime_award_types": ["A", "B", "C", "D"],  # Definitive contracts only
            "agency": "all",
            "date_type": "action_date",
            "date_range": {
                "start_date": start_date,
                "end_date": end_date
            }
        },
        "columns": [],  # Empty = all columns (includes source_selection_process)
        "file_format": "csv"
    }

    resp = requests.post(url, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def wait_for_download(status_url, max_wait=1800):
    """Poll status URL until download is ready. Returns file URL."""
    start = time.time()
    while time.time() - start < max_wait:
        resp = requests.get(status_url, timeout=30)
        data = resp.json()
        status = data.get("status", "unknown")

        if status == "finished":
            return data.get("file_url") or data.get("url")
        elif status == "failed":
            print(f"  Download FAILED: {data.get('message', 'unknown error')}")
            return None

        # Show progress
        pct = data.get("total_rows", 0)
        print(f"  Status: {status} | Rows: {pct:,} | Elapsed: {int(time.time()-start)}s", end="\r")
        time.sleep(10)

    print(f"\n  Timed out after {max_wait}s")
    return None


def download_file(url, filepath):
    """Download a file with progress reporting."""
    resp = requests.get(url, stream=True, timeout=600)
    resp.raise_for_status()
    total = int(resp.headers.get('content-length', 0))

    downloaded = 0
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            if total:
                pct = downloaded / total * 100
                print(f"  Downloading: {pct:.1f}% ({downloaded/1e6:.1f}/{total/1e6:.1f} MB)", end="\r")

    print(f"\n  Saved: {filepath} ({downloaded/1e6:.1f} MB)")
    return filepath


def extract_zip(zip_path, extract_dir):
    """Extract CSV files from a ZIP archive."""
    with zipfile.ZipFile(zip_path, 'r') as z:
        csv_files = [f for f in z.namelist() if f.endswith('.csv')]
        for csv_file in csv_files:
            z.extract(csv_file, extract_dir)
            extracted = extract_dir / csv_file
            size_mb = extracted.stat().st_size / 1e6
            print(f"  Extracted: {csv_file} ({size_mb:.1f} MB)")
    return csv_files


def main():
    parser = argparse.ArgumentParser(description="Download USAspending contract data")
    parser.add_argument("--fy", type=str, default="2020-2025",
                       help="Fiscal year or range (e.g., 2024 or 2020-2025)")
    args = parser.parse_args()

    # Parse fiscal year range
    if "-" in args.fy:
        start_fy, end_fy = map(int, args.fy.split("-"))
    else:
        start_fy = end_fy = int(args.fy)

    fiscal_years = range(start_fy, end_fy + 1)

    # Create output directory
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Track downloads
    manifest = {
        "download_date": datetime.now().isoformat(),
        "fiscal_years": list(fiscal_years),
        "downloads": []
    }

    print(f"=== USAspending Bulk Download ===")
    print(f"Fiscal years: {start_fy}-{end_fy}")
    print(f"Output directory: {RAW_DIR}")
    print()

    for fy in fiscal_years:
        quarters = get_fy_quarters(fy)
        for q in quarters:
            label = q["label"]
            zip_path = RAW_DIR / f"{label}_contracts.zip"

            # Skip if already downloaded
            csv_exists = list(RAW_DIR.glob(f"*{label}*.csv")) + list(RAW_DIR.glob(f"*{q['start_date']}*.csv"))
            if zip_path.exists() or csv_exists:
                print(f"[SKIP] {label} already downloaded")
                continue

            print(f"[{label}] Requesting download ({q['start_date']} to {q['end_date']})...")

            try:
                # Request the download
                result = request_download(q["start_date"], q["end_date"])
                file_url = result.get("file_url")
                status_url = result.get("status_url")

                if not file_url and status_url:
                    print(f"  Waiting for generation...")
                    file_url = wait_for_download(status_url)

                if not file_url:
                    print(f"  [ERROR] Could not get download URL for {label}")
                    manifest["downloads"].append({"label": label, "status": "failed"})
                    continue

                # Download the file
                download_file(file_url, zip_path)

                # Extract
                csv_files = extract_zip(zip_path, RAW_DIR)

                manifest["downloads"].append({
                    "label": label,
                    "status": "success",
                    "file_url": file_url,
                    "zip_file": str(zip_path),
                    "csv_files": csv_files
                })

            except Exception as e:
                print(f"  [ERROR] {label}: {e}")
                manifest["downloads"].append({"label": label, "status": "error", "message": str(e)})

    # Save manifest
    manifest_path = RAW_DIR / "download_manifest_archive.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest saved: {manifest_path}")

    # Summary
    success = sum(1 for d in manifest["downloads"] if d["status"] == "success")
    total = len(manifest["downloads"])
    print(f"\n=== Download Complete ===")
    print(f"Successful: {success}/{total} quarters")


if __name__ == "__main__":
    main()
