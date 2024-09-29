import sys

# Combined map to Braille for alphabets and symbols
to_combined_braille = {
    # Letters
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    # Punctuation and symbols
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

# Map to Number Braille 
to_number_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reversed for mapping to English
to_combined_english = {v: k for k, v in to_combined_braille.items()}
to_number_english = {v: k for k, v in to_number_braille.items()}

# Special prefixes
capital_prefix = '.....O'
number_prefix = '.O.OOO'


# Function to translate Braille to English
def braille_to_english(braille_input):
    translated_text = ''
    capital = False
    number_mode = False

    for i in range(0, len(braille_input), 6):
        braille = braille_input[i:i+6]
        translated_braille = ''

        # Check for special prefixes
        if braille == capital_prefix:
            capital = True
        elif braille == number_prefix:
            number_mode = True

        #translate to English depending on mode
        if number_mode:
            if braille == '......':  # Reset number mode on space
                translated_braille = ' '
                number_mode = False
            else:
                #get number
                translated_braille = to_number_english.get(braille, '')
        else:
            #get letter or symbol
            translated_braille = to_combined_english.get(braille, '')

        if capital and translated_braille.isalpha():
            #capitalize one following letter
            translated_braille = translated_braille.upper()
            capital = False

        #add to translated result
        translated_text += translated_braille

    return translated_text


# Function to translate English to Braille
def english_to_braille(english_input):
    translated_text = ''
    is_num = False

    for eng in english_input:
        if eng.isupper():
            #add one capital prefix per upper character
            translated_text += capital_prefix
            eng = eng.lower()

        if eng.isdigit():
            if not is_num:
                #add number prefix in beginning of number sequence
                translated_text += number_prefix
                is_num = True       
            #add number braille
            translated_text += to_number_braille.get(eng, '')
        elif is_num:
            #not digit but is_num = True
            #sequence of number end, add space braille to indicate 
            if eng != ' ':
                #only need to manually add space when it's not space
                translated_text += to_combined_braille.get(' ')
            is_num = False  # Reset number mode
            translated_text += to_combined_braille.get(eng, '')           
        else:
            #not digit,is_num = False
            translated_text += to_combined_braille.get(eng, '')
              
    return translated_text


# Function to detect if input is Braille or not
def is_braille_input(input_text):
    # Check if input length is a multiple of 6 and contains only 'O' and '.'
    if len(input_text) % 6 == 0 and all(char in {'O', '.'} for char in input_text):
        return True
    return False


# Main function to handle input and call appropriate translation function
def translator(input_text):
    if not input_text:
        return "Input is empty."
    if is_braille_input(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)


# Entry point to handle command-line input
if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(translator(input_text))
    else:
        print("Please provide an input string for translation.")
