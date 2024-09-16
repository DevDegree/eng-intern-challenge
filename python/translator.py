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
    for token in text:
        if token.isdigit():
            string += KEYS["number_follows"]  # Add number marker before any digits

        if token.isupper():
            string += KEYS["capital_follows"]
            token = token.lower()

        # Handle standalone period (as punctuation, not part of a decimal)
        if token == ".":
            string += PUNCTUATION["."]  # Direct Braille for period

        

        elif token in LETTERS:
            string += LETTERS[token]
        elif token in NUMBERS:
            string += NUMBERS[token]
        elif token in PUNCTUATION:
            string += PUNCTUATION[token]

    return string


def translate_to_text(text):
    string = ""
    capitalFlag = False
    numFlag = False
    prevChar = None  # Keeps track of the previous character for context

    for i in range(0, len(text), 6):
        cur = text[i:i + 6]

        if cur == KEYS["capital_follows"]:
            capitalFlag = True
            continue  # Skip to the next character after applying the flag

        elif cur == KEYS["number_follows"]:
            numFlag = True
            continue  # Skip this marker and move to the next character

        # Process numbers when number flag is set
        if numFlag:
            if cur in NUMBERS.values():
                for key, value in NUMBERS.items():
                    if value == cur:
                        string += key
            numFlag = False  # Reset the number flag after processing the digit

        # Process capital letters when capital flag is set
        elif capitalFlag:
            if cur in LETTERS.values():
                for key, value in LETTERS.items():
                    if value == cur:
                        string += key.upper()
            capitalFlag = False  # Reset the capital flag after processing the letter

        # Handle ambiguous cases: punctuation vs letters
        else:
            # First, try matching punctuation (give priority to punctuation)
            if cur in PUNCTUATION.values():
                for key, value in PUNCTUATION.items():
                    if value == cur:
                        # Only add punctuation if it's not directly preceded by another letter
                        if prevChar and prevChar in LETTERS.values():
                            # If previous char was a letter, treat it as a letter
                            for letter_key, letter_value in LETTERS.items():
                                if letter_value == cur:
                                    string += letter_key
                        else:
                            # Add punctuation
                            string += key
                        prevChar = cur  # Update previous character to current

            # If not punctuation, treat it as a letter
            if cur in LETTERS.values() and cur not in PUNCTUATION.values():
                for key, value in LETTERS.items():
                    if value == cur:
                        string += key
                prevChar = cur  # Update previous character to current

    return string


def main():
    
    args = sys.argv
    print(args)
    text = args

    # text = input("Enter Braille or Text: ")
    if len(text) % 6 == 0 and all(char in "O." for char in text):
        # print("Translating braille to text")
        val = translate_to_text(text)
        print(val)
        # print(translate_to_braille(val))
    else:
        # print("Translating text to braile")
        val = translate_to_braille(text)
        print(val)
        # print(translate_to_text(val))

if __name__ == "__main__":
    main()
