from leetcode_importer.generators.base import BaseGenerator
from leetcode_importer.models.problem import LeetCodeProblem
from leetcode_importer.parsers.html import html_to_text


class PythonGenerator(BaseGenerator):
    template_name = "python.j2"
    language = "python"
    extension = "py"

    def generate(self, problem: LeetCodeProblem) -> str:
        return self.render(
            problem=problem,
            description=html_to_text(problem.content_html),
        )