import sys

char_key = {
    'O.....':'A',
    'O.O...':'B',
    'OO....':'C',
    'OO.O..':'D',
    'O..O..':'E',
    'OOO...':'F',
    'OOOO..':'G',
    'O.OO..':'H',
    '.OO...':'I',
    '.OOO..':'J',
    'O...O.':'K',
    'O.O.O.':'L',
    'OO..O.':'M',
    'OO.OO.':'N',
    'O..OO.':'O',
    'OOO.O.':'P',
    'OOOOO.':'Q',
    'O.OOO.':'R',
    '.OO.O.':'S',
    '.OOOO.':'T',
    'O...OO':'U',
    'O.O.OO':'V',
    '.OOO.O':'W',
    'OO..OO':'X',
    'OO.OOO':'Y',
    'O..OOO':'Z'
    }

def english_to_braille(s):
    is_alphabet = True
    result = ""
    for i in range(len(s)):
        if ord(s[i])>=97 and ord(s[i])<=122:
            result += list(char_key.keys())[ord(s[i])-97]
        elif ord(s[i])>=65 and ord(s[i])<=90:
            result += '.....O' + list(char_key.keys())[ord(s[i])-65]
        elif ord(s[i])>=48 and ord(s[i])<=57:
            if is_alphabet:
                result += '.O.OOO'
            is_alphabet = False
            if ord(s[i]) == 48:
                result += '.OOO..'
                continue
            result += list(char_key.keys())[ord(s[i])-49]
        else:
            is_alphabet = True
            result += '......'
    return result

def braille_to_english(s):
    char_stack = []
    result = ""
    for i in range(len(s)-1,-1,-6):
        char_stack.append(s[i-5:i+1])
    is_alphabet = True
    while len(char_stack)>0:
        curr = char_stack.pop()
        if curr == '.....O':
            curr = char_stack.pop()
            result += char_key[curr]
        elif curr == '.O.OOO':
            is_alphabet = False
            continue
        elif curr == '......':
            is_alphabet = True
            result+=' '
        else:
            if is_alphabet:
                result += char_key[curr].lower()
            else:
                if curr == '.OOO..':
                    result+='0'
                    continue
                result += chr(ord(char_key[curr])-16)
    return result


user_input = sys.argv
output = ""
curr_input = ""
is_english = False
for j in range(len(user_input[1])):
        if user_input[1][j]!='.' and user_input[1][j]!='O':
            is_english = True
            break
for i in range(1,len(user_input)):
    curr_input += user_input[i]
    if i==len(user_input)-1:
        break
    if is_english:
        curr_input += ' '
    else:
        curr_input += '......'

if is_english:
    output += english_to_braille(curr_input) 
else:
    output += braille_to_english(curr_input)
print(output)