# Braille and English mappings
ENGLISH_TO_BRAILLE = {
    # Letters A-Z
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOO.O", "r": "O.OO.O", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",

    # Numbers 0-9 (Same as A-J with number prefix)
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "number": ".O..OO",  # Number prefix

    # Special characters (punctuation)
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OO.O",
    ":": "..OO..", ";": "..O.O.", "-": "..O..O", "/": "..OOO.",
    "<": ".O..O.", ">": ".OO..O", "(": "..O.OO", ")": "..OO.O",

    # Space
    " ": "......",

    # Capital letter indicator
    "capital": ".O.O.O"
}

# Invert the ENGLISH_TO_BRAILLE mapping for Braille-to-English conversion
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}

def translate(input_str):
    """Translates between English and Braille based on the input."""
    if all(char in 'O.' for char in input_str):
        return translate_to_english(input_str)
    else:
        return translate_to_braille(input_str)

def translate_to_braille(english):
    """Converts English text to Braille."""
    braille = ""
    number_mode = False
    for char in english:
        if char.isupper():
            braille += ENGLISH_TO_BRAILLE["capital"]
            braille += ENGLISH_TO_BRAILLE[char.lower()]
        elif char.isdigit():
            if not number_mode:
                braille += ENGLISH_TO_BRAILLE["number"]
                number_mode = True
            braille += ENGLISH_TO_BRAILLE[char]
        else:
            if number_mode and char == " ":
                number_mode = False
            braille += ENGLISH_TO_BRAILLE.get(char, "")
    return braille

def translate_to_english(braille):
    """Converts Braille to English text."""
    english = ""
    chars = [braille[i:i+6] for i in range(0, len(braille), 6)]  # Split Braille into 6-character chunks
    capital_next = False
    number_mode = False

    for symbol in chars:
        if symbol == ENGLISH_TO_BRAILLE["capital"]:
            capital_next = True
        elif symbol == ENGLISH_TO_BRAILLE["number"]:
            number_mode = True
        else:
            letter = BRAILLE_TO_ENGLISH.get(symbol, "")
            if number_mode and letter in "abcdefghij":
                english += str(ord(letter) - ord('a') + 1)  # Convert a-j to 1-9
            else:
                english += letter.upper() if capital_next else letter
                capital_next = False
            number_mode = False if letter == " " else number_mode
    return english

# Entry point for the script
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        input_str = sys.argv[1]
        print(translate(input_str))
    else:
        print("Please provide a valid input string")

