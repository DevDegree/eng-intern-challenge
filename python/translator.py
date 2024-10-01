import sys

BRAILLE_DICT = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......'
}

NUMBERS_DICT = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', 
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}


BRAILLE_SIZE = 6
NUMBER_SIGN = '.O.OOO'
SPACE_SIGN = '......' 
DECIMAL_SIGN = '.O...O'
CAPITAL_SIGN = '.....O'


def __init__(self, input_to_translate):
    self.input = input_to_translate

def IsBraille(input_to_translate):
    return len(input_to_translate) % BRAILLE_SIZE == 0 and all(c in 'O.' for c in input_to_translate)

def BrailleToEnglish(braille_to_translate):
    result = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_to_translate), BRAILLE_SIZE):
        braille_char = braille_to_translate[i:i + BRAILLE_SIZE]

        if braille_char == CAPITAL_SIGN:
            is_capital = True
        elif braille_char == NUMBER_SIGN:
            is_number = True
        elif braille_char == SPACE_SIGN:
            result.append(' ')
            is_capital = False
            is_number = False
        else:
            if is_number:
                for key, value in NUMBERS_DICT.items():
                    if value == braille_char:
                        result.append(key)
                        break
            else:
                for key, value in BRAILLE_DICT.items():
                    if value == braille_char:
                        if is_capital:
                            result.append(key.upper())
                            is_capital = False
                        else:
                            result.append(key)
                        break
            is_number = False

    return ''.join(result)


def EnglishToBraille(input_to_translate):
    result = []
    is_number_mode = False

    for char in input_to_translate:
        if char == ' ':
            result.append(SPACE_SIGN)
            is_number_mode = False

        elif char.isdigit():
            if not is_number_mode:
                result.append(NUMBER_SIGN)
                is_number_mode = True
            result.append(NUMBERS_DICT[char])

        elif char.isupper():
            result.append(CAPITAL_SIGN)
            result.append(BRAILLE_DICT[char.lower()])
            is_number_mode = False

        else:
            result.append(BRAILLE_DICT[char])
            is_number_mode = False 

    return ''.join(result)


def main():
    input_to_translate = " ".join(sys.argv[1:])
    translated_string = BrailleToEnglish(input_to_translate) if IsBraille(input_to_translate) else EnglishToBraille(input_to_translate)
    print(translated_string)


if __name__ == "__main__": 
    main()