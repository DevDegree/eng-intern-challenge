import brailleToEnglishMap, englishToBrailleMap
import sys

CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

def brailleToEnglish(message):
    res = ""
    capitalizeNext = False
    isNumber = False


    for i in range(0, len(message), 6):
        c = ""

        # get the braille character
        for j in range(0, 6):
            c += message[i + j]

        if c == CAPITAL:
            capitalizeNext = True

        elif c == NUMBER:
            isNumber = True

        elif c == SPACE:
            res += " "
            isNumber = False

        else: # either letter or number
            if capitalizeNext:
                res += (brailleToEnglishMap.letters[c]).upper()
                capitalizeNext = False
            
            elif isNumber:
                res += brailleToEnglishMap.numbers[c]

            else:
                res += brailleToEnglishMap.letters[c]

    return res

def englishToBraille(message):
    res = ""
    isFirstDigit = True

    for c in message:
        if c.isdigit() and isFirstDigit: # first number in string of digit(s)
            res += NUMBER
            res += englishToBrailleMap.numbers[c]
            isFirstDigit = False
        
        elif c.isdigit():
            res += englishToBrailleMap.numbers[c]

        elif c.isalpha() and c.isupper():
            res += CAPITAL
            res += englishToBrailleMap.letters[c.lower()]

        elif c.isalpha():
            res += englishToBrailleMap.letters[c]

        else:
            res += SPACE
            isFirstDigit = True
        
    return res

def main():
    message = ' '.join(sys.argv[1:])

    # check whether the message is in braille or english
    isBraille = True if all(c in ".O" for c in message) else False

    if isBraille:
        print(brailleToEnglish(message))
    else:
        print(englishToBraille(message))

if __name__ == "__main__":
    main()