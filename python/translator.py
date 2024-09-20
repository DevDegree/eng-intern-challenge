from sys import argv

ENGLISH_TO_BRAILLE = {
    '!': '..OOO.', 
    '?': '..OO.O', 
    '.': '..OO.O', 
    ',': '..O...', 
    ':': '..OO..', 
    ';': '..O.O.', 
    '-': '....OO', 
    '/': '.O..O.', 
    "(": "O.O..O",
    ")": ".O.OO.",
    "<": ".OO..O",
    ">": "O..OO.",
    'a': 'O.....', 
    'b': 'O.O...', 
    'c': 'OO....', 
    'd': 'OO.O..', 
    'e': 'O..O..', 
    'f': 'OOO...', 
    'g': 'OOOO..', 
    'h': 'O.OO..', 
    'i': '.OO...', 
    'j': '.OOO..', 
    'k': 'O...O.', 
    'l': 'O.O.O.', 
    'm': 'OO..O.', 
    'n': 'OO.OO.', 
    'o': 'O..OO.', 
    'p': 'OOO.O.', 
    'q': 'OOOOO.', 
    'r': 'O.OOO.',
    's': '.OO.O.', 
    't': '.OOOO.', 
    'u': 'O...OO', 
    'v': 'O.O.OO', 
    'w': '.OOO.O', 
    'x': 'OO..OO', 
    'y': 'OO.OOO', 
    'z': 'O..OOO',
    ' ': '......',
    'capital_next': '.....O', 
    'decimal_next': '.O...O', 
    'number_next': '.O.OOO'
}

NUMBER_TO_BRAILLE = {
    '0': '.OOO..', 
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...',
}
#reversing to get braille to english map
BRAILLE_TO_ENGLISH = {val : key for key, val in ENGLISH_TO_BRAILLE.items()}

BRAILLE_TO_NUMBER = {val : key for key, val in NUMBER_TO_BRAILLE.items()}

def convert_to_english(string: str) -> str:
    """
    This function converts a braille input to english.

    Args:
        string (str): The input braille string

    Returns:
        str: The converted english string
    """
    res_string = ''
    number_follows = False
    decimal_follows = False
    capital_follows = False
    
    # get each braille symbol of size 6
    for i in range(0, len(string), 6):
        braille_symbol = string[i: i + 6]
        #check to see if next symbol will be capital, decimal or number
        if BRAILLE_TO_ENGLISH[braille_symbol] == 'number_next':
            number_follows = True
            
        elif BRAILLE_TO_ENGLISH[braille_symbol] == 'decimal_next':
            decimal_follows = True
            
        elif BRAILLE_TO_ENGLISH[braille_symbol] == 'capital_next':
            capital_follows = True
        
        else:
            # At this point, we want to append to the result string
            if braille_symbol == '......': # want to hard code this case to switch from number to english after space
                res_string += BRAILLE_TO_ENGLISH[braille_symbol]
                number_follows = False
            
            elif decimal_follows:
                res_string += BRAILLE_TO_ENGLISH[braille_symbol]
                decimal_follows = False
                               
            elif number_follows:
                res_string += BRAILLE_TO_NUMBER[braille_symbol] # don't want to set number_follows to false in case of consecutive numbers
                
                
            elif capital_follows:
                res_string += BRAILLE_TO_ENGLISH[braille_symbol].upper()
                capital_follows = False
                
            else:
                res_string += BRAILLE_TO_ENGLISH[braille_symbol]
                   
    return res_string

def convert_to_braille(string: str) -> str:
    """
    This function converts an english input to braille

    Args:
        string (str): The english input string

    Returns:
        str: The converted braille string
    """
    res_string = ''
    is_num = False
    
    for char in string:
        if char.isdigit():
            if not is_num:
                is_num = True
                res_string += ENGLISH_TO_BRAILLE['number_next'] # for the first number, we also want to add number indicator
            
            res_string += NUMBER_TO_BRAILLE[char]
            
        elif char.isupper():            
            is_num = False
            res_string += ENGLISH_TO_BRAILLE['capital_next'] # want to add capital indication
            res_string += ENGLISH_TO_BRAILLE[char.lower()]
        
        elif char == '.':
            is_num = False
            res_string += ENGLISH_TO_BRAILLE['decimal_next'] # want to add decimal indication
            res_string += ENGLISH_TO_BRAILLE[char]

        else:
            is_num = False
            res_string += ENGLISH_TO_BRAILLE[char]
            
    return res_string
            
    
def is_english(string: str) -> bool:
    """
    This function returns wether the given input is braille or english

    Args:
        string (str): The input string from the command line

    Returns:
        bool: True if input is english, otherwise false
    """
    for char in string:
        if char != '.' and char != 'O':
            return True
    
    return False

def is_english_valid(string: str) -> bool:
    """
    This function checks if the english input string contains valid characters

    Args:
        string (str): The input english string

    Returns:
        bool: True if input string is valid, false otherwise
    """
    allowed = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()<>.,?!:;-/ ")
    for char in string:
        if char not in allowed:
            return False
    return True

def main():
    if len(argv) < 2:
        return
    
    string = ' '.join(argv[1:])
    
    if is_english(string):
        # input is english
        if not is_english_valid(string):
            print("invalid english string")
            return 
        braille_string = convert_to_braille(string)
        print(braille_string)
    else:
        # input is braille
        if len(string) % 6 != 0: # checks if braille input is valid
            print("invalid braille string")
            return
        
        english_string = convert_to_english(string)
        print(english_string)
    
if __name__ == "__main__":
    main()

