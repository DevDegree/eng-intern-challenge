import sys

# Dictionary mapping English characters to Braille
EBdic = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', # single space
    'CAPITAL': '.....O', # capital follows
    'number': '.O.OOO' # number follows
}

# reverse of English to Braille dict
alphaBEdic = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    '.....O': 'CAPITAL', 
    '.O.OOO': 'number',
    '......': ' '
}
digitBEdic = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def isBraille(st):
    uniqueChars = set(st)
    brailleUniqueChars = {'O', '.'}
    if (uniqueChars - brailleUniqueChars): # this checks if the resulting set is empty
        return False
    return True

def EBtranslate(st): # English to braille
    ans = []
    curNumber = False # you are currently iterating over the digits of a number
    for c in st:
        # special case characters
        if not curNumber and c.isdigit(): # you find the first digit in number
            ans.append(EBdic['number'])
            curNumber = True
        elif c == ' ': # spaces "terminate" numbers
            curNumber = False
        
        if c.isalpha() and c.isupper():
            ans.append(EBdic['CAPITAL'])
            c = c.lower()
        
        ans.append(EBdic.get(c, '......'))  # Add each translation braille character
    
    return ''.join(ans)

def BEtranslate(st):
    groups = []
    for i in range(0, len(st), 6): # makelist of braille chars
        groups.append(st[i: i+6])

    ans = []
    isNumber = False # Flag for if you need to use the digit dict
    capital = False

    for c in groups:
        if c == EBdic['CAPITAL']:  # Check for capitalization
            capital = True # The next character should be capitalized, so continue to the next iteration
            continue
        elif c == EBdic['number']:  # Check for number mode
            isNumber = True
            continue  # Skip adding 'number' to ans
        elif c == EBdic[' ']:  # terminates numbers
            ans.append(' ')
            isNumber = False  # Reset number mode after a space
        else:
            if isNumber:  # If in number mode, use the digit dictionary
                ans.append(digitBEdic.get(c, ''))
            else:  # Normal letter mode
                if c in alphaBEdic:
                    letter = alphaBEdic[c]
                    if capital:
                        letter = letter.upper()
                        capital = False
                    ans.append(letter)
                else:
                    ans.append('')

    return ''.join(ans)  # Convert to a string



# Main function to handle input and output
def main():
    inputStr = ' '.join(sys.argv[1:])
    
    if isBraille(inputStr):
        print(BEtranslate(inputStr))
    else:
        print(EBtranslate(inputStr))

if __name__ == '__main__':
    main()