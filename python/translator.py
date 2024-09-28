
import sys
import re
# Braille dictionary for alphabet
englishToBrailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'cap': '.....O', 'num': '.O.OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
}


# Braille dictionary for alphabet
brailletoEnglishDict = {
    '.....O': 'cap', '.O.OOO': 'num', '......': ' ', 'O.....': 'a', 'O.O...': 'b', 
    'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 
    'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 
    'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v',
    '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', 

}

#isBraille() Checks if a text is Braille by ensuring the text is in 6 character blocks
#and uses a regex match to check if the string consists of only "O" and "."
def isBraille(text):
    return ((len(text) % 6 == 0) and bool(re.fullmatch(r"^(O|\.)+", text)))

#engToBraille() converts english text to braille
def engToBraille(text):
    numberFlag = False
    brailleText = ""
    for char in text:
        #Capital using ascii 64 - 91 is the capital letters
        if (64 < ord(char) < 91):
            brailleText = brailleText + englishToBrailleDict['cap'] + englishToBrailleDict[char.lower()]
        #Number using ascii 47 - 58 are the numbers
        elif (47 < ord(char) < 58):
            if numberFlag == False:
                brailleText += englishToBrailleDict['num']
                numberFlag = True
            brailleText += englishToBrailleDict[char]
        #Lowercase using ascii 96 - 123 are the lowercase letters
        elif (96 < ord(char) < 123):
            brailleText += englishToBrailleDict[char]
        #Spaces
        else:
            numberFlag = False 
            brailleText += englishToBrailleDict[' ']
    return brailleText

#engToBraille() converts braille to english text
def brailleToEng(text):
    englishText = ""
    numberFlag = False
    capitalFlag = False
    for i in range(0, len(text), 6):
        #grabbing 6 character chunks
        currentBraille = text[i:i+6]

        #setting flags for capitals and numbers
        if (brailletoEnglishDict[currentBraille] == "num") :
            numberFlag = True
            continue
        elif (brailletoEnglishDict[currentBraille] == "cap") :
            capitalFlag = True
            continue
        
        if capitalFlag:
            englishText += brailletoEnglishDict[currentBraille].upper()
            capitalFlag = False
        elif numberFlag:

            #resets flag if a space in encountered
            if brailletoEnglishDict[currentBraille] == ' ':
                numberFlag = False
                englishText += brailletoEnglishDict[currentBraille]
                continue

            #due to mapping from braille to ascii not consistent for 0 this was made
            if ord(brailletoEnglishDict[currentBraille]) == 106:
                englishText += '0'
            else:
                #all other numbers can be properly mapped
                englishText += str(ord(brailletoEnglishDict[currentBraille]) - 96)
        else:
            numberFlag = False
            englishText += brailletoEnglishDict[currentBraille]
    return englishText

#Driver/Wrapper function  
def translate(text):
    if isBraille(text):
        return brailleToEng(text)
    else:
        return engToBraille(text)
    

if __name__ == "__main__":
    input = ' '.join(sys.argv[1:])
    print(translate(input))
