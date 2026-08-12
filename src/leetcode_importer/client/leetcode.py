from __future__ import annotations

from typing import Any

import requests

from leetcode_importer.client.queries import (
    QUESTION_DATA_QUERY,
    QUESTION_LIST_QUERY,
)
from leetcode_importer.exceptions import (
    InvalidAPIResponseError,
    ProblemNotFoundError,
)
from leetcode_importer.models.problem import LeetCodeProblem


class LeetCodeClient:
    GRAPHQL_URL = "https://leetcode.com/graphql"

    def __init__(self, session: requests.Session | None = None):
        self._session = session or requests.Session()

    def fetch_problem(self, problem_id: int, language: str) -> LeetCodeProblem:

        title_slug = self._get_title_slug(problem_id)

        question = self._get_question(title_slug)

        try:
            code = next(
                snippet["code"] for snippet in question["codeSnippets"]
                if snippet["langSlug"] == language
            )
        except StopIteration as exc:
            raise InvalidAPIResponseError(
                f"Language '{language}' is unavailable."
            ) from exc

        return LeetCodeProblem(
            id=int(question["questionFrontendId"]),
            title=question["title"],
            tags=[tag["name"] for tag in question["topicTags"]],
            content_html=question["content"],
            code=code,
        )

    def _get_title_slug(self, problem_id: int) -> str:

        payload = {
            "query": QUESTION_LIST_QUERY,
            "variables": {
                "skip": max(problem_id - 10, 0),
            },
        }

        response = self._post(payload)

        questions = response["data"]["problemsetQuestionListV2"]["questions"]

        for question in questions:
            if question["questionFrontendId"] == str(problem_id):
                return question["titleSlug"]

        raise ProblemNotFoundError(
            f"Problem {problem_id} not found."
        )

    def _get_question(self, title_slug: str) -> dict[str, Any]:

        payload = {
            "operationName": "questionData",
            "query": QUESTION_DATA_QUERY,
            "variables": {
                "titleSlug": title_slug,
            },
        }

        response = self._post(payload)

        try:
            return response["data"]["question"]
        except KeyError as exc:
            raise InvalidAPIResponseError(
                "Invalid response from LeetCode."
            ) from exc

    def _post(self, payload: dict[str, Any]) -> dict[str, Any]:

        response = self._session.post(
            self.GRAPHQL_URL,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()