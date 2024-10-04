

import sys

map_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

map_nums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Needed to identify a Capital letter and a Number
indicator_cap = '.....O'
indicator_num = '.O.OOO'

# Reverse braille_map, needed to convert braille to english 
reverse_braille_map = {}
for k, v in map_braille.items():
    reverse_braille_map[v] = k

# Reverse number_map, needed to convert braille to english 
reverse_numbers_map = {}
for k, v in map_nums.items():
    reverse_numbers_map[v] = k

# Needed to switch between english-to-braille or braille-to-english functions 
def is_braille(s):
    for c in s:
        if c not in "O.":
            return False
    return True

# Converts input from english to braille 
def english_to_braille(text):
    result = []
    num = False 
    
    for char in text:
        if char.isdigit():
            if not num:
                result.append(indicator_num)
                num = True
            result.append(map_nums[char])
        elif char.isalpha():
            if num:
                num = False 
            if char.isupper():
                result.append(indicator_cap)
            result.append(map_braille[char.lower()])
        elif char == ' ':
            result.append(map_braille[' '])
            num = False

    return ''.join(result)

# Converts input from braille to english
def braille_to_english(braille):
    result = []
    cap = False
    num = False 
    
    i = 0 
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == indicator_cap:
            cap = True
        elif symbol == indicator_num:
            num = True
        else:
            if num:
                result.append(reverse_numbers_map[symbol])
                num = False
            elif cap:
                result.append(reverse_braille_map[symbol].upper())
                cap = False
            else:
                result.append(reverse_braille_map[symbol])
        i += 6 # Advances index by 6 
    
    return ''.join(result)

def main():
    # Combine arguments into a single string
    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(braille_to_english(input_string)) 
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()

