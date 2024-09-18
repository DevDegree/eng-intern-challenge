import sys

brailleToEng = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    "......": " ",  "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", 
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", 
    "O.O..O": "(", ".O.OO.": ")", ".....O": "capital follows", ".O.OOO": "number follows"
}

englishToBraille = {v: k for k, v in brailleToEng.items()} # Credit: https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping


def isBraille(text) -> int:
    for char in text:
        if char == 'O' or char == '.':
            continue
        else:
            return 0
    return 1

def translateToEnglish(braille) -> str:
    # 1) Break up braille in chunks
    # 2) If 'capital follows' is detected, then on next iteration, capitlize character. Then set flag to False
    # 3) If 'number follows' is detected, then obtain numerical value via ASCII (Eg, 97 = a, therefore 97-96 = 1). Then set flag to False
    # 4) If step 2 and 3 are not detected/True, then just add the eng character

    capitalFollows = False
    numberFollows = False
    result = ""
    for i in range(0, len(braille), 6):
        brailleChunk = braille[i: i+6]

        if (capitalFollows):
            result += brailleToEng[brailleChunk].upper()
            capitalFollows = False
        elif (numberFollows):
            if (brailleToEng[brailleChunk] == " "):
                numberFollows = False
            result += str(ord(brailleToEng[brailleChunk]) - 96)
        elif brailleToEng[brailleChunk] == "capital follows":
            capitalFollows = True
        elif brailleToEng[brailleChunk] == "number follows":
            numberFollows = True
        else:
            result += brailleToEng[brailleChunk]
            
    return result

def translateToBraille(string) -> str:
    result = ""
    numberFound = False
    for char in string:
        if char.isalpha():
            if numberFound:
                result += englishToBraille[' ']
                numberFound = False

            if char.isupper():
                result += englishToBraille["capital follows"]

            result += englishToBraille[char.lower()]
        elif char.isnumeric():
            if numberFound == False:
                result += englishToBraille["number follows"]
                numberFound = True
            result += englishToBraille[chr(ord(char) + 48)]
        else: # Spaces, dashes, periods, etc
            if numberFound:
                numberFound = False
            result += englishToBraille[char]

    return result

def main():
    joinedText: str = ' '.join(sys.argv[1:])
    result: int = isBraille(joinedText)
    if not result:
        print(translateToBraille(joinedText))
    else:
        print(translateToEnglish(joinedText))

    return

if __name__ == "__main__":
    main()