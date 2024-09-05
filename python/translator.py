import sys

# This program ASSUMES valid, well-formed input
def main():
    # We first create our dictionaries to map between English and Braille
    englishToBrailleDict = {}

    # Alpha-numerics
    englishToBrailleDict['1'] = 'O.....'
    englishToBrailleDict['2'] = 'O.O...'
    englishToBrailleDict['3'] = 'OO....'
    englishToBrailleDict['4'] = 'OO.O..'
    englishToBrailleDict['5'] = 'O..O..'
    englishToBrailleDict['6'] = 'OOO...'
    englishToBrailleDict['7'] = 'OOOO..'
    englishToBrailleDict['8'] = 'O.OO..'
    englishToBrailleDict['9'] = '.OO...'
    englishToBrailleDict['0'] = '.OOO..'

    englishToBrailleDict['a'] = "O....."
    englishToBrailleDict['b'] = 'O.O...'
    englishToBrailleDict['c'] = 'OO....'
    englishToBrailleDict['d'] = 'OO.O..'
    englishToBrailleDict['e'] = 'O..O..'
    englishToBrailleDict['f'] = 'OOO...'
    englishToBrailleDict['g'] = 'OOOO..'
    englishToBrailleDict['h'] = 'O.OO..'
    englishToBrailleDict['i'] = '.OO...'
    englishToBrailleDict['j'] = '.OOO..'
    englishToBrailleDict['k'] = 'O...O.'
    englishToBrailleDict['l'] = 'O.O.O.'
    englishToBrailleDict['m'] = 'OO..O.'
    englishToBrailleDict['n'] = 'OO.OO.'
    englishToBrailleDict['o'] = 'O..OO.'
    englishToBrailleDict['p'] = 'OOO.O.'
    englishToBrailleDict['q'] = 'OOOOO.'
    englishToBrailleDict['r'] = 'O.OOO.'
    englishToBrailleDict['s'] = '.OO.O.'
    englishToBrailleDict['t'] = '.OOOO.'
    englishToBrailleDict['u'] = 'O...OO'
    englishToBrailleDict['v'] = 'O.O.OO'
    englishToBrailleDict['w'] = '.OOO.O'
    englishToBrailleDict['x'] = 'OO..OO'
    englishToBrailleDict['y'] = 'OO.OOO'
    englishToBrailleDict['z'] = 'O..OOO'
    
    # Capital follows mapped as C
    englishToBrailleDict['C'] = '.....O'
    # Number follows mapped as N
    englishToBrailleDict['N'] = '.O.OOO'

    # Symbols
    englishToBrailleDict[' '] = '......'

    brailleToEnglishDict = dict((v, k) for k, v in englishToBrailleDict.items())

    # Since digits and chars can map to the same braille string, 
    # we need a separate dict for them.
    brailleToDigitsDict = {}
    brailleToDigitsDict['O.....'] = '1'
    brailleToDigitsDict['O.O...'] = '2'
    brailleToDigitsDict['OO....'] = '3'
    brailleToDigitsDict['OO.O..'] = '4'
    brailleToDigitsDict['O..O..'] = '5'
    brailleToDigitsDict['OOO...'] = '6'
    brailleToDigitsDict['OOOO..'] = '7'
    brailleToDigitsDict['O.OO..'] = '8'
    brailleToDigitsDict['.OO...'] = '9'
    brailleToDigitsDict['.OOO..'] = '0'

    # Get string to translate from cmd line arguments
    strToTranslate = ""

    for i in range(1, len(sys.argv)):
        strToTranslate += sys.argv[i]

        # Since each cmd-line argument implicitly has a space between it we need to add that into our string
        if i < len(sys.argv) - 1:
            strToTranslate += ' '

    # Determine if braille or english. There exists no braille words in our dictionary
    # which contain all O's. So try and read the first 6 chars in our strToTranslate. If a '.' is
    # found we know this letter in not in our english alphabet and thus we are in braille.
    # If there are less than 6 chars we must be in English.
    isEnglish = True

    if len(strToTranslate) >= 6:
        for i in range(0, 6):
            if strToTranslate[i] == '.':
                isEnglish = False
                break
    
    # Convert
    translatedStr = ""

    if isEnglish:
        i = 0
        while i < len(strToTranslate):
            # If char is a number run a while loop to keep feeding in numbers until space is reached or end of str
            if strToTranslate[i].isdigit():
                translatedStr += englishToBrailleDict['N']

                while i < len(strToTranslate) and strToTranslate[i].isdigit():
                    translatedStr += englishToBrailleDict[strToTranslate[i]]
                    i += 1

                continue
            
            # If char is capital add the capital symbol then the char tolower
            if strToTranslate[i].isupper():
                translatedStr += englishToBrailleDict['C']

            translatedStr += englishToBrailleDict[strToTranslate[i].lower()]
            i += 1
    else:
        i = 0
        while i < len(strToTranslate):
            brailleChar = strToTranslate[i:i+6]

            # If the char is numeric, read said number until EOF or a space is reached
            if brailleToEnglishDict[brailleChar] == 'N':
                i += 6
                brailleChar = strToTranslate[i:i+6]

                while i < len(strToTranslate) and brailleToEnglishDict[brailleChar] != ' ':
                    translatedStr += brailleToDigitsDict[brailleChar]
                    i += 6
                    brailleChar = strToTranslate[i:i+6]
                
                continue

            # Check if the alpha char is capital or not
            if brailleToEnglishDict[brailleChar] == 'C':
                i += 6
                brailleChar = strToTranslate[i:i+6]
                translatedStr += brailleToEnglishDict[brailleChar].upper()
            else:
                translatedStr += brailleToEnglishDict[brailleChar]

            i += 6

    # Output translated str
    print(translatedStr, end="")
    return

if __name__ == "__main__":
    main()
