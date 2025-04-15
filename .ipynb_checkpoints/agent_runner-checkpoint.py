from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools.csv_tool import csv_tool

# Your LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Your tool definition
tool = Tool.from_function(
    func=csv_tool,  # <-- FIXED HERE
    name="Search CSV Data",
    description="Use this tool to search the uploaded CSV file for relevant information."
)

tools = [tool]

# Create the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    while True:
        query = input("🔍 Ask something (or type 'exit'): ")
        if query.lower() == "exit":
            break
        result = agent.invoke(query)
        print("💡 Result:", result)
