import sys

# We want to set up a dictionary that maps Braille characters to English characters, numbers, and special characters.
# Braille to English Mapping
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

# Braille to Numbers Mapping
braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Braille to Special Characters Mapping
braille_to_special_chars = {
    '..OO.O': '.', '..O...': ',', '..O.OO': '?',
    '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
    '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '..OOO.': '!'
}

# English to Braille Mapping
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': '.OO...', '9': '.O.O..', '0': '.OOO..'
}

# English to Braille Special Characters Mapping
special_chars_to_braille = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', '!': '..OOO.'
}
# Takes all the characters in the input text and translates them to Braille characters
def translate_to_braille(text):
    result = ""
    number_mode = False
    for char in text:
        # Check if the character is a special character, uppercase letter, digit, or space
        if char in special_chars_to_braille:
            result += special_chars_to_braille[char]
        elif char.isupper():
            if char.lower() in english_to_braille:
                # Adds the braille translation for capitalization
                result += '.....O' + english_to_braille[char.lower()]
            else:
                # Error message for uppercase letters not found in the mapping
                return f"Error: Character '{char}' not valid"
        elif char.isdigit():
            if not number_mode:
                # Adds the braille translation for numbers
                result += '.O.OOO'
                number_mode = True
            if char in english_to_braille:
                result += english_to_braille[char]
            else:
                # Error message for digits not found in the mapping
                return f"Error: Digit '{char}' not valid"
        elif char == ' ':
            # Adds the braille translation for space
            result += '......'
            number_mode = False
        # This will handle the lowercase letters and any other valid characters
        else:
            if number_mode and not char.isdigit():
                # Exits the number mode if a non-digit character is encountered
                number_mode = False
            if char in english_to_braille:
                result += english_to_braille[char]
            else:
                # Error message for characters not found in the mapping
                return f"Error: Character '{char}' not valid"
    return result

# This function translates Braille characters to English characters
def translate_to_english(text):
    result = ""
    i = 0
    # Checker to indicate if the next letter is capitalized
    capital = False
    # Checker to indicate if the next letter is a number
    number_mode = False
    
    # Iterate through in chunks of 6 characters
    while i < len(text):
        # Extract the Braille symbol
        symbol = text[i:i+6]
        
        # Checks to handle space prefix in Braille
        if symbol == '......':
            result += ' '
            i += 6
            number_mode = False
            
        # Checks to handle the number prefix in Braille
        elif symbol == '.O.OOO':
            number_mode = True
            i += 6
            
        # Checks to handle capital letters prefix in Braille
        elif symbol == '.....O':
            capital = True
            i += 6
            
        # Translate Braille digits to English if in number mode
        elif number_mode and symbol in braille_to_numbers:  
            result += braille_to_numbers[symbol]
            i += 6
        
        # Translate Braille letters to English
        elif symbol in braille_to_english:
            letter = braille_to_english[symbol]
            if capital:
                # Applies capitalization if needed
                letter = letter.upper()
                capital = False
            result += letter
            i += 6
        
        # Translate Braille special characters to English
        elif symbol in braille_to_special_chars: 
            result += braille_to_special_chars[symbol]
            i += 6
        else:
            # Error message for unrecognized Braille symbols
            return f"Error: Braille symbol '{symbol}' not valid"
    return result

# Function to check the validity of the braille input if it matches the Braille guidelines
def is_braille_input(braille):
    # Check if the input only contains Braille characters and has a valid length
    return all(c in '.O' for c in braille) and len(braille) % 6 == 0

# Main function to run code
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text>")
        return

    input_text = " ".join(sys.argv[1:])

    # Determine if the input text is in Braille or English
    if is_braille_input(input_text):
        result = translate_to_english(input_text)
    else:
        result = translate_to_braille(input_text)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
