import click
from github_docmaker.generator import generate_docs

@click.group()
def cli():
    """GitHub DocMaker CLI"""
    pass

@cli.command()
@click.option("--repo", required=True, help="GitHub repo URL or path")
@click.option("--output", default="README.md", help="Output file path")
@click.option("--log-s3", default=None, help="S3 URI for logs, e.g., s3://bucket/")
@click.option("--dry-run", is_flag=True, help="Print to console, don’t write file")
def generate(repo, output, log_s3, dry_run):
    """Generate documentation for a GitHub repository."""
    generate_docs(repo_url=repo, output_path=output, log_s3=log_s3, dry_run=dry_run)

if __name__ == "__main__":
    cli()