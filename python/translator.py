# Gabriel Upcott Eng Intern Challenge Fall - Winter 2025
import argparse

# Parse for command line arguments
def create_parser():
    parser = argparse.ArgumentParser(description="Braille Translator")
    parser.add_argument("str", metavar="STRING", type=str, nargs='+', help="The string to be translated")
    return parser

# Function to check if the input is Braille
def is_braille(full_string):
    braille_chars = {'O', '.'}
    
    # Trim spaces from the string
    cleaned_string = full_string.replace(" ", "")
    
    for char in cleaned_string:
        if char not in braille_chars:
            return False
    
    return True

def main():
    # Create the parser and get input arguments
    parser = create_parser()
    args = parser.parse_args()

    # Combine all arguments into a single string
    full_string = ' '.join(args.str)
    
    # Braille dictionary for translation
    braille = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.O.O..', 'j': '.OO...',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.O.OO.', 't': '.OOO..',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OO..O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.O.O..',
        '0': '.OO...', ',': '.O....', ';': '.O.O..', ':': '.OO...', '.': '.OO.O.',
        '?': '.O.OO.', '!': '.OOO..', '-': '..O.O.', '/': '..OO..', '(': '..OOO.',
        ')': '..OOO.', '<': '..OO..', '>': '..OO.O', 'capital': '.....O', 'number': '.O.OOO',
        ' ': '......'
    }
    
    # Disctionary of a-j to 1-9 for number mode
    braille_numbers = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }
    
    # Check if the input is Braille
    braille_check = is_braille(full_string)
    
    # Translate the input
    if braille_check:
        # Process Braille input into Latin text
        full_string = [full_string[i:i+6] for i in range(0, len(full_string), 6)]
        translated_str = ""
        capital_mode = False
        number_mode = False
        for group in full_string:
            # Turn on capital mode if a capital letter is detected
            if group == braille['capital']:
                capital_mode = True
                continue
            # Turn on number mode if a number is detected
            elif group == braille['number']:
                number_mode = True
                continue
            # Turn off number mode if a space is detected
            elif group == braille[' ']:
                translated_str += " "
                number_mode = False
                continue
            
            for key, value in braille.items():
                if value == group:
                    if number_mode:
                        # Need to use braille_numbers to convert a-j to 1-9
                        if key in braille_numbers:
                            translated_str += braille_numbers[key]
                        else:
                            translated_str += key
                    elif capital_mode:
                        translated_str += key.upper()
                    else:
                        translated_str += key
                    # Reset capital mode after applying
                    capital_mode = False
                    break
    
    else:
        # Process Latin input into Braille
        translated_str = ""
        number_mode = False
        
        for char in full_string:
            # If a capital letter is detected, turn on capital mode and
            # convert the letter to lowercase
            if char.isupper():
                translated_str += braille['capital']
                char = char.lower()
            # If a number is detected, turn on number mode
            # and convert the number to Braille
            if char.isdigit():
                if not number_mode:
                    translated_str += braille['number']
                    number_mode = True
            # If a space is detected, turn off number mode
            else:
                number_mode = False
            # Append the Braille translation of the character
            if char in braille:
                translated_str += braille[char]
                
        # Print the translated string
        print(translated_str)

if __name__ == "__main__":
    main()
