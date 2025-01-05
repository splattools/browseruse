from os import environ
from browser_use import Agent
import asyncio
from langchain_openai.chat_models import AzureChatOpenAI
azure = AzureChatOpenAI(
    openai_api_version="2024-05-01-preview",
    azure_endpoint=environ.get("AZURE_OPENAI_ENDPOINT"),
    azure_deployment="gpt-4o",
    model="gpt-4o",
    validate_base_url=False,
    api_key=environ.get("AZURE_OPENAI_API_KEY"),
)

async def main():
    input_text = input("Enter your order: ")
    agent = Agent(
        task=input_text,
        llm=azure,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())