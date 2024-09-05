import sys
input = sys.argv

# create alpha to braille mapping
alphaToBraille = {
'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 'cap': '.....O',
'num': '.O.OOO', ' ': '......'}

keys = list(alphaToBraille.keys()) # used for mapping a-j to numbers

# reverse dictionary
brailleToAlpha = {}
for key in alphaToBraille:
    value = {alphaToBraille[key]: key}
    brailleToAlpha.update(value)

def processBraille():
    if (len(input) != 2):
        return False
    
    potentialBraille = input[1]
    # break up input after every 6th character
    splits = [potentialBraille[i:i+6] for i in range(0, len(potentialBraille), 6)]
    translation = ""
    follows = "low" # denotes whether caps follows, or number follows (low means lowercase)
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
                continue

            if (follows == "low"):
                translation += value
            elif (follows == "cap"):
                translation += value.upper()
                follows = "low" # reset
            elif (follows == "num"):
                # map from a-j to # is just their index + 1
                value = keys.index(value) + 1
                if (value == 10):
                    value = 0 # special case
                value = str(value)
                translation += value;
        except:
            # not Braille!
            return False
    return translation

def processEnglish():
    # loop through all commmand args
    translation = ""
    numFollows = False
    for i in range(1, len(input), 1):
        if (i != 1):
            # put a space
            translation += alphaToBraille[' ']
            numFollows = False # reset
        word = input[i]
        for j in range(0, len(word), 1):
            char = word[j]
            if (char.isnumeric()):
                # num follows
                if (numFollows == False):
                    translation += alphaToBraille['num']
                    numFollows = True
                # map 0-9 to a-j by indexing the keys list               
                translation += alphaToBraille[keys[int(char) - 1]]
            elif (char.isupper()):
                # cap follows
                translation += alphaToBraille['cap']
                translation += alphaToBraille[char.lower()]
            else:
                translation += alphaToBraille[char]
    return translation

# assume input is braille
brailleOut = processBraille()
if processBraille() == False:
    # not Braille, so translate from English to Braille
    print(processEnglish())
else:
    print(brailleOut)