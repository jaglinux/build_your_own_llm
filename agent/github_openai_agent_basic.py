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

@function_tool
async def add(a, b):
    '''
    Function to add 2 numbers, provide 2 inputs and returns one output
    Args:
        a: first number
        b: second number
    '''
    print("input to function ", a, b)
    return a+b

agent = Agent(name="basic_agent", tools=[add],
              model=OpenAIChatCompletionsModel(openai_client=client, model=model))

async def main():
    response = await Runner.run(agent, input="what is 200 + 600 +400 ", max_turns=5)
    print(response.raw_responses)
    #print(response.raw_responses)
    # print("------START LOG---------")
    # for i in response.raw_responses:
    #     print(i)
    #     print("------------------------")
    # print("------END LOG---------")

if __name__ == "__main__":
    asyncio.run(main())