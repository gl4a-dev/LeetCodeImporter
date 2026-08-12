import pytest

from leetcode_importer.models.problem import LeetCodeProblem


@pytest.fixture
def problem():
    return LeetCodeProblem(
        id=1,
        title="Two Sum",
        tags=["Array", "Hash Table"],
        content_html="Given an array...",
        code="class Solution:\n    pass",
    )


def test_problem_creation(problem: LeetCodeProblem):
    assert problem.id == 1
    assert problem.title == "Two Sum"
    assert problem.tags == ["Array", "Hash Table"]


def test_problem_is_immutable(problem: LeetCodeProblem):
    with pytest.raises(AttributeError):
        problem.title = "Other"