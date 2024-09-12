import sys

from pprint import pprint
import textwrap

eng_to_braille = {
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
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    'space': '......'
}
braille_to_eng = {}

def generate_dictionaries():
    
    for character, braille in eng_to_braille.items():
        if braille in braille_to_eng.keys():
            braille_to_eng[braille].append(character)
        else:
            braille_to_eng[braille] = [character]

    # Debugging
    # len_eng_to_braille = O
    # for value in braille_to_eng.values():
    #     print(value)
    #     len_eng_to_braille += len(value)

    # assert len(eng_to_braille) == len_eng_to_braille


def translate(input: str) -> str:
    """
    Check if the input contains any non-braille characters
    Check if the input length divides 6
    If both conditions pass, check if the characters are valid braille
    If there's a decimal
    """

    # Check if the input contains any non-braille characters
    for c in input:
        if c != 'O' and c != '.':
            return translate_english_to_braille(input)
    
    # Check if the input divides 6
    if len(input) % 6 != 0:
        return translate_english_to_braille(input)
    
    # Split the potential braille characters and ensure they are valid
    braille_symbols = textwrap.wrap(input, 6)

    answer = ''
    is_number = False
    is_capital = True

    for braille_symbol in braille_symbols:
        try:
            translation_list = braille_to_eng[braille_symbol]
        except KeyError: # Invalid 
            return translate_english_to_braille(input)

        if translation_list[0] == 'capital follows':
            is_capital = True
        
        elif translation_list[0] == 'space':
            is_number = False
            answer += ' '

        elif translation_list[0] == 'decimal follows' or translation_list[0] == '.':
            answer += '.'

        elif translation_list[0] == 'number follows':
            is_number = True

        elif is_number:
            if len(translation_list) == 2:
                answer += translation_list[1]
            else:
                # Is this right?
                answer += translation_list[0]

        elif is_capital:
            answer += translation_list[0].upper()
            is_capital = False
        
        else:
            answer += translation_list[0]
    
    return answer


def translate_english_to_braille(input: str) -> str:
    is_number = False
    answer = ''
    for idx, char in enumerate(input):
        # If the character is an uppercase
        if char.isupper():
            answer += eng_to_braille['capital follows']
            answer += eng_to_braille[char.lower()]
        
        # if the character is a number
        elif char in {'1','2','3','4','5','6','7','8','9','0'}:
            if not is_number:
                is_number = True
                answer += eng_to_braille['number follows']
            
            answer += eng_to_braille[char]
        
        elif char == ' ':
            is_number = False
            answer += eng_to_braille['space']
        
        elif char == '.':
            try:
                if input[idx + 1] in {'1','2','3','4','5','6','7','8','9','0'}:
                    answer += eng_to_braille['decimal follows']
                else:
                    answer += eng_to_braille['.']

            except IndexError:
                answer += eng_to_braille['.']

        else:
            answer += eng_to_braille[char]

    return answer

args = sys.argv[1:]
input = " ".join(args)
generate_dictionaries()

print(translate(input))