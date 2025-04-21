import os
from openai import OpenAI

endpoint = 'http://localhost:11434/v1'
model = "llama3:latest"

client = OpenAI(
    base_url=endpoint,
    api_key="ollama",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message)
print(response.choices[0].message.content)

