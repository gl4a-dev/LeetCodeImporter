import pytest

from leetcode_importer.models.problem import LeetCodeProblem


@pytest.fixture
def problem():
    return LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array", "Hash Table"],
        content="Given an array...",
        code_snippets={
            "python": "class Solution:",
            "cpp": "class Solution {",
        },
    )


def test_problem_creation(problem: LeetCodeProblem):
    assert problem.id == 1
    assert problem.title == "Two Sum"
    assert problem.tags == ["Array", "Hash Table"]


def test_get_python_code(problem: LeetCodeProblem):
    assert problem.get_code("python") == "class Solution:"


def test_get_cpp_code(problem: LeetCodeProblem):
    assert problem.get_code("cpp") == "class Solution {"


def test_get_invalid_language(problem: LeetCodeProblem):
    with pytest.raises(ValueError):
        problem.get_code("java")