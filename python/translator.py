import sys

braille_to_char = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

braille_to_non_char = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "......": " "
}

def find_key(dict, val):
    for key, value in dict.items():
        if value == val or str(value) == str(val):
            return key
    return ""

input_argument = " ".join(sys.argv[1:])
output_string = ""

input_is_english = False
input_is_braille = False

#check input is braille or english
if (len(input_argument) % 6 == 0 and ("O" in input_argument or "." in input_argument)):
    input_is_braille = True
else:
    input_is_english = True

if input_is_english:
    prev_is_num = False
    for i in input_argument:
        if i.isalpha():
            if i.isupper():
                output_string = output_string + ".....O"
            output_string = output_string + find_key(braille_to_char, i)
            prev_is_num = False
        elif i.isdigit():
            if not prev_is_num:
                output_string = output_string + ".O.OOO"
            output_string = output_string + find_key(braille_to_non_char, i)
            prev_is_num = True
        else:
            output_string = output_string + "......"
            prev_is_num = False

    print(output_string)
    sys.exit(0)

number_switch = False
capital_switch = False
array = []

if input_is_braille:
    for i in range(0, len(input_argument), 6):
        array.append(input_argument[i: i + 6])
    
    for symbol in array:
        if symbol == '.....O':
            capital_switch = True
        elif symbol == ".O.OOO":
            number_switch = True
        elif symbol == "......":
            output_string += " "
            number_switch = False
        elif number_switch == True:
            output_string += braille_to_non_char.get(symbol)
        else:
            if capital_switch == True:
                output_string += braille_to_char.get(symbol).upper()
                capital_switch = False
            else:
                output_string += braille_to_char.get(symbol)
    
    print(output_string)
    sys.exit(0)