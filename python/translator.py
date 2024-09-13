import sys
from enum import Enum

SIX_O: str = "OOOOOO"


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
        pass

    def _translate_english_to_braille(self) -> str:
        pass


def main() -> None:
    args: str = ' '.join(sys.argv[1:])
    translator = Translator(args)
    translated_text: str = translator.translate()
    print(f"{translated_text}")


if __name__ == '__main__':
    main()
