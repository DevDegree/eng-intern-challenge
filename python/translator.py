
# 1. Determining if the input string is Braille or English
''' 
If we see only see 0s, we cannot tell if it is Braille or English. => If there exists a following character, it must be Braille 
    Otherwise, we can immediately determine if English or Braille.
'''
# 2a. If English, we convert to Braille via a Map
'''
- Look out for capitals, must be preceeded by special Braille
- Look out for numbers, [entire number] must be preceeded by a single special Braille. resets on space 
'''

# 2b. If Braille, convert to English via a Map
'''
AMBIGUOUS: OOOOOO => is this english or Braille?!?!?!?!?!?!?!?!?
'''


import sys

'''
We optimize for speed and time.
'''

class BrailleEnglishMap:
    
    isEnglishToBraille = True

    # storing as bitwise encoding
    translateMap = {
        '0': (0,1,1,1,0,0),
        '1': (1,0,0,0,0,0),
        '2': (1,0,1,0,0,0),
        '3': (1,1,0,0,0,0),
        '4': (1,1,0,1,0,0),
        '5': (1,0,0,1,0,0),
        '6': (1,1,1,0,0,0),
        '7': (1,1,1,1,0,0),
        '8': (1,0,1,1,0,0),
        '9': (0,1,1,0,0,0),
        'a': (1,0,0,0,0,0),
        'b': (1,0,1,0,0,0),
        'c': (1,1,0,0,0,0),
        'd': (1,1,0,1,0,0),
        'e': (1,0,0,1,0,0),
        'f': (1,1,1,0,0,0),
        'g': (1,1,1,1,0,0),
        'h': (1,0,1,1,0,0),
        'i': (0,1,1,0,0,0),
        'j': (0,1,1,1,0,0),
        'k': (1,0,0,0,1,0),
        'l': (1,0,1,0,1,0),
        'm': (1,1,0,0,1,0),
        'n': (1,1,0,1,1,0),
        'o': (1,0,0,1,1,0),
        'p': (1,1,1,0,1,0),
        'q': (1,1,1,1,1,0),
        'r': (1,0,1,1,1,0),
        's': (0,1,1,0,1,0),
        't': (0,1,1,1,1,0),
        'u': (1,0,0,0,1,1),
        'v': (1,0,1,0,1,1),
        'w': (0,1,1,1,0,1),
        'x': (1,1,0,0,1,1),
        'y': (1,1,0,1,1,1),
        'z': (1,0,0,1,1,1),
        ' ': (0,0,0,0,0,0),
        '>': (0,0,0,0,0,1), # represents cap follows 
        '<': (0,1,0,1,1,1)  # represent number follows
    }

    # flip only if necessary (potentially saves space)
    @staticmethod
    def flipMap():
        BrailleEnglishMap.translateMap = {v: k for k, v in BrailleEnglishMap.translateMap.items()}

    # prints Braille
    @staticmethod
    def printBraille(englishChar):
        brailleTuple = BrailleEnglishMap.translateMap[englishChar]
        for dot in brailleTuple:
            if dot == 1:
                print('O', end = '')
            else:
                print('.', end = '')

    # prints English
    def printEnglish(brailleTuple):
        engChar = BrailleEnglishMap.translateMap[brailleTuple]
        if (engChar == '<'):
            BrailleTranslator.numberFollows = True                    
        elif (engChar == '>'):
            BrailleTranslator.capitalFollows = True
        elif (engChar == ' '):
            BrailleTranslator.numberFollows = False
            BrailleTranslator.capitalFollows = False
            print(engChar, end = '')
        else: # some other non-special character
            if BrailleTranslator.numberFollows:
                if engChar >= 'a' and engChar <= 'i':
                    engChar = chr( ( ord(engChar) - ord('a') ) + ord('0') + 1)
                elif engChar == 'j':
                    engChar = '0'
            elif (BrailleTranslator.capitalFollows):
                engChar = chr( ord(engChar) - 32 )
            BrailleTranslator.capitalFollows = False
            print(engChar, end = '')


class BrailleTranslator:

    _BRAILLE_INTERVAL = 6

    numberFollows = False
    capitalFollows = False

    def __init__(self, passage):
        self.passage = passage
        # 1. more than word (presence of space), then not Braille
        # 2. If first letter in first word is not '.' ad not 'O', then automatically english 
        if len(passage) > 1 or (passage[0][0] != '.' and passage[0][0] != 'O'):
            BrailleEnglishMap.isEnglishToBraille = True
        # check first 6 chars, cannot be space since it is parsed out by argv, so must exist . if braille
        elif (not (len(passage[0])%6 == 0 and (passage[0][0] == '.' or passage[0][1] == '.' or passage[0][2] == '.' or 
                                             passage[0][3] == '.' or passage[0][4] == '.' or passage[0][5] == '.'))
            ):
            BrailleEnglishMap.isEnglishToBraille = True
        else:
            BrailleEnglishMap.isEnglishToBraille = False
            BrailleEnglishMap.flipMap()

    '''
    translateEnglishToBraille() changes the passage to Braille to English
        Side-Effects: Prints English result to Output
    '''
    def translateEnglishToBraille(self):
        wordIndex = 0
        while wordIndex < len(self.passage):
            word = self.passage[wordIndex]
            for letter in word:
                if letter >= 'A' and letter <= 'Z':
                    BrailleEnglishMap.printBraille('>')
                    letter = chr(ord(letter) - ord('A') + ord('a'))
                elif (not BrailleTranslator.numberFollows) and letter >= '0' and letter <= '9':
                    BrailleEnglishMap.printBraille('<')
                    BrailleTranslator.numberFollows = True
                elif letter == ' ':
                    BrailleTranslator.numberFollows = False    
                BrailleEnglishMap.printBraille(letter)

            if (wordIndex < len(self.passage) - 1):
                BrailleTranslator.numberFollows = False
                BrailleEnglishMap.printBraille(' ') # python takes as space separated args

            wordIndex += 1

    '''
    translateBrailleToEnglish() changes the passage to Braille to English
        Side-Effects: Prints English result to Output
    '''
    def translateBrailleToEnglish(self):
        for word in self.passage: # should only be a wingle word (Braille is not space separated)
            charIndex = 0
            while (charIndex < len(word)):
                brailleTuple = (1 if word[charIndex] == 'O' else 0, 
                                1 if word[charIndex+1] == 'O' else 0, 
                                1 if word[charIndex+2] == 'O' else 0, 
                                1 if word[charIndex+3] == 'O' else 0, 
                                1 if word[charIndex+4] == 'O' else 0, 
                                1 if word[charIndex+5] == 'O' else 0)
                BrailleEnglishMap.printEnglish(brailleTuple)

                charIndex += 6


    '''
    translate() changes the passage to from English to Braille or Braille to English
        Side-Effects: Prints result to Output
    '''
    def translate(self):
        if BrailleEnglishMap.isEnglishToBraille:
            self.translateEnglishToBraille()
        else:
            self.translateBrailleToEnglish()



def main(argv):
    brailleTranslator = BrailleTranslator(argv[1:])
    brailleTranslator.translate()



if __name__ == "__main__":
    main(sys.argv)