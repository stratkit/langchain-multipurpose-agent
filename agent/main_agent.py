from langchain.agents import initialize_agent
# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from tools.csv_tool import csv_tool  # ✅ this is the Tool instance
from to

tools = [csv_tool]

llm = OpenAI(temperature=0)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)