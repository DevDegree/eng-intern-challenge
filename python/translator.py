#Author: Kazi Badrul Arif


import sys

# Braille dictionary with punctuation
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO', 'decimal': '.0...0', '.': '..00.0',
    ',': '..0...', '?': '..0.00', '!': '..000.', ':': '..00..', ';': '..0.0.',
    '-': '....00', '/': '.0..0.', '<': '.00..0', '>': '0..00.', '(': '0.0..0',
    ')': '.0.00.'
}


braille_num_dict = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

# braille_num_dict = {
#     '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
#     '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
# }


english_dict = {v: k for k, v in braille_dict.items()}

def detect_input_type(input_str):
    
    if all(c in 'O.' for c in input_str):
        return 'braille'
    else:
        return 'english'

def braille_to_english(braille_str):
    translated_text = []
    braille_chars = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    # print(braille_chars)

    is_capital = False
    is_number = False

    for braille_char in braille_chars:
        letter = english_dict.get(braille_char, '')
        if braille_char == braille_dict['capital']:
            is_capital = True

        elif braille_char == braille_dict['number']:
            # print(braille_char + " " + str(braille_chars.index(braille_char))  + " Number\n")
            is_number = True

        elif braille_char == braille_dict[' ']:
            translated_text.append(' ')
            is_number = False
            
        else:
            if is_capital:
                # print(letter)
                # here it is converting the overwritten dictionary numbers to letters
                # if the number has not overwritten the alphabet we do not need to use the second dictionary 
                if (letter < 'k'):
                    letter = braille_num_dict[letter]
                letter = letter.upper()
                is_capital = False
            elif not is_capital and not is_number:
                if (letter < 'k'):
                    letter = braille_num_dict[letter]
                
            if is_number and letter.isdigit():
                translated_text.append(letter)
            elif is_number:
                is_number = False
                translated_text.append(letter)
            else:
                translated_text.append(letter)

        # print("Appended: " + letter)

    return ''.join(translated_text).strip()

def english_to_braille(english_str):
    translated_text = []
    is_number = False

    # print(english_str)
    for char in english_str:
        # print("Character: " + char)
        # braille_char = ''
        if char.isupper():
            translated_text.append(braille_dict['capital'])
            char = char.lower()
        elif char.isdigit():
            if not is_number:
                translated_text.append(braille_dict['number'])
                is_number = True
         
        else:
            is_number = False

        if char.isspace():
            translated_text.append(braille_dict[' '])
            # print("The space is translated to: " + braille_dict[' '])
        else:
            # translated_text.append(braille_dict.get(char, ''))
            translated_text.append(braille_dict[char])
        # print("Appended: " + char + " " + translated_text[-1])

    return ''.join(translated_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        return
    
    input_str = ' '.join(sys.argv[1:])
    input_type = detect_input_type(input_str)
    # print(f"Input string: {input_str}")
    # print(f"Detected input type: {input_type}")
    
    if input_type == 'braille':
        output = braille_to_english(input_str)
    else:
        output = english_to_braille(input_str)
    
    print(output)  

if __name__ == "__main__":
    main()


