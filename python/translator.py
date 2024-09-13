import sys

#Assumin there are no edge cases wiht a ix of numbers and letters "0h3ie"

#Use constants because it doesn't take that much extra space but can save on computation
BRAILLE_CAPITAL_FOLLOWS = ".....O"  
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"  

BRAILLE_TO_ENGLISH = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z"
}

BRAILLE_TO_NUMBERS = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

ENGLISH_TO_BRAILLE_NUMBERS = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse mapping
ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

class Translator:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def determine_language(self):
        """
        Determine language is Braille or English!

        
        Check if the input contains only 'O' and '.'
        and its length is divisible by 6
        
        
        """
        if all(char in "O." for char in self.input_string) and len(self.input_string) % 6 == 0:
            return "Braille"
        else:
            return "English"

    def translate(self):
        """
        Call on diff. translation methods given the output of determine_language function


        
        """
        input_type = self.determine_language()
        
        if input_type == "Braille":
            return self.braille_to_english()
        else:
            return self.english_to_braille()

    def braille_to_english(self):
        """
        Translate Braille to English.
        
        """
        output = []
        is_capital = False
        is_number = False
        
        # Split the input into chunks of 6 (Braille symbols are in 2*3 format)
        braille_chars = [self.input_string[i:i+6] for i in range(0, len(self.input_string), 6)]
        
        for char in braille_chars:

            if char == BRAILLE_CAPITAL_FOLLOWS:
                is_capital = True
                continue

            if char == BRAILLE_NUMBER_FOLLOWS:
                is_number = True
                continue
            
            if char == "......":  # Handle space
                output.append(" ")
                is_number = False
                continue

            if is_number:
                # If in numbers mode, use the BRAILLE_TO_NUMBERS dictionary
                if char in BRAILLE_TO_NUMBERS:
                    output.append(BRAILLE_TO_NUMBERS[char])
                else:
                    output.append("?")  # Unrecognized number
            else:
                if str(char) in BRAILLE_TO_ENGLISH:
                    letter = BRAILLE_TO_ENGLISH[str(char)]
                    if letter == "capital":
                        is_capital = True
                        continue
                    
                    if is_capital:
                        letter = letter.upper()
                        is_capital = False  # Only capitalize one letter
                    output.append(letter)
                else:
                    output.append("?")

        return "".join(output)

    def english_to_braille(self):
        """
        
        Translate English to Braille.
        
        """
        output = []
        isNumber = False  # Flag to check if we are in 'number mode'
        
        for char in self.input_string:
            if char == " ":
                output.append("......")  
                isNumber = False  # Reset number mode when space is encountered

            elif char.isupper():
                output.append(BRAILLE_CAPITAL_FOLLOWS)
                output.append(ENGLISH_TO_BRAILLE[char.lower()])
             
            elif char.isdigit():
                if not isNumber:  # Only append the number symbol once
                    output.append(BRAILLE_NUMBER_FOLLOWS)
                    isNumber = True  # Set flag to indicate number mode is active
                    
                # Numbers are translated 
                output.append(ENGLISH_TO_BRAILLE_NUMBERS[char])
                
            else:
                output.append(ENGLISH_TO_BRAILLE.get(char, "......"))  # Default to space if unrecognized
                isNumber = False  # If it's not a number, reset the flag

        # Join the output: not necessary tbh, can use string
        return "".join(output)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        translator = Translator(input_string)
        result = translator.translate()
        print(result)
    else:
        print("Please provide an input string to translate.")
