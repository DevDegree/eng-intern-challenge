import sys

# Braille dictionary
braille_alphabet_extended = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', '.': '.O..OO', ',': '.O....', '?': '..O.OO', '!': '.OOO.O', 
    ':': 'OO..OO', ';': 'O.O...', '-': '...O..', '/': 'O..OO.', '<': 'O.O..O', '>': '.O.O.O', 
    '(': 'O..O.O', ')': '.OO.OO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse dictionary for Braille-to-English
braille_to_english = {v: k for k, v in braille_alphabet_extended.items()}

# Function to detect if the string is Braille or English
def is_braille(input_str):
    return all(char in ['O', '.'] for char in input_str)

# English to Braille
def english_to_braille(text):
    braille_output = []
    number_mode = False  

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_alphabet_extended['number'])
                number_mode = True
            braille_output.append(braille_alphabet_extended[char])
        elif char.isalpha():
            if char.isupper():
                braille_output.append(braille_alphabet_extended['capital'])
                braille_output.append(braille_alphabet_extended[char.lower()])
            else:
                braille_output.append(braille_alphabet_extended[char])
            number_mode = False  
        else:
            braille_output.append(braille_alphabet_extended.get(char, '......'))  
            number_mode = False  

    return ''.join(braille_output)

def braille_to_english_translation(braille_text):
    i = 0
    braille_output = []
    capital_mode = False
    number_mode = False

    # Maps Braille to numbers (1-9, 0) once number mode is activated
    number_map = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
        'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
    }
    
    # Reverse dictionary for Braille to English letters
    letter_map = {v: k for k, v in braille_alphabet_extended.items() if k.isalpha()}

    while i < len(braille_text):
        braille_char = braille_text[i:i+6]

        # Handle capital letter indicator
        if braille_char == braille_alphabet_extended['capital']:
            capital_mode = True
        # Handle number indicator
        elif braille_char == braille_alphabet_extended['number']:
            number_mode = True
        else:
            if number_mode and braille_char in number_map:
                braille_output.append(number_map[braille_char])
            elif braille_char in letter_map:
                char = letter_map[braille_char]
                if capital_mode:
                    braille_output.append(char.upper())
                    capital_mode = False  # Reset capital mode after capitalizing the letter
                else:
                    braille_output.append(char)
            else:
                braille_output.append(' ')  
                capital_mode= False
                number_mode = False

        i += 6  # Move to the next Braille character

    return ''.join(braille_output)




# Main function to handle input and decide on the translation
def main():
    if len(sys.argv) < 1:
        return

    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        print(braille_to_english_translation(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == '__main__':
    main()
