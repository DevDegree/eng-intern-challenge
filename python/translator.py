import sys


BRAILLE_CHAR_LEN = 6

ENGLISH_TO_BRAILLE_CHARS = {
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
    " ": "......",
}

ENGLISH_TO_BRAILLE_NUMS = {
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

CAPITAL_FOLLOWS_BRAILLE = ".....O"

NUMBER_FOLLOWS_BRAILLE = ".O.OOO"

VALID_BRAILLE_CHARS = set(
    list(ENGLISH_TO_BRAILLE_CHARS.values())
    + list(ENGLISH_TO_BRAILLE_NUMS.values())
    + [CAPITAL_FOLLOWS_BRAILLE, NUMBER_FOLLOWS_BRAILLE]
)

VALID_ENGLISH_CHARS = set(
    list(ENGLISH_TO_BRAILLE_CHARS.keys())
    + [char.upper() for char in list(ENGLISH_TO_BRAILLE_CHARS.keys())]
    + list(ENGLISH_TO_BRAILLE_NUMS.keys())
)


def swap_dict_keys_values(d):
    """
    Swap the keys and values of a given dictionary.

    Args:
        d (dict): The dictionary whose keys and values will be swapped.

    Returns:
        dict: A new dictionary with keys and values swapped.
    """
    return {value: key for key, value in d.items()}


BRAILLE_TO_ENGLISH_CHARS = swap_dict_keys_values(ENGLISH_TO_BRAILLE_CHARS)

BRAILLE_TO_ENGLISH_NUMS = swap_dict_keys_values(ENGLISH_TO_BRAILLE_NUMS)


def get_command_line_input():
    """
    Retrieve input from the command-line arguments.

    If no argument is provided, the function will print an error message and exit.

    Returns:
        str: The command-line arguments combined into a single string with " " as the delimiter
    """
    if len(sys.argv) < 2:
        sys.exit("At least one argument required")

    return " ".join(sys.argv[1:])


def chunk_string_by_length(string, chunk_len):
    """
    Split a string into chunks of a specified length.

    Args:
        string (str): The string to be split.
        chunk_len (int): The length of each chunk.

    Returns:
        list[str]: A list of string chunks of the specified length.
    """
    return [string[i : i + chunk_len] for i in range(0, len(string), chunk_len)]


def is_braille(string):
    """
    Check if the input string is a valid Braille sequence.

    The string must be a multiple of `BRAILLE_CHAR_LEN` and consist of valid Braille characters.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is valid Braille, False otherwise.
    """
    if not string or len(string) % BRAILLE_CHAR_LEN != 0:
        return False

    string_chunks = chunk_string_by_length(string, BRAILLE_CHAR_LEN)

    return all(string_chunk in VALID_BRAILLE_CHARS for string_chunk in string_chunks)


def is_english(string: str) -> bool:
    """
    Check if the input string consists only of valid English characters.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string contains only valid English characters, False otherwise.
    """
    return string and all(char in VALID_ENGLISH_CHARS for char in string)


def translate_to_english(braille_text):
    """
    Translate a Braille string to English.

    Handles capital letters and numbers using control characters like `CAPITAL_FOLLOWS_BRAILLE`
    and `NUMBER_FOLLOWS_BRAILLE`.

    Args:
        braille_text (str): The Braille string to translate.

    Returns:
        str: The translated English string.
    """

    english_text = ""

    is_capital = False
    is_num = False

    braille_chars = chunk_string_by_length(braille_text, BRAILLE_CHAR_LEN)

    for braille_char in braille_chars:
        if braille_char == CAPITAL_FOLLOWS_BRAILLE:
            is_capital = True

        elif braille_char == NUMBER_FOLLOWS_BRAILLE:
            is_capital = False
            is_num = True

        elif braille_char == ENGLISH_TO_BRAILLE_CHARS[" "]:
            is_capital = False
            is_num = False
            english_text += BRAILLE_TO_ENGLISH_CHARS[braille_char]

        elif is_capital:
            is_capital = False
            english_text += BRAILLE_TO_ENGLISH_CHARS[braille_char].upper()

        elif is_num:
            english_text += BRAILLE_TO_ENGLISH_NUMS[braille_char]

        else:
            english_text += BRAILLE_TO_ENGLISH_CHARS[braille_char]

    return english_text


def translate_to_braille(english_text):
    """
    Translate an English string to Braille.

    Handles capital letters and numbers by prefixing with control characters
    `CAPITAL_FOLLOWS_BRAILLE` and `NUMBER_FOLLOWS_BRAILLE`.

    Args:
        english_text (str): The English string to translate.

    Returns:
        str: The translated Braille string.
    """

    braille_text = ""

    for i, english_char in enumerate(english_text):
        if english_char in ENGLISH_TO_BRAILLE_CHARS:
            braille_text += ENGLISH_TO_BRAILLE_CHARS[english_char]

        elif english_char.lower() in ENGLISH_TO_BRAILLE_CHARS:
            braille_text += (
                CAPITAL_FOLLOWS_BRAILLE + ENGLISH_TO_BRAILLE_CHARS[english_char.lower()]
            )

        else:
            if i == 0 or english_text[i - 1] not in ENGLISH_TO_BRAILLE_NUMS:
                braille_text += NUMBER_FOLLOWS_BRAILLE

            braille_text += ENGLISH_TO_BRAILLE_NUMS[english_char]

    return braille_text


def main():
    """
    Main function to handle input, check if it's Braille or English, and perform the appropriate translation.

    If the input is not valid Braille or English, it prints an error message and exits.
    """
    user_input = get_command_line_input()

    if is_braille(user_input):
        print(translate_to_english(user_input))

    elif is_english(user_input):
        print(translate_to_braille(user_input))

    else:
        sys.exit("Input is not english nor braille.")


if __name__ == "__main__":
    main()
