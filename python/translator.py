import sys
inarr = sys.argv
instring = ' '.join(inarr[1:])

#print(inarr[1:])
#print('     '.join(list(instring)))

# insane that i spent the vast majority of my time filling this shit out
let_to_braille = {
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
    ' ': '......',
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

#same for this garbage
braille_to_let = {
    'O.....': ['a', 'A', '1'],
    'O.O...': ['b', 'B', '2'],
    'OO....': ['c', 'C', '3'],
    'OO.O..': ['d', 'D', '4'],
    'O..O..': ['e', 'E', '5'],
    'OOO...': ['f', 'F', '6'],
    'OOOO..': ['g', 'G', '7'],
    'O.OO..': ['h', 'H', '8'],
    '.OO...': ['i', 'I', '9'],
    '.OOO..': ['j', 'J', '0'],
    'O...O.': ['k', 'K'],
    'O.O.O.': ['l', 'L'],
    'OO..O.': ['m', 'M'],
    'OO.OO.': ['n', 'N'],
    'O..OO.': ['o', 'O'],
    'OOO.O.': ['p', 'P'],
    'OOOOO.': ['q', 'Q'],
    'O.OOO.': ['r', 'R'],
    '.OO.O.': ['s', 'S'],
    '.OOOO.': ['t', 'T'],
    'O...OO': ['u', 'U'],
    'O.O.OO': ['v', 'V'],
    '.OOO.O': ['w', 'W'],
    'OO..OO': ['x', 'X'],
    'OO.OOO': ['y', 'Y'],
    'O..OOO': ['z', 'Z'],
    '......': [' ']
}


#check if string is english
in_is_english = False
for i in range(len(instring)):
    if instring[i] != '.' and instring[i] != 'O':
        in_is_english = True
        break
        
#print(in_is_english)

outstring = ''
if in_is_english: #out needs to be braille
    is_in_digits = False
    for i in range(len(instring)):
        char = instring[i]

        if char == ' ':
            outstring += '......'
            is_in_digits = False
            continue

        if char.isupper():
            outstring += '.....O'
            outstring += let_to_braille[char.lower()]
            continue

        if char.isdigit():
            if not is_in_digits:
                outstring += '.O.OOO'
                is_in_digits = True
            outstring += let_to_braille[char]
            continue

        outstring += let_to_braille[char]

else:
    is_in_digits = False
    next_is_capital = False
    for i in range(int(len(instring)/6)):
        char = instring[i*6:i*6+6]

        if char == '.....O': #capital letter
            next_is_capital = True
            continue
            
        if next_is_capital:
            outstring += braille_to_let[char][1]
            next_is_capital = False
            continue
        
        if char == '.O.OOO': #digits
            is_in_digits = True
            continue
            
        if is_in_digits:
            outstring += braille_to_let[char][2]
            continue
            
        if char == '......': #space
            outstring += ' '
            is_in_digits = False
            continue
            
        outstring += braille_to_let[char][0]


print(outstring)