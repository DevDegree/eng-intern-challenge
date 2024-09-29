import sys

# Mapping English to Braille
ENGLISH_ALPHABET_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO"
}

ENGLISH_NUMBER_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO..."
}

ENGLISH_SPECIAL_TO_BRAILLE = {
    "Capital Follows": ".....O", "Number Follows": ".O.OOO", "Space": "......"
}

# Reverse mapping (Braille to English)
BRAILLE_TO_ENGLISH_ALPHABET = {braille: english for english, braille in ENGLISH_ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_ENGLISH_NUMBER = {braille: number for number, braille in ENGLISH_NUMBER_TO_BRAILLE.items()}
BRAILLE_TO_ENGLISH_SPECIAL = {braille: special for special, braille in ENGLISH_SPECIAL_TO_BRAILLE.items()}


def is_braille(input_str: str) -> bool:
    """
    Checks if the input string is in Braille.

    Args:
        input_str (str): A Braille or English string.

    Returns:
        bool: True if input_str is Braille, False if input_str is English.
    """
    for c in input_str:
        if c != "." and c != "O":
            return False
    return True

def translate_to_english(braille_str: str) -> str:
    """
    Translates a Braille string to English.

    Args:
        braille_str (str): The Braille string to be translated to its corresponding English string.

    Returns:
        str: English translation of braille_str.
    """
    english_str = ''
    is_capitalized = False
    number_follows = False

    # Iterate in increments of six to retrieve all valid Braille characters in the input string
    for i in range(6, len(braille_str) + 1, 6):
        braille_char = braille_str[i - 6: i]

        # Check if Braille substring is a special character
        if braille_char in BRAILLE_TO_ENGLISH_SPECIAL:
            if BRAILLE_TO_ENGLISH_SPECIAL[braille_char] == "Number Follows":
                number_follows = True
            elif BRAILLE_TO_ENGLISH_SPECIAL[braille_char] == "Capital Follows":
                is_capitalized = True
            else:
                english_str += " "
                number_follows = False
            
        # Check if Braille substring is a number
        elif number_follows:
            english_str += BRAILLE_TO_ENGLISH_NUMBER[braille_char]
        
        # Translate Braille substring as an English alphabet character (uppercase and lowercase)
        else:
            if is_capitalized:
                english_str += BRAILLE_TO_ENGLISH_ALPHABET[braille_char].upper()
                is_capitalized = False
            else:
                english_str += BRAILLE_TO_ENGLISH_ALPHABET[braille_char]

    return english_str

def translate_to_braille(english_str: str) -> str:
    """
    Translates an English string to Braille.

    Args: 
        english_str (str): The English string to be translated to its corresponding Braille string.

    Returns:
        str: Braille translation of english_str.
    """
    braille_str = ''
    is_num = False

    for char in english_str:

        # Check if English character is a number
        if char.isnumeric():
            if not is_num:
                is_num = True
                braille_str += ENGLISH_SPECIAL_TO_BRAILLE["Number Follows"]
            braille_str += ENGLISH_NUMBER_TO_BRAILLE[char]
        
        # Check if English character is a space
        elif char == " ":
            braille_str += ENGLISH_SPECIAL_TO_BRAILLE["Space"]
            is_num = False
        
        # Translate English letter (uppercase or lowercase) to Braille
        else:
            if char.isupper():
                braille_str += ENGLISH_SPECIAL_TO_BRAILLE["Capital Follows"]
                char = char.lower()
            
            braille_str += ENGLISH_ALPHABET_TO_BRAILLE[char]

    return braille_str
    

def braille_translator(input_str: str) -> str:
    """
    Translates input text between English and Braille.

    Args:
        input_str (str): The input string to be translated.

    Returns:
        str: The translated string, converting English to Braille or Braille to English.
    """
    if is_braille(input_str):
        return translate_to_english(input_str)
    else:
        return translate_to_braille(input_str)
        
if __name__ == "__main__":
    inputs = ' '.join(sys.argv[1:])
    result = braille_translator(inputs)
    print(result)