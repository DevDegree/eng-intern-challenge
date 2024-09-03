import sys

# Updated dictionary for mapping Braille characters to English according to the provided image
braille_to_english_char = {
    "......": " ",
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

# Updated dictionary for mapping Braille numbers to English
braille_to_english_num = {
    ".OOOO.": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
    "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9",
    ".....O": "capital follows", ".O.OOO": "number follows"
}

# Updated dictionary for mapping English characters and numbers to Braille
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "0": ".OOOO.", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    " ": "......"
}

# Prefixes for special Braille characters indicating number and capital letters
num_prefix = ".O.OOO"
capital_prefix = ".....O"

def is_english(input):
    """Check if the input text is in English format."""
    return all(char.isalpha() or char.isdigit() or char.isspace() for char in input)

def is_braille(input):
    """Check if the input text is in Braille format."""
    return all(char in 'O.' for char in input.replace(' ', '')) and len(input.replace(' ', '')) % 6 == 0

def convert_to_braille(input):
    """Convert English text to Braille representation."""
    output = []
    is_now_num = False

    for char in input:
        if char.isdigit():
            if not is_now_num:
                output.append(num_prefix)
                is_now_num = True
            output.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                output.append(capital_prefix)
                char = char.lower()
            output.append(english_to_braille[char])
            is_now_num = False  # Reset number mode after letter
        elif char == ' ':
            output.append(english_to_braille[' '])
            is_now_num = False  # Reset number mode on space

    return ''.join(output)

def convert_to_english(input):
    """Convert Braille representation to English text."""
    output = []
    i = 0
    is_now_num = False

    # Break the input into groups of 6-character-long Braille representations
    braille_chars = [input[k:k+6] for k in range(0, len(input), 6)]

    while i < len(braille_chars):
        cur_char = braille_chars[i]

        if cur_char == capital_prefix:
            # Enter capital mode
            is_now_num = False  # Reset number mode when encountering a capital letter
            i += 1
            if i < len(braille_chars):
                cur_char = braille_chars[i]
                output.append(braille_to_english_char[cur_char].upper())
        elif cur_char == num_prefix:
            # Enter number mode
            is_now_num = True
        elif is_now_num:
            # In number mode, interpret characters as numbers
            if cur_char == "......":
                is_now_num = False  # Exit number mode on a space
            else:
                output.append(braille_to_english_num[cur_char])
        else:
            # Regular character interpretation
            output.append(braille_to_english_char[cur_char])

        i += 1

    return ''.join(output)

def main():
    input = ' '.join(sys.argv[1:])

    if is_braille(input):
        print(convert_to_english(input))
    elif is_english(input):
        print(convert_to_braille(input))
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()
