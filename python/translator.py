import sys

""" Important assumptions for this program:
1. The only characters that are being translated to and from morse code are number 0-9 and capital/lowercase alphabet.
"""

CAPITAL = 0
NUMBER = 1
ALPHABET_OR_SYMBOL = 2
SPACE = 3


def get_token_type(token: str) -> int:
    if len(token) != 6:
        raise ValueError("Token must be 6 characters long!")

    if token == ".....O":
        return CAPITAL
    elif token == ".O.OOO":
        return NUMBER
    elif token == "......":
        return SPACE
    else:
        return ALPHABET_OR_SYMBOL


# alphanumeric_dictionary = {
#     "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
#     "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
#     "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
#     "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", "1": "O.....", "2": "O.O...",
#     "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
#     "0": ".OOO..", ".": "O.O.O.", ",": "O.OOO.", "?": "O..OO.", "!": "O.OO..", ":": "O....O", ";": "O..O.O",
#     "-": "O...O.", "/": "..O...", "<": "..OO..", ">": "..OO..", "(": "O.O...", ")": "OO...."
# }

# morse_dictionary = {
#     "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g",
#     "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n",
#     "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u",
#     "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z", "O.....": "1", "O.O...": "2",
#     "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
#     ".OOO..": "0", "O.O.O.": ".", "O.OOO.": ",", "O..OO.": "?", "O.OO..": "!", "O....O": ":", "O..O.O": ";",
#     "O...O.": "-", "..O...": "/", "..OO..": "<", "..OO..": ">", "O.O...": "(", "OO....": ")"
# }


def is_morse_code(check_string: str) -> bool:
    """
    Checks whether the passed string is in morse code.
    :param check_string: The string to check.
    :return: True if the string is in morse else false.
    """
    # The shortest morse string is of length 6 because that's the size of a single morse token.
    if len(check_string) < 6:
        return False

    # Periods are not used in the specifications and all morse tokens use at least one period.
    for i in range(6):
        if check_string[i] == ".":
            return True

    return False

    # Alternative if periods are used
    # for character in check_string:
    #     if character != "." and character != "0":
    #         return False
    # return True


def translate_morse(translate_string: str) -> str:
    if len(translate_string) % 6 != 0:
        raise ValueError("Invalid morse string")

    index = 0

    # Gets the 6 character morse token
    def get_token():
        nonlocal index
        if index >= len(translate_string):
            return None
        current_token = translate_string[index:index + 6]
        index += 6
        return current_token

    # Translates morse code to a number
    def morse_to_number(morse_code: str) -> str:
        morse_to_number_dictionary = {"O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
                                      "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}
        try:
            return morse_to_number_dictionary[morse_code]
        except KeyError:
            raise ValueError("Invalid morse code!")

    # Translates morse code to an alphabet or a symbol
    def morse_to_alphabet_or_symbol(morse_code: str) -> str:
        morse_to_alphabet_dictionary = {"O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
                                        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
                                        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
                                        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
                                        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
                                        "O..OOO": "z", "......": " "}
        try:
            return morse_to_alphabet_dictionary[morse_code]
        except KeyError:
            raise ValueError("Invalid morse code!")

    # Gets a number
    def get_number(morse_string):
        number_string = ""
        i = 0
        while True:
            if i + 6 >= len(morse_string):
                break
            morse_token = morse_string[i: i + 6]
            if morse_token == "......":
                break
            number_string += morse_to_number(morse_token)
            i += 6
        return number_string

    translated_string = ""
    while True:
        if index >= len(translate_string):
            break
        token = get_token()
        token_type = get_token_type(token)
        if token_type == CAPITAL:
            token = get_token()
            if token is None:
                break
            translated_string += morse_to_alphabet_or_symbol(token).capitalize()
        elif token_type == NUMBER:
            token = get_token()
            while token is not None and get_token_type(token) != SPACE:
                translated_string += morse_to_number(token)
                token = get_token()
            if token is None:
                return translated_string
            if get_token_type(token) == SPACE:
                translated_string += " "
        else:
            translated_string += morse_to_alphabet_or_symbol(token)

    return translated_string


def translate_alphabet(translate_string: str) -> str:
    def alphabet_to_morse(alphabet: str) -> str:
        is_capital = alphabet.isupper()
        alphabet = alphabet.lower()
        capital_follows = ".....O"
        alphabet_to_morse_dictionary = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
                                        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
                                        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
                                        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
                                        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
                                        "z": "O..OOO", " ": "......"
                                        }
        try:
            return (capital_follows if is_capital else "") + alphabet_to_morse_dictionary[alphabet]
        except KeyError:
            raise ValueError("Invalid morse code!")

    def number_to_morse(number):
        number_to_morse_dictionary = {"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
                                      "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."}
        try:
            return number_to_morse_dictionary[number]
        except KeyError:
            raise ValueError("Invalid morse code!")

    number_follows = ".O.OOO"
    translated_string = ""
    index = 0
    while index < len(translate_string):
        character = translate_string[index]
        if character.isnumeric():
            translated_string += number_follows
            while True:
                translated_string += number_to_morse(character)
                index += 1
                if index >= len(translate_string):
                    return translated_string
                character = translate_string[index]
                if character == " ":
                    space_morse = "......"
                    translated_string += space_morse
                    index += 1
                    break
        else:
            translated_string += alphabet_to_morse(character)
            index += 1

    return translated_string


def get_morse_tokens(morse_string):
    return [morse_string[i: i + 6] for i in range(0, len(morse_string), 6)]


if __name__ == "__main__":
    # Get args
    args = sys.argv
    string = "".join([args[i] + " " for i in range(1, len(args)) if i < len(args)])
    string = string[:-1]

    if is_morse_code(string):
        print(translate_morse(string))
    else:
        print(translate_alphabet(string))

