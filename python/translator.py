import sys 

# Initialize the alphanumeric dictionary
alphanumeric_to_braille_map = {
    # Letters (a-z)
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..','f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',

    # Numbers (0-9)
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..','6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..',

    # Special (capital following, number following, space, decimal)
    'capital': '.....O', 'number': '.O.OOO', ' ': '......'
}

# Initialize the braille dictionaries
braille_to_english_map = {}
braille_to_number_map = {}

# Populate the braille dictionaries
for k, v in alphanumeric_to_braille_map.items():
    if k.isdigit():
        braille_to_number_map[v] = k
    else:
        braille_to_english_map[v] = k

def is_braille(s):
    return all(c in 'O.' for c in s) and len(s) % 6 == 0

def braille_to_english(input):
    english = []

    scenario = None

    for i in range(0, len(input), 6):
        chunk = input[i:i+6]

        english_mapping = braille_to_english_map[chunk]

        if english_mapping == 'capital' or english_mapping == 'number':
            scenario = english_mapping
            continue

        if scenario == 'number' and english_mapping != ' ':
            english.append(braille_to_number_map[chunk])

        elif scenario == 'capital':
            english.append(english_mapping.upper())
            scenario = None

        else:
            if english_mapping == ' ':
                english.append(' ')
                scenario = None
            else:
                english.append(english_mapping)

    return ''.join(english)

def english_to_braille(input):
    braille = []

    number_check = False

    for char in input:
        if char.isupper():
            braille.append(alphanumeric_to_braille_map['capital'])
            char = char.lower()

        elif char.isnumeric():
            if not number_check:
                braille.append(alphanumeric_to_braille_map['number'])
                number_check = True

        elif char == ' ':
            number_check = False

        braille.append(alphanumeric_to_braille_map[char])


    return ''.join(braille)

def main():
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])

        if is_braille(input_string):
            result = braille_to_english(input_string)
        else:
            result = english_to_braille(input_string)

        print(result)

if __name__ == "__main__":
    main()