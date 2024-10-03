import sys

SPACE = "......"
CAPITAL_INDICATOR = ".....O"
DIGIT_INDICATOR = ".O.OOO"
braille_letters = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO"] # a-z
braille_numbers = [".OOO..", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO..."] # 0-9

def convertToBraille(english_text):
    return
      
def is_braille_input(s):
    return
  
def convertToEnglish(braille_text):
    return

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input = ' '.join(sys.argv[1:])
    if is_braille_input(input.replace(' ', '')):
        convertToEnglish(input.replace(' ', ''))
    else: 
        convertToBraille(input)
    print()
    return

if __name__ == '__main__':
    main()