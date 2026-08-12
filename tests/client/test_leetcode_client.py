from requests import Session, Response
from unittest.mock import Mock, patch

from leetcode_importer.client.leetcode import LeetCodeClient


def test_post_returns_json():

    session = Mock(spec=Session)
    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "data": {}
    }

    session.post.return_value = response

    client = LeetCodeClient(session)

    result = client._post(
        {"query": "..."}
    )

    assert result == {
        "data": {}
    }

def test_post_uses_graphql_url():

    session = Mock(spec=Session)

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {}

    session.post.return_value = response

    client = LeetCodeClient(session)

    payload = {
        "query": "..."
    }

    client._post(payload)

    session.post.assert_called_once_with(
        LeetCodeClient.GRAPHQL_URL,
        json=payload,
        timeout=10,
    )

def test_fetch_problem_returns_model():

    client = LeetCodeClient()

    with (
        patch.object(
            client,
            "_get_title_slug",
            return_value="two-sum",
        ),
        patch.object(
            client,
            "_get_question",
            return_value={
                "questionFrontendId": "1",
                "title": "Two Sum",
                "content": "content",
                "topicTags": [
                    {"name": "Array"},
                ],
                "codeSnippets": [
                    {
                        "langSlug": "python",
                        "code": "class Solution:",
                    }
                ],
            },
        ),
    ):

        problem = client.fetch_problem(
            1,
            "python",
        )

    assert problem.id == 1
    assert problem.title == "Two Sum"
    assert problem.code == "class Solution:"