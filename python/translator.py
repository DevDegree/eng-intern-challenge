import sys

# Check if the correct number of arguments were passed
if len(sys.argv) != 2:
    sys.exit(1)

input_string = sys.argv[1]

def is_braille(input_string):
    return len(input_string) % 6 == 0 and all(c in 'O.' for c in input_string)

alphabet_braille = {
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
    return "Value not found"

def BrailleToEnglish(braille):
    englishWord = ""
    isCapital = False
    isNumber = False

    brailles = [braille[i:i + 6] for i in range(0, len(braille), 6)]
    
    for braille_char in brailles:
        if braille_char == "......":  
            englishWord += " "
            isNumber = False  
        
        elif braille_char == ".....O": 
            isCapital = True
        
        elif braille_char == ".O.OOO": 
            isNumber = True
        
        else:
            if isNumber:
                key = get_key_from_value(alphabet_braille, braille_char)
                if key in 'abcdefghij':  
                    key = str(ord(key) - ord('a') + 1)
                    if key == '10':
                        key = '0'  
                englishWord += key
            else:
                key = get_key_from_value(alphabet_braille, braille_char)
                if isCapital:
                    key = key.upper()  
                    isCapital = False  
                englishWord += key
    
    return englishWord
    
def englishToBraille(word):
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
        newWord += alphabet_braille[char]
    return newWord
        
# Process input
if is_braille(input_string):
    output = BrailleToEnglish(input_string)
else:
    output = englishToBraille(input_string)

print(output)
