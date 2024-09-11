
# Created By: Ben Fisher
# Date: August 29, 2024
#
# This script is designed to solve the Shopify Winter 2025 Eng intern challenge
# It incorporates all technical aspects required, it does not include any implementation of decimal follows nor punctuation
# as functionality was only specified to a-z, A-Z, 0-9, and spaces
import sys
from braille_constants import braille_capital, braille_number, num_dict, alpha_dict


def isEnglish(base_line):
    # Purpose: Determine if a string is english or braille format
    # Parameters: base_line (string) - line to determine format
    # Returns: True - base_line is english, False - base_line is braille
    for character in base_line:
        if character != 'O' and character != '.':
            return True
    return False

def englishToBraille(base_line):
    # Purpose: Convert english text to braille code, including a-z, 0-9, A-Z and spaces
    # Parameters: base_line (string) - english line to convert to braille
    # Returns: braille_string - a string containing translated braille text
    braille_string = ""

    current_number = False
    for character in base_line:
        if character.isupper():
            # Need to signify uppercase and print the lower case version
            braille_string += braille_capital
            braille_string += alpha_dict.get(character.lower())
            continue

        elif character.isnumeric():
            # Need to signify number if not signified and convert 1-9 to 'a'-'k' and 0 to 'l'
            if current_number == False:
                braille_string += braille_number
                current_number = True

            braille_string += num_dict.get(character)
            continue

        if character == " ":
            # Exiting number sequence, reset flag
            current_number = False

        braille_string += alpha_dict.get(character)

    return braille_string



def brailleToEnglish(base_line):
    # Purpose: Convert braille code to english text, successfully converts a-z, 0-9, A-Z and spaces
    # Parameters: base_line (string) - braille code to convert to english
    # Returns: english_string -  a string containing translated english text
    english_string = ""

    is_capital = False
    is_number = False

    for i in range(0,len(base_line),6):
        pattern = base_line[i:i+6]
        
        # Check for flags
        if pattern == braille_capital:
            is_capital = True
            continue
        elif pattern == braille_number:
            is_number = True
            continue

        # Determine if number pattern ended
        if pattern == alpha_dict[' ']:
            is_number = False

        if is_number:
            english_string += list(num_dict.keys())[list(num_dict.values()).index(pattern)]
        else:
            english_char = list(alpha_dict.keys())[list(alpha_dict.values()).index(pattern)]
            
            # Check for Capital
            if is_capital:
                is_capital = False
                english_char = english_char.upper()

            english_string += english_char

    return english_string
    


def main(base_line):
    # Loop through arguements and add spaces between each argument
    english = isEnglish(base_line)
    if english:
        print(englishToBraille(base_line), end='')
    else:
        print(brailleToEnglish(base_line), end='')
    

if __name__ == "__main__":
    main(' '.join(sys.argv[1:]))
    