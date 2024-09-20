import sys

### Braille to String Dictionaries & Functions
braille_follows_cap = {
    '.....O': True
}

braille_follows_num ={
    '.O.OOO': True
}

braille_follows_space ={
    '......': True
}


braille_to_char = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
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
}

braille_to_num = {
    'O.....': '1',
    'O.O...': '2',
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8',
    '.OO...': '9',
    '.OOO..': '0',
    '.O.OOO': '.'
}

braille_to_special_chars = {
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')'
}

# add special chars to both braille_to_char and braille_to_num
braille_to_char.update(braille_to_special_chars)
braille_to_num.update(braille_to_special_chars)

def convert_braille_to_string(s):
    c=""
    uppercase=False
    numeric=False

    for i in range(0,len(s)):
        if braille_follows_cap.get(s[i],False)==True: # if the next symbol is a following capital
            uppercase=True
        elif braille_follows_num.get(s[i],False)==True: # if next symbol is following num
            numeric=True
        elif braille_follows_space.get(s[i],False)==True:
            c+=" "
            numeric=False
        elif numeric==True:
            c+=braille_to_num[s[i]]
        else:
            if uppercase==True:
                c+=braille_to_char[s[i]].upper()
                uppercase=False
            else:
                c+=braille_to_char[s[i]]
            
    return c

### String to Braille Dictionaries and Functions
char_to_braille = {
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
    'z': 'O..OOO'
}

num_to_braille = {
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
    '.': '.O.OOO'
}


special_chars_to_braille = {
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
    ')': '.O.OO.'
}

char_to_braille.update(special_chars_to_braille)
num_to_braille.update(special_chars_to_braille)

def convert_string_to_braille(s):
    b=""
    numeric=False
    for i in range(0,len(s)):
        char = s[i]
        if char.isupper():
            b+='.....O'
            b+=char_to_braille[char.lower()]
        elif char.isnumeric() and numeric==False:
            b+='.O.OOO'
            b+=num_to_braille[char]
            numeric=True
        elif char.isspace():
            b+='......'
            numeric=False
        else:
            if numeric==True:
                b+=num_to_braille[char]
            else:
                b+=char_to_braille[char]

    return b


# For the program to be smart to determine if the input is Braille or string, check if the string only contains '.' and 'O'
def main(arguments):
    inputs = ' '.join(arguments)
    t = 's'  # The input type, s= string b = braille
    converted_string = ""

    braille_chars= set(".O")

    # check if the input is a braille input
    if all(x in braille_chars for x in inputs):
        t='b'


    if t=='b':
        string_arr=[]
        num=0
        index=0
        # populate the string array with each braille symbol
        for x in range(0,len(inputs),6):
            chunk= inputs[x:x+6]
            string_arr.append(chunk)


        # convert the braille symbols in string_arr to characters and append them to converted_string
        converted_string=convert_braille_to_string(string_arr)
    else:
        converted_string=convert_string_to_braille(inputs)

    print(converted_string)
    return converted_string


if __name__ == "__main__":
    main(sys.argv[1:])