import json
import os
import sys
from enum import Enum


class LanguageType(Enum):
    ENGLISH = "english"
    BRAILLE = "braille"


class BrailleTranslator:
    def __init__(self, text: str):
        self.text = text
        self.token_length = None
        self.offset = 0
        self.braille_map = {}
        self.reverse_braille_map = {}

    # assumes english text is not nonsensical
    def initialize(self):
        self.text_type = (
            LanguageType.BRAILLE
            if set(self.text) == {".", "O"}
            else LanguageType.ENGLISH
        )

        self.token_length = 6 if self.text_type == LanguageType.BRAILLE else 1
        self.load_braille_translations()

    def load_braille_translations(self):
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        braille_file_path = os.path.join(script_dir, "translations", "braille.json")
        try:
            with open(braille_file_path, "r") as f:
                self.braille_map = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Could not find braille.json at {braille_file_path}"
            )

        self.reverse_braille_map = {v: k for k, v in self.braille_map.items()}

    def next_token(self) -> str:
        if not self.token_length:
            raise Exception("Please call initialize()")

        if self.offset >= len(self.text):
            return None

        next_offset = self.offset + self.token_length
        token = self.text[self.offset : next_offset]
        self.offset = next_offset
        return token

    def braille_to_english(self) -> str:
        result = []
        capitalize_next = False
        number_mode = False
        while token := self.next_token():
            if token == self.braille_map.get("capital_follows"):
                capitalize_next = True
                continue
            elif token == self.braille_map.get("number_follows"):
                number_mode = True
                continue
            elif token == self.braille_map.get(" "):
                number_mode = False

            translated_char = self.reverse_braille_map.get(token, "?")

            if capitalize_next and translated_char.isalpha():
                translated_char = translated_char.upper()
                capitalize_next = False

            if number_mode and translated_char.isalpha():
                if translated_char in "abcdefghij":
                    translated_char = str(ord(translated_char) - ord("a") + 1)

            result.append(translated_char)
        return "".join(result)

    def english_to_braille(self) -> str:
        result = []
        number_mode = False
        while token := self.next_token():
            if token.isupper():
                result.append(self.braille_map.get("capital_follows"))
                token = token.lower()

            if token.isdigit():
                if not number_mode:
                    result.append(self.braille_map.get("number_follows"))
                    number_mode = True
                token = chr(ord("a") + int(token) - 1)

            elif token == " ":
                number_mode = False

            result.append(self.braille_map.get(token, "......"))
        return "".join(result)

    def translate(self) -> str:
        if self.text_type == LanguageType.BRAILLE:
            return self.braille_to_english()
        return self.english_to_braille()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <text_to_translate>")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])

    translator = BrailleTranslator(input_text)
    translator.initialize()
    print(translator.translate())


if __name__ == "__main__":
    main()
