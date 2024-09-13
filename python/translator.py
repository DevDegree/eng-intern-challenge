import sys

# Define Braille mappings
class Translator:
    
    def __init__(self):
        self.braille_to_eng= {
        # Letters
        "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
        "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
        "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
        "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
        "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", 
        "O..OOO": "z",
        }
        
        self.braille_to_eng_punctuation = {
        "..O...": ",", "..OO.O": ".", "..O.OO": "?", "..OOO..": "!", "..OO..": ":", 
        "..O.O.": ";", "O.O..O": "(", ".O.OO.": ")", "....OO": "-", ".O..O.": "/",
        ".OO..O": "<", "O..OO.": ">", "......": " ",
        }
        
        self.braille_to_eng_digits = {
            "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
            "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
        }

        self.eng_to_braille = {v: k for k, v in self.braille_to_eng.items()}
        self.eng_to_braille_digits = {v: k for k, v in self.braille_to_eng_digits.items()}
        self.eng_to_braille_punctuation = {v: k for k, v in self.braille_to_eng_punctuation.items()}

    def is_braille(self, input_str:str):
        '''
            It checks if the input_str is a braille string. If the length is less than 6
            or if the substring consisting of first 6 letters exists in braille_to_eng
            then it returns True
            
            Parameters:
            -----------
                input_str:str
                    The input string
            
            Returns:
            --------
                bool
        '''
        
        if len(input_str) < 6:
            return False
        
        braille_chars = set(["O", "."])
        chars = set(input_str[:6])
        return braille_chars == chars
        

    def braille_to_english_translation(self, braille_str: str):
        '''
            Translates the braille input string to english.
            Parameters:
            -----------
                braille_str: str
                    The braille string
                    
            Returns:
            --------
                str
                    The translated the string
        '''
        result = []
        # Split Braille string into 2x3 character grids
        braille_chars = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
        next_upper_case = False
        next_digit = False
        for char in braille_chars:
            if next_upper_case:
                char_to_append = self.braille_to_eng.get(char, '?').upper()  # '?' for unrecognized patterns
                next_upper_case = False
            elif next_digit:
                char_to_append = self.braille_to_eng_digits.get(char, "?")
            elif char == ".....O": # next char is a upper case
                next_upper_case = True
                continue
            elif char == ".O.OOO": # next char is a digit
                next_digit = True
                continue
            elif char == ".O...O": # next char should be a decimal we just append a "."
                char_to_append = "."
            elif char in self.braille_to_eng_punctuation: # conflicts with "o" and ">"
                char_to_append = self.braille_to_eng_punctuation.get(char, "?")
            else:
                char_to_append = self.braille_to_eng.get(char, "?")
                
            result.append(char_to_append) 
        return ''.join(result)

    # Translate English to Braille
    def english_to_braille_translation(self, english_str: str):
        """
        Translates the English input string to Braille.

        Parameters:
        -----------
            english_str: str
                The English string

        Returns:
        --------
            str
                The translated Braille string
        """
        result = []
        next_digit = False
        
        for char in english_str:
            if char.isdigit():
                if not next_digit:
                    result.append(".O.OOO") # braille digit prefix
                next_digit = True
                result.append(self.eng_to_braille_digits.get(char))
            else:
                next_digit = False # no longer encoding digits
                if char.isupper():
                    result.append(".....O") # append upper symbol
                    char_to_append = self.eng_to_braille.get(char.lower(), '******')  # '......' for unknown characters
                elif not char.isalnum(): # if not alphnumeric then must be punctuation.
                    char_to_append = self.eng_to_braille_punctuation.get(char)
                else: # otherwise is just a regular letter
                    char_to_append = self.eng_to_braille.get(char.lower(), '******') # '......' for unknown characters
                    
                result.append(char_to_append)
        return ''.join(result)

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: braille_translator <string>")
        sys.exit(1)

    input_str = " ".join(sys.argv[1:])
    
    translator = Translator()

    if translator.is_braille(input_str):
        print(translator.braille_to_english_translation(input_str))
    else:
        print(translator.english_to_braille_translation(input_str))