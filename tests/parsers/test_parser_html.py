from leetcode_importer.parsers.html import html_to_text


def test_remove_html_tags():
    html = "<p>Hello <strong>World</strong></p>"

    assert html_to_text(html) == "Hello World"


def test_unescape_entities():
    html = "2 &lt; 3 &amp; 5 &gt; 4"

    assert html_to_text(html) == "2 < 3 & 5 > 4"