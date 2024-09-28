import sys

# Define alphabet using dictionary (leave out numbers)
braille_alphabet = {
    # letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',

    # special cases
    "capital_follows" : ".....O",
    "decial_follows" : ".O...O.",
    "number_follows" : ".O.OOO" , 
    
    # special characters and space
    '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OO.O." , ':': "..OO..", 
    ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O", '>': "O..OO.", 
    '(': "O.O..O",  ')': ".O.OO.", ' ': "......"
}

# Translate text to Braille"
def translate_to_braille(text):
    braille_translation = []  # Use a list to collect Braille characters    
    number_mode = False  # Flag to indicate if we're in number mode
    number_map = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
                  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', "0": ".OOO..",}
    for char in text:
        # If character is a number
        if char.isdigit():
            if not number_mode:  # Check if we're not already in number mode
                braille_translation.append(braille_alphabet["number_follows"])  # Add number symbol
                number_mode = True  # Set the flag to indicate we're in number mode
            braille_translation.append(number_map[char])  # Add Braille number directly
        else:
            number_mode = False  # Reset the number mode flag when encountering a non-number
            
            # If character is uppercase
            if char.isupper():
                braille_translation.append(braille_alphabet["capital_follows"])  # Add capital symbol

            # Add the Braille representation of the character
            braille_translation.append(braille_alphabet.get(char.lower()))  # Default to space if not found

    return ''.join(braille_translation)  # Join the list into a single string


# Reverse Braille alphabet to translate Braille to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}

# Translate Braille to English
def translate_to_english(braille):
    english_translation = [] #Use a list to collect english characters 
    i = 0
    number_mode = False  # Start in alphabet mode
    capital_mode = False  # Capitalization flag
    
    number_map = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                  'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
    while i < len(braille):
        char = braille[i:i + 6]
         # Check for capitalization activation
         # Check for space character
        if char == braille_alphabet[' ']:
            english_translation.append(' ')  # Add space
            number_mode = False  # Reset number mode
            i += 6  # Move to the next character
            continue
        
        # Check for number mode activation
        if char == braille_alphabet["number_follows"]:
            number_mode = True
            i += 6  # Move to the next character
            continue
        
        # Check for capitalization activation
        if char == braille_alphabet["capital_follows"]:
            capital_mode = True
            i += 6  # Move to the next character
            continue
        
        # Translate Braille to English letter
        letter = reverse_braille_alphabet.get(char, '')

        if number_mode:
            # If in number mode, convert letters a-j to numbers 1-0
            if letter in number_map:
                letter = number_map[letter]
            else:
                # If a letter outside the range a-j is encountered, revert to letter mode
                number_mode = False  # Reset number mode if a non-number character is found
        
        # Apply capitalization if capital_mode is set
        if capital_mode:
            letter = letter.upper()
            capital_mode = False  # Capitalize only one letter

        # Append the translated letter to the result
        if letter:  # Append only if a valid letter is found
            english_translation.append(letter)

        # Move to the next 6-dot Braille character
        i += 6

    # Return the translated English text
    return ''.join(english_translation)

# Detect if input is Braille or English
def is_braille(input_text):
    # If input consists entirely of 6-character groups of "O" and "." with spaces, it's Braille
    return all(c in "O. " for c in input_text) and len(input_text.replace(' ', '')) % 6 == 0

# Main function to handle input and conversion
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])  # Join the command-line arguments into one string

    if is_braille(text):  # If input is Braille
        result = translate_to_english(text)
    else:  # Otherwise, it's assumed to be English
        result = translate_to_braille(text)
        
    print(result)