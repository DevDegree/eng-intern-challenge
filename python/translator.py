import sys
import string as st

SPACE = "......"
CAPITAL_INDICATOR = ".....O"
DIGIT_INDICATOR = ".O.OOO"
BRAILLE_LETTERS = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"] # a-z
BRAILLE_NUMBERS = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."] # 0-9

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
    output = ""
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
            output += " "
            number_mode = False
            capital_mode = False
        elif number_mode:
            output += str(BRAILLE_NUMBERS.index(str(b)))
            capital_mode = False
        elif capital_mode:
            output += st.ascii_uppercase[BRAILLE_LETTERS.index(b)].upper()
            capital_mode = False 
        else :
            output += st.ascii_lowercase[BRAILLE_LETTERS.index(b)]
            number_mode = False
            capital_mode = False
    return output

def convert_to_braille(english_text):
    """
    Convert english text to braille
    """
    output = ""
    number_mode = False
    for c in english_text:
        if c.isspace():
            output += SPACE
            number_mode = False
        elif c.isalpha():
            if c.isupper():
                output += CAPITAL_INDICATOR
                c = c.lower()
            output += BRAILLE_LETTERS[st.ascii_lowercase.index(c)]
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                output += DIGIT_INDICATOR
                number_mode = True
            output += BRAILLE_NUMBERS[int(c)]
    return output

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input = ' '.join(sys.argv[1:])
    output = ""
    if is_alphanumeric(input): 
        output = convert_to_braille(input)
    elif is_braille(input.replace(' ', '')):
        output = convert_to_english(input.replace(' ', ''))
    print(output)
    return

if __name__ == '__main__':
    main()