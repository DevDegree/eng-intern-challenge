import sys

# Directory mapping Braille patterns to English characters
BRAILLE_TO_ENGLISH = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# Directory mapping Braille symbol patterns to English characters
BRAILLE_TO_ENGLISH_SYMBOLS = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
}

# Reverse mapping of Braille_to_english
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
ENGLISH_TO_BRAILLE_SYMBOLS = {v: k for k, v in BRAILLE_TO_ENGLISH_SYMBOLS.items()}

# Dictionary mapping numbers to Braille patterns
NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Special cases for capital letters, numbers, and decimal point
CAPITAL_SYMBOL = '.....O'
NUMBER_SYMBOL = '.O.OOO'
DECIMAL_SYMBOL = '.O...O'

# Translates Braille to English characters
def brailleToEnglish(braille):
    convertedStr = ""
    index = 0
    capitalize = False # Flag to indiciate if the next character should be cpaitzalized
    numberDetected = False # Flag to indicate if the next character is a number

    while index < len(braille):
        symbol = braille[index:index+6]  
        if symbol == CAPITAL_SYMBOL:
            capitalize = True
            index += 6
            continue   
        if symbol == NUMBER_SYMBOL:
            numberDetected = True
            index += 6
            continue    
        if symbol == DECIMAL_SYMBOL:
            convertedStr += '.'
            index += 6
            continue
        if symbol == '......':
            convertedStr += ' '
            numberDetected = False
            index += 6
            continue 
        if numberDetected: # Converts the braille pattern to the corresponding number
            for digit, braille_digit in NUMBER_TO_BRAILLE.items(): 
                if symbol == braille_digit: 
                    convertedStr += digit
                    break
            else:
                numberDetected = False
        else:
            char = BRAILLE_TO_ENGLISH.get(symbol) or BRAILLE_TO_ENGLISH_SYMBOLS.get(symbol, '')  # Looks up the English character for this Braille symbol 
            if capitalize:
                char = char.upper()
                capitalize = False
            convertedStr += char
        index += 6

    return convertedStr

# Translates English to Braille patterns
def englishToBraille(english):
    convertedStr = ""
    numberDetected = False # Flag to indicate if the next character is a number

    for index, char in enumerate(english):
        if char.isdigit():
            if not numberDetected:
                convertedStr += NUMBER_SYMBOL
                numberDetected = True 
            convertedStr += NUMBER_TO_BRAILLE[char] # Converts the digit to the corresponding Braille pattern
        elif char == '.' and index > 0 and english[index-1].isdigit():
            convertedStr += DECIMAL_SYMBOL
        elif char.isalpha():
            if numberDetected:
                convertedStr += '......'
                numberDetected = False
            if char.isupper():
                convertedStr += CAPITAL_SYMBOL
            convertedStr += ENGLISH_TO_BRAILLE[char.lower()]
        elif char in ENGLISH_TO_BRAILLE_SYMBOLS:
            convertedStr += ENGLISH_TO_BRAILLE_SYMBOLS[char]
            numberDetected = False
        elif char == ' ':
            convertedStr += '......'
            numberDetected = False
        else:
            pass

    return convertedStr

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string1> [<input_string2> ...]") # Prints usage instruction if incorrect number of arguments
        sys.exit(1)

    results = []
    for input_str  in sys.argv[1:]:
        if set(input_str ).issubset({'O', '.'}):
            result = brailleToEnglish(input_str ) # If input is Braille, convert to English
        else:
            result = englishToBraille(input_str ) # If input is English, convert to Braille
        results.append(result)

    print("".join(results), end='')