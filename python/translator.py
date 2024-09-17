import sys

ENG_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......'
}

BRAILLE_TO_ENG = {}

for english_char, braille_char in ENG_TO_BRAILLE.items():
    BRAILLE_TO_ENG[braille_char] = english_char

CAPITAL_SIGN = '.....O'
NUMBER_SIGN = '.O.OOO'

def is_braille(input_str):
    if len(input_str) % 6 != 0:
        return False
    for char in input_str:
        if char != 'O' and char != '.':
            return False
    return True

def translate_to_braille(english_str):
    braille_output = []
    num_mode = False

    for ch in english_str:
        if ch.isupper():
            braille_output.append(CAPITAL_SIGN)
            braille_output.append(ENG_TO_BRAILLE[ch.lower()])
        elif ch.isdigit():
            if not num_mode:
                braille_output.append(NUMBER_SIGN)
                num_mode = True
            braille_output.append(ENG_TO_BRAILLE[ch])
        else:
            braille_output.append(ENG_TO_BRAILLE[ch])
            num_mode = False

    return ''.join(braille_output)


def translate_to_english(braille_text):
    """Simplified translation from Braille to English."""
    output = ""
    idx = 0
    is_capital = False
    is_number = False
    
    while idx < len(braille_text):
        braille_char = braille_text[idx:idx+6]
        idx += 6

        if braille_char == CAPITAL_SIGN:
            is_capital = True
        elif braille_char == NUMBER_SIGN:
            is_number = True
        else:
            if braille_char in BRAILLE_TO_ENG:
                translated_char = BRAILLE_TO_ENG[braille_char]
                
                if is_capital:
                    translated_char = translated_char.upper()
                    is_capital = False  
                
                if is_number:
                    is_number = False

                output += translated_char
            else:
                output += '?' 
    
    return output

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <strings_to_translate>")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        translated = translate_to_english(input_str)
    else:
        translated = translate_to_braille(input_str)
    
    print(translated)

if __name__ == "__main__":
    main()




