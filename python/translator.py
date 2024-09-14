import sys

# Mapping from English characters to Braille and vice versa
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O.OO..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', ',': '.O....', ';': '.OO...', ':': '.O.O..',
    '.': '.O.OO.', '!': '.OO.O.', '?': '.OO..O', '-': '..O.O.', '/': '.O.O..',
    '(': '.O.O.O', ')': 'O..O.O', '<': 'OO...O', '>': '..OO.O'
}

english_to_braille_nums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse Braille dictionaries for decoding
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_english.update({v: k for k, v in english_to_braille_nums.items()})

def is_braille(text):
    """
    Determine if the input text is Braille by checking if it only contains 'O' and '.' characters.
    
    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text is Braille, False otherwise.
    """
    return all(char in "O." for char in text)

def english_to_braille_translation(text):
    """
    Translate English text to Braille.
    
    Args:
        text (str): The English text to translate.

    Returns:
        str: The translated Braille text.
    """
    result = []
    number_mode = False

    for char in text:
        # Handle uppercase letters
        if char.isupper():
            result.append(".....O")
            char = char.lower()
        
        # Handle numbers
        if char.isdigit():
            if not number_mode:
                result.append(".O.OOO")
                number_mode = True
            result.append(english_to_braille_nums.get(char, "......"))
        
        # Handle spaces
        elif char == ' ':
            number_mode = False
            result.append("......")
        
        # Handle English characters
        else:
            if char in english_to_braille:
                result.append(english_to_braille[char])
            else:
                result.append("......")  # Default to blank for unsupported characters
    
    return ''.join(result)

def braille_to_english_translation(text):
    """
    Translate Braille text to English.
    
    Args:
        text (str): The Braille text to translate.

    Returns:
        str: The translated English text.
    """
    result = []
    letters = [text[i:i+6] for i in range(0, len(text), 6)]
    number_mode = False
    capitalize = False

    for braille_char in letters:
        # Check for capitalization indicator
        if braille_char == ".....O":
            capitalize = True
        
        # Check for number mode indicator
        elif braille_char == ".O.OOO":
            number_mode = True
        
        # Handle space in Braille
        elif braille_char == "......":
            result.append(" ")
            number_mode = False
        
        # Translate Braille to English
        elif braille_char in braille_to_english:
            char = braille_to_english[braille_char]
            if number_mode:
                result.append(char)
                number_mode = False
            else:
                result.append(char.upper() if capitalize else char)
                capitalize = False
        else:
            result.append(" ")  # Handle unknown Braille patterns as spaces

    return ''.join(result).strip()

def detect_input_type(text):
    """
    Determine the type of input (Braille or English) based on the text.
    
    Args:
        text (str): The input text to check.

    Returns:
        str: 'braille' if the text contains only 'O' and '.', 'english' otherwise.
    """
    if all(char in 'O.' for char in text):
        return 'braille'
    return 'english'

def main():
    """
    Main function to handle command-line arguments and perform the appropriate translation.
    """
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string>")
        sys.exit(1)

    # Concatenate command-line arguments into a single string
    input_text = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_text)

    # Perform the appropriate translation based on the input type
    if input_type == 'braille':
        translated = braille_to_english_translation(input_text)
    else:
        translated = english_to_braille_translation(input_text)

    print(translated)

if __name__ == '__main__':
    main()
