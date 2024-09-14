
import sys

# TRANSLATION MAPS
### NOTE: I did not include the mapping for '>' because it is the same as 'o' in the chart and I am not sure how to handle the conflict. An idea would be to put > if it follows/precedes a digit
### NOTE: characters that are not found in the maps are replaced by ~

# english to braille
english_to_braille_dict = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    'capital follows': '.....O',
    'decimal follows': '.O...O',
    'number follows': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    # '>': 'O..OO.', LIMITATION: > and o are the same
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

# braille (numbers) to english. include space and period for dealing with decimals and ranges of numbers
braille_numbers_to_english_dict = {value: key for key, value in english_to_braille_dict.items() if key.isdigit() or key == ' ' or key == '.'}
# braille (letters) to english
braille_letters_to_english_dict = {value: key for key, value in english_to_braille_dict.items() if not key.isdigit()}

# helper function to determine if input text is Braille
def is_text_braille(text):

    # braille text should have a length multiple of 6 and only consist of '.' and 'O' characters
    # if it only consists of '.' and 'O' characters but is not of a length multiple of 6, then it is English
    if len(text) % 6 != 0:
        return False
    
    # check if all characters are '.' or 'O'
    if all(char in {'.', 'O'} for char in text):
        return True
    else:
        return False
    
# helper function to translate text from braille to english
def translate_braille_to_english(braille_text):
    
    # check every 6 characters
    # flags for whether next character is a number or should be capitalized
    number_follows = False
    capital_follows = False
    
    english_text = ''
    # increment in steps of 6 through whole text
    for idx in range(0, len(braille_text), 6):
        
        # get current braille characters
        braille_character = braille_text[idx:idx+6]
        
        # check if next should be a number
        if braille_character == english_to_braille_dict['number follows']:
            # move on to next character
            number_follows = True
            continue
        
        # check if next should be a capital
        if braille_character == english_to_braille_dict['capital follows']:
            # move on to next character
            capital_follows = True
            continue
        
        # check if it is decimal follows
        if braille_character == english_to_braille_dict['decimal follows']:
            # append decimal and go on to next
            english_text += '.'
            continue
        
        # translate character (if valid)
        if braille_character in braille_numbers_to_english_dict or braille_character in braille_letters_to_english_dict:
            
            # not a number
            if not number_follows:
                
                # get english
                english_character = braille_letters_to_english_dict[braille_character]
                
                # check if capitalization required
                if capital_follows:
                    # capitalize
                    english_character = english_character.upper()
                    # reset variable
                    capital_follows = False
                
                # append char to text
                english_text += english_character
                
                # move on to next character
                continue
            
            else:
                
                # here: we have a number (or space)
                character = braille_numbers_to_english_dict[braille_character]
                
                # if space encountered, set number follows to false
                if character == ' ':
                    number_follows = False
                
                # append character to text
                english_text += character

                # move on to next
                continue
            
        else:
            # character not found, insert ~
            english_text += '~'
        
    return english_text

# helper function to translate text from english to braille
def translate_english_to_braille(english_text):
    
    braille_text = ''
    number_follows = False
    for idx, english_character in enumerate(english_text):
        
        # check if it's a number
        if english_character.isdigit():
            # append number follows if not done already
            if not number_follows:
                braille_text += english_to_braille_dict['number follows']
                number_follows = True
            braille_text += english_to_braille_dict[english_character]
            continue
        
        # check if it's a decimal
        if english_character == '.':
            # check if it follows and precedes a number
            # if so, it should be a decimal, and number_follows should remain true
            if idx > 0 and idx < len(english_text):
                if english_text[idx - 1].isdigit() and english_text[idx + 1].isdigit():
                    # append decimal follows
                    braille_text += english_to_braille_dict['decimal follows']
                    # append period
                    braille_text += english_to_braille_dict['.']
                    # move on to next
                    continue
        
        # here: it's not a number
        # reset number follows to false
        number_follows = False
        
        # check if it's upper case
        if english_character.isupper():
            # append upper case follows
            braille_text += english_to_braille_dict['capital follows']
            # convert to lowercase
            english_character = english_character.lower()
        
        # append character only if it's in the map
        if english_character in english_to_braille_dict:
            braille_text += english_to_braille_dict[english_character]
        else:
            # append ~~~~~~ if not found
            braille_text += '~~~~~~'
        
    return braille_text

if __name__ == '__main__':
    
    # step 0: extract arguments
    arguments = sys.argv[1:]
    
    
    # step 1: determine if arguments are in Braille or English
    # it is Braille if all the characters are valid Braille characters
    # otherwise, it is English, even if it only contain's zeros, spaces and periods
    arguments_string = ' '.join(arguments) # combine arguments with space in between
    is_braille = is_text_braille(arguments_string)

    # step 2: translate
    if is_braille:
        print(translate_braille_to_english(arguments_string))
    else:
        print(translate_english_to_braille(arguments_string))


            