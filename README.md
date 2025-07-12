# PubMed Fetcher

A Python command-line tool to fetch research papers from PubMed with at least one author affiliated with a pharmaceutical or biotech company, outputting results as a CSV file.

## Code Organization
- `pubmed_fetcher/client.py`: Handles PubMed API queries and data parsing.
- `pubmed_fetcher/filter.py`: Filters papers with non-academic authors.
- `pubmed_fetcher/output.py`: Writes results to CSV or console.
- `scripts/cli.py`: Command-line interface.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-github-repo-url>
   cd pubmed-fetcher