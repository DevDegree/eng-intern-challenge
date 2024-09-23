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

ENGLISH_ALPHABET = {v: k for k, v in {**BRAILLE_LETTERS}.items()}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMBER = '.O.OOO'

def is_braille(input_str):
    """Check if the input string consists solely of Braille characters (O and .)."""
    return all(c in 'O.' for c in input_str)

def translate_to_braille(text):
    braille = ""
    number_mode = False

    for char in text:
        if char.isdigit():
            if not number_mode:
                braille += BRAILLE_NUMBER  # Append number mode indicator
                number_mode = True
            braille += BRAILLE_NUMBERS.get(char, '')
        if char == ' ':
            braille += BRAILLE_LETTERS[' ']  # Append space representation
            number_mode = False  
        else:
            if number_mode:
                number_mode = False 
            if char.isupper():
                braille += BRAILLE_CAPITAL  # Append capital indicator
            braille += BRAILLE_LETTERS.get(char.lower(), '')
    return braille

def translate_to_english(braille_str):
    english = ""
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
        elif symbol == '......':  # This represents a space in Braille
            english += ' '  # Append space representation
            is_capital = False
            is_number = False
            continue
        
        char = ENGLISH_ALPHABET.get(symbol, '')

        if char:
            if is_number:
                if char in 'abcdefghij':
                    english += str(ord(char) - ord('a') + 1)
                else:
                    english += char
            else:
                english += char.upper() if is_capital else char
            is_capital = False  # Reset capital after processing the character

    return english

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        return

    input_str = " ".join(sys.argv[1:])
    output = translate_to_english(input_str) if is_braille(input_str) else translate_to_braille(input_str)
    print(output)  


if __name__ == "__main__":
    main()
