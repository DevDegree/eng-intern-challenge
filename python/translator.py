# Submission by Patrick Huang (patrick.huang@uwaterloo.ca)

import sys

class BrailleTranslator:
    def __init__(self):
        """
        Initialize the BrailleTranslator with an English to Braille map, Braille to English map, letter to number map, and number to letter map.
        """
        
        # A map for converting English to Braille
        self.english_to_braille = {
            'a': 'O.....',
            'b': 'O.O...',
            'c': 'OO....',
            'd': 'OO.O..',
            'e': 'O..O..',
            'f': 'OOO...',
            'g': 'OOOO..',
            'h': 'O.OO..',
            'i': '.OO...',
            'j': '.OOO..',
            'k': 'O...O.',
            'l': 'O.O.O.',
            'm': 'OO..O.',
            'n': 'OO.OO.',
            'o': 'O..OO.',
            'p': 'OOO.O.',
            'q': 'OOOOO.',
            'r': 'O.OOO.',
            's': '.OO.O.',
            't': '.OOOO.',
            'u': 'O...OO',
            'v': 'O.O.OO',
            'w': '.OOO.O',
            'x': 'OO..OO',
            'y': 'OO.OOO',
            'z': 'O..OOO',
            'capital_follows': '.....O',
            'number_follows': '.O.OOO',
            ' ': '......'
        }
        
        # Reverse the mapping for a Braille to English converter
        self.braille_to_english = {value: key for key, value in self.english_to_braille.items()}
        
        # A map for converting letters to equivalent numbers
        self.letter_to_number = {
            'j': '0',
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8',
            'i': '9',
        }
        
        # Reverse the mapping for a number to letter converter
        self.number_to_letter = {value: key for key, value in self.letter_to_number.items()}


    def is_braille(self, input_string):
        """
        Function that checks if input_string is in English or Braille.
        """
        
        # Valid Braille characters
        braille_characters = {'O', '.'}
        
        # Determine if input_string is Braille or not, depending on if all its characters are valid Braille characters
        for char in input_string:
            if char not in braille_characters:
                return False
        
        return True
        
    def translate(self, input_string):
        """
        Wrapper function to determine whether input_string should be translated to English or Braille.
        """
    
        if self.is_braille(input_string):
            return self.translate_to_english(input_string)
        else:
            return self.translate_to_braille(input_string)
            
    def translate_to_english(self, input_string):
        """
        Function that translates Braille to English.
        """
        
        english_output = ""
        is_capital = False
        is_number = False
        
        # Each Braille character is six characters, so we process and iterate in 6 six character chunks
        for i in range(0, len(input_string), 6):
            braille_char = input_string[i:i+6]
            
            # Use the mapping to convert the character
            english_char = self.braille_to_english[braille_char]
            
            # Check if next character is a capital
            if english_char == "capital_follows":
                is_capital = True
                continue
            
            # Check if next characters are numbers
            elif english_char == "number_follows":
                is_number = True
                continue
            
            # Check if current character is a capital
            elif is_capital:
                english_char = english_char.upper()
                is_capital = False
        
            # Reset the number activation if the current character is a space
            elif english_char == " ":
                if is_number:
                    is_number = False
            
            # Otherwise, add the appropriate character
            if is_number:
                english_output += self.letter_to_number[english_char]
            else:
                english_output += english_char
            
        return english_output
            
    def translate_to_braille(self, input_string):
        """
        Function that translates English to Braille.
        """
    
        braille_output = ""
        is_number = False
        
        for char in input_string:
            
            # Check if current character is a capital
            if char.isupper():
                braille_output += self.english_to_braille["capital_follows"]
                
                # Lower character if it is, so that character can be matched in the map
                char = char.lower() 
            
            # Check if current character is a digit
            if char.isdigit():
                
                # If it is, then is_number must be activated
                if not is_number:
                    is_number = True
                    braille_output += self.english_to_braille["number_follows"]
                
                # Once is_number is activated, the character can be added as usual
                braille_output += self.english_to_braille[self.number_to_letter[char]]
            
            # If it is not a digit, then is_number should be deactivated
            else:
                is_number = False
                braille_output += self.english_to_braille[char]
                
        return braille_output
    
def main():
    """
    Main function: takes in input, creates an instance of BrailleTranslator, and outputs its translated result.
    """

    input_string = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()
    print(translator.translate(input_string))
    
if __name__ == "__main__":
    main()