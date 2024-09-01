import sys

BRAILLE_IDENTIFIERS = [
    ('CAPITAL', '.....O'), ('DECIMAL', '.O..OO'), ('NUMBER', '.O.OOO')
]

BRAILLE_NUMBERS = [
    ('1', 'O.....'), ('2', 'O.O...'), ('3', 'OO....'), ('4', 'OO.O..'), 
    ('5', 'O..O..'), ('6', 'OOO...'), ('7', 'OOOO..'), ('8', 'O.OO..'),
    ('9', '.OO...'), ('0', '.OOO..')
]

BRAILLE_ALPHABET = [
    ('A', 'O.....'), ('B', 'O.O...'), ('C', 'OO....'), ('D', 'OO.O..'), 
    ('E', 'O..O..'), ('F', 'OOO...'), ('G', 'OOOO..'), ('H', 'O.OO..'),
    ('I', '.OO...'), ('J', '.OOO..'), ('K', 'O...O.'), ('L', 'O.O.O.'),
    ('M', 'OO..O.'), ('N', 'OO.OO.'), ('O', 'O..OO.'), ('P', 'OOO.O.'),
    ('Q', 'OOOOO.'), ('R', 'O.OOO.'), ('S', '.OO.O.'), ('T', '.OOOO.'),
    ('U', 'O...OO'), ('V', 'O.O.OO'), ('W', '.OOO.O'), ('X', 'OO..OO'),
    ('Y', 'OO.OOO'), ('Z', 'O..OOO'), ('.', '.O.O.O'), (',', '.O....'), 
    ('?', '.O..O.'), ('!', '.OO.OO'), (':', '.OO..O'), (';', '.O.O..'),
    ('-', '..O..O'), ('/', '..O.O.'), ('<', '.O...O'), ('>', '...O.O'), 
    ('(', '..OO.O'), (')', '..OOO.'), (' ', '......')
]

def main():
    # process input into a string
    _input = " ".join([sys.argv[i] for i in range(1, len(sys.argv))])

    if not is_braille(_input):
        print(convert_to_braille(_input))
    else:
        print(convert_to_english(_input))

    return    

# determine if input is braille
def is_braille(_input):
    if len(_input) % 6 != 0:
        return False
    
    braille_chars =  {'O', '.'}
    for i in _input:
        if i not in braille_chars:
            return False
    
    return True

# convert braille into English
def convert_to_english(_input):
    output = ""

    # make dict. for braille mappings
    braille_to_number = {braille: number for number, braille in BRAILLE_NUMBERS}
    braille_to_identifier = {braille: sign for sign, braille in BRAILLE_IDENTIFIERS}
    braille_to_letter = {braille: letter for letter, braille in BRAILLE_ALPHABET}
    number, capital = False, False

    for char in range(0, len(_input), 6):
        braille = _input[char:char+6] # current braille

        # check if braille is an identifier
        if braille in braille_to_identifier.keys():
            if braille_to_identifier[braille] == 'NUMBER':
                number = True
            elif braille_to_identifier[braille] == 'CAPITAL':
                capital = True
            elif braille_to_identifier[braille] == 'DECIMAL':
                output += '.'
            elif braille_to_identifier[braille] == ' ':
                number =  False
            continue

        if number:
            output += braille_to_number[braille]
        else:
            letter = braille_to_letter[braille].lower() if not capital else braille_to_letter[braille]
            output += letter
            if capital:
                capital = False

    return output

# convert English into braille
def convert_to_braille(_input):
    output = ""

    # make dict. for braille mappings
    alphabet_to_braille = {letter: braille for letter, braille in BRAILLE_ALPHABET}
    number_to_braille = {number: braille for number, braille in BRAILLE_NUMBERS}
    identifiers_to_braille = {sign: braille for sign, braille in BRAILLE_IDENTIFIERS}
    is_number = False  

    for char in _input:
        if char == '.':
            output += identifiers_to_braille['DECIMAL']
        elif char.isdigit():
            if not is_number:
                output += identifiers_to_braille['NUMBER']
                is_number = True
            output += number_to_braille[char]
        else:
            if is_number:
                is_number = False
            if char.isupper():
                output += identifiers_to_braille['CAPITAL']
            output += alphabet_to_braille[char.upper()]
            
    return output

if "__main__":
    main()

