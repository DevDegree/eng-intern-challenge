import sys

# define a translator Class
class BrailleEnglishTranslator:
    # Braille indicators
    BRAILLE_CHAR_LEN = 6
    CAP_FOLLOWS = '.....O'
    NUM_FOLLOWS = '.O.OOO'

    # English to Braille and Braille to English dictionary/lookup
    LETTER_TO_BRAILLE = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 
        'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
        'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
        's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
        'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    }

    BRAILLE_TO_LETTER = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
        'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
        'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
        '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
        'OO.OOO': 'y', 'O..OOO': 'z', '......': ' '
    }

    BRAILLE_TO_NUMBER = {
        'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6',
        'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', '......': ' '
    }

    NUMBER_TO_BRAILLE = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
        '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', ' ': '......'
    }

    def translate(self, input_str):
        if (self.is_braille(input_str)):
            return self.braille_to_english(input_str)
        else:
            return self.english_to_braille(input_str)

    def is_braille(self, str):
        if (len(str) % self.BRAILLE_CHAR_LEN != 0): # braille must be groupings of 6
            return False
        
        for i in range(0, len(str), 6):
            letter = str[i:i+self.BRAILLE_CHAR_LEN]
            if not ((letter in self.BRAILLE_TO_LETTER.keys()) or letter == self.CAP_FOLLOWS or letter == self.NUM_FOLLOWS):
                return False # valid braille groupings must be in the defined dictionary
        
        return True
    
    def braille_to_english(self, str):
        translated_str = ''
        translate_nums = False
        i = 0

        while i < len(str):
            braille_input = str[i:i+self.BRAILLE_CHAR_LEN] # current group of 6 that represents a character
            
            if (braille_input == self.CAP_FOLLOWS):
                i += 6 # take the next group/character
                next_input = str[i:i+self.BRAILLE_CHAR_LEN] 
                translated_str += self.BRAILLE_TO_LETTER[next_input].upper() # no access errors since it was validated in line 43 already
            
            elif (braille_input == self.NUM_FOLLOWS):
                translate_nums = True # set the flag for future inputs
            
            elif translate_nums and (braille_input in self.BRAILLE_TO_NUMBER.keys()): # avoiding errors on input like 123xyz
                translation = self.BRAILLE_TO_NUMBER[braille_input]
                translated_str += translation
                if (translation == ' '): # reset the flag
                    translate_nums = False
            
            else: # implies current section is a regular letter
                translation = self.BRAILLE_TO_LETTER[braille_input]
                translated_str += translation

            i += 6 # iterate to the next group of 6 chars
        
        return translated_str

    def english_to_braille(self, str):
        translated_str = ''
        prev_is_number = False # flag for whether or not the previous input was already a number

        for char in str:
            if char.isupper():
                translated_str += self.CAP_FOLLOWS
                translated_str += self.LETTER_TO_BRAILLE[char.lower()]
                prev_is_number = False
            
            elif char.isdigit():
                if not prev_is_number: # avoid printing num follows indicator for multiple numbers
                    translated_str += self.NUM_FOLLOWS
                    prev_is_number = True
                translated_str += self.NUMBER_TO_BRAILLE[char]
            
            elif char in self.LETTER_TO_BRAILLE.keys(): # spaces and lowercase
                translated_str += self.LETTER_TO_BRAILLE[char]
                prev_is_number = False
        
        return translated_str
    
if __name__ == "__main__":
    args = sys.argv[1:]
    input_str = ' '.join(args)
    braille_english_translator = BrailleEnglishTranslator()
    
    print(braille_english_translator.translate(input_str))





    

