import sys

from mapper.braille_to_english_mapper import *
from mapper.english_to_braille_mapper import *


def is_braille(input_word: str) -> bool:
    return all(char in "O." for char in input_word)


def translate_english_to_braille(input_word: str) -> str:
    braille_output = ""

    for letter in input_word:
        if letter in ENGLISH_TO_BRAILLE_MAPPING:
            braille_output += ENGLISH_TO_BRAILLE_MAPPING.get(letter)
    return braille_output


def translate_phrase(words: list[str]):
    input_str = ' '.join(words)
    if is_braille(input_str):
        # TO-DO convert from braille to english
        pass
    else:
        print(translate_english_to_braille(input_str))


def main():
    if len(sys.argv) > 1:
        translate_phrase(sys.argv[1:])
    else:
        print("Enter a Phrase to be translated")


if __name__ == "__main__":
    main()
