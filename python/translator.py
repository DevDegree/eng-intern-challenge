"""CLI application to translate messages between Braille and English.

--------------------------------------------------------------------------------
IMPORTANT
--------------------------------------------------------------------------------
I've created a companion repo to store my additional test cases
and documentation. This way, I don't accidentally break the
automated validation by modifying other files in this repo.

You can find the companion repo here:
https://github.com/callumcurtis/shopify-intern-challenge-harness
--------------------------------------------------------------------------------

This application makes some assumptions (since the starter repo did not completely
specify expected behavior in all cases).

- A message is considered to be in Braille if it consists of only 'O' and '.'
  characters.
- If a message is not considered Braille then it is considered English.
- If a message is considered Braille but is not otherwise syntactically correct
  (e.g., its length is not evenly divisibly by 6), then this application will exit
  with an exception.
- If a message is considered English but contains periods then it is considered
  syntactically incorrect and the application will exit with an exception.
- The message is expected to fit in memory.
- Multiple consecutive spaces are combined into a single space in the **input**
  to maintain consistency between usage with quoted and unquoted arguments.
- Trailing and leading spaces are stripped in the **output** as spaces are
  intended only as separators between words.
"""

from __future__ import annotations

import enum


BRAILLE_ALPHABET = {"O", "."}
ENGLISH_ALPHABET = {*(
    [chr(i) for i in range(ord("a"), ord("z") + 1)]
    + [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    + [chr(i) for i in range(ord("0"), ord("9") + 1)]
    + [" "]
)}


class Language(enum.Enum):
    BRAILLE = "braille"
    ENGLISH = "english"


class CliMessageParser:

    def __init__(
        self,
        *,
        separator: str = " ",
        split_compound_args: bool = True,
    ):
        """
        Optional keyword arguments:
            separator: the character(s) to place between tokens in the output message.
            split_compound_args: whether to split quoted arguments containing multiple tokens.
        """
        self.separator = separator
        self.split_compound_args = split_compound_args

    def parse(self, args: list[str] | None = None):
        """Returns the message formed by the given cli arguments.

        The first argument is assumed to be the name of the script and
        is excluded from the message.

        Arguments:
            args: list of cli arguments
        """
        if not args:
            import sys
            args = sys.argv
        if self.split_compound_args:
            args = [
                arg
                for compound in args
                for arg in compound.split()
            ]
        return self.separator.join(args[1:])


class LanguageDiscriminator:

    def __init__(
        self,
        *,
        braille_alphabet: set[str] = BRAILLE_ALPHABET,
        english_alphabet: set[str] = ENGLISH_ALPHABET,
    ):
        self._braille_alphabet = braille_alphabet
        self._english_alphabet = english_alphabet

    def determine(self, message: str) -> Language:
        is_english = is_braille = True
        for character in message:
            is_braille &= character in self._braille_alphabet
            is_english &= character in self._english_alphabet
            if not (is_braille or is_english):
                raise ValueError("the provided message is neither english nor braille")
        if is_braille:
            # braille takes priority over english
            return Language.BRAILLE
        return Language.ENGLISH


if __name__ == "__main__":
    original_message = CliMessageParser().parse()
    original_language = LanguageDiscriminator().determine(original_message)
    print(original_language)

