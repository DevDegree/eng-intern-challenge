import sys

class BrailleTranslator:
    def __init__(self):
        # initializing mappings
        self.map_to_braille = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..',
            'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.',
            'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO',
            'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', '1': 'O.....', '2': 'O.O...',
            '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
            '0': '.OOO..', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
        }
        self.to_eng_char = {}
        self.to_eng_num = {}
        self.map_to_eng()

    def map_to_eng(self):
        """
        Create hash maps to convert Braille to English characters and digits
        Input: None
        Returns: None
        """
        for k, v in self.map_to_braille.items():
            if k.isdigit():
                self.to_eng_num[v] = k
            else:
                self.to_eng_char[v] = k

    def is_braille(self, s):
        """
        Checks if the given string is made up entirely of Braille characters
        Input: string
        Returns: bool
        """
        return all(ch in 'O.' for ch in s)

    def to_eng(self, s):
        """
        Translates Braille to English
        Input: string
        Returns: string
        """
        eng = []
        num_follows, cap_follows = False, False
        braille = [s[i:i+6] for i in range(0, len(s), 6)]
        if not braille:
            return ""

        for ele in braille:
            if num_follows:
                ch = self.to_eng_num.get(ele, '')
            else:
                ch = self.to_eng_char.get(ele, '')

            if not ch:
                # Braille input is not valid
                return ""

            if ch == 'cap':
                cap_follows = True
            elif ch == 'num':
                num_follows = True
            elif cap_follows:
                eng.append(ch.upper())
                cap_follows = False
            else:
                eng.append(ch)

            if ch == ' ':
                num_follows = False

        return ''.join(eng)

    def to_braille(self, s):
        """
        Translate english to braille
        Input: string
        Returns: string
        """
        braille = []
        num_follows = False

        for ch in s:
            if ch.isupper():
                braille.append(self.map_to_braille['cap'])
                ch = ch.lower()
            if ch.isdigit() and not num_follows:
                braille.append(self.map_to_braille['num'])
                num_follows = True
            elif not ch.isdigit():
                num_follows = False

            braille_ch = self.map_to_braille.get(ch, '')
            if not braille_ch:
                # English input is not valid
                return ""

            braille.append(braille_ch)

        return ''.join(braille)

def main():
    translator = BrailleTranslator()
    sentence = " ".join(sys.argv[1:])
    if translator.is_braille(sentence):
        print(translator.to_eng(sentence))
    else:
        print(translator.to_braille(sentence))

if __name__ == "__main__":
    main()
