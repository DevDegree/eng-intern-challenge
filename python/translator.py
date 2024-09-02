
import sys

# mapping of english alphabet to braille
eng_to_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O...',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'CAP': '.....O', 'NUM': '.O.OOO',
}

num_to_alpha = {
    '1' : 'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '0':'j'
}

# reversed mappings
braille_to_eng_dict = {val: key for key, val in eng_to_braille_dict.items()}
alpha_to_num = {val: key for key, val in num_to_alpha.items()}


def convert_eng_to_braille(input):
    """
    Converts english input to braille and returns braille.

    input: str
    """
    converted_str = ''
    num_flag = False

    for char in input:
        if char.isupper(): # check for capital letter
            converted_str += eng_to_braille_dict['CAP']
            converted_str += eng_to_braille_dict[char.lower()]
        elif char.isnumeric() and not num_flag: # check for number
            num_flag = True
            converted_str += eng_to_braille_dict['NUM']
            converted_str += eng_to_braille_dict[num_to_alpha[char]]
        elif char == ' ':
            num_flag = False
            converted_str += eng_to_braille_dict[char]
        elif num_flag:
            converted_str += eng_to_braille_dict[num_to_alpha[char]]
        elif char.lower() in eng_to_braille_dict:
            converted_str += eng_to_braille_dict[char]
        else:
            converted_str += 'OOOOOO'  # unknown character
    return converted_str

def convert_braille_to_eng(input):
    """
    Converts braille input to english and returns english.

    input: str
    """
    converted_str = ''
    cap_flag = False
    num_flag = False
    
    for index in range(0, len(input), 6):
        braille_char = input[index:index+6]
        if braille_char == braille_to_eng_dict['CAP']:
            cap_flag = True
        elif braille_char == braille_to_eng_dict['NUM']:
            num_flag = True
        elif braille_char == braille_to_eng_dict[' ']:
            num_flag = False
        elif braille_char in braille_to_eng_dict:
            if cap_flag:
                converted_str += braille_to_eng_dict[braille_char].upper()
                cap_flag = False
            elif num_flag: # first get alpha equivalent, then convert to number
                converted_str += alpha_to_num[braille_to_eng_dict[braille_char]]
            else:
                converted_str += braille_to_eng_dict[braille_char]
        else:
            converted_str += '?'  # unknown char
    return converted_str

def main():
    
    input_text = sys.argv[1:]
    input_text = ' '.join(input_text)
    
    # Check if input is braille or english
    if all(letters in "O." for letters in input_text):
        output_text = convert_braille_to_eng(input_text)
    else:
        output_text = convert_eng_to_braille(input_text)
    
    print(output_text)

if __name__ == "__main__":
    main()
