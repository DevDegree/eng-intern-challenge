import sys

# Note 1: Braille symbol "o" is the same as ">". There is no way to differentiate between the two when
# translating from braille to English. Therefore, I have changed the braille symbol of ">" to all black: "000000"
# Note 2: Not sure what "decimal follows" means.

# Mapping from Braille patterns to English characters
BRAILLE_TO_ENGLISH_MAP = {
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
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    "OOOOOO": ">",
    "O.O..O": "(",
    ".O.OO.": ")",
    "......": " ",
}

# Mapping from English characters to Braille patterns
ENGLISH_TO_BRAILLE_MAP = {english_char: braille_pattern for braille_pattern, english_char in
                          BRAILLE_TO_ENGLISH_MAP.items()}

# Adding additional mappings for uppercase letters and numbers in Braille
ENGLISH_TO_BRAILLE_MAP.update({
    "A": ".....OO.....",
    "B": ".....OO.O...",
    "C": ".....OOO....",
    "D": ".....OOO.O..",
    "E": ".....OOO.O..",
    "F": ".....OOOO...",
    "G": ".....OOOOO..",
    "H": ".....OO.OO..",
    "I": ".....O.OO...",
    "J": ".....O.OOO..",
    "K": ".....OO...O.",
    "L": ".....OO.O.O.",
    "M": ".....OOO..O.",
    "N": ".....OOO.OO.",
    "O": ".....OO..OO.",
    "P": ".....OOOO.O.",
    "Q": ".....OOOOOO.",
    "R": ".....OO.OOO.",
    "S": ".....O.OO.O.",
    "T": ".....O.OOOO.",
    "U": ".....OO...OO",
    "V": ".....OO.O.OO",
    "W": ".....O.OOO.O",
    "X": ".....OOO..OO",
    "Y": ".....OOO.OOO",
    "Z": ".....OO..OOO",
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
})


def is_braille(text):
    """
    Determines if the input text is in Braille format.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if all characters are 'O' or '.', False otherwise.
    """
    return all(char in "O." for char in text)


def braille_to_english(braille_input):
    """
    Translates a Braille string to its English representation.

    Args:
        braille_input (str): The Braille string to translate.

    Returns:
        str: The translated English string.
    """
    translated_text = []
    capitalize_next = False  # Flag to indicate the next character should be capitalized
    number_mode = False  # Flag to indicate that number mode is active

    # Process the input in chunks of 6 characters (each Braille symbol)
    for i in range(0, len(braille_input), 6):
        braille_symbol = braille_input[i:i + 6]

        if braille_symbol in BRAILLE_TO_ENGLISH_MAP:
            english_char = BRAILLE_TO_ENGLISH_MAP[braille_symbol]

            if english_char == "capital":
                capitalize_next = True
            elif english_char == "number":
                number_mode = True
            elif english_char == " ":
                translated_text.append(" ")
                number_mode = False  # Exit number mode after a space
            else:
                if number_mode:
                    # Translate letters to corresponding numbers
                    number_translation = {
                        "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
                        "f": "6", "g": "7", "h": "8", "i": "9", "j": "0"
                    }
                    english_char = number_translation.get(english_char, "ERROR")

                if capitalize_next:
                    english_char = english_char.upper()
                    capitalize_next = False

                translated_text.append(english_char)
        else:
            # If the Braille symbol is not recognized, append "ERROR"
            translated_text.append("ERROR")

    return ''.join(translated_text)


def english_to_braille(english_input):
    """
    Translates an English string to its Braille representation.

    Args:
        english_input (str): The English string to translate.

    Returns:
        str: The translated Braille string.
    """
    translated_braille = []
    number_mode_active = True  # Flag to manage number mode

    for char in english_input:
        if char.isupper():
            # Add the capital indicator before the Braille pattern
            translated_braille.append(ENGLISH_TO_BRAILLE_MAP["capital"])
            char = char.lower()

        if char.isdigit():
            if number_mode_active:
                # Enter number mode by adding the number indicator
                translated_braille.append(ENGLISH_TO_BRAILLE_MAP["number"])
                number_mode_active = False
            # Append the Braille pattern for the digit
            braille_char = ENGLISH_TO_BRAILLE_MAP.get(char, "ERROR")
            translated_braille.append(braille_char)
        elif char == " ":
            # Append space and exit number mode
            number_mode_active = True
            translated_braille.append(ENGLISH_TO_BRAILLE_MAP[" "])
        else:
            # Append Braille pattern for the character and exit number mode
            number_mode_active = True
            braille_char = ENGLISH_TO_BRAILLE_MAP.get(char, "ERROR")
            translated_braille.append(braille_char)

    return ''.join(translated_braille)


def main():
    """
    Main function to handle command-line input and perform translation.

    Usage:
        python3 translator.py <string>
    """
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <string>")
        return

    # Combine all command-line arguments into a single string
    input_string = " ".join(sys.argv[1:])

    if is_braille(input_string):
        # If input is Braille, translate to English
        translated_output = braille_to_english(input_string)
    else:
        # Otherwise, translate English to Braille
        translated_output = english_to_braille(input_string)

    print(translated_output)


if __name__ == "__main__":
    main()
