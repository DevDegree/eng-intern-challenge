# English to Braille dictionary (6 character strings)
eng_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..', 
    ' ': '......', 'capital': '.....O', 'number': '.O.OOO'
}

# Braille to English letters dictionary
braille_to_eng_letters_dict = {
    'O.....': 'a',  'O.O...': 'b',  'OO....': 'c',  'OO.O..': 'd',  'O..O..': 'e',  'OOO...': 'f',  'OOOO..': 'g',  'O.OO..': 'h', 
    '.OO...': 'i',  '.OOO..': 'j',  'O...O.': 'k',  'O.O.O.': 'l',  'OO..O.': 'm',  'OO.OO.': 'n',  'O..OO.': 'o',  'OOO.O.': 'p', 
    'OOOOO.': 'q',  'O.OOO.': 'r',  '.OO.O.': 's',  '.OOOO.': 't',  'O...OO': 'u',  'O.O.OO': 'v',  '.OOO.O': 'w',  'OO..OO': 'x', 
    'OO.OOO': 'y',  'O..OOO': 'z',  
    '......': ' ',  '.....O': 'capital',  '.O.OOO': 'number'
}

# Braille to English numbers dictionary
braille_to_eng_numbers_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 
    'OOO...': '6','OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

def text_to_braille(text):
    result = []
    is_number_sequence = False  # To track if we're in a number sequence

    for char in text:
        if char.isupper():
            result.append(eng_to_braille_dict['capital'])  # Capital indicator
            char = char.lower()

        if char.isdigit():
            if not is_number_sequence:  # Add number indicator once at the start of a number sequence
                result.append(eng_to_braille_dict['number'])
                is_number_sequence = True
        else:
            if is_number_sequence:
                is_number_sequence = False  # Reset when the sequence of digits ends

        # Add the Braille representation for the character
        result.append(eng_to_braille_dict.get(char, ''))

    return ''.join(result)

def braille_to_text(braille):
    result = []
    capital = False
    number = False
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == eng_to_braille_dict['capital']:
            capital = True
        elif symbol == eng_to_braille_dict['number']:
            number = True
        else:
            if number:
                char = braille_to_eng_numbers_dict.get(symbol, '')
                number = False
            else:
                char = braille_to_eng_letters_dict.get(symbol, '')
                if capital:
                    char = char.upper()
                    capital = False
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    
    # Check if input is Braille or English (assume English if no numbers or dots)
    if all(char in ['O', '.', ' '] for char in input_text):
        # Assume input is Braille, convert to English
        print(braille_to_text(input_text))
    else:
        # Otherwise, assume it's English, convert to Braille
        print(text_to_braille(input_text))