import sys

english_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "cap": ".....O", "num": ".O.OOO", " ": "......"
}

braille_to_english_map = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital", ".O.OOO": "num", "......": " "
}

braille_to_num_map = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}


def is_braille(input_str):
    return all(c in 'O.' for c in input_str)


def braille_to_english(braille_str):
    english = []
    capitalize_next = False
    number_next = False

    for i in range(0, len(braille_str), 6):
        ch = braille_str[i:i+6]
        if ch == ".....O":
            capitalize_next = True
        elif ch == ".O.OOO":
            number_next = True
        elif ch == "......":
            number_next = False
            english.append(" ")
        else:
            char = braille_to_english_map.get(ch, '')
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            if number_next:
                char = braille_to_num_map.get(ch, '')
                english.append(char)
            else:
                english.append(char)

    return ''.join(english)


def english_to_braille(english_str):
    braille = []
    number_next = False
    for char in english_str:
        if char.isupper():
            braille.append(english_to_braille_map.get("cap", ''))
            braille.append(english_to_braille_map.get(char.lower(), ''))
        elif char.isdigit():
            if not number_next:
                braille.append(english_to_braille_map.get("num", ''))
                number_next = True
            braille.append(english_to_braille_map.get(char, ''))
        elif char == " ":
            number_next = False
            braille.append(english_to_braille_map.get(char, ''))
        else:
            braille.append(english_to_braille_map.get(char, ''))
    return ''.join(braille)


def main():
    if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))


if __name__ == "__main__":
    main()
