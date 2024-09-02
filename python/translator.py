import sys

brail_to_letters = \
{
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
    ".OOO0.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

letters_to_brail = \
{
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
    "t": ".OOO0.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
}

brail_to_numbers = \
{
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

number_to_brail = \
{
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

capital_letter = ".....O"
number_follows = ".O.OOO"
space = "......"

def translate(string_to_translate):
    can_be_brail = True

    translation = []

    if len(string_to_translate)%6 > 0:
        can_be_brail = False

    if can_be_brail:
        number = False
        to_capital = False
        for i in range(0, len(string_to_translate), 6):
            brail = string_to_translate[i:i+6]
            if brail in brail_to_letters and not number:
                if to_capital:
                    translation.append(brail_to_letters[brail].upper())
                    to_capital = False
                else:
                    translation.append(brail_to_letters[brail])
            elif number and brail in brail_to_numbers:
                translation.append(brail_to_numbers[brail])
            elif brail == number_follows:
                number = True
            elif brail == capital_letter:
                to_capital = True
            elif brail == space:
                translation.append(" ")
                number = False
            else:
                can_be_brail = False
                break

    if not can_be_brail:
        translation = []
        first_number = True
        for char in string_to_translate:
            if char.islower():
                translation.append(letters_to_brail[char])
            elif char.isupper():
                translation.append(capital_letter + letters_to_brail[char.lower()])
            elif char.isnumeric():
                if first_number:
                    first_number = False
                    translation.append(number_follows)
                translation.append(number_to_brail[char])
            elif char == " ":
                translation.append(space)
                first_number = True

    print("".join(translation))


if __name__ == "__main__":
    inp = " ".join(sys.argv[1:])
    translate(inp)

