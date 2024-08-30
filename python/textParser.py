from constants import alphaToBraile, numberToBraile
class TextParser:
    def __init__(self, string):
        self.string = string

    def textToBraile(self):
        stringBuilder = ""
        i = 0
        while i < len(self.string):
            ch  = self.string[i]
            if ch.isalpha():
                if ch.isupper():
                    stringBuilder += alphaToBraile['CAP']
                stringBuilder += alphaToBraile[ch.lower()]
            elif ch == " ":
                stringBuilder += alphaToBraile[" "]
            else:
                if ch.isnumeric():
                    stringBuilder += alphaToBraile['NUM']
                while i < len(self.string) and self.string[i].isnumeric():
                    stringBuilder += numberToBraile[self.string[i]]
                    i += 1
                i -= 1
            i += 1
        return stringBuilder