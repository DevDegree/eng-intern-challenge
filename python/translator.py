import sys

# Braille & English mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'CAP_follows', '.O...O':'Decimal_follows',
    '.O.OOO': 'NUM_follows', '..OO.O':'.','..O...':',',
    '..O.OO':'?','..OOO.':'!','..OO..':':','..O.O.':';','....OO':'-',
    '.O..O.':'/','.OO..O':'<','':'>','O.O..O':'(','.O.OO.':')','......': ' '
}
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Numbers & Braille 
number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Functions

def is_braille(input_string):
    # Ensure input only contains O, ., or space, and the length is a multiple of 6
    braille_chars = input_string.replace(' ', '')
    return all(c in ['O', '.'] for c in braille_chars) and len(braille_chars) % 6 == 0

def braille_to_english_translator(braille_text):
    words = braille_text.split(' ')
    result = []
    capitalize_next = False
    is_number = False

    for word in words:
        for i in range(0, len(word), 6):
            braille_char = word[i:i + 6]
            if braille_char == '.....O':  # Capital letter indicator
                capitalize_next = True
                continue
            elif braille_char == '.O.OOO':  # Number indicator
                is_number = True
                continue

            if is_number:
                # Convert braille to number if the number indicator is active
                result.append(list(number_to_braille.keys())[list(number_to_braille.values()).index(braille_char)])
                continue  # Continue without resetting is_number here
            elif capitalize_next:
                # Capitalize the next letter after the capital indicator
                result.append(braille_to_english[braille_char].upper())
                capitalize_next = False
            else:
                # Regular letter or space
                result.append(braille_to_english.get(braille_char, ' '))

        result.append(' ')  # Add a space between words

        # After a word ends, reset number indicator
        is_number = False

    return ''.join(result).strip()

def english_to_braille_translator(english_text):
    result = []
    number_mode = False  # To track if we are in number mode

    for char in english_text:
        if char.isdigit():
            if not number_mode:
                result.append('.O.OOO')  # Number indicator 
                number_mode = True  # number mode On
            result.append(number_to_braille[char])
        elif char.isupper():
            number_mode = False  # number mode Off
            result.append('.....O')  # Capital letter 
            result.append(english_to_braille[char.lower()])
        elif char == ' ':
            number_mode = False  # Reset number mode on space
            result.append('......')  # Space
        elif char in english_to_braille:
            number_mode = False  # number mode Off when switching to letters or other chars
            result.append(english_to_braille[char])
        else:
            # Handle special characters
            if char == '.':
                result.append('.O...O')  
            elif char == ',':
                result.append('..O...')  
            elif char == '?':
                result.append('..O.OO')  
            elif char == '!':
                result.append('..OOO.')  
            elif char == ':':
                result.append('..OO..')  
            elif char == ';':
                result.append('..O.O.')  
            elif char == '-':
                result.append('....OO')  
            elif char == '/':
                result.append('.O..O.')  
            elif char == '<':
                result.append('.OO..O')  
            elif char == '>':
                result.append('O..OOO')  
            elif char == '(':
                result.append('O.O..O')  
            elif char == ')':
                result.append('.O.OO.')  
            else:
                # Ignore other chars
                continue


    return ' '.join(result).strip()  

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        return

    input_string = sys.argv[1]

    if is_braille(input_string):
        print(braille_to_english_translator(input_string))
    else:
        print(english_to_braille_translator(input_string))

if __name__ == "__main__":
    main()
