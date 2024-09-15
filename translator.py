import sys

alphadict = {
    "a": "O.....",
    "b":"O.O...",
    "c":"OO....",
    "d":"OO.O..",
    "e":"O..O..",
    "f":"OOO...",
    "g":"OOOO..",
    "h":"O.OO..",
    "i":".OO...",
    "j":".OOO..",
    "k":"O...O.",
    "l":"O.O.O.",
    "m":"OO..O.",
    "n":"OO.OO.",
    "o":"O..OO.",
    "p":"OOO.O.",
    "q":"OOOOO.",
    "r":"O.OOO.",
    "s":".OO.O.",
    "t":".OOOO.",
    "u":"O...OO",
    "v":"O.O.OO",
    "w":".OOO.O",
    "x":"OO..OO",
    "y":"OO.OOO",
    "z":"O..OOO",
    " ":"......"
}

numdict = {
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO..",
}

def get_key_alpha(val):
    for key, value in alphadict.items():
        if val == value:
            return key
        
def get_key_num(val):
    for key, value in numdict.items():
        if val == value:
            return key

alphanum = False
output = ""
args = sys.argv[1:]
result = ""
lastWasNum = False
capNext = False
numNext = False

for arg in args:
    result += " " + arg

result = result[1:]

for i in range(len(result)):
    if result[i] == "O" or result[i] == ".":
        pass
    else:
        alphanum = True

if alphanum:
    for char in result:
        if char in numdict:
            if not lastWasNum:
                output += ".O.OOO"
                lastWasNum = True
            output += numdict[char]
        else:
            if char.isupper():
                output += ".....O"
            char = char.lower()
            output += alphadict[char]
            lastWasNum = False
else:
    result = [result[i:i+6] for i in range(0, len(result), 6)]
    for letter in result:
        if letter == ".O.OOO":
            numNext = True
        elif letter == "......":
            numNext = False
            output += " "
        elif letter == ".....O":
            capNext = True
        elif numNext:
            output += get_key_num(letter)
        else:
            if capNext:
                output += (get_key_alpha(letter)).upper()
                capNext = False
            else:
                output += get_key_alpha(letter)

print(output)
