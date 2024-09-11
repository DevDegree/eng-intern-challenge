# Class translator
# Supports Braille and English
# Expand the dictionaries to support more languages
class translator:


    # Braille to English dictionary
    brailToEnglishDict = {
        "O....." : 'a',
        "O.O..." : 'b',
        "OO...." : 'c',
        "OO.O.." : 'd',
        "O..O.." : 'e',
        "OOO..." : 'f',
        "OOOO.." : 'g',
        "O.OO.." : 'h',
        ".OO..." : 'i',
        ".OOO.." : 'j',
        "O...O." : 'k',
        "O.O.O." : 'l',
        "OO..O." : 'm',
        "OO.OO." : 'n',
        "O..OO." : 'o',
        "OOO.O." : 'p',
        "OOOOO." : 'q',
        "O.OOO." : 'r',
        ".OO.O." : 's',
        ".OOOO." : 't',
        "O...OO" : 'u',
        "O.O.OO" : 'v',
        ".OOO.O" : 'w',
        "OO..OO" : 'x',
        "OO.OOO" : 'y',
        "O..OOO" : 'z',
        ".....O" : "capitalFollows",
        ".O...O" : "decimalFollows",
        ".O.OOO" : "numberFollows",
        "..OO.O" : ".",
        "..O..." : ",",
        "..O.OO" : "?",
        "..OOO." : "!",
        "..OO.." : ":",
        "..O.O." : ";",
        "....OO" : "-",
        ".O..O." : "/",
        "O.O..O" : "(",
        ".O.OO." : ")",
        "......" : " ",
    }
    
    #English to Braille dictionary
    englishTobrailDict = {
    }

    def __init__(self, bIsCaptial, bIsNumber, sTranslateTo):
        # determines if the previus word was the capital sign or not
        self.bIsCapital = False 
        
        # determines if the number is activated or not
        self.bIsNumber = False

        # determines the type of the input text
        self.sTranlateTo = "Braille"

        for entry in self.brailToEnglishDict:
            self.englishTobrailDict[self.brailToEnglishDict[entry]] = entry
    
    # determines if a text is English or Braille
    # updates sTranslateTo accordingly
    def __determineTextType(self, sText):
        if (len(sText) % 6 != 0):
            self.sTranlateTo = "Braille"
            return
        for c in sText:
            if (c != '.' and c != 'O'):
                self.sTranlateTo = "Braille"
                return
        self.sTranlateTo = "English"
    
    # translates the English text to the Braille text
    # returns the result as a string
    def __translateEnglishToBraille(self, sText):
        sresult = ""
        for c in sText:

            # deal with the upperCase letters
            if (c.isupper()):
                c = c.lower()
                sresult = sresult + self.englishTobrailDict["capitalFollows"]
                sresult = sresult + self.englishTobrailDict[c]
                continue

            # deal with the digits
            if (c.isdigit()):

                # only the first time a number appears we must use the numberFollows letter
                if (self.bIsNumber == False):
                    sresult = sresult + self.englishTobrailDict["numberFollows"]
                    self.bIsNumber = True

                # in the alphabet 0 is equal to j which is the 10th letter
                if (c == '0'):
                    c = 10
                else:
                    c = int(c) - 1
                sresult = sresult + self.englishTobrailDict[chr(ord('a') + c)]
                continue

            # deal with spaces
            if (c == " "):
                self.bIsNumber = False
                sresult = sresult + self.englishTobrailDict[" "]
                continue
            
            # all other cases are the default case
            try:
                sresult = sresult + self.englishTobrailDict[c]
            except:
                return "Undefined English Text, please check your input"
        return sresult
    
    # translates the Braille text to English text
    # returns the results as a string
    def __translateBrailleToEnglish(self, sText):
        
        # keep track of brail letters
        lsBrailleLetters = [] 
        sletter = ""
        
        # split the brail text into letters
        for c in sText:
            sletter = sletter + c
            if (len(sletter) == 6):
                lsBrailleLetters.append(sletter)
                sletter = ""
        
        # start the main translation
        result = ""
        for brail in lsBrailleLetters:
            try:
                sBrailleLetter = self.brailToEnglishDict[brail]
            except:
                return "Undefined Braille Text, please check your input"
            
            # deal with space
            # reset the number bool
            # reset the capital bool
            if (sBrailleLetter == " "):
                self.bIsCapital = False
                self.bIsNumber = False
                result = result + " "
                continue
            
            # next letter will be capital
            if (sBrailleLetter == "capitalFollows"):
                self.bIsCapital = True
                continue
            
            # from now to the next space will be numbers following
            if (sBrailleLetter == "numberFollows"):
                self.bIsNumber = True
                continue
            
            # the current letter is a digit
            if (self.bIsNumber):
                sBrailleLetter = ord(sBrailleLetter) - ord('a') + 1
                sBrailleLetter = sBrailleLetter % 10
                result = result + str(sBrailleLetter)
                continue

            # the current letter must be capitalize
            if (self.bIsCapital):
                sBrailleLetter = sBrailleLetter.upper()
                result = result + sBrailleLetter
                self.bIsCapital = False
                continue
            result = result + sBrailleLetter
        return result
    
    def tranlateString(self, sText):
        # determine the input text type
        self.__determineTextType(sText)

        # translate the input accordingly
        if (self.sTranlateTo == "Braille"):
            result = self.__translateEnglishToBraille(sText)
        else:
            result = self.__translateBrailleToEnglish(sText)
        return result


