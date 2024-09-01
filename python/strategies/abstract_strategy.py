from abc import ABC, abstractmethod

class TranslationStrategy(ABC):
    """
    Abstract base class for translation strategies. Using strategy pattern to allow for easy swapping if more languages are added in the future.
    Attributes:
        None
    Methods:
        translate(text, dictionary): Abstract method to translate text using a dictionary.
    """
    @abstractmethod
    def translate(self, text):
        pass