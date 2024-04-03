import boto3
import json
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv(override=True)

session = boto3.Session(profile_name=os.getenv('AWS_PROFILE'))
client = session.client(
    'bedrock-runtime',
    region_name='us-east-1',
    )

prompt = '''
Human: AWSについて教えて
Assistant:
'''

body = {
    'prompt': prompt,
    'max_tokens_to_sample': 300,
}

response = client.invoke_model(
    modelId="anthropic.claude-v2",
    body=json.dumps(body)
)

body = response['body'].readlines()

completion = json.loads(body[0].decode('utf-8'))['completion']

print(completion)
