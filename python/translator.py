import sys

BRAILLE_LETTERS = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

BRAILLE_NUMBERS = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_PUNCTUATION = {
    '.': '..OO.O'
}

ENGLISH_ALPHABET = {v: k for k, v in {**BRAILLE_LETTERS, **BRAILLE_PUNCTUATION}.items()}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'
BRAILLE_DECIMAL = '.O...O'

def is_braille(input_str):
    """Check if the input string consists solely of Braille characters (O and .)."""
    return all(c in 'O.' for c in input_str)

def translate_to_braille(text):
    braille = []
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille.append(BRAILLE_NUMBER)
                number_mode = True
            braille.append(BRAILLE_NUMBERS.get(char))
        elif char == '.':
            braille.append(BRAILLE_DECIMAL)
            number_mode = False  
        elif char in BRAILLE_PUNCTUATION:
            braille.append(BRAILLE_PUNCTUATION[char])
            number_mode = False  
        elif char == ' ':
            braille.append('......')  
            number_mode = False  
        else:
            if number_mode:
                number_mode = False 
            if char.isupper():
                braille.append(BRAILLE_CAPITAL)
            braille.append(BRAILLE_LETTERS.get(char.lower(), ''))

    return ''.join(braille)

def translate_to_english(braille_str):
    english = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        symbol = braille_str[i:i+6]
        if symbol == BRAILLE_CAPITAL:
            is_capital = True
            continue
        elif symbol == BRAILLE_NUMBER:
            is_number = True
            continue
        elif symbol == BRAILLE_DECIMAL:
            english.append('.')
            is_capital = False
            is_number = False
            continue
        elif symbol == '......':
            english.append(' ')
            is_capital = False
            is_number = False
            continue
        
        char = ENGLISH_ALPHABET.get(symbol, '')

        if char:
            if is_number:
                if char in 'abcdefghij':
                    english.append(str(ord(char) - ord('a') + 1))
                else:
                    english.append(char)
            else:
                english.append(char.upper() if is_capital else char)
            is_capital = False

    return ''.join(english)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        return

    results = []
    for input_str in sys.argv[1:]:
        output = translate_to_english(input_str) if is_braille(input_str) else translate_to_braille(input_str)
        results.append(output)
    
    print("".join(results))

if __name__ == "__main__":
    main()
