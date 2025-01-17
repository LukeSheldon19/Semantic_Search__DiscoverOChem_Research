import json
import sys
from config import CONFIG

def get_embedding_from_bedrock(query, model_id="amazon.titan-embed-text-v2:0"):
    """Get the embedding for the query using Bedrock."""
    body = json.dumps({"inputText": query})
    response = CONFIG.bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept='application/json',
        contentType='application/json'
    )
    response_body = json.loads(response['body'].read())
    return response_body.get('embedding')

def search_pinecone(embedding, top_k=5):
    """Search the Pinecone index with the given embedding."""
    return CONFIG.index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True
    )

def main():
    if len(sys.argv) > 1:
        search_query = sys.argv[1]
        embedding = get_embedding_from_bedrock(search_query)

        if embedding:
            results = search_pinecone(embedding)
            for match in results['matches']:
                print(f"Score: {match['score']}")
                print(f"Page Number: {match['metadata']['page_number']}")
                print(f"Sentence Text: {match['metadata']['sentence_text']}")
                print("----")
        else:
            print("Failed to retrieve embedding.")
    else:
        print("No search query provided.")

if __name__ == "__main__":
    main()
