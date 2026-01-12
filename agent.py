# pip install -qU langchain 
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gpt-oss:20B")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
answer = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)


answer