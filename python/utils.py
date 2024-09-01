from consts import INVALID_BRAILLE_STRING, BRAILLE_TO_ENGLISH_DICT, BRAILLE_TYPE, ENGLISH_TYPE, ENGLISH_CHARS, UNKNOWN_TYPE, BRAILLE_TO_NUMBER_DICT, BRAILLE_TO_SPECIAL_DICT, BRAILLE_CAPITAL_FOLLOWS, BRAILLE_NUMBER_FOLLOWS

def is_valid_braille_string(input_string):
    """
    Check if the given input string is a valid Braille string.
    """
    braille_chars = set(BRAILLE_TO_ENGLISH_DICT.keys())
    braille_numbers = set(BRAILLE_TO_NUMBER_DICT.keys())
    braille_special = set(BRAILLE_TO_SPECIAL_DICT.keys())
    special_cases = {BRAILLE_CAPITAL_FOLLOWS, BRAILLE_NUMBER_FOLLOWS}
    
    if len(input_string) % 6 != 0:
        return False
    
    for i in range(0, len(input_string), 6):
        braille_substring = input_string[i:i+6]
        
        if braille_substring not in braille_chars and braille_substring not in braille_numbers and braille_substring not in braille_special and braille_substring not in special_cases:
            return False
    
    return True

def detect_string_type(input_string):
    """
    Detect the type of the given input string.
    """
    is_braille = True
    for c in input_string:
        if c in ' ':
            break
        if c not in 'O.':
            is_braille = False
            break
    if is_braille:
        if is_valid_braille_string(input_string):
            return BRAILLE_TYPE
        else:
            return INVALID_BRAILLE_STRING

    is_english = True
    for char in input_string:
        if char not in ENGLISH_CHARS:
            is_english = False
            break

    if is_english:
        return ENGLISH_TYPE
    
    return UNKNOWN_TYPE


def swap_dict_keys_values(dictionary):
    """
    Swap the keys and values in the given dictionary.
    """
    updated_dict = {}
    for key, value in dictionary.items():
        updated_dict[value] = key
    return updated_dict