
import argparse

braille_dictionary = {
        # Letters with Numbers corresponding for a-j
        'O.....': 'a1', 'O.O...': 'b2', 'OO....': 'c3', 'OO.O..': 'd4', 'O..O..': 'e5',
        'OOO...': 'f6', 'OOOO..': 'g7', 'O.OO..': 'h8', '.OO...': 'i9', '.OOO..': 'j0',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
        # Punctuation
        '..O...': '.', '..OOO.': ',', '..OO.O': '?', '..O.OO': '!', '.O..OO': ':',
        '.O..O.': ';', '....O.': '-', '..OOOO': '/', '.O.O.O': '<', 'O...O.': '>',
        'O.O..O': '(', '.O.OO.': ')',
        # Special Symbols
        '.....O': 'capitalize follows',   # Capital letter
        'O..O.O': '.',      # Decimal
        '.O.OOO': 'number follows',       # Number
        '......': ' ',                # Space
        }

eng_dictionary = {
        # Letters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
        # Number
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        # Punctuation
        '.': '..O...', ',': '..OOO.', '?': '..OO.O', '!': '..O.OO', ':': '.O..OO',
        ';': '.O..O.', '-': '....O.', '/': '..OOOO', '<': '.O.O.O', '>': 'O...O.',
        '(': 'O.O..O', ')': '.O.OO.',
        # Special Symbols
        'capitalize follows': '.....O', 
        'decimal follows': 'O..O.O',
        'number follows': '.O.OOO',
        ' ': '......'
        }
# .O.OOO OO.O.. O..O.O OOO...
# .O.OOO OO.O.. O..O.O OOO...

def get_eng_char(braille_char, is_capital, is_number):

    eng_char = braille_dictionary.get(braille_char)

    if is_number:
        if len(eng_char) == 2:
            return eng_char[1]
        else:
            return eng_char
    else:
        if is_capital:
            return eng_char[0].upper()
        else:
            return eng_char[0]
    

def braille_to_eng(braille):

    braille_list = []
    is_capital = False
    is_number = False
    translation = ''

    for i in range(0, len(braille), 6):
        # is_capital = False
        # is_number = False

        braille_char = braille[i:i + 6]

        if braille_char == '.....O':
            is_capital = True
        elif braille_char == '.O.OOO':
            is_number = True
        elif braille_char == '......':
            is_number = False
            braille_list.append(' ')
        else:
            translated = get_eng_char(braille_char, is_capital, is_number)
            braille_list.append(translated)
            is_capital = False


    return translation.join(braille_list)

def eng_to_braille(eng):
    """
    Translate english to braille
    Use the english dictionary
    """

    translation = []
    is_number = False

    for eng_char in eng:

        if eng_char.isupper():
            translation.append('.....O')
            translation.append(eng_dictionary[eng_char.lower()])
        elif eng_char.isdigit():
            if not is_number:
                translation.append('.O.OOO')
                is_number = True
            translation.append(eng_dictionary[eng_char])
        else:
            if is_number and eng_char == '.':
                translation.append(eng_dictionary['decimal follows'])
            else:
                translation.append(eng_dictionary[eng_char])
    
    return ''.join(translation)


def validate_braille(braille_string):
    # Check if the string contains only valid characters ('.' or 'O')
    if not all(c in '.O' for c in braille_string) or len(braille_string) % 6 != 0:
        return False
    
    return True

# Function to validate if a string is valid English
def validate_english(english_string):
    # Define valid characters (letters, spaces, and common punctuation)
    
    # Check each character in the string
    for char1 in english_string.lower():
        if char1.isalpha() and char1 not in eng_dictionary:
            # print(char1)
            return False
        elif char1 not in eng_dictionary:
            # print(char1)
            return False
    
    return True

# Main function
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert a Braille string (as 6-bit binary) to English.")
    
    # Add the argument for Braille input string
    parser.add_argument("user_input", type=str, help="The Braille string represented as 6-bit binary characters.")
    
    # Parse the arguments
    args = parser.parse_args()

    if validate_braille(args.user_input):
        english_output = braille_to_eng(args.user_input)
        print(english_output)
    elif validate_english(args.user_input):
        print(eng_to_braille(args.user_input))
    else:
        print("Invalid Text!")

