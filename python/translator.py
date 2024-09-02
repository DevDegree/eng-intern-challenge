import sys

# Braille mappings
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', " ": '......', 'capital': '.....O', 'number': '.O.OOO'
}

braille_number_map = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    'number': '.O...O'
}

# Reverse map for Braille to English
reverse_braille_map = {v: k for k, v in braille_map.items()}
reverse_braille_number_map = {v: k for k, v in braille_number_map.items()}

#print(reverse_braille_map)
#print(reverse_braille_number_map)

def is_braille(input_string):
    """Determine if input is Braille based on presence of 'O' and '.' only."""
    return all(c in 'O.' for c in input_string)

def english_to_braille(text):
    """Convert English text to Braille."""
    result = []
    is_number = False
    
    for char in text:
        if char.isdigit() and not is_number:
            result.append(braille_number_map['number'])
            is_number = True
        
        if char.isdigit() and is_number:
            result.append(braille_number_map.get(char))
            is_number = True

        if char.isalpha() and is_number:
            result.append('......')  # add a space to exit number mode
            is_number = False
            
        if char.isupper():
            result.append(braille_map['capital'])
            char = char.lower()
        
        result.append(braille_map.get(char, ''))
    
    return ''.join(result)

def braille_to_english(braille_string):
    output = []
    i = 0
    is_number = False
    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        #print(braille_char)
        if braille_char == '.....O':
            output.append('capital')
            i += 6
        elif braille_char == '.O.OOO':
            is_number = True
            i += 6
        else:
            char = reverse_braille_map.get(braille_char, '')
            if output and output[-1] == 'capital':
                char = char.upper()
                output.pop()
            elif is_number and char.isalpha():
                char = str(ord(char) - ord('a') + 1)  # Convert a-j to 1-0
                if char == '10':
                    char = '0'
            elif char == '':
                is_number = False
            output.append(char)
            i += 6
    return ''.join(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python braille_translator.py 'text to translate '")
        return
    
    input_text = sys.argv[1]
    
    if is_braille(input_text):
        translated_text = braille_to_english(input_text)
    else:
        translated_text = english_to_braille(input_text)
    
    print(translated_text)

if __name__ == "__main__":
    main()
