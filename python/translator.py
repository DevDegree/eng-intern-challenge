import sys
from typing import Dict, List

# Constants
CHUNK_SIZE: int = 6

# Braille mappings
BRAILLE_TO_ENGLISH_MAPPING: Dict[str, str] = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}
ENGLISH_TO_BRAILLE_MAPPING: Dict[str, str] = {
    v: k for k, v in BRAILLE_TO_ENGLISH_MAPPING.items()}

# Special Braille signs
CAPITAL_SIGN: str = '.....O'
NUMBER_SIGN: str = '.O.OOO'


def chunk_string(string: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    """
    Split a string into chunks of a given size.

    Args:
    string (str): The string to be chunked.
    chunk_size (int): The size of each chunk.

    Returns:
    List[str]: A list of string chunks.
    """

    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]


def validate_braille(string: str) -> None:
    """
    Validate the Braille input.

    Args:
    string (str): The braille string to validate.

    Returns:
    None, raises exception.
    """

    if not set(string).issubset('O.'):
        raise ValueError(
            "Invalid characters in Braille input. Only 'O' and '.' are allowed.")
    if len(string) % CHUNK_SIZE != 0:
        raise ValueError(
            f"Braille input length must be a multiple of {CHUNK_SIZE}.")


def braille_to_english(braille: str) -> str:
    """
    Convert Braille to English.

    Args:
    braille (str): The Braille string to be converted.

    Returns:
    str: The converted English string.
    """

    validate_braille(braille)
    result: List[str] = []
    capitalize_next: bool = False
    number_mode: bool = False

    # Process each Braille character (chunk of 6 dots)
    for char in chunk_string(braille):

        # Next character is a capital
        if char == CAPITAL_SIGN:
            capitalize_next = True

        # Next character is a number
        elif char == NUMBER_SIGN:
            number_mode = True

        elif char in BRAILLE_TO_ENGLISH_MAPPING:
            # Use the mapping to retrieve the english letter
            letter: str = BRAILLE_TO_ENGLISH_MAPPING[char]

            # Convert letters a-j to numbers 0-9
            if number_mode and letter in 'abcdefghij':
                result.append(str('abcdefghij'.index(letter) + 1))
            else:
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
                number_mode = False
        else:
            result.append('')

    return ''.join(result)


def english_to_braille(english: str) -> str:
    """
    Convert English to Braille.

    Args:
    english (str): The English string to be converted.

    Returns:
    str: The converted Braille string.
    """

    result: List[str] = []
    number_mode: bool = False

    for char in english:
        # Handle capital letter
        if char.isupper():
            result.append(CAPITAL_SIGN)
            char = char.lower()

        # Handle number
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_SIGN)
                number_mode = True
            # Use numbers 0-9 to get letters a-j and then use the mapping to retrieve the braille chunk
            result.append(
                ENGLISH_TO_BRAILLE_MAPPING['abcdefghij'[int(char) - 1]])
        else:
            if number_mode:
                number_mode = False

            result.append(ENGLISH_TO_BRAILLE_MAPPING.get(char, ''))

    return ''.join(result)


def is_braille(text: str) -> bool:
    """
    Check if the given text is in Braille format.

    Args:
    text (str): The text to check.

    Returns:
    bool: True if text is in Braille format, False otherwise.
    """

    # Check that the input only contains valid Braille characters ('O' and '.') and that the input length
    # is a multiple of 6 (as Braille is in chunks of 6)
    return set(text).issubset('O.') and len(text) % CHUNK_SIZE == 0


def translate(text: str) -> str:
    """
    Main function that translates between Braille and English.

    Args:
    text (str): The text to translate.

    Returns:
    str: The translated text.
    """

    return braille_to_english(text) if is_braille(text) else english_to_braille(text)


def main() -> None:
    """
    Main function to handle command-line input and execute the translation.
    """

    try:
        if len(sys.argv) < 2:
            raise ValueError("No input provided")

        input_text: str = " ".join(sys.argv[1:])

        if not input_text.strip():
            raise ValueError("Empty input provided")

        result: str = translate(input_text)
        print(result)

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        print("Usage: python translator.py <text_to_translate>", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
