
import string
import sys

braille = set('O'+'.')
nums = set(string.digits)
engDict = {'a':"O.....", 'b':"O.O...", 'c':"OO....", 'd':"OO.O..", 'e':"O..O..", 'f':"OOO...", 'g':"OOOO..", 
              'h':"O.OO..", 'i':".OO...", 'j':".OOO..", 'k':"O...O.", 'l':"O.O.O.", 'm':"OO..O.", 'n':"OO.OO.", 
              'o':"O..OO.", 'p':"OOO.O.", 'q':"OOOOO.", 'r':"O.OOO.", 's':".OO.O.", 't':".OOOO.", 'u':"O...OO", 
              'v':"O.O.OO", 'w':".OOO.O", 'x':"OO..OO", 'y':"OO.OOO", 'z':"O..OOO", 
              '1':"O.....", '2':"O.O...", '3':"OO....", '4':"OO.O..", '5':"O..O..", '6':"OOO...", '7':"OOOO..", 
              '8':"O.OO..", '9':".OO...", '0':".OOO..", 
              '.':"..OO.O", ',':"..O...", '?':"..O.OO", '!':"..OOO.", ':':"..OO..", ';':"..O.O.", '-':"....OO", 
              '/':".O..O.", '<':".OO..O", '>':"O..OO.", '(':"O.O..O", ')':".O.OO.", ' ':"......"}

letterDict = {'a':"O.....", 'b':"O.O...", 'c':"OO....", 'd':"OO.O..", 'e':"O..O..", 'f':"OOO...", 'g':"OOOO..", 
              'h':"O.OO..", 'i':".OO...", 'j':".OOO..", 'k':"O...O.", 'l':"O.O.O.", 'm':"OO..O.", 'n':"OO.OO.", 
              'o':"O..OO.", 'p':"OOO.O.", 'q':"OOOOO.", 'r':"O.OOO.", 's':".OO.O.", 't':".OOOO.", 'u':"O...OO", 
              'v':"O.O.OO", 'w':".OOO.O", 'x':"OO..OO", 'y':"OO.OOO", 'z':"O..OOO",
              '.':"..OO.O", ',':"..O...", '?':"..O.OO", '!':"..OOO.", ':':"..OO..", ';':"..O.O.", '-':"....OO",
              '/':".O..O.", '<':".OO..O", '>':"O..OO.", '(':"O.O..O", ')':".O.OO.", ' ':"......"}
numDict = {'1':"O.....", '2':"O.O...", '3':"OO....", '4':"OO.O..", '5':"O..O..", '6':"OOO...", '7':"OOOO..", 
           '8':"O.OO..", '9':".OO...", '0':".OOO.."}

brailleDict = {v:k for k, v in letterDict.items()}
brailleNumDict = {v:k for k, v in numDict.items()}

def isNum(c):
    return set(c) <= nums

def translate(s):
    if set(s) <= braille:
        brailleToEng(s)
    else:
        engToBraille(s)

def engToBraille(s):
    number = False
    translated = ""
    for c in s:
        if c.isupper():
            translated += ".....O"

        elif isNum(c) and not number:
            number = True
            translated += ".O.OOO"
        elif c==' ':
            number = False
        translated += engDict[c.lower()]
    print(translated)



def brailleToEng(s):
    translated = ""
    number = False
    capital = False
    for i in range(int(len(s)/6)):
        c = s[6*i:6*(i+1)]
        if c == ".O.OOO":
            number = True
            continue
        elif c == "......":
            number = False
        elif c == ".....O":
            capital = True
            continue
        if number:
            translated += brailleNumDict[c]
        elif capital:
            translated += brailleDict[c].upper()
            capital = False
        else:
            translated += brailleDict[c]
    print(translated)

if __name__ == "__main__":
    s = ""
    for i in range(len(sys.argv)):
        if i>0:
            s += sys.argv[i]+" "
    translate(s[:-1])