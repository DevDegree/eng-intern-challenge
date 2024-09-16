import sys

def main():
    '''
    Main functions to validate command line input and check whether to 
    translate from Braille to English or English to Braille
    '''
    
    # Get the argument from the command line
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)
        
    # Get input strings and join strings on spaces to handle strings with spaces
    input_string = ' '.join(sys.argv[1:])
    
    
    # Check if input is Braille or English
    if is_braille(input_string):
        print(translate_braille_to_english(input_string))
    else:
        print(translate_english_to_braille(input_string))
    
    
    
def is_braille(string):
    '''
    Checks if the input string is Braille containing only '0' and '.'
    Input: String
    Output: Boolean: True if the input is Braille, else, returns False
    '''
    
    return all(char in '0.' for char in string)


def translate_english_to_braille(english_string):
    '''
    Translate English to Braille
    Input: String in English
    Output: Braille translation of the input string
    '''
    braille_output = []
    for char in english_string:
        if char.isupper():
            braille_output.append(capital_prefix)
            braille_output.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            braille_output.append(number_prefix)
            braille_output.append(braille_numbers[char])
        else:
            braille_output.append(braille_alphabet[char])
    return ''.join(braille_output)


def translate_braille_to_english(braille_string):
    '''
    Translate Braille to English
    Input: String in Braille
    Output: English translation of the input string
    '''
    return

# Braille mapping for lowercase English letters
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Braille mapping for numbers
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Capital and number indicators
capital_prefix = '.....O'
number_prefix = '.O.OOO'


if __name__ == "__main__":
    main()