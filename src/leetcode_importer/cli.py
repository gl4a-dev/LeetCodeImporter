import click


@click.command()
@click.option("--id", "problem_id", required=True, type=int)
@click.option("--language", required=True)
def main(problem_id: int, language: str):
    click.echo(f"ID: {problem_id}")
    click.echo(f"Language: {language}")