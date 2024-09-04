import sys

# Mappings using dict
ENGLISH_TO_BRAILLE_NUMERIC = {
    '1' : 'O.....',
    '2' : 'O.O...',
    '3' : 'OO....',
    '4' : 'OO.O..',
    '5' : 'O..O..',
    '6' : 'OOO...',
    '7' : 'OOOO..',
    '8' : 'O.OO..',
    '9' : '.OO...',
    '0' : '.OOO..',
}

# Mappings using dict
ENGLISH_TO_BRAILLE_ALPHA = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'p' : 'OOO.O.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}


# Mappings using dict
BRAILLE_TO_ENGLISH_ALPHA = {
    value : key for key, value in ENGLISH_TO_BRAILLE_ALPHA.items()
}

# Mappings using dict
BRAILLE_TO_ENGLISH_NUMERIC = {
    value : key for key, value in ENGLISH_TO_BRAILLE_NUMERIC.items()
}

# More commonly used braille
BRAILLE_SPACE   = '......'
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMERIC = '.O.OOO'

def isThisBraille(text : str) -> bool: return set(text) <= set('.O') and not len(text) % 6

def englishToBraille(text: str) -> str:
    res = []
    numFollow = False

    for char in text:
        if char == ' ':
            numFollow = False
            res.append(BRAILLE_SPACE)
        elif char.isdigit():
            if not numFollow:
                res.append(BRAILLE_NUMERIC)
                numFollow = True
            res.append(ENGLISH_TO_BRAILLE_NUMERIC[char])
        elif char.isalpha():
            if char.isupper():
                res.append(BRAILLE_CAPITAL)
            res.append(ENGLISH_TO_BRAILLE_ALPHA[char.lower()])
            numFollow = False
        else:
            # You could add logic here for any special characters if needed
            pass

    return ''.join(res)

def brailleToEnglish(text: str) -> str:
    res = []
    capFollow = False
    numFollow = False

    for i in range(0, len(text), 6):
        brailleCode = text[i:i + 6]

        if brailleCode == BRAILLE_CAPITAL:
            capFollow = True
        elif brailleCode == BRAILLE_NUMERIC:
            numFollow = True
        elif brailleCode == BRAILLE_SPACE:
            numFollow = False
            res.append(' ')
        elif numFollow and brailleCode in BRAILLE_TO_ENGLISH_NUMERIC:
            res.append(BRAILLE_TO_ENGLISH_NUMERIC[brailleCode])
        elif brailleCode in BRAILLE_TO_ENGLISH_ALPHA:
            char = BRAILLE_TO_ENGLISH_ALPHA[brailleCode]
            if capFollow:
                res.append(char.upper())
                capFollow = False
            else:
                res.append(char)
    
    return ''.join(res)

def main():
    text = ' '.join(sys.argv[1:])
    brailleToEnglish(text) if isThisBraille(text) else englishToBraille(text)

if __name__ == '__main__':
    main()