import sys

# Special symbols
BRAILE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS = '.O.OOO' 
BRAILLE_SPACE = '......'
ENGLISH_SPACE = ' '

# Dictionaries
ENGLISH_TO_BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'  # Space
}

ENGLISH_TO_BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..'
}

BRAILLE_TO_ENGLISH_ALPHABET = {bra: eng for eng, bra in ENGLISH_TO_BRAILLE_ALPHABET.items()}
BRAILLE_TO_ENGLISH_NUMBERS = {bra: eng for eng, bra in ENGLISH_TO_BRAILLE_NUMBERS.items()}

# Converts input text in braille to english and prints the english string
def decode(text):
    CAPITAL_FLAG = False
    NUMBER_FLAG = False
    for i in range(0, len(text), 6):
        braille_char = text[i:i+6]

        if braille_char == BRAILE_CAPITAL_FOLLOWS: # Special character
            CAPITAL_FLAG = True
        elif braille_char == BRAILLE_NUMBER_FOLLOWS: # Special character
            NUMBER_FLAG = True
        else:
            if braille_char == BRAILLE_SPACE: # Space
                char = ENGLISH_SPACE
                NUMBER_FLAG = False
            elif NUMBER_FLAG: # Number
                char = BRAILLE_TO_ENGLISH_NUMBERS[braille_char]
            elif braille_char in BRAILLE_TO_ENGLISH_ALPHABET: # Character
                char = BRAILLE_TO_ENGLISH_ALPHABET[braille_char]
                if CAPITAL_FLAG:
                    char = char.upper()
                    CAPITAL_FLAG = False
            else: # Unknown
                continue
            print(char, end='')

# Converts input text in english to braille and prints the braille string
def encode(text):
    NUMBER_FLAG = False

    for char in text:
        braille_char = str()
        if char.isnumeric(): # Number
            if NUMBER_FLAG == False:
                braille_char = BRAILLE_NUMBER_FOLLOWS
                NUMBER_FLAG = True
            braille_char += ENGLISH_TO_BRAILLE_NUMBERS[char]
        elif char == ' ': # Space
            braille_char = BRAILLE_SPACE
            NUMBER_FLAG = False
        elif char.lower() in ENGLISH_TO_BRAILLE_ALPHABET: # Character
            if char.isupper():
                braille_char = BRAILE_CAPITAL_FOLLOWS
            braille_char += (ENGLISH_TO_BRAILLE_ALPHABET[char.lower()])
        else: # Unknown 
            continue

        print(braille_char, end='')


# Return true if text is likely in braille and false otherwise
def is_braille(text):
    # Likely to be braille if all characters are O or ., and the input size is a multiple of 6
    if all(char in 'O.' for char in text) and (len(text) % 6 == 0):
        return True
    return False

# Translate the input text from english to braille or vice versa
def translate(text):
    if is_braille(text):
        decode(text)
    else:
        encode(text)

def main():
    text = ' '.join(sys.argv[1:])
    translate(text)

if __name__ == "__main__":
    main()
