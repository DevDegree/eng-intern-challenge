import sys

# Braille mappings for lowercase, uppercase, numbers, and space
BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'space': '......',
    'capital': '.....O',
    'number': '.0.000'
}

# Reverse Braille dictionary for translating Braille to English
BRAILLE_TO_ENGLISH = {v: k for k, v in BRAILLE_DICT.items()}

# Mappings for numbers 1-9 and 0 in Braille
NUMBERS_DICT = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

def is_braille(input_string):
    # If it contains O or ., it's Braille
    return all(char in 'O.' for char in input_string.replace(' ', ''))

def translate_to_braille(english_string):
    result = []
    numbers_mode = False
    
    for char in english_string:
        if char == ' ':
            result.append(BRAILLE_DICT['space'])  # Braille for space
            numbers_mode = False  # Reset numbers mode after space
            continue
        
        if char.isdigit():
            if not numbers_mode:  # Insert number marker if not already in numbers mode
                result.append(BRAILLE_DICT['number'])
                numbers_mode = True
            result.append(BRAILLE_DICT[NUMBERS_DICT[char]])  # Convert digit to Braille
        else:
            if char.isupper():
                result.append(BRAILLE_DICT['capital'])  # Braille for capital marker
                char = char.lower()  # Handle the actual letter after the capital marker
            result.append(BRAILLE_DICT[char])  # Convert letter to Braille
            numbers_mode = False  # Reset numbers mode when processing letters
    
    return ''.join(result)  # Concatenate all Braille characters without spaces

def translate_to_english(braille_string):
    result = []
    braille_chars = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    
    capitalize_next = False
    numbers_mode = False
    
    for braille_char in braille_chars:
        if braille_char == BRAILLE_DICT['capital']:
            capitalize_next = True
            continue
        if braille_char == BRAILLE_DICT['number']:  # Correct number marker for Braille
            numbers_mode = True
            continue
        if braille_char == BRAILLE_DICT['space']:  # Space character
            result.append(' ')
            numbers_mode = False  # Reset numbers mode after space
            continue
        if braille_char in BRAILLE_TO_ENGLISH:
            letter = BRAILLE_TO_ENGLISH[braille_char]
            if numbers_mode:
                # Convert Braille letter to a number (a -> 1, b -> 2, etc.)
                if letter in NUMBERS_DICT.values():
                    result.append([k for k, v in NUMBERS_DICT.items() if v == letter][0])
            else:
                result.append(letter.upper() if capitalize_next else letter)
            capitalize_next = False  # Reset capital flag after using it

    return ''.join(result)

def main():
    # Get input from command line arguments
    input_string = ' '.join(sys.argv[1:])  # Combine all command line arguments
    
    # Determine if the input is Braille or English
    if is_braille(input_string):
        # It's Braille, translate to English
        print(translate_to_english(input_string))
    else:
        # It's English, translate to Braille
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
