
# Python version 3.8
import sys

from utils import *

def translate_to_braille(input_str: str) -> str:
    """
    Translate an input string to Braille.
    """
    result = []
    number_mode = False
    for char in input_str:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_FOLLOWS)
                number_mode = True
            result.append(braille_alphabet.get(char, ''))

        elif char.isalpha():
            if char.isupper():
                result.append(CAPITAL_FOLLOWS)
                char = char.lower()
            number_mode = False
            result.append(braille_alphabet.get(char, ''))

        elif char == ' ':
            result.append(SPACE)
            number_mode = False
    return ''.join(result)



def translate_to_english(braille_input: str) -> str:
    """
    Translate a Braille string to English.
    """
    output = []
    is_capital = False
    is_number = False
    i = 0

    while i < len(braille_input):
        braille_char = braille_input[i:i+6]
        i += 6

        if braille_char == CAPITAL_FOLLOWS:
            is_capital = True
            continue
        
        if braille_char == NUMBER_FOLLOWS:
            is_number = True
            continue

        if braille_char == SPACE:
            output.append(' ')
            is_number = False
            continue

        if is_number:
            digit = braille_to_number(braille_char)
            output.append(digit)
            is_number = False  # End number mode after processing the digit
        else:
            letter = braille_to_letter(braille_char)
            if letter == '?':
                output.append('?')  # Handle unrecognized Braille symbols
            else:
                if is_capital:
                    letter = letter.upper()
                    is_capital = False
                output.append(letter)
    
    return ''.join(output)

def braille_translator(input_str: str) -> str:
    if is_braille(input_str):
        return translate_to_english(input_str)

    return translate_to_braille(input_str)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
        print(braille_translator(input_str))
    else:
        print("Please provide an input string.")
