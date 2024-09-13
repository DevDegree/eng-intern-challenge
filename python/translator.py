# Define mappings from Braille to English and vice versa
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", 
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "CAPITAL", ".O.OOO": "NUMBER", "......": " "
}

# Braille digits are the same as letters 'a' to 'j'
braille_to_number = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", 
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", 
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", 
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", 
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", 
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", 
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", 
    "0": ".OOO..", " ": "......"
}

CAPITAL_SIGN = ".....O"
NUMBER_SIGN = ".O.OOO"

def is_braille(input_str):
    """ Check if the input is Braille (contains only 'O' and '.') """
    return all(char in 'O.' for char in input_str)

def translate_braille_to_english(braille_str):
    """ Convert Braille to English """
    result = []
    is_capital = False
    is_number = False

    for i in range(0, len(braille_str), 6):
        braille_char = braille_str[i:i+6]

        if braille_char == CAPITAL_SIGN:
            is_capital = True
            continue

        if braille_char == NUMBER_SIGN:
            is_number = True
            continue

        if is_number:
            # Translate Braille as a number
            char = braille_to_number.get(braille_char, '')
            if char:
                result.append(char)
            else:
                # Exit number mode after encountering a non-number character
                is_number = False
        else:
            # Translate Braille as a letter
            char = braille_to_english.get(braille_char, '')
            if is_capital:
                char = char.upper()
                is_capital = False
            result.append(char)

    return ''.join(result)

def translate_english_to_braille(english_str):
    """ Convert English to Braille """
    result = []
    is_in_number_mode = False
    
    for char in english_str:
        if char.isupper():
            result.append(CAPITAL_SIGN)  # Add capital sign for uppercase letters
            char = char.lower()

        if char.isdigit():
            if not is_in_number_mode:
                result.append(NUMBER_SIGN)  # Add number sign only once for a sequence of digits
                is_in_number_mode = True
            result.append(english_to_braille[char])
        else:
            is_in_number_mode = False  # Exit number mode after a non-number character
            braille_char = english_to_braille.get(char, '')
            result.append(braille_char)

    return ''.join(result)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Please provide input to translate.")
        return

    input_str = sys.argv[1]

    if is_braille(input_str):
        print(translate_braille_to_english(input_str))
    else:
        print(translate_english_to_braille(input_str))

if __name__ == "__main__":
    main()

