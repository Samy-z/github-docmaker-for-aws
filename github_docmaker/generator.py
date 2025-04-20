import os
import tempfile
from github_docmaker.utils import clone_repo, call_bedrock, write_output, upload_logs
from github_docmaker.parser import parse_files, generate_repo_tree
import json

def generate_docs(repo_url: str, output_path: str, log_s3: str | None, dry_run: bool):
    # 1. Clone repo
    tmpdir = tempfile.mkdtemp()
    repo_path = clone_repo(repo_url, tmpdir)

    # 2. Parse files
    repo_tree = generate_repo_tree(repo_path)
    code_chunks = parse_files(repo_path)

    # 3. Call Bedrock model
    prompt = f"""Your job is to Generate README.md documentation files for GitHub repository.
    You are being given the code in chuncks as well as the repository file tree to understand what is each file about in details.     
    Try to be as explainative as you can while being concise, and go over these non-exaustive list of points:
    0 - Introduction
    1 - list all features and tackle what can be customized
    2 - Prerequisites
    3 - Installation (if the setup file doesn't contain a package name then most likely the method to install is to clone the repo and run the setup file, in case you need it here is the repo link: {repo_url})
    4 - What are the Dependencies for running the project
    5 - Usage
    6 - Customization
    7 - Explain the code logic and globally what part of the logic is defined where
    9 - Potential disclaimers

    Always Include repo structure (the tree) at the end of the output :
    {repo_tree}
    Then at the end of the output, write a gentle reminder to the user that with generative AI halucinations can happen.

    Include the repository structure as a code block **within the appropriate section**, not at the beginning of the file. 
    Do not start the README with the raw file tree. Focus on clarity, helpful descriptions, and avoid redundancy.
    
    Here are the code chuncks for you to analyze source files:
    {code_chunks}
    """
    # Format the request payload using the model's native structure.
    native_request = {
        "prompt": prompt,
        "max_tokens": 4096,
        "temperature": 0.8,
    }
    
    # Convert the native request to JSON.
    request = json.dumps(native_request)
    response = call_bedrock(request)

    # Extract text from response (JSON)
    parsed = json.loads(response)
    readme = parsed["outputs"][0]["text"]

    # 4. Output
    if dry_run:
        print(readme)
    else:
        write_output(output_path, readme)

    # 5. Optionally upload logs
    if log_s3:
        upload_logs(repo_url, docs, log_s3)
