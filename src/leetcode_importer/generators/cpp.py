from leetcode_importer.generators.base import BaseGenerator
from leetcode_importer.models.problem import LeetCodeProblem
from leetcode_importer.parsers.html import html_to_text


class CppGenerator(BaseGenerator):
    language = "cpp"
    extension = "cpp"
    template_name = "cpp.j2"

    def generate(self, problem: LeetCodeProblem) -> str:
        return self.render(
            problem=problem,
            description=html_to_text(problem.content_html),
        )