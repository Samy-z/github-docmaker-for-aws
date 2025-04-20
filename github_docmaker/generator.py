import os
import tempfile
from github_docmaker.utils import clone_repo, call_bedrock, write_output, upload_logs
from github_docmaker.parser import parse_files

def generate_docs(repo_url: str, output_path: str, log_s3: str | None, dry_run: bool, only_code: bool):
    # 1. Clone repo
    tmpdir = tempfile.mkdtemp()
    repo_path = clone_repo(repo_url, tmpdir)

    # 2. Parse files
    repo_tree = generate_repo_tree(repo_path)
    code_chunks = parse_files(repo_path, only_code=only_code)

    # 3. Call Bedrock model
    prompt = f"""Generate README.md documentation for this repository.

    Include repo structure:
    {repo_tree}

    Then analyze the following source files:
    {code_chunks}
    """
    
    
    docs = call_bedrock(prompt)

    # 4. Output
    if dry_run:
        print(docs)
    else:
        write_output(output_path, docs)

    # 5. Optionally upload logs
    if log_s3:
        upload_logs(repo_url, docs, log_s3)