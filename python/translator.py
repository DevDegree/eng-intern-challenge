import itertools
import string
from abc import ABC, abstractmethod
import sys

"""
Assumptions: 
- more than one space is treated as a single space
- decimals do not exist before the digits (such as .5), they are treated as periods
- if decimal, it is followed by a "." character in the braille
- if any character not in dictionary, it gives an error message and exits
- if braille text cannot be split into 6 character chunks, it gives an error message and exits
"""

class TranslationStrategy(ABC):
    """
    Abstract base class for translation strategies. Using strategy pattern to allow for easy swapping if more languages are added in the future.
    Attributes:
        None
    Methods:
        translate(text, dictionary): Abstract method to translate text using a dictionary.
    """
    @abstractmethod
    def translate(self, text, dictionary):
        pass

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
    def translate(self, text, dictionary): 
        return self._strategy.translate(text, dictionary)

class EnglishToBrailleStrategy(TranslationStrategy):
    def __init__(self, translate_dict):
        self.translate_dict = translate_dict

    def translate(self, english_text, dictionary):
        braille_text = ''
        number_flag = False
        for char in english_text:
            if char.lower() in dictionary: # ignores all characters not in dictionary
                if char.isupper(): # if capital, add "C" before braille and lowercase the letter
                    braille_text += dictionary['C']
                    char = char.lower()
                if char.isdigit() and not number_flag: # if number, add "N" before and assume numbers until space symbol is encountered
                    number_flag = True
                    braille_text += dictionary['N']
                if char == '.' and number_flag: # if dot, assume decimal if we're assuming numbers
                    braille_text += dictionary['D']
                if char == ' ': # if space, reset number flag
                    number_flag = False
                braille_text += dictionary[char]
            else:
                print("Please ensure the input text is limited to letters, digits, and punctuation.")
                sys.exit(1)
                
        return braille_text

class BrailleToEnglishStrategy(TranslationStrategy):
    def __init__(self, translate_dict):
        self.translate_dict = translate_dict
        
    def get_key_by_value(self, dictionary, target_value):
        return [key for key, value in dictionary.items() if value == target_value]

    def translate(self, braille_text, dictionary):
        english_text = ''
        number_flag = False
        capital_flag = False
        
        # Process the Braille text in chunks of 6 characters
        for i in range(0, len(braille_text), 6):
            braille_char = braille_text[i:i+6]
            
            if len(braille_char) < 6:
                print("Please ensure the braille text is complete with 6 digits for each character.")
                sys.exit(1)
            
            keys = self.get_key_by_value(dictionary, braille_char)
            
            if not keys: # Empty list means the braille character is not in the dictionary
                print("Please ensure the braille text translates correctly to an English character.")
                sys.exit(1)
            
            if keys[0] == 'D': continue # if decimal, it wouldn't affect the output so skip to next iteration
            if keys[0] == 'C': 
                capital_flag = True
                continue # skip to next iteration
            if keys[0] == 'N':
                number_flag = True
                continue # skip to next iteration
            if keys[0] == ' ' and number_flag:
                number_flag = False
                
            char = keys[0] if (not number_flag) else keys[1] if (len(keys) > 1) else keys[0]
            
            if capital_flag:
                char = char.upper()
                capital_flag = False
            
            english_text += char
            
        return english_text


def generate_dictionary():
    """
    The dictionary is generated dynamically due to the following reasons:
    - Maintainability: Easier to maintain if the Braille representations or English characters change.
    - Efficiency: Generally efficient because it uses pre-computed indices and is based on a structured approach to generate the dictionary.
    - Readability: The code might be more complex but provides a clear, systematic way to generate the dictionary.
    """
    
    states = ['O', '.'] # Possible states for each dot: colored (O) or not colored (.)
    combinations = list(itertools.product(states, repeat=6)) # Because its 2 possibilities for each dot and 6 dots in total = 2 ^ 6 = 64 combinations
    braille = list(''.join(combo) for combo in combinations) # Convert the tuples to strings
    english = list(string.ascii_lowercase + string.digits + '.'+ ','+'?'+'!'+':'+';'+'-'+'/'+'<'+'('+')'+' '+'C'+'D'+'N') # Create a list of all lowercase letters, digits, and punctuation

    # Braille indices for each English character in the order of the English list
    braille_indices=[31,23,15,11,27,7,3,19,39,35,29,21,13,0,25,5,1,17,37,33,28,20,34,12,8,24,35,31,23,15,11,27,7,3,19,39,50,55,52,49,51,53,60,45,38,22,41,63,62,46,40]
    if len(english) != len(braille_indices):
        raise ValueError("Mismatch between English characters and Braille indices length.")

    translate_dict = {}
    for index, character in enumerate(english):
        translate_dict[character] = braille[braille_indices[index]]
        
    return translate_dict


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
    output_text = translator.translate(input_text, translate_dict)
    print(output_text)


if __name__ == "__main__":
    main()
