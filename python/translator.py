import sys
def translate(stringList):
    letterDict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '!': '..O.OO',
    '(': '.OOO..',
    ')': '.OOOO.',
    '-': '..O...',
    '?': '.OO.O.',
    '/': '..OO..',
    ':': 'O.O...',
    ';': '..OO..',
    "'": '..O...',
    '"': '..O..O',
    ',': 'O.....',
    '.': '.OO...',
    ' ': '......',
    'A': '.....OO.....',
    'B': '.....OO.O...',
    'C': '.....OOO....',
    'D': '.....OOO.O..',
    'E': '.....OO..O..',
    'F': '.....OOOO...',
    'G': '.....OOOOO..',
    'H': '.....OO.OO..',
    'I': '.....O.OO...',
    'J': '......',
    'K': '.....OO...O.',
    'L': '.....OO.O.O.',
    'M': '.....OOO..O.',
    'N': '.....OOO.OO.',
    'O': '.....OO..OO.',
    'P': '.....OOOO.O.',
    'Q': '.....OOOOOO.',
    'R': '.....OO.OOO.',
    'S': '.....O.OO.O.',
    'T': '....O.',
    'U': '.....OO...OO',
    'V': '.....OO.O.OO',
    'W': '.....O.OOO.O',
    'X': '.....OOO..OO',
    'Y': '.....OOO.OOO',
    'Z': '.....OO..OOO'}
    numberDict = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    }

    check = ""
    res = ""
    check1 = True
    numCheck = False
   
    c = " ".join(stringList)
    if "O." in c:
        check1 = False
    
    
    if check1:
        for i in c:
            if i in letterDict:
                if i == " ":
                    numCheck = False
                res+=letterDict[i]
            elif i in numberDict:
                numCheck = True
                res+=".O.OOO"
            if numCheck:
                res+=numberDict[i]
           
    
    if check1 == False:
        for i in c:
            if check == "......":
                numCheck == False
                res+=list(letterDict.keys())[list(letterDict.values()).index(check)]
                check = ""
            if check == ".O.OOO":
                    numCheck=True
                    check = ""
            if numCheck:
                if check in numberDict.values():
                    res+=list(numberDict.keys())[list(numberDict.values()).index(check)]
                    check = ""


            if check in letterDict.values():
                key1 = list(letterDict.keys())[list(letterDict.values()).index(check)]
                res+=key1
                check = ""
                
            
                        
            
            check+=i
        res+=list(letterDict.keys())[list(letterDict.values()).index(check)]
  
    return res
    
def main(c):
   print(translate(c))

if __name__ == "__main__":
    main(sys.argv[1:])
