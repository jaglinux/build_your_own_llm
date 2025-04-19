# Agent  
Use https://github.com/marketplace/models/azure-openai/gpt-4-1/playground with Python wrapper.

# Create your own LLM / Transformer

Transformer blocks are
1. Create tokens from input text and assign/create token_ids to each token.
2. Assign vector embeddings for each token. (semantic meaning)
3. Add positional value to each vector embedding.
4. Add contextual meaning to each vector. This is done by an attention mechanism. Q, K, V matrix concept.
5. Feed forward network / activation function on each context rich vector.
6. Logits, convert the vectors into logits size and apply softmax to predict the next token.
   Each context-rich vector predicts the next token.
