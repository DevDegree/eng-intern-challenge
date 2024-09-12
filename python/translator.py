import sys

# Braille representations for English characters, numbers, capitalization, and special symbols.
english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
    'capital': ".....O",  # Braille symbol indicating the next character is uppercase
    'number': ".O.OOO"    # Braille symbol indicating that subsequent characters are numbers
}

# Inverse mapping from Braille to English characters
braille_to_english = {v: k for k, v in english_to_braille.items()}

def is_braille(text):
    """
    Determine if the given text is Braille by checking if all characters are 'O' or '.'.
    
    :param text: String input to check.
    :return: Boolean indicating if the text is Braille.
    """
    return all(char in ['O', '.'] for char in text)

def translate_to_braille(text):
    """
    Translate English text to Braille.
    
    :param text: English text to translate.
    :return: Braille representation of the text.
    """
    result = []
    num_mode = False  # Flag to indicate if we are in number mode

    for char in text:
        if char.isdigit():
            if not num_mode:
                # Entering number mode
                result.append(english_to_braille['number'])
                num_mode = True
            result.append(english_to_braille[char])
        else:
            if num_mode:
                # Exiting number mode on encountering non-digit
                num_mode = False
            if char.isalpha():
                if char.isupper():
                    # Capital letter handling
                    result.append(english_to_braille['capital'])
                    char = char.lower()
                result.append(english_to_braille[char])
            elif char == ' ':
                result.append(english_to_braille[' '])
    
    return ''.join(result)

def translate_to_english(braille):
    """
    Translate Braille text to English.
    
    :param braille: Braille string to translate.
    :return: English representation of the Braille text.
    """
    result = []
    i = 0
    num_mode = False  # Flag to indicate if we are in number mode

    while i < len(braille):
        symbol = braille[i:i+6]  # Each Braille character is represented by 6 characters
        if symbol == english_to_braille['number']:
            num_mode = True
        elif symbol == english_to_braille['capital']:
            # Handle capitalization
            next_char = braille[i+6:i+12]
            result.append(braille_to_english[next_char].upper())
            i += 6
        else:
            char = braille_to_english[symbol]
            if num_mode and char.isdigit():
                result.append(char)
            else:
                result.append(char)
            num_mode = False
        i += 6
    
    return ''.join(result)

def main():
    # Read input from command line arguments
    input_text = ' '.join(sys.argv[1:])
    
    if is_braille(input_text):
        # Input is Braille, translate to English
        print(translate_to_english(input_text))
    else:
        # Input is English, translate to Braille
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
