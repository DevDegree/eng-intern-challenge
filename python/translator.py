import sys

CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE_BRAILLE = '......'

CHAR_TO_BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',
}

INT_SYMBOL_TO_BRAILLE_MAP = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', '.': '..OO.O', ',': '..O...', 
    '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', 
    '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': SPACE_BRAILLE
}

BRAILLE_TO_CHAR_MAP = {v: k for k, v in CHAR_TO_BRAILLE_MAP.items()}
BRAILLE_TO_INT_SYMBOL_MAP = {v: k for k, v in INT_SYMBOL_TO_BRAILLE_MAP.items()}


def is_brail(input: str) -> bool:
    """
    Determine if the input string is in Braille or English.
    
    Parameters:
    input (str): The string to check.

    Returns:
    bool: True if the input is in Braille, False otherwise.
    """
    # Check if the length of the string is a multiple of 6 and contains only '.' and 'O'
    if len(input) % 6 == 0 and all(c in ['.', 'O'] for c in input):
        return True

    return False


def braille_to_english(input: str) -> str:
    """
    Translate a Braille string into its English equivalent.
    
    Parameters:
    input (str): The Braille string to translate.

    Returns:
    str: The translated English string.
    """
    res = ""
    is_capital = False
    number_follows = False

    for i in range(0, len(input), 6):

        # Check if the next characters are numbers
        if input[i:i+6] == NUMBER_FOLLOWS:
            number_follows = True

        # Check if the next character is capital
        elif input[i:i+6] == CAPITAL_FOLLOWS:
            is_capital = True
        
        # Check for spaces
        elif input[i:i+6] in BRAILLE_TO_INT_SYMBOL_MAP and BRAILLE_TO_INT_SYMBOL_MAP[input[i:i+6]] == ' ':
            res += ' '
            number_follows = False

        # Translate numbers
        elif input[i:i+6] in BRAILLE_TO_INT_SYMBOL_MAP and number_follows:
            res += BRAILLE_TO_INT_SYMBOL_MAP[input[i:i+6]]
        
        # Translate letters
        elif input[i:i+6] in BRAILLE_TO_CHAR_MAP:
            char = BRAILLE_TO_CHAR_MAP[input[i:i+6]]
            if is_capital:
                char = char.upper()
                is_capital = False
            res += char
        
        # Translate symbols
        elif input[i:i+6] in BRAILLE_TO_INT_SYMBOL_MAP:
            res += BRAILLE_TO_INT_SYMBOL_MAP[input[i:i+6]]

        else:
            raise ValueError(f"Unsupported Braille character: {input[i:i+6]}")
    
    return res

def english_to_braille(input: str) -> str:
    """
    Translate an English string into its Braille equivalent.
    
    Parameters:
    input (str): The English string to translate.

    Returns:
    str: The translated Braille string.
    """
    res = ""
    number_follows = False

    for char in input:

        # Translate letters
        if char.isalpha():
            if char.isupper():
                res += CAPITAL_FOLLOWS
            res += CHAR_TO_BRAILLE_MAP[char.lower()]
        
        # Translate digits
        elif char.isdigit():
            if not number_follows:
                res += NUMBER_FOLLOWS
                number_follows = True
            res += INT_SYMBOL_TO_BRAILLE_MAP[char]
        
        # Translate spaces
        elif char == ' ':
            number_follows = False
            res += SPACE_BRAILLE
        
        # Translate symbols
        else:
            if char not in CHAR_TO_BRAILLE_MAP and char not in INT_SYMBOL_TO_BRAILLE_MAP:
                raise ValueError(f"Invalid character: {char}")
            
            res += INT_SYMBOL_TO_BRAILLE_MAP[char]

    return res


def main(input: str) -> str:
    """
    Determine if the input string is Braille or English and translate it accordingly.
    
    Parameters:
    input (str): The string to translate, either in Braille or English.

    Returns:
    str: The translated string in the opposite format (Braille to English or English to Braille).
    """
    if is_brail(input):
        return braille_to_english(input)
    else:
        return english_to_braille(input)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inputs = sys.argv[1:]
        inputs = " ".join(inputs)
        print(main(inputs))
    else:
        print("Usage: python3 translator.py <input1> <input2> ... <inputN>")
        sys.exit(1)
