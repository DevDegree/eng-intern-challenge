import sys


braille_map = {

    "CAPITAL": ".....O",  # Capital follows symbol
    "DECIMAL": ".O...O", # Decimal follows symbol
    "NUMBER": ".O.OOO", # Number follows symbol

    # Numbers (Braille uses the letters a-j with the number sign for digits O-9)
    '1': "O.....",  # Same as 'a'
    '2': "O.O...",  # Same as 'b'
    '3': "OO....",  # Same as 'c'
    '4': "OO.O..",  # Same as 'd'
    '5': "O..O..",  # Same as 'e'
    '6': "OOO...",  # Same as 'f'
    '7': "OOOO..",  # Same as 'g'
    '8': "O.OO..",  # Same as 'h'
    '9': ".OO...",  # Same as 'i'
    '0': ".OOO..",  # Same as 'j'

     # Common punctuation
    '.': "..OO.O",  # Period
    ',': "..O...",  # Comma
    ';': "..O.O.",  # Semicolon
    ':': "..OO..",  # Colon
    '?': "..O.OO",  # Question mark
    '!': "..OOO.",  # Exclamation mark
    '/': ".O..O.",  # Black slash
    '<': ".OO..O",  # Left caret
    '>': "O..OO.",  # Right caret
    '-': "....OO",  # Hyphen
    '(': ".OO.OO",  # Left parenthesis
    ' ': "......",  # Space
    ')': ".OO.OO",  # Right parenthesis (same as left)

    # Letters
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    
}

# Reverse mapping for decoding Braille to English
reverse_braille_map = {v: k for k, v in braille_map.items()}

def eng_to_braille(text):
    result = []
    is_num = False

    for char in text:
        if char == ' ':
            is_num = False

        if char.isdigit() and not is_num:
            result.append(braille_map["NUMBER"])
            is_num = True
            result.append(braille_map[char])
        elif char.isdigit():
            result.append(braille_map[char])
        elif char.isupper():
            result.append(braille_map["CAPITAL"])
            result.append(braille_map[char.lower()])
        elif char in braille_map:
            result.append(braille_map[char])
        else:
            break
    return ''.join(result)

def braille_to_eng(text):
    result = []
    words = [text[i:i+6] for i in range(0, len(text), 6)]
    is_number_mode = False
    is_capital_mode = False
    is_decimal_mode = False

    for braille_char in words:
        if braille_char == braille_map["NUMBER"]:
            is_number_mode = True
        elif braille_char == braille_map["CAPITAL"]:
            is_capital_mode = True
        elif braille_char ==braille_map["DECIMAL"]:
            is_decimal_mode = True
        elif braille_char == braille_map[' ']:
            result.append(' ')  # Add space
        elif braille_char in reverse_braille_map:
            symbol = reverse_braille_map[braille_char]

            if is_number_mode:
                if symbol.isalpha():
                    symbol = str(ord(symbol) - ord('a') + 1)  # Convert letter to number (a=1, b=2, etc.)
                is_number_mode = False  # Reset after converting a number

            if is_decimal_mode:
                if symbol.isalpha():
                    symbol = str(ord(symbol) - ord('a') + 1)  # Convert letter to number (a=1, b=2, etc.)
                is_number_mode = False  # Reset after converting a number


            if is_capital_mode:
                symbol = symbol.upper()
                is_capital_mode = False  # Reset after converting a capital

            result.append(symbol)
        else:
            result.append('?')  # Handle unknown characters
    return ''.join(result)

def translator(input_text):
    if all(c in 'O.' for c in input_text.replace(' ', '')):  # If input looks like Braille
        return braille_to_eng(input_text)
    else:
        return eng_to_braille(input_text)

    
# # Test the translator
if __name__ == "__main__":
    
    text = ' '.join(sys.argv[1:])
    print(translator(text))


