import argparse

class Translator:
    def __init__(self):
        """
        A translator that translates Braille to English and vice versa.
        
        Requirements:
        1. Letters a through z
            - The ability to capitalize letters
        2. Numbers 0 through 9
        3. The ability to include spaces (multiple words)
        
        NOTE:
        When a Braille CAPITAL symbol is read, assume only the next symbol should be capitalized.
        When a Braille NUMBER symbol is read, assume all following symbols are numbers until the next SPACE symbol.
        """
        self.alphabet_to_braille = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", 
                                    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", 
                                    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
                                    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", 
                                    "y": "OO.OOO", "z": "O..OOO"}
        self.braille_to_alphabet = {val: key for key, val in self.alphabet_to_braille.items()}
        self.SPACE = "......"
        self.CAPITAL = ".....O"
        self.NUMBER = ".O.OOO"
    
    def translate(self, words):
        """Determine if the string given is either Braille or English and convert it accordingly.

        Args:
            words (str): the string to be translated

        Returns:
            list: the final result of translation
        """
        translation = []
        is_brail = self._is_braille(words)
    
        if not is_brail:
            self.eng_to_braille(words, translation)
        else:
            self.braille_to_eng(words, translation)
            
        return "".join(translation)
    
    def _is_braille(self, words):
        """Return True if words is braille and False if not.

        Args:
            words (str): a string given to be translated

        Returns:
            boolean: True if words is braille.
        """
        return all(char == "." or char == "O" for char in words)
    
    def eng_to_braille(self, words, translation):
        """Convert an alphanumeric string to brailles.

        Args:
            words (str): a string given to be translated
            translation (list): stores translated word
        """
        is_digit = [False]
        for char in words:
            if char.isnumeric():
                self.num_to_braille(char, translation, is_digit)
            elif char == " ": # char is space
                if is_digit[0]:
                    is_digit[0] = False
                translation.append(self.SPACE)
            else:
                self.alph_to_braille(char, translation)

    def num_to_braille(self, char, translation, is_digit):
        """Convert a numeric string to braille.
        
        NOTE: Brailles of numeric characters of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] are equal to 
        those of alphabetical characters from a to j, respectively.
        To avoid redundancy, we calculate the integer representation of the numerical char 
        to match the braille of the corresponding alphabet in the self.alphabet_to_braille.

        Args:
            char (str): a string to be translated
            translation (list): stores translated char
            is_digit (bool): tells whether the following strings should be numbers
        """
        if not is_digit[0]:
            translation.append(self.NUMBER)
            is_digit[0] = True
        
        if char == "0":
            translation.append(self.alphabet_to_braille["j"])
        else:
            translation.append(self.alphabet_to_braille[chr(ord(char) + ord("0"))])
            
    def braille_to_num(self, char, translation):
        """Convert a braille string of an alphabet to a digit.
        
        NOTE: Brailles of numeric characters of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] are equal to 
        those of alphabetical characters from a to j, respectively.
        To avoid redundancy, we calculate the integer representation of the alphabetical char
        to convert it to a digit.

        Args:
            char (str): a string to be translated
            translation (list): stores translated char
        """
        if char == "j":
            translation.append("0")
        else:
            translation.append(chr(ord(char) - ord("0")))
                           
    def alph_to_braille(self, char, translation): 
        """Convert an alphabetical string to braille.

        Args:
            char (str): a string to be translated
            translation (list): stores translated char
        """
        if char.isupper():
            translation.append(self.CAPITAL)
            translation.append(self.alphabet_to_braille[char.lower()])
        else:
            translation.append(self.alphabet_to_braille[char.lower()])
        
    def braille_to_eng(self, words, translation):
        """Convert brailles to an alphanumeric string.

        Args:
            words (str): a string given to be translated
            translation (list): stores translated word
        """
        curr_braille = ""
        is_capital = False
        is_digit = False
        
        # do this to ensure we translate the last 6 braille dots
        new_word = words + "+"
        
        for i in range(len(new_word)):
            char = new_word[i]
            if len(curr_braille) == 6:
                if curr_braille == self.CAPITAL:
                    is_capital = True
                elif curr_braille == self.NUMBER:
                    is_digit = True
                elif curr_braille == self.SPACE:
                    if is_digit:
                        is_digit = False
                    translation.append(" ") 
                else: # curr_braille corresponds to alpha
                    alph = self.braille_to_alphabet[curr_braille]
                    if is_capital:
                        translation.append(alph.upper())
                        is_capital = False
                    elif is_digit:
                        alph = self.braille_to_alphabet[curr_braille]
                        self.braille_to_num(alph, translation)
                    else: # it's just a regular alphabet now
                        translation.append(alph)
                curr_braille = char

            else:       
                curr_braille += char

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words_list", nargs='*')
    parsed_args = parser.parse_args()
    translator = Translator()    
    words = " ".join(parsed_args.words_list)
    print(translator.translate(words))

if __name__ == "__main__":
    main()