import sys

# Defines The Braille Map For Lowercase Letters And Numbers
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Adds The Capitalization Indicator For Uppercase Letters
capital_indicator = '.....O'

for letter in 'abcdefghijklmnopqrstuvwxyz':
    braille_map[letter.upper()] = capital_indicator + braille_map[letter]

# Reverses The Braille Map
english_map = {value: key for key, value in braille_map.items()}

def is_braille(input_str):
  # Checks If Each Character Is 'O' or '.'
    for c in input_str:
        if c not in 'O.':
            return False
    return True  

def english_to_braille(text):
    # Initializes An Empty List To Store The Translation
    result = []
    for char in text:
        if char in braille_map:
            result.append(braille_map[char])
        else:
            # Handles Unknown Characters (Translates To A Space)
            result.append('......')
    # Joins List Elements Into A Single String
    return ''.join(result)

def braille_to_english(braille):
    result = []
    i = 0 
    while i < len(braille):
        # Gets Next 6 Characters
        chunk = braille[i:i+6]
        # Checks For A Capital Letter
        if chunk == '.....O':
            # Gets The Letter Characters
            next_chunk = braille[i+6:i+12]
            if next_chunk in english_map:
                result.append(english_map[next_chunk].upper())
            i += 12
        else:
            # Appends The Lowercase Letter
            if chunk in english_map:
                result.append(english_map[chunk])
            else:
                # Handles Unknown Characters (Translates To A Space)
                result.append(' ')
            i += 6
    # Joins List Elements Into A Single String
    return ''.join(result)

def main():
  input_str = sys.argv[1]

    # Checks Language And Calls The Appropriate Function
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
