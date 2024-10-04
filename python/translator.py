

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
          'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
          'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
          'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
          'O..OOO': 'z',
          
          # Special symbols
          '.....O': 'capital follows',
          '.O.OOO': 'number follows',
          '......': 'space',
          
          # Punctuation
          '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!',
          '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/',
          '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')'
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
          ' ': '......',        # space

          # Punctuation
          '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.',
          ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
          '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
        }
        return english_to_braille_dict


    def string_to_translate():
        """
        If string contains symbol or space that is not 'O' or '.' then english, else it is braille.
        """
        return

    def translate_braille():
        """
        Pattern match every 6 symbols. If capital or first number; prefix with relevant 6 symbols
        otherwise 6 symbols for letter, number, space or punctuation.
        """
        return 


    def translate_english():
        """
        pattern match every letter, number, space and other symbols to the braille configuration.
        include prefix for capital letters and first number. 
        """
        return 


if __name__ == "__main__":
    # Test code
    brailletranslator = BrailleTranslator()
    print("Testing braille_to_english_dict:")
    print(f"'O.....' translates to: {brailletranslator.braille_to_english_dict['O.....']}")
    print("\nTesting english_to_braille_dict:")
    print(f"'a' translates to: {brailletranslator.english_to_braille_dict['a']}")











































