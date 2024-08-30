import sys

class Translator:
    #Dictionary mapping for English to Braille translation
    _english_braille_dict = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        ' ': '......',  #Space
        '.': '.O..OO', ',': '.O....', '?': '.OO.OO', '!': '.OOO.O', ':': '.O.OO.',
        ';': '.OO.O.', '-': '......O', '/': '......O.', '<': 'O..O..', '>': '.O...O',
        '(': 'O...OOO', ')': '.OO.OOO',
        'CAP': '.....O',  #Capital letter
        'NUM': '.O.OOO'   #Number
    }

    #Reverse dictionary for Braille to English translation
    _braille_alpha_dict = {v: k for k, v in _english_braille_dict.items() if k.isalpha() or k in " .,?!:;-/<>()"}
    _braille_num_dict = {v: k for k, v in _english_braille_dict.items() if k.isdigit()}

    def _is_english(self, arg: str) -> bool:
        """Checks if the input string is English or Braille"""
        #Assume it's English if it contains characters other than 'O' or '.'
        return bool(set(arg) - {"O", "."})

    def _get_braille(self, english: str) -> str:
        """Convert English text to Braille"""
        braille = []
        num_flag = False

        for char in english:
            if char.isdigit():
                if not num_flag:
                    num_flag = True
                    braille.append(self._english_braille_dict["NUM"])
            else:
                num_flag = False
                if char.isupper():
                    braille.append(self._english_braille_dict["CAP"])

            braille.append(self._english_braille_dict[char.lower()])

        return "".join(braille)

    def _get_english(self, braille: str) -> str:
        """Convert Braille to English text"""
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
                if num_flag:
                    english.append(self._braille_num_dict[chars])
                elif cap_flag:
                    english.append(self._braille_alpha_dict[chars].upper())
                    cap_flag = False
                else:
                    english.append(self._braille_alpha_dict[chars])

                if chars == self._english_braille_dict[' ']:
                    num_flag = False

        return "".join(english)

    def translate(self, args: str) -> str:
        """Translate from English to Braille or vice versa"""
        args = " ".join(args)

        if self._is_english(args):
            return self._get_braille(args)
        else:
            return self._get_english(args)

def main():
    translator = Translator()
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    print(translator.translate(sys.argv[1:]))

if __name__ == "__main__":
    main()
