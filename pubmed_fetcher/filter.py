from typing import List, Dict

class AuthorFilter:
    """Filter papers based on author affiliations."""
    def filter_papers(self, papers: List[Dict]) -> List[Dict]:
        """Return papers with at least one non-academic author."""
        return [paper for paper in papers if paper["Non-academic Author(s)"]]