import sys
import string

input = ' '.join(sys.argv[1:])
letToBrail = {"A":"O.....", "B":"O.O...", "C":"OO....", "D":"OO.O..","E":"O..O..","F":"OOO...","G":"OOOO..","H":"O.OO..","I":".OO...","J":".OOO..","K":"O...O.","L":"O.O.O.","M":"OO..O.",
           "N":"OO.OO.","O":"O..OO.","P":"OOO.O.","Q":"OOOOO.","R":"O.OOO.","S":".OO.O.","T":".OOOO.","U":"O...OO","V":"O.O.OO","W":".OOO.O","X":"OO..OO","Y":"OO.OOO","Z":"O..OOO"," ":"......"}
commandToBrail = {"CF":".....O","DF":".O...O","NF":".O.OOO"}
numToBrail = {"1":"O.....","2":"O.O...","3":"OO....","4":"OO.O..","5":"O..O..","6":"OOO...","7":"OOOO..","8":"O.OO..","9":".OO...","0":".OOO.."}
decToBrail = {".":"..OO.O",",":"..O...","?":"..O.OO","!":"..OOO.",":":"..OO..",";":"..O.O.","-":"....OO","/":".O..O.","<":".OO..O",">":"O..OO.","(":"O.O..O",")":".O.OO."}
brailToLet = {v: k for k, v in letToBrail.items()}
brailToNum = {v: k for k, v in numToBrail.items()}
brailToDec = {v: k for k, v in decToBrail.items()}
brailToCommand = {v: k for k, v in commandToBrail.items()}

def is_english(sentence):
    
    braille_segments = [sentence[i:i+6] for i in range(0, len(sentence), 6)]
    braille_patterns = set(letToBrail.values()) | set(commandToBrail.values()) | set(numToBrail.values()) | set(decToBrail.values())
    if all(segment in braille_patterns for segment in braille_segments):
        return False
    
    if any(char.isalpha() or char.isdigit() or char in string.punctuation for char in sentence):
        return True
    return False

isCapital = False
isNumber = False
isPrevNumber = False
isDecimal = False
isEnglish = is_english(input)
output = ""
currentBrailString = ""

for letter in input:
    if isEnglish:        
        isCapital = letter.isupper()
        isNumber = letter.isdigit()
        isDecimal = letter in string.punctuation
        if isCapital:            
            output += commandToBrail["CF"]
            output+= letToBrail[letter.upper()]
            isPrevNumber = False
        elif isDecimal:
            output += commandToBrail["DF"]
            output+= decToBrail[letter]
            isPrevNumber = False
        elif isNumber:
            if isPrevNumber == False:
                output += commandToBrail["NF"]
            output+= numToBrail[letter]
            isPrevNumber = True
        else:
            output += letToBrail[letter.upper()]
            isPrevNumber = False
    else:
        currentBrailString += letter
        if len(currentBrailString) == 6:            
            if currentBrailString in brailToCommand.keys():
                status = brailToCommand[currentBrailString]
                isCapital = status == "CF"
                isNumber = status == "NF"
                isDecimal = status == "DF"
            elif isCapital:
                output += brailToLet[currentBrailString]
                isCapital = False
            elif isNumber:
                output += brailToNum[currentBrailString]
            elif isDecimal:
                output += brailToDec[currentBrailString]
                isDecimal = False
            else:
                output += brailToLet[currentBrailString].lower()
            currentBrailString = ""

print(output)

