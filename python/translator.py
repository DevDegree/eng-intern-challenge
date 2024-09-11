import sys

# Braille to English (letters only)
BRAILLE_TO_ENGLISH_LETTERS = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z"
}

# Braille to English (numbers only)
BRAILLE_TO_ENGLISH_NUMBERS = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

# English to Braille (letters only)
ENGLISH_TO_BRAILLE_LETTERS = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO"
}

# English to Braille (numbers only)
ENGLISH_TO_BRAILLE_NUMBERS = {
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

# Special symbols
ENGLISH_TO_BRAILLE_SPECIAL = {
    "Capital": ".....O",  # Capital letter follows
    "Number": ".O.OOO",  # Number follows
    "Space": "......"  # Space
}

# Function that translates English to Braille
def english_to_braille(input_string):
    result = []
    number_mode = False

    for char in input_string:
        # Handles numbers
        if char.isdigit():
            if not number_mode:
                result.append(ENGLISH_TO_BRAILLE_SPECIAL["Number"])  # Adds number mode symbol
                number_mode = True  # Enters number mode
            result.append(ENGLISH_TO_BRAILLE_NUMBERS[char])  # Translates the number
            continue  # Skips further processing for numbers

        # Exits number mode when we encounter a non-digit
        if not char.isdigit() and number_mode:
            number_mode = False  # Exits number mode

        # Handles capital letters
        if char.isupper():
            result.append(ENGLISH_TO_BRAILLE_SPECIAL["Capital"])  # Adds capital symbol

        # Converts to uppercase for dict lookup
        char = char.upper()

        # Translates letters
        if char in ENGLISH_TO_BRAILLE_LETTERS:
            result.append(ENGLISH_TO_BRAILLE_LETTERS[char])

        # Handles spaces
        if char == " ":
            if result and result[-1] != ENGLISH_TO_BRAILLE_SPECIAL["Space"]:
                result.append(ENGLISH_TO_BRAILLE_SPECIAL["Space"])  # Adds space in Braille
            number_mode = False  # Exits number mode when space is encountered

    return ''.join(result)

# Function that translates Braille to English
def braille_to_english(input_string):
    result = []
    braille_cells = [input_string[i:i + 6] for i in range(0, len(input_string), 6)]
    number_mode = False
    capital_mode = False

    for cell in braille_cells:
        # Handles capital letter signal
        if cell == ".....O":  # Capital signal found
            capital_mode = True
            continue

        # Handles number signal
        if cell == ".O.OOO":  # Number signal found
            number_mode = True
            continue

        # Handles numbers when number mode is ON
        if number_mode and cell in BRAILLE_TO_ENGLISH_NUMBERS:
            result.append(BRAILLE_TO_ENGLISH_NUMBERS[cell])  # Appends number
            continue  # Stays in number mode until space or capital mode occurs

        # Handles capital letters (when capital mode is ON)
        if capital_mode and cell in BRAILLE_TO_ENGLISH_LETTERS:
            result.append(BRAILLE_TO_ENGLISH_LETTERS[cell].upper())  # Appends capital letter
            capital_mode = False  # Resets capital mode after one letter
            continue

        # Handles lowercase letters
        if cell in BRAILLE_TO_ENGLISH_LETTERS:
            result.append(BRAILLE_TO_ENGLISH_LETTERS[cell].lower())  # Appends lowercase letter

        # Handles spaces
        if cell == "......":
            result.append(" ")  # Appends space
            number_mode = False  # Resets number mode after a space

    return ''.join(result)

# Determines translation direction
def translate(input_string):
    if set(input_string).issubset({"O", "."}):  # If input is Braille
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)

# Gets input from command line arguments
if __name__ == "__main__":
    input_string = ' '.join(sys.argv[1:])  # Join all arguments with a space
    print(translate(input_string))

