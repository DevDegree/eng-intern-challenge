import sys

braille_to_english_map = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "CAP",
    ".O...O": "DEC",
    ".O.OOO": "NUM",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

english_to_braille_map = {
    english: braille for braille, english in braille_to_english_map.items()
}

braille_to_number_map = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

number_to_braille_map = {
    number: braille for braille, number in braille_to_number_map.items()
}


def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char == " ":
            result.append(english_to_braille_map[" "])
            is_number = False
        elif char.isdigit():
            if not is_number:
                result.append(english_to_braille_map["NUM"])
                is_number = True
            result.append(number_to_braille_map[char])
        else:
            if is_number:
                is_number = False
            if char.isupper():
                result.append(english_to_braille_map["CAP"])
            result.append(english_to_braille_map[char.lower()])
    return "".join(result)


def braille_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    i = 0
    for i in range(0, len(braille), 6):
        char = braille[i : i + 6]

        if char == english_to_braille_map["CAP"]:
            is_capital = True
            continue
        if char == english_to_braille_map["NUM"]:
            is_number = True
            continue
        if char == english_to_braille_map[" "]:
            result.append(" ")
            is_number = False
            continue

        if is_number:
            decoded_char = braille_to_number_map[char]
        else:
            decoded_char = braille_to_english_map[char]

        if is_capital:
            decoded_char = decoded_char.upper()
            is_capital = False

        result.append(decoded_char)

    return "".join(result)


def main():
    args = sys.argv
    input_text = " ".join(args[1:])
    if set(input_text).issubset({"O", ".", " "}):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))


if __name__ == "__main__":
    main()
