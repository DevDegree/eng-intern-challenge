import sys

# Dictionary to map English alphabet to Braille patterns
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
    ' ': '......',
    'capital': '.....O', # Indicator for capitalization
    'number': '.O.OOO',  # Indicator for numbers
}

# Dictionary to map Braille patterns to English alphabet
BRAILLE_TO_ALPHA = {v:k for k,v in ALPHA_TO_BRAILLE.items()}

# Dictionary to map alphabet to corresponding numbers used for Braille
ALPHA_TO_NUM = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}

# Dictionary to map numbers to corresponding alphabet used for Braille
NUM_TO_ALPHA = {v:k for k,v in ALPHA_TO_NUM.items()}

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
                corresponding_alpha = NUM_TO_ALPHA[text[i]]
                result.append(ALPHA_TO_BRAILLE[corresponding_alpha])
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
            char = BRAILLE_TO_ALPHA[braille[i+6:i+12]].upper()
            result.append(char)
            i += 12
        # Handle numbers
        elif BRAILLE_TO_ALPHA[braille_char] == 'number':
            i += 6
            while i < len(braille) and BRAILLE_TO_ALPHA[braille[i:i+6]] != ' ':
                char = ALPHA_TO_NUM[BRAILLE_TO_ALPHA[braille[i:i+6]]]
                result.append(char)
                i+=6           
        # Handle all other characters
        else:
            char = BRAILLE_TO_ALPHA[braille[i:i+6]]
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