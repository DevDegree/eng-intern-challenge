class BrailleTranslationError(Exception):
    """
    Base class for Braille Translation errors.

    Attributes:
        message (str): The error message.
    """
    def __init__(self, message: str):
        """
        Initializes the BrailleTranslationError with a message.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)

class InvalidBrailleCharacterError(BrailleTranslationError):
    """
    Raised when an invalid Braille character is encountered.

    Attributes:
        invalid_char_set (set): The set of invalid Braille characters.
    """
    def __init__(self, invalid_char_set: set):
        """
        Initializes the InvalidBrailleCharacterError with the invalid characters.

        Args:
            invalid_char_set (set): The set of invalid Braille characters.
        """
        self.invalid_char_set = invalid_char_set
        message = f"Invalid Braille characters encountered: {invalid_char_set}"
        super().__init__(message)

class IncompleteBrailleSequenceError(BrailleTranslationError):
    """
    Raised when the input Braille sequence is incomplete (not a multiple of cell_size).

    Attributes:
        length (int): The length of the input Braille sequence.
        cell_size (int): The size of a Braille cell (default is 6).
    """
    def __init__(self, length: int, cell_size: int = 6):
        """
        Initializes the IncompleteBrailleSequenceError with the length of the sequence.

        Args:
            length (int): The length of the input Braille sequence.
            cell_size (int): The size of a Braille cell (default is 6).
        """
        message = f"Incomplete Braille sequence detected. Input length: {length} (must be a multiple of {cell_size})."
        super().__init__(message)

class UnsupportedBrailleCharacterError(BrailleTranslationError):
    """
    Raised when a Braille character is not mapped to an English letter.

    Attributes:
        braille_char (str): The unsupported Braille character.
    """
    def __init__(self, braille_char: str):
        """
        Initializes the UnsupportedBrailleCharacterError with the unsupported character.

        Args:
            braille_char (str): The unsupported Braille character.
        """
        self.braille_char = braille_char
        message = f"Braille character '{braille_char}' is not supported in the current mapping."
        super().__init__(message)

class UnsupportedEnglishCharacterError(BrailleTranslationError):
    """
    Raised when an English character is not mapped to a Braille cell.

    Attributes:
        english_char (str): The unsupported English character.
    """
    def __init__(self, english_char: str):
        """
        Initializes the UnsupportedEnglishCharacterError with the unsupported character.

        Args:
            english_char (str): The unsupported English character.
        """
        self.english_char = english_char
        message = f"English character '{english_char}' is not supported in the current mapping."
        super().__init__(message)

class EmptyInputError(BrailleTranslationError):
    """
    Raised when the input text is empty.
    """
    def __init__(self):
        """
        Initializes the EmptyInputError with a default message.
        """
        message = "No input provided for translation."
        super().__init__(message)