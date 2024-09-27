import sys
from constants import CHAR_TO_BRAILLE, BRAILLE_TO_CHAR, NUM_TO_BRAILLE, BRAILLE_TO_NUM, CAPITAL_FOLLOWS, NUMBER_FOLLOWS


def eng_to_braille(eng_string: str) -> str:
    """
    converts a string with English characters to Braille

    Args:
        eng_string (str): the English string to convert

    Returns:
        str: the converted Braille string
    """
    
    braille_string = ""
    in_number_mode = False
    
    for char in eng_string:
        
        if char.isupper():
            braille_string += CAPITAL_FOLLOWS + CHAR_TO_BRAILLE[char.lower()]

        elif char.isdigit():
            if not in_number_mode:
                braille_string += NUMBER_FOLLOWS
                in_number_mode = True
            braille_string += NUM_TO_BRAILLE[char]
            
        else:
            braille_string += CHAR_TO_BRAILLE[char.lower()]
            in_number_mode = False if char == ' ' else in_number_mode
    
    return braille_string


def braille_to_eng(braille_string: str) -> str:
    """
    converts a string with Braille characters to English

    Args:
        braille_string (str): the Braille string to convert

    Returns:
        str: the converted English string
    """
    
    eng_string = ""
    capital_follows = False
    number_follows = False
    
    for i in range(0, len(braille_string), 6):
        
        # get next 6 {'O', '.'} to determine English char
        braille_char = braille_string[i:i+6]
        
        if braille_char == CAPITAL_FOLLOWS:
            capital_follows = True
        
        elif braille_char == NUMBER_FOLLOWS:
            number_follows = True
        
        else:
            if number_follows:
                eng_string += BRAILLE_TO_NUM[braille_char]
            elif capital_follows:
                eng_string += BRAILLE_TO_CHAR[braille_char].upper()
                capital_follows = False
            elif BRAILLE_TO_CHAR[braille_char] == ' ':
                eng_string += BRAILLE_TO_CHAR[braille_char]
                number_follows = False
            else:
                eng_string += BRAILLE_TO_CHAR[braille_char]
    
    return eng_string


def is_braille(input_string: str) -> bool:
    """
    checks if a string is Braille

    Args:
        input_string (str): the string to check

    Returns:
        bool: True if the string is Braille, False otherwise
    """
    
    # each Braille character is 6 characters long
    if len(input_string) % 6 != 0:
        return False
    
    # each element in a Braille character is either 'O' or '.'
    for char in input_string:
        if char not in {'O', '.'}:
            return False
    
    return True


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <string>")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    
    
    if is_braille(input_string):
        print(braille_to_eng(input_string))
    else:
        print(eng_to_braille(input_string))

