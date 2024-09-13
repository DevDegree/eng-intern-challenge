
from typing import Literal


def detect_language(input_string) -> Literal["Braille", "English"]:
    """
    Detects whether the input string is in English or Braille using character set analysis.
    """
    cleaned_input = input_string.replace(' ', '').upper()
    characters = set(cleaned_input)
    braille_chars = {'O', '.'}
    if characters.issubset(braille_chars):
        return 'Braille'
    else:
        return 'English'

def format_output(translated_text, output_type):
    pass