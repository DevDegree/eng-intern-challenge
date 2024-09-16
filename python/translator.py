import sys

dictionary = {
    "a" : "O.....",
    "b" : "O.O...",
    "c" : "OO....",
    "d" : "OO.O..",
    "e" : "O..O..",
    "f" : "OOO...",
    "g" : "OOOO..",
    "h" : "O.OO..",
    "i" : ".OO...",
    "j" : ".OOO..",
    "k" : "O...O.",
    "l" : "O.O.O.",
    "m" : "OO..O.",
    "n" : "OO.OO.",
    "o" : "O..OO.",
    "p" : "OOO.O.",
    "q" : "OOOOO.",
    "r" : "O.OOO.",
    "s" : ".OO.O.",
    "t" : ".OOOO.",
    "u" : "O...OO",
    "v" : "O.O.OO",
    "w" : ".OOO.O",
    "x" : "OO..OO",
    "y" : "OO.OOO",
    "z" : "O..OOO",
    "cap" : ".....O",
    "dec" : ".O...O",
    "num" : ".O.OOO",
    "." : "..OO.O",
    "," : "..O...",
    "?" : "..O.OO",
    "!" : "..OOO.",
    ":" : "..OO..",
    ";" : "..O.O.",
    "_" : "....OO",
    "/" : ".O..O.",
    "<" : ".OO..O",
    ">" : "O..OO.",
    "(" : "O.O..O",
    ")" : ".O.OO.",
    "space" : "......"
}   
# tests if sentence is english or braille
def isEnglish(sentence):
    # if sentence is less than 6 characters, it cannot possibly be braille
    if(len(sentence) < 6):
        return True
    # here if the first 6 characters of the sentence is not in dict.values, that is,
    # is not a braille symbol, then the sentence is in english
    return not(sentence[:6] in dictionary.values())


def brailleToEnglish(sentence):
    isNumber = False
    toCapitalize = False
    translated = ""
    for i in range(len(sentence)):
        if((i+1) % 6 == 0 and i != 0):
            braille = sentence[i-5:i+1]
            char = getValFromDict(braille)
            if char == "cap" :
                toCapitalize = True
                char = ""
            elif char == "num" :
                isNumber = True
                char = ""
            elif toCapitalize:
                char = char.capitalize()
                toCapitalize = False
            elif isNumber:
                # here we check that we have not reached a space, that is, the end of the number
                if char != "space":
                    # numbering in question is 1-9 then 0 so we have to readjust without ASCII
                    if char == "j":
                        char = "0"
                    elif char == "dec":
                        char = "."
                    # readjustment using ASCII to save space in dictionary
                    else:
                        char = chr(ord(char) - 48)
                # here we set bool back to false to stop reading number and add space
                else:
                    isNumber = False
                    char = " "
            elif char == "space":
                char = " "
            translated = translated + char
    return translated

def englishToBraille(sentence):
    translated = ""
    numSymbolAdded = False
    for i in range(len(sentence)):
        char = sentence[i]
        # checks for ASCII of capital letters
        if (65 <= ord(char) <= 90):
            translated = translated + dictionary.get("cap")
            char = chr(ord(char) + 32)
        # check if digit
        elif (48 <= ord(char) <= 57):
            if(not numSymbolAdded):
                translated = translated + dictionary.get("num")
                numSymbolAdded = True
            if char == "0":
                char = "j"
            else:
                char = chr(ord(char) + 48)
        elif (char == " "):
            # here we need to set bool numSymbolAdded back to false since we have reached end of
            # number and we might need to readd number follows symbol if there are more numbers in
            # sentence
            if((i-1 > -1 and (48 <= ord(sentence[i-1]) <= 57))):
                numSymbolAdded = False
            char = "space"
        # check if number is a decimal and then add decimal follows symbol
        elif (char == "." and (i+1 < len(sentence) and (48 <= ord(sentence[i+1]) <= 57))):
            char = "dec"
        translated = translated + dictionary.get(char)
    return translated

# get key based on value in dictionary
def getValFromDict(val):
    for key, value in dictionary.items():
        if(val == value):
            return key

# reading inputs 
args = sys.argv[1:]
if len(args) >= 1:
    sentence = args[0]
    for i in args[1:]:
        sentence += " " + i
    if(isEnglish(sentence)):
        print(englishToBraille(sentence))
    else:
        print(brailleToEnglish(sentence))


