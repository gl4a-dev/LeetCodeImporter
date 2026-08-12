from dataclasses import dataclass


@dataclass(slots=True)
class LeetCodeProblem:
    id: int
    title: str
    tags: list[str]
    content: str
    code_snippets: dict[str, str]

    def get_code(self, language: str) -> str:
        try:
            return self.code_snippets[language]
        except KeyError as exc:
            raise ValueError(
                f"Language '{language}' is not available for this problem."
            ) from exc