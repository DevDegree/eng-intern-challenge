import sys

BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

def brailleToEnglish(braille):
    result = []
    i = 0
    capitalizeNext = False
    numberMode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == '.....O':
            capitalizeNext = True
        elif symbol == '.O.OOO':
            numberMode = True
        elif symbol in BRAILLE_TO_ENGLISH:
            char = BRAILLE_TO_ENGLISH[symbol]
            if char == ' ':
                numberMode = False
            elif numberMode:
                if char in 'abcdefghij':
                    char = str('1234567890'['abcdefghij'.index(char)])
            elif capitalizeNext:
                char = char.upper()
                capitalizeNext = False
            result.append(char)
        
        i += 6

    return ''.join(result)

def englishToBraille(english):
    result = []
    numberMode = False

    for char in english:
        if char.isdigit():
            if not numberMode:
                result.append(ENGLISH_TO_BRAILLE['number'])
                numberMode = True
            letterChar = 'abcdefghij'[int(char) - 1] if char != '0' else 'j'
            result.append(ENGLISH_TO_BRAILLE[letterChar])
        elif char == ' ':
            if numberMode:
                numberMode = False
            result.append(ENGLISH_TO_BRAILLE[' '])
        elif char.lower() in ENGLISH_TO_BRAILLE:
            if numberMode:
                result.append(ENGLISH_TO_BRAILLE[' '])
                numberMode = False
            
            if char.isupper():
                result.append(ENGLISH_TO_BRAILLE['capital'])
                char = char.lower()
            
            result.append(ENGLISH_TO_BRAILLE[char.lower()])
        else:
            result.append(char)

    return ''.join(result)

def translate(inputString):
    if set(inputString).issubset({'O', '.'}):
        return brailleToEnglish(inputString)
    else:
        return englishToBraille(inputString)

if __name__ == "__main__":
    inputString = ' '.join(sys.argv[1:])
    print(translate(inputString))
