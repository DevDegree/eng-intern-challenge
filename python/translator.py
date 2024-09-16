import sys

def main():
    '''
    Main functions to validate command line input and check whether to 
    translate from Braille to English or English to Braille
    '''
    
    # Get the argument from the command line
    if len(sys.argv) < 2:
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
    Checks if the input string is Braille containing only 'O' and '.'
    Input: String
    Output: Boolean: True if the input is Braille, else, returns False
    '''
    
    return all(char in 'O.' for char in string)


def translate_english_to_braille(english_string):
    '''
    Translate English to Braille
    Input: String in English
    Output: Braille translation of the input string
    '''
    braille_output = []
    is_number = False
    
    for char in english_string:
        if char.isupper():
            braille_output.append(capital_prefix)
            braille_output.append(braille_alphabet[char.lower()])
            is_number = False 
        elif char.isdigit():
            if not is_number:
                braille_output.append(number_prefix)
                is_number = True
            braille_output.append(braille_numbers[char])
        else:
            braille_output.append(braille_alphabet.get(char, ''))
            is_number = False
    return ''.join(braille_output)


def translate_braille_to_english(braille_string):
    '''
    Translate Braille to English
    Input: String in Braille
    Output: English translation of the input string
    '''
    english_output = []
    i = 0
    while i < len(braille_string):
        if braille_string[i:i+6] == capital_prefix:
            i += 6
            letter = get_letter_from_braille(braille_string[i:i+6]).upper()
        elif braille_string[i:i+6] == number_prefix:
            i += 6
            letter = get_number_from_braille(braille_string[i:i+6])
        elif braille_string[i:i+6] == '......':
            letter = ' '
        else:
            letter = get_letter_from_braille(braille_string[i:i+6])
        
        english_output.append(letter)
        i += 6
    
    return ''.join(english_output)


def get_letter_from_braille(braille_char):
    '''
    Get the English letter from a Braille Character
    Input: 6-character Braille string
    Output: corresponding English letter or an empty string if not found
    '''
    for letter, braille in braille_alphabet.items():
        if braille == braille_char:
            return letter
    return ''

def get_number_from_braille(braille_char):
    '''
    Get the number corresponding to a Braille character
    Input: 6-character Braille string
    Output: Corresponding number as a string or an empty string if not found
    '''
    for number, braille in braille_numbers.items():
        if braille == braille_char:
            return number
    return ''

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