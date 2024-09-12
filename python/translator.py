import sys


message = sys.argv[1]

char_to_braile = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......'

}

numbers_to_braile = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}


braile_to_char = {value: key for key, value in char_to_braile.items()}
braile_to_numbers = {value: key for key, value in numbers_to_braile.items()}
unique = ['O', '.']


def braile_text(message: str) -> None:
    '''
    Translates english input into braile text.
    '''
    translated = ''
    numeric = False
    for i in range(len(message)):
        if message[i].isupper() and numeric == False:
            translated = translated + '.....O' + char_to_braile[message[i].lower()]
        if message[i].isnumeric() and numeric == False:
            translated = translated + '.O.OOO'
            numeric = True
        if numeric == True:
            translated = translated + char_to_braile[message[i]]
        if message[i] == ' ':
            numeric == False
            translated = translated + char_to_braile[message[i]]
        
        if message[i].islower() and numeric == False:
            translated = translated + char_to_braile[message[i]]
    print(translated)


def text_braile(message: str) -> None:
    '''
    Translates braile input from the command line into english text
    '''
    isCap = False
    isNum = False
    result = ''
    count = 0
    
    while count < len(message):
        if message[count: count + 6] == '.....O':
            isCap = True
        
        elif message[count: count + 6] == '.O.OOO':
            isNum = True
        
        else:
            if not isCap and isNum:
                result = result + braile_to_numbers[message[count: count + 6]]
            elif isCap and not isNum:
                result = result + braile_to_char[message[count: count + 6]].upper()
                isCap = False
            elif not isCap and not isNum:
                result = result + braile_to_char[message[count: count + 6]]
    
        count = count + 6
    print(result)


#Check to see if the input is in braile or english
for i in range(len(message)):
    if message[i] not in unique:
        braile_text(message)

text_braile(message)
