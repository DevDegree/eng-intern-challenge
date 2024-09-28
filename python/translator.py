import json
import os
import sys
 
class BrailleTranslator:
    """
    A class to translate between English text and Braille.
 
    Attributes:
        braille_dict (dict): The Braille dictionary loaded from a JSON file.
        letters_dict (dict): Dictionary mapping letters to Braille patterns.
        numbers_dict (dict): Dictionary mapping numbers to Braille patterns.
        other_dict (dict): Dictionary mapping special characters to Braille patterns.
        inverse_letters_dict (dict): Dictionary mapping Braille patterns to letters.
        inverse_numbers_dict (dict): Dictionary mapping Braille patterns to numbers.
    """
 
    def __init__(self, file_path='braille_mapping.json'):
        """
        Initializes the BrailleTranslator with the given Braille dictionary file.
 
        Args:
            file_path (str): The path to the Braille dictionary JSON file.
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_path)
        self.braille_dict = self.read_braille_dictionary(file_path)
        self.letters_dict = self.braille_dict['alphabets']
        self.numbers_dict = self.braille_dict['numbers']
        self.other_dict = self.braille_dict['other']
        self.inverse_letters_dict = {v: k for k, v in self.letters_dict.items()}
        self.inverse_numbers_dict = {v: k for k, v in self.numbers_dict.items()}

    def detect_text(self, input_text):
        """
        Detects the input type (Braille or English) and translates accordingly.
 
        Args:
            input_text (str): The input string to translate.
 
        Returns:
            str: The translated string.
        """
        if all(c in 'O.' for c in input_text) and len(input_text) % 6 == 0:
            return self.braille_to_english(input_text)
        else:
            return self.english_to_braille(input_text)

    def read_braille_dictionary(self, file_path):
        """
        Loads the Braille dictionary from a JSON file.
 
        Args:
            file_path (str): The path to the Braille dictionary JSON file.
 
        Returns:
            dict: The loaded Braille dictionary.
        """
        with open(file_path, 'r') as file:
            return json.load(file)
        
 
    def english_to_braille(self, input):
        """
        Translates English text to Braille.
 
        Args:
            input (str): The English text to translate.
 
        Returns:
            str: The translated Braille string.
        """
        braille_output = []
        isNumber = False
        for char in input:
 
            if char.isupper():
                braille_output.append(self.other_dict.get('capital', '......'))
                char = char.lower()
                isNumber = False
 
            if char.isdigit():
                if not isNumber:
                    isNumber = True
                    braille_output.append(self.other_dict.get('number', '......'))
                braille_output.append(self.numbers_dict.get(char, '......'))
            elif char == ' ':
                braille_output.append(self.other_dict.get('space', '......'))
                isNumber = False
            elif char in self.other_dict:
                braille_output.append(self.other_dict.get(char, '......'))
                isNumber = False
            else:
                braille_output.append(self.letters_dict.get(char, '......'))
                isNumber = False
 
        return ''.join(braille_output)
 
    def braille_to_english(self, braille_input):
        """
        Translates Braille to English text.
 
        Args:
            braille_input (str): The Braille string to translate.
 
        Returns:
            str: The translated English text.
        """
        english_output = []
        isCapital = False
        isNum = False
        i = 0
        while i < len(braille_input):
            char = braille_input[i:i + 6]
            if char == self.other_dict.get('capital'):
                i += 6
                isCapital = True
                continue
            elif char == self.other_dict.get('number'):
                i += 6
                isNum = True
                continue
            elif char == self.other_dict.get('space'):
                english_output.append(' ')
            elif isNum and char in self.inverse_numbers_dict:
                english_output.append(self.inverse_numbers_dict.get(char))
            elif char in self.inverse_letters_dict:
                letter = self.inverse_letters_dict.get(char)
                if (isCapital):
                    letter = letter.upper()
                    isCapital = False
                english_output.append(letter)
                isNum = False
            i += 6
        return ''.join(english_output)
 
 
def main():
    """
    Main function to handle command-line input and perform translation.
    """
    translator = BrailleTranslator(file_path='braille_mapping.json')
    if len(sys.argv) > 1:
        input = " ".join(sys.argv[1:])
        output = translator.detect_text(input)
        print(output)
    else:
        print("Please provide an input string to translate.")
 
if __name__ == "__main__":
    main()