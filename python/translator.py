from enum import Enum
import sys

class BrailleControlType(Enum):
    CAPITAL = 'CAPITAL'
    DECIMAL = 'DECIMAL'
    NUMBER = 'NUMBER'

class Language(Enum):
    BRAILLE = 'BRAILLE'
    ENGLISH = 'ENGLISH'

char_to_braille = {
    'alphabet': {
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
    },
    'numbers': {
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
    },
    'symbols': {
        '.': '..OO.O',
        ',': '..O...',
        '?': '..O.OO',
        '!': '..OOO.',
        ':': '..OO..',
        ';': '..O.O.',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        '(': 'O.O..O',
        ')': '.O.OO.', 
        ' ': '......',
    },
    'controls': {
        BrailleControlType.NUMBER: '.O.OOO',
        BrailleControlType.CAPITAL: '.....O',
        BrailleControlType.DECIMAL: '.O...O',
    }
}

braille_to_alphabet = { braille: char for char, braille in char_to_braille['alphabet'].items() }
braille_to_number = { braille: char for char, braille in char_to_braille['numbers'].items() }
braille_to_symbol = { braille: char for char, braille in char_to_braille['symbols'].items() }

braille_to_control = { braille: control for control, braille in char_to_braille['controls'].items() }


def guess_language(input_string: str) -> Language:
    """
    To be Braille, we must have the following:
    1. The string must have length multiple of 6
    2. The string must only contain 'O' and '.' characters.

    We say these heuristics are also sufficient for us to assume it is Braille.

    Later, if during translation parsing Braille fails, then we will treat the string as if it were English instead.

    Returns True for Braille to English, False for English to Braille.
    """
    return Language.BRAILLE if len(input_string) % 6 == 0 and all(char in 'O.' for char in input_string) else Language.ENGLISH


def translate_braille(input_string: str):
    """
    Greedily loops through each chunk of 6 characters, and tries to parse as Braille.

    If parsing fails, then we raise ValueError.
    """

    chunk_idx = 0
    control = None

    translation = ""

    while chunk_idx * 6 < len(input_string):
        # get current chunk of 6 characters
        chunk = input_string[chunk_idx*6:(chunk_idx+1) * 6]

        try:
            # First handle all control cases
            if control == BrailleControlType.NUMBER:
                # If we are reading numbers and see space, stop reading numbers
                if chunk == char_to_braille['symbols'][' ']:
                    control = None
                    translation += ' '
                # If we are reading numbers and see a decimal follows, add the decimal
                # but continue reading numbers
                elif chunk == char_to_braille['controls'][BrailleControlType.DECIMAL]:
                    translation += '.'
                else:
                    translation += braille_to_number[chunk]
                
            elif control == BrailleControlType.CAPITAL:
                translation += braille_to_alphabet[chunk].upper()
                control = None
                
            else:
                # If no control flag is set, try getting chunk as each type of char 

                # First we see if it is a control (not decimal follows, which should only
                # appear while reading numbers)
                if chunk in braille_to_control and braille_to_control[chunk] != BrailleControlType.DECIMAL:
                    # Update control but don't append anything to translation
                    control = braille_to_control[chunk]
                    chunk_idx += 1
                    continue
                elif chunk in braille_to_alphabet:
                    translation += braille_to_alphabet[chunk]
                else:
                    translation += braille_to_symbol[chunk]

                control = None
            chunk_idx += 1
        except KeyError:
            raise ValueError(f"Unparseable Braille string at chunk {chunk_idx}: {chunk}. Control {control}.")
        
    
    return translation



def translate_english(input_string: str):
    """
    Converts each english character to Braille, adding controls when necessary.

    Assuming input_string contains only valid characters, this function should never fail.
    """
    chars = list(input_string)
    is_num_sequence = False

    braille = ''

    for char in chars:
        # Condition on the type of char seen
        if char.isdigit():
            # Add number control before the sequence of numbers
            if not is_num_sequence:
                braille += char_to_braille['controls'][BrailleControlType.NUMBER]
                is_num_sequence = True

            braille += char_to_braille['numbers'][char]

        # Checking for decimals
        elif is_num_sequence and char == '.':
            braille += char_to_braille['controls'][BrailleControlType.DECIMAL]

        elif char == ' ':
            # Whenever space is seen, any existing sequence of numbers ends
            is_num_sequence = False
            braille += char_to_braille['symbols'][' ']

        elif char.isalpha():
            # Add capital control whenever char is capitalised
            if char.isupper():
                braille += char_to_braille['controls'][BrailleControlType.CAPITAL]

            braille += char_to_braille['alphabet'][char.lower()]
        else: 
            # must be a symbol
            braille += char_to_braille['symbols'][char]

    
    return braille



def main():
    input_string = " ".join(sys.argv[1:])

    if not input_string:
        print("Usage: python translator.py <word1> [word2] [word3] ...")

    language = guess_language(input_string)
    if language == Language.BRAILLE:
        try: 
            translation = translate_braille(input_string)
        except ValueError:
            # If translating braille returns an error, then the language was not braille
            # So translate english instead
            translation = translate_english(input_string)
    else:
        translation = translate_english(input_string)
    
    print(translation)

if __name__ == "__main__":
    main()