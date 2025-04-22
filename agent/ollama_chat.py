import argparse
import os, sys
from openai import OpenAI

endpoint = 'http://localhost:11434/v1'
model = "llama3:latest"

client = OpenAI(
    base_url=endpoint,
    api_key="ollama",
)

def call_llm(content, post_content=None):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": content + post_content,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    print(response.choices[0].message)
    return response.choices[0].message.content
    
def parse(file_loc, person_name):
    chat_summary = []
    with open(file_loc) as f:
        content = f.readlines()
        print(len(content))
        for i in range(0, len(content), 100):
            print("---------index--------- ", i)
            #print("\n".join(content[i:i+100]))
            summary = call_llm("\n".join(content[i:i+100]), f"\n Summarize {person_name} role in few lines from above group chat message.")
            chat_summary.append(summary)
            # temporary break after 300 lines of chat
            if i == 300:
                break
    print("-----FINAL Summary-----------")
    print(chat_summary)
    call_llm("\n".join(chat_summary), f"\n Above content are list of summary of {person_name}'s message from a group chat. Summarize all of them together and provide final summary of {person_name}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_loc")
    parser.add_argument("person_name")
    args = parser.parse_args()
    if args.file_loc:
        parse(args.file_loc, args.person_name)