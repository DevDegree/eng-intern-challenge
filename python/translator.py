import sys
import textwrap


# Two dictionaries:
# eng_to_braille maps english characters to braille
# braille_to_eng maps braille characters to a list of possible english characters
# braille_to_eng is to be initialized in generate_dictionaries()
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

def generate_dictionaries() -> None: 
    """
    Initializes the braille_to_eng dicitionary.
    """
    for character, braille in eng_to_braille.items():
        if braille in braille_to_eng.keys():
            braille_to_eng[braille].append(character) # add to the list if the braille symbol is there
        else:
            braille_to_eng[braille] = [character] # otherwise create a mapping


def translate(input: str) -> str:
    """
    Translates the input.
    If at any point the translator detects that the input is not braille,
    it translates from english to braille.
    Otherwise, it proceeds with translating to english.
    """

    # Check if the input contains any non-braille characters
    for c in input:
        if c != 'O' and c != '.':
            return translate_english_to_braille(input)
    
    # Check if the input divides 6. If not, this is not valid braille.
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
        except KeyError: # Invalid braille
            return translate_english_to_braille(input)

        # Handles all the special braille characters
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
    """
    Function to translate from english to braille
    """
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