import boto3
import json
import sys
from pinecone import Pinecone, ServerlessSpec

bedrock = boto3.client(
    service_name='bedrock-runtime',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-2'
)

model_id = 'amazon.titan-embed-text-v2:0'
accept = 'application/json'
content_type = 'application/json'

pc = Pinecone(api_key="")

index_name = "semanticsearchaws"

index = pc.Index(index_name)

if len(sys.argv) > 1:

    search_query = sys.argv[1]

    body = json.dumps({
    "inputText": search_query,
    })

    response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept=accept,
    contentType=content_type
    )

    response_body = json.loads(response['body'].read())
    embedding = response_body.get('embedding')

    top_k = 5

    response = index.query(
        vector=embedding,
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

