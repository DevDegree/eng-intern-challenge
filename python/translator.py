import sys

# Dictionary for braille letters. Each letter is represented by a unique 6-dot pattern.
braille_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO'
}

# Dictionary for braille numbers. Uses the same patterns as letters but requires a number marker.
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Dictionary for braille symbols. Contains punctuation and special characters.
braille_symbols = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '...O..',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......'  
}

# Combined braille alphabet (letters, numbers, and symbols).
braille_alphabet = {**braille_symbols, **braille_numbers, **braille_letters}

# Special braille follow markers for capitalization, decimals, and numbers.
braille_follows = {
    'capital': '.....O' ,   # Marks the following letter as capital.
    'decimal': '.O...O',    # Decimal point marker.
    'number': '.O.OOO'      # Number marker.
}

# Helper function to retrieve the key from a dictionary based on its value.
def getKeyFromValue(braille_dict, value):
    for key, val in braille_dict.items():
        if val == value:
            return key
    return None

# Checks if the given text is in braille format (contains only 'O' or '.').
def isBraille(text):
    for char in text:
        if char != '.' and char.lower() != 'o':
            return False
    return True
  
# Converts braille text into English characters.
def brailleToEnglish(text):
    # Split the braille text into chunks of 6 dots (each representing a character).
    def splitStringToParts(s, num_parts):
        return [s[i:i+num_parts] for i in range(0, len(s), num_parts)]
    
    parts = splitStringToParts(text, 6)
    english = ''
    follows = ''  # Tracks special markers like 'capital' or 'number'.

    for braille in parts:
        if braille == '......':  # Handle space.
            english += ' '
            follows = ''
            continue

        # Check for follow markers.
        if braille in braille_follows.values():
            follows = getKeyFromValue(braille_follows, braille)
            continue
        
        # If follows is 'number', prioritize numbers or symbols.
        if follows == 'number' or follows == 'decimal':
            character = getKeyFromValue({**braille_numbers, **braille_symbols}, braille)
        else:
            # Handle letters.
            character = getKeyFromValue(braille_letters, braille)
            if follows == 'capital':  # Uppercase the letter if 'capital' follows.
                character = character.upper()
                follows = ''  # Reset follows after capital.

        if character:
            english += character

    return english

# Converts English text into braille.
def englishToBraille(text):
    braille = ''
    follows = ''
    
    for char in text:
        # Handle capital letters.
        if char.isupper():
            braille += braille_follows['capital']  # Add capital follow marker.
            braille += braille_letters[char.lower()]
        # Handle lowercase letters.
        elif char.lower() in braille_letters:
            braille += braille_letters[char.lower()]
        # Handle numbers (number follow marker required).
        elif char in braille_numbers:
            if follows != 'number':
                braille += braille_follows['number']  # Add number follow marker if needed.
                follows = 'number'
            braille += braille_numbers[char]
        # Handle symbols.
        elif char in braille_symbols:
            braille += braille_symbols[char]
            follows = ''  # Reset the follows context for other characters.
        # Handle space.
        elif char == ' ':
            braille += braille_symbols[' ']
            follows = ''  # Reset follows as spaces don't affect context.

    return braille
    
# Main function to handle command-line arguments and convert text.
def main():
    text = ' '.join(sys.argv[1:])  # Join command-line arguments into a single string.
    if (isBraille(text)):
        print(brailleToEnglish(text))  # Convert braille to English.
    else:
        print(englishToBraille(text))  # Convert English to braille.

# Run the main function if the script is executed.
if __name__ == "__main__":
    main()
