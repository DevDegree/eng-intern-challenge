from src.constants.constants import BRAILLE_ALPHABET, BRAILLE_CHARACTER_LENGTH


def is_text_braille(text: str) -> bool:
    """Determines if a text is composed of only braille characters (O and .)'s

    Parameters:
        text (str): The text that is either in english or braille

    Returns:
        bool: If the text is in braille or not (its in english)
    """
    return set(text) == BRAILLE_ALPHABET and len(text) % BRAILLE_CHARACTER_LENGTH == 0