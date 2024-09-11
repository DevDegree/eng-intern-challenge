import sys
import re

letters_table = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",   
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", 
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", 
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", " ": "......", 

    "capital": ".....O",
    "number":  ".O.OOO"
}

numbers_table = {
    "1": "O.....",   
    "2": "O.O...",   
    "3": "OO....",  
    "4": "OO.O..",   
    "5": "O..O..",   
    "6": "OOO...",   
    "7": "OOOO..",   
    "8": "O.OO..",   
    "9": ".OO...",   
    "0": "O...OO",
    " ": "......", 
}

"""Converts a string from Braille to English

:param initial_string: string to be translated
:returns: translated string 
"""
def braille_to_english(initial_string: str) -> str: 
    char_size = 6
    braille_to_english = {v: k for k, v in letters_table.items()}
    braille_to_numbers = {v: k for k, v in numbers_table.items()}

    capital_follows = False
    is_number = False

    english_string = ""

    for i in range(0, len(initial_string), char_size): 
        braille_char = initial_string[i:i + char_size]
        
        if not is_number: english_char = braille_to_english[braille_char]
        else: english_char = braille_to_numbers[braille_char]

        if english_char == "capital": 
            capital_follows = True 
            continue
        
        elif capital_follows: 
            english_string += english_char.upper()
            capital_follows = False
            continue

        elif english_char == "number": 
            is_number = True
            continue
        
        elif english_char == " ": 
            is_number = False

        
        english_string += english_char

    return english_string
        
"""Converts a string from English to Braille

:param initial_string: string to be translated
:returns: translated string 
"""
def english_to_braille(initial_string: str) -> str: 
    braille_string = ""
    first_numeric = False

    for char in initial_string: 
        if char.isupper(): 
            braille_string += letters_table["capital"]
        
        elif char.isnumeric():
            if not first_numeric: 
                first_numeric = True
                braille_string += letters_table["number"]
            braille_string += numbers_table[char]
            continue

        elif not char.isnumeric(): 
            first_numeric = False

        braille_string += letters_table[char.lower()]
    return braille_string

"""Checks if input string is in Braille or English

:param initial_string: string to be translated
:returns: translated string 
"""
def is_braille(initial_string: str) -> bool: 
    return bool(re.fullmatch(r"[O.]*", initial_string))

def main() -> None: 
    initial_string = " ".join(sys.argv[1:])
    
    if is_braille(initial_string): print(braille_to_english(initial_string))
    else: print(english_to_braille(initial_string))


if __name__ == "__main__":
    main()