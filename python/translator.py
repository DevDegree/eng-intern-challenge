"""
Translator class and script for Braille to English and vice versa
"""

import sys

class EnglishAndBrailleTranslator:
    """
    A class to represent a translator that translates a string in Braille to a string in English and vice versa.

    Attributes:
    -----------
    braille_to_english_map : dict[str, str]
        A mapping of braille string representation to english letters
    english_to_braille_map : dict[str, str]
        A mapping of english letters to braille string representation
    """

    START_PATTERNS = ["O...", "O.O.", "OO..", "OO.O", "O..O", "OOO.", "OOOO", "O.OO", ".OO.", ".OOO"]
    END_PATTERNS = ["..", "O.", "OO"]
    ALPHABET_NO_W = "abcdefghijklmnopqrstuvxyz"
    W = ".OOO.O"  # behaves differently than other a-z characters
    SPACE = "......"
    CAPITAL = ".....O"
    NUM_FOLLOWS = ".O.OOO"

    def get_braille_char(self, eng_char: str) -> str:
        """Returns braille representation of an english character"""
        if eng_char == " ":
            return self.SPACE
        if eng_char == "capital":
            return self.CAPITAL
        if eng_char == "number follows":
            return self.NUM_FOLLOWS
        if eng_char == "w":
            return self.W
        
        if eng_char.isdigit():
            return self.START_PATTERNS[int(eng_char) - 1] + self.END_PATTERNS[0]
        
        idx = self.ALPHABET_NO_W.index(eng_char)
        start_idx, end_idx = idx % 10, idx // 10
        return self.START_PATTERNS[start_idx] + self.END_PATTERNS[end_idx]

    def get_eng_char(self, braille_char: str, is_num: bool) -> str:
        """Returns english representation of braille character given info if it should be a number or not"""
        if len(braille_char) != 6:
            raise ValueError("Braille character not a valid length.")
        
        if braille_char == self.SPACE:
            return " "
        if braille_char == self.CAPITAL:
            return "capital"
        if braille_char == self.NUM_FOLLOWS:
            return "number follows"
        if braille_char == self.W:
            return "w"
        
        start, end = braille_char[:4], braille_char[4:]
        idx = self.END_PATTERNS.index(end) * 10 + self.START_PATTERNS.index(start)
        if is_num:
            return str((1 + idx) % 10)
        return self.ALPHABET_NO_W[idx]
        
    def translate(self, s: str) -> str:
        """Takes a string, either english or braille and translates it to the opposite lang"""
        if len(s) % 6 == 0 and not any(c not in ".O" for c in s):
            return self._braille_to_english(s)
        elif "." not in s:
            return self._english_to_braille(s)
        return ""  # no valid translation
    
    def _english_to_braille(self, eng_s: str) -> str:
        """Helper to translate an english string to braille"""
        num_follows = False
        braille_chars = []

        for c in eng_s:
            if c.isdigit():
                if not num_follows:
                    braille_chars.append(self.get_braille_char("number follows"))
                braille_chars.append(self.get_braille_char(c))
                num_follows = True
                continue

            braille_char = self.get_braille_char(c.lower())
            if c.isupper():
                braille_chars.append(self.get_braille_char("capital"))
                braille_chars.append(braille_char)
            else:
                braille_chars.append(braille_char)

            num_follows = False

        return "".join(braille_chars)

    def _braille_to_english(self, braille_s: str) -> str:
        """Helper to translate a braille string to english"""
        num_follows, cap_follows = False, False
        english_str = ""

        for i in range(0, len(braille_s), 6):
            braille_char = braille_s[i : i + 6]
            eng_char = self.get_eng_char(braille_char, num_follows)
            if eng_char == "capital":
                cap_follows = True
                continue
            if eng_char == "number follows":
                num_follows = True
                continue
            if eng_char == " ":
                num_follows = False
            
            if cap_follows:
                english_str += eng_char.upper()
                cap_follows = False
            else:
                english_str += eng_char
    
        return english_str
    

def main():
    """Runs translator application"""
    if len(sys.argv) < 2:
        print("ERROR: Invalid number of arguments. Usage: python3 translator.py [str] ... [str]")
        return

    translator = EnglishAndBrailleTranslator()
    args = " ".join(sys.argv[1:])
    print(translator.translate(args))

if __name__ == "__main__":
    main()