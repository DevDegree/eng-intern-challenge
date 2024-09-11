import sys

# Braille mappings
BRAILLE_TO_ENG = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ', '.....O': 'CAP', '.O.OOO': 'NUM'
}

ENG_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENG.items()}

# Number mappings
NUMBER_MAP = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

def braille_to_english(braille):
    result = ""
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        
        if char == ENG_TO_BRAILLE['CAP']:
            capitalize_next = True
        elif char == ENG_TO_BRAILLE['NUM']:
            number_mode = True
        elif char in BRAILLE_TO_ENG:
            letter = BRAILLE_TO_ENG[char]
            if letter == ' ':
                result += ' '
                number_mode = False
            elif number_mode and letter in 'abcdefghij':
                result += str('abcdefghij'.index(letter) + 1)[-1]
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result += letter
        
        i += 6

    return result

def english_to_braille(english):
    result = ""
    number_mode = False

    for char in english:
        if char.isdigit():
            if not number_mode:
                result += ENG_TO_BRAILLE['NUM']
                number_mode = True
            result += ENG_TO_BRAILLE[NUMBER_MAP[char]]
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result += ENG_TO_BRAILLE['CAP']
            result += ENG_TO_BRAILLE[char.lower()]
        elif char == ' ':
            result += ENG_TO_BRAILLE[' ']
            number_mode = False
        else:
            pass

    return result

def is_braille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    result = translate(input_text)
    print(result)
    sys.stdout.flush()