import sys

# braille mapping for letters, numbers, special characters, and punctuation
eng_to_braille = {
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
}
braille_to_eng = {v: k for k, v in eng_to_braille.items()}

num_to_braille = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}
braille_to_num = {v: k for k, v in num_to_braille.items()}

special_chars_braille = {
    '......' : 'SPACE',
    '.....O' : 'CAPS',
    '.O.OOO' : 'NUM'
}
special_chars_eng = {v: k for k, v in special_chars_braille.items()}

punc_to_braille = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.O..O.',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}
braille_to_punc = {v: k for k, v in punc_to_braille.items()}

def braille_to_english(string):
    input = [string[i:i+6] for i in range(0, len(string), 6)]
    output = ""
    isNum = False
    isCaps = False
    for character in input:
        if character in special_chars_braille:
            if special_chars_braille[character] == 'CAPS':
                isCaps = True
            elif special_chars_braille[character] == 'NUM':
                isNum = True
            elif special_chars_braille[character] == 'SPACE':
                output += ' '
                isNum = False # numbers terminated with space from reqs
        else:
            if isNum:
                num = braille_to_num.get(character)
                if num:
                    output += num
            else:
                char = braille_to_eng.get(character)
                if char:
                    if isCaps:
                        output += char.upper()  
                        isCaps = False
                    else:
                        output += char
                else: # not num, and not in letters
                    output += braille_to_punc.get(character)
    
    return output

def english_to_braille(string):
    output = ""
    isNum = False
    for character in string:
        if character.isalpha():
            if character.isupper():
                output += special_chars_eng['CAPS']
            output += eng_to_braille.get(character.lower())
        elif character.isdigit():
            if not isNum:
                output += special_chars_eng['NUM']
                isNum = True
            output += num_to_braille.get(character)
        elif character == ' ':
            output += special_chars_eng['SPACE']
            isNum = False
        else:
            output += braille_to_punc.get(character)
    return output

def is_braille(string):
    # has to be only O's and .'s, and divisible by 6
    return set(string) <= set('O.') and len(string) % 6 == 0
            


if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    if is_braille(input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))
    
