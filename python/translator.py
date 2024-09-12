
#converts braille to english
def brailleToEnglish(string):
    return 0

#converts english to braille
def englishToBraille(string):
    return 0

#checks if inputted string is already braille or not
def isBraille(string):
    for i in range(len(string)):
        if string[i] != "." and string[i] != "O":
            return 0
    return 1

text = input("String: ")
print(text)
x = isBraille(text[0:9])
