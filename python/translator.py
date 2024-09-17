import sys

# Braille codes for letters
braille_letters = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

braille_nums = {
    '1': 'O.....',  # a
    '2': 'O.O...',  # b
    '3': 'OO....',  # c
    '4': 'OO.O..',  # d
    '5': 'O..O..',  # e
    '6': 'OOO...',  # f
    '7': 'OOOO..',  # g
    '8': 'O.OO..',  # h
    '9': '.OO...',  # i
    '0': '.OOO..',  # j
}

# Braille special symbols
capital_sign = '.....O'
number_sign = '.O.OOO'
space_sign = '......'

# Reverse mappings for decoding
braille_to_letter = {v: k for k, v in braille_letters.items()}
braille_to_digit = {v: k for k, v in braille_nums.items()}

def braille_to_english(braille_text):
    """
    Translates Braille text to English.
    """
    output = ''
    number_mode = False  # Indicates if we're currently in number mode
    capital_next = False  # Indicates if the next letter should be capitalized

    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    i = 0
    while i < len(braille_chars):
        symbol = braille_chars[i]
        if symbol == space_sign:
            # Add space and reset modes
            output += ' '
            number_mode = False
            capital_next = False
            i += 1
        elif symbol == capital_sign:
            # Next letter should be capitalized
            capital_next = True
            i += 1
        elif symbol == number_sign:
            # Enter number mode
            number_mode = True
            i += 1
        else:
            if number_mode:
                # In number mode, symbols correspond to digits
                if symbol in braille_to_digit:
                    output += braille_to_digit[symbol]
                else:
                    pass # Invalid

            else:
                # Symbols correspond to letters
                if symbol in braille_to_letter:
                    letter = braille_to_letter[symbol]

                    if capital_next:
                        letter = letter.upper()
                        capital_next = False

                    output += letter
                else:
                    pass # Invalid
            i += 1

    return output

def is_braille(text):
    """
    Determines if the input text is Braille.
    """
    return all(c in ('O', '.') for c in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <text>')
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        # Convert Braille to English
        output_text = braille_to_english(input_text)
    else:
        # Convert English to Braille
        print("Braille")

    print(output_text)

if __name__ == '__main__':
    main()
