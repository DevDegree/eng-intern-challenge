"""
Translator class and script for Braille to English and vice versa
"""

import sys

class EnglishAndBrailleTranslator:
    """
    A class to represent a translator that translates a string in Braille to a string in English and vice versa.

    Constants:
    ----------
    _START_PATTERNS : list[str]
        A list of the 10 set beginning patterns of braille characters, ordered in sequence
    _END_PATTERNS : list[str]
        A list of the 3 relevant ending patterns that is used by a-z, 0-9, ordered by magnitude from smallest to largest
    _ALPHABET_NO_W : str
        A string containing the sequence of English characters that are sequential in Braille
    _W : str
        Braille representation of w, since its pattern differs from the rest of the a-z characters
    _SPACE : str
        Braille representation of a space
    _CAPITAL : str
        Braille representation that denotes capital follows
    _NUM_FOLLOWS: str
        Braille representation that denotes number follows 
    """

    _START_PATTERNS = ["O...", "O.O.", "OO..", "OO.O", "O..O", "OOO.", "OOOO", "O.OO", ".OO.", ".OOO"]
    _END_PATTERNS = ["..", "O.", "OO"]
    _ALPHABET_NO_W = "abcdefghijklmnopqrstuvxyz"
    _W = ".OOO.O"  # behaves differently than other a-z characters
    _SPACE = "......"
    _CAPITAL = ".....O"
    _NUM_FOLLOWS = ".O.OOO"

    def translate(self, s: str) -> str:
        """Takes a string, either english or braille and translates it to the opposite lang"""
        if len(s) % 6 == 0 and not any(c not in ".O" for c in s):
            return self.braille_to_english(s)
        elif "." not in s:
            return self.english_to_braille(s)
        return ""  # no valid translation
    
    def english_to_braille(self, eng_s: str) -> str:
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

    def braille_to_english(self, braille_s: str) -> str:
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
    
    def get_braille_char(self, eng_char: str) -> str:
        """Returns braille representation of an english character"""
        if eng_char == " ":
            return self._SPACE
        if eng_char == "capital":
            return self._CAPITAL
        if eng_char == "number follows":
            return self._NUM_FOLLOWS
        if eng_char == "w":
            return self._W
        
        if eng_char.isdigit():
            return self._START_PATTERNS[int(eng_char) - 1] + self._END_PATTERNS[0]
        
        idx = self._ALPHABET_NO_W.index(eng_char)
        start_idx, end_idx = idx % 10, idx // 10
        return self._START_PATTERNS[start_idx] + self._END_PATTERNS[end_idx]

    def get_eng_char(self, braille_char: str, is_num: bool) -> str:
        """Returns english representation of braille character given info if it should be a number or not"""
        if len(braille_char) != 6:
            raise ValueError("Braille character not a valid length.")
        
        if braille_char == self._SPACE:
            return " "
        if braille_char == self._CAPITAL:
            return "capital"
        if braille_char == self._NUM_FOLLOWS:
            return "number follows"
        if braille_char == self._W:
            return "w"
        
        start, end = braille_char[:4], braille_char[4:]
        idx = self._END_PATTERNS.index(end) * 10 + self._START_PATTERNS.index(start)
        if is_num:
            return str((1 + idx) % 10)
        return self._ALPHABET_NO_W[idx]
    

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