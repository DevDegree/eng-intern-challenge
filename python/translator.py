import sys

# Define the Braille to English dictionary
bte_letters = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", 
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", 
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
    "O..OOO": "z",
}

bte_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")", "......": " ", 
    ".....O": "capital", ".O...O": "decimal", ".O.OOO": "number"
}

# Define the English to Braille dictionary (reversed the key and value from Braille to English Dict)
english_to_braille = {val:key for key, val in bte_letters.items()}

english_to_braille.update({val:key for key, val in bte_numbers.items()})

# Function to translate Braille to English
def translate_braille_to_english(braille_input):
    result = []
    i = 0
    capitalize = False
    number_mode = False
    
    while i < len(braille_input):
        braille_char = braille_input[i:i+6]  # Consider 6 characters at a time
        
        if braille_char == ".....O":  # Capital letter indicator
            capitalize = True
        elif braille_char == ".O.OOO":  # Number mode indicator
            number_mode = True
        elif braille_char == ".O...O":  # Decimal point indicator
            result.append('.')
        elif number_mode and (braille_char in bte_numbers):
            result.append(bte_numbers[braille_char])
        elif braille_char in bte_letters:
            char = bte_letters[braille_char]
            if capitalize:
                result.append(char.upper())
                capitalize = False
            else:
                result.append(char)
        elif braille_char in bte_numbers:
            result.append(bte_numbers[braille_char])
        elif braille_char == "......":
            # Reset number mode after a space
            number_mode = False
        else:
            result.append("?")  # Handle unknown Braille patterns
            
        i += 6

    return ''.join(result)

# Function to translate English to Braille
def translate_english_to_braille(english_input):
    result = []
    number_mode = False

    for char in english_input:
        if char.isupper():
            result.append(".....O")  # Capitalization symbol
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            if not number_mode:
                result.append(".O.OOO")  # Number follows symbol
                number_mode = True
            result.append(english_to_braille[char])
        elif char in english_to_braille:
            result.append(english_to_braille[char])
        elif char in english_to_braille:
            result.append(english_to_braille[char])
        elif char == " ":
            result.append("......")  # Space symbol
            number_mode = False
        else:
            result.append("......")  # Unknown or unsupported character
    return ''.join(result)


def is_braille(input_string):
    # Remove spaces for accurate length and character checking
    cleaned_input = input_string.replace(" ", "")
    
    # Check if length is a multiple of 6 and contains only 'O' and '.'
    if len(cleaned_input) % 6 == 0 and all(char in {'O', '.'} for char in cleaned_input):
        return True
    return False

# Main execution logic
if __name__ == "__main__":
    input_string = ' '.join([string for string in sys.argv[1:]])
    if is_braille(input_string):
        # Assuming the input is in Braille
        translated = translate_braille_to_english(input_string)
    else:
        # Assuming the input is in English
        translated = translate_english_to_braille(input_string)
    
    print(translated)