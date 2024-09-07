import sys 


# Define symbols for following char being capital, decimal, or number
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"
SPACE = "......"

# Define Braille alphabet for translation
braille_to_letter = {
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

braille_to_number = {
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

letters_to_braille = {v: k for k, v in braille_to_letter.items()}
numbers_to_braille = {v: k for k, v in braille_to_number.items()}


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


def braille_to_english(braille_string: str) -> str:
    """
    Translates Braille text into English text.
    
    Args:
        braille_string (str): Braille text to be translated into English.
        
    Returns:
        str: English translation of the given Braille text.
    """
    
    translated_string = []
    i = 0
    is_number = False  # Flag to indicate next char is number
    is_capital = False  # Flag to indicate next char is capital
    
    while i < len(braille_string):
        current_char = braille_string[i:i+6]
        
        # Handle special chars and modes
        if current_char == SPACE:
            translated_string.append(" ")
        elif current_char == CAPITAL_FOLLOWS:
            is_capital = True
        elif current_char == NUMBER_FOLLOWS:
            is_number = True
        # Handle regular braille translation of letters and numbers
        else:
            if is_number and current_char in braille_to_number:
                translated_string.append(braille_to_number[current_char])
            elif is_capital:
                translated_string.append(braille_to_letter[current_char].upper())
                is_capital = False
            else:
                translated_string.append(braille_to_letter[current_char])
                
        i += 6  # Read next char
        
    return "".join(translated_string)
                

def english_to_braille(braille_string: str) -> str:
    pass
    

if __name__ == "__main__":
    # Get command line args as one string
    string_input = sys.argv[1:]
    combined_imput = " ".join(string_input)
    translation_mode = determine_translation_mode(combined_imput)
    
    if translation_mode == "braille-to-english":
        result = braille_to_english(combined_imput)
    else:
        result = english_to_braille(combined_imput)
        
    print(result)
    
    
