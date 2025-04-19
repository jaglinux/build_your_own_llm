import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

input_message = input("type the message ")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": input_message,
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message)
print(response.choices[0].message.content)

