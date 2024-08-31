'''
Shopify Engineering Internship (Winter 2025) - Braille Translator Submission
Prasanna Thallapalli
August 31st, 2024
'''

import sys

#Constants
englishToBrailleAlpha = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
}

numToBraille = {
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

brailleToEngAlpha = {v: k for k, v in englishToBrailleAlpha.items()} #Reversed dictionary of Braille as keys and English as values

brailleToNum = {v: k for k, v in numToBraille.items()} #Reversed dictionary of Braille as keys and English as values

#Special Braille characters to indicate a capitalized character, number and space
capitalFollows = ".....O"
numFollows = ".O.OOO"
space = "......"


def isBraille(text):
    '''
    Purpose: determines whether the given text string is Braille or not

    Input: text (str) representing the command line argument to be translated
    
    Output: returns true if text is Braille and false if it's English
    '''
    if (len(text) % 6 != 0): return False
    
    for c in text:
        if c != "O" and c != ".":
            return False
    return True


def brailleToEnglish(text):
    '''
    Purpose: translates Braille text to English text

    Input: text (str) representing a sequence of Braille symbols

    Output: prints the English translation of the input text
    '''
    
    capital = False #Tracks if a capital follows symbol was seen
    number = False #Tracks if a number follows symbol was seen
    tokenizedInput = [text[i:i+6] for i in range(0, len(text), 6)] #Breaks up the input into tokens of 6 characters for each Braille symbol
    output = ""

    for i in tokenizedInput:
        #capital and number follows checks
        if i == capitalFollows:
            capital = True
        elif i == numFollows:
            number = True
        #numeric case
        elif i in brailleToNum and number:
            output += brailleToNum[i]
            capital = False
        #character case
        elif i in brailleToEngAlpha:
            if capital:
                output += (brailleToEngAlpha[i]).upper()
                capital = False
            else:
                output += brailleToEngAlpha[i]
        #space case
        else:
            output += " "
            number = False
    
    print(output)


def englishToBraille(text):
    '''
    Purpose: translates English text to Braille symbols

    Input: text (str) representing a sequence of English characters

    Output: prints the Braille translation of the input text
    '''

    output = ""
    currNum = False #Tracks if the current characters are numbers

    for c in text:
        #numeric case
        if c.isnumeric():
            if not currNum:
                output += numFollows
                currNum = True
            output += numToBraille[c]
        #character cases (upper and lower)
        elif c.isupper():
            output += capitalFollows
            output += englishToBrailleAlpha[c.lower()]
            currNum = False
        elif c in englishToBrailleAlpha:
            output += englishToBrailleAlpha[c]
            currNum = False
        #space case
        else:
            output += space
            currNum = False

    print(output)


def main():
    inputStr = " ".join(sys.argv[1:]) #join all command line arguments by a single space

    if isBraille(inputStr): #directs which translation function should be called based on if the input is in Braille or English
        return brailleToEnglish(inputStr)
    return englishToBraille(inputStr)

if __name__ == "__main__":
    main()
