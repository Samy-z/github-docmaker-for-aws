import os
import subprocess
import boto3
from urllib.parse import urlparse

def clone_repo(repo_url: str, target_base_dir: str ='./') -> str:
    repo_name = os.path.splitext(os.path.basename(urlparse(repo_url).path))[0]
    target_dir = os.path.join(target_base_dir, repo_name)

    if repo_url.startswith("http"):
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
        return target_dir
    else:
        return os.path.abspath(repo_url)

        
def write_output(output_path: str, content: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def call_bedrock(request) -> str:
    # Default example, adapt to your preferred model & boto3 client setup
    client = boto3.client("bedrock-runtime")
    response = client.invoke_model(
        modelId="mistral.mistral-large-2402-v1:0",
        body=request
    )
    return response["body"].read().decode("utf-8")

def upload_logs(repo_url: str, content: str, s3_uri: str):
    s3 = boto3.client("s3")
    parsed = urlparse(s3_uri)
    bucket = parsed.netloc
    key = os.path.join(parsed.path.lstrip("/"), "log.txt")

    s3.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
