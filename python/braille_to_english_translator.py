from utils import BRAILLE_DICT, ENGLISH_DICT
"""
    Translate a given Braille string to English.

    Args:
        braille_string (str): The Braille string to translate from Braille to English.

    Returns:
        str: The English translation of the input Braille string.
"""
def translate_braille_to_english(braille_string: str) -> str:
    # Initialize an empty list to store the English characters
    english_characters = []
    
    # Initialize a variable to keep track of whether the previous character was a digit
    number_mode = False
    
    # Iterate over each 6-character sequence in the given Braille string
    i = 0
    while i < len(braille_string):
        # If the current character sequence is the capital symbol, uppercase the next character
        if braille_string[i:i+6] == BRAILLE_DICT["capital"]:
            i += 6
            char = ENGLISH_DICT[braille_string[i:i+6]].upper()
        # If the current character sequence is the number symbol, set number_mode to True
        elif braille_string[i:i+6] == BRAILLE_DICT["number"]:
            number_mode = True
            i += 6
            continue
        # If the current character sequence is the space symbol, set number_mode to False
        elif braille_string[i:i+6] == BRAILLE_DICT[" "]:
            number_mode = False
            char = " "
        else:
            # Get the English character corresponding to the current Braille character
            char = ENGLISH_DICT.get(braille_string[i:i+6], "")

            # Check if we are still interpreting in number_mode. 
            # If we are, we have to convert the english letter to the corresponding ASCI number
            if number_mode:
                char = str(ord(char) - ord('a') + 1)

                # Correct mapping for '0' by replacing '10' with '0'
                if char == '10':
                    char = '0'

        # Append the English character to the list
        english_characters.append(char)

        # Increment the index to move to the next Braille character
        i += 6

    # Join all the English characters in the list into one string and return it
    return "".join(english_characters)