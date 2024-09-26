import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'CAPITAL', '.O.OOO': 'NUMBER'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isalpha():
            if number_mode:
                result.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['CAPITAL'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char])
        elif char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            number_mode = False
            result.append(ENGLISH_TO_BRAILLE[char])
    
    return ''.join(result)

def braille_to_english(braille):
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capitalize_next = False
    number_mode = False
    
    for char in braille_chars:
        if char == ENGLISH_TO_BRAILLE['CAPITAL']:
            capitalize_next = True
        elif char == ENGLISH_TO_BRAILLE['NUMBER']:
            number_mode = True
        else:
            if char in BRAILLE_TO_ENGLISH:
                letter = BRAILLE_TO_ENGLISH[char]
                if number_mode:
                    for num, braille_num in BRAILLE_NUMBERS.items():
                        if braille_num == char:
                            result.append(num)
                            break
                    else:
                        number_mode = False
                        if capitalize_next:
                            letter = letter.upper()
                            capitalize_next = False
                        result.append(letter)
                else:
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    result.append(letter)
                if letter == ' ':
                    number_mode = False
            else:
                result.append('?')  # Unknown character
    
    return ''.join(result)

def translate(text):
    if set(text).issubset({'O', '.'}):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text), end='')
    else:
        print("Please provide a string to translate.")