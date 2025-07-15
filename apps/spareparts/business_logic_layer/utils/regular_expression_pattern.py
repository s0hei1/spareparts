import re
from typing import ClassVar


class RePatterns:


    STANDARD_PATTERN_1: ClassVar[str] = r"^(?!\d)(?!.* {2})[A-Za-z][A-Za-z0-9 _-]*$"
    """
    Regex Pattern: NAME_PATTERN

    Description:
        Validates a name string based on the following rules:

        1. Must not start with a digit.
        2. Must not contain two or more consecutive spaces.
        3. Must start with a letter (A–Z or a–z).
        4. Can contain:
            - Letters (A–Z, a–z)
            - Digits (0–9)
            - Single spaces (no double spaces)
            - Underscores `_`
            - Hyphens `-`
        5. Entire string is matched from start `^` to end `$`.

    Examples:
        OK : "JohnDoe"
        OK : "John_Doe"
        OK : "John Doe"
        OK : "J"
        Fail : "  John"          → starts with space
        Fail : "123John"        → starts with number
        Fail : "John  Doe"      → double space
        Fail : "Jo@hn"          → contains invalid character (@)

    Usage:
        import re
        if re.match(NAME_PATTERN, name):
            # Valid name
            ...
    """

    NO_DOUBLE_SPACES_PATTERN = r"^(?!.* {2}).+$"
    """
    Regex Pattern: NO_DOUBLE_SPACES_PATTERN

    Ensures that the input string does not contain two or more consecutive spaces anywhere within it.
    The pattern uses a negative lookahead to detect and reject strings that include double spaces,
    while still allowing single spaces and any other characters. Useful for validating names, sentences,
    or user input where spacing rules are important.
    """
