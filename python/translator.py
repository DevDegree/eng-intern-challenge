import sys

def converter(s):

    # Flag that indicates if we're converting from braille to English 
    braille = True

    # Determine whether the input string is braille or English
    for ch in s:
        if ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN0PQRSTUVWXYZ123456789,/?!():;-<> ":
            braille = False

    if len(s) % 6 != 0:
        braille = False


    
    # Map from English alphabet to braille
    toBraille = {"a": "O.....",
                 "b": "O.O...",
                 "c": "OO....",
                 "d": "OO.O..",
                 "e": "O..O..",
                 "f": "OOO...",
                 "g": "OOOO..",
                 "h": "O.OO..",
                 "i": ".OO...",
                 "j": ".OOO..",
                 "k": "O...O.",
                 "l": "O.O.O.",
                 "m": "OO..O.",
                 "n": "OO.OO.",
                 "o": "O..OO.",
                 "p": "OOO.O.",
                 "q": "OOOOO.",
                 "r": "O.OOO.",
                 "s": ".OO.O.",
                 "t": ".OOOO.",
                 "u": "O...OO",
                 "v": "O.O.OO",
                 "w": ".OOO.O",
                 "x": "OO..OO",
                 "y": "OO.OOO",
                 "z": "O..OOO",
                 ".": "..OO.O",
                 ",": "..O...",
                 "?": "..O.OO",
                 "!": "..OOO.",
                 ":": "..OO..",
                 ";": "..O.O.",
                 "-": "....OO",
                 "/": ".O..O.",
                 "<": ".OO..O",
                 "(": "O.O..O",
                 ")": ".O.OO.",
                 " ": "......"}

    # Mapping from braille to English 
    toEnglish = {v: k for k, v in toBraille.items()}

    # Mapping from letters to numbers
    toNumber = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8", "i":"9", "j":"0"}

    # Mapping from numbers to letters
    toLetter = {v: k for k, v in toNumber.items()}

    # Stores every braille letter (6 characters)
    tempStr = ""

    # Counts number of letters processed
    counter = 1

    # Stores the result string
    newStr = ""

    # Flag to show whether we should add the capital after symbol
    capitalNext = False

    # Flag to show whether we should add the number after symbol
    numberNext = False

    # Convert braille to English    
    if braille:
        for ch in s:
            tempStr = tempStr + ch
            if counter % 6 == 0:
               if tempStr == ".....O":
                   capitalNext = True
               elif tempStr == ".O.OOO":
                   numberNext = True
               else:
                   if capitalNext:
                       newStr = newStr + toEnglish[tempStr].upper()
                       capitalNext = False
                   elif numberNext:
                       if tempStr == "......":
                           numberNext = False
                           newStr = newStr + toEnglish[tempStr]
                       else:
                           newStr = newStr + toNumber[toEnglish[tempStr]]
                   else:
                       newStr = newStr + toEnglish[tempStr]
               tempStr = ""
            counter += 1
    # Convert English to Braille
    else:
        for ch in s:
            if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                newStr = newStr + ".....O"
                newStr = newStr + toBraille[ch.lower()]
            elif ch in "1234567890" and not numberNext:
                numberNext = True
                newStr = newStr + ".O.OOO"
                newStr = newStr + toBraille[toLetter[ch]]
            elif numberNext and ch != " ":
                newStr = newStr + toBraille[toLetter[ch]]
            elif ch == " ":
                numberNext = False
                newStr = newStr + toBraille[ch]
            else:
                newStr = newStr + toBraille[ch]
                
                

    return newStr

if __name__ == "__main__":
    s = ""
    for i in range(1, len(sys.argv) - 1):
        s = s + sys.argv[i] + " "
    s = s + sys.argv[len(sys.argv) - 1]
    print(converter(s))
