import sys

ENGLISH_TO_BRAILLE_ALPHA = {
    'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..',
    'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...', 'j' : '.OOO..',
    'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
    'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
    'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO',
    'z' : 'O..OOO'
    }

ENGLISH_TO_BRAILLE_NUMERIC = {
    '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....', '4' : 'OO.O..', '5' : 'O..O..', 
    '6' : 'OOO...', '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...', '0' : '.OOO..',
    }

BRAILLE_TO_ENGLISH_ALPHA = {value : key for key, value in ENGLISH_TO_BRAILLE_ALPHA.items()}
BRAILLE_TO_ENGLISH_NUMERIC = {value : key for key, value in ENGLISH_TO_BRAILLE_NUMERIC.items()}

BRAILLE_SPACE   = '......'
BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMERIC = '.O.OOO'

def is_braille(text : str) -> bool:
    if set(text) <= set('.O') and not len(text) % 6:
        return True
    else:
        return False

def english_to_braille(text : str) -> str:
    braille_result = ''

    numeric_follows = False # numeric characters follow

    for character in text:
        if character == ' ':
            numeric_follows = False
            braille_result += BRAILLE_SPACE
        elif character.lower() in ENGLISH_TO_BRAILLE_ALPHA:
            if character.isupper():
                braille_result += BRAILLE_CAPITAL

            braille_result += ENGLISH_TO_BRAILLE_ALPHA[character.lower()]
        elif character in ENGLISH_TO_BRAILLE_NUMERIC:
            if not numeric_follows:
                braille_result += BRAILLE_NUMERIC
                numeric_follows = True

            braille_result += ENGLISH_TO_BRAILLE_NUMERIC[character]

    return braille_result

def braille_to_english(text : str) -> str:
    english_result = ''

    capital_follows = False # next char will be a capital
    numeric_follows = False # numeric characters follow

    for i in range(0, len(text), 6):
        braille_code = text[i : i + 6]

        if braille_code == BRAILLE_CAPITAL:
            capital_follows = True
        elif braille_code == BRAILLE_NUMERIC:
            numeric_follows = True
        elif braille_code == BRAILLE_SPACE:
            numeric_follows = False
            english_result += ' '
        elif numeric_follows:
            if braille_code in BRAILLE_TO_ENGLISH_NUMERIC:
                english_result += BRAILLE_TO_ENGLISH_NUMERIC[braille_code]
        else:
            if capital_follows:
                english_result += BRAILLE_TO_ENGLISH_ALPHA[braille_code].upper()
                capital_follows = False
            else:
                english_result += BRAILLE_TO_ENGLISH_ALPHA[braille_code]

    return english_result

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

if __name__ == '__main__':
    main()
