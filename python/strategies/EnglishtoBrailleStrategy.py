from strategy import Strategy

# Concrete strategy for English to Braille translation
class EnglishtoBrailleStrategy(Strategy):
    def __init__(self, input=None, dictionary=None):
        self.input = input
        self.dictionary = self.reverse_dictionary(dictionary)  # Reverse dict on initialization

    # Function to create the English to Braille dictionary
    def reverse_dictionary(self, braille_to_english_dict):
        english_to_braille_dict = {}

        for braille, english_list in braille_to_english_dict.items():
            for english in english_list:
                if english is not None:  # Skip None values
                    if english not in english_to_braille_dict:
                        english_to_braille_dict[english] = []
                    english_to_braille_dict[english].append(braille)
        
        return english_to_braille_dict
    
    def translate(self):
        braille_output = []
        number_mode = False  # To keep track of number mode
        decimal_mode = False  # To keep track of decimal mode

        for char in self.input:
            if char.isupper():  # Check if character is uppercase
                braille_output.append(self.dictionary['C'][0])  # Add 'C'
                char = char.lower()  # Convert to lowercase
            
            if char.isdigit():  # Check if character is a digit
                if not number_mode:  # If not already in number mode, turn it on
                    braille_output.append(self.dictionary['N'][0])  # Add 'N'
                    number_mode = True
                braille_output.append(self.dictionary[char][0])  # Add the corresponding Braille for the number
            
            elif char == '.':  # Check for decimal
                if number_mode:  # If in number mode
                    braille_output.append(self.dictionary['D'][0])  # Add 'D'
                    braille_output.append(self.dictionary['.'][0])  # Add the Braille for the decimal point
                    decimal_mode = True
                else:
                    braille_output.append(self.dictionary['.'][0])  # Just add the Braille for the period
            
            elif char == ' ':  # Check for space
                braille_output.append(self.dictionary[' '][0])  # Add Braille for space
                number_mode = False  # Reset number mode on space
            
            else:  # For all other characters
                braille_output.append(self.dictionary.get(char, [''])[0])  # Add corresponding Braille, defaulting to empty
            
            if char != ' ' and not char.isdigit():  # Reset number mode for non-digit characters
                number_mode = False
            
        return ''.join(braille_output)