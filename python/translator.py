import sys


#bRAILLE MAPPINGS
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',  # Braille space
}

REVERSE_BRAILLE_ALPHABET = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ' , # Space mapping
}
REVERSE_BRAILLE_NUMBERS = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}
CAPITAL_PREFIX = '.....O'  # Marks that the next letter is capitalized
NUMBER_PREFIX = '.O.OOO'   # Marks that the following characters are numbers

#to dtermine if input is english or braille
def is_braille(input_str):
    return all(c in 'O.' for c in input_str)

# Translate English to Braille
def english_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(CAPITAL_PREFIX)  # Add the capital prefix
            char = char.lower()

        if char in BRAILLE_ALPHABET:
            result.append(BRAILLE_ALPHABET[char])

        elif char.isdigit():
            result.append(NUMBER_PREFIX)  # Start number mode
            result.append(BRAILLE_NUMBERS[char])
    return ''.join(result)

# Translate Braille to English
def braille_to_english(braille_text):
    result = []
    # Split Braille into 6-character chunks
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    
    capitalize_next = False
    number_mode = False
    
    for braille_char in braille_chars:
        # Skip incomplete chunks
        if len(braille_char) < 6:
            continue
        
        
        # Handle capital letter prefix
        if braille_char == CAPITAL_PREFIX:
            capitalize_next = True
            continue  # Move to the next character after the capital indicator
        
        # Handle number mode prefix
        elif braille_char == NUMBER_PREFIX:
            number_mode = True
            continue  # Move to the next character after number mode indicator
        
        # Handle space
        elif braille_char == '......':
            result.append(' ')
            number_mode = False  # Exit number mode after a space
            capitalize_next = False  # Exit capitalization mode after a space
            continue  # Move to the next character after the space
        
        # Handle numbers in number mode
        if number_mode:
            letter = REVERSE_BRAILLE_NUMBERS.get(braille_char, '?')
            if letter == '?':
                print(f"Error: Unknown number Braille: {braille_char}")
            else:
                result.append(letter)
            number_mode = False    
            continue  # Continue to the next character
        
        # Handle normal letters
        else:
            letter = REVERSE_BRAILLE_ALPHABET.get(braille_char, '?')
            if letter == '?':
                print(f"Error: Unknown letter Braille: {braille_char}")
                continue
            if capitalize_next:
                letter = letter.upper()
                capitalize_next = False
            result.append(letter)

    return ''.join(result)

def main():
    if len(sys.argv) < 2:  # Check if at least one argument is passed
        print("Error: No input provided. Please pass a string to translate.")
        sys.exit(1)

    input_str = sys.argv[1]  # Read the first argument from the command line
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
