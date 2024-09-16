import sys

# Braille mappings for letters and numbers
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

# Number mappings: digits to letters 'a' to 'j'
number_map = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}

# Add number mappings to the braille_map
for digit, letter in number_map.items():
    braille_map[digit] = braille_map[letter]

# Reverse mapping: Braille to English
braille_to_english_map = {v: k for k, v in braille_map.items()}
braille_to_english_map[braille_map['cap']] = 'cap'
braille_to_english_map[braille_map['num']] = 'num'

def is_braille(text):
    """Check if the input text is in Braille."""
    stripped_text = text.replace(' ', '')
    return all(char in 'O.' for char in stripped_text)

def translate_braille_to_english(braille_text):
    """Translate Braille text to English."""
    braille_cells = braille_text.split(' ')
    result = ''
    capitalize = False
    number_mode = False
    
    for cell in braille_cells:
        if cell == braille_map['cap']:
            capitalize = True
        elif cell == braille_map['num']:
            number_mode = True
        elif cell == braille_map[' ']:
            result += ' '
            number_mode = False
        else:
            char = braille_to_english_map.get(cell, '?')
            if char == 'cap':
                capitalize = True
            elif char == 'num':
                number_mode = True
            else:
                if number_mode:
                    result += next((d for d, l in number_map.items() if l == char), '?')
                    number_mode = False
                else:
                    result += char.upper() if capitalize else char
                    capitalize = False
    return result

def translate_english_to_braille(text):
    """Translate English text to Braille."""
    result = ''
    number_mode = False
    
    for char in text:
        if char == ' ':
            result += braille_map[' ']
            number_mode = False
        elif char.isupper():
            result += braille_map['cap'] + braille_map[char.lower()]
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result += braille_map['num']
                number_mode = True
            result += braille_map[char]
        else:
            result += braille_map.get(char, '')
            number_mode = False
    return result

def main():
    if len(sys.argv) < 2:
        print("Please provide input text.")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        output = translate_braille_to_english(input_string)
    else:
        output = translate_english_to_braille(input_string)
    
    print(output)

if __name__ == '__main__':
    main()
