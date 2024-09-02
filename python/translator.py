# O(n) time complexity, where n is the length of the input string.
import sys

braille_to_english_letters = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital follows", ".O...O": "decimal follows", ".O.OOO": "number follows",
}

braille_to_numbers = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
}

braille_to_special = {
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
    "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">",
    "O.O..O": "(", ".O.OO.": ")", "......": " ",
}

english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", 'O': ".O..",
    'capital follows': ".....O", 'number follows': ".O.OOO", 'decimal follows': ".O...O",
    '.': "..OO.O", ',': "..O...", '?': "..O.OO", '!': "..OOO.", ':': "..OO..",
    ';': "..O.O.", '-': "....OO", '/': ".O..O.", '<': ".OO..O", '>': "O..OO.",
    '(': "O.O..O", ')': ".O.OO.", ' ': "......",
}

def verify_braille(input_string):
    """Check if the input string is in Braille format."""
    for char in input_string:
        if char not in ('.', 'O'):
            return False
    return True

def braille_to_eng(braille_string):
    """Translate Braille input to English."""
    translated = []
    is_capital_letter = False
    is_number = False

    for i in range(0, len(braille_string), 6):
        char = braille_string[i:i+6]

        if char == "......":
            # Append space if 6 dots are empty
            translated.append(' ')
            is_number = False
        elif char == ".O.OOO":
            # Is number indicator
            is_number = True
        elif char == ".....O":
            # Is Capital letter indicator
            is_capital_letter = True
        else:
            if is_number:
                letter = braille_to_numbers.get(char)
            else:
                letter = (braille_to_english_letters.get(char) or braille_to_special.get(char))
            if is_capital_letter and letter.isalpha():
                letter = letter.upper()  # Capitalize letter if needed
                is_capital_letter = False
            translated.append(letter)

    return ''.join(translated)


def eng_to_braille(english_string):
    """Translate English input to Braille without spaces between chunks."""
    translated = []
    is_number = False

    for char in english_string:
        if char.isdigit():
            if not is_number:
                # Undicate that a number follows
                translated.append(english_to_braille['number follows'])
                is_number = True
            translated.append(english_to_braille.get(char))
        else:
            is_number = False
            if char.isupper():
                # Indicate that a capital letter follows
                translated.append(english_to_braille['capital follows'])
                translated.append(english_to_braille.get(char.lower()))
            else:
                translated.append(english_to_braille.get(char))
    return ''.join(translated)

def main():
    if len(sys.argv) != 2:
        print("Please use the format of: translator.py argument")
        sys.exit(1)

    input_string = sys.argv[1]
    if verify_braille(input_string):
        print(braille_to_eng(input_string))
    else:
        print(eng_to_braille(input_string))

if __name__ == "__main__":
    main()
