import sys


CAPITAL_FOLLOWS_CASE = ".....O"

DECIMAL_FOLLOWS_CASE = ".O...O"

NUMBER_FOLLOWS_CASE = ".O.OOO"

SPACE_CASE = "......"

BRAILLE_TO_ENGLISH_MAPPINGS = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
}

BRAILLE_TO_NUMBERS_MAPPINGS = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

BRAILLE_TO_PUNCTUATION_MAPPINGS = {
    "..OO.O": ".",
    "..O...": ",",
    "...OOO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "O..OO.": ">",
    "O.O..O": "(",
    ".O.OO..": ")",
}

ENGLISH_TO_BRAILLE_MAPPINGS = {
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
}

NUMBERS_TO_BRAILLE_MAPPINGS = {
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

PUNCTUATION_TO_BRAILLE_MAPPINGS = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "...OOO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
}


global iterator_index 
iterator_index = 0

def translate_braille_text_to_number(braille_text: list[str]) -> str:
    translate_to_number_array = []

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i : i+6]

        if braille_char not in BRAILLE_TO_NUMBERS_MAPPINGS:
            break

        translate_to_number_array.append(BRAILLE_TO_NUMBERS_MAPPINGS[braille_char])

        global iterator_index
        iterator_index += 6
    
    return "".join(translate_to_number_array)

def translate_to_english_char(braille_char: str,
                              braille_text: list[str]) -> str:
    if braille_char == SPACE_CASE:
        return " "

    if braille_char == CAPITAL_FOLLOWS_CASE:
        character_to_be_capitalized = BRAILLE_TO_ENGLISH_MAPPINGS[braille_text[:6]]
        global iterator_index
        iterator_index += 6
        return character_to_be_capitalized.upper()
    
    if braille_char == NUMBER_FOLLOWS_CASE:
        return translate_braille_text_to_number(braille_text)

    if braille_char in BRAILLE_TO_PUNCTUATION_MAPPINGS:
        return BRAILLE_TO_PUNCTUATION_MAPPINGS[braille_char]
    
    return BRAILLE_TO_ENGLISH_MAPPINGS[braille_char]
    
def translate_to_english(text: str) -> str:
    translate_to_english_array = []

    global iterator_index
    while iterator_index < len(text):
        braille_char = text[iterator_index : iterator_index + 6]
        translate_to_english_array.append(translate_to_english_char(braille_char,
                                                                    text[iterator_index + 6:]))
        iterator_index += 6
        
    return "".join(translate_to_english_array)


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

def is_text_braille(text: str) -> bool:
    braille_characters = ["O", "."]

    for char in text:
        if char not in braille_characters:
            return False

    return True

def translate(text: str) -> str:
    if not is_text_braille(text):
        return translate_to_braille(text)
    
    return translate_to_english(text)
     
def main():
    args = sys.argv[1:]
    string_to_be_translated = ""

    for i, arg in enumerate(args):
        if i == len(args) - 1:
            string_to_be_translated += arg
        else:
            string_to_be_translated += arg + " "

    print(translate(string_to_be_translated))

if __name__ == "__main__":
    main()
