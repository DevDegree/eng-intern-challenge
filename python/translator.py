import sys

# Dictionary for alphabetic characters to braille
alpha_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
}

# Dictionary for numbers to braille
numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..'
}

# Reverse lookup dictionaries
braille_to_letter = {v: k for k, v in alpha_to_braille.items()}
braille_to_number = {v: k for k, v in numbers.items()}

# Function to check if input is braille or regular string
def is_braille(string):
    return all(char in 'O.' for char in string.replace(" ", ""))

# Translate string to braille without spaces
def print_string_to_braille(string):
    result = []
    is_number = False
    
    for char in string:
        if char.isdigit():
            if not is_number:  # Insert 'number' symbol only once before a sequence of digits
                result.append(alpha_to_braille['number'])
                is_number = True
            result.append(numbers[char])  # Translate the digit
        elif char.isalpha():
            is_number = False  # Reset number mode when a letter appears
            if char.isupper():
                result.append(alpha_to_braille['capital'])
                char = char.lower()
            result.append(alpha_to_braille[char])  # Translate the letter
        else:
            result.append(alpha_to_braille[char])  # Handle spaces or any other special char
    
    return "".join(result)  # Join without spaces between braille characters

# Translate braille to alphabet
def print_braille_to_alphabet(string):
    result = []
    is_capital = False
    is_number = False

    # Split into 6-character braille symbols
    braille_letters = string.split()

    for symbol in braille_letters:
        if symbol == alpha_to_braille['capital']:
            is_capital = True
        elif symbol == alpha_to_braille['number']:
            is_number = True
        elif is_number:
            result.append(braille_to_number.get(symbol, ''))
            if symbol == '......':  # Handle spaces
                is_number = False
        else:
            letter = braille_to_letter.get(symbol, '')
            if is_capital:
                letter = letter.upper()
                is_capital = False
            result.append(letter)
    
    return "".join(result)

def main():
    # Combine all arguments passed to the script into one input string
        input_string = " ".join(sys.argv[1:])

        # Determine if the input is braille or regular text
        if is_braille(input_string):
            print(print_braille_to_alphabet(input_string))
        else:
            print(print_string_to_braille(input_string))


if __name__ == '__main__':
    main()

