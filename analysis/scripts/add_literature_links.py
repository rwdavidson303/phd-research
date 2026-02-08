#!/usr/bin/env python3
"""
One-time script: Add DOI links to the top 100 articles and reorder
each topic section newest-first.

Reads research/articles/top_100_articles.md, looks up DOIs via CrossRef,
adds hyperlinks to article titles, reorders by year within each section,
and writes the result back.
"""

import re
import time
import urllib.parse
import urllib.request
import json
from pathlib import Path

PROJECT = Path.home() / "phd-research"
SOURCE = PROJECT / "research" / "articles" / "top_100_articles.md"

# CrossRef polite pool — include email for faster responses
CROSSREF_BASE = "https://api.crossref.org/works"
MAILTO = "rwdavidson303@gmail.com"


def lookup_doi(title, author_last=None, year=None):
    """Look up a DOI from CrossRef by title. Returns DOI string or None."""
    # Clean the title for query
    clean = re.sub(r"[*_\[\]()]", "", title).strip()
    clean = clean[:200]  # CrossRef has query length limits

    params = {"query.title": clean, "rows": "1", "mailto": MAILTO}
    if author_last:
        params["query.author"] = author_last
    url = f"{CROSSREF_BASE}?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": f"PhDResearch/1.0 (mailto:{MAILTO})"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            items = data.get("message", {}).get("items", [])
            if items:
                item = items[0]
                # Verify title is a reasonable match
                item_title = " ".join(item.get("title", [""])).lower()
                query_words = set(clean.lower().split()[:6])
                match_words = set(item_title.split()[:6])
                overlap = len(query_words & match_words)
                if overlap >= min(3, len(query_words)):
                    return item.get("DOI")
    except Exception:
        pass
    return None


def parse_articles(text):
    """Parse the markdown into sections and articles."""
    # Split into sections by ## headers
    sections = []
    current_section = None
    current_articles = []
    lines = text.split("\n")

    # Track everything before first topic section
    preamble_lines = []
    in_preamble = True

    # Track everything after last section (summary stats, notes, etc.)
    postamble_start = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect section headers like "## 1. Source Selection..."
        section_match = re.match(r"^## (\d+)\. (.+)$", line)
        # Detect supplemental section
        supplemental_match = re.match(r"^## (Supplemental .+)$", line)
        # Detect summary/notes sections (end of articles)
        summary_match = re.match(r"^## (Summary Statistics|Notes on Citation)", line)

        if summary_match:
            # Save current section
            if current_section and current_articles:
                sections.append((current_section, current_articles))
            # Everything from here is postamble
            postamble_start = i
            break
        elif section_match or supplemental_match:
            in_preamble = False
            # Save previous section
            if current_section and current_articles:
                sections.append((current_section, current_articles))

            if section_match:
                current_section = f"## {section_match.group(1)}. {section_match.group(2)}"
            else:
                current_section = f"## {supplemental_match.group(1)}"
            current_articles = []
            i += 1
        elif in_preamble:
            preamble_lines.append(line)
            i += 1
        else:
            # Check for article start: ### Article N
            article_match = re.match(r"^### Article (\d+)", line)
            if article_match:
                # Collect all lines for this article until next ### or ## or EOF
                article_lines = [line]
                i += 1
                while i < len(lines):
                    if re.match(r"^###? ", lines[i]) or re.match(r"^## ", lines[i]):
                        break
                    article_lines.append(lines[i])
                    i += 1
                current_articles.append("\n".join(article_lines))
            else:
                i += 1

    # Save last section if no postamble found
    if current_section and current_articles:
        sections.append((current_section, current_articles))

    postamble = "\n".join(lines[postamble_start:]) if postamble_start else ""
    preamble = "\n".join(preamble_lines)

    return preamble, sections, postamble


def extract_year(article_text):
    """Extract publication year from an article entry."""
    # Look for (YYYY) pattern in the citation line
    match = re.search(r"\((\d{4})\)", article_text)
    if match:
        return int(match.group(1))
    return 0


def extract_title_and_author(article_text):
    """Extract the article title and first author last name from APA citation."""
    # The citation is in **bold** on the line after ### Article N
    lines = article_text.strip().split("\n")
    citation = ""
    for line in lines:
        if line.startswith("**") and not line.startswith("***"):
            citation = line
            break

    if not citation:
        return None, None, None

    # Extract first author last name
    author_match = re.match(r"\*\*(.+?)[,.]", citation)
    author_last = author_match.group(1).strip() if author_match else None

    # Extract year
    year_match = re.search(r"\((\d{4})\)", citation)
    year = year_match.group(1) if year_match else None

    # Extract title — it's after "(YYYY). " and before the next period+space
    # that precedes an italic journal name or publisher
    after_year = re.split(r"\(\d{4}\)\.\s*", citation, maxsplit=1)
    if len(after_year) < 2:
        return None, author_last, year

    rest = after_year[1]

    # For books: title is in *italics*
    book_match = re.match(r"\*(.+?)\*", rest)
    if book_match:
        title = book_match.group(1).rstrip(".")
        return title, author_last, year

    # For journal articles: title ends before the journal in *italics*
    # or before a period followed by a capital letter
    parts = re.split(r"\.\s+\*", rest, maxsplit=1)
    if len(parts) >= 1:
        title = parts[0].rstrip(".")
        # Also handle case where title ends before (Report number)
        title = re.split(r"\s+\(GAO|CRS|R\d|IF\d", title)[0].rstrip(".")
        return title, author_last, year

    return None, author_last, year


def add_link_to_citation(article_text, doi):
    """Add a DOI link to the article title in the citation."""
    if not doi:
        return article_text

    href = f"https://doi.org/{doi}"
    lines = article_text.split("\n")
    new_lines = []

    for line in lines:
        if line.startswith("**") and not line.startswith("***"):
            # Find the title and wrap it in a link
            # For books (title in italics): *Title*
            # For articles (title plain text): after (Year). Title. *Journal*

            after_year = re.split(r"(\(\d{4}\)\.\s*)", line, maxsplit=1)
            if len(after_year) >= 3:
                before = after_year[0] + after_year[1]
                rest = after_year[2]

                # Book: title in *italics*
                book_match = re.match(r"(\*)(.+?)(\*)", rest)
                if book_match:
                    linked = f"[*{book_match.group(2)}*]({href})"
                    rest = linked + rest[book_match.end():]
                    new_lines.append(before + rest)
                    continue

                # Journal article: title before "*Journal*"
                parts = re.split(r"(\.\s+\*)", rest, maxsplit=1)
                if len(parts) >= 2:
                    title = parts[0]
                    linked = f"[{title}]({href})"
                    rest = linked + parts[1] + (parts[2] if len(parts) > 2 else "")
                    new_lines.append(before + rest)
                    continue

            new_lines.append(line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


def main():
    text = SOURCE.read_text()
    preamble, sections, postamble = parse_articles(text)

    print(f"Parsed {len(sections)} sections")
    total_articles = sum(len(arts) for _, arts in sections)
    print(f"Total articles: {total_articles}")

    # Look up DOIs and add links
    doi_found = 0
    doi_cache = {}

    for sec_idx, (section_header, articles) in enumerate(sections):
        print(f"\n{section_header}")
        for art_idx, article in enumerate(articles):
            title, author_last, year = extract_title_and_author(article)
            if title:
                short = title[:60] + "..." if len(title) > 60 else title
                print(f"  Looking up: {short}", end="", flush=True)

                cache_key = (title[:50], year)
                if cache_key in doi_cache:
                    doi = doi_cache[cache_key]
                else:
                    doi = lookup_doi(title, author_last, year)
                    doi_cache[cache_key] = doi
                    time.sleep(0.15)  # Be polite to CrossRef

                if doi:
                    doi_found += 1
                    articles[art_idx] = add_link_to_citation(article, doi)
                    print(f" -> {doi}")
                else:
                    print(" -> no DOI found")
            else:
                print(f"  Could not parse title from article")

        # Sort articles within section: newest first
        articles.sort(key=lambda a: extract_year(a), reverse=True)

        # Renumber articles within section
        article_num_offset = sum(len(sections[i][1]) for i in range(sec_idx))
        for art_idx, article in enumerate(articles):
            global_num = article_num_offset + art_idx + 1
            articles[art_idx] = re.sub(
                r"### Article \d+",
                f"### Article {global_num}",
                article,
                count=1,
            )

    print(f"\nDOIs found: {doi_found}/{total_articles}")

    # Rebuild the markdown
    output_parts = [preamble.rstrip()]

    for section_header, articles in sections:
        output_parts.append("")
        output_parts.append(section_header)
        for article in articles:
            output_parts.append("")
            output_parts.append(article.rstrip())
        output_parts.append("")
        output_parts.append("---")

    if postamble:
        output_parts.append("")
        output_parts.append(postamble)

    result = "\n".join(output_parts)

    # Write back
    SOURCE.write_text(result)
    print(f"\nWrote updated file: {SOURCE}")


if __name__ == "__main__":
    main()
