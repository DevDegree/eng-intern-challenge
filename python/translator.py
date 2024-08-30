import sys

lowercase = {
    'a': 'O.....', 'b': 'O.O...','c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..','i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.','m': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.','q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.','u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO','y': 'OO.OOO','z': 'O..OOO',
}
numbers = {
    '1': 'O.....', '2': 'O.O...','3': 'OO....','4': 'OO.O..','5': 'O..O..','6': 'OOO...','7': 'OOOO..','8': 'O.OO..','9': '.OO...','0': '.OOO..',
}

special_bin = {
    'uppercase': '.....O',
    'number' : '.O.OOO',
    'space' : '......'
}

def reverse_dict(d):
    return {v: k for k, v in d.items()}

first_element = sys.argv[1]
# Determines if first string consists of only O's and .'s (Binary to English)
if first_element.count('O') + first_element.count('.') == len(first_element):
    english = ''

    # Converts dicts to use binary keys
    lowercase_b = reverse_dict(lowercase) 
    numbers_b = reverse_dict(numbers)
    # Creates a list of each binary character
    characters = [first_element[i:i+6] for i in range(0, len(first_element), 6)]

    upper = False
    num = False
    for line in characters:
        if upper:
            english += lowercase_b[line].upper()
            upper = False
        elif line == special_bin['space']:
            english += ' '
            num = False
        elif num:
            english += numbers_b[line]
        elif line == special_bin['uppercase']: # Next char is uppercase
            upper = True
            num = False
        elif line == special_bin['number']: # Next char is number
            num = True
        else:
            english += lowercase_b[line]
    print(english)

# English to Binary
else:
    binary = ''


    prev_num = False # Ensures the number flag only appears before the group of numbers
    sentance = sys.argv[1:]
    for word in sentance:
        for char in word:
            if char.isnumeric():
                if not prev_num:
                    binary += special_bin['number']
                    prev_num = True
                binary += numbers[char]
            else:
                prev_num = False
                if char.isupper():
                    binary += special_bin['uppercase']
                binary += lowercase[char.lower()]
        binary += special_bin['space']
    binary = binary[:-6]
    print(binary)