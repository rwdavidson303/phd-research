#!/usr/bin/env python3
"""
Generate research reports as website pages.

Reads the article database and research files, then generates
markdown pages for the Hugo website. Run this anytime to update
the site with the latest data.

Usage:
    python generate_site_reports.py
"""

import sqlite3
from datetime import datetime
from pathlib import Path

PROJECT = Path.home() / "phd-research"
SITE_CONTENT = PROJECT / "website" / "content"
ARTICLES_DB = PROJECT / "research" / "articles" / "articles.db"


def _article_link(title, doi, url):
    """Return a markdown link for the article title.

    Prefers DOI link (https://doi.org/...) when available,
    falls back to the OpenAlex/source URL.
    """
    display = title or "Untitled"
    if doi:
        # Some DOIs in the DB are already full URLs
        if doi.startswith("http"):
            href = doi
        else:
            href = f"https://doi.org/{doi}"
    elif url:
        href = url
    else:
        return display  # no link available
    # Escape pipes in title so markdown tables don't break
    display = display.replace("|", "–")
    return f"[{display}]({href})"


def generate_articles_page():
    """Generate the articles feed page from the database."""
    if not ARTICLES_DB.exists():
        print("  No article database found. Run daily_article_search.py first.")
        return

    conn = sqlite3.connect(str(ARTICLES_DB))
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM articles")
    total = c.fetchone()[0]

    # Get ALL articles ordered newest to oldest (by year, then citations as tiebreaker)
    c.execute("""
        SELECT title, authors, year, journal, citation_count, doi, url
        FROM articles
        ORDER BY year DESC, citation_count DESC
    """)
    all_articles = c.fetchall()

    conn.close()

    # Build the page
    page = f"""---
title: "Articles Feed"
description: "Scholarly articles discovered by automated daily search"
weight: 6
---

## Article Database

**{total} total articles** in the database | Last updated: {datetime.now().strftime('%B %d, %Y')}

Articles are discovered automatically each morning through searches of OpenAlex and Semantic Scholar. Click any title to read the original article.

---

## All Articles — Newest First

| # | Article | Authors | Year | Journal | Citations |
|---|---------|---------|------|---------|-----------|
"""
    for i, (title, authors, year, journal, cites, doi, url) in enumerate(all_articles, 1):
        # Build linked title, truncated for table readability
        short_title = (title[:70] + "...") if title and len(title) > 70 else (title or "")
        linked_title = _article_link(short_title, doi, url)
        short_authors = (authors[:40] + "...") if authors and len(authors) > 40 else (authors or "")
        short_journal = (journal[:30] + "...") if journal and len(journal) > 30 else (journal or "")
        page += f"| {i} | {linked_title} | {short_authors} | {year or ''} | {short_journal} | {cites or 0:,} |\n"

    output = SITE_CONTENT / "articles" / "_index.md"
    output.write_text(page)
    print(f"  Articles page: {output}")


def generate_literature_page():
    """Copy the top 100 articles list to the website."""
    source = PROJECT / "research" / "articles" / "top_100_articles.md"
    if not source.exists():
        print("  No top 100 articles file found.")
        return

    content = source.read_text()

    page = f"""---
title: "Literature & Bibliography"
description: "Top 100 scholarly articles and recommended books"
weight: 2
---

{content}
"""
    output = SITE_CONTENT / "literature" / "_index.md"
    output.write_text(page)
    print(f"  Literature page: {output}")


def generate_books_page():
    """Create a books subpage."""
    source = PROJECT / "research" / "books" / "recommended_books.md"
    if not source.exists():
        return

    content = source.read_text()
    books_dir = SITE_CONTENT / "literature" / "books"
    books_dir.mkdir(parents=True, exist_ok=True)

    page = f"""---
title: "Recommended Books"
description: "Essential reading for the dissertation"
weight: 1
---

{content}
"""
    output = books_dir / "_index.md"
    output.write_text(page)
    print(f"  Books page: {output}")


def generate_people_page():
    """Copy the influential people list to the website."""
    source = PROJECT / "research" / "people" / "top_25_influential_people.md"
    if not source.exists():
        return

    content = source.read_text()

    page = f"""---
title: "Key People in Procurement"
description: "Top 25 most influential people in US government RFPs"
weight: 5
---

{content}
"""
    output = SITE_CONTENT / "people" / "_index.md"
    output.write_text(page)
    print(f"  People page: {output}")


def generate_global_page():
    """Copy the global practices report to the website."""
    source = PROJECT / "research" / "global-practices" / "successful_rfp_processes_worldwide.md"
    if not source.exists():
        return

    content = source.read_text()

    page = f"""---
title: "Global Best Practices"
description: "Successful procurement systems around the world"
weight: 4
---

{content}
"""
    output = SITE_CONTENT / "global" / "_index.md"
    output.write_text(page)
    print(f"  Global practices page: {output}")


def main():
    print(f"Generating website reports - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)

    generate_articles_page()
    generate_literature_page()
    generate_books_page()
    generate_people_page()
    generate_global_page()

    print()
    print("Done! Preview your site:")
    print(f"  cd {PROJECT / 'website'} && hugo server")
    print()
    print("Then push to publish:")
    print("  cd ~/phd-research && git add -A && git commit -m 'Update site' && git push")


if __name__ == "__main__":
    main()
