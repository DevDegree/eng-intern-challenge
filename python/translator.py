
import sys

# Braille mappings for alphabet, numbers, and special characters
braille_map = {
    'alphabet': {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO'
    },
    'digits': {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    },
    'symbols': {
        'cap': '.....O', 'num': '.O.OOO', 'sp': '......', 
        'period': '..OO.O', 'comma': '..O...', 'question': '..O.OO', 'exclamation': '..OOO.', 
        'colon': '..OO..', 'semicolon': '..O.O.', 'dash': '....OO', 'slash': '.O..O.', 
        'lt': '.O.O.O', 'gt': 'O.O.O.', 'open_paren': 'O.O..O', 'close_paren': '.O.OO.'
    }
}

# Reversed Braille mappings for decoding back to English
english_map = {
    'alphabet': {v: k for k, v in braille_map['alphabet'].items()},
    'digits': {v: k for k, v in braille_map['digits'].items()},
    'symbols': {v: k for k, v in braille_map['symbols'].items()}
}

def is_braille(string):
    """Validates if the provided string is in Braille format by checking each 6-dot cell."""
    if len(string) % 6 != 0:
        return False

    for i in range(0, len(string), 6):
        cell = string[i:i+6]
        if cell not in english_map['alphabet'] and cell not in english_map['digits'] and cell not in english_map['symbols']:
            return False

    return True

def english_to_braille(text):
    """Converts English text to Braille, managing capital letters and number mode."""
    braille_output = []
    num_mode = False

    for char in text:
        if char.isdigit():
            if not num_mode:
                braille_output.append(braille_map['symbols']['num'])
                num_mode = True
            braille_output.append(braille_map['digits'][char])

        elif char == ' ':
            braille_output.append(braille_map['symbols']['sp'])
            num_mode = False  # Reset number mode after space

        elif char.isupper():
            braille_output.append(braille_map['symbols']['cap'])
            braille_output.append(braille_map['alphabet'][char.lower()])
            num_mode = False  # Reset number mode after capital

        else:
            braille_output.append(braille_map['alphabet'].get(char, '?'))  # Handle unknown characters
            num_mode = False  # Reset number mode after any other character

    return ''.join(braille_output)

def braille_to_english(braille):
    """Decodes Braille back to English, recognizing capital letters, numbers, and spaces."""
    english_output = []
    num_mode = False
    cap_mode = False

    for i in range(0, len(braille), 6):
        cell = braille[i:i+6]
        if cell == braille_map['symbols']['cap']:
            cap_mode = True

        elif cell == braille_map['symbols']['num']:
            num_mode = True

        elif cell == braille_map['symbols']['sp']:
            num_mode = False
            cap_mode = False
            english_output.append(' ')

        else:
            if cell in (english_map['alphabet'] if not num_mode else english_map['digits']):
                char = (english_map['alphabet'] if not num_mode else english_map['digits'])[cell]

                if cap_mode:
                    char = char.upper()
                    cap_mode = False

                english_output.append(char)
            else:
                english_output.append('?')

    return ''.join(english_output)

def translate(input_text):
    """Determines whether the input is Braille or English, then translates accordingly."""
    if is_braille(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)

def main():
    """Main function to handle command-line input and perform the translation."""
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
        return

    input_text = ' '.join(sys.argv[1:])
    result = translate(input_text)
    sys.stdout.write(result)

if __name__ == "__main__":
    main()
