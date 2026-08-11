from click.testing import CliRunner

from leetcode_importer.cli import main


def test_cli_requires_problem_id():
    runner = CliRunner()

    result = runner.invoke(
        main,
        ["--language", "python"],
    )

    assert result.exit_code != 0

def test_cli_requires_language():
    runner = CliRunner()

    result = runner.invoke(
        main,
        ["--id", "30"],
    )

    assert result.exit_code != 0

def test_cli_receives_problem_id_and_language():
    runner = CliRunner()

    result = runner.invoke(
        main,
        ["--id", "30", "--language", "python"],
    )

    assert result.exit_code == 0
    assert "ID: 30" in result.output
    assert "Language: python" in result.output