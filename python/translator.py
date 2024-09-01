import itertools
import string
from abc import ABC, abstractmethod
import sys

import sys
from strategies.english_to_braille_strategy import EnglishToBrailleStrategy
from strategies.braille_to_english_strategy import BrailleToEnglishStrategy
from strategies.abstract_strategy import TranslationStrategy
from utils.generate_dictionary import generate_dictionary

"""
Assumptions: 
- more than one space is treated as a single space
- decimals do not exist before the digits (such as .5), they are treated as periods
- if decimal, it is followed by a "." character in the braille
- if any character not in dictionary, it gives an error message and exits
- if braille text cannot be split into 6 character chunks, it gives an error message and exits
"""

class Translator:
    """
    A class that represents a Translator.
    Attributes:
        _strategy (TranslationStrategy): The translation strategy used by the translator.
    Methods:
        __init__(self, strategy: TranslationStrategy): Initializes a Translator object with a given strategy.
        set_strategy(self, strategy: TranslationStrategy): Sets the translation strategy for the translator.
        translate(self, text, dictionary): Translates the given text using the current strategy and dictionary.
    """
    
    def __init__(self, strategy: TranslationStrategy): 
        self._strategy = strategy
    def set_strategy(self, strategy: TranslationStrategy): 
        self._strategy = strategy
    def translate(self, text): 
        return self._strategy.translate(text)



def main():
    # Get input text
    if len(sys.argv) < 2:
        print("Please provide the input text.")
        sys.exit(1)
    input_text = ' '.join(sys.argv[1:]).strip()
    
    # Instantiate dictionary and strategies
    translate_dict = generate_dictionary()
    english_to_braille_strategy = EnglishToBrailleStrategy(translate_dict)
    braille_to_english_strategy = BrailleToEnglishStrategy(translate_dict)
    
    # Determine whether the input text is English or Braille
    states = ['O', '.']
    if any(char not in states for char in input_text):
        translator = Translator(english_to_braille_strategy)
    else:
        translator = Translator(braille_to_english_strategy) 
    
    # Translate the input text
    output_text = translator.translate(input_text)
    print(output_text)


if __name__ == "__main__":
    main()
