import sys

# Dictionnaries for translation
brailDict = { 
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '.....O': 'upper', '.O...O': 'decimal', '.O.OOO': 'number',
    '......': 'space',
}

decimals = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
}

numberDict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0',
}

# In charge of receiving a string from the user
def receiveMessage():
    # Join the command-line arguments into a single string, with spaces between them
    message = ' '.join(sys.argv[1:])
    
    if isMessageBraille(message):
        return translateFromBraille(message)
    else:
        return translateToBraille(message)


# Checks if message is Braille or not
def isMessageBraille(msg) :
    return set(msg).issubset({'.', 'O'})

# Function to translate a message from Braille
def translateFromBraille(msg):
    # Translation array + iteration counter
    translation = []
    i = 0

    # Flags necessary for traduction
    upper_mode = False
    number_mode = False
    decimal_mode = False

    # Checking every strings in an interval of 6
    for i in range(0, len(msg), 6) :
        currentMsg = ''

        # If not a number or decimal, we translate it
        if not number_mode and not decimal_mode or msg[i:i+6] == '......':
            currentMsg = brailDict[msg[i:i+6]]

        # If space, we append space and end number mode if it was active
        if currentMsg == 'space' :
            translation.append(' ')
            number_mode = False
        
        # If number mode, we turn on the flag and continue
        elif currentMsg == 'number' :
            number_mode = True
            continue
        
        # If decimal mode, we turn on the flag and continue
        elif currentMsg == 'decimal' :
            decimal_mode = True
            continue

        # If upper mode, we turn on the flag and continue
        elif currentMsg == 'upper' :
            upper_mode = True
            continue
        
        else : 
            # If number, we append from number dict
            if number_mode :
                translation.append(numberDict[msg[i:i+6]])

            # If decimal, we append from decimal dict then turn off flag
            elif decimal_mode :
                translation.append(decimals[msg[i:i+6]])
                decimal_mode = False

            # If upper, we make string upper then add it then turn off flag
            elif upper_mode :
                translation.append(currentMsg.upper())
                upper_mode = False

            # Else, we just add the message
            else :
                translation.append(currentMsg)

        decimal_mode = False

    # Join the array into a string then return it
    translated = ''.join(translation)
    print(translated)


# Translates from keys to braille
def translateToBraille(msg) :
    # We swap the dicts for easier translation
    swappedBrail = dict((v,k) for k,v in brailDict.items())
    swappedDecimals = dict((v,k) for k,v in decimals.items())
    swappedNumbers = dict((v,k) for k,v in numberDict.items())

    translation = []
    lastIsNum = False

    for char in msg :
        # If char isupper, it is a letter, so we add the flag, then the lowercase letter
        if char.isupper() :
            if char.lower() in swappedBrail :
                translation.append(swappedBrail['upper'])
                translation.append(swappedBrail[char.lower()])
        
        # If the char is in an english character, we add it to the translation
        elif char in swappedBrail :
            translation.append(swappedBrail[char])

        # If the char is a decimal, we add the decimal tag, then the decimal
        elif char in swappedDecimals :
            translation.append(swappedBrail['decimal'])
            translation.append(swappedDecimals[char])

        # If the char is a number, we add the number tag, then the number
        elif char in swappedNumbers :
            if not lastIsNum :
                translation.append(swappedBrail['number'])
                lastIsNum = True
            translation.append(swappedNumbers[char])
        
        # We add the space tag if its a space
        elif char == ' ' :
            translation.append(swappedBrail['space'])
            lastIsNum = False
    
    # Join the array into a string then return it
    translated = ''.join(translation)
    print(translated)

# Run the message receiver
if __name__ == "__main__":
    receiveMessage()