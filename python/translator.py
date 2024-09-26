# import library
import re
import sys

# Dictionary mapping of lowercase English letters and spaces to Braille.
ENG_BRAILLE = {
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
    " ": "......"
}

# Dictionary mapping digits (1-9, 0) to Braille.
ENG_BRAILLE_NUMS = {
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

# Braille control symbols
CAPITAL_BRAILLE = ".....0"
NUMBER_BRAILLE = ".0.000"

# Combine valid Braille patterns and characters for validation
VALID_BRAILLE = set(ENG_BRAILLE.values()).union(set(ENG_BRAILLE_NUMS.values()), {CAPITAL_BRAILLE, NUMBER_BRAILLE})
VALID_ENG = set(ENG_BRAILLE.keys()).union(set(ENG_BRAILLE_NUMS.keys()), set(char.upper() for char in ENG_BRAILLE.keys()))

# Reverse mappings for Braille-to-English translation
BRAILLE_ENG = {v: k for k, v in ENG_BRAILLE.items()}
BRAILLE_ENG.update({v: k for k, v in ENG_BRAILLE_NUMS.items()})

# Global mode tracking
mode = "alpha"  # alpha for letters, nums for numbers
result = ""

# Handle unsupported characters in translation
def handle_unsupported_char(char: str, to_braille: bool = True) -> str:
    """
    Handle unsupported characters during translation by returning a placeholder.

    Args:
    - char (str): The unsupported character.
    - to_braille (bool): If True, it's during English-to-Braille translation; if False, it's Braille-to-English.

    Returns:
    - str: Placeholder for unsupported characters.
    """
    if to_braille:
        return "? (" + char + ")"
    return "? (" + ' '.join(chunk_braille(char)[0]) + ")"  # Return braille chunk as unsupported text

# Chunking Braille strings
def chunk_braille(string: str, chunk_size: int = 6) -> list:
    """
    Split the Braille string into chunks of specified length (default is 6 characters for Braille).

    Args:
    - string (str): The Braille string to be chunked.
    - chunk_size (int): The size of each chunk (6 for Braille characters).

    Returns:
    - list: A list of Braille character chunks.
    """
    return [string[i:i + chunk_size] for i in range(0, len(string), chunk_size)]

# Check if input is Braille using regex
def is_braille(string: str) -> bool:
    """
    Determine if the input string is valid Braille.

    Args:
    - string (str): The input string to be checked.

    Returns:
    - bool: True if the string is valid Braille, False otherwise.
    """
    return bool(re.fullmatch(r"([O\.]{6}\s*)+", string))

# Check if input is English
def is_english(string: str) -> bool:
    """
    Determine if the input string is valid English.

    Args:
    - string (str): The input string to be checked.

    Returns:
    - bool: True if the string contains valid English characters, False otherwise.
    """
    return all(char in VALID_ENG or char.isdigit() or char in ".,;?!'\"" for char in string)  # Allow some punctuation marks

# Translate Braille to English
def translate_braille_to_english(braille_text: str) -> str:
    """
    Translate Braille text into English.

    Args:
    - braille_text (str): The Braille text to translate.

    Returns:
    - str: The translated English text.
    """
    global result, mode
    result = ""
    mode = "alpha"  # Reset mode to alpha at the beginning
    braille_chars = chunk_braille(braille_text.replace(' ', ''))

    for braille_char in braille_chars:
        if braille_char == CAPITAL_BRAILLE:
            result += BRAILLE_ENG.get(braille_chars.pop(0), '?').upper()
        elif braille_char == NUMBER_BRAILLE:
            mode = "nums"
        else:
            if mode == "nums":
                result += BRAILLE_ENG.get(braille_char, '?')
                mode = "alpha"  # Switch back after number
            else:
                result += BRAILLE_ENG.get(braille_char, '?')

    return result

# Translate English to Braille
def translate_english_to_braille(english_text: str) -> str:
    """
    Translate English text into Braille.

    Args:
    - english_text (str): The English text to translate.

    Returns:
    - str: The translated Braille text.
    """
    global result, mode
    result = ""
    mode = "alpha"  # Start in letter mode

    for char in english_text:
        if char.isupper():
            result += CAPITAL_BRAILLE + ENG_BRAILLE.get(char.lower(), handle_unsupported_char(char))
        elif char.isdigit():
            if mode != "nums":
                result += NUMBER_BRAILLE
                mode = "nums"
            result += ENG_BRAILLE_NUMS.get(char, handle_unsupported_char(char))
        else:
            result += ENG_BRAILLE.get(char, handle_unsupported_char(char))
            mode = "alpha"  # Switch back to alpha mode after handling letters

    return result

# Main function to process input
def main():
    """
    Main function that processes command-line input, determines the input type (Braille or English),
    and translates accordingly.
    """
    if len(sys.argv) < 2:
        print("No input received!")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    
    if is_braille(user_input):
        print(translate_braille_to_english(user_input))
    elif is_english(user_input):
        print(translate_english_to_braille(user_input))
    else:
        print("Input is not supported!")
        sys.exit(1)

if __name__ == "__main__":
    main()
