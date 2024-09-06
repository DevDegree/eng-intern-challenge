import sys


eng_to_braille = {
    'a': 'O.....',  
    'b': 'O.O...',  
    'c': 'OO....',  
    'd': 'OO.O..',  
    'e': 'O..O..',  
    'f': 'OOO...',  
    'g': 'OOOO..',  
    'h': 'O.OO..',  
    'i': '.OO...',  
    'j': '.OOO..',  
    'k': 'O...O.',  
    'l': 'O.O.O.',  
    'm': 'OO..O.',  
    'n': 'OO.OO.',  
    'o': 'O..OO.',  
    'p': 'OOO.O.',  
    'q': 'OOOOO.',  
    'r': 'O.OOO.',  
    's': '.OOOO.',  
    't': '.OOOOO',  
    'u': 'O...OO',  
    'v': 'O.O.OO', 
    'w': '.OOO.O',  
    'x': 'OO..OO',  
    'y': 'OO.OOO',  
    'z': 'O..OOO', 
    '.': '..OO.O',  
    '?': '..O.OO',  
    '!': '..OOO.',  
    ':': '..OO..',  
    ';': '..O.O.',  
    '-': '..O.O.',  
    '/': '.O..O.',  
    '<': '.OO..O',
    '>': "O..OO.",  
    '(': '.OO.O.',  
    ')': '.OOOO.',  
    ",": '..O...',  
    ' ': '......',
    'capital': '.....O',  
    'decimal': '.O...O',  
    'number': '.O.OOO'    
}

digits_to_braille = {
    '1': 'O.....',  
    '2': 'O.O...',  
    '3': 'OO....',  
    '4': 'OO.O..',  
    '5': 'O..O..',  
    '6': 'OOO...',  
    '7': 'OOOO..',  
    '8': 'O.OO..',  
    '9': '.OO...',  
    '0': '.OOO..'   
}


braille_to_eng = {v: k for k, v in eng_to_braille.items()}
braille_to_eng["O..OO."] = "o"

braille_to_digits = {v: k for k,v in digits_to_braille.items()}

def split_by_6(string):
    while string:
        yield string[:6]
        string = string[6:]


def getEnglish(sentence):
    braille = list(split_by_6(sentence))
    letters = []

    capital = False
    number = False
    decimal = False
    for index, item in enumerate(braille):
        letter = ""
        english = braille_to_eng[item]
        if english == 'capital':
            capital = True
            continue
        elif english == 'number':
            number = True
            continue
        elif english == 'decimal':
            letters.append(".")
            continue
        elif english == ' ':
            number = False

        if (decimal):
            letter = "."
            decimal = False
        elif (number):
            letter = braille_to_digits[item]
            letters.append(letter)
        else:
            letter = english

            # Overlap between > and o, check context
            if letter == "o" and index < len(braille) - 1 and letters[-1] == " " and braille_to_eng[braille[index+1]] == " ":
                letters.append(">")
                continue

            if (capital):
                letter = letter.upper()
                capital = False

        
            letters.append(letter)
    
    return "".join(letters)


def getBraille(sentence):
    letters = list(sentence)
    brailleLetters = []

    number = False

    for index, item in enumerate(letters):
        braille = ""
        # check decimal condition
        if item == "." and letters[index-1].isnumeric() and index < len(letters) - 1 and letters[index+1].isnumeric():
            brailleLetters.append(eng_to_braille['decimal'])
            continue
        if item.isnumeric() == False:
            braille = eng_to_braille[item.lower()]
            if item.isupper():
                brailleLetters.append(eng_to_braille['capital'])
                brailleLetters.append(braille)
                continue
        elif item.isnumeric() and number == False:
            number = True
            brailleLetters.append(eng_to_braille['number'])
        if braille == eng_to_braille[" "]:
            number = False
        if number:
            brailleLetters.append(digits_to_braille[item])
        else:
            brailleLetters.append(braille)
            
    return "".join(brailleLetters)

def checkIfBraille(sentence):
    brailleSet = {"O", "."}
    return set(sentence).issubset(brailleSet) and (len(sentence) % 6 == 0)


def checkArguments(args):
    if len(args) < 2:
        print(f"Incorrect number of arguments. Had: {len(args)} Minimum: 2")
        exit()


def main():
    arguments = sys.argv
    checkArguments(arguments)
    text = " ".join(arguments[1:])
    brailleCheck = checkIfBraille(text)

    if brailleCheck:
        print(getEnglish(text))
    else:
        print(getBraille(text))

main()




    