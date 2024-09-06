import sys

# Create maps for english symbols to braille representations
LETTER_TO_BRAILLE = {
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
    'z': 'O..OOO'
}

NUMBER_TO_BRAILLE = {
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
}

WHITESPACE_TO_BRAILLE = {
    ' ': '......'
}

# invert maps to achieve braille to english symbol mappings
BRAILLE_TO_LETTER = {braille: symbol for symbol,braille in LETTER_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {braille: symbol for symbol,braille in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_WHITESPACE = {braille: symbol for symbol, braille in WHITESPACE_TO_BRAILLE.items()}

# create constant variables for special braille escape sequences
BRAILLE_CAPITALIZE_SEQUENCE = '.....O'
BRAILLE_NUMBER_SEQUENCE = '.O.OOO'

# HELPER FUNCTIONS
def is_braille(user_input: str) -> bool:
    '''
    Check that a string is made up of only valid braille 'chunks'
    '''
    if len(user_input) % 6 != 0:
        return False
    
    # read 6 character 'chunks' and ensure they are valid
    left, right = 0, 6
    while right <= len(user_input):
        current_chunk = user_input[left:right]

        # check if the current chunk is valid braille symbol
        if current_chunk not in BRAILLE_TO_LETTER and current_chunk not in BRAILLE_TO_NUMBER and current_chunk not in BRAILLE_TO_WHITESPACE and current_chunk != BRAILLE_CAPITALIZE_SEQUENCE and current_chunk != BRAILLE_NUMBER_SEQUENCE:
            return False
        
        left = right
        right += 6

    return True

def is_english(user_input: str) -> bool:
    '''
    Check that a string is made up of only allowable characters
    '''
    for character in user_input:
        character = character.lower()

        # check if current character is an allowable symbol
        if character not in LETTER_TO_BRAILLE and character not in NUMBER_TO_BRAILLE and character not in WHITESPACE_TO_BRAILLE:
            return False
        
    return True

def convert_english_to_braille(user_input: str) -> str:
    '''
    Takes the english string and transforms it into the braille equivalent
    '''
    result_string = ''

    NUMBER_SEQUENCE_WRITTEN = False

    for character in user_input:
        if character.lower() in LETTER_TO_BRAILLE:
            # matches all upper or lower case letters and add the capitalize sequence if needed
            if character.isupper():
                result_string += BRAILLE_CAPITALIZE_SEQUENCE

            result_string += LETTER_TO_BRAILLE[character.lower()]

        elif character in NUMBER_TO_BRAILLE:
            # match numbers and add number sequence if it is the first number following a new word
            if not NUMBER_SEQUENCE_WRITTEN:
                NUMBER_SEQUENCE_WRITTEN = True
                result_string += BRAILLE_NUMBER_SEQUENCE

            result_string += NUMBER_TO_BRAILLE[character]

        elif character in WHITESPACE_TO_BRAILLE:
            # matches the space symbol and resets the number sequence flag variable
            result_string += WHITESPACE_TO_BRAILLE[character]
            
            NUMBER_SEQUENCE_WRITTEN = False
            
    return result_string

def convert_braille_to_english(user_input: str) -> str:
    '''
    Takes a string of braille symbols and translates it to english equivalent
    '''
    result_string = ''

    capitalize_next_letter_flag = False
    currently_reading_numbers_flag = False

    left, right = 0, 6
    while right <= len(user_input):
        # get curent braille symbol
        current_chunk = user_input[left:right]

        # determine if the current symbol is an escape sequence or a num/letter and handle accordingly
        if current_chunk == BRAILLE_CAPITALIZE_SEQUENCE:
            capitalize_next_letter_flag = True

        elif current_chunk == BRAILLE_NUMBER_SEQUENCE:
            currently_reading_numbers_flag = True

        elif current_chunk in BRAILLE_TO_LETTER:
            # match valid letters and numbers, differentiating based on 'currently_reading_numbers_flag'
            if capitalize_next_letter_flag:
                result_string += BRAILLE_TO_LETTER[current_chunk].capitalize()
                capitalize_next_letter_flag = False
            elif currently_reading_numbers_flag:
                result_string += BRAILLE_TO_NUMBER[current_chunk]
            else:
                result_string += BRAILLE_TO_LETTER[current_chunk]

        elif current_chunk in BRAILLE_TO_WHITESPACE:
            # match whitespace characters
            result_string += BRAILLE_TO_WHITESPACE[current_chunk]
            currently_reading_numbers_flag = False

        left = right
        right += 6

    return result_string

def main():
    if len(sys.argv) < 2:
        exit('Correct usage is: python translator.py {YOUR STRING HERE}')

    user_input = " ".join(sys.argv[1:])

    if is_english(user_input):
        print(convert_english_to_braille(user_input))
    elif is_braille(user_input):
        print(convert_braille_to_english(user_input))

if __name__ == '__main__':
    main()