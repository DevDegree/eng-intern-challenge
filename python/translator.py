import sys

## create a braille_dict, we are given this configuration from the setup
## note maybe there is a way we can manually create this configuration? such that it is extensible for future character additions
## im thinking something along the line of using the matrix representation of the braille itself, ie. an actual 3x2 matrix
## potentially deriving some formula from the ASCII value to generating that matrix, but unsure about the specifics
## also as an engineer, I know its not in the scope of this question but how would we extend this in the future?
## do we add ability to do math in braille ie. see https://www.researchgate.net/publication/316146600_Conversion_of_2D_Mathematical_Equation_to_Linear_Form_for_Transliterating_into_Braille_An_aid_for_Visually_Impaired_People
## do we do something else? If so, for every new operation do we need to have something added in the braille dict or is there some better way to approach this
## not sure right now, but definitely something to think about


## Also another consideration is do we 
englishToBrailleDict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'numberChar': '.O.OOO',
    'decimalFollows': '.O...O', '.': '..OO.O'
}

## do this as it ensures changes are reflected between both dicts, rather than editing one and then the other
brailleToEnglishDict = {v: k for k, v in englishToBrailleDict.items()}
## I don't believe this would be significantly different from manually defining the reverse_braille_dict considering
## the time complexity is the same (we also have constant elements in dictionary so effectively O(1))

## In case our boolean numberChar = True, we must have a way to translate the number to the appropriate braille
## for example how do we get from 123 to braille?
## well we first have to see what letter 1 corresponds to, then we can use that in the englishToBrailleDict
numberToLetterDict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j', '.': '.'}
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
            if numberChar and char == ".":
                braille.append(englishToBrailleDict['decimalFollows'])
                braille.append(englishToBrailleDict['.'])
            else:
                numberChar = False
                ## if we can't find the char make it space/skip?
                braille.append(englishToBrailleDict.get(char, '......'))
    return ''.join(braille)


def braille_to_english(braille_text):
    english = []
    i = 0
    while i < len(braille_text):
        ## we are guaranteed that braille characters will be read in windows of 6
        ## ie. 0:6 since it doesn't include the last ie, [0:6] = first 6 letters indexes 0->5
        symbol = braille_text[i:i+6]
        if symbol == englishToBrailleDict['capital']:
            i += 6
            symbol = braille_text[i:i+6]
            english.append(brailleToEnglishDict[symbol].upper())
        elif symbol == englishToBrailleDict['numberChar']:
            i += 6
            while i < len(braille_text) and braille_text[i:i+6] in brailleToEnglishDict:
                symbol = braille_text[i:i+6]
                if brailleToEnglishDict[symbol] == 'decimalFollows':
                    i+= 12
                    english.append('.')
                else:
                    english.append(letterToNumberDict[brailleToEnglishDict[symbol]])
                    i += 6
            continue
        else:
            english.append(brailleToEnglishDict.get(symbol, '?'))
        i += 6
    return ''.join(english)

def is_braille(text):
    return all(char in 'O.' for char in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    text = ' '.join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(englishToBraille(text))

if __name__ == '__main__':
    main()

