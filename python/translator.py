import sys

def read_from_command_line():
    # read input as string
    input_str = " ".join(sys.argv[1:])
    return input_str

def write_to_command_line(output_str):
    # print the output string
    print(output_str)

def detect_braille_or_str(input_str):
    # check if english or braille, only check the first 6 characters
    # because there must be a '.' which is not in english (in this exercise of course)
    first_chars = input_str[0:6]
    braille_check = False

    for c in first_chars:
        if c == '.':
            braille_check = True
        
    return braille_check

# Braille/English dictionary
braille_to_english_mappings = [
    ('O.....', 'a'), ('O.O...', 'b'), ('OO....', 'c'), ('OO.O..', 'd'), ('O..O..', 'e'),
    ('OOO...', 'f'), ('OOOO..', 'g'), ('O.OO..', 'h'), ('.OO...', 'i'), ('.OOO..', 'j'),
    ('O...O.', 'k'), ('O.O.O.', 'l'), ('OO..O.', 'm'), ('OO.OO.', 'n'), ('O..OO.', 'o'),
    ('OOO.O.', 'p'), ('OOOOO.', 'q'), ('O.OOO.', 'r'), ('.OO.O.', 's'), ('.OOOO.', 't'),
    ('O...OO', 'u'), ('O.O.OO', 'v'), ('.OOO.O', 'w'), ('OO..OO', 'x'), ('OO.OOO', 'y'), ('O..OOO', 'z'),
    ('......', ' '),
    ('.....O', 'cap'),
    ('.O.OOO', 'num')
]


# Extend the list for numbers
numbers_mappings = [
    ('O.....', '1'), ('O.O...', '2'), ('OO....', '3'), ('OO.O..', '4'), ('O..O..', '5'),
    ('OOO...', '6'), ('OOOO..', '7'), ('O.OO..', '8'), ('.OO...', '9'), ('.OOO..', '0'), ('......', ' ')
]

def get_braille_for_char(char, num=False):
    # getting braille for a given char/command
    if num:
        mappings = numbers_mappings
    else:
        mappings = braille_to_english_mappings

    for braille, english in mappings:
        if english == char:
            return braille
    return None

def get_char_for_braille(braille, num=False):
    # getting char/command for given braille
    if num:
        mappings = numbers_mappings
    else:
        mappings = braille_to_english_mappings
    
    for braille_code, english in mappings:
        if braille_code == braille:
            return english
    return None


def convert_braille_to_english(input_str):
    result = []
    i = 0
    while i < len(input_str):
        braille_char = input_str[i:i+6]
        if braille_char == get_braille_for_char('cap'):
            next_char = input_str[i+6:i+12]
            result.append(get_char_for_braille(next_char).upper()) 
            i += 12
        elif braille_char == get_braille_for_char('num'):
            i += 6
            next_char = input_str[i:i+6]
            while (i < len(input_str) and next_char != get_braille_for_char(' ')):
                next_char = input_str[i:i+6]
                result.append(get_char_for_braille(next_char, num=True)) 
                i += 6
        else:
            result.append(get_char_for_braille(braille_char))
            i += 6
    return ''.join(result)



def convert_english_to_braille(input_str):
    result = []
    num_check = False
    for char in input_str:
        if num_check:
            if not (char.isdigit()):
                num_check = False
        
        if char.isupper():
            result.append(get_braille_for_char('cap')) 
            result.append(get_braille_for_char(char.lower()))
        elif char.isdigit() or num_check == True:
            if num_check == False:
                num_check = True
                result.append(get_braille_for_char('num'))
                result.append(get_braille_for_char(char, num=True))
            else:
                result.append(get_braille_for_char(char, num=True))

        else:
            result.append(get_braille_for_char(char))
    return "".join(result)



if __name__ == "__main__":
    input_str = read_from_command_line()

    braille_check = detect_braille_or_str(input_str)

    if braille_check:
        output_str = convert_braille_to_english(input_str)
    
    else:
        output_str = convert_english_to_braille(input_str)

    write_to_command_line(output_str)