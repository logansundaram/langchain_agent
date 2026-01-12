# pip install -qU langchain 
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.messages import SystemMessage, HumanMessage
from langchain.tools import tool

llm = ChatOllama(model="gpt-oss:20B")

@tool
def get_weather(city: str) -> str:
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

messages = []

while True:
    query = input("you: ")
    messages.append(HumanMessage(content=query))

    result = agent.invoke({"messages": messages})

    messages = result["messages"]

    for m in messages:
        m.pretty_print()