import argparse
import os, sys
from openai import OpenAI

endpoint = 'http://localhost:11434/v1'
model = "llama3:latest"

client = OpenAI(
    base_url=endpoint,
    api_key="ollama",
)

def call_llm(content):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": content + "\n Summarize Jag role in few lines from above group chat message",
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    print(response.choices[0].message)
    
def parse(file_loc):
    with open(file_loc) as f:
        content = f.readlines()
        print(len(content))
        for i in range(0, len(content), 100):
            print("---------index--------- ", i)
            #print("\n".join(content[i:i+100]))
            call_llm("\n".join(content[i:i+100]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_loc")
    args = parser.parse_args()
    if args.file_loc:
        parse(args.file_loc)