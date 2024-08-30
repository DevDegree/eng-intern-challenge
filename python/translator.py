import sys

braille_to_eng = {
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
    '......': ' ', 
    '..OO.O': '.',
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
}

eng_to_braille = { v: k for k,v in braille_to_eng.items()}
num_to_braille = { v: k for k,v in braille_to_num.items()}


CAPITAL = '.....O'
NUMBER  = '.O.OOO'

def to_eng(s: str) -> str:
    ans = ""
    nextCap = False
    nextNum = False
    for i in range(6, len(s)+1,6):
        sub = s[i-6:i]
        if sub == '......':
            ans += " "
            nextNum = False
            continue
        if sub == CAPITAL:
            nextCap = True
        elif sub == NUMBER:
            nextNum = True
        else:
            if nextCap:
                ans += braille_to_eng[sub].upper()
                nextCap = False
            elif nextNum:
                ans += braille_to_num[sub]
            else:
                ans += braille_to_eng[sub]
    return ans

def to_braille(s: str) -> str:
    # if capital, prepend capital follows
    # if number, prepend number follows
    ans = ""
    num = False
    for c in s:
        if c.isupper():
            ans += CAPITAL
            ans += eng_to_braille[c.lower()].upper()
        else:
            if c == " ":
                num = False
                ans += eng_to_braille[c]
            elif num:
                ans += num_to_braille[c]
            elif c.isdigit():
               num = True
               ans += NUMBER
               ans += num_to_braille[c]
            else:
                ans += eng_to_braille[c]
        # print(c, ans)
            


    return ans

def translate():
    input_string = " ".join(sys.argv[1:])
    # input_string = "Abc 234 xYz"
    # input_string = ".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO"
    if len(set(input_string)) == 2:
        print(to_eng(input_string))
    else:
        print(to_braille(input_string))
        

if __name__ == "__main__":
    translate()

