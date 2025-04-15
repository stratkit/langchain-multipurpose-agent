from langchain.tools import Tool
import pandas as pd

df = pd.read_csv("data/sample.csv")

def list_columns(_: str) -> str:
    return f"Column headers: {', '.join(df.columns)}"

column_tool = Tool(
    name="List Column Headers",
    func=list_columns,
    description="Use this to get the column names from the dataset."
)