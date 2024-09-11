import sys


def is_braille(string_list):

    if len(string_list) > 1:
        for i in range(len(string_list)):
            if not string_list[i].isalnum():
                return "Invalid"
        return False

    string = string_list[0]

    contains_dot = False

    for i in range(len(string)):
        if string[i] == ".":
            contains_dot = True

        if string[i] != "." and string[i] != "O":
            if string.isalnum():
                return False
            else:
                return "Invalid"

    if contains_dot and len(string) % 6 == 0:
        return True
    else:
        return "Invalid"


def main():

    braille_to_characters = {
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
    }

    characters_to_braille = {v: k for k, v in braille_to_characters.items()}

    braille_to_numbers = {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
    }

    numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}

    braille_space = "......"
    braille_capital_follows = ".....O"
    braille_number_follows = ".O.OOO"

    user_input = sys.argv[1:]

    if len(user_input) == 0:
        print("")
        return

    is_braille_var = is_braille(user_input)

    if is_braille_var == "Invalid":
        print("Invalid Input")

    final_output = ""
    capital = False
    number = False

    if is_braille_var:
        user_input = user_input[0]

        for i in range(int(len(user_input) / 6)):
            next_braille = user_input[i * 6 : (i + 1) * 6]
            if next_braille == braille_space:
                final_output += " "
                number = False
                capital = False
            elif number and next_braille != braille_space:
                final_output += braille_to_numbers[next_braille]
            elif capital:
                final_output += braille_to_characters[next_braille].upper()
                capital = False
            elif next_braille == braille_capital_follows:
                capital = True
            elif next_braille == braille_number_follows:
                number = True
            else:
                final_output += braille_to_characters[next_braille]
    else:
        for i in range(len(user_input)):
            number = False
            next_word = user_input[i]

            for j in range(len(next_word)):
                next_character = next_word[j]

                if number:
                    if 48 <= ord(next_character) <= 57:
                        final_output += numbers_to_braille[next_character]
                    else:
                        print("Invalid Input")
                        return
                elif 48 <= ord(next_character) <= 57:
                    final_output += (
                        braille_number_follows + numbers_to_braille[next_character]
                    )
                    number = True
                elif 65 <= ord(next_character) <= 90:
                    final_output += (
                        braille_capital_follows
                        + characters_to_braille[next_character.lower()]
                    )
                else:
                    final_output += characters_to_braille[next_character]

            if i != len(user_input) - 1:
                final_output += braille_space

    print(final_output)


if __name__ == "__main__":
    main()
