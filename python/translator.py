import sys

# lets first map all the alphabets to their respective braille codes
braille_mapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 'capital': '.....O', 'number': '.O.OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..O.OO', ',': '..O...', '?': '..OO.O', '!': '..OOO.', ':': '..OO..',
    ';': 'O.OO..', '-': '....O.', '/': '.O..O.', '<': '.O..OO', '>': 'OO..O.',
    '(': '.O.OO.', ')': '.O.OOO' 
}

def text_to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_mapping['number'])
                number_mode = True
            braille_output.append(braille_mapping[char])
        elif char.isalpha():
            if number_mode:
                braille_output.append('......')
                number_mode = False
            
            if char.isupper():
                braille_output.append(braille_mapping['capital']) 
                char = char.lower()
            braille_output.append(braille_mapping[char])
        elif char in braille_mapping:
            braille_output.append(braille_mapping[char])
            number_mode = False

    return ''.join(braille_output)



def braille_to_english(braille):
    out = []
    i = 0
    number_mode = False
    
    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == braille_mapping['capital']:
            i += 6 
            next_symbol = braille[i:i+6]
            for key, value in braille_mapping.items():
                if value == next_symbol:
                    char = key.upper() 
                    out.append(char)
                    break
        
        elif symbol == braille_mapping['number']:
            number_mode = True 
        
        elif symbol in braille_mapping.values():
            for key, value in braille_mapping.items():
                if value == symbol:
                    char = key
                    if number_mode and char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
                        number_conversion = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                                             'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
                        out.append(number_conversion[char])
                    else:
                        out.append(char)
                    if char == ' ':
                        number_mode = False
                    break
        
        i += 6
    return ''.join(out)


def main():
    input_str = ' '.join(sys.argv[1:])

    if all(c in 'Oo.' for c in input_str):
        print(braille_to_english(input_str))
    else: 
        print(text_to_braille(input_str))

if __name__ == "__main__":
    main()