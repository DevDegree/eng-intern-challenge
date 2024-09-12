import sys

# Diccionarios para letras, números y caracteres especiales
lettersList = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO'
}

numbersList = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

specialList = {
    '.': '..O...', ',': '..OO..', ';': '..OO.O', ':': '..O.O.', '!': '.O..O.', '?': '.O.OO.',
    '-': '.O...O', "'": '.O....', '/': '.OO...', '(': 'O.OOOO', ')': '.OOOOO', '<': 'O..O..',
    '>': 'O..O.O'
}

numberStart = ".O.OOO"
capitalLetterStart = ".....O"
space = "......"

# Función para traducir de texto inglés a Braille
def english_to_braille(text):
    braille_output = []
    for char in text:
        if char.isdigit():
            braille_output.append(numberStart)
            braille_output.append(numbersList[char])
        elif char.isalpha():
            if char.isupper():
                braille_output.append(capitalLetterStart)
            braille_output.append(lettersList[char.lower()])
        elif char in specialList:
            braille_output.append(specialList[char])
        else:
            braille_output.append(space)
    return ''.join(braille_output)

# Función para traducir de Braille a texto inglés
def braille_to_english(braille):
    text_output = []
    i = 0
    is_number = False
    is_capital = False

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == numberStart:
            is_number = True
            i += 6
            continue
        elif symbol == capitalLetterStart:
            is_capital = True
            i += 6
            continue
        elif symbol == space:
            text_output.append(' ')
        elif is_number:
            text_output.append(list(numbersList.keys())[list(numbersList.values()).index(symbol)])
            is_number = False
        elif is_capital:
            text_output.append(list(lettersList.keys())[list(lettersList.values()).index(symbol)].upper())
            is_capital = False
        else:
            text_output.append(list(lettersList.keys())[list(lettersList.values()).index(symbol)])
        i += 6

    return ''.join(text_output)

# Función principal para detectar el formato y traducir
def translate(input_string):
    if all(char in 'O.' for char in input_string):  # Si solo contiene 'O' y '.'
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

# Ejemplos de ejecución
if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])
    translate(input_string)
