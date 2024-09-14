import sys

# Braille dictionary: maps English characters (letters, digits, punctuation) to Braille codes.
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '.O.O..', ',': '.O....', '?': '.O..O.', '!': '.O.OO.', ':': '.O.O..', ';': '.OO...', '-': '..OO..', '/': '.O..O.', '<': 'O..O.O', '>': '.OOO..', '(': 'O.OOO.', ')': '.O.OOO',
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}


# Reverse the braille_map to create a dictionary for Braille-to-English translation
english_dict = {value: key for key, value in braille_map.items()}

# Function to check if a given text consists only of Braille characters (O and .)
def is_braille(text):
    
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

# Converts English text into its Braille equivalent
def english_to_braille(text):
    
    braille_translation = ""
    is_number = False

    for char in text:
        if char.isdigit():
            # set is_number flag to True
            if not is_number:
                braille_translation += braille_map['number']
                is_number = True
            braille_translation += braille_map[char]
        elif char.isupper():
            # Prefix uppercase letters with the capital indicator
            braille_translation += braille_map['capital'] + braille_map[char.lower()]
            is_number = False
        else:
            # Exit number mode if a non-digit character is encountered
            if is_number and not char.isdigit():
                is_number = False
            braille_translation += braille_map.get(char.lower(), '')

    return braille_translation

# Function to convert Braille text into its English equivalent
def braille_to_english(braille):
    
    english_translation = ""
    i = 0
    capitalize_next = False
    is_number = False

    while i < len(braille):
        brailleBlock = braille[i:i+6]

        if brailleBlock == braille_map['capital']:
            # Activate capitalization for the next letter
            capitalize_next = True
            i += 6
            continue

        if brailleBlock == braille_map['number']:
            is_number = True
            i += 6
            continue

        if brailleBlock == braille_map[' ']:
            english_translation += ' '
            is_number = False
            i += 6
            continue

        char = english_dict.get(brailleBlock, '')

        if is_number:
            if char in '123456789':
                english_translation += char
            else:
                is_number = False
                if capitalize_next:
                    english_translation += char.upper()
                    capitalize_next = False
                else:
                    english_translation += char
        else:
            # Always interpret as letter if it is not a number
            letter = english_dict.get(brailleBlock, '')
            if letter in '123456789':
                letter = chr(ord('a') + int(letter) - 1)
            if capitalize_next:
                english_translation += letter.upper()
                capitalize_next = False
            else:
                english_translation += letter

        i += 6

    return english_translation

if __name__ == "__main__":
    # Get input from command line argument
    input_text = ' '.join(sys.argv[1:])

    # Check if input is in Braille or English, then translate accordingly
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))