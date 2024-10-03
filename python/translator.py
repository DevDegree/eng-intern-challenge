import sys  # Import the sys module to access command-line arguments

# Braille mappings
braille_to_eng = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
    'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
    'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
    'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
    'O..OOO': 'Z', '......': ' ',
    '.....O': 'CAPITAL', '.O.OOO': 'NUMBER'
}  # Dictionary mapping Braille characters to English characters

# Create a new dictionary that is the inverse of braille_to_eng
eng_to_braille = {v: k for k, v in braille_to_eng.items()}  # Dictionary mapping English characters to Braille characters

# Number mappings
number_map = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}  # Dictionary mapping English letters to their corresponding numbers

def braille_to_english(braille):
    """
    Function to translate Braille to English.
    
    This function takes a Braille string as input, and returns the corresponding English string.
    It uses the braille_to_eng dictionary to map Braille characters to English characters.
    It also handles capitalization and numbers.
    """
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        if char == '.....O':  # Capital indicator
            capitalize_next = True
        elif char == '.O.OOO':  # Number indicator
            number_mode = True
        else:
            if char in braille_to_eng:
                letter = braille_to_eng[char]
                if number_mode and letter in number_map:
                    result.append(number_map[letter])
                else:
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    result.append(letter)
                    number_mode = False
            else:
                result.append('?')
        i += 6
    
    return ''.join(result)

def english_to_braille(text):
    """
    Function to translate English to Braille.
    
    This function takes an English string as input, and returns the corresponding Braille string.
    It uses the eng_to_braille dictionary to map English characters to Braille characters.
    It also handles capitalization and numbers.
    """
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(eng_to_braille['NUMBER'])
                number_mode = True
            result.append(eng_to_braille[list(number_map.keys())[list(number_map.values()).index(char)]])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(eng_to_braille['CAPITAL'])
                result.append(eng_to_braille[char.upper()])
            else:
                result.append(eng_to_braille[char.upper()])
    
    return ''.join(result)

def is_braille(text):
    """
    Function to check if a string is a valid Braille string.
    
    This function checks if all characters in the string are either 'O' or '.', and if the length of the string is a multiple of 6.
    """
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def translate(text):
    """
    Main translation function.
    
    This function determines whether the input string is Braille or English, and calls the corresponding translation function.
    """
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

if __name__ == '__main__':
    # Check if the script is being run directly (not being imported as a module)
    if len(sys.argv) > 1:
               # If command-line arguments are provided, join them into a single string
        text = ' '.join(sys.argv[1:])
        print(translate(text))  # Translate the input string and print the result
    else:
        print("No input provided") 