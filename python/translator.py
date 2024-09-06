import sys 

# braille_alphabet: Dictionary
# Maps English letters, numbers, and special symbols to their corresponding Braille pattersn.
# Note: Each Braille character is represented using 6 characters (either 'O' or '.'), where 'O' represents a raised dot
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
    'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
    'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    'cap': '.....O', 'num': '.O.OOO',
    ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

english_alphabet = {v: k for k, v in braille_alphabet.items()}

def is_braille(input_str : str) -> bool:
    """
    Inputs:
    - input_str (str): A string (potentially representing Braille)

    Outputs:
    - bool: Returns True if the string contains only valid Braille characters ('O' and '.') and,
    - is a multiple of 6 characters long.

    Description:
    - Checks if all characters in the input are either 'O' or '.'.
        - Verifies if the length of the input string is divisible by 6, as each Braille character is represented by 6 dots.
    """
    return all(ch in 'O.' for ch in input_str) and len(input_str) % 6 == 0

def braille_to_english(braille):
    """
    Inputs:
        - braille (str): A string containing Braille symbols.
    Outputs:
        - str: Returns the English translation of the input Braille string.
    
    Description:
        - Initializes two flags: 'is_cap' for capitalization and 'is_num' for numbers.
        - Processes the input Braille string in chunks of 6 characters.
        - If 'cap' is encountered, sets the capitalization flag.
        - If 'num' is encountered, sets the number flag.
        - Translates each 6-character Braille symbol into the corresponding English character using the 'english_alphabet' dictionary.
        - Handles spaces, capitalization, and number mode appropriately.
        - Joins and returns the list of translated English characters as a string.
    """
    english = []
    is_cap = False
    is_num = False
    for i in range(0, len(braille), 6):
        symbol = braille[i : i + 6]
        if symbol == braille_alphabet['cap']:
            is_cap = True
            continue
        if symbol == braille_alphabet['num']:
            is_num = True
            continue
        if symbol == '......':
            english.append(' ')
            is_cap = False
            is_num = False
            continue
        char = english_alphabet.get(symbol, '')
        if is_num:
            english.append(char)
        else:
            if is_cap:
                english.append(char.upper())
            else:
                english.append(char)
            is_cap = False
    return ''.join(english)


def english_to_braille(english):
    """
    Accepts:
        - english (str): A string containing English text.
    Outputs:
        - str: Returns the Braille translation of the input English string.
    
    Description:
        - Initializes the 'is_num' flag for managing number mode.
        - Processes each character of the input English string.
        - If a digit is encountered, switches to number mode and prepends the 'num' symbol.
        - If an uppercase letter is encountered, prepends the 'cap' symbol and converts the letter to lowercase.
        - Looks up each character in 'braille_alphabet' and appends the corresponding Braille symbol.
        - Joins and returns the Braille symbols as a single string.
    """
    braille = []
    is_num = False
    for char in english:
        if char.isdigit() and not is_num:
            braille.append(braille_alphabet['num'])
            is_num = True
        elif char.isalpha() and is_num:
            is_num = False
        if char.isupper():
            braille.append(braille_alphabet['cap'])
            char = char.lower()
        braille.append(braille_alphabet.get(char, '......'))  
    return ''.join(braille)

def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
