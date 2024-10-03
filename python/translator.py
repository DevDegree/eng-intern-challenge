import sys
import string as st

SPACE = "......"
CAPITAL_INDICATOR = ".....O"
DIGIT_INDICATOR = ".O.OOO"
BRAILLE_LETTERS = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"] # a-z
BRAILLE_NUMBERS = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."] # 0-9

def convert_to_braille(english_text):
    """
    Convert english text to braille
    """
    number_mode = False
    for c in english_text:
        if c.isspace():
            print(SPACE, end = "")
            number_mode = False
        elif c.isalpha():
            if c.isupper():
                print(CAPITAL_INDICATOR, end = "")
                c = c.lower()
            print(BRAILLE_LETTERS[st.ascii_lowercase.index(c)], end = "")
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                print(DIGIT_INDICATOR, end="")
                number_mode = True
            print(BRAILLE_NUMBERS[int(c)], end = "")

def is_braille(s):
    """
    Check if the input string is a valid braille string
    """
    valid_chars = {'O', '.'}
    return len(s) % 6 == 0 and all(c in valid_chars for c in s)

def is_alphanumeric(s):
    """
    Check if the input string is alphanumeric
    """
    return all(c.isalnum() or c.isspace() for c in s)

def convert_to_english(braille_text):
    """
    Convert braille text to english
    """
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    number_mode = False
    capital_mode = False
    for b in braille_chars:
        if b == CAPITAL_INDICATOR:
            capital_mode = True
        elif b == DIGIT_INDICATOR:
            number_mode = True
            capital_mode = False
        elif b == SPACE:
            print(" ", end="")
            number_mode = False
            capital_mode = False
        elif number_mode:
            print(BRAILLE_NUMBERS.index(str(b)), end="")
            capital_mode = False
        elif capital_mode:
            print(st.ascii_uppercase[BRAILLE_LETTERS.index(b)].upper(), end="")
            capital_mode = False 
        else :
            print(st.ascii_lowercase[BRAILLE_LETTERS.index(b)], end="")
            number_mode = False
            capital_mode = False

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input = ' '.join(sys.argv[1:])
    if is_braille(input.replace(' ', '')):
        convert_to_english(input.replace(' ', ''))
    elif is_alphanumeric(input): 
        convert_to_braille(input)
    print()
    return

if __name__ == '__main__':
    main()