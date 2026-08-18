from leetcode_importer.generators.cpp import CppGenerator
from leetcode_importer.models.problem import LeetCodeProblem


def test_generate_cpp():

    problem = LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array"],
        content_html="<p>Hello World</p>",
        code="class Solution {\n};",
    )

    generator = CppGenerator()

    result = generator.generate(problem)

    assert "0001. Two Sum" in result
    assert "Hello World" in result
    assert "class Solution" in result