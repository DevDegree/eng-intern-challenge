import sys

ALPHA_TO_BRAILLE = {
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
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    " ": "......",
}
BRAILLE_TO_ALPHA = {v: k for k, v in ALPHA_TO_BRAILLE.items()}
NUM_TO_BRAILLE = {
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
    " ": "......",
}
BRAILLE_TO_NUM = {v: k for k, v in NUM_TO_BRAILLE.items()}


def braille_to_text(braille: str) -> str:
    """Translates Braille to English."""

    text = ""
    is_numeric = False
    is_capitalized = False

    # Split the braille string into 6-character cells
    for cell in [braille[i:i+6] for i in range(0, len(braille), 6)]:
        try:
            # Check if the cell is a number or letter and get the corresponding character
            char = BRAILLE_TO_NUM[cell] if is_numeric else BRAILLE_TO_ALPHA[cell]
        except KeyError:
            sys.exit("Invalid braille input following 'number follows'")

        if char == " ":
            is_numeric = False
            text += char
        elif char == "number follows":
            is_numeric = True
        elif char == "capital follows":
            is_capitalized = True
        elif is_capitalized:
            text += char.upper()
            is_capitalized = False
        else:
            text += char

    return text


def text_to_braille(text: str) -> str:
    """Translates English to Braille."""

    braille = ""
    is_numeric = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                braille += ALPHA_TO_BRAILLE["capital follows"]
            braille += ALPHA_TO_BRAILLE[char.lower()]

        elif char.isdigit():
            if not is_numeric:
                braille += ALPHA_TO_BRAILLE["number follows"]
                is_numeric = True
            braille += NUM_TO_BRAILLE[char]

        elif char == " ":
            braille += ALPHA_TO_BRAILLE[char]
            is_numeric = False

        else:
            sys.exit("Invalid character in input")

    return braille


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 translator.py <text/braille>")

    # Check if the input is braille or English
    if "." in sys.argv[1]:
        braille = sys.argv[1]
        text = braille_to_text(braille)
        print(text)
    else:
        text = " ".join(sys.argv[1:])
        braille = text_to_braille(text)
        print(braille)
