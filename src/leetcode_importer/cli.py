from pathlib import Path
import click


from leetcode_importer.services.importer import ImportService


@click.command()
@click.option(
    "--id", 
    "problem_id", 
    required=True, 
    type=int,
)
@click.option(
    "--language", 
    required=True,
)
@click.option(
    "--output-dir",
    type=click.Path(
        path_type=Path,
        file_okay=False,
        dir_okay=True,
    ),
    default=Path("problems"),
    show_default=True,
)
@click.option("--overwrite", is_flag=True)
def main(
    problem_id: int,
    language: str,
    output_dir: str,
    overwrite: bool,
):
    service = ImportService()

    path = service.import_problem(
        problem_id=problem_id,
        language=language,
        output_dir=output_dir,
        overwrite=overwrite,
    )

    click.echo(f"Created: {path}")