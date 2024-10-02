import sys

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
DECIMAL_FOLLOWS = '.O...O'
BRAILLE_CHAR_SIZE = 6
SPACE='......'

braille_alphabet = {
        'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 
        'D': 'OO.O..', 'E': 'O..O..', 'F': 'OOO...', 
        'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 
        'J': '.OOO..', 'K': 'O...O.', 'L': 'O.O.O.', 
        'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 
        'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 
        'S': '.OO.O.', 'T': '.OOOO.', 'U': 'O...OO', 
        'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 
        'Y': 'OO.OOO', 'Z': 'O..OOO', 
}

braille_numbers = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
        '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', 
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
        '0': '.OOO..', 
}

braille_special_chars = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', 
        '!': '..OOO.', ':': '..OO..', ';': '..O.O.', 
        '-': '....OO', '/': '.O..O.', '<': '.OO..O', 
        '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', 
        ' ': '......'
}

english_alphabet = {value: key for key, value in braille_alphabet.items()}
english_numbers = {value: key for key, value in braille_numbers.items()}
english_special_chars = {value: key for key, value in braille_special_chars.items()}

# is_input_braille (input: str): Returns True if input is braille and False if english
def is_input_braille(input):
    # Braille symbol length cannot be less than 6
    if len(input) < 6: 
        return False
    
    return all(char in ['O', '.'] for char in input)


# english_to_braille (input: str): Returns input as a string of braille characters
def english_to_braille(input):
   braille_text = ""
   is_number_following = False

   for char in input:
        if char.isalpha(): 
            if char.isupper():
               braille_text += CAPITAL_FOLLOWS + braille_alphabet[char]
            else:
               braille_text += braille_alphabet[char.upper()]

        elif char.isdigit(): 
            if not is_number_following:
                braille_text += NUMBER_FOLLOWS + braille_numbers[char]
                is_number_following = True
            else:
                braille_text += braille_numbers[char]

        elif char.isspace():
            braille_text += braille_special_chars[char]
            is_number_following = False

        elif char == '.':
            braile_text += DECIMAL_FOLLOWS + braille_special_chars[char]

        else: 
            braille_text += braille_special_chars[char]

   return braille_text


# braile_to_english (input: str): Returns input as a string of english characters
def braille_to_english(input):
    english_text = ""
    is_number_following = False
    is_capital_following = False
    is_decimal_following = False

    for i in range(0, len(input), BRAILLE_CHAR_SIZE):
        braille_symbol = input[i:i + BRAILLE_CHAR_SIZE]

        if braille_symbol == CAPITAL_FOLLOWS:
            is_capital_following = True
        
        elif braille_symbol == NUMBER_FOLLOWS:
            is_number_following = True
        
        elif braille_symbol == SPACE:
            english_text += english_special_chars[braille_symbol]
            is_number_following = False

        elif braille_symbol == DECIMAL_FOLLOWS:
            is_decimal_following = True
        
        elif is_decimal_following:
            english_text += english_special_chars[braille_symbol]
            is_decimal_following = False
        
        else:
            if is_number_following:
                english_text += english_numbers[braille_symbol]
            
            elif is_capital_following:
                english_text += english_alphabet[braille_symbol]
                is_capital_following = False
            
            else:
                if braille_symbol in english_alphabet:
                    english_text += english_alphabet[braille_symbol].lower()
                else:
                    english_text += english_special_chars[braille_symbol]

    return english_text


def main():
    input = ' '.join(sys.argv[1:])
    
    if is_input_braille(input):
        print(braille_to_english(input))
    else:
        print(english_to_braille(input))
        


if __name__ == "__main__":
    main()