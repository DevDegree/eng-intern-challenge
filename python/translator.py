import sys
 
#Braille characters to english alphabets
BRAILLE_CHARS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

#Braille characters for numbers
BRAILLE_NUMS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

#Braille characters for capital, number and space signs
CAPITAL_SIGN = '.....O'
NUMBER_SIGN = '.O.OOO'
SPACE_SIGN = '......'

# Reverse mappings for decoding Braille to letters and digits
BRAILLE_TO_LETTER = {v: k for k, v in BRAILLE_CHARS.items()}
BRAILLE_TO_DIGIT = {v: k for k, v in BRAILLE_NUMS.items()}

# This method translates Braille text to english
def braille_to_english(braille_text):
    # Output string to collect translated English text
    result = ''
    # Flag to indicate if we are processing digits
    number_mode = False
    # Flag to indicate if the next letter should be capitalized
    capital_next = False

    # Split the input Braille text into chunks of 6 characters each
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    
    for symbol in braille_chars:
        
        if symbol == SPACE_SIGN:
            # Add space to output and reset modes
            result += ' '
            number_mode = False
            capital_next = False
            continue

        if symbol == CAPITAL_SIGN:
            # Set flag to capitalize next letter
            capital_next = True
            continue

        if symbol == NUMBER_SIGN:
            # Enter number mode for digits
            number_mode = True
            # Continue to next Braille symbol
            continue

        if number_mode:
            # Translate Braille digits to English
            char = BRAILLE_TO_DIGIT.get(symbol)
            if char:
                result += char
            else:
                pass
            continue 
        # Translate Braille letters to English
        char = BRAILLE_TO_LETTER.get(symbol)
        if char:
            if capital_next:
                # Apply capitalization to the character if needed
                char = char.upper()
                capital_next = False
            result += char
        else:
            pass 

    return result

#This method translates english text to braille characters
def english_to_braille(text):

    result = []
    number_mode = False

    for char in text:
        if char == ' ':
            # Add Braille space sign for space characters
            result.append(SPACE_SIGN)
            number_mode = False
        elif char.isdigit():
            # Enter number mode if a digit is encountered
            if not number_mode:
                result.append(NUMBER_SIGN)
                number_mode = True
            result.append(BRAILLE_NUMS[char])
        elif char.isalpha():
            # Exit number mode when encountering a letter
            if number_mode:
                number_mode = False
            # Add capital sign if the letter is uppercase
            if char.isupper():
                result.append(CAPITAL_SIGN)
            result.append(BRAILLE_CHARS[char.lower()])
    
    return ''.join(result)

#This method determines if the input text is Braille or not
def is_braille(text):
     # Check if all characters are Braille symbols and length is a multiple of 6
    return all(c in ('O', '.') for c in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print('Usage: python translator.py <text>')
        sys.exit(1)
    
    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        # Convert Braille to English if input is Braille
        result_text = braille_to_english(input_text)
    else:
        # Convert English to Braille if input is not Braille
        result_text = english_to_braille(input_text)

    print(result_text)

if __name__ == '__main__':
    main()
