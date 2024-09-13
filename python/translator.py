import sys

braille_to_letter = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    # Special symbols
    '.....O': 'capital',  # Capital follows
    '.O.OOO': 'number',   # Number follows
    '......': ' ',        # Space
}

braille_to_digit = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# English to Braille mapping (reverse of braille_to_letter and braille_to_digit)
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    # Numbers 0-9 (same patterns as a-j in Braille numbers mode)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    # Special symbols
    ' ': '......',         # Space
    'capital': '.....O',   # Capital follows
    'number': '.O.OOO',    # Number follows
}

def is_braille(input_string):
    return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0

def translate_braille_to_english(braille_string):
    result = []
    i = 0
    capitalize = False
    number_mode = False

    while i < len(braille_string):
        chunk = braille_string[i:i+6]

        # Handle special Braille symbols
        if chunk == '.....O':  # Capitalize next letter
            capitalize = True
        elif chunk == '.O.OOO':  # Number follows
            number_mode = True
        elif chunk == '......':  # Space
            result.append(' ')
            number_mode = False  # Reset number mode after a space
        else:
            if number_mode:
                # Use digit mapping
                letter = braille_to_digit.get(chunk, '')
                if letter == '':
                    # If not a digit, exit number mode and process as letter
                    number_mode = False
                    letter = braille_to_letter.get(chunk, '')
            else:
                # Use letter mapping
                letter = braille_to_letter.get(chunk, '')

            # Handle capitalization
            if capitalize and letter.isalpha():
                letter = letter.upper()
                capitalize = False  # Reset capitalization after applying it

            result.append(letter)

        i += 6  # Move to the next Braille cell (6 characters at a time)

    return ''.join(result)

def translate_english_to_braille(english_string):
    result = []
    number_mode = False

    for char in english_string:
        if char.isupper():
            result.append('.....O')  # Capital follows
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                result.append('.O.OOO')  # Number follows
                number_mode = True
            result.append(english_to_braille[char])
        else:
            if number_mode:
                # Exit number mode
                number_mode = False
            result.append(english_to_braille.get(char, ''))

    return ''.join(result)

def main():
    input_strings = sys.argv[1:]
    output = ''
    for idx, input_string in enumerate(input_strings):
        if is_braille(input_string):
            output += translate_braille_to_english(input_string)
        else:
            output += translate_english_to_braille(input_string)
        if idx < len(input_strings) - 1:
            # Add Braille space between translations
            output += '......'  # Braille space
    print(output)


if __name__ == "__main__":
    main()

