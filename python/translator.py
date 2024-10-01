import sys


BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
}

BRAILLE_NUMS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 
}


CAPITAL_FOLLOWS = '.....O'
# DECIMAL_FOLLOWS = '...O.O'
NUMBER_FOLLOWS = '.O.OOO'
BRAILLE_BYTE_SIZE = 6 # braille characters needed to encode an english character

def __init__(self, input_string):
    self.input = input_string


def isBraille(input_string):
    # Check if the string is in Braille format
    if all(char in ['O', '.'] for char in input_string):
        return True
    else:
        return False


# Translate from English to Braille
def translateToBraille(input_string):

    output_string = ''
    number_follows_flag = False

    for char in input_string:
        # if Uppercase
        if char.isupper():
            output_string += CAPITAL_FOLLOWS + BRAILLE_DICT[char.lower()]
        # if Number
        elif char.isdigit():
            if number_follows_flag:
                output_string += BRAILLE_NUMS[char]
            else:
                output_string += NUMBER_FOLLOWS + BRAILLE_NUMS[char]
                number_follows_flag = True
        # if Space
        elif char == ' ':
            number_follows_flag = False # reset flag becuase of space character
            output_string += BRAILLE_DICT[char]
        # if Lowercase and symbols
        else:
            output_string += BRAILLE_DICT[char]

    return output_string


# Translate from Braille to English
def translateToEnglish(input_string):
    
    # Reversing the key, value pairs for faster lookup from braille to english
    reversed_braille_dict = {v: k for k, v in BRAILLE_DICT.items()}
    reversed_braille_nums = {v: k for k, v in BRAILLE_NUMS.items()}

    capital_follows_flag = False
    number_follows_flag = False

    output_string = ''

    for i in range(0, len(input_string), BRAILLE_BYTE_SIZE):
        braille_chunk = input_string[i:i + BRAILLE_BYTE_SIZE]

        # detect flags
        if braille_chunk == CAPITAL_FOLLOWS:
            capital_follows_flag = True
        elif braille_chunk == NUMBER_FOLLOWS:
            number_follows_flag = True
        
        # if there's a spcace, remove flags and append ' ' to output
        elif braille_chunk == BRAILLE_DICT[' ']:
            capital_follows_flag = False
            number_follows_flag = False
            output_string += ' '
        
        # decode braille character
        else:
            if number_follows_flag:
                output_string += reversed_braille_nums[braille_chunk]
            elif capital_follows_flag:
                output_string += reversed_braille_dict[braille_chunk].upper()
                capital_follows_flag = False
            else:
                output_string += reversed_braille_dict[braille_chunk]

    return output_string


def main():
    input_string = ' '.join(sys.argv[1:])

    translated_string = translateToEnglish(input_string) if isBraille(input_string) \
        else translateToBraille(input_string)
    
    print(translated_string)


if __name__ == "__main__":
    main()