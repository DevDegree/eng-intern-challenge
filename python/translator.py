'''
Technical Eng Intern Challenge (Braille Translator) given by Shopify for their Winter Engineering Cohort, 2025.
Authored by Henry So (1ncipient)
'''

import argparse
from typing import List, Tuple

# Separate dictionaries as the digits 0-9 share the same pattern as the first ten letters of the alphabet in Braille.
ENGLISH_TO_BRAILLE_ALPHABET = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
    'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
    'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO", 'z': "O..OOO",

    '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.",
    ':': "..OO..", ';': "..O.O.", '-': "....OO", '/': ".O..O.",
    '<': ".OO..O", '>': "O..OO.", '(': "O.O..O", ')': ".O.OO.",
     
    ' ': "......",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO"
    }

NUMBER_TO_BRAILLE_ALPHABET = {
    '0': ".OOO..", '1': "O.....", '2': "O.O...", '3': "OO....",
    '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..",
    '8': "O.OO..", '9': ".OO..."
}
# Inverse dictionary to map Braille characters back to English characters.
BRAILLE_TO_ENGLISH_ALPHABET = {value: key for key, value in ENGLISH_TO_BRAILLE_ALPHABET.items()}
BRAILLE_TO_NUMBER_ALPHABET = {value: key for key, value in NUMBER_TO_BRAILLE_ALPHABET.items()}

# Braille characters are represented by a 6-dot pattern.
BRAILLE_CHARACTER_LENGTH = 6

# A set of characters that represent the character '.' in Braille.
BRAILLE_DECIMAL_REPRESENTATION = {ENGLISH_TO_BRAILLE_ALPHABET["decimal"], ENGLISH_TO_BRAILLE_ALPHABET['.']}

def main(input_strings: List[str]) -> None:
    """
    Controls the program flow. Arguments from the command line are translated accordingly and printed to the console.
    """

    # Stores tuples of the input_string and its corresponding language (should there be a mix of parameters both in English and Braille).
    translation_list = build_translation_list(input_strings)
    translated_output = append_translated_parameters(translation_list)
    
    print(translated_output, flush=True)

def build_translation_list(input_strings: List[str]) -> List[Tuple[str, str]]:
    """
    Translates all input strings to their corresponding languages.
    """
    translate_input = []

    for input_string in input_strings:
        language = check_input_language(input_string)
        translate_input.append((input_string, language))

    return translate_input

def append_translated_parameters(input_strings: List[Tuple[str, str]]) -> str:
    """
    Appends the translated output from the input strings. If we are translating from English to Braille, a Braille space is added between each string.
    """

    translated_output = []
    translate_to_braille = False
    BRAILLE_SPACE = "......"

    for tupled_input in input_strings:
        language = tupled_input[1]
        
        if language == "English":
            translate_to_braille = True
        
        translated_output.append(translate_input_string(tupled_input))

    if translate_to_braille:
        return BRAILLE_SPACE.join(translated_output)
        
    return "".join(translated_output)

def check_input_language(input_string: str) -> str:
    """
    Checks the language of an input string.
    """

    english = "English"
    braille = "Braille"

    # Edgecase: Since each character in the Braille system is represented by a 6-dot pattern, a valid Braille string must have a length that is a multiple of 6.
    if len(input_string) % 6 != 0:
        return english
    
    # Braille characters only consist of 'O' and '.' characters; return "english" otherwise.
    for char in input_string:
        if char not in {'O', '.'}:
            return english
        
    return braille
    
def translate_input_string(input: Tuple[str, str] ) -> str:
    """
    Translates an input string to its corresponding language.
    """

    # Tuple unpacking to get the input_string and its corresponding language.
    input_string, language = input

    if language == "English":
        return translate_english_to_braille(input_string)
    elif language == "Braille":
        return translate_braille_to_english(input_string)
    else:
        raise ValueError("Language not recognized / supported")
    
def translate_english_to_braille(english_string: str) -> str:
    """
    Returns a Braille string representation of an English string.
    """

    braille_string = ""
    previous_character = None

    # Return empty string if the input string is empty.
    if not english_string:
        return ""

    for character in english_string:
        if character.isupper():
            braille_string += ENGLISH_TO_BRAILLE_ALPHABET["capital"]
            braille_string += ENGLISH_TO_BRAILLE_ALPHABET[character.lower()]
        elif character.isdigit():
            # Edgecase: In Braille, a number indicator character precedes the number value to help distinguish it from the alphabet, as numbers share the same pattern as the first ten letters of the alphabet.
            # If it's the first occurrence of a digit, we append the number indicator character first.
            if previous_character is None or not previous_character.isdigit():
                braille_string += ENGLISH_TO_BRAILLE_ALPHABET["number"]
                braille_string += NUMBER_TO_BRAILLE_ALPHABET[character]
            else:
                braille_string += NUMBER_TO_BRAILLE_ALPHABET[character]
        elif character == '.':
            # Edgecase: In Braille, a decimal point does not typically start a sequence of characters, eg. ".59". Rather, it is preceded by a 'number' character, eg. "0.59".
            # Periods and decimal points read differently in Braille (this will provide more clarity for the visually impaired).
            if previous_character.isdigit():
                # Uses key '.' - For decimal points
                braille_string += ENGLISH_TO_BRAILLE_ALPHABET["decimal"]
            else:
                # Uses the period key - For periods
                braille_string += ENGLISH_TO_BRAILLE_ALPHABET[character]
        else:
            braille_string += ENGLISH_TO_BRAILLE_ALPHABET[character]

        previous_character = character
    
    return braille_string

def translate_braille_to_english(braille_string: str) -> str:
    """
    Returns an English string representation of a Braille string.
    """

    if not braille_string:
        return ""

    # List of Braille characters of length 6.
    braille_characters = split_braille_string(braille_string)
    english_string = ""
    current_index = 0
    braille_while_number = False

    while current_index < len(braille_characters):
        braille_character = braille_characters[current_index]
        # Check if the braille character is not within the set of Braille characters that represent numbers, and if so, set the flag that we are checking numbers to False, since we are no longer tracking numbers.
        if braille_character not in BRAILLE_TO_NUMBER_ALPHABET and braille_while_number:
            braille_while_number = False

        if braille_character == ENGLISH_TO_BRAILLE_ALPHABET["capital"]:
            # Skip index to get the next character as we know the following character is a capitalized letter.
            current_index += 1
            english_string += BRAILLE_TO_ENGLISH_ALPHABET[braille_characters[current_index]].upper()
        elif braille_character == ENGLISH_TO_BRAILLE_ALPHABET["number"]:
            # Skip index to get the next character as we know the following character is a number.
            current_index += 1
            english_string += BRAILLE_TO_NUMBER_ALPHABET[braille_characters[current_index]]
            # Set flag to True to indicate that we are checking numbers.
            braille_while_number = True
        elif braille_character in BRAILLE_DECIMAL_REPRESENTATION:
            english_string += "."
        else:
            if braille_while_number:
                english_string += BRAILLE_TO_NUMBER_ALPHABET[braille_character]
            else:
                english_string += BRAILLE_TO_ENGLISH_ALPHABET[braille_character]
        
        current_index += 1

    return english_string
        
def split_braille_string(braille_string: str) -> List[str]:
    """
    Helper method. Splits a Braille string into a list of Braille characters of length 6.
    """

    return [braille_string[i:i + BRAILLE_CHARACTER_LENGTH] for i in range(0, len(braille_string), BRAILLE_CHARACTER_LENGTH)]
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_strings", nargs='*', help="Input strings to be translated")
    args = parser.parse_args()

    main(args.input_strings)
