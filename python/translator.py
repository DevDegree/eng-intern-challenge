import sys

letters = {
    'a':'O.....', 'b':'O.O...', 'c':'OO....',
    'd':'OO.O..', 'e':'O..O..', 'f':'OOO...',
    'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...',
    'j':'.OOO..', 'k':'O...O.', 'l':'O.O.O.',
    'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.',
    'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.',
    's':'.OO.O.', 't':'.OOOO.', 'u':'O...OO',
    'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO',
    'y':'OO.OOO', 'z':'O..OOO'
}

numbers = {
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

brailleLetters = {v: k for k, v in letters.items()}

brailleNumbers = {v: k for k, v in numbers.items()}

def toBraille(text):
    translated = ''
    for i in range(len(text)):
        char = text[i]
        if char.isdigit():
            if not (i-1>=0 and text[i-1].isdigit()):
                translated += '.O.OOO'
            translated += numbers[char]
        elif char == ' ':
            translated += '......'
        else:
            if char.isupper():
                translated += '.....O'
                char = char.lower()
            translated += letters[char]
    return translated

def toEnglish(text):
    translated = ''
    capitalFollows = False
    numbersFollows = False
    for i in range(0, len(text), 6):
        char = text[i:i+6]
        if char == '.....O':
            capitalFollows = True
            continue
        if char == '.O.OOO':
            numbersFollows = True
            continue
        if char == '......':
            translated += ' '
            numbersFollows = False
            continue
        if numbersFollows:
            translated += brailleNumbers[char]
        if capitalFollows:
            translated += brailleLetters[char].upper()
            capitalFollows = False
        else:
            translated += brailleLetters[char]
    return translated

def translate(text):
    if all(char in 'O.' for char in text):
        translated = toEnglish(text)
    else:
        translated = toBraille(text)
    print(translated)

if __name__ == "__main__":
    if len(sys.argv)==1:
        exit(1)
    text = ' '.join(sys.argv[1:])
    translate(text)