import sys

# Constants for special characters
CAPITAL = ".....O"
NUMBER = ".O.OOO"
SPACE = "......"

# Maps between English alphabets and Braille alphabets
ALPHABET_TO_BRAILLE = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
}

BRAILLE_TO_ALPHABET = {v: k for k, v in ALPHABET_TO_BRAILLE.items()}

# Maps between digits and Braille alphabets
DIGIT_TO_BRAILLE = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
}

BRAILLE_TO_DIGIT = {v: k for k, v in DIGIT_TO_BRAILLE.items()}

# Common exceptions raised in the program
INVALID_BRAILLE_CHARACTER_ERROR = Exception("Invalid braille character")
INVALID_ENGLISH_CHARACTER_ERROR = Exception("Invalid english character")
EMPTY_INPUT_ERROR = Exception("No input is provided")

def check_is_braille(input: str) -> bool:
    """Checks if the input string is in Braille

    Args:
        input (str): the input string

    Returns:
        bool: whether the input string is in Braille
    """
    # "." is not part of the English character set and all Braille characters contain at least one empty dot
    return "." in input

def translate_english_to_braille(input: str) -> str:
    """Translates English text to Braille

    Args:
        input (str): the English text to be translated

    Returns:
        str: the Braille translation of the input text
    """
    braille_translation = ""
    is_digit = False
    
    def translate_english_to_braille_token(character: str, is_digit: bool = False) -> str:
        """Translates a single English character to its Braille representation

        Args:
            character (str): the English character to be translated
            is_digit (bool, optional): whether the character is a digit. Defaults to False.

        Returns:
            str: the Braille representation of the character

        Raises:
            INVALID_ENGLISH_CHARACTER_ERROR: if the character cannot be translated to Braille
        """
        if is_digit:
            braille_token = DIGIT_TO_BRAILLE[character]
            if braille_token == None:
                raise INVALID_ENGLISH_CHARACTER_ERROR
            return braille_token
        
        braille_token = ALPHABET_TO_BRAILLE[character.lower()]
        if braille_token == None:
            raise INVALID_ENGLISH_CHARACTER_ERROR
        if character.isupper():
            braille_token = CAPITAL + braille_token
        return braille_token
    
    for character in input:
        if character == " ":
            is_digit = False
            braille_translation += SPACE
        elif character.isdigit():
            if is_digit:
                braille_translation += translate_english_to_braille_token(character, True)
            else: 
                is_digit = True
                braille_translation += NUMBER + translate_english_to_braille_token(character, True)
        else:
            is_digit = False
            braille_translation += translate_english_to_braille_token(character, False)
    
    return braille_translation

def translate_braille_to_english(input: str) -> str:
    """Translates Braille text to English

    Args:
        input (str): the Braille text to be translated

    Returns:
        str: the English translation of the input text
    """
    english_translation = ""
    is_capital = False
    is_decimal = False
    
    def translate_braille_token_to_english(braille_token: str, is_capital: bool = False, is_decimal: bool = False) -> str: 
        """Translates a single Braille token to its English representation

        Args:
            braille_token (str): the Braille token to be translated
            is_capital (bool, optional): whether the token represents a capital letter. Defaults to False.
            is_decimal (bool, optional): whether the token represents a digit. Defaults to False.

        Returns:
            str: the English representation of the Braille token

        Raises:
            INVALID_BRAILLE_CHARACTER_ERROR: if the Braille token cannot be translated to English
        """
        if is_decimal:
            digit = BRAILLE_TO_DIGIT[braille_token]
            if digit == None:
                raise INVALID_BRAILLE_CHARACTER_ERROR
            return digit
        
        char = BRAILLE_TO_ALPHABET[braille_token]
        if char == None:
            raise INVALID_BRAILLE_CHARACTER_ERROR
        if is_capital:
            char = char.capitalize()
        return char
    
    for start_index in range(0, len(input), 6):
        end_index = start_index + 6
        braille_token = input[start_index:end_index]
        if braille_token == SPACE:
            is_capital = False
            is_decimal = False
            english_translation += " "
        elif braille_token == NUMBER:
            is_decimal = True
        elif braille_token == CAPITAL:
            is_capital = True
        else:
            english_translation += translate_braille_token_to_english(braille_token, is_capital, is_decimal)
            is_capital = False
    
    return english_translation

def main():
    input = ""
    if len(sys.argv) > 1:
        input = " ".join(sys.argv[1:])
    else:
        raise EMPTY_INPUT_ERROR
    
    is_braille = check_is_braille(input)
    translated_text = ""
    if is_braille:
        translated_text = translate_braille_to_english(input)
    else:
        translated_text = translate_english_to_braille(input)
        
    print(translated_text)
        

if __name__ == "__main__":
    main()
