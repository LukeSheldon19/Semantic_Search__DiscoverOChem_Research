import sys
from pinecone import Pinecone
import numpy as np

vocab_dict = {}
with open('vocab.txt', "r", encoding="utf-8") as f:
    for line in f:
        word, index = line.strip().split()
        vocab_dict[word] = int(index)

def generate_frequency_vector(words, vocab_dict):
    frequency_vector = np.zeros(len(vocab_dict))
    
    for word in words:
        if word in vocab_dict:  
            index = vocab_dict[word]
            frequency_vector[index] += 1 
    
    return frequency_vector


pc = Pinecone(api_key="")

index_name = "semanticsearch"

index = pc.Index(index_name)

if len(sys.argv) > 1:

    search_query = sys.argv[1]
    input = [w.lower() for w in search_query.split(" ")]    
    input_embedding = generate_frequency_vector(input, vocab_dict)
    clean_query_embedding = [float(e) for e in input_embedding]

    top_k = 5

    response = index.query(
        vector=clean_query_embedding,
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