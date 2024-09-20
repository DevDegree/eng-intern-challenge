from constants import brailleToAlpha, brailleToNumber

class BraileParser:
    def __init__(self, string):
        self.string = string

    def braileToText(self):
        stringBuilder = ""
        i = 0
        while i < len(self.string):
            brailleToken = self.string[i:i+6]
            if self.isCapital(brailleToken):
                i, stringBuilder = self.processCapital(i, stringBuilder)
            elif self.isNumber(brailleToken):
                i, stringBuilder = self.processNumber(i, stringBuilder)
            else:
                i, stringBuilder = self.processToken(i, stringBuilder)
        return stringBuilder

    def isCapital(self, brailleToken):
        return brailleToken == '.....O'
    
    def isNumber(self, brailleToken):
        return brailleToken == '.O.OOO'
    
    def processCapital(self, i, stringBuilder):
        i += 6
        if i < len(self.string):
            brailleToken = self.string[i:i+6]
            mappedString = brailleToAlpha[brailleToken].upper()
            stringBuilder = stringBuilder + mappedString
            i += 6
        return (i, stringBuilder)
    
    def processNumber(self, i, stringBuilder):
        i += 6
        while i < len(self.string):
            brailleToken = self.string[i:i+6]
            if brailleToken == "......":
                break
            mappedString = brailleToNumber[brailleToken]
            stringBuilder = stringBuilder + mappedString
            i += 6
        return (i, stringBuilder)
    
    def processToken(self, i, stringBuilder):
        if i < len(self.string):
            brailleToken = self.string[i:i+6]
            mappedString = brailleToAlpha[brailleToken]
            stringBuilder = stringBuilder + mappedString
            i += 6
        return (i, stringBuilder)



    @staticmethod
    def isBraileString(string):
        #check if the length of the string is a multiple of 6
        if len(string) % 6 != 0:
            return False
        
        if not BraileParser.onlyBraileLetters(string):
            return False
        
        #Check if each braile letter is an actual braile letter. 
        #You can make 2^6 = 64 combinations, but there are only 52 actual supported braile chars
        for i in range(0, len(string), 6):
            token = ""
            for j in range(i, i+6):
                token += string[j]
            if token not in brailleToAlpha: #numbers have the same braile
                print(token)
                return False
        return True
    
    #check if the string is only made of . and O
    @staticmethod
    def onlyBraileLetters(string):
        for letter in string:
            if letter not in ["O", "."]:
                return False
        return True
