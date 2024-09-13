import sys

braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'cap': '.....O',
    'num': '.O.OOO'
}

braille_to_english_dict = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', 
    '......': ' ', 
    '.....O': 'cap',
    '.O.OOO': 'num'
}

braille_to_digit_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}


def is_braille(input_str):
    return all(c in ['O', '.'] for c in input_str)

def english_to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_dict['num'])
                number_mode = True
            braille_output.append(braille_dict[char])
        else:
            number_mode = False
            if char.isupper():
                braille_output.append(braille_dict['cap'])
                braille_output.append(braille_dict[char.lower()])
            else:
                braille_output.append(braille_dict.get(char, '......'))
    
    return ''.join(braille_output)

def braille_to_english(braille_text):
    english_output = []
    i = 0
    number_mode = False
    
    while i < len(braille_text):
        chunk = braille_text[i:i+6]
        
        if chunk == '.....O': 
            i += 6
            chunk = braille_text[i:i+6]
            char = braille_to_english_dict.get(chunk, '')
            english_output.append(char.upper())
        elif chunk == '.O.OOO': 
            number_mode = True
            i += 6
            continue  
        else:
            if number_mode:
                char = braille_to_digit_dict.get(chunk, '')
                if char: 
                    english_output.append(char)
                else:  
                    number_mode = False
                    char = braille_to_english_dict.get(chunk, '')
                    english_output.append(char)
            else:
                char = braille_to_english_dict.get(chunk, '')
                english_output.append(char)
        
        i += 6
    
    return ''.join(english_output)

def main():
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()
