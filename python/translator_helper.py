from mappings.braille_to_english import (
    BRAILLE_TO_ENGLISH_ALPHABET_MAPPING,
    BRAILLE_TO_NUMBERS_MAPPING,
    BRAILLE_TO_SPECIAL_CHARS_MAPPING,
    BRAILLE_NOT_POSSIBLE_NUMBER_OPERATORS_TO_SPECIAL_CHARS_MAPPING
)

from mappings.constants import (
    BRAILLE_CAPITAL_FOLLOWS_CONSTANT,
    BRAILLE_DECIMAL_FOLLOWS_CONSTANT,
    BRAILLE_NUMBER_FOLLOWS,
)

from mappings.english_to_braille import (
    ENGLISH_TO_BRAILLE_ALPHABET_MAPPING,
    NUMBER_TO_BRAILLE_MAPPING,
    SPECIAL_TO_BRAILLE_MAPPING,
)


def translate_braille_to_english(braille: str) -> str:
    n = len(braille)
    if n % 6 != 0:
        raise ValueError(f"Provided braille may not be valid or does not follow the expected convention")

    number_of_brailles = n // 6
    res = list()

    is_decimal = False
    is_number = False
    is_capitalized_word = False
    is_upper_cased_word = False
    follows_chars = {
        BRAILLE_CAPITAL_FOLLOWS_CONSTANT,
        BRAILLE_NUMBER_FOLLOWS,
        BRAILLE_DECIMAL_FOLLOWS_CONSTANT
    }

    for i in range(1, number_of_brailles + 1):
        current_index = i * 6
        current_char = braille[current_index - 6: current_index]
        if current_char in follows_chars:
            if current_char == BRAILLE_CAPITAL_FOLLOWS_CONSTANT:
                if is_capitalized_word:
                    is_capitalized_word = False
                    is_upper_cased_word = True
                else:
                    is_capitalized_word = True
                    is_upper_cased_word = False
            if current_char == BRAILLE_NUMBER_FOLLOWS or current_char == BRAILLE_DECIMAL_FOLLOWS_CONSTANT:
                is_number = True
        else:
            if not any([is_decimal, is_number, is_capitalized_word, is_upper_cased_word]):
                res.append(get_braille_char_or_special_char(current_char))
            else:
                if is_number:
                    if current_char not in BRAILLE_TO_NUMBERS_MAPPING:
                        if current_char in BRAILLE_NOT_POSSIBLE_NUMBER_OPERATORS_TO_SPECIAL_CHARS_MAPPING:
                            is_number = False
                            res.append(BRAILLE_NOT_POSSIBLE_NUMBER_OPERATORS_TO_SPECIAL_CHARS_MAPPING[current_char])
                        else:
                            res.append(get_braille_char_or_special_char(current_char))
                    else:
                        res.append(BRAILLE_TO_NUMBERS_MAPPING[current_char])

                if is_capitalized_word:
                    res.append(BRAILLE_TO_ENGLISH_ALPHABET_MAPPING[current_char].upper())
                    is_capitalized_word = False

                if is_upper_cased_word:
                    if current_char not in BRAILLE_TO_ENGLISH_ALPHABET_MAPPING:
                        is_upper_cased_word = False
                        res.append(get_braille_char_or_special_char(current_char))
                    else:
                        res.append(BRAILLE_TO_ENGLISH_ALPHABET_MAPPING[current_char].upper())
    return ''.join(res)


def get_braille_char_or_special_char(braille_char: str) -> str:
    if braille_char in BRAILLE_TO_ENGLISH_ALPHABET_MAPPING:
        return BRAILLE_TO_ENGLISH_ALPHABET_MAPPING[braille_char]
    return BRAILLE_TO_SPECIAL_CHARS_MAPPING[braille_char]


def translate_english_to_braille(english: str) -> str:
    res = list()
    is_digit_flag = False
    for char in english:
        if char.isalpha():
            if char.isupper():
                res.append(f"{BRAILLE_CAPITAL_FOLLOWS_CONSTANT}{ENGLISH_TO_BRAILLE_ALPHABET_MAPPING[char.lower()]}")
            else:
                res.append(ENGLISH_TO_BRAILLE_ALPHABET_MAPPING[char])
            is_digit_flag = False
        elif char.isdigit():
            if not is_digit_flag:
                res.append(f"{BRAILLE_NUMBER_FOLLOWS}{NUMBER_TO_BRAILLE_MAPPING[char]}")
                is_digit_flag = True
            else:
                res.append(NUMBER_TO_BRAILLE_MAPPING[char])
        elif char in SPECIAL_TO_BRAILLE_MAPPING:
            res.append(SPECIAL_TO_BRAILLE_MAPPING[char])
        else:
            raise ValueError("Provided english may not be valid or does not follow the expected convention")
    return ''.join(res)
