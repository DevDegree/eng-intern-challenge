import sys

brailleAlphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......', '.': '.O..OO', ',': '.O....', ';': '.O.O..', ':': '.OO...',
    '!': '.OOO..', '?': '.OO.O.', '-': '....OO', '/': '.O..O.', '(': 'O..O.O',
    ')': 'O..O.O',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse lookup dictionary for numbers
numbersMapping = {v: str(i) for i, v in enumerate(['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..'], start=1)}

def brailleToEnglish(brailleText):
    englishText = ''
    capitalFlag = False
    numberFlag = False
    
    # Make sure there are correct number of characters (multiple of 6)
    if len(brailleText) % 6 != 0:
        return englishText
    
    # Split Braille into chunks of 6 characters
    brailleChunks = [brailleText[i:i+6] for i in range(0, len(brailleText), 6)]
    
    for chunk in brailleChunks:
        if chunk == brailleAlphabet['capital']:
            capitalFlag = True
        elif chunk == brailleAlphabet['number']:
            numberFlag = True
        elif chunk == brailleAlphabet[' ']:
            englishText += ' '
            numberFlag = False  # Reset number flag after a space
        else:
            # Use reverse lookup if mapping is true
            if numberFlag:
                englishText += numbersMapping.get(chunk, '')
            else:
                char = next((k for k, v in brailleAlphabet.items() if v == chunk), None)
                if char is None:
                    return
                if capitalFlag:
                    englishText += char.upper()
                    capitalFlag = False
                else:
                    englishText += char
    return englishText

def englishToBraille(text):
    brailleText = ''
    numberFlag = False
    for char in text:
        # Add space and reset number flag
        if char == ' ':
            brailleText += brailleAlphabet[' ']
            numberFlag = False
            continue

        # Set number flag
        if char.isdigit():
            if numberFlag == False:
                brailleText += brailleAlphabet['number']
                numberFlag = True

        # Add braille for capital and make the character lowercase
        if char.isupper():
            brailleText += brailleAlphabet['capital']
            char = char.lower()

        # Get the braille for the character
        brailleText += brailleAlphabet.get(char)
    return brailleText

def detectAndTranslate(inputText):
    # To check if its Braille, make sure the input is at least 6 characters and the first 6 characters consists of O and .
    if len(inputText) >= 6 and all(char in 'O.' for char in inputText[:6]):
        return brailleToEnglish(inputText)
    else:
        return englishToBraille(inputText)

def main():
    if len(sys.argv) < 2:
        return
    
    # Join the inputs into 1 string
    inputText = ' '.join(sys.argv[1:])
    result = detectAndTranslate(inputText)
    print(result)

if __name__ == "__main__":
    main()