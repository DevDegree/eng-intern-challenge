import sys
import argparse
from enum import Enum


class Translator:

    NUM_FOLLOWS = ".O.OOO"
    SPACE = "......"
    CAPITAL_FOLLOWS = ".....O"

    eng_to_braille = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..'
    }

    braille_to_eng = {
        'O.....': 'a',
        'O.O...': 'b',
        'OO....': 'c',
        'OO.O..': 'd',
        'O..O..': 'e',
        'OOO...': 'f',
        'OOOO..': 'g',
        'O.OO..': 'h',
        '.OO...': 'i',
        '.OOO..': 'j',
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': 'o',
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z'
    }

    braille_to_num = {
        'O.....': '1',
        'O.O...': '2',
        'OO....': '3',
        'OO.O..': '4',
        'O..O..': '5',
        'OOO...': '6',
        'OOOO..': '7',
        'O.OO..': '8',
        '.OO...': '9',
        '.OOO..': '0'
    }

    class Lang(Enum):
        ENGLISH = 1
        BRAILLE = 2

    def detect_lang(self, text):
        if set(text) == {'.', 'O'}:
            return Translator.Lang.BRAILLE
        return Translator.Lang.ENGLISH

    def translate_to_braille(self, text):
        braille = ""
        num_follows = False
        for c in text:
            if c.isupper():
                braille += self.CAPITAL_FOLLOWS
                braille += self.eng_to_braille[c.lower()]
            elif c.isspace():
                braille += self.SPACE
                num_follows = False
            elif c.isnumeric() and not num_follows:
                braille += self.NUM_FOLLOWS
                num_follows = True
                braille += self.eng_to_braille[c] 
            else:
                braille += self.eng_to_braille[c]
        return braille

    def translate_to_english(self, text):
        braille_list = [text[i:i+6] for i in range(0, len(text), 6)]
        eng_txt = ""
        capital_follows = False
        num_follows = False
        for braille in braille_list:
            if braille == self.NUM_FOLLOWS:
                num_follows = True
                continue
            if braille == self.CAPITAL_FOLLOWS:
                capital_follows = True
                continue
            if braille == self.SPACE:
                eng_txt += " "
                num_follows = False
                continue
            if num_follows:
                eng_txt += self.braille_to_num[braille]
            elif capital_follows:
                capital_follows = False
                eng_txt += self.braille_to_eng[braille].upper()
            else:
                eng_txt += self.braille_to_eng[braille]
        return eng_txt
                            
    def translate(self, text):
        lang = self.detect_lang(text)
        if lang == Translator.Lang.ENGLISH:
            print(self.translate_to_braille(text))
        elif lang == Translator.Lang.BRAILLE:
            print(self.translate_to_english(text))

if __name__ == "__main__":
    translator = Translator()
    text = " ".join(sys.argv[1:])
    translator.translate(text)