import sys

# Braille mappings
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

# Braille signs
capital_sign = '.....O'
number_sign = '.O.OOO'

# Numbers in Braille (0-9)
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Inverse dictionary for reverse translation (Braille -> English)
inverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
inverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_string):
    """ Check if the input string is Braille by verifying its characters """
    return all(c in 'O.' for c in input_string)

def english_to_braille(text):
    """
    Converts a given English text into Braille notation.
    
    Time Complexity: O(n), where n is the length of the input text. We traverse each character once.
    
    Algorithm:
    - For each character in the input, check if it is a number or a letter.
    - If it is a number, append the number Braille prefix if necessary.
    - If it is a capital letter, append the capital prefix and convert the letter to lowercase.
    - Handle spaces and other supported characters by appending their respective Braille patterns.
    - Return the Braille string concatenated from all the characters.
    """
    result = []
    number_mode = False
    
    for char in text:
        if char.isupper():
            result.append(capital_sign)
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(number_sign)
                number_mode = True
            result.append(braille_numbers[char])
        else:
            if number_mode and char != ' ':
                number_mode = False
            result.append(braille_alphabet[char])
    
    return ''.join(result)

def braille_to_english(braille):
    """
    Converts a given Braille string into English text.
    
    Time Complexity: O(n), where n is the length of the input Braille string. Each Braille character is 6 dots, and we process them in chunks of 6.
    
    Algorithm:
    - For every 6-character chunk (representing a Braille character), check if it is a special prefix for numbers or capitals.
    - If a capital prefix is encountered, capitalize the next character.
    - If a number prefix is encountered, treat subsequent characters as numbers.
    - Append each translated character to the result string.
    - Return the full English text.
    """
    result = []
    i = 0
    number_mode = False
    capital_mode = False
    
    while i < len(braille):
        current_symbol = braille[i:i+6]
        
        if current_symbol == capital_sign:
            capital_mode = True
        elif current_symbol == number_sign:
            number_mode = True
        elif current_symbol == '......':
            result.append(' ')
            number_mode = False  # Reset number mode on space
        else:
            if number_mode:
                result.append(inverse_braille_numbers.get(current_symbol, '?'))  # Fallback for invalid numbers
            else:
                letter = inverse_braille_alphabet.get(current_symbol, '?')  # Fallback for invalid symbols
                if capital_mode:
                    letter = letter.upper()
                    capital_mode = False
                result.append(letter)
        i += 6
    
    return ''.join(result)

def main():
    # Get input from the command line
    input_string = ' '.join(sys.argv[1:]).strip()
    
    if is_braille(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == '__main__':
    main()