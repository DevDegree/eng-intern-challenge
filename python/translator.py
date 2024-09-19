# SHOPIFY ENG INTERN CHALLENGE
# Divya Vithiyatharan

# follows flags
CAPITAL_FOLLOWS_FLAG = '.....O'
DECIMAL_FOLLOWS_FLAG = '.O...O'
NUMBER_FOLLOWS_FLAG = '.O.OOO'

# english to braille dicts
LETTER_BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOOO.', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}
NUMBER_BRAILLE_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
PUNCTUATION_BRAILLE_DICT = {
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
}

#lists of keys and values for each dict for braille_to_eng() to get key using value
LETTER_KEY_LIST = list(LETTER_BRAILLE_DICT.keys())
letter_VALUE_LIST = list(LETTER_BRAILLE_DICT.values())
NUMBER_KEY_LIST = list(NUMBER_BRAILLE_DICT.keys())
NUMBER_VALUE_LIST = list(NUMBER_BRAILLE_DICT.values())
PUNCT_KEY_LIST = list(PUNCTUATION_BRAILLE_DICT.keys())
PUNCT_VALUE_LIST = list(PUNCTUATION_BRAILLE_DICT.values())

def braille_to_eng(braille_input_str: str) -> str:
    split_braille_str = []
    eng_output = ''
    captial_flag = False # tracks whether following char is a capitalized letter
    number_flag = False # tracks whether the current char are/should be numbers

    split_braille_str = [braille_input_str[i:i+6] for i in range(0, len(braille_input_str), 6)]

    for char in split_braille_str:
        if char == NUMBER_FOLLOWS_FLAG:
            number_flag = True
            continue
        elif char == CAPITAL_FOLLOWS_FLAG:
            captial_flag = True
            number_flag = False # disable number if capital is encountered
            continue 

        if char in NUMBER_BRAILLE_DICT.values() and number_flag:
            number = NUMBER_KEY_LIST[NUMBER_VALUE_LIST.index(char)]
            eng_output += number
        
        elif char in LETTER_BRAILLE_DICT.values():
            letter = LETTER_KEY_LIST[letter_VALUE_LIST.index(char)]
            # assume only the next symbol should be capitalized
            if captial_flag:
                letter = letter.upper()
                captial_flag = False
            eng_output += letter
        
        elif char in PUNCTUATION_BRAILLE_DICT.values():
            punct = PUNCT_KEY_LIST[PUNCT_VALUE_LIST.index(char)]
            # assume all following symbols are numbers until the next space symbol
            if number_flag and punct == ' ':
                number_flag = False
            eng_output += punct

        else:
            return "error: input contains invalid character(s) " + char
        
    return eng_output

def eng_to_braille(eng_input_str: str) -> str:
    braille_output = ''

    for char in eng_input_str:
        if char in LETTER_BRAILLE_DICT:
            if char.isupper():
                braille_output += CAPITAL_FOLLOWS_FLAG # add capital flag before capitalized letter
            braille_output += LETTER_BRAILLE_DICT.get(char.lower())

        elif char in NUMBER_BRAILLE_DICT:
            braille_output += NUMBER_FOLLOWS_FLAG # add number flag before numbers
            braille_output += NUMBER_BRAILLE_DICT[char]
        
        elif char in PUNCTUATION_BRAILLE_DICT:
            braille_output += PUNCTUATION_BRAILLE_DICT[char]
        
        else:
            return "error: input contains invalid character(s) " + char
    
    return braille_output

def main():
    input_str = input("enter value: ")
    if set(input_str).issubset({'O', '.'}) and len(input_str) % 6 == 0:
        print(braille_to_eng(input_str))
    else:
        print(eng_to_braille(input_str))

if __name__ == '__main__':
    main()