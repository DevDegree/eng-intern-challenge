# translator.py
import sys

# Braille to English and English to Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.O.OOO': 'capital_follows', '.O.O.O': 'number_follows',
    '......': ' '
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Numbers in Braille
NUMBERS = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        char = braille[i:i+6]
        if char == ENGLISH_TO_BRAILLE['capital_follows']:
            capitalize_next = True
            i += 6
            continue
        elif char == ENGLISH_TO_BRAILLE['number_follows']:
            number_mode = True
            i += 6
            continue
        elif char == '......':
            result.append(' ')
            number_mode = False
            i += 6
            continue

        if char in BRAILLE_TO_ENGLISH:
            letter = BRAILLE_TO_ENGLISH[char]
            if number_mode and letter in NUMBERS:
                result.append(NUMBERS[letter])
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
                number_mode = False
        i += 6

    return ''.join(result)

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number_follows'])
                number_mode = True
            result.append(ENGLISH_TO_BRAILLE[list(NUMBERS.keys())[list(NUMBERS.values()).index(char)]])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital_follows'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            result.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
        else:
            # Handle other characters if needed
            pass

    return ''.join(result)

def translate(input_string):
    # Determine if input is Braille or English
    if all(c in 'O.' for c in input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text), end='')
    else:
        print("Please provide a string to translate.")


#Comitting with new github account

        