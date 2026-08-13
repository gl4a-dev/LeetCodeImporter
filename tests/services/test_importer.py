from pathlib import Path
from unittest.mock import Mock, patch

from leetcode_importer.models.problem import LeetCodeProblem
from leetcode_importer.services.importer import ImportService


def test_import_problem():

    client = Mock()

    writer = Mock()

    client.fetch_problem.return_value = LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array"],
        content_html="<p>Hello</p>",
        code="class Solution:",
    )

    generator = Mock()

    generator.generate.return_value = "generated"

    with patch(
        "leetcode_importer.services.importer.GeneratorFactory.create",
        return_value=generator,
    ):

        service = ImportService(
            client=client,
            writer=writer,
        )

        service.import_problem(
            problem_id=1,
            language="python",
        )

    client.fetch_problem.assert_called_once_with(
        1,
        "python",
    )

    generator.generate.assert_called_once()

    writer.write.assert_called_once()

def test_build_filename():

    problem = LeetCodeProblem(
        id=12,
        title="Integer To Roman",
        tags=[],
        content_html="",
        code="",
    )

    filename = ImportService._build_filename(
        problem,
        "py",
    )

    assert filename == "0012_IntegerToRoman.py"