from translator_mappings import (
    ENGLISH_TO_BRAILLE_MAPPINGS,
    NUMBERS_TO_BRAILLE_MAPPINGS,
    PUNCTUATION_TO_BRAILLE_MAPPINGS,
    CAPITAL_FOLLOWS_CASE,
    DECIMAL_FOLLOWS_CASE,
    NUMBER_FOLLOWS_CASE,
    SPACE_CASE
)

def translate_to_braille_char(char: str, previous_char: str) -> str:    
    if char == " ":
        return SPACE_CASE
    
    if previous_char.isnumeric():
        return NUMBERS_TO_BRAILLE_MAPPINGS[char]
    
    if char.isupper():
        return CAPITAL_FOLLOWS_CASE + ENGLISH_TO_BRAILLE_MAPPINGS[char.lower()]

    if char.isnumeric():
        return NUMBER_FOLLOWS_CASE + NUMBERS_TO_BRAILLE_MAPPINGS[char]
    
    if char in PUNCTUATION_TO_BRAILLE_MAPPINGS:
        return PUNCTUATION_TO_BRAILLE_MAPPINGS[char]
    
    return ENGLISH_TO_BRAILLE_MAPPINGS[char.lower()]

def translate_to_braille(text: str) -> str:
    translate_to_braille_array = []
    previous_char = ""

    for i, char in enumerate(text):
        previous_char = text[i - 1] if i > 0 else ""
        translate_to_braille_array.append(translate_to_braille_char(char, previous_char))
    
    return "".join(translate_to_braille_array)
