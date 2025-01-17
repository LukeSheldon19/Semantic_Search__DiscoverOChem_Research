import boto3
from pinecone import Pinecone
import json

class Config:
    def __init__(self):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='us-east-2'
        )

        self.pc = Pinecone(api_key="")
        self.index = self.pc.Index("semanticsearchaws")

CONFIG = Config()
