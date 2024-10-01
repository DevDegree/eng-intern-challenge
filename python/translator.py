import sys

english_to_braille_dict = {
    # Letters
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 'G': 'OOOO..', 
    'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 
    'O': 'O..OO.', 'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO', 
    'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO',
    
    # Numbers (numbers in Braille are preceded by a number sign ⠼ represented by '....O.')
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
    
    # Punctuation
    '.': '..OO.O', ',': 'O.....', '?': '..O.OO', '!': '..OOO.', ':': 'O.OO..', ';': 'O.O...', '-': '..O..O', 
    '/': '..O.O.', '<': 'O..OOO', '>': 'OO.OOO', '(': 'OO..OO', ')': 'OO.OOO', 'space': '......',
    
    # Special Symbols
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

braille_to_english_letters = {
    'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 
    'O..O..': 'E', 'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', 
    '.OO...': 'I', '.OOO..': 'J', 'O...O.': 'K', 'O.O.O.': 'L', 
    'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O', 'OOO.O.': 'P', 
    'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T', 
    'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 
    'OO.OOO': 'Y', 'O..OOO': 'Z'
}


braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', 
    '.OO...': '9', '.OOO..': '0'
}


braille_to_english_punctuation = {
    '..OO.O': '.', 'O.....': ',', '..O.OO': '?', '..OOO.': '!', 
    'O.OO..': ':', 'O.O...': ';', '..O..O': '-', '..O.O.': '/', 
    'O..OOO': '<', 'OO.OOO': '>', 'OO..OO': '(', 'OO.OOO': ')', 
    '......': ' '
}



english_to_braille_special = {
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
}

def convert_braille_to_english(braille_str):
    english_output = []
    in_number_mode = False
    is_capital = False

    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i:i+6]

        if braille_char == '......':
            english_output.append(' ')
            continue
        
        if braille_char == '.....O':
            is_capital = True
            continue

        elif braille_char == '.O...O':
            english_output.append('.')
            continue

        elif braille_char == '.O.OOO':
            in_number_mode = True
            continue

        if in_number_mode:
            english_output.append(braille_to_english_numbers.get(braille_char))
            continue
        else:
            in_number_mode = False
        
        if is_capital:
            english_output.append(braille_to_english_letters.get(braille_char).upper())
            is_capital = False
        else:
            english_output.append(braille_to_english_letters.get(braille_char).lower())

        if braille_char in braille_to_english_punctuation.values():
            english_output.append(braille_to_english_punctuation.get(braille_char))

    return ''.join(english_output)


def convert_english_to_braille(english_str):
    braille_output = []
    in_number_mode = False

    for char in english_str:
        if char == ' ':
            braille_output.append(english_to_braille_dict.get('space'))
            in_number_mode = False
            continue

        if char.isupper():
            braille_output.append(english_to_braille_dict.get('capital'))
        
        if char.isnumeric():
            if not in_number_mode:
                braille_output.append(english_to_braille_dict.get('number'))
                in_number_mode = True
            braille_output.append(english_to_braille_dict.get(char))
            continue

        if char == '.':
            braille_output.append(english_to_braille_dict.get('decimal'))
        
        braille_output.append(english_to_braille_dict.get(char.upper()))
        in_number_mode = False


    return ''.join(braille_output)

def identify_input_type(input_str):
    braille_chars = {'O' , '.'}

    if all(char in braille_chars for char in input_str):
        return "Braille"
    else:
        return "English"
    
def main():
    input_value = " ".join(sys.argv[1:])

    result = identify_input_type(input_value)

    if result == 'Braille':
        output = convert_braille_to_english(input_value)
    elif result == 'English':
        output = convert_english_to_braille(input_value)
    else:
        print("Unrecognized input.")

    print(output)

if __name__ == '__main__':
    main()
