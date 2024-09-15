
import sys


# Braille alphabet mapping for letters and punctuation
braille_alphabet = {
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
    'CAPITAL': '.....O',
    'NUMBER' : '.O.OOO',
    'DECIMAL': '.O...O',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......',


}


# Separate mapping for numbers
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


# Reverse dictionaries for Braille-to-English translation
braille_to_english = {v: k for k, v in braille_alphabet.items()}
braille_to_numbers = {v: k for k, v in braille_numbers.items()}






def translate_to_english(braille_text):
    english_output = ""
    is_capital = False
    is_number = False


    # Split the Braille text into chunks of 6
    for i in range(0, len(braille_text), 6):
        symbol = braille_text[i:i+6]


        if symbol == braille_alphabet['CAPITAL']: # Capital indicator
            is_capital = True
            continue  # Skip to the next symbol
        elif symbol == braille_alphabet[' ']:  # Space indicator
            is_number = False
        elif symbol == braille_alphabet['NUMBER']:  # Number indicator
            is_number = True
            continue  # Skip to the next symbol


        if is_number:  # Interpret following symbols as numbers
            if symbol in braille_to_numbers:
                english_output += braille_to_numbers[symbol]


        else:  # Interpret as letters
            if symbol in braille_to_english:
                letter = braille_to_english[symbol]
                if is_capital:
                    letter = letter.upper()
                    is_capital = False  # Reset capital flag
                english_output += letter

    return english_output




def translate_to_braille(text):
    braille_output = ""
    is_number_sequence = False  # To track if we are processing a number sequence
   
    for char in text:
        if char.isalpha():  # If it's a letter
            if is_number_sequence:
                is_number_sequence = False  # Reset if we were in number mode
           
            if char.isupper():  # Capital letters
                braille_output += braille_alphabet['CAPITAL']  # Add capital sign
            braille_output += braille_alphabet[char.lower()]  # Add the Braille for the letter
       
        elif char.isdigit():  # If it's a number
            if not is_number_sequence:  # If this is the first number, add the number indicator
                braille_output += braille_alphabet['NUMBER']
                is_number_sequence = True  # Set flag that we are in a number sequence
            braille_output += braille_numbers[char]  # Add the Braille for the number
       
        elif char == ".":  # Handle periods (for decimals or punctuation)
            braille_output += braille_alphabet['.']  # Always add Braille for period/punctuation
       
        elif char == " ":  # Handle spaces
            braille_output += braille_alphabet[' ']  # Add Braille for a space
       
        elif char in braille_alphabet:  # Handle punctuation and other characters
            if is_number_sequence:
                is_number_sequence = False  # Reset if we were in number mode
            braille_output += braille_alphabet[char]
   
    return braille_output


def is_braille(text):
    # Check if the text seems to be Braille (must consist of 'O' and '.' only and lengths divisible by 6)
    return all(c in "O." for c in text) and len(text) % 6 == 0





# Command line check

def main():
    # Read the input from the command-line arguments
    if len(sys.argv) < 2:
        print("Please provide input text as a command-line argument.")
        sys.exit(1)
    
    # Join all the command-line arguments (in case the input has spaces)
    input_text = ' '.join(sys.argv[1:])
    
    # Check if the input is Braille or English
    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()