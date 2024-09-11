from typing import List
import sys

ENG_TO_BRAILLE_DICT = {
    "a": "O.....", "b": "O.O...",
    "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO",
    "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

NUMS_TO_BRAILLE_DICT = {
    "0": ".OOO..", "1": "O.....",
    "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO..."
}

# Special Symbols
BRAILLE_NUMBER  = ".O.OOO" # Numbers until next space
BRAILLE_SPACE   = "......" # Space character
BRAILLE_CAPITAL = ".....O" # Capital letter follows

# For reverse translation
BRAILLE_TO_ENG_DICT  = {v: k for k, v in ENG_TO_BRAILLE_DICT.items()}
BRAILLE_TO_NUMS_DICT = {v: k for k, v in NUMS_TO_BRAILLE_DICT.items()}


# Length of braille string must be multiple of 6
def braille_to_english(text: str):
    text_english: str = ''

    number_next: bool = False
    capital_next: bool = False
    
    i : int = 0
    while i+6 <= len(text):
        char: str = text[i:i+6] # Parse the text 6 characters at a time
        i += 6
        
        if char == BRAILLE_NUMBER: number_next = True; continue
        if char == BRAILLE_CAPITAL: capital_next = True; continue
        if char == BRAILLE_SPACE:
            number_next = False
            text_english += ' '
            continue
        
        char_eng: str = BRAILLE_TO_NUMS_DICT[char] if number_next else BRAILLE_TO_ENG_DICT[char]
        if capital_next and not number_next: char_eng = char_eng.upper(); capital_next = False
        
        text_english += char_eng
    
    return text_english


# Assume that numbers are only at the end of words
def english_to_braille(word_list: List[str]):
    text_braille: str = ''

    number_next: bool = False
    
    for i, word in enumerate(word_list):
        for char in word:
            if char in NUMS_TO_BRAILLE_DICT and not number_next: # Found first number in word
                number_next = True
                text_braille += BRAILLE_NUMBER
            
            if number_next: text_braille += NUMS_TO_BRAILLE_DICT[char]; continue
            
            if char.isupper(): text_braille += BRAILLE_CAPITAL
            text_braille += ENG_TO_BRAILLE_DICT[char.lower()]
        
        # Don't add space after last word
        text_braille += BRAILLE_SPACE if i != len(word_list) - 1 else ''
        number_next = False
    
    return text_braille


def is_braille(text : str):
    if len(text) % 6 != 0: return False
    for char in text:
        if char not in ['O', '.']: return False
    return True


def main():
    if len(sys.argv) <= 1:
        return
        
    # Argument is braille
    if len(sys.argv) == 2 and is_braille(sys.argv[1]):
        print(braille_to_english(sys.argv[1]))
    
    # Argument is english
    else:
        print(english_to_braille(sys.argv[1:]))
    

if __name__ == '__main__':
    main()