import re

def braille_to_english(input, number_mapping, non_number_mapping):
    chunked_string = [input[i:i + 6] for i in range(0, len(input), 6)]
    capital_follows = False
    decimal_follows = False
    number_follows = False
    output_list = []
    for item in chunked_string:
        if (item == ".....O"):
            capital_follows = True
            continue
        if (item == ".O...O"):
            decimal_follows = True
            output_list.append(".")
            continue
        if (item == ".O.OOO"):
            number_follows = True
            continue
        if (capital_follows == True):
            output_list.append(non_number_mapping.get(item)).upper()
            capital_follows = False
        elif(number_follows == True):
            output_list.append(number_mapping.get(item))
        else:
            output_list.append(non_number_mapping.get(item))
    output_string = "".join(output_list)
    return output_string
        
def english_to_braille(input, number_mapping, non_number_mapping):
    chunked_string = [input[i:i + 1] for i in range(0, len(input), 1)]
    output_list = []
    for item in chunked_string:
        if (item.isdigit()):
            output_list.append(number_mapping.get(item))
        elif (item.isupper()):
            output_list.append(".....O")
            output_list.append(non_number_mapping.get(item.lower()))
        else:
            output_list.append(non_number_mapping.get(item))
    output_string = "".join(output_list)
    return output_string

user_input = input('Type your braille or english: ')
pattern = '^[o.]+$'
braille_number_mapping = {
        "O.....": "1",
        "O.O..." : "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
    }
braille_non_number_mapping = {
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
        "......": " "
    }
english_number_mapping = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}
english_non_number_mapping = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'
}

if (re.match(pattern, user_input, re.IGNORECASE)):
    print(braille_to_english(user_input.upper(), braille_number_mapping, braille_non_number_mapping))
else:
    print(english_to_braille(user_input, english_number_mapping, english_non_number_mapping))
