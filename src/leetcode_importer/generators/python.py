from leetcode_importer.models.problem import LeetCodeProblem
from leetcode_importer.parsers.html import html_to_text
from leetcode_importer.generators.base import BaseGenerator


class PythonGenerator(BaseGenerator):

    def generate(self, problem: LeetCodeProblem) -> str:

        description = html_to_text(problem.content_html)

        return f'''"""
{problem.id:04d}. {problem.title}

{description}
"""

{problem.code}
'''