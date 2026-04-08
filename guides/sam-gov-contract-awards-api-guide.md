# SAM.gov Contract Awards API: Complete Registration & Usage Guide

**Purpose:** Access FPDS contract award data via the SAM.gov Contract Awards API, including the `sourceSelectionProcess` field (LPTA, Trade-off, Other) critical for dissertation research on best-value source selection in government RFPs.

**Last Updated:** March 2026

---

## Table of Contents

1. [Overview](#1-overview)
2. [Part 1: Register for a SAM.gov Account](#2-part-1-register-for-a-samgov-account)
3. [Part 2: Get an Individual (Public) API Key (Immediate, 10 req/day)](#3-part-2-get-an-individual-public-api-key)
4. [Part 3: Get a System Account API Key (1,000 req/day, 1-4 weeks)](#4-part-3-get-a-system-account-api-key)
5. [API Endpoint & Authentication](#5-api-endpoint--authentication)
6. [Key Query Parameters](#6-key-query-parameters)
7. [Source Selection Process Codes](#7-source-selection-process-codes)
8. [Example API Calls (curl)](#8-example-api-calls-curl)
9. [Python Code Examples](#9-python-code-examples)
10. [Response Structure](#10-response-structure)
11. [Rate Limits & Practical Tips](#11-rate-limits--practical-tips)
12. [Important Data Caveats](#12-important-data-caveats)
13. [Sources & References](#13-sources--references)

---

## 1. Overview

The SAM.gov Contract Awards API is the successor to the legacy FPDS Atom Feed. It provides access to all federal contract award data reported by agencies, including the `sourceSelectionProcess` field that identifies whether an award used LPTA (Lowest Price Technically Acceptable), Trade-off (Best Value), or Other source selection methods.

There are **two tiers** of API access:

| Feature | Individual (Public) API Key | System Account API Key |
|---|---|---|
| **Access Level** | Public data only | Public + FOUO/Sensitive data |
| **Rate Limit** | 10 requests/day (some sources say 1,000/day for registered users) | 10,000/day (federal); higher limits by request |
| **Setup Time** | Immediate (minutes) | 1-4 weeks (requires approval) |
| **Key Rotation** | Every 90 days (auto-renewed) | Subject to account expiration |
| **Data Access** | Revealed awards only | Revealed + Unrevealed (DoD <90 days) |

For dissertation research on historical contract data, an **Individual API Key** is sufficient to start. A System Account provides higher throughput for large-scale data collection.

---

## 2. Part 1: Register for a SAM.gov Account

Before you can get any API key, you need a SAM.gov user account. SAM.gov uses Login.gov for authentication.

### Step 1: Go to SAM.gov

Navigate to **https://sam.gov** in your web browser.

### Step 2: Click "Sign In"

Click the **"Sign In"** button in the top-right header of any SAM.gov page.

### Step 3: Create or Use a Login.gov Account

SAM.gov uses Login.gov for authentication. You will be redirected to Login.gov.

- **If you already have a Login.gov account:** Sign in with your existing credentials.
- **If you do not have a Login.gov account:**
  1. Click **"Create an account"** on the Login.gov page.
  2. Enter your **email address** (use a personal or university email; a .gov email is NOT required for non-federal users).
  3. Check your email and click the **confirmation link**.
  4. Create a **strong password** (minimum 12 characters).
  5. Set up **multi-factor authentication** (MFA). Login.gov requires MFA -- options include:
     - Authentication app (Google Authenticator, Authy, etc.) -- recommended
     - SMS/text message
     - Security key (hardware token)
     - Government employee PIV/CAC card
  6. Complete the Login.gov registration.

### Step 4: Complete SAM.gov Profile

After signing in through Login.gov, SAM.gov will prompt you to complete your user profile:

1. Enter your **first and last name**.
2. Select your **account type**: Choose **"Individual"** (not Entity or Government).
3. Complete any additional profile fields.
4. You will be taken to your **Workspace** page.

---

## 3. Part 2: Get an Individual (Public) API Key

**Time required:** Immediate (available as soon as you have a SAM.gov account)

**Rate limit:** 10 requests/day (public/unregistered tier) or up to 1,000 requests/day (registered individual tier -- reports vary)

### Step 1: Navigate to Your Profile

From your SAM.gov Workspace page, click the **user profile icon** located in the header of any page.

### Step 2: Find the Public API Key Section

On your profile/account details page, scroll down to the section titled **"Public API Key"**.

### Step 3: Request Your API Key

Click **"Request API Key"**. Your API key will be generated immediately.

### Step 4: Copy and Save Your API Key

Your API key will display in the **Public API Key** section. It is a **40-character alphanumeric string**. Copy it and store it securely (e.g., in an environment variable or a `.env` file -- never commit it to a Git repository).

### Important Notes on Individual API Keys

- **Expiration:** API keys expire every **90 days**. A new key will be auto-generated before the current one expires.
- **Removal:** If you want to remove a recently requested key, you must wait **24 hours** from the time you made the request before you can remove it.
- **One key per user:** You are allowed one individual account API key.

---

## 4. Part 3: Get a System Account API Key

**Time required:** 1-4 weeks (requires approval by SAM.gov administrators)

**Rate limit:** Up to 10,000 requests/day (federal); 1,000/day default for non-federal; higher limits available by request for federal accounts

### Step 1: Ensure You Have a SAM.gov Account

Complete Part 1 (above) first. You must have a registered SAM.gov user account.

### Step 2: Access the System Accounts Widget

**For Non-Federal Users (university researchers, contractors, etc.):**
- From your SAM.gov **Workspace** page, look for the **"System Accounts"** widget.
- If the widget is not visible, you may need to **request access** to system accounts. Non-federal registered users must submit a request, and if their registration and request criteria are satisfied, the System Accounts widget will appear on their Workspace page.

**For Federal Users:**
- Contact your **CCB (Configuration Control Board) representative** to be granted the system account role.
- Once approved, the System Accounts widget will appear on your Workspace.

### Step 3: Request a System Account

1. Click **"Go to System Accounts"** from the widget on your Workspace.
2. Click **"Request System Account"**.

### Step 4: Fill Out the System Account Request Form

You will need to provide:

1. **System Description and Function:**
   Write a clear business justification. For academic research, something like:
   > "DBA dissertation research at Indiana University, Kelley School of Business. Studying the relationship between source selection methodology (LPTA vs. best-value tradeoff) and contract outcomes in federal procurement. Need to query the Contract Awards API to collect contract award records with sourceSelectionProcess data for statistical analysis. Estimated data volume: ~50,000-200,000 contract records covering FY2020-FY2025."

2. **Domains and Permissions:**
   You will see a list of SAM.gov data domains. Select **"Contract Awards"** (and any other relevant domains). Each domain has specific permissions.

3. **Security Information -- IP Address(es):**
   List **all IP addresses** that your system will use to call the API. You can find your current public IP at https://whatismyipaddress.com. If your IP changes frequently (e.g., residential internet), note this in the justification and ask about dynamic IP support.

4. **Review your application:**
   Click the **Review** button to check all fields before submitting.

### Step 5: Submit and Wait for Approval

After submission, your request will be reviewed by SAM.gov administrators. You will receive an **email notification** when your request is approved or if additional information is needed. This process typically takes **1-4 weeks** (up to 10+ business days).

### Step 6: Set Your System Account Password

Once approved:
1. Go to your **Workspace**.
2. Click **"Go to System Accounts"** in the System Accounts widget.
3. Set a new **system account password** when prompted.

### Step 7: Retrieve Your System Account API Key

1. After setting your password, a new section will appear for retrieving your API key.
2. Click the **"Eye" icon** to reveal the key.
3. Enter the **One-Time Password (OTP)** sent to your registered email address.
4. Click **"Submit"** and your API key will appear.
5. Copy and store it securely.

### System Account Authentication

System account API calls require different authentication than individual keys:

- The **System Account User ID and Password** must be sent as **Basic Auth** in the `Authorization` header, Base64-encoded as `base64(username:password)`.
- The **API Key** must be sent as the **`x-api-key`** header (NOT as a URL query parameter).
- The `Accept` header must be `application/json`.
- The `Content-Type` header must be `application/json`.

---

## 5. API Endpoint & Authentication

### Production Endpoint

```
https://api.sam.gov/contract-awards/v1/search
```

### Authentication Methods

**Individual (Public) API Key -- Simple query parameter:**
```
https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_KEY_HERE&...
```

**System Account API Key -- Header-based authentication:**
```
Headers:
  Authorization: Basic base64(username:password)
  x-api-key: YOUR_SYSTEM_API_KEY
  Accept: application/json
  Content-Type: application/json
```

---

## 6. Key Query Parameters

| Parameter | Description | Example |
|---|---|---|
| `api_key` | Your API key (individual keys only; system keys use header) | `api_key=abcdef123456` |
| `sourceSelectionProcess` | Source selection process code: LPTA, TO, O | `sourceSelectionProcess=LPTA` |
| `sourceSelectionProcessName` | Source selection process name (maps from FPDS `SOURCE_SELECTION_PROCESS_DESC`) | `sourceSelectionProcessName=LOWEST PRICE TECHNICALLY ACCEPTABLE` |
| `lastModifiedDate` | Date range in bracket notation (MM/DD/YYYY) | `lastModifiedDate=[01/01/2024,12/31/2024]` |
| `modificationNumber` | Contract modification number; `0` = base award only | `modificationNumber=0` |
| `dollarsObligated` | Dollar range in bracket notation | `dollarsObligated=[0.0,100000000.99]` |
| `contractingDepartmentCode` | Department code (e.g., 9700 = DoD) | `contractingDepartmentCode=9700` |
| `naicsCode` | NAICS industry code | `naicsCode=541512` |
| `limit` | Records per page (default 10, max 100) | `limit=100` |
| `offset` | Pagination offset (default 0) | `offset=100` |
| `q` | Free text search | `q=software development` |
| `format` | Response format for extract mode (JSON or CSV) | `format=csv` |
| `deletedStatus` | Returns deleted contracts only (last 6 months) | `deletedStatus=true` |
| `piid` | Procurement Instrument Identifier | `piid=GS-35F-0001A` |
| `piidAggregation` | Return award family summary (use with piid) | `piidAggregation=true` |

### Combining Parameters

- **AND condition:** Use `&` between parameters (default behavior)
- **OR condition:** Use `~` within a parameter value (e.g., `naicsCode=541512~541511`)
- **NOT condition:** Use `!` prefix (e.g., `sourceSelectionProcess=!O`)
- **Date ranges:** Use bracket notation `[start,end]` with MM/DD/YYYY format; leave end empty for open-ended `[01/01/2024,]`

---

## 7. Source Selection Process Codes

The `sourceSelectionProcess` field was added to FPDS in **2020** per FY2020 NDAA Section 806. Data is only available for awards from approximately FY2020 onward.

| Code | Name | FAR Reference | Description |
|---|---|---|---|
| **LPTA** | Lowest Price Technically Acceptable | FAR 15.101-2 | Award to the lowest-priced offeror that meets minimum acceptable technical requirements. Non-price factors evaluated on pass/fail basis. |
| **TO** | Trade-off (Best Value Tradeoff / BVTO) | FAR 15.101-1 | Best value tradeoff weighing price/cost against non-price/cost factors. Government may pay more for superior technical merit. |
| **O** | Other | N/A | Neither LPTA nor Trade-off (e.g., sole-source, price-only, simplified acquisition, fully automated actions). |

### Important Notes

- The code in the data is **"TO"** (not "BVTO"), even though "BVTO" (Best Value Trade-Off) is commonly used in the procurement community.
- Noncompetitive awards should be entered as "Other".
- Contracting officers are instructed not to leave this field blank, but older data may have missing values.

---

## 8. Example API Calls (curl)

### Query 1: All LPTA Base Awards Modified Since January 1, 2024

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&sourceSelectionProcess=LPTA&modificationNumber=0&lastModifiedDate=[01/01/2024,]&limit=100&offset=0"
```

### Query 2: All Trade-off (Best Value) Base Awards Modified Since January 1, 2024

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&sourceSelectionProcess=TO&modificationNumber=0&lastModifiedDate=[01/01/2024,]&limit=100&offset=0"
```

### Query 3: LPTA OR Trade-off Awards (Excluding "Other")

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&sourceSelectionProcess=LPTA~TO&modificationNumber=0&lastModifiedDate=[01/01/2024,]&limit=100&offset=0"
```

### Query 4: DoD LPTA Awards Over $100K

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&sourceSelectionProcess=LPTA&modificationNumber=0&contractingDepartmentCode=9700&dollarsObligated=[100000.00,]&lastModifiedDate=[01/01/2024,]&limit=100&offset=0"
```

### Query 5: IT Services Contracts (NAICS 541512) Using Any Source Selection

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&naicsCode=541512&modificationNumber=0&lastModifiedDate=[01/01/2020,]&limit=100&offset=0"
```

### Query 6: Exclude "Other" -- Only Contracts With Known Source Selection Methods

```bash
curl "https://api.sam.gov/contract-awards/v1/search?api_key=YOUR_API_KEY&sourceSelectionProcess=!O&modificationNumber=0&lastModifiedDate=[01/01/2020,]&limit=100&offset=0"
```

---

## 9. Python Code Examples

### Example 1: Basic Query for LPTA Contracts

```python
"""
Basic SAM.gov Contract Awards API query for LPTA contracts.
Requires: pip install requests
"""
import requests
import json
import os

# Load API key from environment variable
API_KEY = os.environ.get("SAM_API_KEY", "YOUR_API_KEY_HERE")

BASE_URL = "https://api.sam.gov/contract-awards/v1/search"

def query_contracts_by_source_selection(process_code="LPTA", date_from="01/01/2024",
                                         limit=100, offset=0):
    """
    Query the SAM.gov Contract Awards API for contracts by source selection process.

    Args:
        process_code: "LPTA", "TO", "O", or "LPTA~TO" for OR logic
        date_from: Start date in MM/DD/YYYY format
        limit: Records per page (max 100)
        offset: Pagination offset

    Returns:
        dict: API response JSON
    """
    params = {
        "api_key": API_KEY,
        "sourceSelectionProcess": process_code,
        "modificationNumber": "0",           # Base awards only
        "lastModifiedDate": f"[{date_from},]",
        "limit": limit,
        "offset": offset,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Query LPTA contracts
    print("=== LPTA Contracts ===")
    result = query_contracts_by_source_selection("LPTA")
    total = result.get("totalRecords", 0)
    print(f"Total LPTA records found: {total}")

    # Print first few results
    for contract in result.get("data", [])[:3]:
        competition = contract.get("competitionInformation", {})
        ssp = competition.get("sourceSelectionProcess", {})
        award_id = contract.get("contractId", {})
        print(f"  PIID: {award_id.get('piid', 'N/A')}")
        print(f"  Source Selection: {ssp.get('code', 'N/A')} - {ssp.get('name', 'N/A')}")
        print(f"  Extent Competed: {competition.get('extentCompeted', {}).get('name', 'N/A')}")
        print("  ---")

    # Query Trade-off (Best Value) contracts
    print("\n=== Trade-off (Best Value) Contracts ===")
    result = query_contracts_by_source_selection("TO")
    total = result.get("totalRecords", 0)
    print(f"Total Trade-off records found: {total}")
```

### Example 2: Paginated Download of All LPTA and Trade-off Awards

```python
"""
Download all LPTA and Trade-off contract awards from SAM.gov with pagination.
Saves results to a JSON file for later analysis.
Requires: pip install requests
"""
import requests
import json
import os
import time
from datetime import datetime

API_KEY = os.environ.get("SAM_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.sam.gov/contract-awards/v1/search"

# Rate limit: be conservative to stay within limits
# Individual key: 10 req/day; System account: 1,000+ req/day
REQUESTS_PER_DAY_LIMIT = 1000   # Adjust based on your key type
REQUEST_DELAY_SECONDS = 1.0      # Polite delay between requests


def fetch_awards_page(process_code, date_from, limit=100, offset=0):
    """Fetch a single page of contract awards."""
    params = {
        "api_key": API_KEY,
        "sourceSelectionProcess": process_code,
        "modificationNumber": "0",
        "lastModifiedDate": f"[{date_from},]",
        "limit": limit,
        "offset": offset,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 429:
        print("Rate limit hit! Stopping.")
        return None

    response.raise_for_status()
    return response.json()


def download_all_awards(process_code, date_from="01/01/2020", output_file=None):
    """
    Download all awards for a given source selection process.

    Args:
        process_code: "LPTA", "TO", or "LPTA~TO"
        date_from: Start date (MM/DD/YYYY)
        output_file: Path to save JSON output

    Returns:
        list: All contract records
    """
    all_records = []
    offset = 0
    limit = 100
    total_records = None
    request_count = 0

    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"sam_awards_{process_code}_{timestamp}.json"

    print(f"Downloading {process_code} awards from {date_from}...")

    while True:
        # Check rate limit
        if request_count >= REQUESTS_PER_DAY_LIMIT:
            print(f"Reached daily request limit ({REQUESTS_PER_DAY_LIMIT}). "
                  f"Downloaded {len(all_records)} of {total_records} records.")
            print("Resume tomorrow with offset={offset}")
            break

        data = fetch_awards_page(process_code, date_from, limit, offset)

        if data is None:
            break

        request_count += 1

        if total_records is None:
            total_records = data.get("totalRecords", 0)
            print(f"Total records to download: {total_records}")

        records = data.get("data", [])
        if not records:
            break

        all_records.extend(records)
        print(f"  Fetched {len(all_records):,} of {total_records:,} records "
              f"(request #{request_count})")

        if len(all_records) >= total_records:
            break

        offset += limit
        time.sleep(REQUEST_DELAY_SECONDS)

    # Save to file
    with open(output_file, "w") as f:
        json.dump({
            "query": {
                "sourceSelectionProcess": process_code,
                "dateFrom": date_from,
                "totalRecords": total_records,
                "recordsDownloaded": len(all_records),
                "downloadDate": datetime.now().isoformat(),
            },
            "data": all_records
        }, f, indent=2)

    print(f"\nSaved {len(all_records):,} records to {output_file}")
    return all_records


if __name__ == "__main__":
    # Download LPTA awards
    lpta_records = download_all_awards("LPTA", date_from="01/01/2020",
                                        output_file="sam_lpta_awards.json")

    # Download Trade-off (Best Value) awards
    to_records = download_all_awards("TO", date_from="01/01/2020",
                                      output_file="sam_tradeoff_awards.json")

    print(f"\n=== Summary ===")
    print(f"LPTA awards: {len(lpta_records):,}")
    print(f"Trade-off awards: {len(to_records):,}")
```

### Example 3: Extract Key Fields for Dissertation Analysis

```python
"""
Extract dissertation-relevant fields from SAM.gov contract awards data
and save to a CSV for statistical analysis.
Requires: pip install requests pandas
"""
import requests
import pandas as pd
import os
import time
import json

API_KEY = os.environ.get("SAM_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.sam.gov/contract-awards/v1/search"


def extract_contract_fields(contract):
    """
    Extract dissertation-relevant fields from a single contract record.

    Returns a flat dictionary suitable for a DataFrame row.
    """
    # Navigate nested JSON structure
    contract_id = contract.get("contractId", {})
    award_details = contract.get("awardDetails", {})
    competition = contract.get("competitionInformation", {})
    product_info = contract.get("productOrServiceInformation", {})
    place_of_perf = contract.get("principalPlaceOfPerformance", {})
    awardee = contract.get("awardee", {})

    return {
        # Contract identification
        "piid": contract_id.get("piid"),
        "modification_number": contract_id.get("modificationNumber"),
        "referenced_idv_piid": contract_id.get("referencedIdvPiid"),

        # Source selection -- THE KEY FIELD
        "source_selection_code": competition.get("sourceSelectionProcess", {}).get("code"),
        "source_selection_name": competition.get("sourceSelectionProcess", {}).get("name"),

        # Competition details
        "extent_competed_code": competition.get("extentCompeted", {}).get("code"),
        "extent_competed_name": competition.get("extentCompeted", {}).get("name"),
        "solicitation_procedures": competition.get("solicitationProcedures", {}).get("name"),
        "number_of_offers": competition.get("numberOfOffersSource", {}).get("code"),

        # Award details
        "dollars_obligated": award_details.get("dollarsObligated"),
        "base_and_exercised_options_value": award_details.get("baseAndExercisedOptionsValue"),
        "base_and_all_options_value": award_details.get("baseAndAllOptionsValue"),
        "date_signed": award_details.get("dateSigned"),
        "effective_date": award_details.get("effectiveDate"),
        "last_modified_date": award_details.get("lastModifiedDate"),

        # Product/service
        "naics_code": product_info.get("naicsCode"),
        "naics_description": product_info.get("naicsDescription"),
        "psc_code": product_info.get("productOrServiceCode"),

        # Contracting agency
        "contracting_department_code": contract.get("contractingDepartmentCode"),
        "contracting_department_name": contract.get("contractingDepartmentName"),
        "contracting_agency_code": contract.get("contractingAgencyCode"),
        "contracting_agency_name": contract.get("contractingAgencyName"),

        # Place of performance
        "pop_state": place_of_perf.get("stateCode"),
        "pop_country": place_of_perf.get("countryCode"),

        # Awardee (vendor) info
        "vendor_name": awardee.get("vendorName"),
        "vendor_uei": awardee.get("ueiSAM"),
        "vendor_duns": awardee.get("dunsNumber"),
    }


def download_and_extract(process_code, date_from="01/01/2020", max_records=None):
    """
    Download contract awards and extract key fields into a DataFrame.
    """
    all_rows = []
    offset = 0
    limit = 100
    total_records = None
    request_count = 0

    print(f"Downloading {process_code} awards from {date_from}...")

    while True:
        params = {
            "api_key": API_KEY,
            "sourceSelectionProcess": process_code,
            "modificationNumber": "0",
            "lastModifiedDate": f"[{date_from},]",
            "limit": limit,
            "offset": offset,
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 429:
            print("Rate limit hit. Stopping.")
            break

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text[:200]}")
            break

        data = response.json()
        request_count += 1

        if total_records is None:
            total_records = data.get("totalRecords", 0)
            print(f"Total records available: {total_records:,}")

        records = data.get("data", [])
        if not records:
            break

        for contract in records:
            row = extract_contract_fields(contract)
            all_rows.append(row)

        print(f"  Downloaded {len(all_rows):,} of {total_records:,} "
              f"(request #{request_count})")

        if max_records and len(all_rows) >= max_records:
            print(f"Reached max_records limit ({max_records})")
            break

        if len(all_rows) >= total_records:
            break

        offset += limit
        time.sleep(1.0)

    df = pd.DataFrame(all_rows)
    return df


if __name__ == "__main__":
    # Download LPTA awards
    df_lpta = download_and_extract("LPTA", date_from="01/01/2020")
    df_lpta.to_csv("sam_lpta_awards.csv", index=False)
    print(f"LPTA: {len(df_lpta):,} records saved to sam_lpta_awards.csv")

    # Download Trade-off (Best Value) awards
    df_to = download_and_extract("TO", date_from="01/01/2020")
    df_to.to_csv("sam_tradeoff_awards.csv", index=False)
    print(f"Trade-off: {len(df_to):,} records saved to sam_tradeoff_awards.csv")

    # Combine for analysis
    df_all = pd.concat([df_lpta, df_to], ignore_index=True)
    df_all.to_csv("sam_all_source_selection_awards.csv", index=False)
    print(f"\nCombined: {len(df_all):,} records saved to sam_all_source_selection_awards.csv")

    # Quick summary statistics
    print("\n=== Source Selection Distribution ===")
    print(df_all["source_selection_code"].value_counts())
    print(f"\n=== Average Dollars Obligated by Source Selection ===")
    print(df_all.groupby("source_selection_code")["dollars_obligated"].describe())
```

### Example 4: System Account Authentication (Higher Rate Limits)

```python
"""
Example using System Account authentication (header-based).
Use this if you have a System Account API key for higher rate limits.
"""
import requests
import base64
import os

# System Account credentials
SYSTEM_USERNAME = os.environ.get("SAM_SYSTEM_USERNAME")
SYSTEM_PASSWORD = os.environ.get("SAM_SYSTEM_PASSWORD")
SYSTEM_API_KEY = os.environ.get("SAM_SYSTEM_API_KEY")

BASE_URL = "https://api.sam.gov/contract-awards/v1/search"


def query_with_system_account(process_code="LPTA", date_from="01/01/2020",
                               limit=100, offset=0):
    """
    Query using System Account authentication (higher rate limits).
    """
    # Encode credentials for Basic Auth
    credentials = f"{SYSTEM_USERNAME}:{SYSTEM_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "x-api-key": SYSTEM_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    # Note: api_key is NOT in the URL params for system accounts
    params = {
        "sourceSelectionProcess": process_code,
        "modificationNumber": "0",
        "lastModifiedDate": f"[{date_from},]",
        "limit": limit,
        "offset": offset,
    }

    response = requests.get(BASE_URL, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = query_with_system_account("LPTA")
    print(f"Total records: {result.get('totalRecords', 0):,}")
```

---

## 10. Response Structure

The API returns JSON with the following top-level structure:

```json
{
  "totalRecords": 15432,
  "limit": 100,
  "offset": 0,
  "data": [
    {
      "contractId": {
        "piid": "GS-35F-0001A",
        "modificationNumber": "0",
        "referencedIdvPiid": "..."
      },
      "competitionInformation": {
        "extentCompeted": {
          "code": "A",
          "name": "FULL AND OPEN COMPETITION"
        },
        "solicitationProcedures": {
          "code": "NP",
          "name": "NEGOTIATED PROPOSAL/QUOTE"
        },
        "sourceSelectionProcess": {
          "code": "LPTA",
          "name": "LOWEST PRICE TECHNICALLY ACCEPTABLE"
        },
        "localAreaSetAside": { "name": "N" },
        "a76Action": { "code": "N", "name": "NO" },
        "preAwardSynopsisRequirement": { "code": "N", "name": "No" },
        "smallBusinessCompetitivenessDemonstrationProgram": { "name": "NO" },
        "numberOfOffersSource": { "code": "B", "name": "IDC" }
      },
      "awardDetails": {
        "dollarsObligated": 1500000.00,
        "baseAndExercisedOptionsValue": 2000000.00,
        "baseAndAllOptionsValue": 5000000.00,
        "dateSigned": "2024-03-15",
        "effectiveDate": "2024-04-01",
        "lastModifiedDate": "2024-06-01"
      },
      "productOrServiceInformation": {
        "naicsCode": "541512",
        "naicsDescription": "COMPUTER SYSTEMS DESIGN SERVICES",
        "productOrServiceCode": "D302"
      },
      "principalPlaceOfPerformance": {
        "stateCode": "VA",
        "countryCode": "USA"
      },
      "awardee": {
        "vendorName": "ACME CONSULTING LLC",
        "ueiSAM": "ABC123DEF456",
        "dunsNumber": "123456789"
      },
      "legislativeMandates": { "...": "..." },
      "acquisitionMarketingData": { "...": "..." }
    }
  ]
}
```

### Key Response Fields for Dissertation Research

| JSON Path | Description | Research Use |
|---|---|---|
| `competitionInformation.sourceSelectionProcess.code` | LPTA, TO, or O | **Primary independent variable** |
| `competitionInformation.extentCompeted.code` | Competition level (A=Full & Open, etc.) | Control variable |
| `awardDetails.dollarsObligated` | Dollars obligated | Outcome / control variable |
| `awardDetails.baseAndAllOptionsValue` | Total potential value | Outcome variable |
| `productOrServiceInformation.naicsCode` | Industry code | Stratification / control |
| `awardDetails.dateSigned` | Award date | Time variable |
| `competitionInformation.numberOfOffersSource` | Number of offers received | Outcome / mediator |

---

## 11. Rate Limits & Practical Tips

### Rate Limit Summary

| Key Type | Requests/Day | Best For |
|---|---|---|
| No key (public) | 10 | Quick testing |
| Individual (public) API key | 10-1,000 (varies by account type) | Initial exploration |
| System Account (non-federal) | 1,000 | Research data collection |
| System Account (federal) | 10,000 | Large-scale analysis |

### Practical Tips for Dissertation Research

1. **Start with the Individual Key immediately.** You can begin exploring the data structure and testing queries today while waiting for a System Account (if needed).

2. **Use `modificationNumber=0`** to get only base awards (not contract modifications), which simplifies analysis.

3. **Use the Extract/CSV format** for large downloads: Add `format=csv` to your request to get asynchronous CSV downloads (up to 1,000,000 records). This is more efficient than paginating through JSON.

4. **Cache everything locally.** Save all API responses to disk. Contract award data is historical and does not change frequently.

5. **Paginate efficiently.** With 100 records per page, downloading 100,000 records requires 1,000 API calls. At the System Account rate of 1,000 requests/day, this takes 1 day. With the Individual key at 10/day, it would take 100 days -- hence the value of a System Account.

6. **Filter aggressively.** Use `sourceSelectionProcess=LPTA~TO` to exclude "Other" records and reduce the dataset to only the records relevant to your LPTA vs. best-value comparison.

7. **Date range strategy.** Source selection process data is only available from ~FY2020 onward. Query from `01/01/2020` to capture all available data.

8. **Handle 429 errors gracefully.** If you hit rate limits, your code should stop and save progress, then resume from the last offset.

---

## 12. Important Data Caveats

1. **Source selection data starts in FY2020.** FPDS did not collect `sourceSelectionProcess` data before 2020. The FY2020 NDAA Section 806 mandated this field.

2. **Revealed vs. Unrevealed data.** DoD contracts signed within the last 90 days are "unrevealed" and only accessible with a System Account or federal credentials. For historical research (FY2020-2024), this is not an issue.

3. **Maximum record limit.** The API returns a maximum of 400,000 records per query (search mode) or 1,000,000 records (extract mode). If your query exceeds this, narrow it with additional filters (e.g., by fiscal year or department).

4. **"Other" category is large.** Many contracts use `sourceSelectionProcess=O` (Other), which includes sole-source, simplified acquisition, and other non-LPTA/non-tradeoff methods. Your analysis should focus on LPTA vs. TO and potentially use "Other" as a comparison group.

5. **FPDS migration to SAM.gov.** Contract awards data migration to SAM.gov launched in July 2025. The API is the authoritative source going forward, replacing the legacy FPDS Atom Feed.

---

## 13. Sources & References

- [SAM.gov Contract Awards API -- Official Documentation (GSA Open Technology)](https://open.gsa.gov/api/contract-awards/)
- [SAM.gov Help Center](https://sam.gov/help)
- [SAM.gov API Key Usage Documentation](https://api.sam.gov/docs/api-key/)
- [System Account User Guide v3.0 (State Department PDF)](https://www.state.gov/wp-content/uploads/2025/05/SAM-User-Guide.pdf)
- [System Account User Guide v3.01 (DoD Procurement Toolbox)](https://dodprocurementtoolbox.com/uploads/System_Account_User_Guide_v3_01_5f66649acf.pdf)
- [FPDS Source Selection Process Help](https://www.fpds.gov/help/Source_Selection_Process.htm)
- [FPDS Atom Feed vs SAM Contract API Mapping (GSA PDF)](https://open.gsa.gov/api/contract-awards/v1/FPDSvsSAM-ContractDataAPI.pdf)
- [FAR 15.101-1 Tradeoff Process (Acquisition.gov)](https://www.acquisition.gov/far/15.101-1)
- [FAR 15.101-2 LPTA Process (Acquisition.gov)](https://www.acquisition.gov/far/15.101-2)
- [DLAD 4.606-90 Source Selection Process Data Element (Acquisition.gov)](https://www.acquisition.gov/dlad/4.606-90-source-selection-process-data-element.)
- [SAM.gov Entity Management API Documentation (GSA Open Technology)](https://open.gsa.gov/api/entity-api/)
- [GSA APIs Portal](https://open.gsa.gov/api/)
- [SAM.gov API Rate Limits Documentation (GovCon API)](https://govconapi.com/sam-gov-rate-limits-reality)
- [SAM.gov API Developer Guide (GovCon API)](https://govconapi.com/sam-gov-api-guide)
