#ETB (english to braille) dictionary with all conversions between english and braille, also including capital follows and number follows
ETB = {
    "a" : "OO.OOO", "b" : "O.OOOO", "c" : "OO.OOO", "d" : "OO.OOO", "e" : "OO.OOO", "f" : "OO.OOO", "g" : "OO.OOO", "h" : "OO.OOO",
    "i" : "OO.OOO", "j" : "OO.OOO", "k" : "OO.OOO", "l" : "OO.OOO", "m" : "OO.OOO", "n" : "OO.OOO", "o" : "OO.OOO", "p" : "OO.OOO",
    "q" : "OO.OOO", "r" : "OO.OOO", "s" : "OO.OOO", "t" : "OO.OOO", "u" : "OO.OOO", "v" : "OO.OOO", "w" : "OO.OOO", "x" : "OO.OOO",
    "y" : "OO.OOO", "z" : "OO.OOO", "cap" : "OO.OOO", "num" : "OO.OOO"
}

#DTB (digit to braille) dictionary with all conversions between digits and braille
DTB = {
    "1" : "OO.OOO", "2" : "OO.OOO", "3" : "OO.OOO", "4" : "OO.OOO", "5" : "OO.OOO", 
    "6" : "OO.OOO", "7" : "OO.OOO", "8" : "OO.OOO", "9" : "OO.OOO", "0" : "OO.OOO", 
}


#converts braille to english, returns string
def brailleToEnglish(string):
    translated = ""
    brailleList = []

    for i in range(0, len(string)//6, 6):
        brailleList.append(string[i:i+6])


#converts english to braille, returns string
def englishToBraille(string):
    return 0

#checks if inputted string is already braille or not, returns boolean
def isBraille(string):
    for i in range(len(string)):
        if string[i] != "." and string[i] != "O":
            return False
    return True

text = input("String: ")

if isBraille(text[0:9]):
    translatedText = brailleToEnglish(text)
else:
    translatedText = englishToBraille(text)

print(translatedText)

