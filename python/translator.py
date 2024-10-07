import sys
# Braille dictionary with shared patterns for letters and numbers
# I didn't want to have 2 copies of this dictionary so I did a function for look up by value
braille_dict = {
    'O.....': 'a',  # or '1'
    'O.O...': 'b',  # or '2'
    'OO....': 'c',  # or '3'
    'OO.O..': 'd',  # or '4'
    'O..O..': 'e',  # or '5'
    'OOO...': 'f',  # or '6'
    'OOOO..': 'g',  # or '7'
    'O.OO..': 'h',  # or '8'
    '.OO...': 'i',  # or '9'
    '.OOO..': 'j',  # or '0'
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',  # space
    '.....O': 'CAPITAL',
    '.O.OOO': 'NUMBER',
    '.O...O': 'DECIMAL',
    '.O....': '.',
    '.O.O..': ',',
    '..O...': '?',
    '..OO..': '!',
    '.O..O.': ';',
    '..O.O.': ':',
    '.O.OO.': '-',
    '..OOO.': '/',
    'O....O': '<',
    'O.O.OO': '>',
    '.OO..O': '(',
    '.O.OO.': ')'
}

braille_num_dict = {
    'O.....': '1',  # or '1'
    'O.O...': '2',  # or '2'
    'OO....': '3',  # or '3'
    'OO.O..': '4',  # or '4'
    'O..O..': '5',  # or '5'
    'OOO...': '6',  # or '6'
    'OOOO..': '7',  # or '7'
    'O.OO..': '8',  # or '8'
    '.OO...': '9',  # or '9'
    '.OOO..': '0',  # or '0'
}

#Get dictionary key by value
def get_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None  # Return None if the value is not found

# Braille to english alphabet
#Outline didn't mention the decimal follows and I wasn't sure how it would work
def braille_to_char(braille_input):
    is_number = False
    is_capital = False
    is_decimal = False
    output = ""
    for i in range(0, len(braille_input), 6):
        braille_char = braille_dict[braille_input[i:i+6]]
        if is_capital:
            braille_char = braille_char.capitalize()
            is_capital = False
        if braille_char == " ":
            is_number = False
        if is_number:
            braille_char = braille_num_dict[braille_input[i:i+6]]
        if braille_char == 'CAPITAL':  # "capital follows" indicator
            is_capital = True
        elif braille_char == 'NUMBER':  # "number follows" indicator
            is_number = True
        elif braille_char == 'DECIMAL':  # "decimal follows" indicator
            is_decimal = True
        else:
            output += braille_char
    
    return output

#English alphabet character to braille
def char_to_braille(char_input):

    output = ""
    previous_numeric = False

    for letter in char_input:
        # print(letter)
        if letter.isupper():
            output += get_key_by_value(braille_dict,"CAPITAL")
            output += get_key_by_value(braille_dict,letter.lower())

        elif letter.isnumeric():
            # numbers.append(letter)
            if not previous_numeric:
                output += get_key_by_value(braille_dict,"NUMBER")
                previous_numeric = True
            output += get_key_by_value(braille_num_dict,letter)
        else:
            output += get_key_by_value(braille_dict,letter)
            previous_numeric = False

    return output
            

#Check the first slice of 6 characters to see if it's braille, if it's braille convert to english alphabet, if it's english alphabet convert to braille
def convert_input(user_input):

    output = ""

    if user_input[:6] in braille_dict:
        output = braille_to_char(user_input)

    else:
        output = char_to_braille(user_input)
        


    return output


if __name__ == '__main__':
    if len(sys.argv) > 1:
            input = " ".join(sys.argv[1:])
            print(convert_input(input))
    else:
        print("No input provided.")