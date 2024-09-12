import sys

# Check if the correct number of arguments were passed
if __name__ == '__main__':
    input_text = sys.argv[1]
    # Concatenate all input arguments into a single string
    fullText = ' '.join(sys.argv[1:])
    
def is_braille(input_string):
    # Check if the input length is a multiple of 6 and contains only 'O' and '.'
    if len(input_string) % 6 == 0 and all(c in 'O.' for c in input_string):
        return True
    return False



braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def brailleToEnglish(braille):
    englishWord = ""
    isCapital = False
    isNumber = False

    # Split the braille string into chunks of 6 characters (each braille letter)
    brailles = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    
    for j in range(len(brailles)):
        if brailles[j] == "......":  # Space
            englishWord += " "
            isNumber = False  # Numbers reset after a space
        
        elif brailles[j] == ".....O":  # Capitalization symbol
            isCapital = True
        
        elif brailles[j] == ".O.OOO":  # Number symbol
            isNumber = True
        
        else:
            # Handle numbers if the number symbol was encountered
            if isNumber:
                key = get_key_from_value(braille_alphabet, brailles[j])
                if key in 'abcdefghij':  # Map letters a-j to numbers 1-0
                    key = str(ord(key) - ord('a') + 1)
                    if key == '10':
                        key = '0'  # Handle "0" being mapped from 'j'
                englishWord += key
            else:
                # Handle regular letters
                key = get_key_from_value(braille_alphabet, brailles[j])
                if isCapital:
                    key = key.upper()  # Capitalize the letter
                    isCapital = False  # Only capitalize the next letter
                englishWord += key
    
    print(englishWord)
    

def englishtToBraille(word):
    newWord = ""
    firstDigit = True
    for char in word:
        if char == " ":
            firstDigit = True
        if char.isupper():
            char = char.lower()
            newWord += ".....O"
        if char.isdigit() and firstDigit:
            newWord += ".O.OOO"
            firstDigit = False
        newWord += braille_alphabet[char]
    print(newWord)
        
if is_braille(fullText):
    brailleToEnglish(fullText)
else:
    englishtToBraille(fullText)

