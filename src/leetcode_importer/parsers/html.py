from html import unescape
import re


_TAG_RE = re.compile(r"<[^>]+>")


def html_to_text(html: str) -> str:
    """Convert LeetCode HTML content to plain text."""

    text = _TAG_RE.sub("", html)

    text = unescape(text)

    return text.strip()