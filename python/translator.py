
import sys

braille_letter_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
}

braille_number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse maps
reverse_braille_letter_map = {v: k for k, v in braille_letter_map.items()}
reverse_braille_number_map = {v: k for k, v in braille_number_map.items()}




def is_braille(input_str):
    return set(input_str) <= set("O.")


def english_to_braille(english_str):
    braille_translation = []
    is_number = False

    for char in english_str:
        if char.isupper():
            braille_translation.append(braille_letter_map['cap'])
            char = char.lower()
        if char.isdigit():
            if not is_number:
                braille_translation.append(braille_letter_map['num'])
                is_number = True
            braille_translation.append(braille_number_map[char])
        elif char.isalpha() or char == ' ':
            is_number = False
            braille_translation.append(braille_letter_map[char])
    
    return ''.join(braille_translation)

def braille_to_english(braille_str):
    english_translation = []
    braille_chars = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    capitalize_next = False
    is_number = False

    for braille_char in braille_chars:
        if braille_char == braille_letter_map['cap']:
            capitalize_next = True
            continue
        elif braille_char == braille_letter_map['num']:
            is_number = True
            continue
        elif braille_char == braille_letter_map[' ']:
            english_translation.append(' ')
            is_number = False  
            continue
        
        if is_number:
            char = reverse_braille_number_map.get(braille_char, '?')
            if char.isdigit():
                english_translation.append(char)
            else:
                is_number = False
                english_translation.append(char)
        else:
            char = reverse_braille_letter_map.get(braille_char, '?')
            if capitalize_next:
                english_translation.append(char.upper())
                capitalize_next = False
            else:
                english_translation.append(char)

    return ''.join(english_translation)


def translate(input_str):
    
    if is_braille(input_str):
                result = braille_to_english(input_str)
    else:
                result = english_to_braille(input_str)
            
    print(result)


if __name__ == "__main__":
    input_str = ' '.join(sys.argv[1:])
    translate(input_str)