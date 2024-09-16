import sys

# Braille dictionary (alphabet -> braille)
english_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',  # Capitalization lead
    'num': '.O.OOO',  # New number lead
}

# Reverse mapping of Braille to English
braille_to_english_dict = {b: e for e, b in english_to_braille_dict.items()}

number_to_braille_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OOO...': '4', 'O..O..': '5',
    'OO.O..': '6', 'OOO.O.': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

braille_to_number_dict = {b: e for e, b in number_to_braille_dict.items()}


def is_braille(input_string : str) -> bool:
    # Check if the input is in Braille or not
    for char in input_string:
        if char != 'O' and char != '.' and char != ' ':
            return False
    return True


def braille_to_english(braille_string: str ) -> str:
    english_output = []
    capitalize_next = False
    number_mode = False
    i = 0
    
    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        i += 6
        
        # Handle special cases and update the state
        handled, capitalize_next, number_mode = handle_special_braille(braille_char, english_output, capitalize_next, number_mode)
        if handled:
            continue
        
        # Convert braille to the appropriate character (number or letter)
        char = convert_braille_to_char(braille_char, number_mode)
        
        # If character was detected, check for capitalization and append to output
        if char:
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english_output.append(char)
    
    return ''.join(english_output)


def handle_special_braille(braille_char: str, english_output: str, capitalize_next: bool, number_mode: bool) -> tuple:
    if braille_char == english_to_braille_dict['cap']:
        return True, True, number_mode  # Set capitalize_next to True
    elif braille_char == english_to_braille_dict['num']:
        return True, capitalize_next, True  # Set number_mode to True
    elif braille_char == english_to_braille_dict[' ']:
        english_output.append(' ')
        return True, capitalize_next, False  # Set number_mode to False after space
    return False, capitalize_next, number_mode


def convert_braille_to_char(braille_char: str, number_mode: False) -> str:
    if number_mode:
        char = number_to_braille_dict.get(braille_char, '')
        if not char:
            number_mode = False  # Exit number mode if invalid number character
        return char
    else:
        return braille_to_english_dict.get(braille_char, '')


def english_to_braille(english_string: str) -> str:
    braille_output = []
    number_mode = False
    
    for char in english_string:

        if char.isupper():
            braille_output.append(english_to_braille_dict['cap'])
            char = char.lower()
        
        if char.isdigit() and not number_mode:
            braille_output.append(english_to_braille_dict['num'])  # Add number marker once before digits
            number_mode = True
        
        if not char.isdigit():
            number_mode = False  # Exit number mode after digits
        
        if char in english_to_braille_dict:
            braille_output.append(english_to_braille_dict[char])
        elif char in braille_to_number_dict:
            braille_output.append(braille_to_number_dict[char]) 
        else:
            braille_output.append(english_to_braille_dict[' '])  # Treat any non-letter, non-number as space
    
    return ''.join(braille_output)



def translate(input_string : str) -> str:
    if is_braille(input_string):
        return braille_to_english(input_string)
    else:
        return english_to_braille(input_string)





if __name__ == '__main__':
    input_string = " ".join(sys.argv[1:])
    print(translate(input_string))
