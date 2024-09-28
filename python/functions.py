from dictionary import braille_to_english, braille_num_to_english, english_to_braille
from typing import Tuple
import re

def is_braille(input: str) -> bool:
    lookFor: Tuple[str, str] = (".", "O")

    if any(char in input for char in lookFor):
        return True
    return False
    

def translate_braille_to_english(braille: str) -> str:
    english: str = ""
    capital: bool = False
    integer: bool = False
    decimal: bool = False

    for char in range(0, len(braille), 6):
        braille_char = braille[char:char +  6]
        translated_char = braille_to_english.get(braille_char, '')
        translated_num = braille_num_to_english.get(braille_char, '')

        if translated_char == "capital":
            capital = True
            integer = False
        elif translated_char == "number":
            integer = True
        elif translated_char == "decimal":
            decimal = True
        else:
            if capital:
                english+= translated_char.upper()
                capital = False
            elif integer and re.findall(r'[a-j]', translated_char):
                english += translated_num
            elif decimal:
                english+= translated_char
                decimal = False
            else:
                english+= translated_char
    
    return english.strip()


def translate_english_to_braille(english: str) -> str:
    braille: str = ""
    integer: bool = False

    for char in english:
        if re.findall(r'[A-Z]', char):
            braille+= english_to_braille.get("capital", '')
            braille+= english_to_braille.get(char.lower(), '')
        elif re.findall(r'[0-9]', char):
            if not integer:
                integer = True
                braille+= english_to_braille["number"]
            braille+= english_to_braille[char]
        else:
            braille+= english_to_braille[char]
            integer = False

    return braille.strip()