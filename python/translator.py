import sys

def iterate_in_chunks(string):
    # Iterate over the string in steps of 6
    for i in range(0, len(string), 6):
        yield string[i:i + 6]

def main():
    input = sys.argv[1]
    output = ""
    
    brailleToEnglishLetters = {
         'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
    }
    
    brailleToEnglishDigits = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
    }
    
    englishToBrailleLetters = {'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'}
    
    englishToBrailleDigits = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'}

    
    # Determine type of input
    if "." in input:
        # Convert to English
        isNumber = isCaps = False
        for char in iterate_in_chunks(input):
            # Check for special characters
            if char == ".....O": # For capital follows
                isCaps = True
            elif char == ".O.OOO": # For number follows
                isNumber = True
            elif char == "......": # For space
                isNumber = False
                output += " "
            else:
                if isNumber:
                    output += brailleToEnglishDigits[char]
                elif isCaps:
                    output += brailleToEnglishLetters[char].upper()
                    isCaps = False
                else:
                    output += brailleToEnglishLetters[char]
        
    else:
        numberMarked = False
        for char in input:
            if char == " ":
                output += "......"
                numberMarked = False
            elif char.isdigit():
                if not numberMarked:
                    output += ".O.OOO"
                    numberMarked = True
                output += englishToBrailleDigits[char]
            else:
                if char.isupper():
                    output += ".....O"
                
                output += englishToBrailleLetters[char.lower()]
    
    print(output)
    
main()
