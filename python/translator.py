import sys

ALPHABET_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...", 
    "c": "OO....", 
    "d": "OO.O..", 
    "e": "O..O..", 
    "f": "OOO...", 
    "g": "OOOO..", 
    "h": "O.OO..", 
    "i": ".OO...", 
    "j": ".OOO..",
    "k": "O...O.", 
    "l": "O.O.O.", 
    "m": "OO..O.", 
    "n": "OO.OO.", 
    "o": "O..OO.", 
    "p": "OOO.O.", 
    "q": "OOOOO.", 
    "r": "O.OOO.", 
    "s": ".OO.O.", 
    "t": ".OOOO.",
    "u": "O...OO", 
    "v": "O.O.OO", 
    "w": ".OOO.O", 
    "x": "OO..OO", 
    "y": "OO.OOO", 
    "z": "O..OOO",
    " ": "......",
    "capital_follows": ".....O",
    "number_follows": ".O.OOO",
}

NUMBERS_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...", 
    "3": "OO....", 
    "4": "OO.O..", 
    "5": "O..O..", 
    "6": "OOO...", 
    "7": "OOOO..", 
    "8": "O.OO..", 
    "9": ".OO...", 
    "0": ".OOO..",
}

BRAILLE_TO_ALPHABET = {
    braille: letter for letter, braille in ALPHABET_TO_BRAILLE.items()
}

BRAILLE_TO_NUMBERS = {
    braille: number for number, braille in NUMBERS_TO_BRAILLE.items()
}

"""
* Reads string from arguments and converts string
* from Braille to English or vice-versa.
"""
def convert_braille(string_to_convert: str) -> str:
        if is_braille_string(string_to_convert):
            return braille_to_english(string_to_convert)
        else:
            return english_to_braille(string_to_convert)
        
def is_braille_string(string: str) -> bool:
    return set(string).issubset({'.', 'O'})

def english_to_braille(english_string: str) -> str:
    braille_string = ""

    for index in range(len(english_string)):
        char = english_string[index]

        if char.isdigit():
            if index == 0 or not english_string[index - 1].isdigit():
                braille_string += ALPHABET_TO_BRAILLE["number_follows"]
            braille_string += NUMBERS_TO_BRAILLE[char]

        elif char.isupper():
            braille_string += ALPHABET_TO_BRAILLE["capital_follows"]
            braille_string += ALPHABET_TO_BRAILLE[char.lower()]
        
        else:
            braille_string += ALPHABET_TO_BRAILLE[char]

    return braille_string

def braille_to_english(braille_string: str) -> str:
    english_string = ""
    capital_flag = False
    number_flag = False
    for char_start in range(0, len(braille_string), 6):
        braille_char = braille_string[char_start : char_start + 6]
        translated_braille = BRAILLE_TO_ALPHABET[braille_char]

        if translated_braille == "capital_follows":
            capital_flag = True

        elif translated_braille == "number_follows":
            number_flag = True

        elif capital_flag:
            english_string += BRAILLE_TO_ALPHABET[braille_char].upper()
            capital_flag = False

        elif number_flag:
            english_string += BRAILLE_TO_NUMBERS[braille_char]
            if char_start + 12 <= len(braille_string):
                next_braille_char = braille_string[char_start + 6 : char_start + 12]
                if next_braille_char not in BRAILLE_TO_NUMBERS:
                    number_flag = False

        else:
            english_string += BRAILLE_TO_ALPHABET[braille_char]
    
    return english_string

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)
    else:
        string_to_convert = " ".join(sys.argv[1:])
        print(convert_braille(string_to_convert))

if __name__ == "__main__":
    main()