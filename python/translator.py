import sys

# define special inputs
braille_capital_follows = '.....O'
braille_number_follows = '.O.OOO'
braille_space = '......'

# lowercase english chars to braille mapping
# based on the braille alphabet defined in the technical requirements, we assume we do not need to handle decimal places and punctuation
english_chars_to_braille = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
}

# numbers to braille mapping
numbers_to_braille = {
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
}

# braille letters and numbers to english
braille_to_english = {v: k for k, v in english_chars_to_braille.items()}
braille_to_number = {v: k for k, v in numbers_to_braille.items()}

# translate from braille to english
def braille_to_english(string):
    output = ""
    is_number = False
    is_capital = False
    n = len(string)
    braille_chars = [string[i:i+6] for i in range(0, n, 6)]
    for char in braille_chars:
        if char == braille_capital_follows:
            is_capital = True
            continue
        elif char == braille_number_follows:
            is_number = True
            continue
        elif char == braille_space:
            if is_capital:
                raise ValueError(f'the "capital follows" input is followed by a space: {char}')
            is_number = False
            c = ' '
        elif is_number:
            c = braille_to_number.get(char)
            if not c:
                raise ValueError(f'the "number follows" input is not followed by a valid number: {char}')
        else:
            c = braille_to_english.get(char)
            if not c:
                raise ValueError(f'inputted invalid character: {char}')
            if is_capital:
                is_capital = False
                c.upper()
        output += c
    return output

# translate from english to braille
def english_to_braille(string):
    is_number = False
    output = ""
    for char in string:
        if char.isdigit():
            if not is_number:
                output += braille_number_follows
                is_number = True
            output += numbers_to_braille[char]
        elif char == ' ':
            is_number = False
            output += braille_space
        else:
            if char.isupper():
                output += braille_capital_follows
            output += english_chars_to_braille[char.lower()]
    return output

# check if input is braille
def is_braille(input):
    # the length of the input is not divisible by 6
    if len(input) % 6 != 0:
        return False
    allowed_chars = {'O', '.'}
    return set(input).issubset(allowed_chars)

# check if the input is english, we assume we only allow the characters we can convert to braille as per the technical requirements
def is_english(input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ')
    return set(input).issubset(allowed_chars)

if __name__ == "__main__":
    input = " ".join(sys.argv[1:])
    # if the input includes the "." character, then we determine that the inputted string is Braille
    if is_braille(input): 
        print(braille_to_english(input))
    elif is_english(input):
        print(english_to_braille(input))
    else:
        raise ValueError("Input is not valid")
