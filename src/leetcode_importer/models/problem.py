from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class LeetCodeProblem:
    id: int
    title: str
    tags: list[str]
    content_html: str
    code: str