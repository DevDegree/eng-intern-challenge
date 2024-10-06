class BrailleTranslator:
    def __init__(self):
        """
        Initialize the translator and create dictionaries
        """
        self.braille_to_english_dict = self.build_braille_to_english_dict()
        self.english_to_braille_dict = self.build_english_to_braille_dict()


    def build_braille_to_english_dict(self):
        """
        Build a dictionary matching braille to english letters, numbers, spaces and specific rules 
        """
        braille_to_english_dict = {
        # Letters and Numbers
        'O.....': ('a', '1'), 'O.O...': ('b', '2'), 'OO....': ('c', '3'), 
        'OO.O..': ('d', '4'), 'O..O..': ('e', '5'), 'OOO...': ('f', '6'), 
        'OOOO..': ('g', '7'), 'O.OO..': ('h', '8'), '.OO...': ('i', '9'), 
        '.OOO..': ('j', '0'),     
        # Letters only
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z',
        # Special symbols
        '.....O': 'capital follows',
        '.O.OOO': 'number follows',
        '.O.OO.': 'decimal follows',
        '......': ' ',
        # Punctuation
        '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
        '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
        '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')',
        # Edge case
        'O..OO.': ('o','>'),
        }
        return braille_to_english_dict

    def build_english_to_braille_dict(self):
        """
        Build a dictionary matching english letters, numbers, spaces and specific rules to braille.
        """
        english_to_braille_dict = {
        # Letters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',
        # Numbers
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        # Special symbols
        'capital': '.....O',  # 'capital follows' indicator
        'number': '.O.OOO',   # 'number follows' indicator
        'decimal': '.O.OO.', # 'decimal follows' indicator
        ' ': '......',        # space
        # Punctuation
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
        ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
        '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
        }
        return english_to_braille_dict

    def translate(self, input_str):
        
        """
        Translates between English and Braille. Automatically detects the input string type. 
        If any 6-character chunk doesn't match a known Braille pattern, the entire output
        is treated as English. 
        """
        braille_str = True
        # Check each 6-character chunk
        for i in range(0, len(input_str),6):
            chunk = input_str[i:i+6]
            #If chunk is not in Braille dictionary, it is not Braille
            if chunk not in self.braille_to_english_dict.keys():
                braille_str = False
                break

        # Translate based on input type
        if braille_str:
            result = self.translate_braille(input_str)
        else:
            result = self.translate_english(input_str)
        
        return result 

    


    def translate_braille(self, input_str):
        """
        Translates a Braille string to English, handling capital letters, numbers, lowercase letters, punctuation and spaces.
        """
        result = []
        number_follows = False
        capital_follows = False
        decimal_follows = False
        open_bracket_count = 0

        for i in range(0, len(input_str), 6):
            chunk = input_str[i:i+6]
            char = self.braille_to_english_dict.get(chunk)

            # Handle special indicators
            if chunk == '.....O' : # Capital follows indicator
                capital_follows = True
                continue
            elif chunk == '.O.OOO': # Number follows indicator
                number_follows = True
                continue

            elif chunk == '.O.OO.': # Decimal follows indicator
                decimal_follows = True
                continue
            
            # Handle 'o' vs '>' edge case
            if chunk == '.OO..O':  # Left angle bracket
                open_bracket_count += 1
            elif chunk == 'O..OO.':  # Potential 'o' or '>'
                if open_bracket_count > 0:
                    char = '>'
                    open_bracket_count -= 1
                else:
                    char = 'o'
            # Process letter/number tuples vs strings
            if isinstance(char, tuple):
                if number_follows:
                    char = char[1]
                else:
                    char = char[0]
            # Capitalization
            if capital_follows:
                char = char.upper()
                capital_follows = False

            # Process for decimal numbers
            if decimal_follows:
                result.append('.')
                decimal_follows = False

            result.append(char)

            # Resetting number follows when space encountered
            if char == ' ':
                number_follows = False
        return ''.join(result)


    def translate_english(self, input_str):
        """
        Translates English to Braille, handling letters, numbers and symbols.
        Includes prefix for captial letters and the first number appearing after a space.
        """
        result = []
        num_prefix_req = True
        for i, char in enumerate(input_str):

            if char.isupper():
                # Add capital indicator for uppercase letters
                result.append(self.english_to_braille_dict['capital'])
                char = char.lower()

            elif char.isnumeric():
                if num_prefix_req:
                    # Add number indicator before first number after a space
                    result.append(self.english_to_braille_dict['number'])
                    num_prefix_req = False
            
            elif char == '.':
                if (i > 0 and input_str[i-1].isnumeric()) and (i + 1 < len(input_str) and input_str[i + 1].isnumeric()):
                    result.append(self.english_to_braille_dict['decimal'])
                

            elif char == ' ':
                # Reset number follows indicator after space encountered
                num_prefix_req = True

            result.append(self.english_to_braille_dict[char])

        return ''.join(result)


if __name__ == "__main__":
    import sys
    
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Error: arguments are missing!")
        sys.exit(1)
    
    # Combine command-line arguments into a single string
    input_str = " ".join(sys.argv[1:]).strip()

    # Create an instance of BrailleTranslator class
    translator = BrailleTranslator()

    # Translate input string
    result = translator.translate(input_str)

    # Print to console
    print(result)