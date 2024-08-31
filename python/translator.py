import sys
from typing import Generator, Tuple, Dict

# Define the Braille dictionary
braille_dict: Dict[Tuple[str, str], str] = {
    ('letter', 'a'): 'O.....', ('letter', 'b'): 'OO....', ('letter', 'c'): 'O..O..', 
    ('letter', 'd'): 'O..OO.', ('letter', 'e'): 'O...O.', ('letter', 'f'): 'OO.O..', 
    ('letter', 'g'): 'OO.OO.', ('letter', 'h'): 'OO..O.', ('letter', 'i'): '.O.O..', 
    ('letter', 'j'): '.O.OO.', ('letter', 'k'): 'O.O...', ('letter', 'l'): 'OOO...', 
    ('letter', 'm'): 'O.OO..', ('letter', 'n'): 'O.OOO.', ('letter', 'o'): 'O.O.O.', 
    ('letter', 'p'): 'OOOO..', ('letter', 'q'): 'OOOOO.', ('letter', 'r'): 'OOO.O.', 
    ('letter', 's'): '.OOO..', ('letter', 't'): '.OOOO.', ('letter', 'u'): 'O.O..O', 
    ('letter', 'v'): 'OOO..O', ('letter', 'w'): '.O.OOO', ('letter', 'x'): 'O.OO.O', 
    ('letter', 'y'): 'O.OOOO', ('letter', 'z'): 'O.O.OO',

    # Special indicators
    ('capital', 'CAPITAL'): '.....O',
    ('number', 'NUMBER'): '..OOOO',
    ('space', ' '): '......'
}

# Reverse dictionary for translating from Braille to English
reverse_braille_dict: Dict[str, Tuple[str, str]] = {v: k for k, v in braille_dict.items()}

class BrailleTranslationError(Exception):
    """Custom exception for Braille translation errors."""
    pass

def translate_to_braille(text: str) -> Generator[str, None, None]:
    """Translate English text to Braille using a functional, generator-based approach."""
    number_mode = False
    for char in text:
        if char.isupper():
            yield braille_dict[('capital', 'CAPITAL')]
            yield braille_dict[('letter', char.lower())]
        elif char.isdigit():
            if not number_mode:
                yield braille_dict[('number', 'NUMBER')]
                number_mode = True
            # Map digits to corresponding letters a-j
            yield braille_dict[('letter', chr(ord('a') + int(char) - 1))]
        elif char == ' ':
            yield braille_dict[('space', ' ')]
            number_mode = False  # Exit number mode after space
        else:
            yield braille_dict[('letter', char.lower())]
            number_mode = False  # Exit number mode for letters

def translate_to_english(braille: str) -> str:
    """Translate Braille to English, processing in chunks of 6 characters."""
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_dict[('capital', 'CAPITAL')]:
            capitalize_next = True
        elif symbol == braille_dict[('number', 'NUMBER')]:
            number_mode = True
        elif symbol == braille_dict[('space', ' ')]:
            result.append(' ')
            number_mode = False  # Correctly exit number mode after space
        elif symbol in reverse_braille_dict:
            char_type, char_value = reverse_braille_dict[symbol]
            if number_mode:
                if char_type == 'letter':  # Assuming a-j mapping for numbers
                    result.append(str(ord(char_value) - ord('a') + 1))
            else:
                if capitalize_next:
                    result.append(char_value.upper())
                    capitalize_next = False
                else:
                    result.append(char_value)
        else:
            raise BrailleTranslationError(f"Invalid Braille symbol: {symbol}")
        i += 6

    return ''.join(result)

def main():
    """Main function to handle command-line input and output."""
    if len(sys.argv) != 2:
        raise ValueError("Expected one argument: the text to translate.")

    input_text = sys.argv[1]

    if all(c in 'O.' for c in input_text):
        try:
            output = translate_to_english(input_text)
        except BrailleTranslationError:
            raise ValueError("Error: Invalid Braille symbol encountered.")
    else:
        try:
            output = ''.join(translate_to_braille(input_text))
        except KeyError as e:
            raise ValueError(f"Translation error: Character '{e.args[0]}' not supported.")

    # Output the result without any additional text or newline characters
    sys.stdout.write(output)

if __name__ == "__main__":
    main()