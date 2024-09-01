import argparse

DECIMAL = 'decimal follows'
CAPITAL = 'capital follows'
NUMBER = 'number follows'

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',

    '.....O': CAPITAL, '.O...O': DECIMAL, 
    '.O.OOO': NUMBER, '......': ' ',

    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';',
    '....OO': '-', '.O..O.' : '/', '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')'
}

# Braille has the same key for Numbers as with some letters
BRAILLE_TO_NUMERIC = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    'O..OO.': '>',
}

# Automatically generate English To Braille, except special cases.
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
ENGLISH_TO_BRAILLE.update({v:k for k, v in BRAILLE_TO_NUMERIC.items()})


def read_input():
    parser = argparse.ArgumentParser(
        description="Braille-English Translator: Translates Braille to English and vice versa."
    )
    
    # Positional argument for the input string
    parser.add_argument(
        'input_string',
        metavar='Input',
        type=str,
        nargs='+',
        help='The input text to translate (either Braille or English).'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose mode for detailed output.'
    )
    
    args = parser.parse_args()
    input_string = ' '.join(args.input_string)
    return input_string

def is_braille(input_string):
    """
    Determine if the input string is Braille based on the presence of only valid Braille characters.
    Braille consists only of characters 'O', '.'
    Handles ambiguity between English and Braille based on string length being divisible by 6.
    
    Args:
    - input_string (str): The input string to check.
    
    Returns:
    - bool: True if input is likely Braille, False otherwise.
    """
    valid_braille_chars = set('O.')
    may_be_braille = all(char in valid_braille_chars for char in input_string)
    length_divisible_by_six = ((len(input_string) % 6) == 0)
    is_english_since_has_spaces = (" " in input_string)

    # If a string may be braille and it is divisible by 6, we assume it is braille.
    # This handles edge cases of english/braille, such as 0.0 being English. 
    # NOTE: There are cases of ambiguity, such as 0.0000 being English OR Braille. 
    return (may_be_braille and length_divisible_by_six) and (not is_english_since_has_spaces)

def english_to_braille(english_input):
    """
    Translate English text to Braille.
    
    Args:
    - english_input (str): A string representing English text.
    
    Returns:
    - str: The translated Braille text.
    """
    braille_output = []
    number_mode = False

    for char in english_input:
        # Handle number_mode.
        if char == "." and number_mode:
          braille_output.append(ENGLISH_TO_BRAILLE[DECIMAL])
          continue
        elif char.isdigit():
          if not number_mode:
              braille_output.append(ENGLISH_TO_BRAILLE[NUMBER])
              number_mode = True
        else:
          number_mode = False
            
        # Handle uppercase.
        if char.isupper():
          braille_output.append(ENGLISH_TO_BRAILLE[CAPITAL])
          char = char.lower()

        try:
          braille_output.append(ENGLISH_TO_BRAILLE[char])
        except KeyError as e:
          continue
            
        
    return ''.join(braille_output)

def braille_to_english(braille_input):
    """
    Translate Braille to English text.
    
    Args:
    - braille_input (str): A string representing Braille with 'O' for raised dots and '.' for non-raised dots.
    
    Returns:
    - str: The translated English text.
    """
    BRAILLE_CHAR_LENGTH = 6
    braille_length = len(braille_input)
    
    # NOTE: Expected to have received true from is_braille, which ensure length is divisible by 6.
    braille_chars = [braille_input[i:i+BRAILLE_CHAR_LENGTH] for i in range(0, braille_length, BRAILLE_CHAR_LENGTH)]
    
    
    capital_next = False
    number_mode = False
    english_output = []

    for braille_char in braille_chars:
        if braille_char not in BRAILLE_TO_ENGLISH:
            continue  # Skip any invalid characters

        if number_mode:
            english_char = BRAILLE_TO_NUMERIC[braille_char]
        else:
            english_char = BRAILLE_TO_ENGLISH[braille_char]
        
        # Handle control characters
        if english_char == 'capital follows':
           capital_next = True
           continue
    
        if english_char == 'number follows':
           number_mode = True
           continue

        if english_char == 'decimal follows':
            english_output.append('.')
            continue
        
        # Continue regular handling, since control follows skipped.
        if capital_next:
            english_char = english_char.upper()
            capital_next = False
        
        # If non-digit (such as a space), we stop number mode.
        if number_mode and english_char.isdigit():
            english_output.append(english_char)
        else:
            number_mode = False
            english_output.append(english_char)

    return ''.join(english_output)


def main():
    input_string = read_input()
    convert = braille_to_english if is_braille(input_string) else english_to_braille
    output = convert(input_string)
    print(output)

if __name__ == "__main__":
    main()