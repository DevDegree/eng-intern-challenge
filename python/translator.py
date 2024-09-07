import sys
import argparse
import logging
from braille_state import BrailleState
from text_state import TextState
from config import VALID_BRAILLE_CHARS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def braille_to_text(braille: str) -> str:
    """
    Convert Braille to text.

    Args:
        braille (str): A string of Braille characters.

    Returns:
        str: The translated text.

    Raises:
        ValueError: If the input contains invalid Braille characters.
    """
    if not set(braille).issubset(VALID_BRAILLE_CHARS):
        raise ValueError("Invalid Braille characters detected.")

    state = BrailleState()
    for i in range(0, len(braille), 6):
        state.process_char(braille[i:i+6])
    return state.get_result()


def text_to_braille(text: str) -> str:
    """
    Convert text to Braille.

    Args:
        text (str): A string of text to be converted.

    Returns:
        str: The Braille representation of the input text.

    Raises:
        ValueError: If the input contains characters that can't be translated to Braille.
    """
    state = TextState()
    for char in text:
        state.process_char(char)
    return state.get_result()


def is_braille(input_string: str) -> bool:
    """
    Determine if the input string is Braille.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the input is Braille, False otherwise.
    """
    return set(input_string).issubset(VALID_BRAILLE_CHARS)


def translate(input_string: str) -> str:
    """
    Translate between Braille and text based on input.

    Args:
        input_string (str): The string to translate.

    Returns:
        str: The translated string.

    Raises:
        ValueError: If the input is invalid.
    """
    if is_braille(input_string):
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)


def main():
    parser = argparse.ArgumentParser(
        description="Translate between Braille and text."
    )
    parser.add_argument(
        "input",
        nargs="+",
        help="The string to translate."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Increase output verbosity"
    )
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    input_string = ' '.join(args.input)
    logger.debug(f"Input string: {input_string}")

    try:
        result = translate(input_string)
        print(result)
    except ValueError as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
