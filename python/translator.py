# Name : Monisha Ranjan
# Email : ranjan.monisha233@gmail.com

class BrailleMappings:
    def __init__(self):
        # Alphabet Braille to English
        self.braille_to_eng_alphabets = {
            "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
            "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
            ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
            "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
            "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
            "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
            "OO.OOO": "y", "O..OOO": "z"
        }

        # Numbers Braille to English
        self.braille_to_eng_number = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4",
            "O..O..": "5", "OOO...": "6", "OOOO..": "7", "O.OO..": "8",
            ".OO...": "9", ".OOO..": "0", ".O...O": "."
        }

        # Special symbols
        self.num = ".O.OOO"
        self.cap = ".....O"
        self.space = "......"

         # Invert dictionaries for English to Braille mappings
        self.eng_to_braille_alphabets = {v: k for k, v in self.braille_to_eng_alphabets.items()}
        self.eng_to_braille_numbers = {v: k for k, v in self.braille_to_eng_number.items()}

    def get_alphabet_mapping(self, char):
        # Retrieve the Braille pattern corresponding to an English alphabet character
        return self.eng_to_braille_alphabets.get(char)

    def get_number_mapping(self, char):
        # Retrieve the Braille pattern corresponding to an English numeric character
        return self.eng_to_braille_numbers.get(char)

    def get_braille_alphabet(self, symbol):
        # Retrieve the English alphabet character corresponding to a Braille pattern
        return self.braille_to_eng_alphabets.get(symbol)

    def get_braille_number(self, symbol):
        # Retrieve the English numeric character corresponding to a Braille pattern
        return self.braille_to_eng_number.get(symbol)

class BrailleTranslator:
    def __init__(self):
        self.mappings = BrailleMappings()

    def translate_to_braille(self, text):
        # Initialize an empty list to store the Braille translation result
        result = []
        
        # Flag to track if the previous character was a number, to handle numeric sequences
        number_flag = False

        # Iterate through each character in the input text
        for char in text:
            # Check if the character is uppercase
            if char.isupper():
                # Append the Braille capitalization indicator before the lowercase character
                result.append(self.mappings.cap)
                # Convert the character to lowercase for mapping purposes
                char = char.lower()

            # Check if the character is a digit
            if char.isdigit():
                # If this is the start of a number sequence, append the Braille number indicator
                if not number_flag:
                    result.append(self.mappings.num)
                    number_flag = True
                # Append the corresponding Braille pattern for the digit
                result.append(self.mappings.get_number_mapping(char))
            elif char == " ":
                # Handle spaces by appending the Braille space pattern
                result.append(self.mappings.space)
                # Reset the number flag since a space breaks the numeric sequence
                number_flag = False
            else:
                # Map the character to its corresponding Braille pattern for alphabets
                braille_char = self.mappings.get_alphabet_mapping(char)
                if braille_char:
                    # Append the Braille pattern if found
                    result.append(braille_char)
                else:
                    # Print a warning if the character is not found in the mapping
                    print(f"Warning: Character '{char}' not found in Braille mapping.")
                # Reset the number flag since the character is not a digit
                number_flag = False

        # Join all the Braille patterns into a single string and return the result
        return "".join(result)

    def translate_to_english(self, braille):
        # Initialize an empty list to store the translated English characters
        result = []
        
        # Initialize a counter for iterating through the Braille string
        i = 0
        
        # Flags to track if the next character should be capitalized or if it's part of a number sequence
        capital_flag = False
        number_flag = False

        # Loop through the Braille string, processing each 6-dot symbol
        while i < len(braille):
            # Extract the next 6-dot Braille symbol
            symbol = braille[i:i+6]

            # Check if the symbol is the Braille number indicator
            if symbol == self.mappings.num:
                number_flag = True
            # Check if the symbol is the Braille capitalization indicator
            elif symbol == self.mappings.cap:
                capital_flag = True
            # Check if the symbol represents a space
            elif symbol == self.mappings.space:
                result.append(" ")
                # Reset the number flag since a space breaks the numeric sequence
                number_flag = False
            else:
                # If we're in a number sequence, translate the symbol as a number
                if number_flag:
                    char = self.mappings.get_braille_number(symbol)
                    result.append(char)
                else:
                    # Otherwise, translate the symbol as an alphabet character
                    char = self.mappings.get_braille_alphabet(symbol)
                    # If the capitalization flag is set, capitalize the character
                    if capital_flag:
                        char = char.upper()
                        capital_flag = False
                    result.append(char)

            # Move to the next 6-dot Braille symbol
            i += 6

        # Join all the translated characters into a single string and return the result
        return "".join(result)




def main():
    # Import the sys module to access command-line arguments
    import sys
    
    # Create an instance of the BrailleTranslator class
    translator = BrailleTranslator()
    
    # Combine all command-line arguments into a single string, separated by spaces
    input_text = " ".join(sys.argv[1:])

    # Determine if the input text is in Braille (composed of 'O', '.', and ' ')
    if all(c in ['O', '.', ' '] for c in input_text):
        # If the input is Braille, translate it to English and print the result
        print(translator.translate_to_english(input_text))
    else:
        # If the input is English text, translate it to Braille and print the result
        print(translator.translate_to_braille(input_text))

# The following block ensures that the main() function is called when the script is executed directly
if __name__ == "__main__":
    main()

