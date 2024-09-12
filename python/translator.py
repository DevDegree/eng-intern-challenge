# Braille mappings for letters, numbers, and symbols
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

capital_symbol = '.....O'
number_symbol = '.O.OOO'

# Convert from English to Braille
def text_to_braille(text: str) -> str:
    result = []
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(number_symbol)  
                is_number = True
            result.append(braille_numbers[char])
        elif char.isalpha():
            if is_number:
                is_number = False  
            if char.isupper():
                result.append(capital_symbol)
            result.append(braille_alphabet[char.lower()])
        elif char == ' ':
            result.append(braille_alphabet[' '])
    return ''.join(result)


# Helper function to get the next Braille symbol (6 characters)
def get_braille_symbol(braille: str, index: int) -> str:
    return braille[index:index+6]

# Helper function to process a capital letter from Braille
def process_capital_letter(braille: str, index: int) -> (str, int):
    next_symbol = get_braille_symbol(braille, index + 6)
    for letter, braille_char in braille_alphabet.items():
        if braille_char == next_symbol:
            return letter.upper(), index + 12
    return '', index + 6  # Default return for safety

# Process a number from Braille
def process_number(symbol: str) -> str:
    for digit, braille_digit in braille_numbers.items():
        if braille_digit == symbol:
            return digit
    return ''  

# Process a letter from Braille
def process_letter(symbol: str) -> str:
    for letter, braille_char in braille_alphabet.items():
        if braille_char == symbol:
            return letter
    return ''  

# Main function to convert from Braille to English
def braille_to_text(braille: str) -> str:
    result = []
    index = 0
    length = len(braille)
    is_number = False

    while index < length:
        symbol = get_braille_symbol(braille, index)

        if symbol == number_symbol:
            is_number = True
            index += 6
        elif symbol == capital_symbol:
            letter, index = process_capital_letter(braille, index)
            result.append(letter)
        else:
            if is_number:
                digit = process_number(symbol)
                result.append(digit)
                index += 6  # Move past the current number
                continue
            else:
                letter = process_letter(symbol)
                result.append(letter)
            index += 6

    return ''.join(result)


# translate the text to braille and vice versa afetr Checking if input is in braille or plain text
def translate(input_str: str) -> str:

    if all(c in 'O. ' for c in input_str):
        return braille_to_text(input_str)
    else:
        return text_to_braille(input_str)

# Main function for command line argument
if __name__ == "__main__":
    text = input()

    translated_text = translate(text)

    print(translated_text)

