import sys
from collections import defaultdict

# Braille dictionary mappings
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',

    ' ': '......',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', '-': 'OOOO..',
    ':': '..OO..', ';': '..O.O.', '/':'.O..O.', '<' : '.OO..O', '>':'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'num_follows' : '.O.OOO', 'capital_follows': '.....O', "decimal_follows":".O...O"
}

braille_to_english = defaultdict(list)
for char, braille in english_to_braille.items():
    braille_to_english[braille].append(char)

def isBraille(input_string: str) -> bool:
    """
    Checks if the input string is a valid Braille representation.

    Parameters:
        input_string (str): A string representing Braille characters.

    Returns:
        bool: True if the input string consists only of valid Braille characters ('O' or '.'), False otherwise.
    """
    return all(char in 'O.' for char in input_string)


def isEnglish(input_str: str) -> bool:
    """
    Checks if the input string is valid English text.

    Parameters:
        input_str (str): A string representing English text.

    Returns:
        bool: True if the input string consists only of valid English characters 
              (letters, digits, and punctuation defined in the English-to-Braille mapping), 
              False otherwise.
    """
    if isBraille(input_str):
        return False
    input_str = input_str.lower()
    valid_english_chars = set(english_to_braille.keys())
    return all(c in valid_english_chars for c in input_str)

def translate(input_string: str):
    """
    Determine the type of input (Braille or English) and convert it accordingly.
    
    Parameters:
        input_string (str): The input string in Braille or English.
    
    Returns:
        str: Translated output or an error message if the input is invalid.
    """
    if isBraille(input_string) and len(input_string) % 6 == 0:
        return braille_to_english_converter(input_string)
    elif isEnglish(input_string):
        return english_to_braille_converter(input_string)
    else:
        return "Error: Invalid input. Please enter valid English text or Braille representation."

def braille_to_english_converter(braille_string: str) -> str:
    """
    Converts a Braille string into English.

    Parameters:
        braille_string (str): A string representing Braille characters.

    Returns:
        str: The converted English text or an error message if the Braille is invalid.
    """
    output = []
    i = 0
    is_number = False
    capitalize_next = False

    while i < len(braille_string):
        braille_char = braille_string[i:i+6]

        if braille_char == '.....O':  # Capital follows symbol
            capitalize_next = True
            i += 6
            continue
        elif braille_char == '.O.OOO':  # Number follows symbol
            is_number = True
            i += 6
            continue
        elif braille_char == '......':  # Space
            output.append(' ')
            is_number = False
            capitalize_next = False
            i += 6
            continue

        if braille_char in braille_to_english:
            char_list = braille_to_english[braille_char]
            if is_number:
                char = next((c for c in char_list if c.isdigit()), None)
                if char is None:
                    return "Error: Invalid Braille representation for number."
            else:
                char = char_list[0]

            if capitalize_next:
                char = char.upper()
                capitalize_next = False

            output.append(char)
            i += 6
        else:
            return "Error: Invalid Braille representation."

    return ''.join(output).strip()


def english_to_braille_converter(english_string: str):
    """
    Converts an English string into Braille.
    
    Parameters:
        english_string (str): A string in English to be converted to Braille.
    
    Returns:
        str: The converted Braille representation or an error message if the English input is invalid.
    """
    output = []
    num_mode = False

    for char in english_string:
        if char == ' ':
            output.append(english_to_braille[' '])
            num_mode = False
        elif char.lower() in english_to_braille:
            if char.isdigit():
                if not num_mode:
                    output.append(english_to_braille['num_follows'])
                    num_mode = True
                output.append(english_to_braille[char])
            else:
                if char.isupper():
                    output.append(english_to_braille['capital_follows'])
                    char = char.lower()
                elif num_mode:
                    output.append(english_to_braille['num_follows'])
                    num_mode = False
                output.append(english_to_braille[char])
        else:
            return "Error: Invalid character."

    return ''.join(output)

if __name__ == "__main__":
    description = """
    Braille to English Converter and Vice Versa
    -------------------------------------------
    This program allows you to convert Braille text to English and vice versa.
    Currently, decimal numbers are not fully supported, and the conversion may 
    not handle them correctly.

    Usage:
    - To run the program, provide the text you want to convert as an input argument.
    - For example:
        python3 translator.py O.....O.O...OO....    # Converts Braille to English
        python3 translator.py abc                     # Converts English to Braille

    - Alternatively, you can enter your text directly when prompted.
    """
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        result = translate(input_text)
        print(result)
    else:
        print(description)
        input_text = input("Please provide an input argument: ")
        print(translate(input_text))
