import sys

def isWordEnglish(word):
    if(any(w.isdigit() for w in word)):
        return True
    elif(" " in word):
        return True
    else:
        for w in word:
            if w in "abcdefghijklmnopqrstuvwxyz":
                return True
            elif w in "ABCDEFGHIJKLMNPQRSTUVWXYZ":
                return True

        if("." in word):
            return False
        else:
            return True


BrailleAlphabet = {"a": "O.....",
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
                   "cap": ".....O",
                   "num": ".O.OOO",
                   "spa": "......"}

BrailleNumber = {"1": "O.....",
                   "2": "O.O...",
                   "3": "OO....",
                   "4": "OO.O..",
                   "5": "O..O..",
                   "6": "OOO...",
                   "7": "OOOO..",
                   "8": "O.OO..",
                   "9": ".OO...",
                   "0": ".OOO..",}

def englishToBraille(word):
    brailleWord=""
    for i in range(len(word)):
        if(word[i].isalpha()):
           if(word[i].isupper()):
               lowerW= word[i].lower()
               brailleWord=brailleWord+BrailleAlphabet["cap"]+BrailleAlphabet[lowerW]
           else:
               brailleWord = brailleWord+BrailleAlphabet[word[i]]
        elif(word[i].isspace()):
            brailleWord = brailleWord +BrailleAlphabet["spa"]
        elif(word[i].isdigit()):
            if(i==0):
                brailleWord = brailleWord + BrailleAlphabet["num"] + BrailleNumber[word[i]]
            elif(word[i-1].isdigit()):
                brailleWord = brailleWord + BrailleNumber[word[i]]
            else:
                brailleWord = brailleWord + BrailleAlphabet["num"]  + BrailleNumber[word[i]]

    return brailleWord


def getKeyOfValue(char, type):
    if(type == "alpha"):
        for key, value in BrailleAlphabet.items():
            if char == value:
                return key
    else:
        for key, value in BrailleNumber.items():
            if char == value:
                return key

def brailleToEnglish(word):
    englishWord = ""
    isCapital = False
    isNum = False
    for i in range(0,len(word),6):
        if(word[i:(i+6)] == "......"):
            isNum = False
            englishWord = englishWord + " "
        elif(word[i:(i+6)] == ".....O"):
            isCapital = True
        elif(word[i:(i+6)] == ".O.OOO"):
            isNum = True
        elif(isNum):
            num = getKeyOfValue(word[i:(i+6)], "num")
            englishWord = englishWord + num
        elif(isCapital):
            letter = getKeyOfValue(word[i:(i+6)], "alpha")
            englishWord = englishWord + letter.upper()
            isCapital = False
        else:
            letter = getKeyOfValue(word[i:(i+6)], "alpha")
            englishWord = englishWord + letter
    return englishWord

def brailleTranslator(str):
    if(isWordEnglish(str)):
        return englishToBraille(str)
    else:
        return brailleToEnglish(str)


if __name__ == "__main__":
    args = sys.argv[1:]
    str = ' '.join(args)
    print(brailleTranslator(str))









