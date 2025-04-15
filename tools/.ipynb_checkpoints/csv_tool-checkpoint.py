from langchain.tools import Tool
import pandas as pd

# Load the dataset once
df = pd.read_csv("data/sample.csv")

def search_csv(query: str) -> str:
    """
    Searches the dataset for rows that match the query.
    """
    matches = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    if matches.empty:
        return "No matching records found."
    return matches.to_string(index=False)

# ✅ This is what you're importing in agent_runner.py
csv_tool = Tool(
    name="CSV Lookup Tool",
    func=search_csv,
    description="Use this tool to search a project dataset by keyword."
)