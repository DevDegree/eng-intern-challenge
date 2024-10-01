# translator.py
import sys

braille_alphabet = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'capital': '.....O',
    'decimal': '.O...O',
    'number': '.O.OOO',
    ' ': '......'
}

braille_alphabet_numerical_and_decimal = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '.': '.O..OO',
    ',': '..O...',
    '?': '.O...O',
    '!': '.OO.O.',
    ':': '..O.O.',
    ';': '..O.OO',
    '-': '..OO..',
    '/': '..OO.O',
    '<': '.OO..O',
    '>': '.OO.OO',
    '(': '..OOO.',
    ')': '..OOOO'
}

alphabet = {v: k for k, v in braille_alphabet.items()}
alphabet_numerical_and_decimal = {v: k for k, v in braille_alphabet_numerical_and_decimal.items()}

class BrailleTranslator():
    """
    A class representing a Braille Translator.

    Attributes:
        args (list[str]): Arguments inputted to the class.
        output (str): The output translation string.

    Methods:
        _braille_to_english(): Translates to English and updates output attribute.
        _english_to_Braille(): Translates to Braille and updates output attribute.
        is_braille(): Returns True if the input is Braille. Otherwise, returns False.
        __str__(): Returns the output attribute as string.
    """

    def __init__(self, args: list[str]):
        """
        Initializes the BrailleTranslator with args from sys.argv.

        Parameters:
            args (list[str]): The args from sys.argv.
        """
        if len(args) <= 1:
            exit(1)

        # Words inputted
        self.args = args[1:]

        # Output as array
        self.output = []

        if self.is_braille():
            self._braille_to_english()
        else:
            self._english_to_braille()
    
    def _braille_to_english(self) -> None:
        """Translates to English and updates output attribute."""

        argument = self.args[0]
        special_characters = {
            "capital": False,
            "decimal": False,
            "number": False
        }

        for n in range(0, len(argument), 6):
            character: str = argument[n:n+6]

            # Checks whether to capitalize the following letter
            if special_characters["capital"]:
                character = alphabet.get(character).capitalize()
                special_characters["capital"] = False

            # Checks whether the following character is a decimal or number
            elif alphabet.get(character) != " " and (special_characters["decimal"] or special_characters["number"]) :
                character: str = alphabet_numerical_and_decimal.get(character)

            # Checks whether the following character is space
            elif alphabet.get(character) == " ":
                special_characters["capital"] = False
                special_characters["decimal"] = False
                special_characters["number"] = False
                character: str = " "

            # Check whether the following character is a special case: capital, decimal or number
            elif alphabet.get(character) in special_characters.keys():
                special_characters[alphabet.get(character)] = True
                character: str = ""

            # Checks other cases
            else:
                character: str = alphabet.get(character)

            self.output.append(character) if character not in ["", None] else None
            
        self.output = "".join(self.output)
        
    def _english_to_braille(self) -> None:
        """Translates to Braille and updates output attribute."""

        special_characters = {
            "decimal": False,
            "number": False
        }
        
        for k, argument in enumerate(self.args):

            for n in argument:

                # Checks whether the following character is a letter and in uppercase
                if n.isupper():
                    special_characters["decimal"] = False
                    special_characters["number"] = False
                    character: str = braille_alphabet.get("capital") + braille_alphabet.get(n.lower())
                
                # Checks whether the following character is a letter and in lowercase
                elif n.islower():
                    special_characters["decimal"] = False
                    special_characters["number"] = False
                    character: str = braille_alphabet.get(n)

                # Checks whether the following character is a number
                elif n.isdigit():
                    special_characters["decimal"] = False
                    character: str = braille_alphabet.get("number") if special_characters["number"] == False else ""
                    special_characters["number"] = True
                    character: str = character + braille_alphabet_numerical_and_decimal.get(n)
                
                # Checks whether the following character is a decimal
                elif n in braille_alphabet_numerical_and_decimal.keys():
                    special_characters["number"] = False
                    character: str = braille_alphabet.get("decimal") if special_characters["decimal"] == False else ""
                    special_characters["decimal"] = True
                    character: str = character + braille_alphabet_numerical_and_decimal.get(n)

                # Checks other cases, such as whether the following character is space
                else:
                    character: str = braille_alphabet.get(n)
                    special_characters["decimal"] = False
                    special_characters["number"] = False
                
                self.output.append(character)
            
            special_characters["decimal"] = False
            special_characters["number"] = False

            if k < len(self.args) - 1:
                self.output.append(braille_alphabet.get(" "))
            
        self.output = "".join(self.output)
    
    def is_braille(self) -> bool:
        """
        Checks whether the input text is Braille.
        
        Returns:
            bool: True if the input is Braille. Otherwise, returns False.
        """
        if len(self.args) == 1 and len(self.args[0]) % 6 == 0 and all(char in "O." for char in self.args[0]):
            return True
        
        return False
        
    def __str__(self) -> str:
        """
        Returns the output as string.

        Returns:
            str: output as string.
        """
        return self.output

def main():
    braille_translation = BrailleTranslator(sys.argv)

    print(braille_translation)

if __name__ == '__main__':
    main()