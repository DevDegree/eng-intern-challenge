#By: Ahmed Ali


import sys

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_DECIMAL_POINT = ".O...O"

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", ".": "..OO.O", ",": "..O...", "?": "..OOO.", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", " ": "......"
}

number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english[".O...O"] = "."

braille_to_number = {v: k for k, v in number_to_braille.items()}


def main():
    if len(sys.argv) < 2:
        print("Invalid Amount of arguments")
        return

    input_str = " ".join(sys.argv[1:])

    # Improved detection for Braille vs English input
    if all(c in ['O', '.'] for c in input_str):  # Braille only contains 'O' and '.'
        convert_to_english(input_str)
    else:
        convert_to_braille(input_str)


def convert_to_braille(text):
    is_first_number = True
    number_follows = False
    output = []

    for character in text:
        if character not in number_to_braille and character.lower() not in english_to_braille:
            print(
                "All character must be a-z, A-Z, 0-9, '.', ',', '?', '!', ':', ';', '-', '/', '<', '>', '(', ')', or ' '")
            return

        if character.isupper() and not number_follows:
            output.append(BRAILLE_CAPITAL_FOLLOWS)
            braille_character = english_to_braille[character.lower()]
            output.append(braille_character)
            # number_follows = False  # Reset after capital letter
        elif character == " ":
            is_first_number = True
            output.append(english_to_braille[character])
            number_follows = False  # Reset after space
        elif character.isdigit():
            if is_first_number:
                output.append(BRAILLE_NUMBER_FOLLOWS)
                is_first_number = False
            output.append(number_to_braille[character])
            number_follows = True  # Numbers are following
        elif character == "." and number_follows:
            # Prepend the decimal point with `.O...O` if inside a number
            output.append(BRAILLE_DECIMAL_POINT)
        else:
            output.append(english_to_braille[character])
            number_follows = False  # Reset after any non-number and non-decimal

    # Print the continuous output without any spaces between
    print("".join(output))


def convert_to_english(braille_str):
    if len(braille_str) % 6 != 0:
        print("Invalid braille, each braille character should be 6 in length")
        return

    seperated_braille_arr = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]
    capital_follows = False
    number_follows = False

    output = []

    for character in seperated_braille_arr:
        if (character not in braille_to_number and character not in braille_to_english
                and character != BRAILLE_CAPITAL_FOLLOWS and character != BRAILLE_NUMBER_FOLLOWS
                and character != BRAILLE_DECIMAL_POINT):
            print("One or more braille characters are invalid")
            return

        if character == BRAILLE_CAPITAL_FOLLOWS:
            capital_follows = True
        elif character == BRAILLE_NUMBER_FOLLOWS:
            number_follows = True
        elif capital_follows:
            english_character = braille_to_english[character]
            output.append(english_character.upper())
            capital_follows = False
        elif character == "......":
            english_character = braille_to_english[character]
            output.append(english_character)
        elif number_follows:
            english_number = braille_to_number[character]
            output.append(english_number)
        else:
            english_character = braille_to_english[character]
            output.append(english_character)

    print("".join(output))


if __name__ == "__main__":
    main()

