import sys
from enum import Enum
from typing import List

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'cap': '.....O', 'num': '.O.OOO', ' ': '......',
}
BRAILLE_TO_ENGLISH = {j: i for i, j in ENGLISH_TO_BRAILLE.items() if not i.isdigit()}
BRAILLE_TO_DIGIT = {j: i for i, j in ENGLISH_TO_BRAILLE.items() if i.isdigit()}

CAPITAL = "cap"
NUM = "num"
SPACE = " "
SIX_O = "OOOOOO"


class Language(Enum):
    BRAILLE = "BRAILLE"
    ENGLISH = "ENGLISH"


class Translator:
    def __init__(self, text: str):
        self.text: str = text

    def translate(self) -> str:
        language: Language = self._determine_language()

        if language == Language.BRAILLE:
            return self._translate_braille_to_english()
        return self._translate_english_to_braille()

    def _determine_language(self) -> Language:
        is_length_multiple_of_six: bool = len(self.text) % 6 == 0
        is_all_chars_O_or_dot: bool = all(char == 'O' or char == '.' for char in self.text)

        if self.text == SIX_O or not (is_length_multiple_of_six and is_all_chars_O_or_dot):
            return Language.ENGLISH
        else:
            return Language.BRAILLE

    def _translate_braille_to_english(self) -> str:
        translated_chars: List[str] = []
        cap_next: bool = False
        num_next: bool = False

        for i in range(0, len(self.text), 6):
            braille_char: str = self.text[i:i + 6]

            if braille_char in BRAILLE_TO_DIGIT:
                if num_next:
                    translated_chars.append(BRAILLE_TO_DIGIT[braille_char])
                    continue
            if braille_char in BRAILLE_TO_ENGLISH:
                if braille_char == ENGLISH_TO_BRAILLE[CAPITAL]:
                    cap_next = True
                elif braille_char == ENGLISH_TO_BRAILLE[NUM]:
                    num_next = True
                elif braille_char == ENGLISH_TO_BRAILLE[SPACE]:
                    num_next = False
                    translated_chars.append(SPACE)
                else:
                    if cap_next:
                        cap_next = False
                        translated_chars.append(BRAILLE_TO_ENGLISH[braille_char].upper())
                    else:
                        translated_chars.append(BRAILLE_TO_ENGLISH[braille_char])

        return ''.join(translated_chars)

    def _translate_english_to_braille(self) -> str:
        pass


def main() -> None:
    args: str = ' '.join(sys.argv[1:])
    translator = Translator(args)
    translated_text: str = translator.translate()
    print(f"{translated_text}")


if __name__ == '__main__':
    main()
