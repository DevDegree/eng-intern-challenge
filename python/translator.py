import sys

class BrailleTranslator:
    # braille to alphanumeric dictionary
    ENG_TO_BRAI = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
        "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", 
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", 
        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
        "y": "OO.OOO", "z": "O..OOO", " ": "......",
    }

    # mapping english letters that can also represent digits in braille
    ENG_LETTER_TO_NUM = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }

    # alphanumeric to braille dictionary
    BRAI_TO_ENG = {v: k for k, v in ENG_TO_BRAI.items()}
    NUM_TO_ENG_LETTER = {v: k for k, v in ENG_LETTER_TO_NUM.items()}

    CAP_FOLLOWS = ".....O"
    NUM_FOLLOWS = ".O.OOO"
    SPACE = "......"

    # determine whether the text is braille or alphanumeric
    # return True if the text is braille, False otherwise
    def is_braille(self, text):
        # if the text is not a multiple of 6, it is not braille
        if (len(text) % 6 != 0):
            return False
    
        # check if all cells are in the braille dictionary
        # loop through text in increments of 6 (braille cell length is 6)
        cells = [text[i:i+6] for i in range(0, len(text), 6)]
        for cell in cells:
            if cell not in self.BRAI_TO_ENG and cell != self.CAP_FOLLOWS and cell != self.NUM_FOLLOWS:
                return False
        return True

    # translate english text to braille text
    # returns a string in braille format
    def translate_eng_to_braille(self, text):
        braille_text = ""
        # flag to determine if a num_follow cell is needed
        num_follows = False

        for char in text:
            # uppercase letter
            if char.isupper():
                braille_text += self.CAP_FOLLOWS
                braille_text += self.ENG_TO_BRAI[char.lower()]
            # char is a digit
            elif char.isdigit():
                # dont need to add a num_follow cell if the prev cell was a digit
                if num_follows:
                    braille_text += self.ENG_TO_BRAI[self.NUM_TO_ENG_LETTER[char]]
                # first digit, add a num_follow cell
                else:
                    braille_text += self.NUM_FOLLOWS
                    braille_text += self.ENG_TO_BRAI[self.NUM_TO_ENG_LETTER[char]]
                    num_follows = True
            # char is a space
            elif char == " ":
                # need to reset num_follows flag
                braille_text += self.ENG_TO_BRAI[char]
                num_follows = False
            # char is a letter
            else:
                braille_text += self.ENG_TO_BRAI[char]
        return braille_text

    # translate braille text to english text
    # returns a string in english format
    def translate_braille_to_eng(self, text):
        english_text = ""
        # flag to determine if a capital letter follows
        cap_follows = False
        # flag to determine if a number follows
        num_follows = False

        # loop through text in increments of 6 (braille cell length is 6)
        for i in range(0, len(text), 6):
            cell = text[i:i+6]
            # if braille cell is a num or cap follow cell
            if cell == self.CAP_FOLLOWS:
                cap_follows = True
            elif cell == self.NUM_FOLLOWS:
                num_follows = True
            # reset num_follows flag if we hit a space
            elif cell == self.SPACE:
                english_text += " "
                num_follows = False
            # curr char should be capital
            elif cap_follows:
                english_text += self.BRAI_TO_ENG[cell].upper()
                cap_follows = False
                num_follows = False
            # curr char is a digit
            elif num_follows and self.BRAI_TO_ENG[cell] in self.ENG_LETTER_TO_NUM:
                english_text += self.ENG_LETTER_TO_NUM[self.BRAI_TO_ENG[cell]]
            # curr char is a letter
            else:
                english_text += self.BRAI_TO_ENG[cell]
        return english_text
    
    def translate(self, text):
        # check if text is braille
        if self.is_braille(text):
            return self.translate_braille_to_eng(text)
        else:
            return self.translate_eng_to_braille(text)
        
        # if self.is_braille(text):
        #     return self.translate_eng_to_braille(self.translate_braille_to_eng(text))
        # else:
        #     return self.translate_braille_to_eng(self.translate_eng_to_braille(text))

if __name__ == "__main__":
    args = sys.argv[1:]
    inputText = ' '.join(args)
    translater = BrailleTranslator()
    print(translater.translate(inputText))

