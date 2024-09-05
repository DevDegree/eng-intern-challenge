import sys
input = sys.argv

# create alpha to braille mapping
# no need for #s since we'll ascii map them to a-z
alphaToBraille = {
'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'O': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 'cap': '.....O',
'dec': '.O...O', '#': '.O.OOO', '.': '..OO.O', ':': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO',
'/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'}


# reverse dictionary
brailleToAlpha = {}
for key in alphaToBraille:
    value = {alphaToBraille[key]: key} # lower to enforce no O
    brailleToAlpha.update(value)

"""
for i in range(1, len(input)):
    # do stuff
    print(input[i])
"""

def processBraille():
    if (len(input) != 2):
        return False
    
    potentialBraille = input[1]
    # break up input after every 6th character
    splits = [potentialBraille[i:i+6] for i in range(0, len(potentialBraille), 6)]
    translation = ""
    follows = "low" # denotes whether caps follows, decimal follows, or number follows (low means lowercase)
    for i in range (0, len(splits), 1):
        try:
            key = splits[i]
            value = brailleToAlpha[key]
            if (len(value) != 1):
                follows = value
                continue
            elif (value == ' '):
                translation += value
                follows = "low" # reset

            if (follows == "low"):
                translation += value
            elif (follows == "cap"):
                translation += value.upper()
            elif (follows == "dec"):
                value -= 'a'
                if (value == 'j' - 'a'):
                    value = '0'
                translation += value - 'a'
        except:
            # not Braille!
            return False
    return translation


def processEnglish():
    i = 1

# assume input is braille
brailleOut = processBraille()
if processBraille() == False:
    # not Braille, so translate from English to Braille
    print(1)
else:
    print(brailleOut)