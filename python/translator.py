import sys

braille_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': 'O..OO.', '>': '.OO..O', '(': '.O.OO.', ')': 'O.O..O',
}

number_dict = {
    '.OOO..': '0', 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9',
}

def translate_braille(text):
    result = ''
    number_mode = False 

    if '.' not in text:
     
        for char in text:
            if char == ' ':
                number_mode = False 
            elif char.isdigit() and not number_mode:
                result += ".O.OOO"  
                number_mode = True
            elif char.isalpha() and char.isupper():
                result += '.....O'  

            result += braille_dict[char.upper()]  

    else:
        message_chunks = [text[i:i+6] for i in range(0, len(text), 6)]
        capitalize_next = False

        for chunk in message_chunks:
            if chunk == '.....O': 
                capitalize_next = True
            elif chunk == '.O.OOO':
                number_mode = True
            elif chunk == '......': 
                result += ' '
                number_mode = False  
            elif number_mode and chunk in number_dict:
                result += number_dict[chunk]
            else:
               
                if chunk in braille_dict.values():
                    char = list(braille_dict.keys())[list(braille_dict.values()).index(chunk)]
                    result += char.upper() if capitalize_next else char.lower()
                    capitalize_next = False

    return result

if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    translated_text = translate_braille(input_text)
    print(translated_text)


