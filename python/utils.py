def is_braille(input_text: str) -> bool:
    # Define valid characters for Braille (O for raised dots, . for unraised dots)
    braille_chars = {'O', '.'}

    # Return False if any character is not a valid Braille character
    return not any(char not in braille_chars for char in input_text)
