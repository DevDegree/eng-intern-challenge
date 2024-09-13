import sys

# braille translated to english
brailleToEnglish = {
    'O.....': 'a', 
    'O.O...': 'b', 
    'OO....': 'c', 
    'OO.O..': 'd', 
    'O..O..': 'e',
    'OOO...': 'f', 
    'OOOO..': 'g', 
    'O.OO..': 'h', 
    '.OO...': 'i', 
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l', 
    'OO..O.': 'm', 
    'OO.OO.': 'n', 
    'O..OO.': 'o',
    'OOO.O.': 'p', 
    'OOOOO.': 'q', 
    'O.OOO.': 'r', 
    '.OO.O.': 's', 
    '.OOOO.': 't',
    'O...OO': 'u', 
    'O.O.OO': 'v', 
    '.OOO.O': 'w', 
    'OO..OO': 'x', 
    'OO.OOO': 'y',
    'O..OOO': 'z', 
    '..OO.O': '.', 
    '..O...': ',', 
    '..O.OO': '?',
    '..OOO.': '!', 
    '..OO..': ':', 
    '..O.O.': ';', 
    '....OO': '-', 
    '.O..O.': '/', 
    '.OO..O': '<', 
    '.O.OO.': '>',
    'O.O..O': '(', 
    '.O.OO.': ')',
    '......': ' ',
    '.....O': 'Capital', 
    '.O.OOO': 'Number'
}

# english translated to braille; reverse of previous dictionary
englishToBraille = {value: key for key, value in brailleToEnglish.items()}

# numbers to braille
numsToBraille = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..',
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...',
    '0': '.OOO..'
}

# braille to numbers
brailleToNums = {value: key for key, value in numsToBraille.items()}

# function to convert english to braille
def toBraille(english):
    braille = []
    number = False

    
    for character in english:
        # if character is a valid character
        if character in englishToBraille:
            if number:
                number = False
            braille.append(englishToBraille.get(character, '......'))
        
        # if character is a digit
        elif character.isdigit():
            if not number:
                braille.append(englishToBraille['Number'])
                number = True

            braille.append(numsToBraille[character])
        
        # if character is a uppercase character
        elif character.isupper():
            braille.append(englishToBraille['Capital'])
            braille.append(englishToBraille.get(character.lower(), '......'))

        # unexpected characters
        else:
            braille.append('......') 

    res = ""

    for word in braille:
        res += word

    return res


# function to convert braille to english
def toEnglish(braille):
    english = []
    curr = 0
    capitalize = False
    number = False

    # loop through the whole braille phrase in groups of 6
    while curr < len(braille):
        symbol = braille[curr:curr + 6]

        # Capitalize
        if symbol == '.....O':
            capitalize = True
            curr += 6
            continue

        # Number
        elif symbol == '.O.OOO':
            number = True
            curr += 6
            continue
        
        if number:
            character = brailleToNums.get(symbol, '?')
            number = False
        else:
            character = brailleToEnglish.get(symbol, '?')

        # is capitalized
        if capitalize:
            if character != " ":
                character = character.upper()
                capitalize = False

        english.append(character)
        curr += 6

    res = ""

    for word in english:
        res += word

    return res

# system code ensuring script can be run from command line / terminal
if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = ' '.join(sys.argv[1:])
    else:
        input = ''
    
    if 'O' in input or '.' in input:
        print(toEnglish(input), end='')
    else:
        print(toBraille(input), end='')