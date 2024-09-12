import sys

n = len(sys.argv)-1

input = ""
output = ""

bToE = {
    "O....." : "a",
    "O.O..." : "b",
    "OO...." : "c",
    "OO.O.." : "d",
    "O..O.." : "e",
    "OOO..." : "f",
    "OOOO.." : "g",
    "O.OO.." : "h",
    ".OO..." : "i",
    ".OOO.." : "j",
    "O...O." : "k",
    "O.O.O." : "l",
    "OO..O." : "m",
    "OO.OO." : "n",
    "O..OO." : "o",
    "OOO.O." : "p",
    "OOOOO." : "q",
    "O.OOO." : "r",
    ".OO.O." : "s",
    ".OOOO." : "t",
    "O...OO" : "u",
    "O.O.OO" : "v",
    ".OOO.O" : "w",
    "OO..OO" : "x",
    "OO.OOO" : "y",
    "O..OOO" : "z",
}

eToB = {}

for b in bToE:
    eToB[bToE[b]] = b

bToI = {
    "O....." : "1",
    "O.O..." : "2",
    "OO...." : "3",
    "OO.O.." : "4",
    "O..O.." : "5",
    "OOO..." : "6",
    "OOOO.." : "7",
    "O.OO.." : "8",
    ".OO..." : "9",
    ".OOO.." : "0",
}

iToB = {}

for i in bToI:
    iToB[bToI[i]] = i

if '.' in str(sys.argv[1]):
    # BRAILLE to ENGLISH
    input = str(sys.argv[1])
    isCapital = False
    isNumber = False
    for i in range(0, len(input), 6):
        cur = input[i : i+6]
        if (cur == '.....O'):
            isCapital = True
        elif (cur == '.O.OOO'):
            isNumber = True
        elif (cur == '......'):
            isNumber = False
            isCapital = False
            output += ' '
        else:
            if isCapital:
                output += bToE[cur].upper()
                isCapital = False
            elif isNumber:
                output += bToI[cur]
            else:
                output += bToE[cur]

else:
    # ENGLISH TO BRAILLE
    for i in range(n):
        input += str(sys.argv[i+1])
        if i != n-1:
            input += ' '
    isNumber = False
    for ch in input:
        if ch == ' ':
            output += '......'
            isNumber = False
        elif ch.isdigit():
            if isNumber:
                output += iToB[ch]
            else:
                isNumber = True
                output += '.O.OOO'
                output += iToB[ch]
        elif ch.isupper():
            output += '.....O'
            output += eToB[ch.lower()]
        else:
            output += eToB[ch]


print(output)