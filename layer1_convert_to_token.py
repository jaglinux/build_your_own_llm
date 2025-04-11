import re

class tokenizer():
    def __init__(self):
        self.tokens = []
        self.token_ids = {}
        self.raw_tokens = []
        self.raw_tokens_ids = []
    
    def print_tokens(self):
        print(self.tokens, len(self.tokens))

    def print_token_ids(self):
        print(self.token_ids, len(self.token_ids))

    def print_raw_tokens(self):
        print(self.raw_tokens, len(self.raw_tokens))

    def print_raw_token_ids(self):
        print(self.raw_tokens_ids, len(self.raw_tokens_ids))

    def create_tokens(self):
        with open("The_Verdict.txt") as f:
            buffer = f.read()
            buffer = re.split(r'([,.:;?_!"()\']|--|\s)', buffer)
            buffer = [i.strip() for i in buffer if i.strip()]
            self.raw_tokens = buffer[:]
            buffer = sorted(set(buffer))
            self.tokens = buffer
    
    def create_token_ids(self):
        if len(self.tokens) == 0:
            self.create_tokens()
        for i,j in enumerate(self.tokens):
            self.token_ids[j] = i

    def covert_raw_tokens_to_tokenIds(self):
        for i in self.raw_tokens:
            self.raw_tokens_ids.append(self.token_ids[i])

t = tokenizer()
t.create_tokens()
t.print_tokens()
t.create_token_ids()
t.print_token_ids()
t.print_raw_tokens()
t.covert_raw_tokens_to_tokenIds()
t.print_raw_token_ids()