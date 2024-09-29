import sys

# Dictionary for Braille and txt translation
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..','i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.','u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'CAP': '.....O', 'DEC': '.O...O', 'NUM': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..O.OO', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# Reverse lookup for Braille to text mapping
reverse_braille_dict = dict((value, key) for key, value in braille_dict.items())

def translate(input_string):
    '''
    Translate between normal text and Braille based on input
    Param:
    input_string: String that will be translated
    Return:
    Translated String
    '''
    existing_text = any(char not in '0.' for char in input_string)
    translated_output = []

    # If there is input text, translate it to Braille
    if existing_text:
        # Track markers i.e. 'NUM' or 'CAP'
        next_maker = ""
        for char in input_string:
            if char.isupper() and next_marker != 'CAP':    # Capitals
                translated_output.append(braille_dict['CAP'])
                next_marker = 'CAP'
            if char.isdigit() and next_marker != 'NUM':    # Number
                translated_output.append(braille_dict['NUM'])
            if char.isspace():                             # Space (reset markers)
                next_marker = ""
            translated_output.append(braille_dict[char.lower()])
    #Input is braille, translate to text
    else:
        for i in range(0, len(input_string), 6):
            curr_segment = input_string[i:i+6]
            trans = reverse_braille_dict.get(curr_segment, '')

            if trans == 'CAP':
                next_marker = 'CAP'
            elif trans = 'NUM':
                next_marker = 'NUM'
            else:
                translated_output.append(trans)
            
            next_marker = ""
    return ''.join(transleted_output)

def main():
    print(translate(translation_input))

if __name__ == "main":
    main()
