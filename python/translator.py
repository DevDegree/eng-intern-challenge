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
        pass

    def translate(self, args: str) -> str:
        """ Translate Braille to English or English to Braille
        
        :param args: list of english or braille strings
        :type args: list[str]
        :returns: concatenated string of translated english/braille from args
        :rtype: str
        """
        pass


if __name__ == "__main__":
    translator = Translator()
    print(translator.translate(sys.argv[1:]))
