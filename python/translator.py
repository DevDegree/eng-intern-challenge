import sys

# Braille translation dictionaries
ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..'
}

# Create reverse mappings for Braille to letter and number
BRAILLE_TO_LETTER = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if k not in ['capital', 'number']}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

def text_to_braille(text):
    """
    Translate English text to Braille.
    
    Args:
        text (str): The English text to translate.
        
    Returns:
        str: The Braille representation of the input text.
    """
    braille = ''
    is_number_mode = False

    for char in text:
        if char.isupper():
            # Add capital indicator and translate character to Braille
            braille += ENGLISH_TO_BRAILLE['capital']
            braille += ENGLISH_TO_BRAILLE.get(char.lower(), '')
            is_number_mode = False
        elif char.isdigit():
            if not is_number_mode:
                # Add number indicator for digit mode
                braille += ENGLISH_TO_BRAILLE['number']
                is_number_mode = True
            braille += NUMBER_TO_BRAILLE.get(char, '')
        else:
            braille += ENGLISH_TO_BRAILLE.get(char, '')
            is_number_mode = False

    return braille

def is_valid_braille(braille):
    """
    Check if the Braille input is valid.
    
    Args:
        braille (str): The Braille string to validate.
        
    Returns:
        bool: True if the Braille input is valid, False otherwise.
    """
    if len(braille) % 6 != 0:
        return False
    for i in range(0, len(braille), 6):
        cell = braille[i:i+6]
        # Check if each Braille cell is exactly 6 characters long and contains only 'O' and '.'
        if len(cell) != 6 or not all(c in 'O.' for c in cell):
            return False
    return True

def braille_to_text(braille):
    """
    Translate Braille input to English text.
    
    Args:
        braille (str): The Braille string to translate.
        
    Returns:
        str: The English text representation of the input Braille.
    """
    if not is_valid_braille(braille):
        return "Invalid Braille"

    text = ''
    index = 0
    is_number_mode = False

    while index < len(braille):
        cell = braille[index: index + 6]

        if cell == ENGLISH_TO_BRAILLE['capital']:
            # Handle capital letter
            index += 6
            if index + 6 <= len(braille):
                next_cell = braille[index: index + 6]
                if next_cell in BRAILLE_TO_LETTER:
                    text += BRAILLE_TO_LETTER[next_cell].upper()
                else:
                    text += '?'
                index += 6
            else:
                text += '?'
        elif cell == ENGLISH_TO_BRAILLE['number']:
            # Handle number mode
            index += 6
            while index + 6 <= len(braille):
                next_cell = braille[index: index + 6]
                if next_cell in BRAILLE_TO_NUMBER:
                    text += BRAILLE_TO_NUMBER[next_cell]
                    index += 6
                else:
                    break
            is_number_mode = True
        elif cell in BRAILLE_TO_LETTER:
            text += BRAILLE_TO_LETTER[cell]
            is_number_mode = False
            index += 6
        elif cell in BRAILLE_TO_NUMBER and is_number_mode:
            text += BRAILLE_TO_NUMBER[cell]
            index += 6
        else:
            text += '?'
            index += 6

    return text

def is_braille_input(text):
    """
    Determine if the input text is Braille.
    
    Args:
        text (str): The input text to check.
        
    Returns:
        bool: True if the input is Braille, False otherwise.
    """
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

def main():
    """
    Main function to handle command-line input and execute the appropriate translation.
    """
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    input_text = ' '.join(sys.argv[1:])

    if is_braille_input(input_text):
        result = braille_to_text(input_text)
    else:
        result = text_to_braille(input_text)
    
    print(result)

if __name__ == '__main__':
    main()


