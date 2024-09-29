import sys

# Braille representations for alphabet 
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

# Braille representations for numbers (same as a-j)
braille_numbers = ['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..']

# Create an inverse mapping from Braille to English by reversing braille_alphabet dictionary
english_braille = {v: k for k, v in braille_alphabet.items()}

# Function to check if input is Braille (O and . format)
def is_braille(input_str):
    # return true if all characters in tsring are either 'O' or '.'
    return all(char in 'O.' for char in input_str) and len(input_str) % 6 == 0

# Function to translate English to Braille
def english_to_braille(text):
    braille_text = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille_text.append(braille_alphabet['capital'])  # Append capital prefix
            braille_text.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            if not number_mode:
                braille_text.append(braille_alphabet['number'])  # Append number prefix
                number_mode = True
            if char == '0':
                braille_text.append(braille_numbers[9]) # '0' is last one
            else:
                braille_text.append(braille_numbers[int(char) - 1])
        else:
            if number_mode:
                number_mode = False
            braille_text.append(braille_alphabet[char])
    return ''.join(braille_text)

# Function to translate Braille to English
def braille_to_english(braille):
    text = []
    i = 0 #start at first braille character
    capital_next = False
    number_next = False
    
    while i < len(braille):
        symbol = braille[i:i+6]  # Read 6 characters at a time
        
        if symbol == braille_alphabet['capital']:
            capital_next = True
        elif symbol == braille_alphabet['number']:
            number_next = True
        elif symbol == braille_alphabet[' ']:
            number_next = False
            text.append(' ')
        else:
            if number_next:
                if symbol in braille_numbers:
                    text.append(str(braille_numbers.index(symbol) + 1))
            else:
                letter = english_braille.get(symbol, '')
                if capital_next:
                    text.append(letter.upper())
                    capital_next = False
                else:
                    text.append(letter)
        
        i += 6
    
    return ''.join(text)

# Main function to handle input and detect translation direction
def main():
    # Get the input string passed as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    # input_str = sys.argv[1]
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        # Translate Braille to English
        print(braille_to_english(input_str))
    else:
        # Translate English to Braille
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
