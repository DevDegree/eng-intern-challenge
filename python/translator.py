import sys

string = ""
for i in range(1, len(sys.argv)):
    string += sys.argv[i]
    string += " "

string = string[:-1]

def isBraille(string):
    for i in string:
        if i != "." and i != "O":
            return False
        
    return True

englishToBraile = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',

    "Capital": ".....O",
    "Decimal": ".O...O",
    "Number": ".O.OOO",
}

englishToBraileNums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ',': '.O....', ';': '.OO...', ':': '.O.O..', '.': '.O.OO.', '!': '.OO.O.',
    '?': '.OO..O', '-': '..O.O.', '/': '.O.O..', '(': '.O.O.O', ')': 'O..O.O', 
    '<': 'OO...O', '>': '..OO.O', 
}

brailleToEnglish = {v: k for k, v in englishToBraile.items()}
brailleToEnglishNums = {v: k for k, v in englishToBraileNums.items()}

stringIsBraille = isBraille(string)

if stringIsBraille:
    english = []
    capitalize = False
    number_mode = False

    letters = [string[i:i+6] for i in range(0, len(string), 6)]

    for braille_char in letters:

        print(braille_char)

        if braille_char == ".....O":
            capitalize = True

        elif braille_char == ".O.OOO":
            number_mode = True

        elif braille_char == ".O...O":
            english.append(".")

        else:
            if capitalize:
                english.append(brailleToEnglish[braille_char].upper())
                capitalize = False

            elif number_mode:
                if braille_char == "......":
                    english.append(" ")
                    number_mode = False
                    continue

                english.append(brailleToEnglishNums[braille_char])
                    
            else:
                english.append(brailleToEnglish[braille_char])

    print(''.join(english))

else:
    braille = []

    numberActive = False
    for char in string:

        if char.isupper():
            braille.append(".....O")  # Capital letter symbol
            char = char.lower()

        if char.isdigit() and not numberActive:
            braille.append(".O.OOO")  # Number follows symbol
            numberActive = True

        if char == " ":
            numberActive = False

        if char in englishToBraile:
            braille.append(englishToBraile[char])

        else:
            braille.append(englishToBraileNums[char])

        # print(char, braille)

    print(''.join(braille))


