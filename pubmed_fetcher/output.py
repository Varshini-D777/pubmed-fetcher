from typing import List, Dict
import pandas as pd
import logging

class OutputWriter:
    """Write paper data to CSV or console."""
    def write_results(self, papers: List[Dict], filename: str = None):
        """Write results to file or console."""
        if not papers:
            logging.info("No results to write.")
            return
        df = pd.DataFrame(papers, columns=[
            "PubmedID", "Title", "Publication Date",
            "Non-academic Author(s)", "Company Affiliation(s)",
            "Corresponding Author Email"
        ])
        if filename:
            try:
                df.to_csv(filename, index=False)
                logging.info(f"Results saved to {filename}")
            except Exception as e:
                logging.error(f"Error saving CSV: {e}")
        else:
            print(df.to_string(index=False))