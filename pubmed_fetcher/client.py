from typing import List, Dict
from Bio import Entrez
import logging
from datetime import datetime

class PubMedClient:
    """Client to fetch papers from PubMed API."""
    def __init__(self, email: str, api_key: str = None):
        Entrez.email = email
        Entrez.api_key = api_key

    def search_papers(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search PubMed for papers matching the query."""
        try:
            handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
            result = Entrez.read(handle)
            handle.close()
            ids = result["IdList"]
            if ids:
                handle = Entrez.efetch(db="pubmed", id=ids, retmode="xml")
                papers = Entrez.read(handle)
                handle.close()
                return self.parse_papers(papers)
            logging.info("No papers found for query.")
            return []
        except Exception as e:
            logging.error(f"PubMed API error: {e}")
            return []

    def parse_papers(self, papers: Dict) -> List[Dict]:
        """Parse PubMed XML into structured data."""
        results = []
        for article in papers["PubmedArticle"]:
            try:
                pubmed_id = article["MedlineCitation"]["PMID"]
                title = article["MedlineCitation"]["Article"]["ArticleTitle"]
                pub_date = self._get_pub_date(article)
                authors = article["MedlineCitation"]["Article"].get("AuthorList", [])
                author_data = self._parse_authors(authors)
                results.append({
                    "PubmedID": str(pubmed_id),
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": ", ".join(author_data["non_academic"]),
                    "Company Affiliation(s)": ", ".join(author_data["companies"]),
                    "Corresponding Author Email": author_data["email"]
                })
            except KeyError as e:
                logging.warning(f"Skipping article due to missing data: {e}")
        return results

    def _get_pub_date(self, article: Dict) -> str:
        """Extract publication date."""
        try:
            date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
            year = date.get("Year", "N/A")
            month = date.get("Month", "01")
            day = date.get("Day", "01")
            return f"{year}-{month}-{day}"
        except:
            return "N/A"

    def _parse_authors(self, authors: List) -> Dict:
        """Parse author names, affiliations, and emails."""
        non_academic = []
        companies = []
        email = "N/A"
        for author in authors:
            try:
                name = f"{author.get('LastName', '')} {author.get('ForeName', '')}".strip()
                # Safely access AffiliationInfo
                affiliation_info = author.get("AffiliationInfo", [])
                affiliation = affiliation_info[0].get("Affiliation", "") if affiliation_info else ""
                if self._is_company_affiliated(affiliation):
                    non_academic.append(name)
                    companies.append(affiliation)
                # Safely access email
                if affiliation_info and "Email" in affiliation_info[0]:
                    email = affiliation_info[0]["Email"]
            except (KeyError, IndexError):
                continue
        return {
            "non_academic": non_academic,
            "companies": companies,
            "email": email
        }

    def _is_company_affiliated(self, affiliation: str) -> bool:
        """Check if affiliation indicates a company."""
        if not affiliation:
            return False
        affiliation = affiliation.lower()
        company_keywords = ["pharma", "biotech", "inc", "pfizer", "novartis"]
        academic_keywords = ["university", "institute", "college"]
        has_company = any(keyword in affiliation for keyword in company_keywords)
        has_academic = any(keyword in affiliation for keyword in academic_keywords)
        return has_company and not has_academic