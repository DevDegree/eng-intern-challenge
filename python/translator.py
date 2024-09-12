import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital', '.O.OOO': 'number'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Number mappings
NUMBER_MAPPING = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        
        if char == ENGLISH_TO_BRAILLE['capital']:
            capitalize_next = True
        elif char == ENGLISH_TO_BRAILLE['number']:
            number_mode = True
        elif char == ENGLISH_TO_BRAILLE[' ']:
            result.append(' ')
            number_mode = False
        else:
            if number_mode:
                for num, braille_num in NUMBER_MAPPING.items():
                    if char == braille_num:
                        result.append(num)
                        break
            else:
                letter = BRAILLE_TO_ENGLISH.get(char, '')
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
        
        i += 6
    
    return ''.join(result)

def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                number_mode = True
            result.append(NUMBER_MAPPING[char])
        elif char.isalpha():
            if number_mode:
                result.append(ENGLISH_TO_BRAILLE[' '])  # Space to end number mode
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char == ' ':
            if number_mode:
                number_mode = False
            result.append(ENGLISH_TO_BRAILLE[' '])
        else:
            pass
    
    return ''.join(result)

def translate(input_string):
    if set(input_string).issubset({'O', '.'}):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    print(translate(input_string))