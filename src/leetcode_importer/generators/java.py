from leetcode_importer.generators.base import BaseGenerator
from leetcode_importer.models.problem import LeetCodeProblem
from leetcode_importer.parsers.html import html_to_text


class JavaGenerator(BaseGenerator):
    language = "java"
    extension = "java"
    template_name = "java.j2"

    def generate(self, problem: LeetCodeProblem) -> str:
        return self.render(
            problem=problem,
            description=html_to_text(problem.content_html),
        )