import argparse
import unittest


# Dictionary mapping Braille characters to English letters, numbers, and symbols
braille_to_english = {
    "LETTERS": {
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
        "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
        "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
        ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
        "OO.OOO": "y",  "O..OOO": "z"
    },

    "NUMBERS": {
        ".OOOOO": "0", "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
        "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9"
    },
    
    "SYMBOLS": {
        "......": " ", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":",
        "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O..OO.": ">", "O.O..O": "(",
        ".O.OO.": ")", 
        ".....O": "^", # Indicates Uppercase follows
        ".O...O": "%", # Indicates Decimal follows
        ".O.OOO": "#", # Indicates Number follows
    }
}

# Create the corresponding english_to_braille dictionary with the same structure
# Allows for easy conversion from English to Braille.
english_to_braille = {
    "LETTERS": {v: k for k, v in braille_to_english["LETTERS"].items()},
    "NUMBERS": {v: k for k, v in braille_to_english["NUMBERS"].items()},
    "SYMBOLS": {v: k for k, v in braille_to_english["SYMBOLS"].items()}
}

def check_if_braille(text):
    """
    Function to check if the provided text is Braille or English
    @param text: the input string to check
    @return: True if the text is valid Braille, False if its English
    """

    # Check if the length of the text is a multiple of 6, which is characteristic of Braille characters
    if len("".join(text)) % 6 != 0:
        return False
    
    # Validate each 6-character Braille representation in the text
    for i in range(0, len(text), 6):
        checkBraille = text[i:i+6]
        if not(checkBraille in braille_to_english["LETTERS"].keys() or checkBraille in braille_to_english["NUMBERS"].keys() or checkBraille in braille_to_english["SYMBOLS"].keys()):
            return False
    
    return True

def convert_to_braille(input_str):
    """
    Function to convert an English string to Braille
    @param input_str: List of arg string
    @return: the translated Braille string represented by '.' and 'O'
    """

    is_number = False
    with_space_args = " ".join(input_str)
    output = ""
    
    # Iterate through each character in the input string
    for char in with_space_args:

        # If the character is a number and not already in number mode, prepend the number symbol
        if char.isnumeric() and not is_number:
            output += english_to_braille["SYMBOLS"]['#']
            is_number = True
        
        # Convert the number to its Braille equivalent
        if char.isnumeric() and is_number:
            output += english_to_braille["NUMBERS"][char]
            continue

        # Add space and turn number mode False (number ends with space)
        elif char == ' ':
            output += english_to_braille["SYMBOLS"][' ']
            is_number = False
            continue
        
        # Convert alphabetic characters to Braille, handling uppercase letters
        if char.isalpha():
            if char.isupper():
                output += english_to_braille["SYMBOLS"]['^']

            output += english_to_braille["LETTERS"][char.lower()]
        
        # Handle special symbols in the text
        else:
            output += english_to_braille["SYMBOLS"][char.lower()]
    
    return output


def convert_to_english(input_str):
        """
        Function to convert a Braille string to English
        @param input_str: string of braille represented by '.' and 'O'
        @return: the translated English string
        """

        is_capital = False
        is_number = False
        output = ""

        # Iterate through the Braille string in 6-character increments
        for i in range(0, len(input_str), 6):
            braille = input_str[i:i+6]

            # Detect if the current symbol indicates capitalization
            if braille == english_to_braille["SYMBOLS"]["^"]:
                is_capital= True
                continue
            
            # Detect if the current symbol indicates number mode (doesnt translate to text)
            if braille == english_to_braille["SYMBOLS"]["#"]:
                is_number = True
                continue
            
            if braille == english_to_braille["SYMBOLS"]["%"]:
                output += "."
                continue

            if is_number and braille in braille_to_english["NUMBERS"]:
                output += braille_to_english["NUMBERS"][braille]
                continue

            if is_capital and braille in braille_to_english["LETTERS"]:
                output += braille_to_english["LETTERS"][braille].upper()
                is_capital = False
                continue
            
            if braille in braille_to_english["LETTERS"]:
                output += braille_to_english["LETTERS"][braille]
                continue

            if braille == english_to_braille["SYMBOLS"][" "]:
                output += braille_to_english["SYMBOLS"][braille]
                is_number = False
                continue
            
            if braille in braille_to_english["SYMBOLS"]:
                output += braille_to_english["SYMBOLS"][braille]
                continue
        
        return output

def main():
    parser = argparse.ArgumentParser(description="Process a variable number of arguments")
    parser.add_argument('arguments', nargs='+', help='One or more arguments are required')
    args_list = parser.parse_args().arguments

    no_space_args = "".join(args_list)
    is_braille_text = check_if_braille(no_space_args)

    if is_braille_text:
        output = convert_to_english(no_space_args)
    else:
        output = convert_to_braille(args_list)
    
    print(output)

class TestBrailleConversion(unittest.TestCase):

    def test_braille_to_english(self):
        self.assertEqual(convert_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."), "Hello world")
        self.assertEqual(convert_to_english(".O.OOOOO.O..O.O..."), "42")
        self.assertEqual(convert_to_english(".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."), "Abc 123")
        self.assertEqual(convert_to_english(".....OO.....O..........OO....."), "AaA")
        self.assertEqual(convert_to_english(".O.OOOO.....O.O...OO............OOO...OO.O.....OO..OO...OO.O"), "123 !.O.")
        self.assertEqual(convert_to_english("..OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO......OO..OO."), ".O.O.OO")

    def test_english_to_braille(self):
        self.assertEqual(convert_to_braille(["42"]), ".O.OOOOO.O..O.O...")
        self.assertEqual(convert_to_braille(["Hello world"]), ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
        self.assertEqual(convert_to_braille(["Abc 123"]), ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
        self.assertEqual(convert_to_braille(["AaA"]), ".....OO.....O..........OO.....")
        self.assertEqual(convert_to_braille(["123 !.O."]), ".O.OOOO.....O.O...OO............OOO...OO.O.....OO..OO...OO.O")
        self.assertEqual(convert_to_braille([".O.O.OO"]), "..OO.O.....OO..OO...OO.O.....OO..OO...OO.O.....OO..OO......OO..OO.")

if __name__ == "__main__":
    #main()
    unittest.main()