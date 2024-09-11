import sys

#Dictionary for braille to english translation
BrailleToEng = { 
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",
    ".....O": "shift",
    ".O.OOO": "num"
}

#Dictionary for english to braille translation, opposite of previous dictionary
EngToBraille = {BrailleToEng[a]:a for a in BrailleToEng}

#Braille to number conversions
BrailleToNum = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0",
}

#Number to braille conversions, opposite of previous
NumToBraille = {BrailleToNum[a]:a for a in BrailleToNum}

#Run if input is detected as Braille
def translateBraille(string):
    res = ""
    isCaps = False      #Track if translated letter is capital
    isNum = False       #Track if translatec character is a number
    for i in range(0, len(string)//6):
        segment = string[6*i:6*i+6]
        token = BrailleToEng[segment]   #Identify braille character
        
        #Identify special characters
        if token == "shift":
            isNum = False
            isCaps = True
        elif token == "num":
            isCaps = False
            isNum = True
        else:
            if isCaps and token.isalpha():  #If letter is capital
                res += token.capitalize()
            elif isNum:            #If character is numeric in any way
                if segment in BrailleToNum: 
                    res += BrailleToNum[segment]
                elif segment == "......":   #If character is a space, ending number
                    isNum = False   
                    res += token
            else:
                res += token
            isCaps = False
    return res
               
#Run if input is detected as English
def translateEnglish(string):
    res = ""
    isNum = False
    for letter in string: 
        if letter.isnumeric():  
            if not isNum:       #If translating number and number special character not added
                res += EngToBraille["num"]
                isNum = True
            res += NumToBraille[letter]
        else:   #If alphabetical
            if isNum:
                isNum = False
                if letter is not ' ':
                    res += "......" #Space must end number
            if letter.isupper():    #If upper case, add special character
                res += EngToBraille["shift"]
            res += EngToBraille[letter.lower()]
    return res

def translate(string):
    #Check if string is braille by seeing if length is divisible by 6 and is only comprised of O and .
    if len(string) % 6 == 0:
        for char in string:
            if char != 'O' or char != '.':
                return translateBraille(string)
    return translateEnglish(string)     #If not braille, assume English
    
if __name__ == "__main__":
    inputStr = ' '.join(sys.argv[1:])
    print(translate(inputStr))
