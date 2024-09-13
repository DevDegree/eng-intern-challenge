from utils.constants import (
    VALID_CHARACTER_SET
)

def is_braille(input_string):
    return all(c in 'O.' for c in input_string)

def does_have_unsupported_english_characters(english_string):
    return not set(english_string).issubset(VALID_CHARACTER_SET)
