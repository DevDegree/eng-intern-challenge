import sys

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


def text_to_braille(text: str) -> str:
    """
    Converts the given text (English) into Braille representation.
    
    Parameters:
    text (str): The input English text to be converted into Braille.

    Returns:
    str: The Braille representation of the input text.
    """
    result = []
    is_number = False
    for char in text:
        if char.isdigit():
            if not is_number:
                result.append(number_symbol)  # Add number symbol for digits
                is_number = True
            result.append(braille_numbers[char])
        elif char.isalpha():
            if is_number:
                is_number = False  # Switch back to alphabet mode
            if char.isupper():
                result.append(capital_symbol)  # Add capital symbol for uppercase letters
            result.append(braille_alphabet[char.lower()])
        elif char == ' ':
            result.append(braille_alphabet[' '])  # Add space in Braille
    return ''.join(result)


def get_braille_symbol(braille: str, index: int) -> str:
    """
    Extracts a Braille symbol from the Braille string.

    Parameters:
    braille (str): The Braille string.
    index (int): The starting index to extract the symbol.

    Returns:
    str: A 6-character Braille symbol.
    """
    return braille[index:index+6]


def process_capital_letter(braille: str, index: int) -> (str, int): # type: ignore
    """
    Processes a capital letter from the Braille string.

    Parameters:
    braille (str): The Braille string.
    index (int): The current index of the Braille string.

    Returns:
    (str, int): The capital letter and the updated index.
    """
    next_symbol = get_braille_symbol(braille, index + 6)
    for letter, braille_char in braille_alphabet.items():
        if braille_char == next_symbol:
            return letter.upper(), index + 12
    return '', index + 6  # Default return for safety


def process_number(symbol: str) -> str:
    """
    Converts a Braille symbol into the corresponding number.

    Parameters:
    symbol (str): The Braille symbol representing a number.

    Returns:
    str: The corresponding digit in string format.
    """
    for digit, braille_digit in braille_numbers.items():
        if braille_digit == symbol:
            return digit
    return ''  


def process_letter(symbol: str) -> str:
    """
    Converts a Braille symbol into the corresponding letter.

    Parameters:
    symbol (str): The Braille symbol representing a letter.

    Returns:
    str: The corresponding letter.
    """
    for letter, braille_char in braille_alphabet.items():
        if braille_char == symbol:
            return letter
    return ''  


def braille_to_text(braille: str) -> str:
    """
    Converts a Braille string back into English text.

    Parameters:
    braille (str): The Braille string to be converted.

    Returns:
    str: The English translation of the Braille string.
    """
    result = []
    index = 0
    length = len(braille)
    is_number = False

    while index < length:
        symbol = get_braille_symbol(braille, index)

        if symbol == number_symbol:
            is_number = True
            index += 6
            continue
        elif symbol == capital_symbol:
            letter, index = process_capital_letter(braille, index)
            result.append(letter)
            continue
        elif symbol == braille_alphabet[' ']:  
            result.append(' ')
            is_number = False  
            index += 6
            continue
        else:
            if is_number:
                digit = process_number(symbol)
                result.append(digit)
                index += 6
                continue
            else:
                letter = process_letter(symbol)
                result.append(letter)
                index += 6

    return ''.join(result)


def translate(input_str: str) -> str:
    """
    Detects whether the input string is English or Braille, 
    and translates accordingly.

    Parameters:
    input_str (str): The input string (either Braille or English).

    Returns:
    str: The translated output (Braille to English or English to Braille).
    """
    if all(c in 'O. ' for c in input_str):
        return braille_to_text(input_str)
    else:
        return text_to_braille(input_str)


def main():
    """
    Main function to be executed when the script is run from the command line.
    Reads the input from command-line arguments, translates it, and prints the result.
    """
    input = " ".join(sys.argv[1:])
    translation = translate(input)
    print(translation)


if __name__ == '__main__':
    main()
