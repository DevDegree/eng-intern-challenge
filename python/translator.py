
import sys
def translatorBraille():
    inputType = "braille"
    inputs = sys.argv[1:]
    inputList = []
    for input in inputs:
        inputList.append(input)
    input = ' '.join(inputList)
    for letter in input:
        if letter != '.' and letter != 'O':
            inputType =  "string"
            break
    if inputType == "string":
        return encode_braille(input)
    else:
        return decode_braille(input)

braille_dict = {
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
    'cap_follow':'.....O',
    'decimal_follow':'.O...O',
    'number_follow': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':' : '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/' : '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',
}
braille_dict_num={
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
}
reverse_braille_dict = {
    '.....O': 'cap_follow', 
    '.O...O': 'decimal_follow', 
    '.O.OOO': 'number_follow', 
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
    '.O.OO.': ')', 
    '......': ' ', 
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
    'O..OOO': 'z'
}
reverse_braille_dict_num={
    '.OOO..': '0', 
    'O.....': '1', 
    'O.O...': '2', 
    'OO....': '3', 
    'OO.O..': '4', 
    'O..O..': '5', 
    'OOO...': '6', 
    'OOOO..': '7', 
    'O.OO..': '8', 
    '.OO...': '9'
}

def decode_braille(braille_string):
    braille_list = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    decoded_output = ''
    capNext = False
    num = False
    for braille_char in braille_list:
        if braille_char in reverse_braille_dict:
            if reverse_braille_dict[braille_char] == 'cap_follow':
                capNext = True
                continue
            if capNext:
                decoded_output += reverse_braille_dict[braille_char].upper()
                capNext = False
                continue
            if reverse_braille_dict[braille_char] == 'number_follow':
                num = True
                continue
            if num:
                if reverse_braille_dict[braille_char] == ' ':
                    num = False
                    decoded_output += reverse_braille_dict[braille_char]
                    continue
                if reverse_braille_dict[braille_char] == 'decimal_follow':
                    decoded_output += '.'
                    continue
                decoded_output += reverse_braille_dict_num[braille_char]
                continue
            decoded_output += reverse_braille_dict[braille_char]
    print(decoded_output) 

def encode_braille( plain_string :str ):
    letter_list = list(plain_string)
    encoded_output = ''
    num = False

    for letter in letter_list:
        if letter.isupper():
            encoded_output += braille_dict['cap_follow']
            letter = letter.lower()
        if letter.isnumeric() and not num:
            encoded_output += braille_dict['number_follow']
            num = True
        if num:
            if letter == '.':
                encoded_output += braille_dict['decimal_follow']
                continue
            if letter == ' ':
                num = False
                encoded_output += braille_dict[letter]
                continue
            encoded_output += braille_dict_num[letter]
            continue
        if letter in braille_dict:
            encoded_output += braille_dict[letter]
    print(encoded_output) 

if __name__ == "__main__":
    translatorBraille()