# braille lowercase alphabet
braille_alpha = {
    'a':  'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......'
}

# braille numbers
braille_nums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 'O': '.OOO..'
}

# for capitalization & numbers checker
capital_follows = '.....O'
number_follows = '.O.OOO'

def text_to_braille(text):
    result = []
    num_setting = False

    for c in text:
        if c.isalpha():
            if num_setting:
                num_setting = False
            if c.isupper():
                result.append(capital_follows)
                result.append(braille_alpha[c.lower()])
            else:
                result.append(braille_alpha[c])
        elif c.isdigit():
            if not num_setting:
                result.append(number_follows)
                num_setting = True
            result.append(braille_nums[c])
        elif c == ' ':
            result.append(braille_alpha[' '])
        

    return ''.join(result)
    
def braille_to_text(braille_text):
    # reverse dictionary
    braille_alpha_reverse = {v: k for k, v in braille_alpha.items()}
    braille_num_reverse = {v: k for k, v in braille_nums.items()}

    result = []
    i = 0
    capital_setting = False
    num_setting = False

    while i < len(braille_text):
        symbol = braille_text[i: i + 6]

        if symbol == number_follows:
            num_setting = True
        elif symbol == capital_follows:
            capital_setting = True
        elif symbol in braille_alpha_reverse and num_setting:
            result.append(braille_num_reverse[symbol])
        elif symbol in braille_alpha_reverse:
            letter = braille_alpha_reverse[symbol]
            if capital_setting:
                letter = letter.upper()
                capital_setting = False
            result.append(letter)
        i += 6

    return ''.join(result)
    
# determine if string should be translated to english or braille
def braille_translator(given_text):
    if all(c in 'O.' for c in given_text):
        return braille_to_text(given_text)
    else:
        return text_to_braille(given_text)
        
if __name__ == "__main__":
    import sys
    input_text = ' '.join(sys.argv[1:])
    print(braille_translator(input_text))



