
import sys
from translation_mappings import braille_to_english_letter, braille_to_english_number, english_letter_to_braille, english_number_to_braille, number_follows_braille, capital_follows_braille, space_braille
BRAILLE_CHARS_PER_ENGLISH_CHAR = 6
SPACE_CHAR = ' '

class Validator():
    def is_english_string(self, str_to_check: str) -> bool:
        # since we don't need to translate english periods,
        # and there is no 6-character braille representation that does not contain a period,
        # a string is braille if and only if it contains a period
        if '.' in str_to_check:
            return False
        return True

class Translator():
    def __init__(self) -> None:
        pass

    def translate_english_to_braille(self, eng_str: str) -> str:
        number_follow_active = False
        braille_string = ''
        for cur_char in eng_str:
            if cur_char == SPACE_CHAR:
                number_follow_active = False
                braille_string += space_braille
            elif cur_char.isnumeric():
                if not number_follow_active:
                    braille_string += number_follows_braille
                    number_follow_active = True   
                braille_string += english_number_to_braille[cur_char]
            elif cur_char.isupper():
                braille_string += capital_follows_braille
                braille_string += english_letter_to_braille[cur_char.lower()]
            else:
                braille_string += english_letter_to_braille[cur_char]
        return braille_string
    
    def translate_braille_to_english(self, braille_str: str) -> str:
        next_letter_uppercase = False
        numerical_mode = False
        english_string = ''
        for first_char_idx in range(0, len(braille_str), BRAILLE_CHARS_PER_ENGLISH_CHAR):
            single_english_char_braille = braille_str[first_char_idx : first_char_idx + BRAILLE_CHARS_PER_ENGLISH_CHAR]
            if single_english_char_braille == space_braille:
                numerical_mode = False
                english_string += SPACE_CHAR
            elif single_english_char_braille == capital_follows_braille:
                next_letter_uppercase = True
                continue
            elif single_english_char_braille == number_follows_braille:
                numerical_mode = True
                continue
            elif numerical_mode:
                english_string += braille_to_english_number[single_english_char_braille]
            elif next_letter_uppercase:
                english_string += braille_to_english_letter[single_english_char_braille].upper()
                next_letter_uppercase = False
            else:
                english_string += braille_to_english_letter[single_english_char_braille]
        return english_string
        
def main():
    str_to_translate = ''
    for i in range(1, len(sys.argv)):
        if i == len(sys.argv) - 1:
            str_to_translate = str_to_translate + sys.argv[i]
        else:
            str_to_translate = str_to_translate + sys.argv[i] + ' '

    translator = Translator()
    validator = Validator()
    if validator.is_english_string(str_to_translate):
        print(translator.translate_english_to_braille(str_to_translate))
    else:
        print(translator.translate_braille_to_english(str_to_translate))

            
main()
