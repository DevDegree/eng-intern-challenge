import sys

CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"
BRAILLE_CHARACTER_LENGTH = 6

BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

BRAILLE_TO_NUM = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
NUM_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_NUM.items()}

def english_to_braille(text: str) -> str:
    res = ""
    number_mode = False
    for char in text:
        if char.isalpha():
            if char.isupper():
                res += CAPITAL_FOLLOWS
                char = char.lower()
            res += ENGLISH_TO_BRAILLE[char]
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                res += NUMBER_FOLLOWS
                number_mode = True
            res += NUM_TO_BRAILLE[char]
        elif char == " ":
            res += SPACE
            number_mode = False
    return res

def braille_to_english(braille: str) -> str:
    res = ""
    i = 0
    capitalize = False
    number_mode = False
    while i < len(braille):
        braille_char = braille[i:i + BRAILLE_CHARACTER_LENGTH]
        if braille_char == CAPITAL_FOLLOWS:
            capitalize = True
        elif braille_char == NUMBER_FOLLOWS:
            number_mode = True
        elif braille_char == SPACE:
            res += " "
            number_mode = False
        else:
            if number_mode:
                res += BRAILLE_TO_NUM[braille_char]
            else:
                letter = BRAILLE_TO_ENGLISH[braille_char]
                if capitalize:
                    letter = letter.upper()
                    capitalize = False
                res += letter
        i += BRAILLE_CHARACTER_LENGTH
    return res

def main():
    text = " ".join(sys.argv[1:])
    if '.' in text:
        result = braille_to_english(text)
    else:
        result = english_to_braille(text)
    
    print(result)

if __name__ == "__main__":
    main()