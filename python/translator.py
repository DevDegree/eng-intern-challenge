import sys

# Dictionary to map English letters to Braille characters
ENGLISH_TO_BRAILLE_LETTERS = {
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
    "0": ".OOO..",
}

ENGLISH_TO_BRAILLE_SPECIAL_CHARS = {
    "capital": ".....O",
    "number": ".O.OOO",
    "space": "......",
}

# Dictionary to map Braille characters to English letters
BRAILLE_TO_ENGLISH_LETTERS = {
    val: key for key, val in ENGLISH_TO_BRAILLE_LETTERS.items()
}

BRAILLE_TO_ENGLISH_NUMBERS = {
    val: key for key, val in ENGLISH_TO_BRAILLE_NUMBERS.items()
}


def translate_to_braille(text):
    """
    Translate the given English text to braille text.
    Handles all the special cases like capital letters and numbers.

    Args:
        text (str): input text in English

    Returns:
        str: output text in braille
    """
    # Initialize the flags and the output string
    is_number = False
    output = ""

    for english_char in text:
        braille_char = ""

        # If the character is a number, add the braille number
        if english_char.isnumeric():
            if is_number == False:
                braille_char = ENGLISH_TO_BRAILLE_SPECIAL_CHARS["number"]
                is_number = True
            braille_char += ENGLISH_TO_BRAILLE_NUMBERS[english_char]

        # If the character is a space, add the braille space character
        elif english_char == " ":
            braille_char = ENGLISH_TO_BRAILLE_SPECIAL_CHARS["space"]
            is_number = False

        # If the character is a letter, then also check if it's a capital letter
        elif english_char.lower() in ENGLISH_TO_BRAILLE_LETTERS:
            if english_char.isupper():
                braille_char = ENGLISH_TO_BRAILLE_SPECIAL_CHARS["capital"]
            braille_char += ENGLISH_TO_BRAILLE_LETTERS[english_char.lower()]

        # Add the translated braille character to the output
        output += braille_char
    return output


def translate_to_english(text):
    """
    Translate the given braille text to English text.
    Handles all the special cases like capital letters and numbers.

    Args:
        text (str): input text in braille

    Returns:
        str: translated output text in English
    """
    # Initialize the flags and the output string
    is_capital = False
    is_number = False
    output = ""

    for i in range(0, len(text), 6):
        braille_char = text[i : i + 6]
        english_char = ""

        # If the character is a number,
        if braille_char == ENGLISH_TO_BRAILLE_SPECIAL_CHARS["number"]:
            is_number = True
        # If the character is a capital_follows flag, switch the flag
        elif braille_char == ENGLISH_TO_BRAILLE_SPECIAL_CHARS["capital"]:
            is_capital = True

        else:
            # If the character is a space, add a space to the output and
            # reset the number flag
            if braille_char == ENGLISH_TO_BRAILLE_SPECIAL_CHARS["space"]:
                is_number = False
                english_char += " "
            # If the character is a number, add a number to the output
            elif is_number:
                english_char = BRAILLE_TO_ENGLISH_NUMBERS[braille_char]

            # If the character is a letter, check if it is a capital letter and
            # add the letter to the output
            elif braille_char in BRAILLE_TO_ENGLISH_LETTERS:
                english_char = BRAILLE_TO_ENGLISH_LETTERS[braille_char]
                if is_capital:
                    english_char = english_char.upper()
                    is_capital = False

        # Add the translated English character to the output
        output += english_char
    return output


def is_braille(text):
    """
    Check whether the given text is a valid braille text or not.

    Args:
        text (str): input text

    Returns:
        str: True if the text is a valid braille text, False otherwise
    """
    # If the text is not a multiple of 6 or contains any character other
    # than '.' or 'O', then it is not a valid braille text.
    if len(text) % 6 != 0 or all(char not in ".O" for char in text):
        return False
    else:
        return True


def main():
    """
    Handles the input arguments and calls the appropriate translation function.
    """

    # If no input arguments are provided, print the usage message.
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <str1> <str2> <str3> ...")
        return

    # Join the input arguments and check if they are english or brailler chars.
    input_text = " ".join(sys.argv[1:]).strip()
    if not all(
        char.isdigit() or char.isalpha() or char.isspace() or char == "."
        for char in input_text
    ):
        print(
            "Invalid input. Please use only English letters, numbers, "
            + "spaces or '.' for braille characters."
        )
        return False

    # Call the appropriate translation function based on the valid input text.
    if is_braille(input_text):
        output_text = translate_to_english(input_text)
    else:
        output_text = translate_to_braille(input_text)

    print(output_text)


if __name__ == "__main__":
    main()
