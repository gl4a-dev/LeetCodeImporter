from leetcode_importer.generators.python import PythonGenerator
from leetcode_importer.models.problem import LeetCodeProblem


def test_generate_python_file():

    problem = LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array"],
        content_html="<p>Hello World</p>",
        code="class Solution:\n    pass",
    )

    generator = PythonGenerator()

    content = generator.generate(problem)

    assert "0001. Two Sum" in content
    assert "Hello World" in content
    assert "<p>" not in content
    assert "class Solution" in content