# CONSTANTS
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

BRAILLE_CAPITALIZE_SEQUENCE = '00000.'
BRAILLE_NUMBER_SEQUENCE = '0.0...'

CAPITALIZE = 'CAPITALIZE'
NUMBER = 'NUMBER'

SPECIAL_TO_BRAILLE = {
    CAPITALIZE: '.....O',
    NUMBER: '.O.OOO'
}

BRAILLE_TO_LETTER = {braille: symbol for symbol,braille in LETTER_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {braille: symbol for symbol,braille in NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_WHITESPACE = {braille: symbol for symbol, braille in WHITESPACE_TO_BRAILLE.items()}
BRAILLE_TO_SPECIAL = {braille: symbol for symbol,braille in SPECIAL_TO_BRAILLE.items()}

VALID_SYMBOLS = LETTER_TO_BRAILLE | NUMBER_TO_BRAILLE | WHITESPACE_TO_BRAILLE
VALID_BRAILLE = BRAILLE_TO_LETTER | BRAILLE_TO_NUMBER | BRAILLE_TO_WHITESPACE | BRAILLE_TO_SPECIAL

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

        if current_chunk not in VALID_BRAILLE:
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
        if character not in VALID_SYMBOLS:
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
            # matches all upper or lower case letters
            if character.isupper():
                result_string += BRAILLE_CAPITALIZE_SEQUENCE

            result_string += LETTER_TO_BRAILLE[character.lower()]

        elif character in NUMBER_TO_BRAILLE:
            if not NUMBER_SEQUENCE_WRITTEN:
                NUMBER_SEQUENCE_WRITTEN = True
                result_string += BRAILLE_NUMBER_SEQUENCE

            result_string += NUMBER_TO_BRAILLE[character]

        elif character in WHITESPACE_TO_BRAILLE:
            result_string += WHITESPACE_TO_BRAILLE[character]
            
            NUMBER_SEQUENCE_WRITTEN = False
            
    return result_string

def convert_braille_to_english(user_input: str) -> str:
    '''
    Takes a string of braille symbols and translates it to english equivalent
    '''
    result_string = ''

    NEXT_LETTER_CAPITAL = False
    CURRENTLY_READING_NUMBERS = False

    left, right = 0, 6

    while right <= len(user_input):
        current_chunk = user_input[left:right]

        if current_chunk == BRAILLE_CAPITALIZE_SEQUENCE:
            NEXT_LETTER_CAPITAL = True
        elif current_chunk == BRAILLE_NUMBER_SEQUENCE:
            CURRENTLY_READING_NUMBERS = True
        elif current_chunk in BRAILLE_TO_LETTER:
            if NEXT_LETTER_CAPITAL:
                result_string += BRAILLE_TO_LETTER[current_chunk].capitalize()
                NEXT_LETTER_CAPITAL = False
            elif CURRENTLY_READING_NUMBERS:
                result_string += BRAILLE_TO_NUMBER[current_chunk]
            else:
                result_string += BRAILLE_TO_LETTER[current_chunk]

        elif current_chunk in BRAILLE_TO_WHITESPACE:
            result_string += BRAILLE_TO_WHITESPACE[current_chunk]

            CURRENTLY_READING_NUMBERS = False

        left = right
        right += 6

    return result_string

def main():
    user_input = input().strip()

    if is_english(user_input):
        val =  convert_english_to_braille(user_input)
    elif is_braille(user_input):
        val = convert_braille_to_english(user_input)
    else:
        print('Invalid input!!')

    print(val)

if __name__ == '__main__':
    main()