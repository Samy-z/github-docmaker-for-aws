import os
import subprocess
import boto3
from urllib.parse import urlparse

def clone_repo(repo_url: str, target_dir: str) -> str:
    if repo_url.startswith("http"):
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
        return target_dir
    else:
        return os.path.abspath(repo_url)

def write_output(output_path: str, content: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def call_bedrock(prompt: str) -> str:
    # Default example, adapt to your preferred model & boto3 client setup
    client = boto3.client("bedrock-runtime")
    response = client.invoke_model(
        modelId="mistral.mixtral",
        body=prompt.encode("utf-8"),
        accept="application/json",
        contentType="text/plain"
    )
    return response["body"].read().decode("utf-8")

def upload_logs(repo_url: str, content: str, s3_uri: str):
    s3 = boto3.client("s3")
    parsed = urlparse(s3_uri)
    bucket = parsed.netloc
    key = os.path.join(parsed.path.lstrip("/"), "log.txt")

    s3.put_object(Bucket=bucket, Key=key, Body=content.encode("utf-8"))
