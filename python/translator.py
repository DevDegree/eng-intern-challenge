import sys

# create dictionary to store alphabets to braille chars
ALPHABET_CHAR_LOOKUP = { 
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', 'CAPITAL': '.....O', 'DECIMAL': '.O...O', 'NUMBER': '.O.OOO', 
    ' ': '......'
}

# maps decimal number to braille
DIGIT_NUMBER_LOOKUP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# dictionary to store braille chars mapped to alphabet
BRAILLE_CHAR_LOOKUP = {value: key for key, value in ALPHABET_CHAR_LOOKUP.items()}
BRAILLE_NUMBER_LOOKUP = {value: key for key, value in DIGIT_NUMBER_LOOKUP.items()}

def convert_to_alphabet(user_input):
    i = 0
    '''
    ideally, any braille input should cause len(input) % 6 == 0 to be true
    if for any reason any incomplete braille characters get inputted, the program 
    will disregard the incomplete character
    IMPORTANT assumption: since the technical requirements did not mention it,
    the ability to have decimals or symbols is omitted, however, it could be added with 
    if converted_char == 'DECIMAL' or 'SYMBOL' then add leading '.' character to result and then the numbers!
    '''
    result = ""
    # set conditions
    number, uppercase, decimal = False, False, False
    while i < len(user_input)-5:
        # get char and convert
        braille_char = user_input[i:i+6]
        converted_char = BRAILLE_CHAR_LOOKUP[braille_char]
        if converted_char == 'CAPITAL':
            # set uppercase to true
            uppercase = True
        elif converted_char == 'NUMBER':
            # set number to true
            number = True
        else:
            if converted_char == ' ':
                number = False
            if number:
                # should lookup number
                result += BRAILLE_NUMBER_LOOKUP[braille_char]
            else:
                # only alpha chars left
                if uppercase:
                    result += BRAILLE_CHAR_LOOKUP[braille_char].upper()
                    uppercase = False
                else:
                    result += BRAILLE_CHAR_LOOKUP[braille_char]
            
        i += 6

    return result
    
def convert_to_braille(user_input):
    res = ""
    last_item = None
    for char in user_input:
        if char.isdigit():
            # check last element to see whether it was also a number, if not, add number_follows symbol
            if res and last_item.isdigit():
                res += DIGIT_NUMBER_LOOKUP[char]
            else:
                # if no res (beginnig of a string), or res[-1] is not a digit, i still want to insert a number follows symbol!
                res += ALPHABET_CHAR_LOOKUP['NUMBER']
                res += DIGIT_NUMBER_LOOKUP[char]
        else:
            if char.isupper():
                res += ALPHABET_CHAR_LOOKUP['CAPITAL']
            res += ALPHABET_CHAR_LOOKUP[char.lower()]
        last_item = char
    return res


def main():
    if len(sys.argv) >= 2:
        # get user input and turn into one string (multiple strings are consecutive with no space)
        user_input = ' '.join(sys.argv[1:])
        # detect input type by seeing if user_input is a subset of {'O', '.'}
        if set(user_input).issubset({'O', '.'}):
            print(convert_to_alphabet(user_input))
        else:
            print(convert_to_braille(user_input))

    else:
        print("Please input a string.")
    # get arguments

if __name__ == '__main__':
    main()