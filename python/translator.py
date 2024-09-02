import sys

def translator(s):
    translation = ""
    for i in s[0:5]:
        if i == ".":
            translation = brailleHandler(s)
            return translation
    translation = englishHandler(s)
    return translation


def brailleHandler(s):
    translation = ""
    letter = ""
    mydict = dictMaker("braille")
    upper = 0
    for i in range(6,len(s)+1,6):
        letter = mydict.get(s[i-6:i])
        if letter == "cap":
            upper = 1
            continue
        elif letter == "num":
            mydict = dictMaker("braillenums")
        elif letter == " ":
            mydict = dictMaker("braille")
        
        if upper == 1:
            letter = letter.upper()
            upper = 0
        translation += letter
    return translation
         

def englishHandler(s):
    translation = ""
    letter = ""
    edict = dictMaker("english")
    space = 1
    upper = 0
    for i in s:
        letter = i
        if i.isupper():
            translation += edict.get("cap")
            upper = 1 
        elif i.isnumeric():
            if space == 1:
                translation += edict.get("num")
                edict = dictMaker("englishnums")
                space = 0
        elif i == " ":
            edict = dictMaker("english")
            space = 1

        if upper == 1:
            letter = i.lower()
            upper = 0
        letter = edict.get(letter)
        translation += letter
    return translation


def dictMaker(lang):

    english = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.O.O..',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OO.O.O',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    "cap": '.....O',
    "num": '.O.OOO'
                }
    
    englishnums = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.O.O..',
    '0': '.OOO..',
                    }   
    
    match lang:
        case "english":
            return english
        case "englishnums":
            return englishnums
        case "braille":
            braille = dict((v, k) for k, v in english.items())
            return braille
        case "braillenums":
            braillenums = dict((v, k) for k, v in englishnums.items())
            return braillenums
        
if __name__ == "__main__":
  n = len(sys.argv)
  for i in range(1,n):
    s = sys.argv[i]
    print(translator(s), end = "")

# test wants braille spaces btwn braille outputs, thus the code below
    edict = dictMaker("english")
    enumdict = dictMaker("englishnums")
    if (edict.get(s[i].lower()) or enumdict.get(s[i].lower())) != None:
        if i != n-1:
            print("......", end = "")
        


