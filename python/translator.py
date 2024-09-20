import sys
from typing import Dict, List, Callable
from functools import partial
from itertools import groupby
from string import ascii_lowercase

class BrailleTranslator:
    ENGLISH_TO_BRAILLE: Dict[str, str] = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO", " ": "......"
    }
    PUNC_TO_BRAILLE: Dict[str, str] = {
        '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
        ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '(': 'O.O..O',
        ')': '.O.OO.'
    }

    NUMBER_TO_BRAILLE: Dict[str, str] = {}
    BRAILLE_TO_ENG: Dict[str, str] = {}
    BRAILLE_TO_NUM: Dict[str, str] = {}
    BRAILLE_TO_PUNC: Dict[str, str] = {}

    NUM: str = ".O.OOO"
    SPACE: str = "......"
    CAP: str = ".....O"

    @classmethod
    def initialize(cls):
        number_chars = '123456789' + '0'
        cls.NUMBER_TO_BRAILLE = dict(zip(number_chars, [cls.ENGLISH_TO_BRAILLE[c] for c in ascii_lowercase[:10]]))
        cls.BRAILLE_TO_ENG = {v: k for k, v in cls.ENGLISH_TO_BRAILLE.items()}
        cls.BRAILLE_TO_NUM = {v: k for k, v in cls.NUMBER_TO_BRAILLE.items()}
        cls.BRAILLE_TO_PUNC = {v: k for k, v in cls.PUNC_TO_BRAILLE.items()}

    @staticmethod
    def is_braille(s: str) -> bool:
        return len(s) % 6 == 0 and set(s).issubset({'O', '.'})

    @classmethod
    def to_english(cls, s: str) -> str:
        brailles: List[str] = [s[i:i+6] for i in range(0, len(s), 6)]
        
        def translate_group(key: str, group: List[str]) -> str:
            if key == cls.NUM:
                return ''.join(map(cls.BRAILLE_TO_NUM.get, group, [''] * len(group)))
            elif key == cls.SPACE:
                return ' ' * len(group)
            else:
                return ''.join(map(cls.BRAILLE_TO_ENG.get, group, [''] * len(group)))

        result = []
        for key, group in groupby(brailles, key=lambda x: x if x in (cls.NUM, cls.SPACE) else 'char'):
            group = list(group)
            if key == cls.CAP:
                result.append(translate_group('char', group[1:]).upper())
            else:
                result.append(translate_group(key, group))

        return ''.join(result)

    @classmethod
    def to_braille(cls, s: str) -> str:
        def char_to_braille(char: str) -> str:
            if char.isdigit():
                return cls.NUMBER_TO_BRAILLE[char]
            elif char.isalpha():
                return (cls.CAP if char.isupper() else '') + cls.ENGLISH_TO_BRAILLE[char.lower()]
            elif char in cls.PUNC_TO_BRAILLE:
                return cls.PUNC_TO_BRAILLE[char]
            else:
                return cls.SPACE

        result = []
        for key, group in groupby(s, key=str.isdigit):
            if key:
                result.append(cls.NUM)
            result.extend(map(char_to_braille, group))

        return ''.join(result)

# Initialize the class
BrailleTranslator.initialize()

def main():
    s: str = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    
    translate: Callable[[str], str] = translator.to_english if translator.is_braille(s) else translator.to_braille
    print(translate(s))

if __name__ == "__main__":
    main()
