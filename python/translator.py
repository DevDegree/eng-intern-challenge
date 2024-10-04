import sys

ALPHABET_TO_BRAILLE = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
  'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
  'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
  'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO'
}

NUMBER_TO_BRAILLE = {
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
  '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

BRAILLE_CAPITAL_FOLLOWS = '.....O'
BRAILLE_NUMBER_FOLLOWS  = '.O.OOO'
BRAILLE_SPACE = '......'
BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER = {v: k for k, v in NUMBER_TO_BRAILLE.items()}

# given a braille string, splits it & returns an array of strings where each string is exactly 6 chars long
def split_into_six(s):
    braille_array = []
    for i in range(0, len(s), 6):
        braille_array.append(s[i:i+6])
    return braille_array

# given a string, returns a boolean value representing whether the string is braille
def is_braille(input: str) -> bool:
    input_size = len(input)
    if input_size % 6 != 0:
        return False
    for i in range(input_size):
        if input[i] != 'O' and input[i] != '.':
            return False
    return True

# given an english string, returns a string representing its braille translation
def to_braille(english_text: str) -> str:
    input_size = len(english_text)
    if input_size == 0:
        return ""
    braille_text = ""
    for i in range(input_size):
        is_letter = english_text[i].isalpha()
        is_capital = is_letter and english_text[i].isupper()
        if (is_letter and is_capital):
            braille_text += BRAILLE_CAPITAL_FOLLOWS
        if (is_letter):
            braille_text += ALPHABET_TO_BRAILLE[english_text[i].lower()]
        elif (english_text[i] == ' '):
            braille_text += BRAILLE_SPACE
        elif (i > 0 and english_text[i - 1].isdigit()):
            braille_text += NUMBER_TO_BRAILLE[english_text[i]]
        elif (i == 0 or not english_text[i - 1].isdigit()):
            braille_text += BRAILLE_NUMBER_FOLLOWS
            braille_text += NUMBER_TO_BRAILLE[english_text[i]]
    return braille_text

# given a braille string, returns a string representing its english translation
def to_english(braille_text: str) -> str:
    english_text = ""
    braille_array = split_into_six(braille_text)
    length = len(braille_array)
    if (length == 0):
        return ""
    is_letter = not braille_array[0] == BRAILLE_NUMBER_FOLLOWS
    is_capital = braille_array[0] == BRAILLE_CAPITAL_FOLLOWS
    for i in range(length):
        if (braille_array[i] == BRAILLE_SPACE and not is_letter):
            is_letter = True
            english_text += " "
        elif (braille_array[i] == BRAILLE_SPACE):
            english_text += " "
        elif (braille_array[i] == BRAILLE_NUMBER_FOLLOWS):
            is_letter = False
        elif (braille_array[i] == BRAILLE_CAPITAL_FOLLOWS):
            is_capital = True
        elif (not is_letter):
            english_text += BRAILLE_TO_NUMBER[braille_array[i]]
        elif (is_capital):
            english_text += BRAILLE_TO_ALPHABET[braille_array[i]].upper()
            is_capital = False
        else:
            english_text += BRAILLE_TO_ALPHABET[braille_array[i]]
    return english_text


def main():
    input = ' '.join(sys.argv[1:])
    if (is_braille(input)):
        print(to_english(input))
    else:
        print(to_braille(input))


if __name__ == "__main__":
    main()
