import sys

# Casual Braille dictionary mapping: Letters, numbers, capitalization, and spaces
BRAILLE_DICT = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO..",  # Numbers
    " ": "......",  # Space
    "capital": ".....O",  # Capital letter marker
    "number": ".O.OOO"  # Number mode marker
}

# Reverse lookup for Braille-to-English conversion
REVERSE_BRAILLE_DICT = {v: k for k, v in BRAILLE_DICT.items()}


def is_braille(input_string):
    """Figure out if we're looking at Braille based on 'O' and '.' characters."""
    return all(c in 'O.' for c in input_string)


def translate_to_braille(text):
    """Converts English to Braille, plain and simple."""
    braille_output = []
    number_mode = False

    for char in text:
        if char.isdigit() and not number_mode:
            # Flip to number mode, only once per sequence
            braille_output.append(BRAILLE_DICT["number"])
            number_mode = True

        if char.isalpha():
            if char.isupper():
                # Capital marker for the next letter
                braille_output.append(BRAILLE_DICT["capital"])
            braille_output.append(BRAILLE_DICT[char.lower()])
        elif char.isdigit():
            braille_output.append(BRAILLE_DICT[char])
        elif char == " ":
            braille_output.append(BRAILLE_DICT[" "])
            number_mode = False  # Reset number mode after a space

    return ''.join(braille_output)


def translate_to_english(braille):
    """Converts Braille to plain English."""
    result = []
    i = 0
    capital_mode = False
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i + 6]  # Braille characters are chunks of 6

        if symbol == BRAILLE_DICT["capital"]:
            capital_mode = True
            i += 6
        elif symbol == BRAILLE_DICT["number"]:
            number_mode = True
            i += 6
        else:
            char = REVERSE_BRAILLE_DICT.get(symbol, "")
            if number_mode:
                result.append(char)
            elif capital_mode:
                result.append(char.upper())  # Capitalize the next letter
                capital_mode = False
            else:
                result.append(char)
            if char == " ":
                number_mode = False  # Reset number mode after a space
            i += 6

    return ''.join(result)


def main():
    """Takes input and decides which way to translate: English -> Braille or Braille -> English."""
    # Combine all the arguments into one string
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    # Grab everything passed in after the script name, joining them with spaces
    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        # If it's Braille, we translate to English
        print(translate_to_english(input_string))
    else:
        # Otherwise, it's English and we go to Braille
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()

