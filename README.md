# GitHub DocMaker

GitHub DocMaker is a command-line interface (CLI) tool designed to generate README.md documentation from GitHub repositories using the Mistral Large model via AWS. This tool is intended to help developers quickly create and maintain high-quality documentation for their projects.

## Features

- Generates a tree of the files in the repository.
- Pull and parses code files from a GitHub repository, to split them into chuncks for model consumption.
- Generates documentation in Markdown format at a specified location on current device or S3 Bucket.
- Possibility to uploads logs to an S3 bucket for auditing and debugging purposes.
- Supports dry-run mode for testing and debugging.

## Prerequisites

- Python 3.9 or higher
- A GitHub account with access to the desired repository
- An AWS account with access to the Mistral AI model (access to self-grant on Bedrock) and S3 (if using log uploads)

## Dependencies

This project requires the following dependencies:

- click
- boto3
- langchain

These dependencies can be installed using pip by running:

```bash
pip install -r requirements.txt
```

## Installation

To install GitHub DocMaker, you can clone the repository and install it using pip:

```bash
git clone https://github.com/Samy-z/github-docmaker-for-aws.git
cd github-docmaker-for-aws
pip install .
```

## Usage

To use GitHub DocMaker, run the following command:

```bash
gm-doc generate --repo <REPO_URL> [--output <OUTPUT_PATH>] [--log-s3 <S3_URI>] [--dry-run]
```

- `--repo`: The URL or path to the GitHub repository.
- `--output`: The output file path (default: `README.md`).
- `--log-s3`: The S3 URI for logs (e.g., `s3://bucket/`).
- `--dry-run`: Prints the output to the console without writing to a file.

## Customization

You can customize the behavior of GitHub DocMaker by using the available command-line options. For example, you can choose to parse only code files or upload logs to a specific S3 bucket.

## Code Logic

The main logic of the tool is divided into several components:

1. **CLI**: Defined in `github_docmaker/cli.py`, it provides the command-line interface for the user.
2. **Generator**: Defined in `github_docmaker/generator.py`, it handles the overall process of generating documentation, including cloning the repository, parsing files, calling the Mistral AI model, and writing the output.
3. **Parser**: Defined in `github_docmaker/parser.py`, it parses the files in the repository and prepares them for processing by the Mistral AI model.
4. **Utils**: Defined in `github_docmaker/utils.py`, it contains utility functions for cloning repositories, writing output, and interacting with AWS services.

## Disclaimers

- This tool relies on the Mistral AI model provided by AWS. The quality of the generated documentation depends on the performance of the AI model.
- GitHub DocMaker is not responsible for any potential misuse or unauthorized access to repositories or AWS services.

## Repository Structure

```
github-docmaker-for-aws/
├── LICENSE
├── requirements.txt
├── setup.py
├── .git/
│   ├── description
│   ├── HEAD
│   ├── config
│   ├── packed-refs
│   ├── index
│   ├── branches/
│   ├── hooks/
│   ├── info/
│   ├── refs/
│   ├── objects/
│   └── logs/
└── github_docmaker/
    ├── __init__.py
    ├── cli.py
    ├── generator.py
    ├── parser.py
    └── utils.py
```

**Reminder**: Generative AI models like the one used in this tool can sometimes produce inaccurate or misleading outputs. Always review and verify the generated documentation to ensure its accuracy and relevance.
