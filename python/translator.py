import sys

#ETB (english to braille) dictionary with all conversions between english and braille, also including capital follows and number follows
ETB = {
    "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..",
    "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.",
    "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
    "y" : "OO.OOO", "z" : "O..OOO", " " : "......", "cap" : ".....O", "num" : ".O.OOO"
}

#DTB (digit to braille) dictionary with all conversions between digits and braille
DTB = {
    "1" : "O.....", "2" : "O.O...", "3" : "OO....", "4" : "OO.O..", "5" : "O..O..", 
    "6" : "OOO...", "7" : "OOOO..", "8" : "O.OO..", "9" : ".OO...", "0" : ".OOO..", 
}


#converts braille to english, returns string
def brailleToEnglish(string):
    translated = ""
    numFollows = False
    capFollows = False
    brailleList = []

    #puts each 6 digit braille symbol into a list
    for i in range(0, len(string), 6):
        brailleList.append(string[i:i+6])
    
    #iterating through list of braille
    for i in range(0, len(brailleList)):
        #if number
        if numFollows == True:
            #if space, a space is added and the next character is not a number
            if brailleList[i] == "......":
                numFollows = False
                translated += " "
            else:
                #iterates through the dictionary of numbers until it finds matching value, that number is added
                for key, value in DTB.items():
                    if value == brailleList[i]:
                        translated += key
                        break
        #if not a number
        else:
            #iterates through ETB dictionary
            for key, value in ETB.items():
                if value == brailleList[i]:
                    #next character will be capitalized
                    if key == "cap":
                        capFollows = True
                    #next character will be a number
                    elif key == "num":
                        numFollows = True
                    else:
                        #if a capital letter follows, it will capitalize the next letter and turn itself to false
                        if capFollows:
                            translated += key.upper()
                            capFollows = False
                            break
                        #adds an uncapitlized letter
                        else:
                            translated += key
                            break
                            
    return translated

#converts english to braille, returns string
def englishToBraille(string):
    translated = ""
    chars = []
    firstDigit = True

    #populates list with each character of the string
    for i in range(len(string)):
        chars.append(string[i])

    #iterate through list of characters
    for i in range(len(chars)):
        #if digit
        if chars[i].isdigit():
            #if its the first digit, add the num follows signifier
            if firstDigit:
                firstDigit = False
                translated += ETB.get("num")
                translated += DTB.get(chars[i])                
            else:
                translated += DTB.get(chars[i])
        #if space
        elif chars[i] == " ":
            #if following a number, then reset firstDigit, allows for the signifier to be placed again
            if firstDigit == False:
                firstDigit = True
            translated += ETB.get(chars[i])
        #if character
        else:
            #if uppercase, add the capital follows signifier
            if chars[i].isupper():
                translated += ETB.get("cap")
            translated += ETB.get(chars[i].lower())

    return translated

#checks if inputted string is already braille or not, returns boolean
def isBraille(string):
    for i in range(len(string)):
        if string[i] != "." and string[i] != "O":
            return False
    return True

text = sys.argv[1]

if isBraille(text[0:9]):
    translatedText = brailleToEnglish(text)
else:
    translatedText = englishToBraille(text)

print(translatedText)