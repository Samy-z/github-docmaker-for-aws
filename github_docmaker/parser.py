import os
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

# File extensions that are to be considered code
CODE_EXTENSIONS = [".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs", ".rb", ".go", ".rs", ".php", ".html", ".css"]
# Markdown and general text files
TEXT_EXTENSIONS = [".md", ".txt"]

def should_include(file: str) -> bool:
    return any(file.endswith(ext) for ext in (CODE_EXTENSIONS))

def load_text_files(repo_path: str) -> List[str]:
    collected = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if should_include(file):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        header = f"# File: {os.path.relpath(full_path, repo_path)}\n"
                        collected.append(header + content)
                except Exception as e:
                    print(f"Warning: skipping {full_path} due to error: {e}")
    return collected

def parse_files(repo_path: str) -> str:
    files = load_text_files(repo_path)
    full_text = "\n\n".join(files)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_text(full_text)

    return "\n\n".join(chunks)
    
def generate_repo_tree(path: str) -> str:
    tree = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = "  " * level
        tree += f"{indent}{os.path.basename(root)}/\n"
        subindent = "  " * (level + 1)
        for f in files:
            tree += f"{subindent}{f}\n"
    return tree