import sys

class BrailleTranslator:
    def __init__(self):
        """
        Initializes the BrailleTranslator with mappings for English letters,
        numbers, symbols, and indicators to their corresponding Braille representations.
        Also initializes reverse mappings from Braille to English.
        """
        
        # Mapping from English letters to Braille patterns
        self.english_to_braille_map = {
            "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
            "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
            "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
            "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
            "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
            "z": "O..OOO",
        }

        # Reverse mapping from Braille patterns to English letters
        self.braille_to_english_map = {}
        for k, v in self.english_to_braille_map.items():
            self.braille_to_english_map[v] = k


        # Mapping from numbers (as characters) to Braille patterns
        self.number_to_braille_map = {
            "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
            "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
        }

        # Reverse mapping from Braille patterns to numbers
        self.braille_to_number_map = {}
        for k, v in self.number_to_braille_map.items():
            self.braille_to_number_map[v] = k

        # Mapping from symbols to Braille patterns
        self.symbol_to_braille_map = {
            ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
            ";": "..O.O.", "_": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.",
            " ": "......",
        }

        # Reverse mapping from Braille patterns to symbols
        self.braille_to_symbol_map = {}
        for k, v in self.symbol_to_braille_map.items():
            self.braille_to_symbol_map[v] = k

        # Mapping from indicators (capitalization, number, etc.) to Braille patterns
        self.indicator_to_braille_map = {
            "capital": ".....O", "number": ".O.OOO", "decimal": ".O...O"
        }

        # Reverse mapping from Braille patterns to indicators
        self.braille_to_indicator_map = {}
        for k, v in self.indicator_to_braille_map.items():
            self.braille_to_indicator_map[v] = k

    def detect_input_type(self, input_text: str) -> str:
        """
        Detects whether the input string is in English or Braille.
        
        Args:
            input_text (str): The string to be translated.
        
        Returns:
            str: Returns "english" if the input is in English, and "braille" if it is in Braille.
        
        Raises:
            ValueError: If the input string is empty.
        """
        
        # Handle the case where the input string is empty
        if not input_text:
            raise ValueError("Cannot process empty string")

        # Set of valid English characters, excluding '.' to avoid confusion with Braille
        valid_english_chars = set(self.english_to_braille_map.keys()) | set(
            self.number_to_braille_map.keys() | self.symbol_to_braille_map.keys()
        )
        valid_english_chars.remove(".")

        # If any character in the input is a valid English character, assume the input is English
        for char in input_text:
            if char in valid_english_chars:
                return "english"

        # If no valid English characters are found, assume the input is Braille
        return "braille"

    def translate_braille_to_english(self, braille_text: str) -> str:
        """
        Translates a Braille string into English.
        
        Args:
            braille_text (str): A string of Braille patterns to be translated.
        
        Returns:
            str: The translated English string.
        
        Description:
            This function breaks down the Braille input into 6-character "cells," 
            interprets each one, and composes the corresponding English translation.
        """
        
        translated_text = []
        is_capital = False
        is_number = False

        # Split the Braille input into 6-character cells
        braille_cells = []
        i = 0
        while i < len(braille_text):
            braille_cells.append(braille_text[i:i + 6])
            i += 6


        # Process each Braille cell
        for cell in braille_cells:
            if cell in self.braille_to_indicator_map:
                # Handle special indicators for capitalization and numbers
                indicator = self.braille_to_indicator_map[cell]
                if indicator == "capital":
                    is_capital = True
                elif indicator == "number":
                    is_number = True

            elif is_number and cell in self.braille_to_number_map:
                # Convert Braille number cells to their respective digits
                translated_text.append(self.braille_to_number_map[cell])

            elif is_number and cell in self.braille_to_indicator_map:
                # Handle decimals or other indicators that may occur after numbers
                translated_text.append(".")

            elif cell in self.braille_to_english_map:
                # Convert Braille alphabet cells to their respective letters
                letter = self.braille_to_english_map[cell]
                if is_capital:
                    letter = letter.upper()  # Apply capitalization if required
                    is_capital = False
                translated_text.append(letter)

            elif cell in self.braille_to_symbol_map:
                # Convert Braille symbol cells to their respective symbols
                symbol = self.braille_to_symbol_map[cell]
                if symbol == " ":
                    is_number = False  # Reset number processing on encountering space
                translated_text.append(symbol)

        return "".join(translated_text)

    def translate_english_to_braille(self, english_text: str) -> str:
        """
        Translates an English string into Braille.
        
        Args:
            english_text (str): A string of English text to be translated.
        
        Returns:
            str: The translated Braille string.
        
        Description:
            This function processes each character in the English input, 
            converting it to its Braille equivalent and handling special cases like capitalization and numbers.
        """
        
        translated_text = []
        is_number = False

        # Process each character in the English input
        for char in english_text:
            if char.isalpha():
                # Handle uppercase letters by prefixing with the capitalization indicator
                if char.isupper():
                    translated_text.append(self.indicator_to_braille_map["capital"])
                    char = char.lower()

                translated_text.append(self.english_to_braille_map[char])

            elif char.isdigit():
                # Handle numbers by prefixing with the number indicator
                if not is_number:
                    is_number = True
                    translated_text.append(self.indicator_to_braille_map["number"])

                translated_text.append(self.number_to_braille_map[char])

            elif char in self.symbol_to_braille_map:
                # Handle symbols and reset number processing on encountering space
                if char == " ":
                    is_number = False

                translated_text.append(self.symbol_to_braille_map[char])

        return "".join(translated_text)

    def translate(self, input_text: str) -> str:
        """
        Detects the input type and translates the string accordingly.
        
        Args:
            input_text (str): The string to be translated (either in English or Braille).
        
        Returns:
            str: The translated string, either in Braille (if input was English) or in English (if input was Braille).
        
        Description:
            This function determines the input type (English or Braille) and calls the appropriate translation method.
        """
        
        # Detect whether the input is English or Braille
        input_type = self.detect_input_type(input_text)
        
        # Translate based on the detected input type
        if input_type == "english":
            return self.translate_english_to_braille(input_text)
        elif input_type == "braille":
            return self.translate_braille_to_english(input_text)


def main():
    """
    Main function to run the Braille translator.
    
    Description:
        This function reads input from the command line, 
        translates it using the BrailleTranslator class, and prints the result.
    """
    
    # Create an instance of BrailleTranslator
    translator = BrailleTranslator()
    
    # Read the user input from command-line arguments
    user_input = " ".join(sys.argv[1:])
    
    # Perform the translation
    translated_text = translator.translate(user_input)
    
    # Output the translated text
    print(translated_text)


if __name__ == "__main__":
    main()
