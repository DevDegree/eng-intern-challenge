# Constants class for storing various constants used in the Braille translation
class BrailleConstants:
    BRAILLE_CELL_LENGTH = 6  # Length of each Braille character

    # Map for translating English letters and spaces to Braille
    BRAILLE_LETTER_MAP = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO", " ": "......"
    }

    # Map for translating numbers to Braille
    BRAILLE_NUMBER_MAP = {
        "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
        "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
    }

    # Map for Braille control flags used to modify the interpretation of subsequent characters.
    BRAILLE_CONTROL_FLAG_MAP = {
        "uppercase": ".....O",  # Braille representation for the uppercase flag
        "number": ".O.OOO"  # Braille representation for the number flag
    }

# Braille translation class for converting between English and Braille
class BrailleTranslator:
    # Inverted maps for reverse translation from Braille to English
    INVERTED_BRAILLE_LETTER_MAP = {v: k for k, v in BrailleConstants.BRAILLE_LETTER_MAP.items()}
    INVERTED_BRAILLE_NUMBER_MAP = {v: k for k, v in BrailleConstants.BRAILLE_NUMBER_MAP.items()}

    def translate_english_to_braille(self, english):
        """
        Converts an English string into its Braille representation.
        For uppercase letters, the Braille translation is prefixed with an 'uppercase' flag.
        For numbers, the translation is prefixed with a 'number' flag to switch into number mode.
        If a space or other character is encountered, it is directly translated based on the Braille map.
        """
        result = ""  # Resulting Braille string
        number_flag = False  # Flag to track if we're currently in number mode

        for char in english:
            if char.isupper():
                # Prefix with uppercase flag and convert the character to its lowercase Braille equivalent
                result += BrailleConstants.BRAILLE_CONTROL_FLAG_MAP["uppercase"]
                result += BrailleConstants.BRAILLE_LETTER_MAP[char.lower()]
                number_flag = False  # Reset number mode when switching to letters
            elif char.isdigit():
                if not number_flag:
                    # If we're not already in number mode, add the number flag
                    result += BrailleConstants.BRAILLE_CONTROL_FLAG_MAP["number"]
                    number_flag = True  # Enter number mode
                result += BrailleConstants.BRAILLE_NUMBER_MAP[char]
            elif char in BrailleConstants.BRAILLE_LETTER_MAP:
                # Translate a regular lowercase letter
                result += BrailleConstants.BRAILLE_LETTER_MAP[char]
                number_flag = False  # Reset number mode when switching to letters
            elif char == " ":
                # Translate the space character
                result += BrailleConstants.BRAILLE_LETTER_MAP[" "]
                number_flag = False  # Reset number mode after a space
            else:
                # Raise an error if an unsupported character is encountered
                raise ValueError(f"Unsupported character: {char}")

        return result

    def translate_braille_to_english(self, braille):
        """
        Converts a Braille string back into its English representation.
        If the Braille string includes an 'uppercase' flag, the following letter is translated as uppercase.
        If the Braille string includes a 'number' flag, the following characters are treated as numbers.
        Spaces and other recognized characters are directly translated.
        """
        result = ""  # Resulting English string
        i = 0  # Index for iterating over the Braille string
        uppercase_next = False  # Flag to track if the next letter should be uppercase
        number_flag = False  # Flag to track if we're currently in number mode

        while i < len(braille):
            chunk = braille[i:i + BrailleConstants.BRAILLE_CELL_LENGTH]  # Extract a 6-character chunk
            if chunk == BrailleConstants.BRAILLE_CONTROL_FLAG_MAP["uppercase"]:
                # If the chunk is an uppercase flag, set the uppercase_next flag
                uppercase_next = True
            elif chunk == BrailleConstants.BRAILLE_CONTROL_FLAG_MAP["number"]:
                # If the chunk is a number flag, set the number_mode flag
                number_flag = True
            else:
                # Handle number or letter translation
                if number_flag and chunk in self.INVERTED_BRAILLE_NUMBER_MAP:
                    # If in number mode and the chunk matches a Braille number,
                    # look up the corresponding digit and add it to the result.
                    result += self.INVERTED_BRAILLE_NUMBER_MAP[chunk]
                elif uppercase_next and chunk in self.INVERTED_BRAILLE_LETTER_MAP:
                    # If the uppercase_next flag is set and the chunk matches a Braille letter,
                    # translate it to uppercase, add to the result, and reset the flag.
                    result += self.INVERTED_BRAILLE_LETTER_MAP[chunk].upper()
                    uppercase_next = False
                elif chunk in self.INVERTED_BRAILLE_LETTER_MAP:
                    # If no special modes are active, translate the chunk as a regular letter
                    result += self.INVERTED_BRAILLE_LETTER_MAP[chunk]
                    number_flag = False  # Reset number mode when switching to letters
                else:
                    # Raise an error if an unsupported Braille sequence is encountered
                    raise ValueError(f"Unsupported Braille sequence: {chunk}")

            i += BrailleConstants.BRAILLE_CELL_LENGTH  # Move to the next chunk

        return result

    def translate(self, input_string):
        """
        Determines if the input string is in Braille or English and translates it.
        If the input string contains only 'O' and '.' characters, it is assumed to be Braille.
        Otherwise, the input is treated as an English string.
        """
        is_braille = all(char in 'O.' for char in input_string)
        if is_braille:
            return self.translate_braille_to_english(input_string)
        else:
            return self.translate_english_to_braille(input_string)


def main():
    import sys

    if len(sys.argv) < 2:
        raise Exception("Arguments missing. Please try again.")

    input_string = " ".join(sys.argv[1:])  # Capture input from command-line arguments
    translator = BrailleTranslator()  # Initialize the translator

    try:
        translation = translator.translate(input_string)  # Perform the translation
        print(translation)  # Output the result
    except ValueError as e:
        # Handle any errors during translation
        print(f"Error: {e}")


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
