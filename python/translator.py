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
    number_mode = False
    capital_next = False

    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    # Loop through each Braille symbol
    for symbol in braille_chars:
        # Translate Braille space sign to English space
        if symbol == space_sign:
            output += ' '
            number_mode = False
            capital_next = False
            continue

        if symbol == capital_sign:
            capital_next = True
            continue

        if symbol == number_sign:
            number_mode = True
            continue

        if number_mode:
            # Translate Braille digits when in number mode
            char = braille_to_digit.get(symbol)
            if char:
                output += char
            else:
                pass # Invalid
            continue # Continue to next Braille symbol

        # Translate Braille letters to English letters
        char = braille_to_letter.get(symbol)
        if char:
            if capital_next:
                char = char.upper()
                capital_next = False
            output += char
        else:
            pass # Invalid

    return output

def english_to_braille(text):
    """
    Translates English text to Braille.
    """
    output = ''
    number_mode = False

    # Loop through each character in the input text
    for char in text:
        if char == ' ':
            # Translate space to Braille space sign
            output += space_sign
            number_mode = False
            continue

        if char.isdigit():
            # Enter number mode if a digit is encountered
            if not number_mode:
                output += number_sign
                number_mode = True
            output += braille_nums[char]
            continue

        if char.isalpha():
            # Exit number mode when encountering a letter
            if number_mode:
                number_mode = False
            # Add capital sign if the letter is uppercase
            if char.isupper():
                output += capital_sign
            output += braille_letters[char.lower()]
            continue

        continue # Ignore non-alphanumeric characters

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
        output_text = english_to_braille(input_text)

    print(output_text)

if __name__ == '__main__':
    main()
