import sys

# Braille to English mappings
brailleToEnglish = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',  # Corrected mapping
    'O..OOO': 'z', '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', 'O.O..O': '(',
    '.O.OO.': ')'
}

# English to Braille mappings
englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',  # Corrected mapping
    'z': 'O..OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O',
    ')': '.O.OO.'
}

# Numbers and their Braille equivalents
convertNums = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Check if input is Braille
def isBraille(inputText):
    for c in inputText:
        if (c != '.') and (c != 'O'):
            return False
    return True

# Convert Braille to English
def convertBraille(inputText):
    full = inputText
    translation = ''
    numbers = False
    cap = False
    while(full != ''):
        temp = full[:6]
        full = full[6:]
        if (temp == '......'):  # Space
            numbers = False
            translation += ' '
        elif (temp == '.....O'):  # Capitalization sign
            cap = True
        elif (temp == '.O.OOO'):  # Number sign
            numbers = True
        elif (numbers == True):
            translation += convertNums.get(temp, 'error')
        elif (cap == True):
            translation += brailleToEnglish.get(temp, 'error').upper()
            cap = False
        else:
            translation += brailleToEnglish.get(temp, 'error')    
    return translation

# Convert English to Braille
def convertEnglish(inputText):
    full = inputText
    translation = ''
    numbers = False
    while (full != ''):
        temp = full[:1]
        full = full[1:]
        if (temp == ' '):
            numbers = False
            translation += '......'  # Braille for space
        elif (temp.isnumeric()):
            if (numbers == False):
                numbers = True
                translation += '.O.OOO'  # Number sign
            translation += convertNums.get(temp, 'error')
        elif (temp.isupper()):
            translation += '.....O' + englishToBraille.get(temp.lower(), 'error')  # Other capital letters
        else:
            translation += englishToBraille.get(temp, 'error')  # Lowercase letters
    return translation




def main():
    if (len(sys.argv) < 2):
        print("No input detected. Running manual tests...")

        # Manual test cases
        test_cases = [
            {"input": "Hello world", "expected": ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."},
            {"input": "42", "expected": ".O.OOOOO.O..O.O..."},
            {"input": ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", "expected": "Abc 123"},
            {"input": "xYz", "expected": "OO..OO.....OO.OOOO..OOO"}  # Corrected expected output
        ]

        # Run manual test cases
        for case in test_cases:
            input_text = case["input"]
            expected = case["expected"]

            # Detect if input is Braille or English
            if isBraille(input_text):
                result = convertBraille(input_text)
            else:
                result = convertEnglish(input_text)

            print(f"Input: {input_text}")
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Test {'Passed' if result == expected else 'Failed'}")
            print("-" * 40)

    else:
        args = sys.argv[1:]

        # Check if input is Braille
        if isBraille(args[0]):
            translationText = '......'.join(args)  # Join args for Braille input
            print(convertBraille(translationText))
        else:
            translationText = ' '.join(args)  # Join args for English input
            print(convertEnglish(translationText))

if __name__ == "__main__":
    main()