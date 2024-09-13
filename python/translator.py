import sys

from utils.constants import (
    ENGLISH_TO_BRAILLE_ALPHABET, 
    ENGLISH_TO_BRAILLE_DIGITS, 
    ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS, 
    BRAILLE_TO_ENGLISH_ALPHABET, 
    BRAILLE_TO_ENGLISH_DIGITS, 
    BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS,
    CAPITAL_FOLLOWS,
    NUMBER_FOLLOWS,
    BRAILLE_CHARACTER_LENGTH
)
from utils.helpers import does_have_unsupported_english_characters, is_braille

def translate_english_to_braille(english_string):
    braille_string_result = []
    in_number_mode = False
    braille_number_follows = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[NUMBER_FOLLOWS]
    braille_capital_follows = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[CAPITAL_FOLLOWS]
    braille_space_character = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[' ']

    for char in english_string:
        if char.isdigit():
            if not in_number_mode:
                braille_string_result.append(braille_number_follows)
                in_number_mode = True
            braille_string_result.append(ENGLISH_TO_BRAILLE_DIGITS[char])

        elif char.isalpha():
            if char.isupper():
                braille_string_result.append(braille_capital_follows)
                char = char.lower() 
            braille_string_result.append(ENGLISH_TO_BRAILLE_ALPHABET[char])

        elif char == ' ':
            braille_string_result.append(braille_space_character)
            in_number_mode = False

        else:
            braille_string_result.append(ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[char])

    return ''.join(braille_string_result)


def translate_braille_to_english(braille_string):
    english_string_result = []
    is_next_capital = False 
    in_number_mode = False 
    braille_number_follows = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[NUMBER_FOLLOWS]
    braille_capital_follows = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[CAPITAL_FOLLOWS]
    braille_space_character = ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[' ']

    i = 0
    while i < len(braille_string):
        braille_char = braille_string[i:i + BRAILLE_CHARACTER_LENGTH]

        if braille_char == braille_number_follows:
            in_number_mode = True
            i += BRAILLE_CHARACTER_LENGTH
            continue

        if braille_char == braille_capital_follows:
            is_next_capital = True
            i += BRAILLE_CHARACTER_LENGTH
            continue
        
        if braille_char == braille_space_character:
            english_string_result.append(' ')
            in_number_mode = False
            i += BRAILLE_CHARACTER_LENGTH
            continue

        if in_number_mode:
            if braille_char in BRAILLE_TO_ENGLISH_DIGITS:
                english_string_result.append(BRAILLE_TO_ENGLISH_DIGITS[braille_char])
            else:
                # If got here, the Braille input is not valid
                return "Invalid Braille string input. Character is not a number"
        else:
            # We know that character has to be either a 
            if braille_char in BRAILLE_TO_ENGLISH_ALPHABET:
                letter = BRAILLE_TO_ENGLISH_ALPHABET[braille_char]
                if is_next_capital:
                    letter = letter.upper()
                    is_next_capital = False
                english_string_result.append(letter)
            elif braille_char in BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS:
                english_string_result.append(BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS[braille_char])
                # need to ensure that a character after special character doesn't get capitalized
                is_next_capital = False
            else:
                return "Invalid Braille string input. Character is not a special character or a letter" 

        i += BRAILLE_CHARACTER_LENGTH

    return ''.join(english_string_result)


def main():
    if len(sys.argv) < 2:
        print("Incorrect input. Passed arguments don't contain a string to translate")
        return

    # This collapses spaces (i.e. ... Hello    world -> Hello world)
    # To preserve spacing, pass the string in quotes (i.e "Hello    world")
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        if (len(input_string) % BRAILLE_CHARACTER_LENGTH != 0):
            print("Incorrect input. Passed Braille string is malformed, incorrect number of characters")
            return

        print(translate_braille_to_english(input_string))
    else:
        # Since not Braille, need to check if the string contains invalid characters for English alphabet. 
        if (does_have_unsupported_english_characters(input_string)):
            print("Incorrect input. Passed english string contains invalid characters")
            return
        else:  
            print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()
