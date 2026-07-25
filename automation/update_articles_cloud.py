#!/usr/bin/env python3
"""
Cloud-friendly article search and site update.

Designed to run in GitHub Actions (no SQLite, no local paths).
Searches OpenAlex for new scholarly articles, updates articles.json,
and regenerates the Hugo articles page.

Usage:
    python automation/update_articles_cloud.py          # Run from repo root
    python automation/update_articles_cloud.py --dry-run # Search but don't write
"""

import argparse
import hashlib
import html
import json
import re
import time
from datetime import datetime
from pathlib import Path

import requests

# Paths relative to repo root (GitHub Actions checks out to workspace root)
REPO_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_JSON = REPO_ROOT / "research" / "articles" / "articles.json"
ARTICLES_PAGE = REPO_ROOT / "website" / "content" / "articles" / "_index.md"
DIGEST_DIR = REPO_ROOT / "research" / "articles" / "digests"

# OpenAlex API (free, open, no auth required)
OPENALEX_API = "https://api.openalex.org"

# Same search queries as daily_article_search.py
SEARCH_QUERIES = [
    # Core topic
    "best value source selection government procurement",
    "LPTA lowest price technically acceptable outcomes",
    "best value tradeoff public procurement",
    # Public value
    "public value theory procurement",
    "value for money public procurement",
    # Transaction cost economics
    "transaction cost economics government contracts",
    "contract incompleteness procurement",
    # Bid protests
    "bid protest government procurement delay",
    "GAO bid protest outcomes",
    "procurement protest accountability",
    # Procurement reform
    "procurement reform federal acquisition",
    "procurement administrative lead time PALT",
    "government procurement modernization",
    # RFP design
    "RFP requirements clarity solicitation quality",
    "incumbent advantage procurement tender steering",
    # Change orders / renegotiation
    "strategic underbidding government contracts",
    "change orders renegotiation public procurement",
    "post-award cost growth government contracts",
    # Oversight
    "procurement oversight review boards delay",
    # Competition
    "competition public procurement innovation",
    # Methods
    "difference-in-differences procurement policy",
    "propensity score matching public administration",
]


def generate_article_id(title, authors=""):
    """Generate a unique ID for an article based on title and authors."""
    text = f"{title.lower().strip()}|{authors.lower().strip()}"
    return hashlib.md5(text.encode()).hexdigest()


def search_openalex(query, per_page=10):
    """Search OpenAlex for academic articles."""
    url = f"{OPENALEX_API}/works"
    params = {
        "search": query,
        "per_page": per_page,
        "sort": "relevance_score:desc",
        "filter": "type:article",
        "select": "id,title,authorships,publication_year,primary_location,cited_by_count,doi,abstract_inverted_index",
    }

    try:
        resp = requests.get(
            url,
            params=params,
            headers={"User-Agent": "mailto:phd-research@example.com"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        results = []

        for work in data.get("results", []):
            # Reconstruct abstract from inverted index
            abstract = ""
            if work.get("abstract_inverted_index"):
                inv_idx = work["abstract_inverted_index"]
                words = {}
                for word, positions in inv_idx.items():
                    for pos in positions:
                        words[pos] = word
                abstract = " ".join(words[k] for k in sorted(words.keys()))

            # Extract author names
            authors = "; ".join(
                a.get("author", {}).get("display_name", "Unknown")
                for a in work.get("authorships", [])[:5]
            )

            # Extract journal
            journal = ""
            loc = work.get("primary_location", {})
            if loc and loc.get("source"):
                journal = loc["source"].get("display_name", "")

            results.append({
                "title": work.get("title", ""),
                "authors": authors,
                "year": work.get("publication_year"),
                "journal": journal,
                "abstract": abstract,
                "doi": work.get("doi", ""),
                "url": work.get("id", ""),
                "citation_count": work.get("cited_by_count", 0),
                "source": "openalex",
            })

        return results

    except requests.exceptions.RequestException as e:
        print(f"  OpenAlex error: {e}")
        return []


def load_articles():
    """Load the existing articles JSON file."""
    if not ARTICLES_JSON.exists():
        return {"metadata": {}, "articles": []}
    with open(ARTICLES_JSON) as f:
        return json.load(f)


def save_articles(data):
    """Save the articles JSON file."""
    ARTICLES_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(ARTICLES_JSON, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def sanitize_markdown(text):
    """Sanitize text for safe use in markdown tables."""
    text = text.replace("|", "–")
    text = text.replace("[", "(").replace("]", ")")
    text = text.replace("\n", " ").replace("\r", "")
    return text


def article_link(title, doi, url):
    """Return a markdown link for an article title."""
    display = sanitize_markdown(title) if title else "Untitled"
    if doi:
        href = doi if doi.startswith("http") else f"https://doi.org/{doi}"
    elif url:
        href = url
    else:
        return display
    # Only allow https DOI/OpenAlex URLs
    if not href.startswith(("https://doi.org/", "https://openalex.org/")):
        return display
    return f"[{display}]({href})"


def generate_articles_page(articles):
    """Generate the Hugo articles markdown page."""
    total = len(articles)
    # Sort newest first, then by citations
    sorted_articles = sorted(
        articles,
        key=lambda a: (a.get("year") or 0, a.get("citation_count") or 0),
        reverse=True,
    )

    page = f"""---
title: "Articles Feed"
description: "Scholarly articles discovered by automated daily search"
weight: 6
---

## Article Database

**{total} total articles** in the database | Last updated: {datetime.now().strftime('%B %d, %Y')}

Articles are discovered automatically each day through searches of OpenAlex. Click any title to read the original article.

---

## All Articles — Newest First

<div class="articles-table-wrap">

| # | Article | Authors | Year | Journal | Citations |
|---|---------|---------|------|---------|-----------|
"""
    for i, a in enumerate(sorted_articles, 1):
        title = a.get("title") or ""
        short_title = (title[:70] + "...") if len(title) > 70 else title
        linked = article_link(short_title, a.get("doi", ""), a.get("url", ""))
        authors = a.get("authors") or ""
        short_authors = (authors[:40] + "...") if len(authors) > 40 else authors
        journal = a.get("journal") or ""
        short_journal = (journal[:30] + "...") if len(journal) > 30 else journal
        year = a.get("year") or ""
        cites = a.get("citation_count") or 0
        page += f"| {i} | {linked} | {short_authors} | {year} | {short_journal} | {cites:,} |\n"

    page += "\n</div>"

    ARTICLES_PAGE.parent.mkdir(parents=True, exist_ok=True)
    ARTICLES_PAGE.write_text(page)


def normalize_doi(doi):
    """Normalize a DOI for comparison: lowercase, strip trailing slash and
    any doi.org URL prefix, so "https://doi.org/10.x/y" == "10.x/y"."""
    d = (doi or "").strip().rstrip("/").lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi.org/"):
        if d.startswith(prefix):
            d = d[len(prefix):]
            break
    return d


def normalize_title(title):
    """Normalize a title for comparison: unescape HTML entities (twice, for
    double-escaped values like "R&amp;amp;D"), then keep only [a-z0-9]."""
    raw = html.unescape(html.unescape(title or ""))
    return re.sub(r'[^a-z0-9]', '', raw.lower())


def deduplicate_articles(existing):
    """Remove duplicate articles by checking DOI and normalized titles.

    Returns the deduplicated dict and count of removed duplicates.
    """
    # Build DOI index to find duplicates with same DOI but different title/author hash
    doi_index = {}
    duplicates_to_remove = set()

    for aid, article in existing.items():
        doi_lower = normalize_doi(article.get("doi"))
        if not doi_lower:
            continue
        if doi_lower in doi_index:
            # Keep the one with higher citations, or the earlier one
            other_aid = doi_index[doi_lower]
            other = existing[other_aid]
            if (article.get("citation_count") or 0) > (other.get("citation_count") or 0):
                duplicates_to_remove.add(other_aid)
                doi_index[doi_lower] = aid
            else:
                duplicates_to_remove.add(aid)
        else:
            doi_index[doi_lower] = aid

    # Also check for near-duplicate titles (same title, different author formatting)
    title_index = {}
    for aid, article in existing.items():
        if aid in duplicates_to_remove:
            continue
        title_norm = normalize_title(article.get("title"))
        if not title_norm:
            continue
        if title_norm in title_index:
            other_aid = title_index[title_norm]
            other = existing[other_aid]
            if (article.get("citation_count") or 0) > (other.get("citation_count") or 0):
                duplicates_to_remove.add(other_aid)
                title_index[title_norm] = aid
            else:
                duplicates_to_remove.add(aid)
        else:
            title_index[title_norm] = aid

    for aid in duplicates_to_remove:
        del existing[aid]

    return existing, len(duplicates_to_remove)


def generate_digest(new_articles):
    """Generate a daily digest markdown file for newly found articles."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    digest_date = datetime.now().strftime("%Y-%m-%d")
    digest_path = DIGEST_DIR / f"digest_{digest_date}.md"

    # Sort new articles by citation count
    sorted_new = sorted(new_articles, key=lambda a: a.get("citation_count") or 0, reverse=True)

    with open(digest_path, "w") as f:
        f.write(f"# Daily Article Digest - {digest_date}\n\n")
        f.write(f"**New articles found today: {len(sorted_new)}**\n\n")

        if not sorted_new:
            f.write("No new articles discovered today.\n")
        else:
            f.write("## Top New Articles (by citation count)\n\n")
            for i, a in enumerate(sorted_new[:20], 1):
                f.write(f"### {i}. {a.get('title', 'Untitled')}\n")
                f.write(f"- **Authors:** {a.get('authors', 'Unknown')}\n")
                f.write(f"- **Year:** {a.get('year', 'N/A')}\n")
                f.write(f"- **Journal:** {a.get('journal', 'N/A')}\n")
                f.write(f"- **Citations:** {a.get('citation_count', 0)}\n")
                abstract = a.get("abstract", "")
                if abstract:
                    f.write(f"- **Abstract:** {abstract[:300]}...\n")
                f.write("\n")

    print(f"Digest saved: {digest_path}")
    return digest_path


def run_search(dry_run=False):
    """Search OpenAlex, update JSON, regenerate Hugo page."""
    print(f"Article Search - {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)

    data = load_articles()
    existing = {a["id"]: a for a in data.get("articles", [])}

    # Deduplicate existing articles first
    existing, dedup_count = deduplicate_articles(existing)
    if dedup_count:
        print(f"Removed {dedup_count} duplicate articles from database")

    initial_count = len(existing)
    new_count = 0
    updated_count = 0
    new_articles = []

    # Build DOI index for fast lookup during search
    doi_set = set()
    title_set = set()
    for a in existing.values():
        doi = normalize_doi(a.get("doi"))
        if doi:
            doi_set.add(doi)
        title_norm = normalize_title(a.get("title"))
        if title_norm:
            title_set.add(title_norm)

    for i, query in enumerate(SEARCH_QUERIES):
        print(f"[{i + 1}/{len(SEARCH_QUERIES)}] {query}")

        results = search_openalex(query, per_page=10)
        print(f"  Found {len(results)} results", end="")

        query_new = 0
        for article in results:
            aid = generate_article_id(article["title"], article.get("authors", ""))

            # Check by ID (title+author hash)
            if aid in existing:
                old_cites = existing[aid].get("citation_count") or 0
                new_cites = article.get("citation_count") or 0
                if new_cites > old_cites:
                    existing[aid]["citation_count"] = new_cites
                    updated_count += 1
                continue

            # Check by DOI
            doi = normalize_doi(article.get("doi"))
            if doi and doi in doi_set:
                continue

            # Check by normalized title
            title_norm = normalize_title(article.get("title"))
            if title_norm and title_norm in title_set:
                continue

            article["id"] = aid
            article["date_found"] = datetime.now().isoformat()
            article["search_query"] = query
            existing[aid] = article
            new_articles.append(article)
            new_count += 1
            query_new += 1

            # Track new entries for future iterations
            if doi:
                doi_set.add(doi)
            if title_norm:
                title_set.add(title_norm)

        print(f", {query_new} new")

        # Be polite to the API
        time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print(f"Total: {new_count} new articles, {updated_count} citation updates")
    print(f"Database: {initial_count} → {len(existing)} articles")

    if dry_run:
        print("\nDry run — no files written.")
        return

    # Save updated JSON
    data["articles"] = list(existing.values())
    data["metadata"] = {
        "last_updated": datetime.now().isoformat(),
        "total_articles": len(existing),
        "last_search_date": datetime.now().strftime("%Y-%m-%d"),
    }
    save_articles(data)
    print(f"Updated: {ARTICLES_JSON}")

    # Regenerate Hugo page
    generate_articles_page(data["articles"])
    print(f"Updated: {ARTICLES_PAGE}")

    # Generate daily digest
    generate_digest(new_articles)


def main():
    parser = argparse.ArgumentParser(description="Cloud article search and site update")
    parser.add_argument("--dry-run", action="store_true", help="Search but don't write files")
    args = parser.parse_args()
    run_search(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
