import sys

# Braille alphabet dictionary for letters
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Braille numbers (actually reuse the first 10 letters + number indicator)
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille punctuation dictionary
braille_punctuation = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
    '<': '.OO..O', '>': 'OO...O'
}

# Special symbols in Braille
capital_follows = '.....O'  # Indicates next letter is capital
decimal_follows = '.O...O'   # Indicates decimal follows
number_follows = '.O.OOO'     # Indicates numbers are following
braille_space = '......'      # Space in Braille

# Reverse mappings for translation from Braille to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}
reverse_braille_punctuation = {v: k for k, v in braille_punctuation.items()}

def translate_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char == ' ':
            result.append(braille_space)
        elif char.isdigit():
            if not number_mode:
                result.append(number_follows)
                number_mode = True
            result.append(braille_numbers[char])
        elif char == '.':
            result.append(decimal_follows)  # Append decimal indicator
        elif char.isalpha():
            if char.isupper():
                result.append(capital_follows)
            result.append(braille_alphabet[char.lower()])
            number_mode = False  # Reset number mode if a letter is encountered
        elif char in braille_punctuation:
            result.append(braille_punctuation[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    number_mode = False
    capitalize_next = False

    while i < len(braille):
        chunk = braille[i:i + 6]  # Read the next 6-dot Braille character
        
        if chunk == braille_space:
            result.append(' ')
            i += 6  # Move past the space
            continue
            
        if chunk == number_follows:
            number_mode = True
        elif chunk == capital_follows:
            capitalize_next = True
        elif number_mode and chunk in reverse_braille_numbers:
            # Process numbers
            result.append(reverse_braille_numbers[chunk])
        elif chunk == decimal_follows:
            # Handle decimal point when it is detected
            result.append('.')
        elif chunk in reverse_braille_punctuation:
            # Process punctuation
            result.append(reverse_braille_punctuation[chunk])
        elif chunk in reverse_braille_alphabet:
            # Process letters
            letter = reverse_braille_alphabet[chunk]
            if capitalize_next:
                letter = letter.upper()
                capitalize_next = False
            result.append(letter)
        else:
            # Handle unknown chunks (if any)
            result.append('?')  # Placeholder for unknown chunks
        i += 6
    
    return ''.join(result)

def is_braille(input_string):
    # Check if input consists only of O's, .'s, and spaces
    return all(char in 'O. ' for char in input_string)

def main():
    # Get input string from command line arguments
    if len(sys.argv) < 2:
        print("Please provide input text.")
        return
    
    input_text = sys.argv[1]
    
    if is_braille(input_text):
        # Translate from Braille to English
        print(translate_to_english(input_text))
    else:
        # Translate from English to Braille
        print(translate_to_braille(input_text))

if __name__ == '__main__':
    main()
