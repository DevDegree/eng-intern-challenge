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
          # Note: 'O..OO.' will always return letter 'o' as per challenge requirements.
          # The challenge doesn't specify handling '>' (which has the same braile pattern as 'o',
          # so we're interpreting this pattern solely as the letter 'o'.
          'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
          'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
          'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
          'O..OOO': 'z',
          # Special symbols
          '.....O': 'capital follows',
          '.O.OOO': 'number follows',
          '......': ' ',
          '......': ' ',
          # Punctuation
          '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
          '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
          '.OO..O': '<', 'O.O..O': '(', '.O.OO.': ')',
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
          'decimal': '.O.OO.',
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
                print("Type is English:")
                return self.translate_english(input_str)
        print("Type is Braille")    
        result = self.translate_braille(input_str)
        return ''.join(result)     
    

    def translate_braille(self, input_str):
        """
        Translates a Braille string to English, handling capital letters, numbers, lowercase letters, punctuation and spaces.
        """
        result = []
        number_follows = False
        capital_follows = False
        for i in range(0, len(input_str), 6):
            chunk = input_str[i:i+6]
            if chunk == '.....O' :
                capital_follows = True
                continue
            elif chunk == '.O.OOO':
                number_follows = True
                continue
            
            char = self.braille_to_english_dict[chunk]
            if capital_follows:
                char = char[0].upper()
                capital_follows = False
            if type(char) == tuple:
                if number_follows:
                    char = char[1]
                else:
                    char = char[0]
            result.append(char)
        return ''.join(result)


    def translate_english(self, input_str):
        """
        Translates English to Braille, handling letters, numbers and symbols.
        Includes prefix for captial letters and the first number appearing after a space.
        """
        result = []
        cap_prefix_req = False
        num_prefix_req = True
        for char in input_str:
            if char.isupper():
                cap_prefix_req = True
                result.append(self.english_to_braille_dict['capital'])
                continue
            elif char.isnumeric():
                if num_prefix_req:
                    result.append(self.english_to_braille_dict['number'])
                    num_prefix_req = False
                result.append(self.english_to_braille_dict[char])
                continue
            elif char == ' ':
                num_prefix_req = True
            
            if cap_prefix_req:
                result.append(self.english_to_braille_dict[char.lower()])
                cap_prefix_req = False
            result.append(self.english_to_braille_dict[char])
                

        return ''.join(result)

if __name__ == "__main__":
    # Test code
    brailletranslator = BrailleTranslator()
    print("Testing braille_to_english_dict:")
    print(f"'O.....' translates to: {brailletranslator.braille_to_english_dict['O.....']}")
    print("\nTesting english_to_braille_dict:")
    print(f"'a' translates to: {brailletranslator.english_to_braille_dict['a']}")
    print("Testing string_to_translate with braille string")
    print(brailletranslator.translate(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
    print("Testing string_to_translate with english string")
    print(brailletranslator.translate("Hello World!"))











































