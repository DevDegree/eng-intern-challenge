import sys

# Diccionarios para letras, números y caracteres especiales
lettersList = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O..O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "CAP": ".....O", "NUM": ".O.OOO", ".": "..OO.O", " ": "......"
}

numbersList = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

specialList = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
}

braillEnglishList = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O..O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", ".....O": "CAP", ".O.OOO": "NUM", "......": " ", ".O...O": "."
}

numberStart = ".O.OOO"
capitalLetterStart = ".....O"
space = "......"

# Función para traducir de texto inglés a Braille
def english_to_braille(text):
    braille_output = ""
    num_state = False

    for char in text:
        if char.isdigit():
            if not num_state:
                braille_output += lettersList["NUM"]
                num_state = True
            braille_output += numbersList[char]
        else:
            if num_state:
                num_state = False
            if char.isupper():
                braille_output += lettersList["CAP"]
            braille_output += lettersList[char.lower()]

    return braille_output

# Función para traducir de Braille a texto inglés
def braille_to_english(text):
    text_output = ""
    capital = False
    num_state = False

    for i in range(0, len(text), 6):
        symbol = text[i:i + 6]

        if symbol == lettersList["CAP"]:
            capital = True
            continue
        elif symbol == lettersList["NUM"]:
            num_state = True
            continue

        if num_state:
            text_output += numbersList.get(symbol, "?")
            if symbol == " ":
                num_state = False
        else:
            if capital:
                text_output += braillEnglishList.get(symbol, "?").upper()
                capital = False
            else:
                text_output += braillEnglishList.get(symbol, "?")

    return text_output

# Función principal para detectar el formato y traducir
def translate(input_string):
    if all(char in 'O.' for char in input_string):  # Si solo contiene 'O' y '.'
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)


def main():
    """
    The main function
    """

    input_strings = sys.argv[1:]  # This captures all arguments after the script name
    for input_string in input_strings:
        result = translate(input_string)


if __name__ == "__main__":
    main()
