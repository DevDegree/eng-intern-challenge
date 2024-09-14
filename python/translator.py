import sys

BRAILLE_DICT = {
    'O.....': 'a',  
    'O.O...': 'b',  
    'OO....': 'c',  
    'OO.O..': 'd',  
    'O..O..': 'e',  
    'OOO...': 'f',  
    'OOOO..': 'g',  
    'O.OO..': 'h',  
    '.OO...': 'i',  
    '.OOO..': 'j',  
    'O...O.': 'k',  
    'O.O.O.': 'l',  
    'OO..O.': 'm',  
    'OO.OO.': 'n',  
    'O..OO.': 'o',  
    'OOO.O.': 'p',  
    'OOOOO.': 'q',  
    'O.OOO.': 'r',  
    '.OO.O.': 's',  
    '.OOOO.': 't',  
    'O...OO': 'u',  
    'O.O.OO': 'v',  
    '.OOO.O': 'w',  
    'OO..OO': 'x',  
    'OO.OOO': 'y',  
    'O..OOO': 'z',
    '.....O': 'capital',
    '.O.OOO': 'number',
    '......': ' ',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '_',
    '.O..O.': '/',
    'O.O..O': '(',
    '.O.OO.': ')',
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0'
}
ENG_DICT = {value: key for key, value in BRAILLE_DICT.items()}

def to_english(input: str) -> str:
    """
    Converts a Braille-encoded string into its corresponding English string.

    Args:
        input (str): A string of Braille characters (O and .), where each Braille character is 
                     represented by a 6-character string.

    Returns:
        str: The corresponding English translation of the input Braille string.
    
    Raises:
        ValueError: If an invalid Braille sequence is encountered.
    """
    english = []
    special = 0  # 0: none, 1: capital, 2: number

    
    for i in range(0, len(input), 6):
        braille = input[i:i+6]
        if braille in BRAILLE_DICT:
            braille = BRAILLE_DICT[braille]
            if braille == 'capital':
                special = 1
            elif braille == 'number':
                special = 2
            elif braille == ' ':
                special = 0
                english.append(' ')
            else:
                match special:
                    case 1:
                        braille = braille.upper()
                        special = 0
                    case 2:
                        braille = BRAILLE_DICT[braille] #translate to num        
                english.append(braille)
        else:
            raise ValueError(f"Invalid Braille sequence: {braille}")
    return ''.join(english)
            

def to_braille(input: str) -> str:
    """
    Converts an English string into its corresponding Braille-encoded string.

    Args:
        input (str): An English string containing letters, numbers, and punctuation.

    Returns:
        str: The corresponding Braille translation of the input English string.
    
    Raises:
        ValueError: If a character in the input string cannot be translated to Braille.
    """
    braille = []
    num = False

    for char in input:
        if char.isupper():
            braille.append(ENG_DICT['capital'])
            char = char.lower()
        if char.isdigit():
            if not num:
                braille.append(ENG_DICT['number'])
                num = True
            braille.append(ENG_DICT[ENG_DICT[char]])
        else:
            num = False
            if char not in ENG_DICT:
                raise ValueError(f"Character '{char}' not found in Braille dictionary.")
            braille.append(ENG_DICT[char])
    return ''.join(braille)
            

def braille_or_english(input: str) -> None:
    """
    Determines if the input string is in Braille or English, and converts it accordingly.

    Args:
        input (str): A string in either Braille or English.

    Prints:
        str: The translated string, either from Braille to English or vice versa.
    """
    if (all(char in {'O', '.'} for char in input)):
        translated = to_english(input)
        sys.stdout.write(translated)
    else:
        translated = to_braille(input)
        sys.stdout.write(translated)

if __name__ == '__main__':
    """
    Command-line interface for translating between Braille and English.
    
    Usage:
        python script.py <input_string>
    
    The script automatically detects whether the input is Braille or English 
    and performs the corresponding translation.
    """
    if len(sys.argv) < 2:
        sys.exit("No argument Found")
    else:
        user_input = ' '.join(sys.argv[1:])
        try:
            braille_or_english(user_input)
        except ValueError as e:
            sys.exit(f"Error: {e}")
