import sys

SPACE = "......"
CAPITAL_INDICATOR = ".....O"
DIGIT_INDICATOR = ".O.OOO"
braille_letters = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"] # a-z
braille_numbers = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."] # 0-9

def convert_to_braille(english_text):
    number_mode = False
    for c in english_text:
        if c.isspace():
            print(SPACE, end = "")
            number_mode = False
        elif c.isalpha():
            if c.isupper():
                print(CAPITAL_INDICATOR, end = "")
                c = c.lower()
            print(braille_letters[st.ascii_lowercase.index(c)], end = "")
            number_mode = False
        elif c.isdigit():
            if not number_mode:
                print(DIGIT_INDICATOR, end="")
                number_mode = True
            print(braille_numbers[int(c)], end = "")

      
def is_braille(s):
    valid_chars = {'O', '.'}
    return len(s) % 6 == 0 and all(c in valid_chars for c in s)
  
def convert_to_english(braille_text):
    return

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input = ' '.join(sys.argv[1:])
    if is_braille(input.replace(' ', '')):
        convert_to_english(input.replace(' ', ''))
    else: 
        convert_to_braille(input)
    print()
    return

if __name__ == '__main__':
    main()