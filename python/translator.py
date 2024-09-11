import sys

# Special characters
CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"
DECIMAL = ".O...O"

# Braille mappings for English letters and digits
letter_to_braille = {
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

digit_to_braille = {
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

# Reverse mappings for Braille to English
braille_to_letter = {k: v for v, k in letter_to_braille.items()}
braille_to_digit = {k: v for v, k in digit_to_braille.items()}


def is_braille(text: str) -> bool:
    """Check if a given string is in Braille"""
    return all(char in "O." for char in text) and len(text) % 6 == 0


def braille_to_english(braille: str) -> str:
    """Translate given Braille input to English"""
    res = ""
    capitalize = False
    in_number = False
    for i in range(0, len(braille), 6):
        char = braille[i : i + 6]
        if char == CAPITAL:
            capitalize = True
        elif char == NUMBER:
            in_number = True
        elif char == SPACE:
            res += " "
            in_number = False
        elif in_number:
            res += braille_to_digit[char]
        else:
            res += (
                braille_to_letter[char].upper()
                if capitalize
                else braille_to_letter[char]
            )
            capitalize = False
    return res


def english_to_braille(english: str) -> str:
    """Translate given English input to Braille"""
    res = ""
    idx = 0
    in_number = False
    while idx < len(english):
        char = english[idx]
        if char.isupper():
            res += CAPITAL
            res += letter_to_braille[char.lower()]
        elif char.isdigit():
            if not in_number:
                res += NUMBER
                in_number = True
            res += digit_to_braille[char]
        elif char == " ":
            res += SPACE
            in_number = False
        elif char == ".":
            res += DECIMAL
        else:
            res += letter_to_braille[char]
        idx += 1
    return res


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    input_string = " ".join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))
