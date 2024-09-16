
"""
This script translates between English and Braille. It detects the language and performs the translation.

Functions:
    - detect_language(input_text): Detects whether the input is in English or Braille.
    - translate_english(input_text): Translates English text to Braille.
    - translate_braille(input_text): Translates Braille notation to English text.
    - translate(input_text): Automatically detects and translates between English and Braille.
    - main(): Command-line interface for translating text.

Limitations:
    - The example Braille aplhabet provided lacks a 'letter sign' character.
    - It also must assume that when `num` is present, the following characters are numbers.
    - Therefore, translation to English cannot handle cases where letters follow numbers.
    - Translation to Braille treats a section with one period and only numbers as a decimal.
    - Ex: '1.1a' to Braille will not be considered a decimal; each number will use a `num` indicator.
"""

import argparse
import re

braille_alphabet = {
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
    'cap': '.....O',  # Capital follows
    'num': '.O.OOO',  # Number follows
    'dec': '.O...O',  # Decimal follows
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',    
    '.': '..OO.O', # Period
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'  # Space
}

# Create a reverse dictionary to map Braille characters to English characters.
# This is used for faster querying of Braille characters during translation.

reverse_braille_alphabet = {}
for k, v in braille_alphabet.items():
    if v not in reverse_braille_alphabet:
        reverse_braille_alphabet[v] = []
    reverse_braille_alphabet[v].append(k)

def detect_language(input_text):
    """
    Detects whether the input text is English or Braille.
    Returns 'english' if any character other than '.' or 'O' is found, otherwise returns 'braille'.
    Trims any empty spaces from the input text.
    """
    trimmed_text = input_text.strip()
    trimmed_text = trimmed_text.replace(" ", "")
    valid_braille_chars = {'.', 'O'}
    input_chars = set(trimmed_text)
    
    # Check if there are any characters in the input that are not valid Braille characters
    if input_chars - valid_braille_chars:
        return 'english'
    return 'braille'

def is_valid_float(section):
    """
    Check if the given section represents a valid float.
    """
    parts = section.split('.')
    return len(parts) == 2 and all(part.isnumeric() for part in parts)

def translate_english(input_text):
    """
    Translates English characters into Braille.
    """
    braille_translation = []
    sections = re.split(r'(\s+)', input_text)
    
    for section in sections:
        section_result = []
        for i, char in enumerate(section):

            if char.isupper():  # Handle uppercase letters
                section_result.append(braille_alphabet['cap'])
                char = char.lower()
                section_result.append(braille_alphabet.get(char, ''))

            elif char.isnumeric():  # Handle numeric characters
                
                if i == 0 or (not section[i - 1].isnumeric() and not is_valid_float(section)):
                    section_result.append(braille_alphabet['num'])
                section_result.append(braille_alphabet.get(char, ''))

            elif char == '.' and is_valid_float(section):  # Handle decimal points
                section_result.append(braille_alphabet['dec'])

            else: # Handle all other characters
                section_result.append(braille_alphabet.get(char, ''))

        braille_translation.append(''.join(section_result))

    return ''.join(braille_translation)

def translate_braille(input_text):
    """
    Translates Braille characters into English.
    """

    # Error handling for lenght of input_text
    if len(input_text) % 6 != 0:
        return "Braille input lenght not divisible by 6. Check input and try again."

    english_translation = []
    # Split the input text into chunks of 6 characters each, representing Braille characters
    characters = [input_text[i:i+6] for i in range(0, len(input_text), 6)] 
    num_mode = False
    cap_next = False

    for char in characters:
        if char == braille_alphabet['cap']:
            cap_next = True
        elif char == braille_alphabet['num']:
            num_mode = True
        elif char == braille_alphabet['dec']:
            english_translation.append('.')
        else:
            possible_keys = reverse_braille_alphabet.get(char, [])
            
            for symbol in possible_keys:
                if num_mode:
                    if symbol.isnumeric():
                        english_translation.append(symbol)
                        break
                    if not symbol.isalpha():
                        english_translation.append(symbol)
                        num_mode = False  # Reset num_mode for non-numbers
                        break
                else:
                    if symbol.isalpha():
                        english_translation.append(symbol.upper() if cap_next else symbol)
                        cap_next = False  # Reset cap_next after first occurrence
                        break
                    else:
                        english_translation.append(symbol)
                        break

    return ''.join(english_translation)

def translate(input_text):
    """
    Detects the language of the input text and translates it accordingly.
    """
    detected_language = detect_language(input_text)
    if detected_language == 'braille':
        return translate_braille(input_text)
    return translate_english(input_text)

def main():
    """
    Main function to handle the argument parsing and translation logic.
    """
    parser = argparse.ArgumentParser(description="Translate between English and Braille.")
    parser.add_argument('input_text', nargs='*', help="The text to be translated.")
    args = parser.parse_args()
    
    input_text = ' '.join(args.input_text)
    translated_text = translate(input_text)
    print(translated_text)

if __name__ == "__main__":
    main()
