import sys
from utils import detect_string_type, swap_dict_keys_values
from consts import BRAILLE_TO_ENGLISH_DICT, BRAILLE_TYPE, ENGLISH_TYPE, BRAILLE_CAPITAL_FOLLOWS, BRAILLE_TO_NUMBER_DICT, BRAILLE_TO_SPECIAL_DICT, BRAILLE_NUMBER_FOLLOWS

def translate_braille_to_english(braille_string):
    """
    Translate the given Braille string to English.
    """
    result = ""
    is_capital = False
    is_number = False

    for i in range(0, len(braille_string), 6):
        braille_chunk = braille_string[i:i+6]
        
        if braille_chunk == BRAILLE_CAPITAL_FOLLOWS:
            is_capital = True
            continue
        if braille_chunk == BRAILLE_NUMBER_FOLLOWS:
            is_number = True
            continue
        if braille_chunk == "......":
            result += " "
            is_number = False
            continue        
        if is_number and braille_chunk in BRAILLE_TO_NUMBER_DICT:
            result += BRAILLE_TO_NUMBER_DICT[braille_chunk]
            continue

        if braille_chunk in BRAILLE_TO_ENGLISH_DICT:
            english_char = BRAILLE_TO_ENGLISH_DICT[braille_chunk]
            if is_capital:
                result += english_char.upper()
                is_capital = False
            else:
                result += english_char
        elif braille_chunk in BRAILLE_TO_SPECIAL_DICT:
            result += BRAILLE_TO_SPECIAL_DICT[braille_chunk]
    return result

def translate_english_to_braille(english_string):
    """
    Translate the given English string to Braille.
    """
    english_to_braille_dict = swap_dict_keys_values(BRAILLE_TO_ENGLISH_DICT)
    number_to_braille_dict = swap_dict_keys_values(BRAILLE_TO_NUMBER_DICT)
    special_to_braille_dict = swap_dict_keys_values(BRAILLE_TO_SPECIAL_DICT)
    result = ""
    in_number_mode = False

    for char in english_string:
        if char.isalpha():
            if char.isupper():
                result += BRAILLE_CAPITAL_FOLLOWS
            result += english_to_braille_dict[char.lower()]
            in_number_mode = False
        elif char.isdigit():
            if not in_number_mode:
                result += BRAILLE_NUMBER_FOLLOWS
                in_number_mode = True                
            result += number_to_braille_dict[char]
        elif char in special_to_braille_dict:
            result += special_to_braille_dict[char]
            in_number_mode = False
    return result

def main():
    """
    Main function that handles command line arguments and calls the appropriate translation function.
    """
    input_string = ' '.join(sys.argv[1:])
    string_type = detect_string_type(input_string)
    
    if string_type == BRAILLE_TYPE:
        translated_string = translate_braille_to_english(input_string)
    elif string_type == ENGLISH_TYPE:
        translated_string = translate_english_to_braille(input_string)
    else:
        translated_string = string_type
    
    print(translated_string)
     

if __name__ == '__main__':
    main()