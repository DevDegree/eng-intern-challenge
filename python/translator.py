import sys


class Translator:
    # alpha -> braille
    _english_braille_dict = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
        "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
        "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO", "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....",
        "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
        ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
        "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",
        " ": "......", "CAP": ".....O", "DEC": ".O...O", "NUM": ".O.OOO",
    }

    # braille -> alpha (alpha/symbols only)
    _braille_alpha_dict = {
        val: key for key, val 
        in _english_braille_dict.items() 
        if key.isalpha() or key in " .,?!:;-/<>()"
    }
    
    # braille -> alpha (nums only)
    _braille_num_dict = {
        val: key for key, val 
        in _english_braille_dict.items() 
        if key.isdigit()
    }

    def _is_english(self, arg: str) -> bool:
        """ Checks if `arg` is braille
        
        :param arg: english or braille string
        :type arg: str
        :returns: True if arg is english else False
        :rtype: bool
        """
        # cannot be braille if len(arg) % 6 != 0
        if len(arg) % 6:
            return True

        # cannot be braille if arg contains any character other than `O` or `.`
        return bool(set(arg) - {"O", "."})

    def _get_braille(self, english: str) -> str:
        """ Convert english to braille

        :param english: english string
        :type english: str
        :returns: braille translation
        :rtype: str
        """
        braille = []
        num_flag = False

        for char in english:
            if char.isdigit():
                # only add `number follows` for intial number
                if not num_flag:
                    num_flag = True
                    braille.append(self._english_braille_dict["NUM"])
            else:
                num_flag = False
                if char.isupper():
                    braille.append(self._english_braille_dict["CAP"])

            braille.append(self._english_braille_dict[char.lower()]) # will not throw error even if char is numeric 

        return "".join(braille)

    def _get_english(self, braille: str) -> str:
        """ Convert braille to english

        :param braille: braille string
        :type braille: str
        :returns: english translation
        :rtype: str
        """
        english = []
        num_flag = False
        cap_flag = False

        for idx in range(0, len(braille), 6):
            chars = braille[idx:idx+6]

            if chars == self._english_braille_dict["NUM"]:
                num_flag = True
            elif chars == self._english_braille_dict["CAP"]:
                cap_flag = True
            else:
                # end of sequence of numbers (or just a space)
                if chars == self._english_braille_dict[" "]:
                    num_flag = False
                    english.append(self._braille_alpha_dict[chars])
                elif num_flag:
                    english.append(self._braille_num_dict[chars])
                elif cap_flag:
                    cap_flag = False
                    english.append(self._braille_alpha_dict[chars].upper())
                else:
                    english.append(self._braille_alpha_dict[chars])

        return "".join(english)

    def translate(self, args: str) -> str:
        """ Translate Braille to English or English to Braille
        
        :param args: list of english or braille strings
        :type args: list[str]
        :returns: concatenated string of translated english/braille from args
        :rtype: str
        """
        # adding spaces inbetween arguments
        args = [item for arg in args for item in (arg, " ")][:-1]

        return "".join([
            self._get_braille(arg) 
            if self._is_english(arg) 
            else self._get_english(arg) 
            for arg in args
        ])


if __name__ == "__main__":
    translator = Translator()
    print(translator.translate(sys.argv[1:]))
