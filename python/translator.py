import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO', '.': '..OO.O', ',': '..O...',
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', '-': '....OO', '/': '.O..O.', '<': '.OO..O' ,
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(eng):
    result = []
    is_number_mode = False
    
    for char in eng:
        if char.isdigit():
            if not is_number_mode:
                result.append(braille_dict['number'])
                is_number_mode = True
        else:
            if is_number_mode:
                is_number_mode = False
        
        if char.isupper():
            result.append(braille_dict['capital'])
            char = char.lower()
        
        if char in braille_dict:
            result.append(braille_dict[char])
        else:
            # Handle unknown characters gracefully
            result.append('......')  # Default to space for unknown characters
    
    return ''.join(result)

def translate_to_eng(braille):
    result = []
    i = 0
    is_capital = False
    is_number = False

    while i < len(braille):
        symbol = braille[i:i+6]

        if symbol == braille_dict['capital']:
            is_capital = True
            i += 6
            continue
        
        if symbol == braille_dict['number']:
            is_number = True
            i += 6
            continue
        
        if symbol in inverse_braille_dict:
            char = inverse_braille_dict[symbol]
            if is_capital:
                char = char.upper()
                is_capital = False
            
            if is_number:
                if char.isdigit():
                    result.append(char)
                else:
                    # Non-digit character after number indicator
                    is_number = False
                    result.append(' ')
            else:
                if char.isdigit() and not is_number:
                    # Map digits back to corresponding letters if no number mode is active
                    letter = chr(ord('a') + int(char) - 1)  # '1' -> 'a', '2' -> 'b', etc.
                    result.append(letter)
                else:
                    result.append(char)
        else:
            result.append('?')  # Handle unknown symbols
        
        i += 6
    
    return ''.join(result).strip()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py [text]")
        return
    
    input_text = ' '.join(sys.argv[1:])
    
    # Check if the input is Braille or English
    if all(c in "O." for c in input_text):
        # If the input contains only 'O' and '.', assume it's Braille and translate to English
        output = translate_to_eng(input_text)
    else:
        # Otherwise, assume it's English and translate to Braille
        output = translate_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()