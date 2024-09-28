import sys

from typing import List


# TODO : 2 Hashmaps constantes avec lettres et braille
braille_to_english = {
    "O....."
}

def args_is_braille(args: List[str]) -> bool:
    return len(args) == 2 and all(char in 'O.' for char in args[1])


def split_into_letters(braille: str) -> List[str]:
    letters = []
    lettre = ''
    iterator = 1
    for char in braille:
        lettre += char
        iterator += 1
        if iterator == 7:
            letters.append(lettre)
            iterator = 1
            lettre = ''
    return letters
    # return [braille[i:i+6] for i in range(0, len(braille), 6)]


def translate_to_english(braille: str) -> str:
    return 'input est braille'


def translate_to_braille(english_words: List[str]) -> str:
    return 'input est anglais'


def main():
    if args_is_braille(sys.argv):
        print(translate_to_english(sys.argv[1]))
    else:
        print(translate_to_braille(sys.argv[1:]))


if __name__ == "__main__":
    main()
