"""CLI application to translate messages between Braille and English.


Note:
- I've created a companion repo to store my additional test cases
  and documentation. This way, I don't accidentally break the
  automated validation by modifying other files in this repo.
- You can find the companion repo here:
  https://github.com/callumcurtis/shopify-intern-challenge-harness


Assumptions:
- A message is considered to be in Braille if it consists of only 'O' and '.'
  characters.
- If a message is not considered Braille then it is considered English.
- If a message is considered Braille but is not otherwise syntactically correct
  (e.g., its length is not evenly divisibly by 6), then this application will exit
  with an exception.
- If a message is considered English but contains periods then it is considered
  syntactically incorrect and the application will exit with an exception.
- The message is expected to fit in memory.
- Multiple consecutive English-encoded spaces are combined into a single space in
  the **input** to maintain consistency between usage with quoted and unquoted arguments.
- Trailing and leading whitespace is discarded from English **inputs** to maintain
  consistency between usage with quoted and unquoted arguments.
- Braille-encoded spaces are **not** modified (e.g., combined into a single space)
  as their usage is unambiguous from the command line.


Possible Improvements:
- Generalizing the translators to accept any modes/modifiers, not just numbers
  and capitalization.
- Support streaming (input and output) for real-time translation.
"""

from __future__ import annotations

import typing
import enum


BRAILLE_ALPHABET = {"O", "."}
ENGLISH_ALPHABET = {*(
    [chr(i) for i in range(ord("a"), ord("z") + 1)]
    + [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    + [chr(i) for i in range(ord("0"), ord("9") + 1)]
    + [" "]
)}
BRAILLE_CELL_SIZE = 6
CAPITALIZED_BRAILLE_AND_ENGLISH = [
    # uppercase letters
    ("O.....", "A"),
    ("O.O...", "B"),
    ("OO....", "C"),
    ("OO.O..", "D"),
    ("O..O..", "E"),
    ("OOO...", "F"),
    ("OOOO..", "G"),
    ("O.OO..", "H"),
    (".OO...", "I"),
    (".OOO..", "J"),
    ("O...O.", "K"),
    ("O.O.O.", "L"),
    ("OO..O.", "M"),
    ("OO.OO.", "N"),
    ("O..OO.", "O"),
    ("OOO.O.", "P"),
    ("OOOOO.", "Q"),
    ("O.OOO.", "R"),
    (".OO.O.", "S"),
    (".OOOO.", "T"),
    ("O...OO", "U"),
    ("O.O.OO", "V"),
    (".OOO.O", "W"),
    ("OO..OO", "X"),
    ("OO.OOO", "Y"),
    ("O..OOO", "Z"),
]
BRAILLE_SPACE = "......"
UNMODDED_BRAILLE_AND_ENGLISH = [
    # lowercase letters
    ("O.....", "a"),
    ("O.O...", "b"),
    ("OO....", "c"),
    ("OO.O..", "d"),
    ("O..O..", "e"),
    ("OOO...", "f"),
    ("OOOO..", "g"),
    ("O.OO..", "h"),
    (".OO...", "i"),
    (".OOO..", "j"),
    ("O...O.", "k"),
    ("O.O.O.", "l"),
    ("OO..O.", "m"),
    ("OO.OO.", "n"),
    ("O..OO.", "o"),
    ("OOO.O.", "p"),
    ("OOOOO.", "q"),
    ("O.OOO.", "r"),
    (".OO.O.", "s"),
    (".OOOO.", "t"),
    ("O...OO", "u"),
    ("O.O.OO", "v"),
    (".OOO.O", "w"),
    ("OO..OO", "x"),
    ("OO.OOO", "y"),
    ("O..OOO", "z"),
    # space
    (BRAILLE_SPACE, " "),
]
NUMERIC_BRAILLE_AND_ENGLISH = [
    # numbers
    (".OOO..", "0"),
    ("O.....", "1"),
    ("O.O...", "2"),
    ("OO....", "3"),
    ("OO.O..", "4"),
    ("O..O..", "5"),
    ("OOO...", "6"),
    ("OOOO..", "7"),
    ("O.OO..", "8"),
    (".OO...", "9"),
]
CAPITALIZED_BRAILLE_TO_ENGLISH = dict(CAPITALIZED_BRAILLE_AND_ENGLISH)
UNMODDED_BRAILLE_TO_ENGLISH = dict(UNMODDED_BRAILLE_AND_ENGLISH)
NUMERIC_BRAILLE_TO_ENGLISH = dict(NUMERIC_BRAILLE_AND_ENGLISH)
BRAILLE_CAPITALIZE_MODIFIER = ".....O"
BRAILLE_NUMBER_MODE_MODIFIER = ".O.OOO"
BRAILLE_NUMBER_MODE_TERMINAL = BRAILLE_SPACE


T = typing.TypeVar("T")
V = typing.TypeVar("V")

def flip_pairs(pairs: list[tuple[T, V]]) -> list[tuple[V, T]]:
    """Flips tupled pairs within a list."""
    return [(pair[1], pair[0]) for pair in pairs]


CAPITALIZED_ENGLISH_TO_BRAILLE = dict(flip_pairs(CAPITALIZED_BRAILLE_AND_ENGLISH))
UNMODDED_ENGLISH_TO_BRAILLE = dict(flip_pairs(UNMODDED_BRAILLE_AND_ENGLISH))
NUMERIC_ENGLISH_TO_BRAILLE = dict(flip_pairs(NUMERIC_BRAILLE_AND_ENGLISH))


def chunk(s: str, chunk_size: int) -> typing.Iterator[str]:
    """Splits a string into a series of fixed-size chunks."""
    return (s[i:i + chunk_size] for i in range(0, len(s), chunk_size))


class Language(enum.Enum):
    BRAILLE = "braille"
    ENGLISH = "english"


class CliMessageParser:
    """Parses a message from the command line."""

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
    """Determines which language a message belongs to."""

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


class BrailleToEnglishTranslator:

    class _Mode(enum.Enum):
        CAPITALIZE = "capitalize"
        NUMBER = "number"

    def __init__(
        self,
        *,
        braille_cell_size: int = BRAILLE_CELL_SIZE,
        unmodded_braille_to_english: dict[str, str] = UNMODDED_BRAILLE_TO_ENGLISH,
        capitalized_braille_to_english: dict[str, str] = CAPITALIZED_BRAILLE_TO_ENGLISH,
        numeric_braille_to_english: dict[str, str] = NUMERIC_BRAILLE_TO_ENGLISH,
        braille_capitalize_modifier: str = BRAILLE_CAPITALIZE_MODIFIER,
        braille_number_mode_modifier: str = BRAILLE_NUMBER_MODE_MODIFIER,
        braille_number_mode_terminal: str = BRAILLE_NUMBER_MODE_TERMINAL,
    ):
        """
        Optional keyword arguments:
            braille_cell_size: size of each braille cell, equal to width x height
            unmodded_braille_to_english: mapping of normal-mode english characters by braille cell
            capitalized_braille_to_english: mapping of capitalize-mode english characters by braille cell
            numeric_braille_to_english: mapping of number-mode english characters by braille cell
            braille_capitalize_modifier: braille cell signaling use of the capitalize mode
            braille_number_mode_modifier: braille cell signaling beginning of the number mode
            braille_number_mode_terminal: braille cell signaling end of the number mode
        """
        self._braille_cell_size = braille_cell_size
        self._unmodded_braille_to_english = unmodded_braille_to_english
        self._capitalized_braille_to_english = capitalized_braille_to_english
        self._numeric_braille_to_english = numeric_braille_to_english
        self._braille_capitalize_modifier = braille_capitalize_modifier
        self._braille_number_mode_modifier = braille_number_mode_modifier
        self._braille_number_mode_terminal = braille_number_mode_terminal

    def translate(self, message: str) -> str:
        if len(message) % self._braille_cell_size != 0:
            raise ValueError("the message size is not divisible by the braille cell size")

        mode: BrailleToEnglishTranslator._Mode | None = None
        has_used_mode = False
        translated: list[str] = []
        for cell in chunk(message, self._braille_cell_size):
            if cell == self._braille_capitalize_modifier:
                if mode:
                    raise ValueError(f"cannot enter uppercase mode when mode is already {mode}")
                mode = self._Mode.CAPITALIZE
                has_used_mode = False
            elif cell == self._braille_number_mode_modifier:
                if mode:
                    raise ValueError(f"cannot enter number mode when mode is already {mode}")
                mode = self._Mode.NUMBER
                has_used_mode = False
            elif mode is self._Mode.NUMBER and cell == self._braille_number_mode_terminal:
                if not has_used_mode:
                    raise ValueError(f"cannot terminate number mode before translating any numbers")
                translated.append(self._unmodded_braille_to_english[cell])
                mode = None
            elif mode is self._Mode.CAPITALIZE:
                translated.append(self._capitalized_braille_to_english[cell])
                mode = None
            elif mode is self._Mode.NUMBER:
                translated.append(self._numeric_braille_to_english[cell])
                has_used_mode = True
            else:
                translated.append(self._unmodded_braille_to_english[cell])

        if mode is not None and not has_used_mode:
            raise ValueError(f"cannot terminate mode {mode} before using it")

        return "".join(translated)


class EnglishToBrailleTranslator:

    class _Mode(enum.Enum):
        NUMBER = "number"

    def __init__(
        self,
        *,
        unmodded_english_to_braille: dict[str, str] = UNMODDED_ENGLISH_TO_BRAILLE,
        capitalized_english_to_braille: dict[str, str] = CAPITALIZED_ENGLISH_TO_BRAILLE,
        numeric_english_to_braille: dict[str, str] = NUMERIC_ENGLISH_TO_BRAILLE,
        braille_capitalize_modifier: str = BRAILLE_CAPITALIZE_MODIFIER,
        braille_number_mode_modifier: str = BRAILLE_NUMBER_MODE_MODIFIER,
        braille_number_mode_terminal: str = BRAILLE_NUMBER_MODE_TERMINAL,
    ):
        """
        Optional keyword arguments:
            unmodded_english_to_braille: mapping of normal-mode braille cells by english character
            capitalized_english_to_braille: mapping of capitalize-mode braille cells by english character
            numeric_braille_to_english: mapping of number-mode braille cells by english character
            braille_capitalize_modifier: braille cell signaling use of the capitalize mode
            braille_number_mode_modifier: braille cell signaling beginning of the number mode
            braille_number_mode_terminal: braille cell signaling end of the number mode
        """
        self._unmodded_english_to_braille = unmodded_english_to_braille
        self._capitalized_english_to_braille = capitalized_english_to_braille
        self._numeric_english_to_braille = numeric_english_to_braille
        self._braille_capitalize_modifier = braille_capitalize_modifier
        self._braille_number_mode_modifier = braille_number_mode_modifier
        self._braille_number_mode_terminal = braille_number_mode_terminal

    def translate(self, message: str) -> str:
        mode: EnglishToBrailleTranslator._Mode | None = None
        translated: list[str] = []
        for character in message:
            if character in self._capitalized_english_to_braille:
                translated.extend([
                    self._braille_capitalize_modifier,
                    self._capitalized_english_to_braille[character],
                ])
            elif character in self._numeric_english_to_braille:
                if mode is not self._Mode.NUMBER:
                    translated.append(self._braille_number_mode_modifier)
                translated.append(self._numeric_english_to_braille[character])
                mode = self._Mode.NUMBER
            elif mode is self._Mode.NUMBER and character == self._braille_number_mode_terminal:
                mode = None
                translated.append(self._unmodded_english_to_braille[character])
            else:
                translated.append(self._unmodded_english_to_braille[character])

        return "".join(translated)


if __name__ == "__main__":
    message = CliMessageParser().parse()
    language = LanguageDiscriminator().determine(message)
    if language is Language.BRAILLE:
        translator = BrailleToEnglishTranslator()
    else:
        translator = EnglishToBrailleTranslator()
    translated = translator.translate(message)
    print(translated, end="")

