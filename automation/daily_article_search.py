#!/usr/bin/env python3
"""
Daily Article Search for PhD Research

Searches for new scholarly articles relevant to the dissertation topic:
"From Lowest Price to Highest Public Value: Best-Value Source Selection in Government RFPs"

Stores results in a local SQLite database and generates a daily digest.

Usage:
    python daily_article_search.py              # Run daily search
    python daily_article_search.py --report     # Generate summary report
    python daily_article_search.py --export     # Export database to CSV

Schedule with cron/launchd for daily automation.
"""

import argparse
import hashlib
import json
import os
import re
import sqlite3
import urllib.parse
from datetime import datetime, timedelta
from pathlib import Path

import requests

DB_PATH = Path(__file__).parent.parent / "research" / "articles" / "articles.db"
DIGEST_DIR = Path(__file__).parent.parent / "research" / "articles" / "digests"

# Search queries organized by research topic
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

# Google Scholar search URL (for reference - actual scraping requires care)
SCHOLAR_BASE = "https://scholar.google.com/scholar"

# Semantic Scholar API (free, no key required, academic article search)
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"

# OpenAlex API (free, open academic metadata)
OPENALEX_API = "https://api.openalex.org"


def init_database():
    """Initialize the SQLite database for storing articles."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            authors TEXT,
            year INTEGER,
            journal TEXT,
            abstract TEXT,
            doi TEXT,
            url TEXT,
            citation_count INTEGER DEFAULT 0,
            search_query TEXT,
            source TEXT,
            relevance_score REAL DEFAULT 0.0,
            date_found TEXT,
            date_published TEXT,
            read_status TEXT DEFAULT 'unread',
            notes TEXT,
            tags TEXT,
            bibtex TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_date TEXT,
            query TEXT,
            source TEXT,
            results_count INTEGER,
            new_articles INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_digest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            digest_date TEXT,
            total_new INTEGER,
            top_articles TEXT,
            summary TEXT
        )
    """)

    conn.commit()
    return conn


def generate_article_id(title, authors=""):
    """Generate a unique ID for an article based on title and authors."""
    text = f"{title.lower().strip()}|{authors.lower().strip()}"
    return hashlib.md5(text.encode()).hexdigest()


def search_openalex(query, per_page=25):
    """
    Search OpenAlex for academic articles.

    OpenAlex is free, open, and has excellent coverage of academic literature.
    No API key required.
    """
    url = f"{OPENALEX_API}/works"
    params = {
        "search": query,
        "per_page": per_page,
        "sort": "relevance_score:desc",
        "filter": "type:article",
        "select": "id,title,authorships,publication_year,primary_location,cited_by_count,doi,abstract_inverted_index",
    }

    try:
        resp = requests.get(url, params=params, headers={"User-Agent": "mailto:research@example.com"})
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
        print(f"  OpenAlex search error: {e}")
        return []


def search_semantic_scholar(query, limit=20):
    """
    Search Semantic Scholar for academic articles.

    Free API, no key required for basic usage (100 requests/5 min).
    """
    url = f"{SEMANTIC_SCHOLAR_API}/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,venue,abstract,externalIds,citationCount,url",
    }

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        results = []

        for paper in data.get("data", []):
            authors = "; ".join(
                a.get("name", "Unknown") for a in paper.get("authors", [])[:5]
            )
            doi = paper.get("externalIds", {}).get("DOI", "")

            results.append({
                "title": paper.get("title", ""),
                "authors": authors,
                "year": paper.get("year"),
                "journal": paper.get("venue", ""),
                "abstract": paper.get("abstract", ""),
                "doi": doi,
                "url": paper.get("url", ""),
                "citation_count": paper.get("citationCount", 0),
                "source": "semantic_scholar",
            })

        return results

    except requests.exceptions.RequestException as e:
        print(f"  Semantic Scholar search error: {e}")
        return []


def store_articles(conn, articles, query):
    """Store new articles in the database. Returns count of new articles."""
    cursor = conn.cursor()
    new_count = 0

    for article in articles:
        article_id = generate_article_id(article["title"], article.get("authors", ""))

        # Check if already exists
        cursor.execute("SELECT id FROM articles WHERE id = ?", (article_id,))
        if cursor.fetchone():
            # Update citation count if higher
            cursor.execute(
                "UPDATE articles SET citation_count = MAX(citation_count, ?) WHERE id = ?",
                (article.get("citation_count", 0), article_id),
            )
            continue

        cursor.execute(
            """INSERT INTO articles
            (id, title, authors, year, journal, abstract, doi, url,
             citation_count, search_query, source, date_found)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                article_id,
                article.get("title", ""),
                article.get("authors", ""),
                article.get("year"),
                article.get("journal", ""),
                article.get("abstract", ""),
                article.get("doi", ""),
                article.get("url", ""),
                article.get("citation_count", 0),
                query,
                article.get("source", ""),
                datetime.now().isoformat(),
            ),
        )
        new_count += 1

    conn.commit()
    return new_count


def run_daily_search(conn):
    """Run the daily search across all queries and sources."""
    print(f"Daily Article Search - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    total_new = 0
    cursor = conn.cursor()

    for i, query in enumerate(SEARCH_QUERIES):
        print(f"\n[{i+1}/{len(SEARCH_QUERIES)}] Searching: {query}")

        # Search OpenAlex
        print("  Searching OpenAlex...", end=" ")
        articles = search_openalex(query, per_page=10)
        new = store_articles(conn, articles, query)
        print(f"Found {len(articles)}, {new} new")

        cursor.execute(
            "INSERT INTO search_log (search_date, query, source, results_count, new_articles) VALUES (?, ?, ?, ?, ?)",
            (datetime.now().isoformat(), query, "openalex", len(articles), new),
        )
        total_new += new

        # Search Semantic Scholar (with rate limiting)
        print("  Searching Semantic Scholar...", end=" ")
        import time
        time.sleep(3)  # Rate limit: 100 requests per 5 minutes
        articles = search_semantic_scholar(query, limit=10)
        new = store_articles(conn, articles, query)
        print(f"Found {len(articles)}, {new} new")

        cursor.execute(
            "INSERT INTO search_log (search_date, query, source, results_count, new_articles) VALUES (?, ?, ?, ?, ?)",
            (datetime.now().isoformat(), query, "semantic_scholar", len(articles), new),
        )
        total_new += new

    conn.commit()

    # Generate daily digest
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    digest_date = datetime.now().strftime("%Y-%m-%d")

    # Get today's new articles sorted by citation count
    cursor.execute(
        """SELECT title, authors, year, journal, citation_count, abstract
        FROM articles WHERE date(date_found) = date('now')
        ORDER BY citation_count DESC LIMIT 20""",
    )
    top_articles = cursor.fetchall()

    digest_path = DIGEST_DIR / f"digest_{digest_date}.md"
    with open(digest_path, "w") as f:
        f.write(f"# Daily Article Digest - {digest_date}\n\n")
        f.write(f"**New articles found today: {total_new}**\n\n")
        f.write("## Top New Articles (by citation count)\n\n")

        for i, (title, authors, year, journal, citations, abstract) in enumerate(top_articles, 1):
            f.write(f"### {i}. {title}\n")
            f.write(f"- **Authors:** {authors}\n")
            f.write(f"- **Year:** {year}\n")
            f.write(f"- **Journal:** {journal}\n")
            f.write(f"- **Citations:** {citations}\n")
            if abstract:
                f.write(f"- **Abstract:** {abstract[:300]}...\n")
            f.write("\n")

    print(f"\n{'='*60}")
    print(f"Search complete. {total_new} new articles found.")
    print(f"Digest saved: {digest_path}")

    # Save digest record
    cursor.execute(
        "INSERT INTO daily_digest (digest_date, total_new, summary) VALUES (?, ?, ?)",
        (digest_date, total_new, f"Found {total_new} new articles across {len(SEARCH_QUERIES)} queries"),
    )
    conn.commit()


def generate_report(conn):
    """Generate a summary report of all articles in the database."""
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM articles")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT search_query) FROM articles")
    queries = cursor.fetchone()[0]

    cursor.execute(
        "SELECT title, authors, year, journal, citation_count FROM articles ORDER BY citation_count DESC LIMIT 25"
    )
    top_articles = cursor.fetchall()

    print(f"\nArticle Database Report")
    print(f"{'='*60}")
    print(f"Total articles: {total}")
    print(f"Unique search queries: {queries}")
    print(f"\nTop 25 Articles by Citation Count:")
    print(f"{'-'*60}")

    for i, (title, authors, year, journal, citations) in enumerate(top_articles, 1):
        print(f"{i:3d}. [{citations:,} cites] {title}")
        print(f"     {authors} ({year}) - {journal}")


def export_to_csv(conn):
    """Export the article database to CSV."""
    import pandas as pd

    df = pd.read_sql_query("SELECT * FROM articles ORDER BY citation_count DESC", conn)
    export_path = DB_PATH.parent / "articles_export.csv"
    df.to_csv(export_path, index=False)
    print(f"Exported {len(df)} articles to {export_path}")


def main():
    parser = argparse.ArgumentParser(description="Daily academic article search")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--export", action="store_true", help="Export to CSV")
    args = parser.parse_args()

    conn = init_database()

    if args.report:
        generate_report(conn)
    elif args.export:
        export_to_csv(conn)
    else:
        run_daily_search(conn)

    conn.close()


if __name__ == "__main__":
    main()
