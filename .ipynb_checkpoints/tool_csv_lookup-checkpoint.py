# tool_csv_lookup.py
import pandas as pd
from langchain.tools import tool

# Load the dataset at module level
df = pd.read_csv("data/sample.csv")

@tool
def search_csv(keyword: str) -> str:
    """Searches for a keyword in the sample CSV and returns matching rows."""
    matches = df[df.apply(lambda row: keyword.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    if matches.empty:
        return f"No matches found for '{keyword}'."
    return matches.head(5).to_string(index=False)
