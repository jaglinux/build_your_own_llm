import os
from openai import OpenAI

import sys
#export OPENAI_LOG="debug"

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

messages_history=[
            # Prompt goes here
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ]

def add_message(input_message=None, response_message=None):
    if input_message:
        message =  {
                    "role": "user",
                    "content": input_message,
                }
    elif response_message:
        message =  {
                    "role": response_message.choices[0].message.role,
                    "content": response_message.choices[0].message.content,
                }  
    messages_history.append(message)
    
def chat(input_message):
    response = client.chat.completions.create(
        messages=messages_history,
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    return response
    
while True:
    print("messages history is ")
    print(f"{messages_history}")
    print("type e to quit")
    input_message = input("type the message ")
    if input_message == "e":
        sys.exit()
    add_message(input_message=input_message)
    response = chat(input_message)
    add_message(response_message=response)
    print(response.choices[0].message.content)

