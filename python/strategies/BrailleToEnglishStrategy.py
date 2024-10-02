from strategy import Strategy

# Concrete strategy for Braille to English translation
class BrailleToEnglishStrategy(Strategy):
    def __init__(self, input=None, dictionary=None):
        """
        Initialize the BrailleToEnglishStrategy with input and dictionary.

        Args:
            input (str): The Braille input string to be translated.
            dictionary (dict): A mapping of Braille chunks to their English representations.
        """
        self.input = input
        self.dictionary = dictionary  # Directly assign the Braille dictionary
    
    def translate(self):
        """
        Translate the Braille input string into English.

        The method processes the Braille input in chunks of six characters.
        It checks each chunk against the provided Braille dictionary and 
        translates it to the corresponding English character(s). It handles 
        special cases for numbers, decimal points, and capitalization.

        Raises:
            SystemExit: If the input length is not a multiple of 6 or if any 
            Braille chunk is not found in the dictionary.

        Returns:
            str: The translated English representation of the Braille input.
        """
        # Initialize an empty list to store the English representation
        english_output = []
        is_number_mode = False  # Flag to indicate number mode
        capitalize_next = False  # Flag to capitalize the next character

        # Validate length of input
        if len(self.input) % 6 != 0:
            print("Error: Braille text cannot be split into 6 character chunks.")
            exit(1)

        # Iterate over the Braille input string in chunks of 6 characters
        for i in range(0, len(self.input), 6):
            braille_chunk = self.input[i:i+6]  # Get the current chunk of 6 characters

            # Check if the chunk is in the Braille dictionary
            if braille_chunk in self.dictionary:
                translated_values = self.dictionary[braille_chunk]
                # Determine which value to take based on the rules
                if is_number_mode:
                    # If in number mode, take the second element (if it exists)
                    translated = translated_values[1] if len(translated_values) > 1 else translated_values[0]
                else:
                    # Otherwise, take the first element
                    translated = translated_values[0]
                
                # Process special cases
                if translated == 'N':
                    is_number_mode = True  # Switch to number mode
                elif translated == 'D':
                    # Treat it as decimal point
                    english_output.append('.')  # Add a period directly
                    continue  # Skip adding 'D'
                elif translated == 'C':
                    capitalize_next = True  # Capitalize the next character
                    continue  # Skip adding 'C'
                else:
                    # Normal translation
                    if capitalize_next:
                        english_output.append(translated.upper())  # Capitalize the character
                        capitalize_next = False  # Reset flag after using it
                    else:
                        english_output.append(translated)

            else:
                # If the chunk is not valid, print an error message and exit
                print(f"Error: Braille chunk '{braille_chunk}' not found in dictionary.")
                exit(1)
        
        # Join all English representations into a single string
        return ''.join(english_output)