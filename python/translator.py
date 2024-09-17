import sys

LETTERS = {
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

NUMBERS = {
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

KEYS = {
    "capital_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
}

PUNCTUATION = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

def translate_to_braille(text):
    string = ""
    i = 0
    while i < len(text):
        token = text[i]

        if token.isdigit():
            string += KEYS["number_follows"]  # Add number marker before any digits
            while i < len(text) and text[i].isdigit():
                string += NUMBERS[text[i]]
                i += 1
            continue

        if token.isupper():
            string += KEYS["capital_follows"]  # Add capital marker before any uppercase letters
            while i < len(text) and text[i].isupper():
                string += LETTERS[text[i].lower()]
                i += 1
            continue

        # Handle standalone period (as punctuation, not part of a decimal)
        if token == ".":
            string += PUNCTUATION["."]  # Direct Braille for period

        elif token in LETTERS:
            string += LETTERS[token]
        elif token in PUNCTUATION:
            string += PUNCTUATION[token]

        i += 1

    return string

def translate_to_text(text):
    string = ""
    capitalFlag = False
    numFlag = False

    for i in range(0, len(text), 6):
        cur = text[i:i + 6]

        # Handle capital letter marker
        if cur == KEYS["capital_follows"]:
            capitalFlag = True
            continue  # Skip to the next character after applying the flag

        # Handle number marker
        elif cur == KEYS["number_follows"]:
            numFlag = True
            continue  # Skip this marker and move to the next character

        # Handle space
        if cur == "......":
            string += " "
            continue

        # Process numbers when number flag is set
        if numFlag:
            if cur in NUMBERS.values():
                for key, value in NUMBERS.items():
                    if value == cur:
                        string += key  # Add the corresponding number
            numFlag = False  # Reset the number flag after processing the digit
            continue  # Skip further processing for this character

        # Process capital letters when capital flag is set
        if capitalFlag:
            if cur in LETTERS.values():
                for key, value in LETTERS.items():
                    if value == cur:
                        string += key.upper()  # Add the capital letter
            capitalFlag = False  # Reset the capital flag
            continue

        # Handle punctuation and letters
        if cur in PUNCTUATION.values():
            for key, value in PUNCTUATION.items():
                if value == cur:
                    string += key  # Add punctuation
                    break
        elif cur in LETTERS.values():
            for key, value in LETTERS.items():
                if value == cur:
                    string += key  # Add the lowercase letter

    return string

def main():
    args = sys.argv
    if len(args) > 2:
        texts = args[1:]
        text = " ".join(texts)
    else:
        text = args[1]

    if len(text) % 6 == 0 and all(char in "O." for char in text):
        val = translate_to_text(text)
        print(val)
    else:
        val = translate_to_braille(text)
        print(val)

if __name__ == "__main__":
    main()

