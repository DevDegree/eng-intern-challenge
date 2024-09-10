import sys

# Braille mappings for letters and special case strings
braille_mapping = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', 'CAP': '.....O', 'NUM' : '.O.OOO', ' ' : '......'
}

# Braille mappings for digits
braille_nums_mapping = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Alphabet mappings for braille
alphabet_mapping = {v: k for k, v in braille_mapping.items()}
alphabet_nums_mapping = {v: k for k, v in braille_nums_mapping.items()}

def is_braille(input):
    """
    Determine if the input string is Braille.
    Braille consists of chars 'O' and '.' and with lengths that are multiples of 6.
    """
    if (len(input) % 6 != 0):
        return False
    
    for char in input:
        if char not in (".", "O"):
            return False
    return True

def braille_to_english(input):
    """
    Convert a Braille string to English text.
    """
    output = "" 
    capital_marker = False
    number_marker = False

    for i in range(0, len(input), 6):
        braille_val = input[i:i+6]

        if (braille_val == braille_mapping['CAP']):
            capital_marker = True
            continue
        elif (braille_val == braille_mapping['NUM']):
            number_marker = True
            continue
        elif (braille_val == braille_mapping[' ']):
            output += " "
            number_marker = False
            continue


        if (capital_marker):
            output += alphabet_mapping[braille_val].upper()
            capital_marker = False
        elif (number_marker):
            output += alphabet_nums_mapping[braille_val]
        else:
            output += alphabet_mapping[braille_val].lower()

    return output

def english_to_braille(input):
    """
    Convert English text to Braille
    """
    found_space = False
    output = ""

    for char in input:
        if (char.isalpha()):
            if (char.isupper()):
                output += braille_mapping['CAP']
            output += braille_mapping[char.lower()]
        
        elif (char.isdigit()):
            if (not found_space):
                output += braille_mapping['NUM']
                found_space = True
            output += braille_nums_mapping[char]

        else:
            output += braille_mapping[' ']
            found_space = False

    return output

def main():
    #Parse input
    input_str = ' '.join(sys.argv[1:])

    if (is_braille(input_str)):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

#Call main function
if __name__ == "__main__":
    main()