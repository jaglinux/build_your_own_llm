import os, asyncio
from openai import AsyncOpenAI
from agents import (Agent, OpenAIChatCompletionsModel, Runner, 
function_tool, enable_verbose_stdout_logging)

#enable_verbose_stdout_logging()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4o"

client = AsyncOpenAI(
    base_url=endpoint,
    api_key=token,
)

agent = Agent(name="basic_agent", model=OpenAIChatCompletionsModel(openai_client=client, model=model))

async def main():
    response = await Runner.run(agent, input="what is ac milan")
    print(response.final_output)

if __name__ == "__main__":
    asyncio.run(main())