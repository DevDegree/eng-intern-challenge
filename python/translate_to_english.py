from translator_mappings import (
    BRAILLE_TO_ENGLISH_MAPPINGS, 
    BRAILLE_TO_NUMBERS_MAPPINGS, 
    BRAILLE_TO_PUNCTUATION_MAPPINGS,
    CAPITAL_FOLLOWS_CASE,
    DECIMAL_FOLLOWS_CASE,
    NUMBER_FOLLOWS_CASE,
    SPACE_CASE
)

global current_text_index 
current_text_index = 0

def translate_braille_text_to_number(braille_text: list[str]) -> str:
    translate_to_number_array = []

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i : i+6]

        if braille_char not in BRAILLE_TO_NUMBERS_MAPPINGS:
            break

        translate_to_number_array.append(BRAILLE_TO_NUMBERS_MAPPINGS[braille_char])

        global current_text_index
        current_text_index += 6
    
    return "".join(translate_to_number_array)

def translate_to_english_char(braille_char: str,
                              braille_text: list[str]) -> str:
    if braille_char == SPACE_CASE:
        return " "

    if braille_char == CAPITAL_FOLLOWS_CASE:
        character_to_be_capitalized = BRAILLE_TO_ENGLISH_MAPPINGS[braille_text[:6]]
        global current_text_index
        current_text_index += 6
        return character_to_be_capitalized.upper()
    
    if braille_char == NUMBER_FOLLOWS_CASE:
        return translate_braille_text_to_number(braille_text)

    if braille_char in BRAILLE_TO_PUNCTUATION_MAPPINGS:
        return BRAILLE_TO_PUNCTUATION_MAPPINGS[braille_char]
    
    return BRAILLE_TO_ENGLISH_MAPPINGS[braille_char]
    
def translate_to_english(text: str) -> str:
    translate_to_english_array = []

    global current_text_index
    while current_text_index < len(text):
        braille_char = text[current_text_index : current_text_index + 6]
        translate_to_english_array.append(translate_to_english_char(braille_char,
                                                                    text[current_text_index + 6:]))
        current_text_index += 6
        
    return "".join(translate_to_english_array)
