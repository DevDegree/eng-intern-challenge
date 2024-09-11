# plan: use a map to store the encodings to letters
# make a function to check if text or braille
# make a function to convert text to braille
# make a function to convert braille to binary

# note that if its a number for numbers, use: num = (ord(char) - ord("a"));
import sys

englishToBraille = {
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
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO',
}

brailleToEnglish = {v: k for k, v in englishToBraille.items()}

# add the numbers later because you do not want conflicting keys in the braille to english
englishToBraille.update({
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
})

lettersToNumbers = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0',
}

def isBraille(text):
    if (len(text) % 6 != 0 ):
        return False
    else:
        # you want to make sure that every combination is inside the braille to english map
        # you also want to make sure that you are ONLY capitalizing letters, not numbers or punctuation
        # when in numMode, you want to make sure that you are only running by numbers or spaces, NOT punctuation, NOT other letters,
        asciia = ord('a')
        asciiz = ord('z')
        numMode = False
        capMode = False
        last = ""
        for i in range(0, len(text) - 5, 6): 
            substring = text[i:i+6]
            if substring not in brailleToEnglish:
                return False # if the combination is not inside the map, return false, it should be translated to braille
            char = brailleToEnglish[substring]
            if capMode: # the char must be a letter
                if char == 'num' or char == 'cap':
                    return False
                if (ord(char) < asciia or ord(char) > asciiz):
                    return False
                else:
                    capMode = False
            if char == ' ':
                numMode = False
            if numMode: # the char must be a number, so between a - j
                if char == 'num' or char == 'cap':
                    return False
                if (ord(char) < asciia or ord(char) > ord('j')):
                    return False
            if char == 'cap':
                capMode = True
            elif char == 'num':
                numMode = True
            last = char
    if last == 'num' or last == 'cap': # does not end with capital follows or number follows
        return False
    return True # otherwise, return true, it should be translated to english

def translateEnglishToBraille(text) :
    ans = []
    asciiA = ord('A')
    asciiZ = ord('Z')
    ascii0 = ord('0')
    ascii9 = ord('9')
    numMode = False
    for char in text:
        asciiVal = ord(char)
        # check if upper case
        if (asciiVal >= asciiA and asciiVal <= asciiZ):
            ans.append(englishToBraille['cap'])
            ans.append(englishToBraille[char.lower()])
        elif (asciiVal >= ascii0 and asciiVal <= ascii9): # check if its a number
            if not(numMode):
                numMode = True
                ans.append(englishToBraille['num'])
            ans.append(englishToBraille[char])
        elif (char == ' '): # check if its a space
            numMode = False
            ans.append(englishToBraille[char])
        else:
            ans.append(englishToBraille[char])
        
    return ''.join(ans)

def translateBrailleToEnglish(text):
    ans = []
    numMode = False
    capMode = False
    for i in range(0, len(text) - 5, 6):

        char = brailleToEnglish[text[i:i+6]]
        if char == ' ':
            numMode = False
            ans.append(char)
        elif char == 'cap':
            capMode = True
        elif char == 'num':
            numMode = True
        elif numMode:
            ans.append(lettersToNumbers[char])
        elif capMode:
            ans.append(chr(ord(char) - 32))
            capMode = False
        else:
            ans.append(char)
    return ''.join(ans)

def main():
    inputString = " ".join(sys.argv[1:])
    if len(inputString) > 0:
        if isBraille(inputString):
            print(translateBrailleToEnglish(inputString))
        else:
            print(translateEnglishToBraille(inputString))

if __name__ == '__main__':
    main()