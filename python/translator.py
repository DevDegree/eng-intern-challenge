import sys
from typing import Dict, List

BRAILLE_TO_ENGLISH: Dict[str, str] = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?",
    "..OOO.": "!", "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..O": "<", "O.O..O": "(", ".O.OO.": ")", ".....O": "capital follows",
    ".O.OOO": "number follows"
}

ENGLISH_TO_BRAILLE: Dict[str, str] = {
    v: k for k, v in BRAILLE_TO_ENGLISH.items()}

NUMBER_TO_BRAILLE: Dict[str, str] = {
    str(i): braille for i, braille in enumerate([
        ".OOO..", "O.....", "O.O...", "OO....", "OO.O..",
        "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."
    ])
}


def translate_to_braille(text: str) -> str:
    result: List[str] = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE["number follows"])
                number_mode = True
            result.append(NUMBER_TO_BRAILLE[char])
        elif char.isalpha():
            if number_mode:
                result.append(BRAILLE_TO_ENGLISH["......"])
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE["capital follows"])
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
        else:
            if number_mode:
                number_mode = False
            result.append(ENGLISH_TO_BRAILLE.get(char, ''))

    return ''.join(result)


def translate_to_english(braille: str) -> str:
    result: List[str] = []
    i = 0

    while i < len(braille):
        chunk = braille[i:i+6]
        if chunk == ENGLISH_TO_BRAILLE["capital follows"]:
            i += 6
            next_chunk = braille[i:i+6]
            result.append(BRAILLE_TO_ENGLISH[next_chunk].upper())
        elif chunk == ENGLISH_TO_BRAILLE["number follows"]:
            i += 6
            while i < len(braille) and braille[i:i+6] != BRAILLE_TO_ENGLISH["......"]:
                number = next(str(j) for j, braille_num in NUMBER_TO_BRAILLE.items()
                              if braille_num == braille[i:i+6])
                result.append(number)
                i += 6
            continue
        else:
            result.append(BRAILLE_TO_ENGLISH.get(chunk, ''))
        i += 6

    return ''.join(result)


def is_braille(text: str) -> bool:
    return all(char in 'O.' for char in text)


def main() -> None:
    input_text = ' '.join(sys.argv[1:])
    translation = translate_to_english(input_text) if is_braille(
        input_text) else translate_to_braille(input_text)
    print(translation)


if __name__ == "__main__":
    main()
