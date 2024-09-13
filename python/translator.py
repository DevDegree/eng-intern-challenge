import sys

brailleToEnglish = {
  "a": "O.....",
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
}

brailleFollows = {
    "cap": ".....O",
    "dec": ".O...O",
    "num": ".O.OOO",
}

brailleToNums = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

brailleToSyms = {
    ".": "..OO.O",
    ",": "..O...",
    "?": "..O.OO",
    "!": "..OOO.",
    ":": "..OO..",
    ";": "..O.O.",
    "-": "....OO",
    "/": ".O..O.",
    "<": ".OO..O",
    ">": "O..OO.",
    "(": "O.O..O",
    ")": ".O.OO.",
    " ": "......",
}

braille = [".", "O"]

def isBraille(input):
    for x in range(6):
        if input[x] not in braille:
            return False
    return True

def getEnglishForm(letter, brailleList):
    word = ""
    for char, braille in brailleList.items():
        if letter == braille:
            word += char
    
    return word

def convertToEnglish(input):
    letter = ""
    cmd = ""
    word = ""

    l = 0
    r = 6

    while(r <= len(input)):
        while (l < r):
            letter += input[l]  
            l = l + 1
        
        if letter in brailleFollows.values():
            for follows, braille in brailleFollows.items():
                if letter == braille:
                    cmd = follows

        elif ((cmd == "" or cmd == "cap") and (letter in brailleToEnglish.values())):
            if (cmd == "cap"):
                word += getEnglishForm(letter, brailleToEnglish).capitalize()
                cmd = ""
            else: 
                word += getEnglishForm(letter, brailleToEnglish)  

        elif ((cmd == "" or cmd == "dec" or cmd == "num") and (letter in brailleToSyms.values())):
            word += getEnglishForm(letter, brailleToSyms)
        
        elif cmd == "num" and letter in brailleToNums.values():
            word += getEnglishForm(letter, brailleToNums)

        r = r + 6
        letter = ""
        
    return word
       
def convertToBraille(input):
    word = ""
    cmd = ""

    for letter in input:
        if letter.isupper() or letter in brailleToEnglish:
            if letter.isupper():
                word += brailleFollows.get("cap")
                word += brailleToEnglish.get(letter.lower())
            else:
                word += brailleToEnglish.get(letter)
        
        elif letter in brailleToNums:
            if (cmd == ""):
                cmd = "num"
                word += brailleFollows.get("num")
            word += brailleToNums.get(letter)

        elif letter in brailleToSyms:
            word += brailleToSyms.get(letter)

    return word

def translator():
    input = ""

    # getting inputs
    n = len(sys.argv)
    for i in range(1, n):
        input += sys.argv[i]
        if i == n-1:
            break
        input += " "

    if (isBraille(input)):
        print (convertToEnglish(input))
    else:
        print (convertToBraille(input))

translator()