import sys

ENGLISH_TO_BRAILLE_ALPHA = {
    'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..',
    'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.OO...', 'j' : '.OOO..',
    'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
    'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
    'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO',
    'z' : 'O..OOO', ' ' : '......'
    }

ENGLISH_TO_BRAILLE_NUMERIC = {
    '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....', '4' : 'OO.O..', '5' : 'O..O..', 
    '6' : 'OOO...', '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...', '0' : '.OOO..',
    }

BRAILLE_TO_ENGLISH_ALPHA = {value : key for key, value in ENGLISH_TO_BRAILLE_ALPHA.items()}
BRAILLE_TO_ENGLISH_NUMERIC = {value : key for key, value in ENGLISH_TO_BRAILLE_NUMERIC.items()}

BRAILLE_CAPITAL = '.....O'
BRAILLE_NUMERIC = '.O.OOO'

def is_braille(text : str) -> bool:
    if set(text) <= set('.O') and not len(text) % 6:
        return True
    else:
        return False

def braille_to_english(text : str) -> str:
    english_result = ''

    parse_capital = False # if next char will be a capital
    parsing_numeric = False # if parsing numeric characters

    for i in range(0, len(text), 6):
        braille_code = text[i : i + 6]

        if braille_code == BRAILLE_CAPITAL:
            parse_capital = True
        elif braille_code == BRAILLE_NUMERIC:
            parsing_numeric = True
        elif BRAILLE_TO_ENGLISH_ALPHA[braille_code] == ' ':
            parsing_numeric = False
            english_result += ' '
        elif parsing_numeric:
            if braille_code in BRAILLE_TO_ENGLISH_NUMERIC:
                english_result += BRAILLE_TO_ENGLISH_NUMERIC[braille_code]
        else:
            if parse_capital:
                english_result += BRAILLE_TO_ENGLISH_ALPHA[braille_code].upper()
                parse_capital = False
            else:
                english_result += BRAILLE_TO_ENGLISH_ALPHA[braille_code]

    return english_result

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    text = " ".join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_english(text))

if __name__ == "__main__":
    main()
