
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
def receiveMessage() :

    message = str(input(""))
    
    if isMessageBraille(message) :
        translateFromBraille(message)
    else : 
        translateToBraille(message)

# Checks if message is Braille or not
def isMessageBraille(msg) :
    return set(msg).issubset({'.', 'O'})

# Function to translate a message from Braille
def translateFromBraille(msg):
    translation = []
    i = 0
    upper_mode = False
    number_mode = False
    decimal_mode = False

    for i in range(0, len(msg), 6) :
        currentMsg = ''

        if not number_mode and not decimal_mode or msg[i:i+6] == '......':
            currentMsg = brailDict[msg[i:i+6]]

        if currentMsg == 'space' :
            translation.append(' ')
            number_mode = False
        
        elif currentMsg == 'number' :
            number_mode = True
            continue
        
        elif currentMsg == 'decimal' :
            decimal_mode = True
            continue

        elif currentMsg == 'upper' :
            upper_mode = True
            continue

        else : 
            if number_mode :
                translation.append(numberDict[msg[i:i+6]])

            elif decimal_mode :
                translation.append(decimals[msg[i:i+6]])
                decimal_mode = False

            elif upper_mode :
                translation.append(currentMsg.upper())
                upper_mode = False

            else :
                translation.append(currentMsg)

        decimal_mode = False

    print(''.join(translation))

# Translates from keys to braille
def translateToBraille(msg) :
    swappedBrail = dict((v,k) for k,v in brailDict.items())
    swappedDecimals = dict((v,k) for k,v in decimals.items())
    swappedNumbers = dict((v,k) for k,v in numberDict.items())

    translation = []
    lastIsNum = False

    for char in msg :
        

        if char.isupper() :
            if char.lower() in swappedBrail :
                translation.append(swappedBrail['upper'])
                translation.append(swappedBrail[char.lower()])
        
        elif char in swappedBrail :
            translation.append(swappedBrail[char])

        elif char in swappedDecimals :
            translation.append(swappedBrail['decimal'])
            translation.append(swappedDecimals[char])

        elif char in swappedNumbers :
            if not lastIsNum :
                translation.append(swappedBrail['number'])
                lastIsNum = True
            translation.append(swappedNumbers[char])
        
        elif char == ' ' :
            translation.append(swappedBrail['space'])
            lastIsNum = False
        
    print(''.join(translation))
    
receiveMessage()