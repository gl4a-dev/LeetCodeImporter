from pathlib import Path

from leetcode_importer.client.leetcode import LeetCodeClient
from leetcode_importer.filesystem.writer import FileWriter
from leetcode_importer.generators.factory import GeneratorFactory
from leetcode_importer.models.problem import LeetCodeProblem


class ImportService:

    def __init__(
        self,
        client: LeetCodeClient | None = None,
        writer: FileWriter | None = None,
    ) -> None:
        self.client = client or LeetCodeClient()
        self.writer = writer or FileWriter()

    def import_problem(
        self,
        problem_id: int,
        language: str,
        output_dir: Path = Path("problems"),
        overwrite: bool = False,
    ) -> Path:

        problem = self.client.fetch_problem(
            problem_id,
            language,
        )

        generator = GeneratorFactory.create(language)

        content = generator.generate(problem)

        filename = self._build_filename(
            problem,
            generator.extension,
        )

        path = output_dir / filename

        return self.writer.write(
            path=path,
            content=content,
            overwrite=overwrite,
        )

    @staticmethod
    def _build_filename(
        problem: LeetCodeProblem,
        extension: str,
    ) -> str:

        title = "".join(
            word.capitalize()
            for word in problem.title.split()
        )

        return f"{problem.id:04d}_{title}.{extension}"