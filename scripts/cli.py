import argparse
import logging
from pubmed_fetcher.client import PubMedClient
from pubmed_fetcher.filter import AuthorFilter
from pubmed_fetcher.output import OutputWriter

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")
    parser.add_argument("query", help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("-f", "--file", help="Output CSV file")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        client = PubMedClient(email="varshinid.tech@gmail.com")
        papers = client.search_papers(args.query)
        filter = AuthorFilter()
        filtered_papers = filter.filter_papers(papers)
        writer = OutputWriter()
        writer.write_results(filtered_papers, args.file)
    except Exception as e:
        logging.error(f"Program failed: {e}")
        raise

if __name__ == "__main__":
    main()