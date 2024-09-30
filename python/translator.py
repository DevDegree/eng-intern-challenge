import sys

BRAILLE_TO_LETTERS = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
}

BRAILLE_TO_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

ENGLISH_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..", " ": "......",
}

SPACE_CELL = "......"

CAPITAL_FOLLOWS_CELL = ".....O"
NUMBER_FOLLOWS_CELL = ".O.OOO"

def translate_braille_to_english(braille: str) -> str:
    output = ""
    cells = [braille[i:i+6] for i in range(0, len(braille), 6)]
    capital_follows = False
    number_follows = False
    for cell in cells:
        if capital_follows:
            output += BRAILLE_TO_LETTERS[cell].upper()
            capital_follows = False
        elif cell == SPACE_CELL:
            output += " "
            number_follows = False
        elif number_follows:
            output += BRAILLE_TO_NUMBERS[cell]
        elif cell == CAPITAL_FOLLOWS_CELL:
            capital_follows = True
        elif cell == NUMBER_FOLLOWS_CELL:
            number_follows = True
        else:
            output += BRAILLE_TO_LETTERS[cell]
    return output

def translate_english_to_braille(english: str) -> str:
    output = ""
    number_follows = False
    for char in english:
        if char.isupper():
            output += CAPITAL_FOLLOWS_CELL
        elif char.isdigit() and not number_follows:
            output += NUMBER_FOLLOWS_CELL
            number_follows = True
        elif char == " ":
            number_follows = False
        output += ENGLISH_TO_BRAILLE[char.lower()]
    return output

def is_braille(input: str) -> bool:
    return "." in input

def main():
    input = " ".join(sys.argv[1:])

    if is_braille(input):
        print(translate_braille_to_english(input))
    else:
        print(translate_english_to_braille(input))

if __name__ == "__main__":
    main()
