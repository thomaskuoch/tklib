import re
import unicodedata

# Below is inspired / stolen from https://github.com/scrapinghub/dateparser/blob/master/dateparser/date.py
RE_NBSP = re.compile("\xa0", flags=re.UNICODE)
RE_SPACES = re.compile(r"\s+")
APOSTROPHE_LOOK_ALIKE_CHARS = [
    "\N{RIGHT SINGLE QUOTATION MARK}",  # '\u2019'
    "\N{MODIFIER LETTER APOSTROPHE}",  # '\u02bc'
    "\N{MODIFIER LETTER TURNED COMMA}",  # '\u02bb'
    "\N{ARMENIAN APOSTROPHE}",  # '\u055a'
    "\N{LATIN SMALL LETTER SALTILLO}",  # '\ua78c'
    "\N{PRIME}",  # '\u2032'
    "\N{REVERSED PRIME}",  # '\u2035'
    "\N{MODIFIER LETTER PRIME}",  # '\u02b9'
    "\N{FULLWIDTH APOSTROPHE}",  # '\uff07'
    "'",
]
DASH_LOOK_ALIKE_CHARS = [
    "\u002D",
    "\u00AD",
    "\u2010",
    "\u2011",
    "\u2012",
    "\u2013",
    "\u2014",
    "\u2015",
    "\u2043",
    "\u2212",
    "\u2500",
    "-",
]
RE_SANITIZE_APOSTROPHE = re.compile(
    "(" + "|".join(APOSTROPHE_LOOK_ALIKE_CHARS) + ")"
)
RE_SANITIZE_DASH = re.compile("(" + "|".join(DASH_LOOK_ALIKE_CHARS) + ")")


def remove_multiple_ws(s: str) -> str:
    return re.sub(r"\s+", " ", str(s))


def strip_accents(s: str) -> str:
    # From https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
    return "".join(
        c
        for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


def sanitize_spaces(text: str) -> str:
    text = RE_NBSP.sub(" ", text)
    text = RE_SPACES.sub(" ", text)
    return text


def sanitize_apostrophes(text: str) -> str:
    return RE_SANITIZE_APOSTROPHE.sub("'", text)


def sanitize_dashes(text: str) -> str:
    return RE_SANITIZE_DASH.sub("-", text)


def sanitize_text(text: str) -> str:
    """Do some sanitizing steps for a cleaner text"""
    text = sanitize_spaces(text)
    text = sanitize_apostrophes(text)
    text = sanitize_dashes(text)
    text = remove_multiple_ws(text)
    text = text.strip()
    return text
