import sys

if len(sys.argv) == 1:
    raise Exception("usage: python3 translator.py [braille/english string]")

text = sys.argv[1]
for i in range (2, len(sys.argv)):
    text += ' ' + sys.argv[i]

mapping = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..OO',
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
    '0': '.OOO..',
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'number': '.O.OOO',
    'caps': '.....O',
    'space': '......'
}

# braille must contain a .

is_braille = False
if '.' in text:
    is_braille = True
    new_mapping = {}
    for key in mapping:
        if key.isdigit():
            new_mapping['x' + mapping[key]] = key
        else:
            new_mapping[mapping[key]] = key
    mapping = new_mapping


res = ''
is_caps, is_number = False, False
if is_braille:
    # read 6, find letter
    char = ''
    i = 0
    j = 0
    while i < len(text):
        if j == 6:
            if is_number:
                res += mapping['x' + char]
            elif is_caps:
                res += mapping[char].upper()
                is_caps = False
            else:
                translated = mapping[char]
                if translated == 'number':
                    is_number = True
                elif translated == 'caps':
                    is_caps = True
                elif translated == 'space':
                    res += ' '
                    is_number = False
                else:
                    res += translated
            char = ''
            j = 0
        j += 1
        char += text[i]
        i += 1
    translated = mapping[char]
    if translated == 'number':
        is_number = True
    elif translated == 'caps':
        is_caps = True
    elif translated == 'space':
        res += ' '
        is_number = False
    else:
        res += translated
else:
    is_digit = True
    for c in text:
        if c == ' ':
            res += mapping['space']
            is_digit = False
        elif c.isdigit():
            if not is_digit:
                res += mapping['number']
                is_digit = True
            res += mapping[c]
        elif c == c.upper():
            is_digit = False
            res += mapping['caps'] + mapping[c.lower()]
        else:
            is_digit = False
            res += mapping[c]
print(res)