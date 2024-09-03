# Dictionaries
#strings equals

import sys

input = sys.argv[1:]
input_string = " ".join(input)
output= ""

braille_dict_letters = {
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
    "z": "O..OOO"
}

special_symbols = {
    "cap_follows": ".....O",
    "decimal_follows": ".O...O",
    "number_follows": ".O.OOO",
    "space": "......"
}

number_braille = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "10": ".OOO..",
}

def get_key(val, type):

    if type == "letter":
        for key, value in braille_dict_letters.items():
            if val == value:
                return key
    
    if type == "number":
        for key, value in number_braille.items():
            if val == value:
                return key

    return -1

#state 0: braille to english
#state 1: english to braille

state = 0
char_is_num = False

if (input_string.find('.') == -1):
    state = 1


if (state == 1):
    #english to braille
    for i in range(0, len(input_string)):
        if (input_string[i].isupper()):
            char_is_num = False
            output += special_symbols.get("cap_follows")
            output += braille_dict_letters.get(input_string[i].lower())
        elif (input_string[i].isdigit()):
            if char_is_num == False:
                char_is_num = True
                output += special_symbols.get("number_follows")
            output += number_braille.get(input_string[i])
        elif (input_string[i] == ' '):
            char_is_num = False
            output += special_symbols.get("space")
        else:
            char_is_num = False
            output += braille_dict_letters.get(input_string[i])
else:
    #braille to english
    count = 0
    while (count < len(input_string)):
        if (input_string[count:count+6] == special_symbols.get("cap_follows")):
            char_is_num = False
            temp =  get_key(input_string[count+6: count+12], "letter")
            output += temp.upper()
            count += 12
        elif (input_string[count:count+6] == special_symbols.get("number_follows") or char_is_num):
            if (char_is_num == False):
                char_is_num = True
                output +=  get_key(input_string[count+6: count+12], "number")
                count += 12
                if (get_key(input_string[count: count+6], "number") == -1):
                    char_is_num = False
            else:
                output += get_key(input_string[count: count+6], "number")
                count += 6
                if (get_key(input_string[count: count+6], "number") == -1):
                    char_is_num = False
        elif (input_string[count:count+6] == special_symbols.get("space")):
            char_is_num = False
            output += ' '
            count += 6
        else:
            char_is_num = False
            output += get_key(input_string[count: count+6], "letter")
            count += 6

print(output)