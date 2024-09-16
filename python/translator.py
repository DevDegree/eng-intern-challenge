import sys

class BrailleTranslator:
    """
    A class used to translate between English and Braille

    Supports the entire English alphabet, capitalization, 
    spaces, and numbers. Can be extended to support other 
    symbols
    """
    # Braille symbols
    CAPITAL_SYMBOL = '.....O'
    NUMBER_SYMBOL  = '.O.OOO'
    SPACE_SYMBOL   = '......'
    
    # Character translation dictionaries
    ENGLISH_TO_BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......'
    }

    NUMBER_TO_BRAILLE = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
    }

    BRAILLE_TO_ENGLISH = {braille: english for english, braille in ENGLISH_TO_BRAILLE.items()}
    BRAILLE_TO_NUMBER  = {braille: english for english, braille in NUMBER_TO_BRAILLE.items()}

    def __init__(self):
        pass

    def is_braille(self, input: str) -> bool:
        """
        Checks if the input string is in Braille
        """
        return all(char in 'O.' for char in input)

    def translate_to_english(self, input: str) -> str:
        """
        Translates a Braille string to English
        """

        # Using a list because it is more efficient than concatenating strings
        result = []
        i = 0
        capitalize_next = False
        translating_numbers = False
        
        while i < len(input):
            braille_char = input[i:i+6]
            
            if braille_char == self.CAPITAL_SYMBOL:
                capitalize_next = True
            elif braille_char == self.NUMBER_SYMBOL:
                translating_numbers = True
            elif braille_char == self.SPACE_SYMBOL:
                translating_numbers = False
                result.append(' ')
            elif translating_numbers and braille_char in self.BRAILLE_TO_NUMBER:
                result.append(self.BRAILLE_TO_NUMBER[braille_char])
            elif braille_char in self.BRAILLE_TO_ENGLISH and not translating_numbers:
                char = self.BRAILLE_TO_ENGLISH[braille_char]
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
            else:
                raise ValueError(f"Invalid Braille character: {braille_char}")
            
            # Move to index of the next Braille character
            i += 6
        
        return ''.join(result)

    def translate_to_braille(self, input: str) -> str:
        """
        Translates an English string to Braille
        """
        # Using a list because it is more efficient than concatenating strings
        result = []
        translating_numbers = False
        
        for char in input:
            if char.isdigit():
                if not translating_numbers:
                    result.append(self.NUMBER_SYMBOL)
                    translating_numbers = True
                result.append(self.NUMBER_TO_BRAILLE[char])
            elif char.isupper():
                result.append(self.CAPITAL_SYMBOL)
                result.append(self.ENGLISH_TO_BRAILLE[char.lower()])
            elif char.lower() in self.ENGLISH_TO_BRAILLE:
                result.append(self.ENGLISH_TO_BRAILLE[char.lower()])
            elif char == ' ':
                result.append(self.SPACE_SYMBOL)
                translating_numbers = False
            else:
                raise ValueError(f"Invalid English character: {char}")
        
        return ''.join(result)

    def translate(self, input: str) -> str:
        """
        Translates input to the appropriate output, based on input type
        """
        if self.is_braille(input):
            return self.translate_to_english(input)
        else:
            return self.translate_to_braille(input)


def main():
    # Read command line arguments
    if len(sys.argv) > 1:
        input_str = ' '.join(sys.argv[1:])
        translator = BrailleTranslator()
        
        try:
            output = translator.translate(input_str)
            print(output)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Please provide a string to translate")

if __name__ == "__main__":
    main()
