from leetcode_importer.generators.python import PythonGenerator
from leetcode_importer.models.problem import LeetCodeProblem


def test_generate_python():

    problem = LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array"],
        content_html="<p>Hello World</p>",
        code="class Solution:\n    pass",
    )

    generator = PythonGenerator()

    result = generator.generate(problem)

    assert "0001. Two Sum" in result
    assert "Hello" in result
    assert "class Solution" in result