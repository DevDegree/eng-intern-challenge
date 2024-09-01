braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
}

reverse_braille_map = {v: k for k, v in braille_map.items()}

def translate_to_braille(text: str) -> str:
    result = []
    number_mode = False
    for char in text:
        if char.isupper():
            result.append(braille_map['capital'])
            char = char.lower()
        if char.isdigit() and not number_mode:
            result.append(braille_map['number'])
            number_mode = True
        if not char.isdigit() and number_mode:
            number_mode = False
        if char in braille_map:
            result.append(braille_map[char])
        else:
            print(f"Warning: Character '{char}' not found in Braille map.")
    return ''.join(result)

def translate_to_english(braille: str) -> str:
    result = []
    i = 0
    capital_mode = False
    number_mode = False
    
    while i < len(braille):
        chunk = braille[i:i+6]
        
        if chunk == braille_map['capital']:
            capital_mode = True
        elif chunk == braille_map['number']:
            number_mode = True
        else:
            char = reverse_braille_map.get(chunk, '')
            if capital_mode:
                char = char.upper()
                capital_mode = False
            
            if number_mode:
                if char.isdigit():
                    result.append(char)
                else:
                    number_mode = False  
                    result.append(char)  
            else:
                result.append(char)
        
        i += 6
        
    return ''.join(result)

def detect_and_translate(input_string: str) -> str:
    if len(input_string) % 6 == 0 and all(c in "O." for c in input_string):
        return translate_to_english(input_string)
    else:
        return translate_to_braille(input_string)

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    input_text = sys.argv[1]
    output = detect_and_translate(input_text)
    print(output)
