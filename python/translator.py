import sys 


# Define symbols for following char being capital, decimal, or number
CAPITAL_FOLLOWS = "....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

# Define Braille alphabet for translation
braille_to_letters = {
    'O.....' : 'a', 
    'O.O...' : 'b',
    'OO....' : 'c',
    'OO.O..' : 'd',
    'O..O..' : 'e',
    'OOO...' : 'f',
    'OOOO..' : 'g',
    'O.OO..' : 'h',
    '.OO...' : 'i',
    '.OOO..' : 'j',
    'O...O.' : 'k',
    'O.O.O.' : 'l',
    'OO..O.' : 'm',
    'OO.OO.' : 'n',
    'O..OO.' : 'o',
    'OOO.O.' : 'p',
    'OOOOO.' : 'q',
    'O.OOO.' : 'r',
    '.OO.O.' : 's',
    '.OOOO.' : 't',
    'O...OO' : 'u',
    'O.O.OO' : 'v',
    '.OOO.O' : 'w',
    'OO..OO' : 'x',
    'OO.OOO' : 'y',
    'O..OOO' : 'z', 
}

braille_to_numbers = {
    'O.....' : '1',
    'O.O...' : '2',
    'OO....' : '3',
    'OO.O..' : '4',
    'O..O..' : '5',
    'OOO...' : '6',
    'OOOO..' : '7',
    'O.OO..' : '8',
    '.OO...' : '9',
    '.OOO..' : '0',
}

letters_to_braille = {v: k for k, v in braille_to_letters.items()}
numbers_to_braille = {v: k for k, v in braille_to_numbers.items()}


def determine_translation_mode(string_input: str) -> str:
    """
    Determines the translation mode based on the characters in the input string.
    If the string contains only 'O', '.', or ' ', the translation mode is 'braille-to-english', otherwise it is 'english-to-braille'.
    
    Args:
        string_input (str): Input string to determine the translation mode.
    
    Returns:
        str: 'braille-to-english' if string only contains Braille characters, otherwise 'english-to-braille'
    """
    
    is_braille = all(c in ['O', '.', ' '] for c in string_input)
    return "braille-to-english" if is_braille else "english-to-braille"
    

if __name__ == "__main__":
    # Get command line args as one string
    string_input = sys.argv[1:]
    combined_imput = " ".join(string_input)
    translation_mode = determine_translation_mode(combined_imput)
    print(translation_mode)
    
