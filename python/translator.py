import sys

# Braille mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

braille_punc = {
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO', 'decimal': '.O...O',
    ',': 'O.....', '.': 'O..OO.', '?': 'O.O.OO', '!': 'O.OO.O', ':': 'O...OO',
    ';': 'O.O...', '-': 'OO....', '/': 'OO.O..', '<': 'O..O..', '>': 'OOO...',
    '(': 'OOOO..', ')': 'O.OO..', '.': '..OO.O'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Inverse lookup for braille_alphabet
inverse_braille_alphabet = {}
for m, n in braille_alphabet.items():
    inverse_braille_alphabet[n] = m

# Inverse lookup for braille_punc
inverse_braille_punc = {}
for m, n in braille_punc.items():
    inverse_braille_punc[n] = m

# Inverse lookup for braille_numbers
inverse_braille_numbers = {}
for m, n in braille_numbers.items():
    inverse_braille_numbers[n] = m


# Function to translate from English to Braille
def translate_to_braille(input_text):
    translated_text = []
    num_follow = False
    
    for char in input_text:
         # Handle spaces
        if char == ' ':
            translated_text.append(braille_punc[' '])

        # Handle punctuation 
        elif char in braille_punc:
            translated_text.append(braille_punc[char])
            
        # Handle numbers
        elif char.isdigit():
            if not num_follow:
                translated_text.append(braille_punc['num'])
                num_follow = True
            translated_text.append(braille_numbers[char])
        
        # Handle letters
        elif char.isalpha():  
            if num_follow:
                num_follow = False
            if char.isupper():
                translated_text.append(braille_punc['cap'])
                char = char.lower()
            translated_text.append(braille_alphabet[char])
    
    return ''.join(translated_text)


# Function to translate from Braille to English
def translate_to_english(braille_text):
    translated_text = []
    num_follow = False
    cap_follow = False
    i = 0
    
    # Break the input Braille string into chunks of 6 characters
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        # Handle space
        if braille_char == '......':
            translated_text.append(' ')
        
        # Handle capital
        elif braille_char == braille_punc['cap']:
            cap_follow = True
        
        # Handle number
        elif braille_char == braille_punc['num']:
            num_follow = True
        
        elif num_follow and braille_char in inverse_braille_numbers:
            translated_text.append(inverse_braille_numbers[braille_char])
            num_follow = False
            
        elif braille_char in inverse_braille_alphabet:
            letter = inverse_braille_alphabet[braille_char]
            if cap_follow:
                letter = letter.upper()
                cap_follow = False
            translated_text.append(letter)
            
        elif braille_char in inverse_braille_punc:
            translated_text.append(inverse_braille_punc[braille_char])
        
        i += 6
    
    return ''.join(translated_text)


# Determine if the input is Braille or English
def is_braille(input_text):
    # Braille is represented by only 'O' and '.' in chunks of 6 characters
    return all(char in 'O.' for char in input_text) and len(input_text) % 6 == 0

def main():
    # read input from terminal
    input_text = ' '.join(sys.argv[1:]) 
    
    if is_braille(input_text):
        translated_text = translate_to_english(input_text)
    else:
        translated_text = translate_to_braille(input_text)
    
    print(translated_text)

if __name__ == "__main__":
    main()
