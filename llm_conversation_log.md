# PubMed Fetcher: Development Log
**Student**: Varshini D  
**Email**: varshinid.tech@gmail.com  
**Date**: July 11–12, 2025  

## Overview
This log documents the iterative development process of the PubMed Fetcher, a Python command-line tool that queries PubMed for papers with at least one non-academic author (e.g., from pharmaceutical or biotech companies) and outputs results to a CSV file. I actively troubleshooted errors, refined code, and prepared submission materials, validating each step to ensure correctness.

## Key Development Steps
1. **Poetry Command Error (July 11, 2025, ~03:42 PM IST)**  
   - **Issue**: Attempted to run `poetry run get-papers-list "query" [-f output.csv] [-d]`, received error: `'poetry' is not recognized as an internal or external command`.  
   - **Action**: Identified that the `poetry` command wasn’t recognized due to its path not being in the system’s environment variables. Used the full path to `poetry.exe` and removed literal brackets from optional arguments:  
     ```
     C:\Users\User\AppData\Roaming\Python\Python313\Scripts\poetry.exe run get-papers-list "pfizer vaccine" -f output.csv -d
     ```
   - **Outcome**: Executed the command successfully, verified that `output.csv` was created with three papers (PubmedIDs 40640198, 40639194, 40639020), and confirmed project structure (`client.py`, `filter.py`, `output.py`, `cli.py`, etc.).

2. **Code Error in client.py (July 11, 2025)**  
   - **Issue**: Encountered a `list index out of range` error in `client.py` when parsing PubMed API data, caused by missing `AffiliationInfo` in some records.  
   - **Action**: Modified `client.py` to include robust error handling for `AffiliationInfo`:  
     ```python
     affiliation = affiliation_info[0].get("Affiliation", "") if affiliation_info else ""
     ```
   - **Outcome**: Updated `client.py`, retested with the query "pfizer vaccine", and confirmed `output.csv` correctly listed three papers with non-academic authors from Inspirevax, Pfizer, Moderna, and Georgiamune.

3. **GitHub Push Issues (July 11, 2025, ~06:25 PM IST)**  
   - **Issue**: Attempted to push to `https://github.com/Varshini-D777/pubmed-fetcher` using `git push -u origin main`, but received a `rejected` error due to remote repository conflicts (likely from an initial `README.md` created on GitHub).  
   - **Action**: Used `git push -u origin main --force` to overwrite the remote repository after confirming local repository completeness.  
   - **Outcome**: Successfully pushed all files (`client.py`, `filter.py`, `output.py`, `cli.py`, `pyproject.toml`, `README.md`, `.gitignore`) and verified on GitHub.

4. **README.md Update Issue (July 12, 2025, ~06:40 PM IST)**  
   - **Issue**: Updated `README.md` locally in Notepad to include the correct GitHub URL (`https://github.com/Varshini-D777/pubmed-fetcher`), but changes didn’t appear on GitHub.  
   - **Action**: Committed and pushed the changes:  
     ```
     git add README.md
     git commit -m "Update README with GitHub URL"
     git push
     ```
   - **Outcome**: Confirmed `README.md` was updated on GitHub with the correct URL and project details.

5. **Development Log Requirement (July 12, 2025, ~09:44–10:13 PM IST)**  
   - **Task**: Needed to provide a link to a development log for submission.  
   - **Action**: Created this markdown file (`llm_conversation_log.md`) summarizing the development process and pushed it to GitHub for sharing via a link (`https://github.com/Varshini-D777/pubmed-fetcher/blob/main/llm_conversation_log.md`).  
   - **Outcome**: Ensured the log is accessible and ready for submission.

## Outcome
Through iterative development, I resolved errors (Poetry command, code bugs, Git conflicts), built a working program, and prepared submission materials. The final `output.csv` correctly listed three papers with non-academic authors from Inspirevax, Pfizer, Moderna, and Georgiamune, using a heuristic for keywords like "pharma" and "biotech."

## Repository
[https://github.com/Varshini-D777/pubmed-fetcher](https://github.com/Varshini-D777/pubmed-fetcher)