import sys

braille_dict = {"A": "O.....", "1": "O.....", "B": "O.O...", "2": "O.O...", "C": "OO....", "3": "OO....",
                "D": "OO.O..", "4": "OO.O..", "E": "O..O..", "5": "O..O..", "F": "OOO...", "6": "OOO...",
                "G": "OOOO..", "7": "OOOO..", "H": "O.OO..", "8": "O.OO..", "I": ".OO...", "9": ".OO...",
                "J": ".OOO..", "O": ".OOO..", "K": "O...O.", "L": "O.O.O.", "M": "OO..O.", "N": "OO.OO.",
                "O": "O..OO.", "P": "OOO.O.", "Q": "OOOOO.", "R": "O.OOO.", "S": ".OO.O.", "T": ".OOOO.",
                "U": "O...OO", "V": "O.O.OO", "W": ".OOO.O", "X": "OO..OO", "Y": "OO.OOO", "Z": "O..OOO",
                ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..O.O.", "-": "....OO", "/": ".O..O.",
                "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......", ".": "..OO.O"}

print(sys.argv)
def english_parse(string: str):
    new_str = ""
    is_num = False
    for i, char in enumerate(string):
        if char.isupper():
            new_str += ".....O"
        elif not is_num and char.isnumeric():
            new_str += ".O.OOO"
            is_num = True
        elif char == " ":
            is_num = False

        new_str += braille_dict[char.upper()]
    return new_str

def braille_parse(string: str):
    new_str = ""
    is_num = False
    i = 0
    capitalize = False
    while i < len(string) - 1:
        if string[i: i+6] == ".....O":
            capitalize = True
        elif string[i: i+6] == ".O.OOO":
            is_num = True
        elif string[i:i+6] == "......":
            is_num = False
            new_str += " "
        else:
            for letter, braille in braille_dict.items():
                if string[i:i+6] == braille:
                    if is_num:
                        if letter.isnumeric():
                            new_str += letter
                            break
                    else:
                        if capitalize:
                            new_str += letter
                            capitalize = False
                            break

                        new_str += letter.lower()
                        break
        i += 6
    return new_str


if len(sys.argv) < 2:
    exit()

string = " ".join(sys.argv[1:])

if len(string) - (string.count("O") + string.count(".")) > 0:
    print(english_parse(string))
else:
    print(braille_parse(string))
