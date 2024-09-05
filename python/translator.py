import sys

# constants
cap_follows = ".....O"
num_follows = ".O.OOO"

eng2braille_dict = {
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
    # '.': '..OO.O',
    # ',': '..O...',
    # '?': '..O.OO',
    # '!': '..OOO.',
    # ':': '..OO..',
    # ';': '..O.O.',
    # '-': '....OO',
    # '/': '.O..O.',
    # '<': '.OO..O',
    # '>': 'O..OO.',
    # '(': 'O.O..O',
    # ')': '.O.OO.',
    ' ': '......',
}

# reverse mapping of dictionary from 'char': 'braille' to 'braille': 'char'
braille2eng_dict = {v: k for k, v in eng2braille_dict.items()}

num2braille_dict = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    # '.': '.O...O', # decimal point
}

# reverse mapping of dictionary from 'num': 'braille' to 'braille': 'num'
braille2num_dict = {v: k for k, v in num2braille_dict.items()}

def braille_to_eng(input):
    # vars to correctly translate next char

    # encapulated function to get number
    def get_num(input, i):
        cur_char = input[i:i+6]
        get_num_result = ""

        while cur_char != eng2braille_dict[' '] and i < len(input):
            get_num_result += braille2num_dict[cur_char]
            i+=6
            if i >= len(input):
                break
            cur_char = input[i:i+6]
        
        return i, get_num_result

    # encapulated function to get non-number
    def get_char(input, i):
        cur_char = input[i:i+6]
        get_char_result = ""
        cap_flag = False

        while cur_char != num_follows and i < len(input):
            if cur_char == cap_follows:
                cap_flag = True
                i+=6
                cur_char = input[i:i+6]
                continue
            # otherwise
            result_char = braille2eng_dict[cur_char]
            if(cap_flag):
                result_char = result_char.upper()
                cap_flag = False
            get_char_result += result_char
            i+=6
            if i >= len(input):
                break
            cur_char = input[i:i+6]

        return i, get_char_result


    result = ""

    i = 0
    while i < len(input):
        cur_char = input[i:i+6]
        # check if number flag character
        if cur_char == num_follows:
            # num_flag = True
            i+=6
            i, num_result = get_num(input, i)
            result += num_result

            continue
        # otherwise continue aquiring characters
        i, char_result = get_char(input, i)
        result += char_result

    return result

def eng_to_braille(input):
    result = ""

    i = 0
    while i < len(input):
        cur_char = input[i]
        if cur_char.isnumeric():
            result += num_follows
            while cur_char != ' ' and i < len(input):
                result += num2braille_dict[cur_char]
                i+=1
                if i >= len(input):
                    break
                cur_char = input[i]
        elif cur_char.isupper():
            result += cap_follows
            result += eng2braille_dict[cur_char.lower()]
            i+=1
        else:
            # otherwise just add the item as is, do not need to worry about special char
            result += eng2braille_dict[cur_char]
            i+=1
        # i+=1
    
    return result


def eng_braille_translator(input):
    result = ''
    if '.' in input:
        result = braille_to_eng(input)
    else:
        result = eng_to_braille(input)
    
    print(result)

eng_braille_translator(' '.join(sys.argv[1:]))
