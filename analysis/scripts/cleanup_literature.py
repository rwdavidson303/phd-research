#!/usr/bin/env python3
"""Clean up the literature page after DOI linking and reordering."""

import re
from pathlib import Path

SOURCE = Path.home() / "phd-research" / "research" / "articles" / "top_100_articles.md"

text = SOURCE.read_text()
lines = text.split("\n")

# Pass 1: Remove stray --- dividers within sections
# A --- is "stray" if it appears between two ### Article blocks
# (i.e., not immediately before a ## section header)
cleaned = []
i = 0
while i < len(lines):
    if lines[i].strip() == "---":
        # Look ahead: is the next non-empty line a ## section header or end of file?
        j = i + 1
        while j < len(lines) and lines[j].strip() == "":
            j += 1
        if j < len(lines) and (lines[j].startswith("## ") or lines[j].startswith("# ") or lines[j].startswith("| ") or lines[j].startswith("- ") or lines[j].startswith("*This list")):
            # This is a legitimate section divider
            cleaned.append(lines[i])
        else:
            # Stray divider within a section — skip it
            pass
    else:
        cleaned.append(lines[i])
    i += 1

text = "\n".join(cleaned)

# Pass 2: Fix known bad DOI matches
# Moore 1995 — wrong DOI (matched a 2025 paper)
text = text.replace(
    "[*Creating public value: Strategic management in government*](https://doi.org/10.37497/jsim.v12.id179.2025)",
    "*Creating public value: Strategic management in government*"
)

# Stoker 2006 — check if it got no link, add it manually
# DOI: 10.1177/0275074005311220
if "Public value management: A new narrative for networked governance" in text and "doi.org" not in text.split("Public value management: A new narrative for networked governance")[0].split("\n")[-1]:
    text = text.replace(
        "Public value management: A new narrative for networked governance?",
        "[Public value management: A new narrative for networked governance?](https://doi.org/10.1177/0275074005311220)"
    )

# Patrucco 2023 — parentheses in title caused parser failure
# DOI: 10.1111/puar.13575
if "How can procurement create (sustainable) public value" in text:
    text = text.replace(
        "How can procurement create (sustainable) public value under the Bipartisan Infrastructure Deal?",
        "[How can procurement create (sustainable) public value under the Bipartisan Infrastructure Deal?](https://doi.org/10.1111/puar.13575)"
    )

# Bulow & Klemperer 1996 — missed DOI
# DOI: 10.1257/aer.86.1.180
if "Auctions versus negotiations. *American Economic Review*" in text and "doi.org" not in text.split("Auctions versus negotiations. *American Economic Review*")[0].split("\n")[-1]:
    text = text.replace(
        "Auctions versus negotiations. *American Economic Review*",
        "[Auctions versus negotiations](https://doi.org/10.1257/aer.86.1.180). *American Economic Review*"
    )

# Kelman 1990 — no DOI expected (book, AEI Press)
# Gordon 2006 — Public Contract Law Journal, no DOI typical
# GAO reports — no DOI expected

# Benington & Moore 2011 book — DOI: 10.1057/9780230364311
if "Public value: Theory and practice*. London: Palgrave" in text and "doi.org" not in text.split("Public value: Theory and practice")[0].split("\n")[-1]:
    text = text.replace(
        "*Public value: Theory and practice*. London: Palgrave Macmillan.**",
        "[*Public value: Theory and practice*](https://doi.org/10.1057/9780230364311). London: Palgrave Macmillan.**"
    )

# Angrist & Pischke 2009 — DOI: 10.1515/9781400829828
if "Mostly harmless econometrics" in text and "doi.org" not in text.split("Mostly harmless econometrics")[0].split("\n")[-1]:
    text = text.replace(
        "*Mostly harmless econometrics: An empiricist's companion*",
        "[*Mostly harmless econometrics: An empiricist's companion*](https://doi.org/10.1515/9781400829828)"
    )

# Gordon 2013 — Bid protests: The costs are real
# No standard DOI, but SSRN has it
if "Bid protests: The costs are real, but the benefits outweigh them" in text and "doi.org" not in text.split("Bid protests: The costs are real")[0].split("\n")[-1]:
    text = text.replace(
        "Bid protests: The costs are real, but the benefits outweigh them. *Public Contract Law Journal*",
        "[Bid protests: The costs are real, but the benefits outweigh them](https://doi.org/10.2139/ssrn.2178169). *Public Contract Law Journal*"
    )

# Williamson 1979 — the DOI found (10.1093/oso/...) is for a reprint, use canonical
text = text.replace(
    "https://doi.org/10.1093/oso/9780198774358.003.0007",
    "https://doi.org/10.1086/466942"
)

# Williamson 1985 book — DOI found was for a chapter, not the book
text = text.replace(
    "[*The economic institutions of capitalism: Firms, markets, relational contracting*](https://doi.org/10.1007/978-3-8349-9320-5_6)",
    "*The economic institutions of capitalism: Firms, markets, relational contracting*"
)

# Hart, Shleifer, Vishny 1997 — DOI was NBER working paper, use QJE DOI
text = text.replace(
    "https://doi.org/10.3386/w5744",
    "https://doi.org/10.1162/003355397555325"
)

# Bajari & Tadelis 2001 — DOI was SSRN, use RAND DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.193121",
    "https://doi.org/10.2307/2696361"
)

# Decarolis 2014 — DOI was SSRN, use AEJ DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.3475636",
    "https://doi.org/10.1257/app.6.1.108"
)

# Decarolis 2018 comparing auctions — was SSRN, use IER DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.3533352",
    "https://doi.org/10.1111/iere.12276"
)

# Decarolis 2020/2021 bureaucratic competence — was NBER, use JLEO DOI
text = text.replace(
    "https://doi.org/10.3386/w24201",
    "https://doi.org/10.1093/jleo/ewz004"
)

# Goodman-Bacon 2021 — was NBER, use JoE DOI
text = text.replace(
    "https://doi.org/10.3386/w25018",
    "https://doi.org/10.1016/j.jeconom.2021.03.014"
)

# Imbens & Wooldridge 2009 — was CeMMAP, use JEL DOI
text = text.replace(
    "https://doi.org/10.1920/wp.cem.2008.2408",
    "https://doi.org/10.1257/jel.47.1.5"
)

# Creswell 2018 — DOI was for a different chapter, remove it
text = text.replace(
    "[*Designing and conducting mixed methods research*](https://doi.org/10.1037/13742-003)",
    "*Designing and conducting mixed methods research*"
)

# Decarolis 2009 working paper — was SSRN, that's fine
text = text.replace(
    "https://doi.org/10.2139/ssrn.1523216",
    "https://doi.org/10.2139/ssrn.1523216"
)

# Calvo et al 2019 — was SSRN, use Management Science DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.2876840",
    "https://doi.org/10.1287/mnsc.2018.3216"
)

# Ganuza 2007 — was SSRN, use JIE DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.848487",
    "https://doi.org/10.1111/j.1467-6451.2007.00323.x"
)

# Laffont & Tirole 1993 book — DOI was for a book review, remove
text = text.replace(
    "[*A theory of incentives in procurement and regulation*](https://doi.org/10.2307/2235329)",
    "*A theory of incentives in procurement and regulation*"
)

# Spagnolo 2012 — was SSRN, use IJIO DOI
text = text.replace(
    "https://doi.org/10.2139/ssrn.1988818",
    "https://doi.org/10.1016/j.ijindorg.2012.01.007"
)

# Schooner 2002 — was SSRN, use that
text = text.replace(
    "https://doi.org/10.2139/ssrn.304620",
    "https://doi.org/10.2139/ssrn.304620"
)

# Yukins 2012 — was SSRN wrong match, remove
text = text.replace(
    "[Feature comment: Bid protests in the U.S. procurement system: Assessing proposed reforms -- Part I](https://doi.org/10.2139/ssrn.5417195)",
    "Feature comment: Bid protests in the U.S. procurement system: Assessing proposed reforms -- Part I"
)

# ADB 2018 — wrong DOI match, remove
text = text.replace(
    "[*Guidance note on procurement: Value for money*](https://doi.org/10.22617/tim189667-3)",
    "*Guidance note on procurement: Value for money*"
)

# Johansson & Lahtinen 2015 — wrong DOI (matched IJISPM paper), remove
text = text.replace(
    "[Getting the balance right between functional and non-functional requirements: The case of requirement specification in IT procurement](https://doi.org/10.12821/ijispm010101)",
    "Getting the balance right between functional and non-functional requirements: The case of requirement specification in IT procurement"
)

# Rosenbaum & Rubin 1983 — DOI was for a Cambridge textbook chapter, use Biometrika DOI
text = text.replace(
    "https://doi.org/10.1017/cbo9780511810725.016",
    "https://doi.org/10.1093/biomet/70.1.41"
)

# Pass 3: Renumber all articles sequentially
article_num = 0
new_lines = []
for line in text.split("\n"):
    match = re.match(r"^### Article \d+", line)
    if match:
        article_num += 1
        new_lines.append(f"### Article {article_num}")
    else:
        new_lines.append(line)

text = "\n".join(new_lines)

SOURCE.write_text(text)
print(f"Cleanup complete. {article_num} articles total.")
