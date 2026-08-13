from pathlib import Path
from unittest.mock import patch
from click.testing import CliRunner

from leetcode_importer.cli import main


def test_cli_import_problem():
    runner = CliRunner()

    with patch(
        "leetcode_importer.cli.ImportService"
    ) as service_cls:

        service = service_cls.return_value

        service.import_problem.return_value = Path(
            "problems/0001_TwoSum.py"
        )

        result = runner.invoke(
            main,
            [
                "--id",
                "1",
                "--language",
                "python",
            ],
        )

    assert result.exit_code == 0

    service.import_problem.assert_called_once_with(
        problem_id=1,
        language="python",
        output_dir=Path("problems"),
        overwrite=False,
    )

    assert "Created:" in result.output