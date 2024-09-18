import sys

# English to Braille Dictionary
english_to_braille = {
    # Numbers
    '0': '..O.OO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    # Lowercase letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    # Special characters
    'capital': '.....O', # Capitalization prefix
    'space': '......',   # Space
    'number': '.O.OOO'   # Number prefix
}

# Braille Dictionary
braille_dictionary = { 
    # Numbers
    '..O.OO': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
    # Lowercase letters
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    # Capitalization symbol
    '.....O': 'capital',
    # Space in Braille
    '......': 'space',
    # Number indicator in Braille
    '.O.OOO': 'number'
}

# Convert English string to Braille
def english_to_braille_translation(english_string):
    result = []
    for char in english_string:
        if char.isupper():  # Capitalization
            result.append(english_to_braille['capital'])
            char = char.lower()
        if char.isdigit():  # Numbers
            result.append(english_to_braille['number'])
            result.append(english_to_braille.get(char, '......'))  # Braille for number
        else:
            result.append(english_to_braille.get(char, '......'))  # Default to space if not found
    return ''.join(result)

# Convert Braille string to English
def braille_to_english_translation(braille_input):
    result = []
    capitalize = False
    number_mode = False

    chars = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]

    for char in chars:
        if char == english_to_braille['capital']:  # Capital letter indicator in Braille
            capitalize = True
        elif char == english_to_braille['number']:  # Number indicator in Braille
            number_mode = True
        elif char == english_to_braille['space']:  # Space in Braille
            result.append(' ')
            number_mode = False  # Reset number mode after space
        else:
            letter = braille_dictionary.get(char, '?')
            if number_mode:
                if letter.isdigit():
                    result.append(letter)
                    number_mode = False  # Exit number mode after processing a digit
                else:
                    number_mode = False  # Exit number mode
                    result.append(letter)  # Append the letter instead of a digit
            elif capitalize:
                if letter.isalpha():
                    result.append(letter.upper())  # Capitalize the letter
                capitalize = False  # Reset capitalization after using it
            else:
                result.append(letter)  # Append the regular letter/character

    return ''.join(result)

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("No arguments provided", file=sys.stderr)
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])
    print(f"{input_text}", file=sys.stderr)

    # Check if input is Braille or English
    if all(char in 'O.' for char in input_text):  # Simple check for Braille
        output = braille_to_english_translation(input_text)
    else:
        output = english_to_braille_translation(input_text)

    print(f"{output}", file=sys.stderr)