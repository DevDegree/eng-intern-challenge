import sys

# Braille to English dictionaries or vice versa
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', '^': '.....O', '#': '.O.OOO', 
    ' ': '......', 
    
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', 
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '(': 'O.O..O', ')': '.O.OO.'
} # '>': 'O..OO.',
braille_number = {
    '1': braille_alphabet['a'], '2': braille_alphabet['b'], 
    '3': braille_alphabet['c'], '4': braille_alphabet['d'], 
    '5': braille_alphabet['e'], '6': braille_alphabet['f'], 
    '7': braille_alphabet['g'], '8': braille_alphabet['h'], 
    '9': braille_alphabet['i'], '0': braille_alphabet['j']
}
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_number = {v: k for k, v in braille_number.items()}

def is_braille(s: str) -> bool:
    """
    Check if the input string is valid Braille.
    
    Args:
        s (str): 
            The input string to check.

    Returns:
        bool: 
            True if the string is a valid Braille sequence, False otherwise.
    """
    valid_char = set('O.')

    for i in s:
        if i not in valid_char:
            return False
        
    return len(s) % 6 == 0

def braille_to_english(braille_str: str) -> str:
    """
    Translate a Braille string to English.

    Args:
        braille_str (str): 
            The input Braille string, where each 
            character is represented by 6 symbols.

    Returns:
        str: The translated English string.
    """
    output = ''
    input_size = len(braille_str) // 6
    number_follows = False
    capital_follows = False

    for i in range(input_size):
        symbol = english_alphabet[braille_str[i*6:i*6+6]]

        if symbol == '^':
            capital_follows = True
            continue
        elif symbol == '#':
            number_follows = True
            continue
        elif symbol == ' ':
            number_follows = False

        if number_follows:
            output += english_number[braille_str[i*6:i*6+6]]
        elif capital_follows:
            output += symbol.upper()
            capital_follows = False
        else:
            output += symbol

    return output

def english_to_braille(arguments: list[str]) -> str:
    """
    Translate an English string to Braille.

    Args:
        arguments (list[str]): 
            A list where the first element is the program 
            name and the rest are words to be translated.

    Returns:
        str: The translated Braille string.
    """
    output = ''
    first_number = True

    for word in arguments[1:]:
        for char in word:

            if char.isdigit():
                if first_number:
                    output += braille_alphabet['#']
                    first_number = False
                output += braille_number[char]
            elif char.isupper():
                output += braille_alphabet['^'] + braille_alphabet[char.lower()]
            else:
                output += braille_alphabet[char]

        output += braille_alphabet[' ']
        first_number = True

    return output[:len(output)-6]

def translator(arguments: list[str]) -> str:
    """
    Determines whether input is Braille or English, then translates accordingly.

    Args:
        arguments (list[str]): 
            The list of input args, either a Braille string or English words.

    Returns:
        str: 
            The translated string, either from Braille to English or vice versa.
    """
    if len(arguments) <= 1:
        return 'Error: No input provided.'
    
    if is_braille(arguments[1]):
        return braille_to_english(arguments[1])
    else:
        return english_to_braille(arguments)

if __name__ == '__main__':
    """
    Entry point of program. Reads input arguments and prints translated result.
    """
    print(translator(sys.argv))
