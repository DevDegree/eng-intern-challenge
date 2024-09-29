import sys


braille_alphabet = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
}

braille_numbers = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}


braille_capital = ".....O"
braille_number = ".O.OOO"


english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}


def translate_braille_to_english(braille_string):
    result = []
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille_string):
        char = braille_string[i : i + 6]

        if char == braille_capital:
            is_capital = True
            i += 6
            continue
        if char == braille_number:
            is_number = True
            i += 6
            continue
        if is_number:
            result.append(english_numbers.get(char, "?"))
            i += 6
            continue
        letter = english_alphabet.get(char, "?")
        if is_capital:
            letter = letter.upper()
            is_capital = False
        result.append(letter)
        i += 6
    return "".join(result)


def translate_english_to_braille(english_string):
    result = []
    is_number = False

    for char in english_string:
        if char.isupper():
            result.append(braille_capital)
            char = char.lower()
        if char.isdigit():
            if not is_number:
                result.append(braille_number)
                is_number = True
            result.append(braille_numbers[char])
        else:
            result.append(braille_alphabet.get(char, "......"))
            is_number = False
    return "".join(result)


def translate(input_string):
    if all(c in "O." for c in input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)


if __name__ == "__main__":

    input_string = " ".join(sys.argv[1:])
    result = translate(input_string)
    print(result)
