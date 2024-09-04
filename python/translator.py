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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
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
    '.': '.O...O', # decimal point
}

# reverse mapping of dictionary from 'num': 'braille' to 'braille': 'num'
braille2num_dict = {v: k for k, v in num2braille_dict.items()}

def braille_to_eng(input):
    # vars to correctly translate next char

    # encapulated function to get number
    def get_num(input, i):
        cur_char = input[i:i+6]
        result = ""

        while cur_char != braille2eng_dict[' '] or cur_char != braille2eng_dict['.']:
            result += braille2num_dict[cur_char]
            i+=6
            if i >= len(input):
                break
            cur_char = input[i:i+6]
        
        return i, result

    result = ""
    cap_follows = ".....O"
    num_follows = ".O.OOO"

    cap_flag = False

    i = 0
    while i < len(input):
        cur_char = input[i:i+6]
        # print(cur_char)
        # check if flag character
        if cur_char == num_follows:
            # num_flag = True
            i+=6
            i, num_result = get_num(input, i)
            result += num_result

            continue


        # i+=6 # increment to next braille char
