import pandas as pd

class CSVSearchTool:
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)

    def search(self, query: str) -> str:
        # Basic keyword search in all text columns
        mask = self.df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
        results = self.df[mask]
        return results.to_string(index=False) if not results.empty else "No matches found."
