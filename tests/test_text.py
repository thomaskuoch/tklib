from tklib.helpers.text import sanitize_text, strip_accents


def test_sanitize_text():
    text = "  ⁃Hello‵   world\xa0 "
    assert sanitize_text(text) == "-Hello' world"


def test_strip_accents():
    text = "Héllô world"
    assert strip_accents(text) == "Hello world"
