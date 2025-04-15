from agent.main_agent import agent

if __name__ == "__main__":
    while True:
        user_input = input("Ask your multi-purpose agent: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        response = agent.run(user_input)
        print(response)
