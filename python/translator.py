import sys

EN_TO_BRAILLE_LETTERS = {
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
    'z' : 'O..OOO',
}

EN_TO_BRAILLE_NUMBERS = {
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

BRAILLE_TO_EN_NUMBERS = {v: k for k, v in EN_TO_BRAILLE_NUMBERS.items()}
BRAILLE_TO_EN_LETTERS = {v: k for k, v in EN_TO_BRAILLE_LETTERS.items()}

SPACE = '......'
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

ALL_BRAILLE_SYMBOLS = set(BRAILLE_TO_EN_LETTERS) | set(BRAILLE_TO_EN_NUMBERS) | {SPACE, CAPITAL_FOLLOWS, NUMBER_FOLLOWS}

def isBraille(text) -> bool:
    #input: braille or english string
    #output: boolean - true if braille, false if english
    if len(text) % 6 != 0:
        return False
    for i in range(0, len(text), 6):
        chunk = text[i:i+6]
        if chunk not in ALL_BRAILLE_SYMBOLS:
            return False
    return True

def translate_braille_to_en(braille: str) -> str: 
    #input: braille string
    #output: translated english string       
    result = ''
    numberFollows = False
    capitalFollows = False
    for i in range(0, len(braille), 6):
        chunk = braille[i:i+6]
        if chunk == SPACE:
            result += ' '
            numberFollows = False
        elif chunk == NUMBER_FOLLOWS:
            numberFollows = True
        elif chunk == CAPITAL_FOLLOWS:
            capitalFollows = True
        elif numberFollows:
            result += BRAILLE_TO_EN_NUMBERS[chunk]
        elif capitalFollows:        
            result += BRAILLE_TO_EN_LETTERS[chunk].upper()
            capitalFollows = False
        elif chunk in BRAILLE_TO_EN_LETTERS:
            result += BRAILLE_TO_EN_LETTERS[chunk]
        elif chunk in BRAILLE_TO_EN_NUMBERS:
            result += BRAILLE_TO_EN_NUMBERS[chunk]
       
    return result

def translate_en_to_braille(english: str) -> str:
    #input: english string
    #output: translated braille string
    result = ''
    numberFollows = False #whether the number follows symbol has been added
    for char in english:
        if char.isdigit():
            if not numberFollows:
                result += NUMBER_FOLLOWS
                numberFollows = True
            result += EN_TO_BRAILLE_NUMBERS[char]
        elif char == ' ':
            result += SPACE
            numberFollows = False #reset number follows
        elif char.isupper():
            result += CAPITAL_FOLLOWS
            result += EN_TO_BRAILLE_LETTERS[char.lower()]
        else: #lowercase
            result += EN_TO_BRAILLE_LETTERS[char]
    return result


def main(args: list) -> None:
    if len(args) < 2:
        print("Usage: python translator.py <text>")
        return
    text = ' '.join(args[1:])
    if isBraille(text):
        print(translate_braille_to_en(text))
    else:
        print(translate_en_to_braille(text))
    
if __name__ == '__main__':
    main(sys.argv)
    