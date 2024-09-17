import sys

# Capture command-line arguments (excluding the script name)
arguments = sys.argv[1:]  # Skipping 'python' and script name

# Dictionary mapping English letters and special symbols to Braille
english_to_braille_map = {
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
    'capital': '.....O',  # Braille prefix for capital letters
    'number': '.O.OOO',   # Braille prefix for numbers
    ' ': '......'         # Braille for space
}

# Dictionary mapping numbers to Braille
numbers_map = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...'
}

# Reverse mapping from Braille to English letters and special symbols
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}
braille_to_number_map = {v: k for k, v in numbers_map.items()}

def translate_input(input_values):
    """
    Determine if the input is Braille or English and translate it accordingly.
    
    Args:
        input_values (list): A list of strings representing Braille or English text.
    """
    # Check if input is Braille (contains only 'O' and '.' characters)
    if len(input_values) == 1 and all(char in 'O.' for char in input_values[0]):
        print(braille_to_text(input_values[0]))
    else:
        braille_translation = ''
        for word in input_values:
            braille_translation += text_to_braille(word) + '......'
        print(braille_translation.rstrip('.'))  # Remove trailing Braille space

def braille_to_text(braille_str):
    """
    Translate a Braille string to English, handling capitalization and numbers.
    
    Args:
        braille_str (str): The Braille string to be translated.
    
    Returns:
        str: The translated English text.
    """
    result = []
    # Split the Braille string into 6-character Braille blocks
    braille_blocks = [braille_str[i:i + 6] for i in range(0, len(braille_str), 6)]

    i = 0
    while i < len(braille_blocks):
        current_char = braille_blocks[i]
        if current_char == english_to_braille_map['capital']:
            # Handle capital letters
            i += 1
            result.append(braille_to_english_map.get(braille_blocks[i], '').upper())
        elif current_char == english_to_braille_map['number']:
            # Handle numbers
            i += 1
            while i < len(braille_blocks) and braille_blocks[i] != '......':
                result.append(braille_to_number_map.get(braille_blocks[i], ''))
                i += 1
        else:
            # Handle normal characters
            result.append(braille_to_english_map.get(current_char, ''))
        i += 1

    return ''.join(result)

def text_to_braille(text):
    """
    Translate an English string to Braille, handling uppercase letters and numbers.
    
    Args:
        text (str): The English string to be translated.
    
    Returns:
        str: The translated Braille string.
    """
    braille_output = []
    number_mode = False  # Flag to track if we are in number mode

    for char in text:
        if char.isdigit():
            if not number_mode:  # If not in number mode, add number prefix
                braille_output.append(english_to_braille_map['number'])
                number_mode = True
            braille_output.append(numbers_map[char])
        else:
            if number_mode:  # If switching back to letters, reset number mode
                number_mode = False
                braille_output.append('......')  # Add Braille space after numbers
            if char.islower():
                braille_output.append(english_to_braille_map[char])
            elif char.isupper():
                braille_output.append(english_to_braille_map['capital'] + english_to_braille_map[char.lower()])
            else:
                braille_output.append(english_to_braille_map.get(char, '......'))  # Handle spaces or unmapped characters
    return ''.join(braille_output)

# Start the translation process
translate_input(arguments)


