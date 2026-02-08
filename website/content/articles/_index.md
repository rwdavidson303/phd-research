---
title: "Articles Feed"
description: "Daily discoveries of new relevant scholarly articles"
weight: 6
---

## Daily Article Feed

New scholarly articles relevant to the dissertation are discovered automatically each day through searches of OpenAlex and Semantic Scholar databases.

### How It Works

An automated script runs daily at 7:00 AM, searching across 20+ research queries covering all dissertation topic areas. New articles are stored in a local SQLite database and daily digests are generated.

### Search Topics

- Best value source selection in government procurement
- LPTA outcomes and performance
- Public value theory and procurement
- Transaction cost economics in contracting
- Bid protests and procurement delay
- Solicitation quality and requirements
- Oversight and red tape in procurement
- Strategic underbidding and renegotiation
- Incumbency advantage and competition
- Procurement reform and modernization

### Commands

```bash
# Run a search manually
python automation/daily_article_search.py

# View database report
python automation/daily_article_search.py --report

# Export all articles to CSV
python automation/daily_article_search.py --export
```

### Recent Digests

*Daily digests will appear here as the automated search runs.*
