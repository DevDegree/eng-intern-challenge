import sys

english_to_braille = {"A":"O.....", "B":"O.O...", "C":"OO....", "D":"OO.O..",
                      "E":"O..O..", "F":"OOO...", "G":"OOOO..", "H":"O.OO..",
                      "I":".OO...", "J":".OOO..", "K":"O...O.", "L":"O.O.O.",
                      "M":"OO..O.", "N":"OO.OO.", "O":"O..OO.", "P":"OOO.O.",
                      "Q":"OOOOO.", "R":"O.OOO.", "S":".OO.O.", "T":".OOOO.",
                      "U":"O...OO", "V":"O.O.OO", "W":".OOO.O", "X":"OO..OO",
                      "Y":"OO.OOO", "Z":"O..OOO", "1":"O.....", "2":"O.O...",
                      "3":"OO....", "4":"OO.O..", "5":"O..O..", "6":"OOO...",
                      "7":"OOOO..", "8":"O.OO..", "9":".OO...", "0":".OOO..",
                      "capital_follows":".....O", "number_follows":".O.OOO",
                      "space": "......"}

braille_to_english = {"O.....":"A", "O.O...":"B", "OO....":"C", "OO.O..":"D",
                      "O..O..":"E", "OOO...":"F", "OOOO..":"G", "O.OO..":"H",
                      ".OO...":"I", ".OOO..":"J", "O...O.":"K", "O.O.O.":"L",
                      "OO..O.":"M", "OO.OO.":"N", "O..OO.":"O", "OOO.O.":"P",
                      "OOOOO.":"Q", "O.OOO.":"R", ".OO.O.":"S", ".OOOO.":"T",
                      "O...OO":"U", "O.O.OO":"V", ".OOO.O":"W", "OO..OO":"X",
                      "OO.OOO":"Y", "O..OOO":"Z", ".....O":"capital_follows",
                      ".O.OOO":"number_follows", "......":"space"}

braille_to_nums = {"O.....":"1", "O.O...":"2", "OO....":"3", "OO.O..":"4",
                   "O..O..":"5", "OOO...":"6", "OOOO..":"7", "O.OO..":"8",
                   ".OO...":"9", ".OOO..":"0"}


def braille_translator(message: str) -> str:
    """
    This function takes in a string in English and translates to Braille.

    All the characters must be letters A-Z or a-z or numbers 0-9, with
    the ability to include spaces.
    """
    output_message = ""
    number_read = False
    # This bool will track if we are currently reading number(s)
    for c in message:
        if c.isupper():
            # If the character is upper case
            output_message += english_to_braille['capital_follows']
            output_message += english_to_braille[c.upper()]

        elif c.isnumeric():
            if not number_read:
                # If this is the first number we have read in this collection
                # of numbers
                number_read = True
                output_message += english_to_braille['number_follows']

            output_message += english_to_braille[c]

        elif number_read and c.isalpha():
            # When transitioning from numbers to letters, reset number_read
            number_read = False
            output_message += english_to_braille[c.upper()]

        elif c == " ":
            # If a space is read, then number_read should be set to False
            number_read = False
            output_message += english_to_braille['space']

        else:
            output_message += english_to_braille[c.upper()]

    return output_message


def english_translator(message: str) -> str:
    """
    This function takes in a string in Braille and translates to English.

    Each character is stored as a series of '.' or 'O' (the letter O), the
    output will only be letters A-Z or a-z or numbers 0-9, with the ability
    to include spaces.
    """
    length = len(message)
    if length % 6 != 0:
        return ("This braille message is not n*6 characters long where n is "
                "any natural number")

    output_message = ""
    number_read = False
    capital_follows = False
    i = 0

    while i < length:
        current_substring = message[i:i+6]

        if capital_follows:
            output_message += braille_to_english[current_substring]
            capital_follows = False

        else:

            if number_read and braille_to_english[current_substring] != 'space':
                # If number_follows was read previously and a space has not
                # been encountered yet, call the braille_to_nums dict
                char = braille_to_nums[current_substring]

            else:
                char = braille_to_english[current_substring]

            if char == "number_follows":
                number_read = True
                char = ""
            elif char == "capital_follows":
                capital_follows = True
                char = ""
            elif char == "space":
                number_read = False
                char = " "

            output_message += char.lower()
            # Lower the character since by default the characters are stored
            # as capitals in the dicts

        i += 6

    return output_message


input_message = ""
if len(sys.argv) > 1:
    input_message = sys.argv[1]

if "." in input_message:
    # Use Braille -> English translator in this case
    message = english_translator(input_message)
    message = message.replace("\n", "")
    print(message.strip())
else:
    message = braille_translator(input_message)
    message = message.replace("\n", "")
    print(message.strip())
