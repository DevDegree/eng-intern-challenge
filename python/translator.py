import sys

# Dictionary to map English alphabet and digits to Braille patterns
ALPHA_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    ' ': '......',
    'capital': '.....O', # Indicator for capitalization
    'number': '.O.OOO',  # Indicator for numbers
}


# Dictionary to map Braille patterns to English alphabet and digits
BRAILLE_TO_ALPHA = {
    'O.....': 'a:1',
    'O.O...': 'b:2',
    'OO....': 'c:3',
    'OO.O..': 'd:4',
    'O..O..': 'e:5',
    'OOO...': 'f:6',
    'OOOO..': 'g:7',
    'O.OO..': 'h:8',
    '.OO...': 'i:9',
    '.OOO..': 'j:0',
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
    '......': ' ',
    '.....O': 'capital', # Indicator for capitalization in Braille
    '.O.OOO': 'number',  # Indicator for numbers in Braille
    '.O.O.O': '.'        # Period symbol
}



# Function to convert English text to Braille
def english_to_braille(text):
    result = []
    i=0
    while i < len(text):
        # Handle capital letters
        if text[i].isupper():
            result.append(ALPHA_TO_BRAILLE['capital']) # Add capital indicator
            result.append(ALPHA_TO_BRAILLE[text[i].lower()])
        # Handle numbers
        elif text[i].isdigit():
            result.append(ALPHA_TO_BRAILLE['number']) # Add number indicator
            while i < len(text) and text[i] != ' ':
                result.append(ALPHA_TO_BRAILLE[text[i]])
                i+=1
            if i<len(text):
                result.append(ALPHA_TO_BRAILLE[text[i]])  # Add space after number
        # Handle all other characters
        else:
            result.append(ALPHA_TO_BRAILLE[text[i]])
           
        i+=1
    
    return ''.join(result)

# Function to convert Braille to English text
def braille_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        # Extract 6-character Braille pattern
        braille_char = braille[i:i+6]
        # Handle capital letters
        if BRAILLE_TO_ALPHA[braille_char] == 'capital':
            char = BRAILLE_TO_ALPHA[braille[i+6:i+12]].split(":")[0].upper()
            result.append(char)
            i += 12
        # Handle numbers
        elif BRAILLE_TO_ALPHA[braille_char] == 'number':
            i += 6
            while i < len(braille) and BRAILLE_TO_ALPHA[braille[i:i+6]] != ' ':
                char = BRAILLE_TO_ALPHA[braille[i:i+6]].split(":")[1]
                result.append(char)
                i+=6           
        # Handle all other characters
        else:
            char = BRAILLE_TO_ALPHA[braille[i:i+6]].split(":")[0]
            result.append(char)
            i += 6
    
    return ''.join(result)

# Function to determine if the input is English or Braille
def determine_mode(input_text):
    # Check if the input is Braille (contains only 'O' and '.' with length multiple of 6)
    if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
        return "braille"
    else:
        return "english"

# Read input text from command-line arguments
input_text = ' '.join(sys.argv[1:])

# Determine the mode based on the input text
mode = determine_mode(input_text)

# Convert and print the result based on the determined mode
if mode == "english":
    print(english_to_braille(input_text))
elif mode == "braille":
    print(braille_to_english(input_text))