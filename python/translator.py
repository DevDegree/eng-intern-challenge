
import sys, re


# Mapping dictionaries from Braille to English
BRAILLE_TO_ENGLISH = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z"
}

SPACE = "......"
CAPITAL_FOLLOWS = ".....O"
NUMBER_FOLLOWS = ".O.OOO"


def num_to_char(num_str):
    """
    Converts a numeric string to its corresponding alphabetic character for Braille encoding.
    
    Args:
        num_str (str): A single character string representing a numeric digit, '0' through '9'.
    
    Returns:
        str: A single character string representing the corresponding alphabetic character in Braille.
             'a' through 'i' are used for '1' to '9', and 'j' is used for '0'.
    """

    if num_str == '0':
        return 'j'
    else:
        return chr(ord('a') + int(num_str) - 1)

def char_to_num(char):
    """
    Converts an alphabetic character to its corresponding number for Braille encoding.
    
    Args:
        char (str): A single lowercase alphabetic character, 'a' through 'j'.
    
    Returns:
        str: A string representing the number that corresponds to the given Braille character.
             '1' through '9' correspond to 'a' through 'i', and '0' corresponds to 'j'.
    """
    return str((ord(char) - ord('a') + 1) % 10)

def is_braille(text) -> bool:
    """
    Checks if a given string contains only valid Braille characters.
    
    Args:
        text (str): The string to check.
    
    Returns:
        bool: True if the string contains only Braille characters ('O', '.', ' '), False otherwise.
    """
    return all(c in "O. " for c in text)

def is_english(text) -> bool:
    """
    Checks if a given string contains only valid English characters as defined in the ENGLISH_TO_BRAILLE mapping.
    
    Args:
        text (str): The string to check.
    
    Returns:
        bool: True if the string contains only valid English characters defined in the ENGLISH_TO_BRAILLE mapping, False otherwise.
    """
    valid_chars = ''.join(ENGLISH_TO_BRAILLE.keys()) + ' '
    escaped_chars = re.escape(valid_chars)
    valid_english_regex = re.compile(f'^[{escaped_chars}]*$', re.IGNORECASE)

    return bool(valid_english_regex.fullmatch(text))

# Mapping dictionaries from English to Braille
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}
for num_str in '1234567890':
    ENGLISH_TO_BRAILLE[num_str] = ENGLISH_TO_BRAILLE[num_to_char(num_str)]


def trans_braille_to_english(text: str) -> str:
    """
    Translates a string of Braille characters to English.

    Args:
        text (str): A string containing Braille characters grouped in 6-character blocks.

    Returns:
        str: The translated English text. Each valid Braille sequence is converted to its corresponding English character.

    Raises:
        ValueError: If the input text is not a multiple of 6 characters or contains invalid Braille sequences, 
                    which is required for Braille translation.
    """
    if len(text) % 6 != 0:
        raise ValueError("Input length must be a multiple of 6.")

    result = []
    capital = False
    number = False
    tokens = [text[i: i + 6] for i in range(0, len(text), 6)]

    for token in tokens:
        if token not in BRAILLE_TO_ENGLISH and token not in (SPACE, NUMBER_FOLLOWS, CAPITAL_FOLLOWS):
            raise ValueError(f"Invalid Braille input: {token}")

        if token == CAPITAL_FOLLOWS:
            capital = True
            continue
        if token == NUMBER_FOLLOWS:
            number = True
            continue
        if token == SPACE:
            number = False
            result.append(" ")
            continue

        char = BRAILLE_TO_ENGLISH[token]
        if number:
            char = char_to_num(char)
        if capital:
            char = char.upper()
            capital = False
        
        result.append(char)

    return "".join(result)

def trans_english_to_braille(text: str) -> str:
    """
    Translates English text to Braille, handling capital letters and numbers specifically.

    Args:
        text (str): The English text to be translated. This string can include
                    alphabetic characters (both upper and lower case) and digits.

    Returns:
        str: A string of Braille characters. Each valid English character or digit is represented
             by a corresponding Braille code.

    Raises:
        ValueError: If any character in the input string cannot be translated to Braille, including characters that
                    are not alphabetic or numeric, an exception is thrown.
    """
    result = []
    number = False
    for char in text:
        if char == " ":
            if number:
                number = False
            result.append(SPACE)
            continue

        if char.isupper():
            result.append(CAPITAL_FOLLOWS)
            char = char.lower()

        if char not in ENGLISH_TO_BRAILLE:
            raise ValueError(f"Invalid English input: {char}")

        if char.isdigit():
            if not number:
                result.append(NUMBER_FOLLOWS)
                number = True
        else:
            if number:
                number = False
                result.append(SPACE)
        
        result.append(ENGLISH_TO_BRAILLE[char])

    return "".join(result)

# Main function to determine translation direction and execute translation
def translate(text: str) -> str:
    """
    Determines the direction of translation based on the input and executes the appropriate translation.
    
    Args:
        texts (list[str]): A list of strings, each string being either entirely in English or entirely in Braille.
    
    Returns:
        str: A single string containing all translated texts. If translating from English to Braille,
             translated segments are separated by "......". If translating from Braille to English,
             they are separated by spaces. If input types are inconsistent, returns an empty string.
    """
    if is_braille(text):
        return trans_braille_to_english(text)
    elif is_english(text):
        return trans_english_to_braille(text)
    else:
        print("Inconsistent input types")
        return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text> [<text2> ...]")
        return

    combined_text = ' '.join(sys.argv[1:])
    translated_text = translate(combined_text)

    print(translated_text)

if __name__ == "__main__":
    main()
