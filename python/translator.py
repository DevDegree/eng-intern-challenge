# William Li
# william.li3@uwaterloo.ca
import sys

CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......'
}
BRAILLE_TO_ALPHABET = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}
BRAILLE_TO_NUMBER = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def isCharCapital(char: str) -> bool:
    return ord(char) >= 65 and ord(char) <= 90

def isCharNumber(char: str) -> bool:
    return ord(char) >= 48 and ord(char) <= 57

def convertToBraille(char: str) -> str:
    if char not in ENGLISH_TO_BRAILLE:
        return ""
    return ENGLISH_TO_BRAILLE[char]

def translateChar(char: str) -> str:
    res = ""

    if (isCharCapital(char)):
        char = char.lower()
        res += CAPITAL
    res += convertToBraille(char)

    return res

def translateBraille(braille: str, isCapital: bool, isNumber: bool) -> str:
    if braille not in BRAILLE_TO_ALPHABET and braille not in BRAILLE_TO_NUMBER:
        return ""

    if isCapital:
        return BRAILLE_TO_ALPHABET[braille].upper()
    elif isNumber:
        return BRAILLE_TO_NUMBER[braille]
    
    return BRAILLE_TO_ALPHABET[braille]

# splits input into braille symbols
def splitBraille(input: str) -> str:
    res = []
    temp = ""
    for letter in input:
        temp += letter
        if len(temp) == 6:
            res.append(temp)
            temp = ""
    
    return res
        

def translateEnglishToBraille(input: str) -> str:
    res = ""
    prevIsNumber = False

    for letter in input:
        if (isCharNumber(letter)):
            # if its start of a new number, add numberFollows to result
            if (not prevIsNumber):
                res += NUMBER
            prevIsNumber = True
        else:
            prevIsNumber = False

        res += translateChar(letter)
    
    return res

def translateBrailleToEnglish(input: str) -> str:
    braille = splitBraille(input)
    res = []
    isCapital = False
    isNumber = False
    for symbol in braille:
        # if isNumber is true and we reach a value that isn't a number
        if isNumber and symbol not in BRAILLE_TO_NUMBER:
            isNumber = False

        if symbol == CAPITAL:
            isCapital = True
        elif symbol == NUMBER:
            isNumber = True
        else:
            res.append(translateBraille(symbol, isCapital, isNumber))
            isCapital = False
    return "".join(res)

def isEnglish(input: str) -> bool:
    # each braille symbol must have 6 chars
    if len(input) % 6 != 0:
        return True

    # each braille letter contains a '.'
    # At least for the requirements no english should contain '.'
    for letter in input:
        if letter == ".":
            return False
    
    return True

def translate(input: str) -> str:
    if isEnglish(input):
        return translateEnglishToBraille(input)

    return translateBrailleToEnglish(input)
    
if __name__ == "__main__":
    args = sys.argv[1:]
    input = " ".join(args)
    print(translate(input), end="")