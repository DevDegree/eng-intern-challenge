import sys

class BrailleTranslator:
    def __init__(self):
        # Bi-directional dictionary for fast lookup time O(1)
        self.english_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
            'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
            'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
            'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
            'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
            'y': 'OO.OOO', 'z': 'O..OOO', '.': '..OO.O', ',': '..O...',
            '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
            '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
            '(': 'O.O..O', ')': '.O.OO.', ' ': '......',
            'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
        }

        # Reverse dictionary for Braille to English
        self.braille_to_english = {v: k for k, v in self.english_to_braille.items()}
        
    def translate_to_braille(self, input):
        output = ""
        isNumber = False

        for char in input:
            # If a character is capitalized, lower the case for lookup
            if char.isupper():
                output += self.english_to_braille['capital']
                char = char.lower()

            # If a character is a number, convert it into an alphabet
            elif char.isnumeric():
                char = chr(int(char) + 96) # ASCII code
                
                # If a character marks the start of number, set isNumber boolean to true
                if not isNumber:
                    output += self.english_to_braille['number']
                    isNumber = True
            
            # If there is a decimal dot, append it to the output string
            elif char == '.' and isNumber:
                output += self.english_to_braille['decimal']
                    
            # If a space is found, isNumber is reset
            elif char == ' ':
                isNumber = False

            output += self.english_to_braille[char]

        return output

    def translate_to_english(self, input):
        output = ""

        # Track the next character's state
        isCapitalize = False
        isNumber = False
        isDecimal = False

        # Split the input string into chunks of 6 characters
        for i in range(0, len(input), 6):
            try:
                chunk = self.braille_to_english[input[i:i+6]]
                
                # Handle special cases
                if len(chunk) > 1: 
                    if chunk == 'capital':
                        isCapitalize = True
                    if chunk == 'number':
                        isNumber = True
                    if chunk == 'decimal':
                        isDecimal = True
                else:
                    if isCapitalize:
                        chunk = chunk.capitalize()
                        isCapitalize = False
                    elif chunk == ' ':
                        isNumber = False
                    elif isDecimal:
                        chunk = '.'
                        isDecimal = False
                    # Edge case where user types special characters in number
                    elif isNumber and input[i+4:i+6] == '..': # Last two nodes of all numbers are dots
                        chunk = str(ord(chunk) - 96) # a = 97 -> number = 1

                    output += chunk
                
            # If a character is not found in the dictionary, it is in English
            except KeyError:
                return ""
            
        return output


def main():
    if len(sys.argv) < 2:
        return ""

    input = ' '.join(sys.argv[1:]) # Include spaces
    output = ""

    # define translator
    translator = BrailleTranslator()

    # Determine input types
    # Case 1: Braille - input is divisible by 6 AND there are no chracters other than 0 and .
    if len(input) % 6 == 0 and any(char not in '0.' for char in input):
        output = translator.translate_to_english(input)
        
    # Case 2: English - other than Braille
    if output == "":
        output = translator.translate_to_braille(input)

    print(output)


if __name__ == "__main__":
    main()