import sys

# Special Braille signs
number_indicator = ".O.OOO"
capital_indicator = ".....O"

# Space character in braille
braille_space = "......"

# Braille mappings for english alphabets and the space character
english_alphabet_mappings = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......" 
}

# Braille mappings for numbers 
english_numeric_mappings = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

# Braile-to-English dictionary by inversing the dictionaries above
braille_to_english_alphabet = {v: k for k, v in english_alphabet_mappings.items()}
braille_to_english_number = {v: k for k, v in english_numeric_mappings.items()}

def is_braille(input_string):
    """
    Check if the input string is written in Braille by
    checking if the input string only consists of 'O'
    which represents a raised dot and '.' which represents no dot.
    """
    return all(c in 'O.' for c in input_string)

def translate_to_english(braille):
    """
    This function translates Braille input into English
    Handles all of capitalization, numbers and spaces.
    """
    result = []
    i = 0
    is_number = False
    is_capital = False
    input_len = len(braille)

    while i < len(braille):
        current_symbol = braille[i:i+6]

        # Capitalization symbol is read
        if current_symbol == capital_indicator:
            is_capital = True
        # Number follows symbol is read
        elif current_symbol == number_indicator:
            is_number = True
        # Space character is read
        elif current_symbol == braille_space:
            result.append(' ')
            # Reset is_number on space since this means next character is not a number
            is_number = False
        else:
            if is_number:
                result.append(braille_to_english_number.get(current_symbol, '?'))
            else:
                alphabet = braille_to_english_alphabet.get(current_symbol, '?')
                if is_capital:
                    # Capitalize alphabet
                    alphabet = alphabet.upper()
                    is_capital = False
                result.append(alphabet)
        # Move to next character
        i += 6


    return ''.join(result)

def translate_to_braille(english_text):
    """
    This function translates English text input to Braille
    Handles all capitalization, numbers and spaces. 
    """
    result = []
    is_number = False

    for character in english_text:
        # Capital letter
        if character.isupper():
            result.append(capital_indicator)
            character = character.lower()
        
        # If current character is a number
        if character.isdigit():
            if not is_number:
                result.append(number_indicator)
                is_number = True
            result.append(english_numeric_mappings[character])
        else:
            # Exit number if current character is an alphabet and is_number is True
            if is_number and character != ' ':
                is_number = False
            result.append(english_alphabet_mappings[character])

    return ''.join(result)
        

def main():
    input_string = ' '.join(sys.argv[1:]).strip()

    if is_braille(input_string):
        # Translate to English if input given is Braille
        print(translate_to_english(input_string))
    else:
        # Translate to Braille if input given is English
        print(translate_to_braille(input_string))


if __name__ == "__main__":
    main()
