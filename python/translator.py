import sys

# Braille mappings
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
    '.....O': 'capital_follows','.O.OOO': 'number_follows',
}

# English mappings
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

# Number mappings
NUMBER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

# Translate Braille to English
def braille_to_english(braille: str) -> str:
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        # Get every 6 Braille characters in text (= 1 English letter)
        char = braille[i:i+6]
        
        if char == '.....O':  # Capital follows
            capitalize_next = True
        elif char == '.O.OOO':  # Number follows
            number_mode = True
        elif char == '......':  # Space
            result.append(' ')
            number_mode = False
        else:
            # Get the corresponding English letter from the Braille mapping
            letter = BRAILLE_TO_ENGLISH.get(char, '')
            if number_mode:
                result.append(NUMBER_MAP[letter])
            elif capitalize_next:
                result.append(letter.upper())
                capitalize_next = False
                number_mode = False
            else:
                result.append(letter)
                number_mode = False
        
        i += 6
        
    return ''.join(result)

# Translate English to Braille
def english_to_braille(english: str) -> str:
    result = []
    number_mode = False

    for char in english:
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE['number_follows'])
                number_mode = True
            digit_as_letter = [k for k, v in NUMBER_MAP.items() if v == char][0]
            result.append(ENGLISH_TO_BRAILLE[digit_as_letter])
        elif char.isalpha():
            if number_mode:
                result.append('......')  # Add a space to exit number mode
                number_mode = False
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital_follows'])
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
            else:
                result.append(ENGLISH_TO_BRAILLE[char.lower()])
        elif char in ENGLISH_TO_BRAILLE:
            result.append(ENGLISH_TO_BRAILLE[char])
            number_mode = False
    
    return ''.join(result)

# Check if string is a valid Braille string
def is_braille(text:str) -> bool:
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

# Main function
def translate(text:str) -> str:
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

# Test script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
