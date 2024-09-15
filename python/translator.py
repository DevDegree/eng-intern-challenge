# 1. find if input needs encoding or decoding
# 2. encode/decode 

import sys

def encode(inp):
    ifNum = False
    encodedict = {"a":"O.....", "b":"O.O...","c":"OO....","d":"OO.O..","e":"O..O..","f":"OOO...","g":"OOOO..","h":"O.OO..","i":".OO...","j":".OOO..","k":"O...O.","l":"O.O.O.","m":"OO..O.","n":"OO.OO.","o":"O..OO.","p":"OOO.O.","q":"OOOOO.","r":"O.OOO.","s":".OO.O.","t":".OOOO.","u":"O...OO","v":"O.O.OO","w":".OOO.O","x":"OO..OO","y":"OO.OOO","z":"O..OOO"," ":"......"}
    encodeDecdict = {".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"..O.O.","-":"....OO","/":".O..O.","<":".OO..O",">":"O..OO.","(":"O.O..O",")":".O.OO."}
    encodeNumdict = {"1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO.."}
    length = len(inp)
    res = ""
    while(length >= 1):
        curChar = inp[0]
        if curChar in encodeDecdict:
            res += ".O...O"
            res += encodeDecdict[curChar]
        elif curChar in encodeNumdict:
            if ifNum == False:
                res += ".O.OOO"
                ifNum = True;
            res += encodeNumdict[curChar]
        elif curChar == " ":
            ifNum = False
            res += "......"
        else:
            if curChar.isupper():
                res += ".....O"
                curChar = curChar.lower()
            res += encodedict[curChar]
        length-=1
        inp = inp[1:]
    return res

def decode(inp):
    res = ""
    ifCap = False
    ifNum = False
    ifDec = False
    decodedict = {"O.....":"a", "O.O...":"b","OO....":"c","OO.O..":"d","O..O..":"e","OOO...":"f","OOOO..":"g","O.OO..":"h",".OO...":"i",".OOO..":"j","O...O.":"k","O.O.O.":"l","OO..O.":"m","OO.OO.":"n","O..OO.":"o","OOO.O.":"p","OOOOO.":"q","O.OOO.":"r",".OO.O.":"s",".OOOO.":"t","O...OO":"u","O.O.OO":"v",".OOO.O":"w","OO..OO":"x","OO.OOO":"y","O..OOO":"z"}
    decodedecdict = {"..OO.O":".","..O...":",","..O.OO":"?","..OOO.":"!","..OO..":":","..O.O.":";","....OO":"-",".O..O.":"/",".OO..O":"<","O..OO.":">","O.O..O":"(",".O.OO.":")"}
    decodeNumdict = {"O.....":"1", "O.O...":"2","OO....":"3","OO.O..":"4","O..O..":"5","OOO...":"6","OOOO..":"7","O.OO..":"8",".OO...":"9",".OOO..":"0"}
    length = len(inp)
    while(length >= 6):
        curChar = str(inp[:6])
        if (curChar == "......"):
            ifNum = False
            res += " "
        elif ifNum:
            res += decodeNumdict[curChar]
        elif ifDec:
            res += decodedecdict[curChar]
            ifDec = False
        elif (curChar == ".O...O"):
            ifDec = True
        elif(curChar == ".....O"):
            ifCap = True
        elif(curChar == ".O.OOO"):
            ifNum = True
        else:
            if (ifCap == True):
                res += decodedict[curChar].capitalize()
                ifCap = False
            else:
                res += decodedict[curChar]
        length -= 6
        inp = str(inp[6:])

    return res

def main():
    currentInput = " ".join(sys.argv[1:])
    # currentInput = input()
    output = ""
    if len(currentInput) < 6:
        output = encode(currentInput)
    else:
        brailleList = ["O.....","O.O...","OO....","OO.O..","O..O..","OOO...","OOOO..","O.OO..",".OO...",".OOO..","O...O.","O.O.O.","OO..O.","OO.OO.","O..OO.","OOO.O.","OOOOO.","O.OOO.",".OO.O.",".OOOO.","O...OO","O.O.OO",".OOO.O","OO..OO","OO.OOO","O..O..",".....O",".O...O",".O.OOO","..OO.O","..O...","..O.OO","..OOO.","..OO..","..O.O.","....OO",".O..O.",".OO..O","O.O..O",".O.OO.","......"]
        firstChar = str(currentInput[:6])
        # print(firstChar)
        if firstChar in brailleList:
            output = decode(currentInput)
        else:
            output = encode(currentInput)
    print(output)

if __name__ == '__main__':
    main()
