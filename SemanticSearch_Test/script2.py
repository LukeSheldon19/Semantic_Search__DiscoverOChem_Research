import sys
import pandas as pd
import numpy as np
import re
from pinecone import Pinecone, ServerlessSpec

import torch
from transformers import AutoTokenizer, AutoModel

import torch.nn.functional as F

model_ckpt = 'sentence-transformers/all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)

index_name = "semanticsearchllmbased"
pc = Pinecone(api_key="")

index = pc.Index(index_name)

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output.last_hidden_state
    input_mask_expanded = (
        attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    )
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
        input_mask_expanded.sum(1), min=1e-9
    )

if len(sys.argv) > 1:

    search_query = sys.argv[1]

    cleaned_query = re.sub(r'[^\w\s]', '', search_query)
    encoded_query = tokenizer([cleaned_query], padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        query_output = model(**encoded_query)

    query_embedding = mean_pooling(query_output, encoded_query["attention_mask"])
    query_embedding = F.normalize(query_embedding, p=2, dim=1)
    np_query_embedding = query_embedding.detach().numpy()

    FINAL_query_embedding = np_query_embedding.flatten().tolist()

    top_k = 5

    response = index.query(
        vector=FINAL_query_embedding,
        top_k=top_k,
        include_metadata=True 
    )

    for match in response['matches']:
        print(f"Score: {match['score']}")
        print(f"Page Number: {match['metadata']['page_number']}")
        print(f"Sentence Text: {match['metadata']['sentence_text']}")
        print("----")
else:
    print("No search query provided.")



