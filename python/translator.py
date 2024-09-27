### imports
import sys

##  constants
# defining mappings since writing out the alphabet saves time and space compared to generating it
# mapping braille -> english
BRAILLE_TO_ENGLISH_ALPHABET = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", 
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "..OO.O": ".",
    "..O...": ",",
    "..O.OO": "?",
    "..OOO.": "!",
    "..OO..": ":",
    "..O.O.": ";",
    "....OO": "-",
    ".O..O.": "/",
    ".OO..O": "<",
    # "O..OO." : ">",
    "O.O..O": "(",
    ".O.OO.": ")"
}

BRAILLE_TO_NUMBER_ALPHABET = {
    "O.....": "1", 
    "O.O...": "2", 
    "OO....": "3", 
    "OO.O..": "4", 
    "O..O..": "5", 
    "OOO...": "6", 
    "OOOO..": "7", 
    "O.OO..": "8", 
    ".OO...": "9", 
    ".OOO..": "0"
}

# inverse mapping number -> braille
NUMBER_TO_BRAILLE_ALPHABET = {
    "1": "O.....", 
    "2": "O.O...", 
    "3": "OO....", 
    "4": "OO.O..", 
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

# inverse mapping english -> braille
# showoing dictionary comphrehension method, a little tedious to reverse the alphabet manually
ENGLISH_TO_BRAILLE_ALPHABET = {value: key for key ,value in BRAILLE_TO_ENGLISH_ALPHABET.items()}

SPACE_CHAR = "......"
CAPITAL_FOLLOWS = ".....O"
DECIMAL_FOLLOWS = ".O...O"
NUMBER_FOLLOWS = ".O.OOO"

# custom exception to handle invalid Braille input
class InvalidBrailleException(Exception):
    pass

## helper functions
def is_braille (s: str) -> bool:
    '''
    Check whether a string is a valid braille string
    
    Parameters:
        s (str): string to check
    
    Returns:
        (bool): True if s is a valid braille string, False otherwise
    '''
    return all(c in ".O" for c in s)

def translate_to_english (s: str) -> str:
    '''
    Translate a Braille string to English text.
    
    Parameters:
        s (str): Braille string to translate, where each character is represented by 6 chars (O or .).
    
    Returns:
        translated_string (str): The translated English text.
    
    Special Handling:
        - Capital letters: When the CAPITAL_FOLLOWS Braille symbol is found, the next letter will be capitalized.
        - Numbers: When the NUMBER_FOLLOWS Braille symbol is found, subsequent Braille characters are interpreted as digits until a space is found.
        - Decimal points: When the DECIMAL_FOLLOWS Braille symbol is encountered, a decimal point is added immediately.
    '''
    translated_string = ""
    capitalize = False # capitalize next word
    number = False # just until the space is found
    decimal = False # add decimal point immediately
    i = 0
    
    while i < len(s):
       
        # grab the current 6 characters
        braille_char = s[i:i+6] 

        # check for special cases
        if braille_char == CAPITAL_FOLLOWS:
            capitalize = True
        elif braille_char == DECIMAL_FOLLOWS:
            decimal = True
        elif braille_char == NUMBER_FOLLOWS:
            number = True
        elif braille_char == SPACE_CHAR:
            number = False
            translated_string += " "
        else:
            if decimal: 
                translated_string += "."
                decimal = False
                continue

            letter = BRAILLE_TO_NUMBER_ALPHABET[braille_char] if number else BRAILLE_TO_ENGLISH_ALPHABET[braille_char]
            
            if capitalize:
                letter = letter.upper()
                capitalize = False
            
            translated_string += letter
        # print(braille_char, " -> ", translated_string)
        i += 6

    return translated_string

def translate_to_braille (s: str) -> str:
    '''
    Translate an English string to Braille.
    
    Parameters:
        s (str): English string to translate to Braille.
    
    Returns:
        translated_string (str): The translated Braille string where each English character is represented by 6 dots (O or .).
    
    Special Handling:
        - Capital letters: When an uppercase letter is encountered, the CAPITAL_FOLLOWS symbol is added before it.
        - Numbers: When a digit is encountered, the NUMBER_FOLLOWS symbol is added before the corresponding Braille representation of the number.
        - Decimal points: When a decimal point is encountered, the DECIMAL_FOLLOWS symbol is added.
    '''
    translated_string = ""
    in_number_sequence = False
    for char in s:
        
        if char.isupper():
            translated_string += CAPITAL_FOLLOWS
            translated_string += ENGLISH_TO_BRAILLE_ALPHABET[char.lower()] 
        
        elif char.isdigit():
            # only add number follows symbol if it's the first time we see a numerical sequence
            if not in_number_sequence:
                translated_string += NUMBER_FOLLOWS
                in_number_sequence = True
            translated_string += NUMBER_TO_BRAILLE_ALPHABET[char]

        # check if the '.' sign comes from a decimal point and not a full stop
        elif char == "." and in_number_sequence:
            translated_string += DECIMAL_FOLLOWS
            
        elif char == " ":
            translated_string += SPACE_CHAR
            # if a non-digit is found, then we are no longer in a number sequence
            # the end of number is sequence is marked by a space
            in_number_sequence = False
        else:
            # if a non-digit is found, then we are no longer in a number sequence
            # the end of number is sequence is marked by a space
            in_number_sequence = False
            translated_string += ENGLISH_TO_BRAILLE_ALPHABET[char]
    return translated_string


## main function
def main (s: str) -> None:
    '''
    Translate a braille string to english or vice versa
    
    Parameters:
        s (str): braille string to translate
    
    Raises:
        InvalidBrailleException: If the input is invalid
    
    Returns:
        void function, just prints the translated string
    '''
    if is_braille(s):
        # check for case when input is Braille but dstring is not a multiple of 6 chars
        if len(s) % 6 != 0:
            raise InvalidBrailleException("Invalid input")
        
        # braille -> english
        print(translate_to_english(s))
    else:
        # check for case when input string only has Braille chars .O but also has spaces -> not English
        cleaned_s = s.replace(" ", "")
        if is_braille(cleaned_s):
            # invalid input
            raise InvalidBrailleException("Invalid input")
        
        # english -> braille
        print(translate_to_braille(s))


if __name__ == "__main__":
    import sys
    # retrieve the list of all the command line arguments and join them with a space
    input_string = ' '.join(sys.argv[1:])
    main(input_string)


