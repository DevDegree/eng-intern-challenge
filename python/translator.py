import sys
input = sys.argv

# create alpha to braille mapping
# no need for #s since we'll ascii map them to a-z
alphaToBraille = {
'a': 'o.....', 'b': 'o.o...', 'c': 'oo....', 'd': 'oo.o..', 'e': 'o..o..', 'f': 'ooo...', 'g': 'oooo..', 'h': 'o.oo..', 'i': '.oo...',
'j': '.ooo..', 'k': 'o...o.', 'l': 'o.o.o.', 'm': 'oo..o.', 'n': 'oo.oo.', 'o': 'o..oo.', 'p': 'ooo.o.', 'q': 'ooooo.', 'r': 'o.ooo.',
's': '.oo.o.', 't': '.oooo.', 'u': 'o...oo', 'v': 'o.o.oo', 'w': '.ooo.o', 'x': 'oo..oo', 'y': 'oo.ooo', 'z': 'o..ooo', 'cap': '.....o',
'dec': '.o...o', '#': '.o.ooo', '.': '..oo.o', ':': '..o...', '?': '..o.oo', '!': '..ooo.', ':': '..oo..', ';': '..o.o.', '-': '....oo',
'/': '.o..o.', '<': '.oo..o', '>': 'o..oo.', '(': 'o.o..o', ')': '.o.oo.', ' ': '......'}


# reverse dictionary
brailleToAlpha = {}
for key in alphaToBraille:
    value = {alphaToBraille[key]: key}
    brailleToAlpha.update(value)

"""
for i in range(1, len(input)):
    # do stuff
    print(input[i])
"""

def processBraille():
    if (len(input) <= 2):
        return False
    
    potentialBraille = input[1]
    # break up input after every 6th character
    splits = [potentialBraille[i:i+6] for i in range(0, len(potentialBraille, 6))]
    translation = ""
    follows = "low" # denotes whether caps follows, decimal follows, or number follows (low means lowercase)
    for i in range (0, len(splits), 1):
        try:
            value = brailleToAlpha[splits[i]]
            if value == "cap":
                follows = "cap"
            elif value == "dec":
                follows = "dec"
            elif value == "num"
        except:
            # not Braille!
            return False


def processEnglish():
    i = 1

# assume input is braille
brailleOut = processBraille()
if processBraille() == False:
    # not Braille, so translate from English to Braille
    print(processEnglish)
else:
    print(brailleOut)