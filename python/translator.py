import sys

braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
    "(": "O.O..O", ")": ".O.OO.", " ": "......",
}

reverse_map_alpha = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
}

reverse_map_symbols = {
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O.O..O": "(", ".O.OO.": ")",
}

reverse_map_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<",
    "O.O..O": "(", ".O.OO.": ")", "O..OO.": ">",
}

CAPITAL_BRAILLE_SYMBOL = ".....O"
DECIMAL_BRAILLE_SYMBOL = ".O...O"
NUMBER_BRAILLE_SYMBOL = ".O.OOO"

def translate_to_braille(input_string):
    result = []
    is_number = False
    for char in input_string:
        if char.isupper():
            result.append(CAPITAL_BRAILLE_SYMBOL)
            result.append(braille_map[char.lower()])
        elif char.isdigit():
            if not is_number:
                result.append(NUMBER_BRAILLE_SYMBOL)
                is_number = True
            result.append(braille_map[char])
        elif char == '.':
            result.append(DECIMAL_BRAILLE_SYMBOL)
        elif char == ' ':
            result.append(braille_map[char])
            is_number = False
        else:
            result.append(braille_map.get(char, ""))
    return ''.join(result)

def translate_to_english(input_string):
    result = []
    is_capital = False
    is_number = False

    for i in range(0, len(input_string), 6):
        symbol = input_string[i:i+6]

        if symbol == CAPITAL_BRAILLE_SYMBOL:
            is_capital = True
        elif symbol == NUMBER_BRAILLE_SYMBOL:
            is_number = True
        elif symbol == DECIMAL_BRAILLE_SYMBOL:
            result.append(".")
        else:
            if is_number:
                if symbol in reverse_map_numbers:
                    result.append(reverse_map_numbers[symbol])
                elif symbol in reverse_map_symbols:
                    result.append(reverse_map_symbols[symbol])
            else:
                if symbol in reverse_map_alpha:
                    val = reverse_map_alpha[symbol]
                    if is_capital:
                        result.append(val.upper())
                        is_capital = False
                    else:
                        result.append(val)
                elif symbol in reverse_map_symbols:
                    result.append(reverse_map_symbols[symbol])
            if symbol == "......":
                result.append(" ")
                is_number = False

    return ''.join(result)

def is_english(input_string):
    return any(char.isalnum() or char in " .,!?:;-/<>()" for char in input_string)


def is_braille(input_string):
    return all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0 and input_string != "OOOOOO"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])

        if is_braille(input_string):
            print(translate_to_english(input_string))
        elif is_english(input_string):
            print(translate_to_braille(input_string))
        else:
            print("Invalid input")
    else:
        print("Usage: python translator.py [input_string]")
