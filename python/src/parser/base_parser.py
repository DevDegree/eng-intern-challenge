from abc import ABC, abstractmethod
from typing import List

class BaseParser(ABC):
    """An abstract base class to represent a parser object that converts from English/Braille to Braille/English
    
    Methods:
        parse(self, text: str) -> List[List[str]]
        translate_line(self, characters: List[str]) -> str
        translate_all(self, text: str) -> str
    """

    @abstractmethod
    def parse(self, text: str) -> List[List[str]]:
        """Converts the text into grouping of characters by seperating on space

        Parameters:
            text (str): The input text that needs to be parsed into individual parts

        Returns:
            List[List[str]]: The characters of the string text that are grouped together by each "word"
        """
        pass

    @abstractmethod
    def translate_line(self, characters: List[str]) -> str:
        """Converts an array of of characters from English/Braille to the other version as a string
        Parameters:
            characters (List[str]): The array of characters to be translated
        
        Returns:
            str: The translated string of the array of characters
        """
        pass

    @abstractmethod
    def translate_all(self, text: str) -> str:
        """Translates a text from English/Braille to Braille/English
        Parameters:
            text (str): The input text to be translated
        
        Returns:
            str: The translated string

        """