from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from tools.csv_tool import CSVSearchTool

# Initialize your tool
csv_tool = CSVSearchTool("data/sample.csv")

tools = [
    Tool(
        name="CSV Search",
        func=csv_tool.search,
        description="Useful for searching internal data based on a keyword or phrase"
    )
]

# Set up LLM
llm = OpenAI(temperature=0)

# Build agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
