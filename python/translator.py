import sys

CAPITAL_INDICATOR = ".....O"
NUMBER_INDICATOR = ".O.OOO"
SPACE = "......"

braille_dict = {
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
    "......": " "
}

braille_number_dict = {
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
    "......": " "
}

english_dict = {
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
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

def translator(arg):
    if is_braille(arg):
        translation = braille_to_english(arg)
    else:
        translation = english_to_braille(arg)
    
    if translation is False:
        return "A character does not exist for braille translation"
    return translation

def is_braille(arg):
    return all(char in ['.', 'O'] for char in arg) and len(arg) % 6 == 0

def braille_to_english(braille):
    translated_chars = []
    next_char_is_capital = False
    next_chars_are_numbers = False

    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]

        if next_char_is_capital:
            translated_chars.append(braille_dict[braille_char].capitalize())
            next_char_is_capital = False
        elif next_chars_are_numbers:
            translated_chars.append(handle_number_braille(braille_char))
            next_chars_are_numbers = braille_char != SPACE
        elif braille_char == CAPITAL_INDICATOR:
            next_char_is_capital = True
        elif braille_char == NUMBER_INDICATOR:
            next_chars_are_numbers = True
        elif braille_char in braille_dict:
            translated_chars.append(braille_dict[braille_char])
        else:
            return False

    return "".join(translated_chars)

def handle_number_braille(braille_char):
    if braille_char == SPACE:
        return " "
    return braille_number_dict.get(braille_char, "")

def english_to_braille(english):
    translated_chars = []
    number = False

    for i in range(len(english)):
        english_char = english[i]

        if english_char.isdigit():
            if not number:
                number = True
                translated_chars.append(NUMBER_INDICATOR)
            translated_chars.append(english_dict[english_char])
            continue
        
        if number:
            number = False

        if english_char.isupper():
            translated_chars.append(CAPITAL_INDICATOR)
            english_char = english_char.lower()

        braille_char = english_dict.get(english_char)
        if braille_char is None:
            return False

        translated_chars.append(braille_char)

    return "".join(translated_chars)

if __name__ == "__main__":
    args = " ".join(sys.argv[1:])
    print(translator(args))