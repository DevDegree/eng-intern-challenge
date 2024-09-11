import sys
import re

## data
braille_dict = {
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
    "z": "O..OOO"
}

braille_nums = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

english_dict = {
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
    "O..OOO": "z" 
}

english_nums = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

## translate
def translate(text):
    if type(text) == "Braille":
        print(transBraToEng(text))
    else:
        print(transEngToBra(text))    

## detect language
def type(text):
    if (text.count(".") + text.count("O") == len(text)):
        return ("Braille")
    return ("Alpha")

## split Braille into single characters    
def splitBraille(brailleText):
    return re.findall('......', brailleText)

## number converter
def convertNum(num):
    if num == ".O....":
        return 48
    else:
        return chr(ord(convertBraToEng(num)) - 48)
    
## translate Braille string to English
def transBraToEng(text):
    text = splitBraille(text)
    cap = False
    number = False
    result = ""
    for char in text:
        if char == "......":
            result += " "
            number = False
            continue
        elif char == ".O.OOO":
            number = True
            continue
        elif cap:
            result += chr(ord(convertBraToEng(char)) - 32)
            cap = False
            continue
        elif number:
            result += convertNum(char)
            continue
        elif char == '.....O':
            cap = True
            continue
        else:
            result += convertBraToEng(char)
    return result            

## translate Braille character to English
def convertBraToEng(char):
    return english_dict[char]

# transltes Braille number to English
def convertBraToNum(num):
    return english_nums[num]

## translate English string to Braille
def transEngToBra(text):
    result = ""
    prevWasNum = False
    for char in text:
        # check if space
        if ord(char) == 32:
            prevWasNum = False
            result += "......"
            continue
        # check if number
        elif checkIfNumber(char):
            if not prevWasNum:
                result += ".O.OOO"
            prevWasNum = True
            result += convertNumToBra(char)
            continue
        # check if caps, if previous char was a number, space is added
        elif ord(char) >= 65 and ord(char) < 91:
            if prevWasNum:
                result += "......"
            prevWasNum = False
            result += ".....O"
            result += convertEngToBra(chr(ord(char) + 32))
            continue
        # if previous char was a number, space is added
        elif prevWasNum:
                result += "......"
        # add lower case letter            
        result += convertEngToBra(char)
        prevWasNum = False
    return result

## translate English character to Braille
def convertEngToBra(char):
    return braille_dict[char]

## translate number character to Braille
def convertNumToBra(num):
    return braille_nums[num]

## checks if char is a number
def checkIfNumber(char):
    if ord(char) >= 48 and ord(char) < 58:
        return True
    return False

def main():
    text = " ".join(sys.argv[1:])
    translate(text)

if __name__ == "__main__":
    main()

#translate("Abc 123 xYz")
#translate(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
#translate(".....OO..........OO.O........OOO..........OO.O..O..O..OOO..............OO.....O.O........OOO...........O.OOOO...........O......O.OOOO.O.........O.O..........O.OOOOO....OO.O.........O.OOOO..O..OOO...")