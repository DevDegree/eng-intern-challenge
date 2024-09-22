import sys
from braille_dict import *

# Please read README2.md for more information on the solution.

BRAILLE_LETTERS = ["O", "."]
is_roman = False

def assign_direction(text):
    global is_roman

    for letter in text:
        if letter not in BRAILLE_LETTERS:
            is_roman = True
            return
    is_roman = False


def translate_to_english(braille_text):
    capitalize = False
    numbers = False
    english_text = ""

    for i in range(0, len(braille_text), 6):
        braille_letter = braille_text[i:i+6]

        if braille_letter == BRAILLE_SPACE:
            # reset numbers if active
            if numbers:
                numbers = False
            english_text += " "
            continue
        
        if numbers:
            english_text += BRAILLE_TO_ENG_NUMS[braille_letter]
            continue

        english_key = BRAILLE_TO_ENG_LETTERS[braille_letter]

        if english_key == "capital":
            capitalize = True
            continue
            
        if english_key == "number":
            numbers = True
            continue

        if capitalize:
            english_text += english_key.upper()
            capitalize = False
        else:
            english_text += english_key
        
    return english_text


def translate_to_braille(english_text):
    braille_text = ""
    numbers_on = False

    for letter in english_text:
        if letter in BRAILLE_TO_ENG_NUMS.values():
            if not numbers_on:
                braille_text += ENGLISH_TO_BRAILLE["number"]
                numbers_on = True
            braille_text += ENGLISH_TO_BRAILLE[letter]
            continue
            
        numbers_on = False
        
        if letter.isupper():
            braille_text += ENGLISH_TO_BRAILLE["capital"]
            letter = letter.lower()
        
        braille_text += ENGLISH_TO_BRAILLE[letter]

    return braille_text


if __name__ == "__main__":
    text = ' '.join(sys.argv[1:])
    assign_direction(text)

    if not is_roman:
        translated_text = translate_to_english(text)
    else:
        translated_text = translate_to_braille(text)
    
    print(translated_text)

    
