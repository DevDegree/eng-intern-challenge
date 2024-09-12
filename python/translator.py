import re

alphabet_to_braille = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    '.': "..OO.O",
    ',': "..O...",
    '?': "..O.OO",
    '!': "..OOO.",
    ':': "..OO..",
    ';': "..O.O.",
    '-': "....OO",
    '/': ".O..O.",
    '<': ".OO..O",
    '>': "O..OO.",
    '(': "O.O..O",
    ')': ".O.OO.",
    ' ': "......",
    'capital_follow': ".....O",
    'number_follow': ".O.OOO",
}


number_to_braille = {
    '1': alphabet_to_braille['a'],
    '2': alphabet_to_braille['b'],
    '3': alphabet_to_braille['c'],
    '4': alphabet_to_braille['d'],
    '5': alphabet_to_braille['e'],
    '6': alphabet_to_braille['f'],
    '7': alphabet_to_braille['g'],
    '8': alphabet_to_braille['h'],
    '9': alphabet_to_braille['i'],
    '0': alphabet_to_braille['j'],
    '.': ".O...O"
}

def is_braille(user_input):
    return bool(re.match("[0.]+",user_input)) and (len(user_input) % 6 ==0)


def get_key_from_value(dictionary, value):
    for key, v in dictionary.items():
        if v == value:
            return key
    return ""

def convert_english_to_braille(user_input):
    is_number_follow = True
    is_decimal_number = False
    braille_result = ""
    for character in user_input:
        if character.isspace():
            braille_result += alphabet_to_braille[character]
            is_decimal_number = False
            is_number_follow = True
        elif not character.isdigit() and not is_decimal_number:
            if character.isupper():
                braille_result += alphabet_to_braille['capital_follow'] + alphabet_to_braille[character.lower()]
            else:
                braille_result += alphabet_to_braille[character]
        elif character.isdigit or (character == "." and is_decimal_number):
            if is_number_follow:
                braille_result += alphabet_to_braille['number_follow']
                is_number_follow = False
            braille_result += number_to_braille[character]
            is_decimal_number = True

    return braille_result

def convert_braille_to_english(user_input):
    is_number_follow = False
    result_arr = []
    value=""
    for character in user_input:
        value += character
        if len(value) == 6:
            braille_character = get_key_from_value(dictionary=alphabet_to_braille, value=value)
            if braille_character == "number_follow":
                is_number_follow = True
                value = ""
                continue

            if braille_character.isspace():
                result_arr.append(" ")
                is_number_follow = False
                value = ""
                continue

            if is_number_follow:
                result_arr.append(get_key_from_value(dictionary=number_to_braille, value=value))
                value = ""
            else:
                result_arr.append(get_key_from_value(dictionary=alphabet_to_braille, value=value))
                value = ""
    return result_arr

# This method will remove the capital_follow text and upper case the next value
def modify_english_result(result_arr):
    modified_result =[]
    index =0
    while index < len(result_arr):
        if result_arr[index] == 'capital_follow':
            index += 1
            modified_result.append(result_arr[index].upper())
            index +=1      # skip the next value
        else:
            modified_result.append(result_arr[index])
            index +=1

    return "".join(modified_result)

def main():
    user_input = input()
    if is_braille(user_input):
        print(modify_english_result(convert_braille_to_english(user_input)))
    else:
        print(convert_english_to_braille(user_input))

if __name__ == '__main__':
    main()



