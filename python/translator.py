import sys

char_to_braille = {
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
    "cap_follows": ".....O",
    "number_follows": ".O.OOO",
}

braille_to_char_letters_space_follows = {}
braille_to_char_numbers = {}

for char, braille in char_to_braille.items():
    if char.isnumeric():
        braille_to_char_numbers[braille] = char
    else:
        braille_to_char_letters_space_follows[braille] = char


def identify_lang(input_str: str) -> bool:
    """Determines whether the input string is written in English or Braille format.

    Args:
        input_str (str): The input string provided (either English or Braille).

    Returns:
        bool: True if the input is identified as English, False if Braille.
    """

    return not set(input_str).issubset({"O", "."})


def convert_english_to_braille(input_str: str) -> str:
    """Converts the given English input string into its Braille representation.

    Args:
        input_str (str): A string of English text (lowercase/uppercase).

    Returns:
        str: The corresponding Braille translation in string format.
    """

    braille_str = ""
    prevNumeric = False

    for i in input_str:
        if i.isupper():
            braille_str += char_to_braille["cap_follows"]
        elif i.isnumeric():
            if not prevNumeric:
                braille_str += char_to_braille["number_follows"]
            prevNumeric = True

        braille_str += char_to_braille[i.lower()]
    return braille_str


def convert_braille_to_english(input_str: str) -> str:
    """Converts a Braille string into its English equivalent.

    Args:
        input_str (str): A string in Braille format (dots as O and periods).

    Returns:
        str: The corresponding English translation of the Braille input.
    """

    english_str = ""
    capitalFollows = False
    numberFollows = True

    for i in range(0, len(input_str), 6):
        six_char_block = input_str[i : i + 6]
        if braille_to_char_letters_space_follows[six_char_block] == "cap_follows":
            capitalFollows = True
            numberFollows = False
            continue
        elif braille_to_char_letters_space_follows[six_char_block] == "number_follows":
            numberFollows = True
            capitalFollows = False
            continue
        elif braille_to_char_letters_space_follows[six_char_block] == " ":
            numberFollows = False
            capitalFollows = False
            english_str += braille_to_char_letters_space_follows[six_char_block]
            continue

        if numberFollows:
            english_str += braille_to_char_numbers[six_char_block]
        elif capitalFollows:
            english_str += braille_to_char_letters_space_follows[six_char_block].upper()
            capitalFollows = False
        else:
            english_str += braille_to_char_letters_space_follows[six_char_block]

    return english_str


def convert(input_str: str) -> str:
    """Main function that decides which conversion to apply (English to Braille or Braille to English).

    Args:
        input_str (str): The input string (English or Braille) to be converted.

    Returns:
        str: The converted string in either Braille or English.
    """

    if identify_lang(input_str):
        return convert_english_to_braille(input_str)

    return convert_braille_to_english(input_str)


if __name__ == "__main__":
    input_str = " ".join(sys.argv[1:])

    print(convert(input_str))
