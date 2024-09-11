import sys
from english_to_braille_translator import translate_english_to_braille
from braille_to_english_translator import translate_braille_to_english

'''
Objective: Translate Braille or English into the other language
Attempt 1:
    - Create a Dictionary that maps English letters and numbers to the corresponding Braille pattern
    - Determine type of the input and translate accordingly
        - If input is English, translate to Braille. 
            - For each character, find its corresponding Braille pattern from the dictionary.
            - Handle capital letters by inserting the capital pattern before the letter
            - Handle numbers by inserting the number pattern before the beginning of the number sequence

        - If input is Braille, translate to English. 
            - Break the string into segments of six characters each and translate each segment.
            - Translate each Braille character back to English using the English to Braille dictionary
            - Note: 
                - English to Braille dictionary cannot contain both letter and number mappings due to duplicate keys.
'''

"""
    This method takes in a string (text) and returns a boolean indicating whether or not the string is a valid Braille sequence.
    A valid Braille sequence only contains the characters 'O' and '.'
    Args: 
        text (str): The string to check.

    Returns:
        bool: True if the string is a valid Braille sequence, False otherwise.     
"""
def is_braille(text: str) -> bool:
    # Get the set of unique characters in the given string
    text_char_set = set(text)

    '''
        Check if the set of characters in the given string is a subset of the set of valid Braille characters

        If the set of characters in the given string is a subset of the set of valid Braille characters, then the string 
        is a valid Braille sequence
    '''
    return text_char_set.issubset({"O", "."})


"""
    This function is the entry point into the program. It takes the arguments passed in on the command line, 
    determines if the input is a valid Braille sequence or an English string, and translates it to the other language.

    The function works as follows:

        1. Build a string from the command line arguments
        2. Check if the built string is a valid Braille sequence using the is_braille function
        3. If the string is a valid Braille sequence, translate it to English using the translate_braille_to_english function
        4. If the string is not a valid Braille sequence, translate it to Braille using the translate_english_to_braille function

"""
def main():
    input_str = ""
    
    # Build a string from the command line arguments
    for arg in sys.argv[1:]:
        input_str += arg + " "

    # Remove the trailing space from the built string
    input_str = input_str.rstrip()

    # Check if the built string is a valid Braille sequence
    if is_braille(input_str):
        # If the string is a valid Braille sequence, translate it to English
        print(translate_braille_to_english(input_str))
    else:
        # If the string is not a valid Braille sequence, translate it to Braille
        print(translate_english_to_braille(input_str))

if __name__ == "__main__":
    main()


