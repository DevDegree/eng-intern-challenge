import sys

# Maping lowercase letters and space to their braille equivalents
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# Numbers map
number_map = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Capital letter and number indicator
capital_ind = '.....O'
number_ind = '.O.OOO'

# Reverse braille_map
reverse_braille_map = {}
for k, v in braille_map.items():
    reverse_braille_map[v] = k

# Reverse number_map
reverse_number_map = {}
for k, v in number_map.items():
    reverse_number_map[v] = k

# Determine if the string is braille or not
def is_braille(s):
    for c in s:
        if c not in "O.":
            return False
    return True


def english_to_braille(text):
    translation = []
    number = False # Keeps track to process numbers or not
    
    for char in text:
        if char.isdigit():
            if not number:
                translation.append(number_ind)
                number = True
            translation.append(number_map[char])
        elif char.isalpha():
            if number:
                number = False  # Reset boolean 
            if char.isupper():
                translation.append(capital_ind)
            translation.append(braille_map[char.lower()])
        elif char == ' ':
            translation.append(braille_map[' '])
            number = False  # Reset boolean

    return ''.join(translation)

def braille_to_english(braille):
    translation = []
    capital = False # Indicates whether the next letter should be uppercase
    number = False # Keeps track to process numbers or not
    
    i = 0 # Initializes index

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_ind:
            capital = True
        elif symbol == number_ind:
            number = True
        else:
            if number:
                translation.append(reverse_number_map[symbol])
                number = False
            elif capital:
                translation.append(reverse_braille_map[symbol].upper())
                capital = False
            else:
                translation.append(reverse_braille_map[symbol])
        i += 6 # Advances index by 6 for the next 6-character Braille symbol
    
    return ''.join(translation)

def main():
    # Combine arguments into a single string
    input_string = ' '.join(sys.argv[1:])
    
    # Determine if the input is Braille or English
    if is_braille(input_string):
        # Translate to English
        print(braille_to_english(input_string)) 
    else:
        # Translate to Braille
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()
