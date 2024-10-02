from strategy import Strategy

# Concrete strategy for Braille to English translation
class BrailleToEnglishStrategy(Strategy):
    def __init__(self, input=None, dictionary=None):
        self.input = input
        self.dictionary = dictionary  # Directly assign the Braille dictionary
    
    def translate(self):
        # Initialize an empty list to store the English representation
        english_output = []
        is_number_mode = False  # Flag to indicate number mode
        capitalize_next = False  # Flag to capitalize the next character

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
                # If the chunk is not valid, append a placeholder (e.g., "?")
                english_output.append("?")  # Indicate an invalid Braille chunk
        
        # Join all English representations into a single string
        return ''.join(english_output)