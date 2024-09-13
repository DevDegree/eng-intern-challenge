import sys

brl_to_eng = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}

eng_to_brl = {v: k for k, v in brl_to_eng.items()}

brl_to_num = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '10',
}

num_to_brl = {v: k for k,v in brl_to_num.items()}

words = sys.argv[1:]
if not len(words): quit() # No commands given

# Check if arguments are in braille or not
isBraille = True
for x in words[0]:
    if x not in ['.','O']:
        isBraille = False
        break

string = ''

# If arguments are not braille
if not isBraille:
    for word in words:
        isNum = False
        for letter in word:
            if letter.isnumeric() and not isNum: # Set to Numeric Mode
                isNum = True
                string = string + '.O.OOO'
            if isNum: string = string + num_to_brl[letter.lower()] # If numeric mode on, use numbers
            if letter.isupper(): string = string + '.....O' # Define uppercase letter
            if not isNum: string = string + eng_to_brl[letter.lower()]
        if word is not words[-1]: string = string + '......'
# Argument is in braille
else:
    brl_msg = words[0]
    chunks = []
    for i in range(0, len(brl_msg), 6):
        chunks.append(brl_msg[i:i+6])
    isNum = False
    isCap = False
    for braille in chunks:
        if braille == '.O.OOO':
            isNum = True
            continue
        if braille == '......':
            string = string + ' '
            isNum = False
            continue
        if isNum: string = string + brl_to_num[braille]
        if braille == '.....O':
            isCap = True
            continue
        if not isNum: 
            if isCap: 
                string = string + brl_to_eng[braille].upper()
                isCap = False
            else: 
                string = string + brl_to_eng[braille]
            
print(string)

