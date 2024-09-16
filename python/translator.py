import sys

# Dictionary for Braille alphabet mapping
BRAILLE_ALPHABET = {
    # Lowercase letters
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..", 
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...", 
    'j': ".OOO..",
    'k': "O...O.", 
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.", 
    'p': "OOO.O.", 
    'q': "OOOOO.", 
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O", 
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    
    # Punctuation
    '.': "..OO.O",
    ',': "..O...",
    '?': "..O.OO",
    '!': "..OOO.",
    ':': "..OO..",
    ';': "..O.O.",
    '-': "..O.O.",
    '/': ".O..O.",
    '>': ".OO..O", 
    '<': "O..OO.", 
    '(': "O.O..O",
    ')': ".O.OO.",
    
    # Special symbols
    'capital': ".....O",
    'number': ".O.OOO",
    'decimal': ".O.O..", 
    'space': "......", 
}

BRAILLE_TO_ENGLISH = {v: k for k, v in BRAILLE_ALPHABET.items()}

# Function to convert English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(BRAILLE_ALPHABET['capital'])  # Capital prefix for uppercase letters
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(BRAILLE_ALPHABET['number'])  # Number prefix
                number_mode = True
            # Map digit to corresponding Braille symbol via letters 'a' to 'j'
            if char == '0':
                letter = 'j'
            else:
                letter = chr(ord('a') + int(char) - 1)
            result.append(BRAILLE_ALPHABET[letter])
        else:
            number_mode = False
            if char == ' ':
                result.append(BRAILLE_ALPHABET['space'])
            elif char in BRAILLE_ALPHABET:
                result.append(BRAILLE_ALPHABET[char])
            else:
                pass
    
    return ''.join(result)

# Function to convert Braille to English
def braille_to_english(braille):
    result = []
    i = 0
    capital_mode = False
    number_mode = False
    
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == BRAILLE_ALPHABET['capital']:
            capital_mode = True
        elif symbol == BRAILLE_ALPHABET['number']:
            number_mode = True
        elif symbol == BRAILLE_ALPHABET['space']:
            result.append(' ')
            number_mode = False  # Reset number mode after space
        elif symbol in BRAILLE_TO_ENGLISH:
            char = BRAILLE_TO_ENGLISH[symbol]
            
            if number_mode:
                if char in 'abcdefghij':
                    digit = str(ord(char) - ord('a') + 1)
                    if digit == '10':
                        digit = '0'
                    result.append(digit)
            else:
                if capital_mode:
                    result.append(char.upper())
                    capital_mode = False
                else:
                    result.append(char)
    
        i += 6  # Move to the next Braille character
    
    return ''.join(result)

def detect_language(input_string):
    # Detect if the input is Braille or English
    if set(input_string).issubset({'O', '.'}):
        return 'braille'
    return 'english'

def translate(input_text):
    language = detect_language(input_text)
    
    if language == 'english':
        return english_to_braille(input_text)
    else:
        return braille_to_english(input_text)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide an input text to translate.")
    else:
        input_text = ' '.join(sys.argv[1:])
        print(translate(input_text))
