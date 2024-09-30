import sys

def create_maps():
    braille_map = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......',
        'CAPITAL': '.....O',  'NUMBER': '.O.OOO'
    }
    return braille_map, {v: k for k, v in braille_map.items()}

def to_braille(text, braille_map):
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(braille_map['CAPITAL'])
            char = char.lower()
            
        if char.isdigit():
            if not number_mode:
                result.append(braille_map['NUMBER'])
                number_mode = True
            char = chr(ord(char) - ord('0') + ord('a')-1) # number handling
        elif number_mode and not char.isdigit():
            number_mode = False
        
        result.append(braille_map.get(char, ''))  # Use '' for unknown characters
                       
    return ''.join(result)

def to_english(text, reverse_map):
    result = []
    i = 0
    capital_next = False
    number_mode = False
    
    while i < len(text):
        char = text[i:i+6]
        if reverse_map[char] == 'CAPITAL':
            capital_next = True
        elif reverse_map[char] == 'NUMBER':
            number_mode = True
        else:
            if char in reverse_map:
                letter = reverse_map[char]
                if number_mode:
                    if reverse_map[char] == ' ':
                        number_mode = False
                    else:
                        digit = str(ord(letter) - ord('a')+1)
                        result.append(digit)
                if not number_mode:
                    if capital_next:
                        letter = letter.upper()
                        capital_next = False
                    result.append(letter)
            else:
                result.append('')
        i += 6
    
    return ''.join(result)

def main():
    input_string = ' '.join(sys.argv[1:])
    
    braille_map, reverse_map = create_maps()
    
    is_braille = all(c in 'O.' for c in input_string)
    
    if is_braille:
        result = to_english(input_string, reverse_map)
    else:
        result = to_braille(input_string, braille_map)
    
    print(result)

if __name__ == "__main__":
    # could add extra handling here for invalid inputs, help string, etc
    main()