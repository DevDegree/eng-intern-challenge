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

# Determine if the input is Braille
def isThisBraille(text: str) -> bool:
    return set(text).issubset({'O', '.'}) and len(text) % 6 == 0

# Translate English text to Braille
def englishToBraille(text: str) -> str:
    res = []
    numMode = False

    for char in text:
        if char == ' ':
            numMode = False
            res.append(BRAILLE_SPACE)
        elif char.isdigit():
            if not numMode:
                res.append(BRAILLE_NUMERIC)
                numMode = True
            res.append(ENGLISH_TO_BRAILLE_NUMERIC[char])
        elif char.isalpha():
            if char.isupper():
                res.append(BRAILLE_CAPITAL)
            res.append(ENGLISH_TO_BRAILLE_ALPHA[char.lower()])

    return ''.join(res)

# Translate Braille to English text
def brailleToEnglish(text: str) -> str:
    res = []
    capitalMode = False
    numMode = False

    for i in range(0, len(text), 6):
        brailleCode = text[i: i + 6]

        if brailleCode == BRAILLE_CAPITAL:
            capitalMode = True
        elif brailleCode == BRAILLE_NUMERIC:
            numMode = True
        elif brailleCode == BRAILLE_SPACE:
            numMode = False
            res.append(' ')
        elif numMode and brailleCode in BRAILLE_TO_ENGLISH_NUMERIC:
            res.append(BRAILLE_TO_ENGLISH_NUMERIC[brailleCode])
        elif brailleCode in BRAILLE_TO_ENGLISH_ALPHA:
            letter = BRAILLE_TO_ENGLISH_ALPHA[brailleCode]
            if capitalMode:
                res.append(letter.upper())
                capitalMode = False
            else:
                res.append(letter)

    return ''.join(res)

# Main logic to handle the input and output based on the type of input
def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    if isThisBraille(text):
        print(brailleToEnglish(text))
    else:
        print(englishToBraille(text))

if __name__ == '__main__':
    main()