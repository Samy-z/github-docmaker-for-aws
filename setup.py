from setuptools import setup, find_packages

setup(
    name="github-docmaker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "boto3",
        "langchain",
    ],
    entry_points={
        "console_scripts": [
            "gm-doc=github_docmaker.cli:cli",
        ],
    },
    author="Your Name",
    description="CLI tool to generate documentation from GitHub repos using Mistral via AWS",
    python_requires=">=3.9",
)
