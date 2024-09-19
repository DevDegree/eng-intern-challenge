import sys

# Braille dictionary for letters (lowercase) and space
ENGLISH_TO_BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
}

NUMBER_TO_BRAILLE_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS = '.O.OOO'

braille_to_english_dict = {v: k for k, v in ENGLISH_TO_BRAILLE_DICT.items()}

def is_braille(input_string):
    """Check if the input is a valid Braille string"""
    braille_chars = set(input_string[i:i+6] for i in range(0, len(input_string), 6))
    is_braille = all(c in 'O.' for c in input_string) and len(input_string) % 6 == 0 and all(c in braille_to_english_dict or c == BRAILLE_CAPITAL_FOLLOWS or c == BRAILLE_NUMBER_FOLLOWS for c in braille_chars)
    return is_braille
    

def english_to_braille(text):
    """Convert English text to Braille"""
    braille = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(BRAILLE_NUMBER_FOLLOWS)
                number_mode = True
            #convert number to a-j
            braille_char = NUMBER_TO_BRAILLE_DICT[str('0123456789'.index(char))]
            braille.append(braille_char)
        elif char.isalpha():
            if char.isupper():
                braille.append(BRAILLE_CAPITAL_FOLLOWS)
            braille_char = ENGLISH_TO_BRAILLE_DICT[char.lower()]
            braille.append(braille_char)
            number_mode = False
        elif char == ' ':
            braille_char = ENGLISH_TO_BRAILLE_DICT[char]
            braille.append(braille_char)
            number_mode = False
            
    return ''.join(braille)

def braille_to_english(braille):
    """Convert Braille to English text"""
    english = []
    i = 0
    number_mode = False
    capital_mode = False
    
    while i < len(braille):
        braille_char = braille[i:i+6]
        if braille_char == BRAILLE_CAPITAL_FOLLOWS:
            capital_mode = True
            i += 6
            continue
        elif braille_char == BRAILLE_NUMBER_FOLLOWS:
            number_mode = True
            i += 6
            continue
        elif braille_char == '......':
            english.append(' ')
            number_mode = False
        else:
            char = braille_to_english_dict.get(braille_char, '')
            if char:
                if number_mode and char in 'abcdefghijklmnopqrstuvwxyz':
                    char = str('0123456789'[ord(char) - ord('a') + 1])
                elif capital_mode:
                    char = char.upper()
                
                english.append(char)
            
            capital_mode = False
        i += 6
    
    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)

if __name__ == "__main__":
    main()