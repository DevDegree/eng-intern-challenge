brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': '0', '.....O.O': '1', '.....O.OO': '2', 
    '.....O.OOO': '3', '.....O.OOOO': '4', '.....O.OOOOO': '5', '.....O.OOOOOO': '6',
    '.....O.OOOOOOO': '7', '.....O.OOOOOOOO': '8', '.....O.OOOOOOOOO': '9', 
    '..O...': 'capital'  
}

englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '0': '.....O', '1': '.....O.', '2': '.....O.O',
    '3': '.....O.OO', '4': '.....O.OOO', '5': '.....O.OOOO', '6': '.....O.OOOOO',
    '7': '.....O.OOOOOO', '8': '.....O.OOOOOOO', '9': '.....O.OOOOOOOO',
    'capital': '..O...'  
}

# Function to check if the input string is Braille
def isBraille(inputText):
    for c in inputText:
        if c != 'O' and c != '.':  # Verify each character is 'O' or '.'
            return False
    return True

# Convert English to Braille
def convertEnglishToBraille(inputEnglish):
    convertText = ""
    for char in inputEnglish:
        if char.isupper():
            convertText += englishToBraille['capital']  # Add capital marker
            char = char.lower()  # Convert to lowercase for Braille lookup
        if char in englishToBraille:
            convertText += englishToBraille[char]
        else:
            convertText += '......'  # For space or unsupported characters
    return convertText

# Convert Braille to English
def convertBrailleToEnglish(inputBraille):
    convertText = ""
    i = 0
    while i < len(inputBraille):
        brailleNumbers = inputBraille[i:i+6]
        if brailleNumbers == englishToBraille['capital']:
            i += 6
            brailleNumbers = inputBraille[i:i+6]
            convertText += brailleToEnglish.get(brailleNumbers, '`~`').upper()  # Capitalize the letter
        else:
            convertText += brailleToEnglish.get(brailleNumbers, '`~`')
        i += 6
    return convertText

# Main function
if __name__ == "__main__":
    inputString = input("Enter the String: ")

    if isBraille(inputString):
        print("Braille")
        print("Converted to English: ", convertBrailleToEnglish(inputString))
    else:
        print("English")
        print("Converted to Braille: ", convertEnglishToBraille(inputString))


