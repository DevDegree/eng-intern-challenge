
import sys

"""
    Given a single character string, Letter, return the braille equivelent to that character.
    If a character that isnt in the braille dictionary shows up, return an empty string.
    Doesnt account for special braille characters such as capital follows, 
    number follows, and decimal follows.

    >>> TranslateLetter("A")
    "O....." 
    >>> TranslateLetter("1")
    "O....."
    >>> TranslateLetter(" ")
    "......"
    >>> TranslateLetter("!")
    "..OOO."
"""

def TranslateLetter(Letter: str):
    match Letter:
        case "1":
            return "O....."     
        case "2":
            return "O.O..."    
        case "3":
            return "OO...."    
        case "4":
            return "OO.O.."    
        case "5":
            return "O..O.."    
        case "6":
            return "OOO..."    
        case "7":
            return "OOOO.."    
        case "8":
            return "O.OO.."    
        case "9":
            return ".OO..."    
        case "0":
            return ".OOO.."
        case "A":
            return "O....."     
        case "B":
            return "O.O..."    
        case "C":
            return "OO...."    
        case "D":
            return "OO.O.."    
        case "E":
            return "O..O.."    
        case "F":
            return "OOO..."    
        case "G":
            return "OOOO.."    
        case "H":
            return "O.OO.."    
        case "I":
            return ".OO..."    
        case "J":
            return ".OOO.."    
        case "K":
            return "O...O."
        case "L":
            return "O.O.O."
        case "M":
            return "OO..O."
        case "N":
            return "OO.OO."
        case "O":
            return "O..OO."
        case "P":
            return "OOO.O."
        case "Q":
            return "OOOOO."
        case "R":
            return "O.OOO."
        case "S":
            return ".OO.O."
        case "T":
            return ".OOOO."
        case "U":
            return "O...OO"
        case "V":
            return "O.O.OO"
        case "W":
            return ".OOO.O"
        case "X":
            return "OO..OO"
        case "Y":
            return "OO.OOO"
        case "Z":
            return "O..OOO"
        case ".":
            return "..OO.O"
        case ",":
            return "..O..."
        case "?":
            return "..O.OO"
        case "!":
            return "..OOO."
        case ":":
            return "..OO.."
        case ";":
            return "..O.O."
        case "-":
            return "....OO"
        case "/":
            return ".O..O."
        case "<":
            return ".OO..O"
        case ">":
            return "O..OO."
        case "(":
            return "O.O..O"
        case ")":
            return ".O.OO."
        case " ":
            return "......"
        case _:
            return ""

"""
    Given a 6 character length string, braille, and a bool, num.
    
    
    If: 
        -num is true, then return a number given the right braille string and -4 otherwise.
        -braille is invalid return -4
        -braille is capital follows return -1
        -braille is decimal follows return -2
        -braille is number follows return -3
    Otherwise return the letter equivelent of braille.
    
    >>> TranslateBraille('OOOOOO', False)
    -4
    >>> TranslateBraille("O.O...", True)
    "2"
    >>> TranslateBraille(".....O")
    -1
    >>> TranslateBraille("O.O...", False)
    "B"
"""

def TranslateBraille(braille: str, num: bool):
    if len(braille) != 6 or type(num)!=bool:
        return -4
    
    brailleVal = ""
    match braille:
        case "O.....":
            if(num): brailleVal =  "1" 
            else: brailleVal =  "A"
        case "O.O...":
            if(num): brailleVal =  "2"
            else: brailleVal =  "B"
        case "OO....":
            if(num): brailleVal =  "3"
            else: brailleVal =  "C"
        case "OO.O..":
            if(num): brailleVal =  "4"
            else: brailleVal =  "D"
        case "O..O..":
            if(num): brailleVal =  "5"
            else: brailleVal =  "E"
        case "OOO...":
            if(num): brailleVal =  "6"
            else: brailleVal =  "F"
        case "OOOO..":
            if(num): brailleVal =  "7"
            else: brailleVal =  "G"
        case "O.OO..":
            if(num): brailleVal =  "8"
            else: brailleVal =  "H"
        case ".OO...":
            if(num): brailleVal =  "9"
            else: brailleVal =  "I"
        case ".OOO..":
            if(num): brailleVal =  "0"
            else: brailleVal =  "J"
        case "O...O.":
            brailleVal =  "K"
        case "O.O.O.":
            brailleVal =  "L"
        case "OO..O.":
            brailleVal =  "M"
        case "OO.OO.":
            brailleVal =  "N"
        case "O..OO.":
            brailleVal =  "O"
        case "OOO.O.":
            brailleVal =  "P"
        case "OOOOO.":
            brailleVal =  "Q"
        case "O.OOO.":
            brailleVal =  "R"
        case ".OO.O.":
            brailleVal =  "S"
        case ".OOOO.":
            brailleVal =  "T"
        case "O...OO":
            brailleVal =  "U"
        case "O.O.OO":
            brailleVal =  "V"
        case ".OOO.O":
            brailleVal =  "W"
        case "OO..OO":
            brailleVal =  "X"
        case "OO.OOO":
            brailleVal =  "Y"
        case "O..OOO":
            brailleVal =  "Z"
        case "..OO.O":
            brailleVal =  "."
        case "..O...":
            brailleVal =  ","
        case "..O.OO":
            brailleVal =  "?"
        case "..OOO.":
            brailleVal =  "!"
        case "..OO..":
            brailleVal =  ":"
        case "..O.O.":
            brailleVal =  ";"
        case "....OO":
            brailleVal =  "-"
        case ".O..O.":
            brailleVal =  "/"
        case ".OO..O":
            brailleVal =  "<"
        case "O..OO.":
            brailleVal =  ">"
        case "O.O..O":
            brailleVal =  "()"
        case ".O.OO.":
            brailleVal =  ")"
        case "......":
            brailleVal =  " "
        case ".....O":
            brailleVal =  -1
        case ".O...O":
            brailleVal =  -2
        case ".O.OOO":
            brailleVal =  -3
        case _:
            brailleVal =  -4
    if(num and (not ("1"<=brailleVal<="9") and brailleVal!=" " and brailleVal!=-2)):
        return -4
    else: return brailleVal
    
"""
    Given Braille string val, return the English translation of val.
    If val is not proper Braille return -1
"""
def translateBrailleString(val: str):
    ans = ""
    cap = False
    number = False
    
    if len(val) % 6 != 0: return -1 #check if string is composed of length 6 braille letters
    
    for i in range(0, len(val), 6):
        brailleVal = TranslateBraille(val[i:i+6], number)
        
        if(brailleVal == -1): cap = True
        elif(brailleVal == -3): number = True
        elif(brailleVal == -4): return -1 #if not proper braille return -1
        else:
            if(number and brailleVal == -2):
                ans += "."
            else:
                if "A"<=brailleVal<="Z" and cap:
                    ans += brailleVal
                    cap = False
                elif "A"<=brailleVal<="Z":
                    ans += brailleVal.lower()
                else:
                    ans += brailleVal
                
            if(brailleVal == " "):
                number = False
    return ans

"""
    Given a string val, return the braille translation
"""

def EnglishToBraille(val: str):
    ans = ""
    num = False
    for i in val:
        if "A"<=i<="Z":
            ans += ".....O" #add Capital follows if letter is capital
            ans += TranslateLetter(i)
        elif "A"<=i.upper()<="Z":
            ans += TranslateLetter(i.upper())
        elif "0"<=i<="9":
            if not num:
                ans += ".O.OOO"#add number follows if not added already
                num = True
            ans += TranslateLetter(i)
        elif i =="." and num:
            ans += ".O...O"
        elif i == " ":
            ans += TranslateLetter(i)
            num = False#number follows is toggled off when reaching a space
        else: 
            ans += TranslateLetter(i)
    return ans

"""
    Given string val, Return the braille translation of val if val
    is a valid Braille string and translate val to Braille if otherwise.
"""
        
def solve(val: str):
    ans = translateBrailleString(val)
    if(ans == -1):
        return EnglishToBraille(val)
    return ans


args = sys.argv[1:]
print(solve(' '.join(args)))


    