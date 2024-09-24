import sys

english_to_braille = {
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..', 
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..', 
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.', 
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.',
    's': '.OO.O.', 
    't': '.OOOO.', 
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO',
    ' ': '......',
    '!': '..OOO.', 
    '?': '..OO.O', 
    '.': '..OO.O', 
    ',': '..O...', 
    ':': '..OO..', 
    ';': '..O.O.', 
    '-': '....OO', 
    '/': '.O..O.', 
    "(": "O.O..O",
    ")": ".O.OO.",
    "<": ".OO..O",
    ">": "O..OO.",
    'capital': '.....O', 
    'decimal': '.O...O', 
    'number': '.O.OOO'
}

numbers_to_braille = {
    '0': '.OOO..', 
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...',
}

braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}



def is_braille(input):
    for char in input:
        if char != "O" and char != ".":
            return False
    return True



def translate_to_braille(text):
    braille = ""
    isNumberNext = False
    isCapitalNext = False

    for char in text:
        if char.isnumeric():
            if not isNumberNext:
                braille += english_to_braille['number']
                isNumberNext = True
            braille += numbers_to_braille[char]
        elif char.isalpha():
            if char.isupper():
                braille += english_to_braille['capital']
                isCapitalNext = True
            braille += english_to_braille[char.lower()]
            isNumberNext = False
        elif char == ' ':
            braille += char
            isNumberNext = False
        else:
            braille += english_to_braille.get(char, char)
            isNumberNext = False
    return braille

def translate_to_english(braille_text):
    english = ""
    isNumberNext = False
    isCapitalNext = False

    i = 0
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        if braille_char == english_to_braille['number']:
            isNumberNext = True
            i += 6
            continue
        elif braille_char == english_to_braille['capital']:
            isCapitalNext = True
            i += 6
            continue
        elif braille_char == '......':
            english += ' '
            isNumberNext = False
            i += 6
            continue
        elif isNumberNext:
            english += braille_to_numbers[braille_char]
            isNumberNext = False
        elif isCapitalNext:
            english += braille_to_english[braille_char].upper()
            isCapitalNext = False
        else:
            english += braille_to_english[braille_char]
        i += 6

    return english

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string1> <input_string2> ...")
        return

    input_strings = sys.argv[1:]

    # Determine if the input is Braille or English
    if all(is_braille(s) for s in input_strings):
        # Translate from Braille to English
        result = '......'.join([translate_to_english(s) for s in input_strings])
    else:
        # Translate from English to Braille
        result = '......'.join([translate_to_braille(s) for s in input_strings])

    print(result)

if __name__ == "__main__":
    main()

