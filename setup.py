from setuptools import setup, find_packages

setup(
    name="github-docmaker-for-aws",
    version="0.1.0",
    packages=find_packages(),
    author="Samy Z",
    author_email="cool.ideas.ai@gmail.com",
    install_requires=[
        "click",
        "boto3",
        "langchain",
    ],
    entry_points={
        "console_scripts": [
            "gen-doc=github_docmaker.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    description="""CLI tool to generate documentation from GitHub repos using Mistral Large via AWS. 
    AWS CLI and credentials must be properly configured to use the package.
    AWS EC2, SageMaker, or similar AWS environments are supported natively, but this package works on any machine with AWS environment keys configured, not just AWS-specific machines.""",
    python_requires=">=3.9",
)
