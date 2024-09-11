from utils import BRAILLE_DICT

"""
Translate a given string from English to Braille.

Args:
    input_string (str): The string to translate from English to Braille.

Returns:
    str: The Braille translation of the input string.
"""
def translate_english_to_braille(input_string: str) -> str:
    """
    Translate a given string from English to Braille.

    Args:
        input_string (str): The string to translate from English to Braille.

    Returns:
        str: The Braille translation of the input string.
    """
    # Initialize an empty list to store the Braille pattern
    braille_pattern_list = []
    
    # Keep track of whether the previous character was a digit
    number_mode = False
    
    # Iterate over each character in the given string
    for current_character in input_string:
        # If the character is an uppercase letter, insert the capital symbol and change the character to lowercase
        if current_character.isupper():
            braille_pattern_list.append(BRAILLE_DICT["capital"])
            current_character = current_character.lower()
        
        # If the character is a digit, insert the number symbol if it is not already inserted
        if current_character.isdigit():
            # If the previous character was not a digit, insert the number symbol
            if not number_mode:
                braille_pattern_list.append(BRAILLE_DICT["number"])
                number_mode = True
        else:
            # If the character is not a digit, set number_mode to False
            number_mode = False
        
        # Append the Braille pattern for the character to the Braille pattern list
        braille_pattern_list.append(BRAILLE_DICT.get(current_character, "CHARACTER NOT FOUND"))
    
    # Join all the Braille patterns in the list into one string and return it
    return "".join(braille_pattern_list)