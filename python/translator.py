import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '.O.O..', ',': '.O....', '?': '.O..O.', '!': '.O.OO.', ':': '.O.O..', ';': '.OO...', '-': '..OO..', '/': '.O..O.', '<': 'O..O.O', '>': '.OOO..', '(': 'O.OOO.', ')': '.O.OOO',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Check if the input text is in Braille and if each character in the text is equal to 6
def is_braille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

# Reverse the braille_dict for English to Braille conversion
english_dict = {value: key for key, value in braille_dict.items()}

# Converts English text into its Braille equivalent
def english_to_braille(text):
    result = ""
    is_number = False
    
    for char in text:
        if char.isdigit():
            if not is_number:
                result += braille_dict['number']
                is_number = True
            result += braille_dict[char]
        elif char.isupper():
            result += braille_dict['capital'] + braille_dict[char.lower()]
            is_number = False
        else:
            if is_number and not char.isdigit():
                is_number = False
            result += braille_dict.get(char.lower(), '')
    
    return result

# Converts Braille text into its English equivalent
def braille_to_english(braille):
    result = ""
    i = 0
    capitalize_next = False
    is_number = False
    
    while i < len(braille):
        brailleBlock = braille[i:i+6]
        
        if brailleBlock == braille_dict['capital']:
            capitalize_next = True
            i += 6
            continue
        
        if brailleBlock == braille_dict['number']:
            is_number = True
            i += 6
            continue
        
        if brailleBlock == braille_dict[' ']:
            result += ' '
            is_number = False
            i += 6
            continue
        
        char = english_dict.get(brailleBlock, '')
        
        if is_number:
            if char in '123456789':
                result += char
            else:
                is_number = False
                if capitalize_next:
                    result += char.upper()
                    capitalize_next = False
                else:
                    result += char
        else:
            # Always interpret as letter if it is not a number
            letter = english_dict.get(brailleBlock, '')
            if letter in '123456789':
                letter = chr(ord('a') + int(letter) - 1)
            if capitalize_next:
                result += letter.upper()
                capitalize_next = False
            else:
                result += letter
        
        i += 6
    
    return result

if __name__ == "__main__":
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))