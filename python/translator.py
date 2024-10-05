
import sys

# Braille symbols
english_to_braile_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO'
}

# Numbers in Braille
numbers_to_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mapping for decoding Braille back to English
braille_to_english_dict = {v: k for k, v in english_to_braile_dict.items()}
braille_to_numbers_dict = {v: k for k, v in numbers_to_braille_dict.items()}

def parse_input():
    if len(sys.argv) < 3:
        print("Usage: python translator.py <mode> <text>")
        sys.exit(1)
    
    # Either "english" or "braille"
    mode = sys.argv[1].lower()
    # Concatenate all arguments as input text
    text = ' '.join(sys.argv[2:]) 
    return mode, text

def english_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isupper():
            is_number = False
            result.append(english_to_braile_dict['capital'])
            char = char.lower()
        if char.isdigit():
            if not is_number:
                result.append(english_to_braile_dict['number'])
                is_number = True
            result.append(numbers_to_braille_dict[char])
        else:
            is_number = False
            # Default to space for unknown symbols
            result.append(english_to_braile_dict.get(char, '......'))  
    return ''.join(result)

def braille_to_english(braille_text):
    result = []
    # Split into 6-character chunks
    chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]  
    is_number = False
    is_capital = False
    
    for char in chars:
        if char == english_to_braile_dict['number']:
            is_number = True
            continue
        elif char == english_to_braile_dict['capital']:
            is_capital = True
            continue
        elif char == '......':
            is_number = False

        if is_number:
            # Handle unknown numbers
            result.append(braille_to_numbers_dict.get(char, '?'))
        else:
            # Handle unknown letters
            letter = braille_to_english_dict.get(char, '?')  
            if is_capital:
                result.append(letter.upper())
                is_capital = False
            else:
                result.append(letter)
    
    return ''.join(result)

def main():
    mode, text = parse_input()

    if mode == 'english':
        print(english_to_braille(text))
    elif mode == 'braille':
        print(braille_to_english(text))
    else:
        print("Invalid mode. Use 'english' or 'braille'.")

if __name__ == "__main__":
    main()
