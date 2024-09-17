"""Split into 3 parts
First recognize if the input is english or braille
If input is english figure out how to translate to braille
Else figure out how to translate to english
"""

"""Braille to english
First split the string into (list)groups of 6 as each braille letter corresponds to 6 chars of Os and .s
Second we should recognize if the 6 chars will affect the next inputs in the list
Third correspond the groups of 6 braille chars to english

"""
def eng_or_braille(text):
    #braille is split into strings of groups of 6
    #if the string is not a multiple of 6 then its english
    if(len(text)%6!=0):
        return 'e'
    #if the string doesnt only contain '.' and 'O' its english
    for i in range(len(text)):
        if (text[i]!='.' and text[i]!='O'):
            return 'e'
    #if it makes it past the checks then its braille
    return 'b'
        
def split_into_groups_of_6(text):
    return [text[i:i + 6] for i in range(0, len(text), 6)]
def getValueFromKey(dict, val):
    for k, v in dict.items():
        if v==val:
            return k
    return ""
def translate(txt):
    l = split_into_groups_of_6(txt)
    #conditions affecting the future letters
    capital = False
    numbers = False
    decimal = False
    output = ""
    dictChar = {
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
    '..OO.O': '.'
    }
    dictNum = {
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
        '......': ' ',
        '..OO.O': '.'
        }
    if(eng_or_braille(txt)=='b'):
        for text in l:
            if text == '.....O':
                #next letter is capital
                capital = True
            elif text == '.O...O':
                #next letter is decimal
                decimal = True
            elif text == '.O.OOO':
                #next letters are numbers until a space
                numbers = True
            else:
                if capital:
                    output+=(dictChar.get(text, "")).upper()
                    capital=False
                elif decimal:
                    output+= '.'
                    decimal = False
                elif numbers:
                    output +=(dictNum.get(text, ""))
                    if(dictNum.get(text)==' '):
                        numbers = False
                else:
                    output+=(dictChar.get(text, ""))
        return output
    else:
        for c in txt:
            if decimal:
                decimal = False
                continue
            if c.isupper():
                capital = True
            elif numbers == False and c.isdigit():
                numbers = True
                output+='.O.OOO'
            elif numbers and c=='.':
                decimal = True
                output+='.O...O..O...'
            if capital:
                output+='.....O'
                capital = False
            if numbers:
                output+=getValueFromKey(dictNum, c)
                if(c == ' '):
                    numbers = False
            else:
                output+=getValueFromKey(dictChar, c.lower())
        return output
            
            

# print(translate(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
# print(translate(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."))
# print((translate("Hello world")))
# print((translate("Hello world"))==".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
# print((translate("Abc 123"))==".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
# print(split_into_groups_of_6(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"))
# print(eng_or_braille("asnaj"))
while True:
    print(translate(input()))
