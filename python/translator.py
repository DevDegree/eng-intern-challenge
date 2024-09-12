import sys

class Translator:
    """
    A class used to translate between English and Braille.

    Attributes:
        eng_to_brail (dict): A dictionary mapping English characters to their Braille representations.
        num_to_brail (dict): A dictionary mapping numbers to their Braille representations.
        brail_to_eng (dict): A dictionary mapping Braille characters to their English equivalents.
        brail_to_num (dict): A dictionary mapping Braille numbers to their numeric equivalents.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Translator with dictionaries for converting between English and Braille.
        """
        
        self.CAPITAL_SYMBOL = ".....O"
        self.NUMBER_SYMBOL = ".O.OOO"
        self.SPACE_SYMBOL = "......"

        self.eng_to_brail = {
            "a": "O.....",
            "b": "O.O...",
            "c": "OO....",
            "d": "OO.O..",
            "e": "O..O..",
            "f": "OOO...",
            "g": "OOOO..",
            "h": "O.OO..",
            "i": ".OO...",
            "j": ".OOO..",
            "k": "O...O.",
            "l": "O.O.O.",
            "m": "OO..O.",
            "n": "OO.OO.",
            "o": "O..OO.",
            "p": "OOO.O.",
            "q": "OOOOO.",
            "r": "O.OOO.",
            "s": ".OO.O.",
            "t": ".OOOO.",
            "u": "O...OO",
            "v": "O.O.OO",
            "w": ".OOO.O",
            "x": "OO..OO",
            "y": "OO.OOO",
            "z": "O..OOO",
            ".": "..OO.O",
            ",": "..O...",
            "?": "..O.OO",
            "!": "..OOO.",
            ":": "..OO..",
            ";": "..O.O.",
            "-": "....OO",
            "/": ".O..O.",
            "<": ".OO..O",
            "(": "O.O..O",
            ")": ".O.OO.", 
            " ": self.SPACE_SYMBOL,
            "capital": self.CAPITAL_SYMBOL,
            "number": self.NUMBER_SYMBOL
        }
        self.num_to_brail = {
            "1": "O.....",
            "2": "O.O...",
            "3": "OO....",
            "4": "OO.O..",
            "5": "O..O..",
            "6": "OOO...",
            "7": "OOOO..",
            "8": "O.OO..",
            "9": ".OO...",
            "0": ".OOO.."
        }
        self.brail_to_eng = {v: k for k, v in self.eng_to_brail.items()}
        self.brail_to_num = {v: k for k, v in self.num_to_brail.items()}

    def translate_to_english(self, inp_string: str) -> str:
        """
        Translates a Braille string to English.

        Args:
            inp_string (str): The input Braille string consisting of 'O' and '.' characters, 
                              representing Braille characters in groups of 6.

        Returns:
            str: The translated English string.

        This function handles capitalization and numbers. If a capital symbol or number 
        symbol is encountered, the subsequent Braille characters are translated accordingly.
        """
        result = []
        capital = False
        number = False
        for i in range(0, len(inp_string), 6):
            braille_char = inp_string[i:i+6]
            
            if braille_char == self.CAPITAL_SYMBOL:
                capital = True
            elif braille_char == self.NUMBER_SYMBOL:
                number = True
            elif braille_char == self.SPACE_SYMBOL:
                result.append(" ")
                number = False
            else:
                if number:
                    result.append(self.brail_to_num[braille_char])
                elif capital:
                    result.append(self.brail_to_eng[braille_char].upper())
                    capital = False
                else:
                    result.append(self.brail_to_eng[braille_char])

        return "".join(result)

    def translate_to_braille(self, inp_string: str) -> str:
        """
        Translates an English string to Braille.

        Args:
            inp_string (str): The input English string to be translated.

        Returns:
            str: The translated Braille string.

        This function handles capitalization and numbers. If a capital letter is encountered,
        a capital symbol is added before its corresponding Braille representation. Numbers are
        preceded by a number symbol.
        """
        number_mode = False
        result = []
        for c in inp_string:
            if c.lower() not in self.eng_to_brail and c not in self.num_to_brail and not c.isspace():
                raise ValueError(f"Unsupported character: {c}")
            if c.isdigit():
                if not number_mode:
                    result.append(self.eng_to_brail['number'])
                    number_mode = True
                result.append(self.num_to_brail[c])
            else:
                number_mode = False
                if c.isupper():
                    result.extend([self.eng_to_brail['capital'], self.eng_to_brail[c.lower()]])
                else:
                    result.append(self.eng_to_brail[c])
        
        return "".join(result)
    
    def is_braille(self, inp_str: str) -> bool:
        """
        Determines if the given string is Braille.

        Args:
            inp_str (str): The string to be checked.

        Returns:
            bool: True if the string is Braille, False otherwise.
        """
        return all(c in "O." for c in inp_str) and len(inp_str) % 6 == 0

    def translate(self, inp_str: str) -> str:
        """
        Translates a given string between English and Braille.

        Args:
            inp_str (str): The input string, either Braille or English.

        Returns:
            str: The translated string, either Braille or English, depending on the input.
        """
        if self.is_braille(inp_str):
            return self.translate_to_english(inp_str)
        return self.translate_to_braille(inp_str)
    
def run_translator(input_str: str) -> str:
    """
    Function that acts as the main entry for translating a string.

    Args:
        input_str (str): The input string to be translated.

    Returns:
        str: The translated result.
    """
    translator = Translator()
    return translator.translate(input_str)    

def main() -> None:
    """
    The main function that executes when the script is run from the command line.

    It reads input from the command line and prints the translation.
    """
    input_str = " ".join(sys.argv[1:])
    result = run_translator(input_str)
    print(result)

if __name__ == "__main__":
    main()