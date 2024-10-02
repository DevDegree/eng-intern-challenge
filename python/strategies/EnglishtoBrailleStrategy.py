from strategy import Strategy

# Concrete strategy for English to Braille translation
class EnglishtoBrailleStrategy(Strategy):
    def __init__(self, input=None, dictionary=None):
        """
        Initialize the EnglishtoBrailleStrategy with input and dictionary.

        Args:
            input (str): The English input string to be translated.
            dictionary (dict): A mapping of English characters to their Braille representations.
        """
        self.input = input
        self.dictionary = self.reverse_dictionary(dictionary)  # Reverse dict on initialization

    def reverse_dictionary(self, braille_to_english_dict):
        """
        Create a mapping from English characters to Braille representations.

        Args:
            braille_to_english_dict (dict): A mapping of Braille chunks to their English representations.

        Returns:
            dict: A mapping of English characters to their corresponding Braille representations.
        """
        english_to_braille_dict = {}

        for braille, english_list in braille_to_english_dict.items():
            for english in english_list:
                if english is not None:  # Skip None values
                    if english not in english_to_braille_dict:
                        english_to_braille_dict[english] = []
                    english_to_braille_dict[english].append(braille)
        
        return english_to_braille_dict
    
    def translate(self):
        """
        Translate the English input string into Braille.

        The method processes the input string, converting characters into
        their Braille equivalents while handling special cases such as
        uppercase letters, digits, and decimal points. It also ensures
        that multiple spaces are treated as a single space and exits 
        gracefully if any invalid characters are found.

        Raises:
            SystemExit: If an invalid character is encountered or if 
            Braille output cannot be generated.

        Returns:
            str: The translated Braille representation of the English input.
        """
        braille_output = []  # List to store Braille output
        number_mode = False  # To keep track of number mode

        # Handle multiple spaces
        input_chars = self.input.split()
        cleaned_input = ' '.join(input_chars)  # Treat multiple spaces as single space

        for char in cleaned_input:
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
                else:
                    braille_output.append(self.dictionary['.'][0])  # Just add the Braille for the period
            
            elif char == ' ':  # Check for space
                if braille_output and braille_output[-1] != self.dictionary[' '][0]:  # Avoid multiple spaces
                    braille_output.append(self.dictionary[' '][0])  # Add Braille for space
                number_mode = False  # Reset number mode on space
            
            else:  # For all other characters
                if char in self.dictionary:
                    braille_output.append(self.dictionary[char][0])  # Add corresponding Braille
                else:
                    print(f"Error: Character '{char}' not found in dictionary.")
                    exit(1)  # Exit on invalid character
            
            if char != ' ' and not char.isdigit():  # Reset number mode for non-digit characters
                number_mode = False
            
        # Check for empty braille output (error handling)
        if not braille_output:
            print("Error: Unable to generate Braille output.")
            exit(1)
        
        return ''.join(braille_output)
