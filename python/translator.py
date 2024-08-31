import sys


## Do we create more tests?
## Unsure if we can honestly, I don't want to mess up the automation.
## I would definitely make tests though for each individual key value pair in the dictionary and make sure
## englishToBraille = brailleToEnglish 
## Would check empty string
## would check complex cases, ie. capital, decimal, decimal and capital?, decimal and number?, etc.
## also want to check if special characters ie. ! work
## explicitly check dups? > vs O?
## How do we handle errors? Should we notify the recipient ie. ? vs skipping with space?? if its not found in our dict
## should we have error handling? 



## create a brailledict, we are given this configuration from the setup
## note maybe there is a way we can manually create this configuration? such that it is extensible for future character additions
## im thinking something along the line of using the matrix representation of the braille itself, ie. an actual 3x2 matrix
## potentially deriving some formula from the ASCII value to generating that matrix, but unsure about the specifics
## also as an engineer, I know its not in the scope of this question but how would we extend this in the future?
## do we add ability to do math in braille ie. see https://www.researchgate.net/publication/316146600_Conversion_of_2D_Mathematical_Equation_to_Linear_Form_for_Transliterating_into_Braille_An_aid_for_Visually_Impaired_People
## do we do something else? If so, for every new operation do we need to have something added in the braille dict or is there some better way to approach this
## not sure right now, but definitely something to think about


## Also another consideration is do we implement the entire thing or only the requirements?
## Some interesting ideas come into play when using special characters, the decimal operator (not making num char = false)
## also ">" has the same symbol as o
## Also note we chose to save the english keys as lower case, simply because those are most common I believe we'd have to call
## tolower more than toupper if the keys were instead uppercase letters
englishToBrailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'numberChar': '.O.OOO',
    # 'decimalFollows': '.O...O', '.': '..OO.O', ',': '..O...',
    # '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-' : '....OO' ,'/': '.O..O.',
    # '<': '.OO..O', '(': 'O.O..O', ')': '.O.OO.'
}

## do this as it ensures changes are reflected between both dicts, rather than editing one and then the other
brailleToEnglishDict = {v: k for k, v in englishToBrailleDict.items()}
## I don't believe this would be significantly different from manually defining the brailleToEnglish considering
## the time complexity is the same (we also have constant elements in dictionary so effectively O(1))

## In case our boolean numberChar = True, we must have a way to translate the number to the appropriate braille
## for example how do we get from 123 to braille?
## well we first have to see what letter 1 corresponds to, then we can use that in the englishToBrailleDict
numberToLetterDict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}
letterToNumberDict = {v: k for k, v in numberToLetterDict.items()}

def englishToBraille(text):
    braille = []
    numberChar = False
    for char in text:
        if char.isupper():
            braille.append(englishToBrailleDict['capital'])
            char = char.lower()
        if char.isdigit():
            ## other consideration, if it was in tech requirements
            ## if it is already in numbermode and we see a dot that means a decimal?
            if not numberChar:
                braille.append(englishToBrailleDict['numberChar'])
                numberChar = True
            braille.append(englishToBrailleDict[numberToLetterDict[char]])
        else:
            # if numberChar and char == ".":
            #     braille.append(englishToBrailleDict['decimalFollows'])
            #     braille.append(englishToBrailleDict['.'])
            # else:
            numberChar = False
                ## if we can't find the char make it space/skip?
            braille.append(englishToBrailleDict.get(char, '......'))
    return ''.join(braille)


def brailleToEnglish(brailleText):
    english = []
    i = 0
    numberChar = False
    while i < len(brailleText):
        symbol = brailleText[i:i+6]
        if symbol == englishToBrailleDict['capital']:
            ## Also unique behavior here, if we encounter a capital we can have a letter interspaced between numbers
            ## We could just introduce a letterInNumber value and append it if numberChar is ever true and there is no space?
            ## We could even append a second numberChar which ends the numberChar spree whenever we encounter a non english numberChar
            ## But again, not necessarily in the constraints of the question in fact it might even cause unit tests to fail
            ## IF we have extra number char symbols in the 
            i += 6
            symbol = brailleText[i:i+6]
            english.append(brailleToEnglishDict.get(symbol, '?').upper())
        elif symbol == englishToBrailleDict['numberChar']:
            numberChar = True
            i += 6
            symbol = brailleText[i:i+6]
            english.append(letterToNumberDict[(brailleToEnglishDict[symbol])])
        elif symbol == englishToBrailleDict[' ']:
            english.append(' ')
            numberChar = False
        else:
            ### PROBLEM HERE IS THE INPUT ONLY ALLOWS FOR NUMBER CHAR TO BE RESET AFTER A SPACE, WE CAN ALSO RESET IT UPON SEEING SOMETHING NOT IN the letter to number dict
            ## However its difficult to determine for letters like a if thats a number or a letter, lets just keep default funtionality for now
            ## but keep that in mind
            if numberChar:
                english.append(letterToNumberDict.get((brailleToEnglishDict[symbol]), '?'))
            else: 
                english.append(brailleToEnglishDict.get(symbol, '?'))
        i += 6
    return ''.join(english)


def isBraille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        return
    
    text = ' '.join(sys.argv[1:])
    ## ERROR CHECKING, but not sure if allowed? or needed
    # for char in text:
    #     cur = char
    #     if char.isupper():
    #         cur = char.lower()
    #     if cur not in englishToBrailleDict and cur not in numberToLetterDict and cur != '.':
    #         print("ERROR, program only supports characters from a-z (upper and lower), and numbers 0-9, as well as spaces unknown value in input")
    #         return
        
    ## Take first entry after command
    

    if isBraille(text):
        print(brailleToEnglish(text))
    else:
        print(englishToBraille(text))

if __name__ == '__main__':
    main()

