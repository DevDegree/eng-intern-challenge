import sys

# Capture command-line arguments (excluding the script name)
arguments = sys.argv[1:]  # Skipping 'python' & script name, the first two arguments

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
    'capital_follows': '.....O',  # Braille prefix for capital letters
    'decimal_follows': '.O...O',  # Braille prefix for decimal points
    'number_follows': '.O.OOO',   # Braille prefix for numbers
    ' ': '......'  # Braille for space
}

# Dictionary mapping numbers to Braille
number_to_braille_map = {
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
braille_to_english_map = {value: key for key, value in english_to_braille_map.items()}

# Reverse mapping from Braille to numbers
braille_to_number_map = {value: key for key, value in number_to_braille_map.items()}

def process_translation(input_values):
    """
    Process the input values and determine if they are Braille or English for translation.
    If input is Braille, translate it to English. If input is English, translate to Braille.
    
    Args:
        input_values (list): A list of strings representing either Braille or English.
    """
    # Check if the input is Braille (only '.' and 'O' characters)
    if len(input_values) == 1 and all(character in '.O' for character in input_values[0]):
        print(braille_to_english(input_values[0]))
    else:
        braille_result = ''
        for english_character in input_values:
            braille_result += english_to_braille(english_character) + '......'  # Braille space between words
        print(braille_result[:-6])  # Remove the trailing space

def braille_to_english(braille_value):
    """
    Translates a Braille string into its English equivalent, handling capitalization and numbers.
    
    Args:
        braille_value (str): A string of Braille characters to be translated.
        
    Returns:
        str: The English translation of the Braille string.
    """
    translated_result = ''
    # Split the Braille string into 6-dot Braille characters
    braille_parts = [braille_value[i:i + 6] for i in range(0, len(braille_value), 6)]
    
    i = 0
    while i < len(braille_parts):
        braille_character = braille_to_english_map.get(braille_parts[i])
        if braille_character == 'capital_follows':  # Handle capitalization
            translated_result += braille_to_english_map.get(braille_parts[i + 1], '').toUpperCase()
            i += 1  # Skip the next character as it's part of the capitalized letter
        elif braille_character == 'number_follows':  # Handle numbers
            for j in range(i + 1, len(braille_parts)):
                if braille_parts[j] == '......':  # End of the number sequence
                    break
                number_character = braille_to_number_map.get(braille_parts[j], '')
                translated_result += number_character
                i = j
        else:
            translated_result += braille_to_english_map.get(braille_parts[i], '')  # Add normal characters
        i += 1
    return translated_result

def english_to_braille(english_value):
    """
    Translates an English string into Braille, handling both lowercase and uppercase characters as well as numbers.
    
    Args:
        english_value (str): A string of English characters to be translated.
        
    Returns:
        str: The Braille translation of the English string.
    """
    braille_result = ''
    english_characters = list(english_value)
    
    for i, character in enumerate(english_characters):
        if character.isdigit():  # Handle numbers
            if i == 0 or not english_characters[i - 1].isdigit():
                braille_result += english_to_braille_map['number_follows']  # Add number prefix
            braille_result += number_to_braille_map[character]  # Translate number
            if i < len(english_characters) - 1 and not english_characters[i + 1].isdigit():
                braille_result += '......'  # Add Braille space after numbers
        elif character.islower():  # Translate lowercase letters
            braille_result += english_to_braille_map[character]
        else:  # Handle uppercase letters
            braille_result += english_to_braille_map['capital_follows'] + english_to_braille_map[character.lower()]
    
    return braille_result

# Start the translation process using the command-line arguments
process_translation(arguments)

