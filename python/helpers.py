
from typing import Literal

def detect_language(input_text: str) -> Literal["Braille", "English"]:
    """
    Detects whether the input string is in English or Braille using character set analysis.
    """
    if not input_text.strip():
        raise ValueError("Input string is empty.")

    cleaned_input = input_text.replace(' ', '').upper()
    characters = set(cleaned_input)
    braille_chars = {'O', '.'}
    if characters.issubset(braille_chars):
        return 'Braille'
    else:
        return 'English'