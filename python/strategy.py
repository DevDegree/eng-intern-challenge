from abc import ABC, abstractmethod

# Base strategy class for translation strategies
class Strategy(ABC):
    """
    Abstract base class for translation strategies.

    Attributes:
        input (str): The input text to be translated.
        dictionary (dict): The dictionary used for translation.
    """

    def __init__(self, input=None, dictionary=None):
        """
        Initializes the Strategy with input text and a translation dictionary.

        Args:
            input (str, optional): The input text to be translated. Defaults to None.
            dictionary (dict, optional): The dictionary used for translation. Defaults to None.
        """
        self.input = input
        self.dictionary = dictionary

    @abstractmethod
    def translate(self):
        """
        Abstract method for translating the input text.

        Must be implemented by subclasses to perform the actual translation.
        
        Returns:
            str: The translated output as a string.
        """
        pass