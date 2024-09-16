import sys

# mapping lowercase letters and space to their Braille equivalents
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# braille dictionary
braille_number_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital_ind = '.....O'
number_ind = '.O.OOO'

# reversing the braille_dict
reversed_braille_dict = {v: k for k, v in braille_dict.items()}

# reverse number_map
reversed_braille_number_dict = {v: k for k, v in braille_number_dict.items()}

# determining whether the string is Braille 
def is_braille(s):
    return all(c in "O." for c in s) and len(s) % 6 == 0

# converting english to braille 
def to_braille(text):
    translation = []
    is_number = False  
    
    for char in text:
        if char.isdigit():
            if not is_number:
                translation.append(number_ind)
                is_number = True
            translation.append(braille_number_dict[char])
        elif char.isalpha():
            if is_number:
                is_number = False  
            if char.isupper():
                translation.append(capital_ind)
            translation.append(braille_dict[char.lower()])
        elif char == ' ':
            translation.append(braille_dict[' '])
            is_number = False  

    return ''.join(translation)

# converting braille to english 
def to_english(braille):
    translation = []
    should_be_capital = False  
    is_number = False  
    
    i = 0  

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_ind:
            should_be_capital = True
        elif symbol == number_ind:
            is_number = True
        else:
            if is_number:
                translation.append(reversed_braille_number_dict.get(symbol, ''))
                is_number = False
            elif should_be_capital:
                translation.append(reversed_braille_number_dict.get(symbol, '').upper())
                should_be_capital = False
            else:
                translation.append(reversed_braille_number_dict.get(symbol, ''))
        i += 6  
    
    return ''.join(translation)

def main():
    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        print(to_english(input_string))
    else:
        print(to_braille(input_string))

if __name__ == "__main__":
    main()
