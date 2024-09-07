import sys

string = " ".join(sys.argv[1:])

#first 10 patterns in braille
brKeys = {
    "O...": 1,
    "O.O.": 2,
    "OO..": 3,
    "OO.O": 4,
    "O..O": 5,
    "OOO.": 6,
    "OOOO": 7,
    "O.OO": 8, 
    ".OO.": 9,
    ".OOO": 10,
    ".O.O": 0,
    "....": -1
}

brOff = {
    "..": 0,
    "O.": 10,
    "OO": 20,
    ".O": -1
}

engKeys = {v: k for k, v in brKeys.items()}
engOff = {v: k for k, v in brOff.items()}

#is input braille or english
b = len(string) % 6 == 0

if b:
    for c in string:
        if c != "." and c != "O":
            b = False
            break

def toEng(br):
    ascii = 96
    eng = ""
    cap = False
    num = False
    for i in range(len(br) // 6):
        pattern = br[i * 6 : i * 6 + 6]     
        key = pattern[:4]
        off = pattern[4:]

        n = brKeys.get(key)
        offset = brOff[off]
        if n == None:
            return "INVALID BRAILLE"
        
        #special cases
        if offset == -1:
            if n == -1:
                cap = True
            else:
                eng += "w"
            continue
        if n == 0:
            num = True
            continue
        if n == -1 and offset == 0:
            eng += " "
            num = False
            continue
        
        #normal case
        if num:
            eng += str(n) if n != 10 else "0"
        else:
            code = ascii + n + offset
            #account for w
            if code > 118:
                code +=1
            letter = chr(code)
            eng += letter.capitalize() if cap else letter
        
        cap = False
    return eng

def toBraille(eng):
    upperBr = engKeys[-1] + engOff[-1]
    numBr = engKeys[0] + engOff[20]
    spaceBr = engKeys[-1] + engOff[0]
    wBr = engKeys[10] + engOff[-1]
    num = False
    
    br = ""
    i = 0
    while i < len(eng):
        brCode = ""
        n = 0
        off = 0
        c = eng[i]
        if c.isupper():
            br += upperBr
        elif c.isnumeric() and not num:
            br += numBr
            num = True
        elif c == " ":
            brCode = spaceBr
            num = False
        elif c.lower() == "w":
            brCode = wBr
            
        if brCode == "":
            if num:
                n = int(c) if c != "0" else 10
                off = 0
            else:
                c = c.lower()
                letterNo = ord(c) - 96 if c < "w" else ord(c) - 1 - 96
                off = (letterNo // 10) * 10
                n = letterNo - off
            brCode = engKeys[n] + engOff[off]
        br += brCode
        i+=1
    
    return br

out = ""
if b:
    out = toEng(string)
else:
    out = toBraille(string)

print(out)
