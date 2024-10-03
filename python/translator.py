import sys

# mapping braille alphabet 
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OO.O..', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.O',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOOOO', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  # space
    'capital': '.....O',  
    'decimal': '.O...O',  
    'number': '.O.OOO',   
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# reverse the mapping
english_letters = {v: k for k, v in braille_alphabet.items() if k.isalpha()}
# english_digit = {v: k for k, v in braille_alphabet.items() if k.isdigit()}
english_alphabet = {v: k for k, v in braille_alphabet.items()}

# check if input is braille
def is_braille(text):
    return all(c in 'O.' for c in text)

# translate Braille to English
def braille_to_english(text):
    result = []
    i = 0
    number_mode = False  

    while i < len(text):
        braille_char = text[i:i + 6]  

        if braille_char == braille_alphabet['capital']:
            # if capital letter, restrict next char to letters only
            i += 6
            braille_char = text[i:i + 6]
            result.append(english_letters.get(braille_char, '').upper()) 
            number_mode = False 


        elif braille_char == braille_alphabet['number']:
            # enter number mode
            number_mode = True

        else:
            if number_mode:
                if braille_char == '......':  
                    # space resets number mode
                    number_mode = False
                    result.append(' ')
                else:
                    # translate numbers
                    result.append(english_alphabet.get(braille_char, ' '))
            else:
                # translate letters
                result.append(english_letters.get(braille_char, ' '))
        i += 6
    return ''.join(result)

# translate English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_alphabet['number'])
                number_mode = True

        if char.isupper():
            result.append(braille_alphabet['capital'])
            char = char.lower()

        result.append(braille_alphabet.get(char, '......'))  
        # default to space for unknown characters
    return ''.join(result)

# define a translation function
def translate(text):
    if is_braille(text):
        return braille_to_english(text)
    else:
        return english_to_braille(text)

# call the function from command line
if __name__ == '__main__':
    input_text = ' '.join(sys.argv[1:])
    print(translate(input_text))
