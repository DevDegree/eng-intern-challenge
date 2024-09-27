import sys
lengthOfBinary = 6

##dictonary containing the letters and their coresponding braille
brailleDictLetters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', 
    'cap': '.....O', 'num': '.O.OOO', 'dec':'.0...0'
}

##dictonary containing the numbers and their coresponding braille
brailleDictNum = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..', '.':'..00.0', ',':'..0...', '?':'..0.00', '!':'..000.', ':':'..0.0.', ':':'..0.0.', 
    '-':'....00', '/':'.0..0.', '<':'.00..0', '>':'0..00.', '(':'0.0..0', ')':'.0.00.'
}

##dictonary containing braille and their corresponding letters (its repetitive, but it removes some icky code later on)
englishDictLetter = {v: k for k, v in brailleDictLetters.items()}
englishDictNum = {v: k for k, v in brailleDictNum.items()}

## String -> Bool
## Taking a given string, it will check if all the characters are either 0 or .
## If that and the string being of a length divisible by 6, it will return true.
## else false.
def isBraille(given):
    return all(c in 'O.' for c in given) and len(given) % lengthOfBinary == 0


## String -> String
## returns the english translation of a braille string
def brailleToEnglish(braille):
    english = []
    isNum = False
    isUpper = False
    index = 0
    while index < len(braille):
        brailleLetter = braille[index:index+6]
        if brailleLetter == brailleDictLetters["cap"]:
            index += lengthOfBinary
            brailleLetter = braille[index:index+lengthOfBinary]
            isUpper = True
        elif brailleLetter == brailleDictLetters["num"]:
            index += lengthOfBinary
            brailleLetter = braille[index:index+lengthOfBinary]
            isNum = True
        elif brailleLetter == brailleDictLetters[" "]:
            isNum = False

        if isNum:
            english.append(englishDictNum[brailleLetter])
        elif isUpper:
            english.append(englishDictLetter[brailleLetter].upper())
            isUpper = False
        else:
            english.append(englishDictLetter[brailleLetter])
        index += lengthOfBinary
    return ''.join(english)


## String -> String
## returns the braille translation of an english string
def englishToBraille(english):
    braille = []
    for letter in english:
        if letter.isdigit():
            braille.append(brailleDictLetters["num"])
            braille.append(brailleDictNum[letter])
        elif letter.isupper():
            braille.append(brailleDictLetters["cap"])
            braille.append(brailleDictLetters[letter.lower()])
        else:
            if letter in brailleDictLetters:
                braille.append(brailleDictLetters[letter]) 
            else:
                braille.append(brailleDictNum[letter])
    return ''.join(braille)

def main():
    given = ' '.join(sys.argv[1:])

    if isBraille(given):
        print(brailleToEnglish(given))
    else:
        print(englishToBraille(given))

if __name__ == "__main__":
    main()
