#Approach:
#Two functions to create the braille-english dictionaries
#One function to determine if braille or english
#Two functions to translate
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
        Determines whether the input string is English or Braille. 
        If 6 character string does not match a known Braille pattern, the input_str is English
        """
        for i in range(0, len(input_str),6):
            chunk = input_str[i:i+6]
            if chunk not in self.braille_to_english_dict.keys():
                return self.translate_english(input_str)
        result = self.translate_braille(input_str)
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


            if char is None: # Invalid chunk encountered
                continue  
            
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
    translator = BrailleTranslator()
    output = translator.translate("Abc 123 xYz")
    print(output)
    output_2 = translator.translate(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
    print(output_2)

        
# if __name__ == "__main__":
#     brailletranslator = BrailleTranslator()

#     # Test 1: braille_to_english_dict
#     test_input = "O....."
#     expected_output = ('a', '1')
#     result = brailletranslator.braille_to_english_dict[test_input]
#     print("Testing braille_to_english_dict:")
#     print(f"Input (Braille): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")
#     print()

#     # Test 2: english_to_braille_dict
#     test_input = "a"
#     expected_output = "O....."
#     result = brailletranslator.english_to_braille_dict[test_input]
#     print("Testing english_to_braille_dict:")
#     print(f"Input (English): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")
#     print()

#     # Test 3: translate with Braille string
#     test_input = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO."
#     expected_output = "Hello World!"
#     result = brailletranslator.translate(test_input)
#     print("Testing translate with Braille string:")
#     print(f"Input (Braille): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")
#     print()

#     # Test 4: translate with English string
#     test_input = "Hello World!"
#     expected_output = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O....OOO."
#     result = brailletranslator.translate(test_input)
#     print("Testing translate with English string:")
#     print(f"Input (English): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")
#     print()

#     # Test 5: 'o' vs '>' distinction
#     test_input = "O..OO..OO..OO..OO."
#     expected_output = "o<>"
#     result = brailletranslator.translate_braille(test_input)
#     print("Testing 'o' vs '>' distinction:")
#     print(f"Input (Braille): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")


#     # Test 6: Decimal number translation
#     test_input = ".O.OOOOO.....O.OO.OO...."  # Braille for "3.14"
#     expected_output = "3.3"
#     result = brailletranslator.translate_braille(test_input)
#     print("Testing decimal number translation:")
#     print(f"Input (Braille): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")

#     # Test 7: Period at end of sentence
#     test_input = "pi."
#     expected_output = "OOO.O..OO.....OO.O"
#     result = brailletranslator.translate_english(test_input)
#     print("Testing simple sentence with period:")
#     print(f"Input (English): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")

#     # Test 2: Sentence with decimal number and period
#     test_input = "3.3."
#     expected_output = ".O.OOOOO.....O.OO...OO.OOO......OO.O"
#     result = brailletranslator.translate_english(test_input)
#     print("\nTesting sentence with decimal number and period:")
#     print(f"Input (English): {test_input}")
#     print(f"Expected Output: {expected_output}")
#     print(f"Actual Output: {result}")
#     print(f"Test {'passed' if result == expected_output else 'failed'}")

































