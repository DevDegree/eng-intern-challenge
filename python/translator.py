user_string = str(input())

# Braille alphabet of all letters and special characters
braille_alphabet = {
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
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO"
}

# Braille alphabet of all digits
braille_numbers = {
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

# Given an english string, convert it to braille string


def convert_to_braille():
    braille_string = ""
    index = 0

    while index < len(user_string):  # Goes through the user string
        char = user_string[index]  # Gets the first english character

        if char.isupper():  # Checks if character is uppercase letter and adds the capital braille
            braille_string += braille_alphabet["capital"]
        elif char.isnumeric():  # Checks if character is a number and adds the number braille
            if (index >= 1 and user_string[index - 1].isnumeric() == False and user_string[index - 1] != ".") or (index == 0):
                braille_string += braille_alphabet["number"]
        # Checks if character is a decimal and adds the decimal braille
        elif char == "." and index <= len(user_string) - 1 and user_string[index + 1].isnumeric():
            braille_string += braille_alphabet["decimal"]

        if char.isalpha():  # Checks if character is a letter and adds the corresponding letter's braille
            braille_string += (braille_alphabet[char.lower()])
        elif char.isdigit():  # Checks if character is a number and adds the corresponding number's braille
            braille_string += (braille_numbers[char])
        else:  # Checks if character is a special character and adds the corresponding character's braille
            if char in braille_alphabet:
                braille_string += (braille_alphabet[char])

        index += 1
    return braille_string


# Given a braille string, converts it to an english string
def convert_to_english():
    english_string = ""
    index = 0

    # Splits the string into 6 characters each to help make iteration easier
    split_string = [user_string[i:i+6] for i in range(0, len(user_string), 6)]

    # Flags that help with adding subsequent braille characters correctly
    is_capital = False
    is_number = False
    is_decimal = False

    for index in range(len(split_string)):  # Goes through the 6 character string list
        # Gets the 6 character braille string
        curr_braille_char = split_string[index]

        # Only check for the next character if it exists
        if len(split_string) >= 2 and index < len(split_string) - 1:
            next_braille_char = split_string[index+1]
        else:
            # Else there isn't any character (assuming that there is only 1 6 character braille string)
            next_braille_char = None

        # Sets the appropriate flags if there is a capita, number, or decimal following
        # It then continues on to the next character
        if curr_braille_char == braille_alphabet["capital"] and next_braille_char:
            is_capital = True
            continue
        elif curr_braille_char == braille_alphabet["number"] and next_braille_char:
            is_number = True
            continue
        elif curr_braille_char == braille_alphabet["decimal"] and next_braille_char:
            is_decimal = True
            # We will assume that for decimals, braille doesn't include the "." after decimal following braille: "..OO.O"
            english_string += "."
            continue

        """If a space is found, reset the number flag
        This is due to the assumption that when braille number follows symbol is read
        all following symbols are numbers until the next space"""
        if curr_braille_char == braille_alphabet[" "]:
            is_number = False
            english_string += " "
            continue

        # Now check the current Braille character based on the state flags
        if is_number == False:  # Only check through alphabet dictionary if number follows symbol is read
            for character, brailleChar in braille_alphabet.items():
                if brailleChar == curr_braille_char:  # Finds the exact braille string
                    if is_capital:  # Checks if capital follows symbol is read and adds the uppercase letter
                        english_string += character.upper()
                        is_capital = False  # Reset after one capital letter
                    elif is_decimal:  # Checks if decimal follows symbol is read and adds the decimal
                        english_string += "."
                        is_decimal = False  # Reset after decimal
                    else:  # Else we just add the corresponding english letter
                        english_string += character
                    break  # Exit the loop once a match is found

        else:  # Only check through numbers dictionary if number follows symbol is read
            for character, brailleChar in braille_numbers.items():
                if brailleChar == curr_braille_char:
                    english_string += character  # Adds the number to the resulting string
                    break

    return english_string


if all(char in "O." for char in user_string):  # Checks if the string is a braille string
    print(convert_to_english())
else:
    print(convert_to_braille())
