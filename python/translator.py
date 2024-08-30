import sys


class BrailleMapping:
    """Handles mapping between English and Braille representations"""

    NUMBER_FOLLOWS = ".O.OOO"
    CAPITAL_FOLLOWS = ".....O"
    SPACE = "......"

    ENGLISH_TO_BRAILLE = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
        "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
        "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
        "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO", " ": SPACE,
        "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....",
        "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
        "8": "O.OO..", "9": ".OO..."
    }

    BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items()}


class Translator:
    """Provides translation between English and Braille"""

    @staticmethod
    def english_to_braille(text: str) -> str:
        result = []
        for word in text.split():
            braille_word = []
            is_number = False
            for char in word:
                if char.isdigit():
                    if not is_number:
                        braille_word.append(BrailleMapping.NUMBER_FOLLOWS)
                        is_number = True
                    braille_word.append(BrailleMapping.ENGLISH_TO_BRAILLE[char])
                else:
                    if is_number:
                        is_number = False
                    if char.isupper():
                        braille_word.append(BrailleMapping.CAPITAL_FOLLOWS)
                        braille_word.append(BrailleMapping.ENGLISH_TO_BRAILLE[char.lower()])
                    else:
                        braille_word.append(BrailleMapping.ENGLISH_TO_BRAILLE[char])
            result.append("".join(braille_word))
        return BrailleMapping.SPACE.join(result)

    @staticmethod
    def braille_to_english(text: str) -> str:
        result = []
        i, n = 0, len(text)
        is_number = False
        while i < n:
            braille_char = text[i:i + 6]
            if braille_char == BrailleMapping.NUMBER_FOLLOWS:
                is_number = True
            elif braille_char == BrailleMapping.CAPITAL_FOLLOWS:
                i += 6
                braille_char = text[i:i + 6]
                result.append(BrailleMapping.BRAILLE_TO_ENGLISH[braille_char].upper())
            elif braille_char == BrailleMapping.SPACE:
                result.append(" ")
                is_number = False
            else:
                result.append(BrailleMapping.BRAILLE_TO_ENGLISH[braille_char])
                is_number = False
            i += 6
        return "".join(result)


class InputClassifier:
    """Determines whether the input string is Braille or English"""

    @staticmethod
    def is_braille(text: str) -> bool:
        return '.' in text or 'O' in text


def main():
    input_text = " ".join(sys.argv[1:])
    if InputClassifier.is_braille(input_text):
        print(Translator.braille_to_english(input_text))
    else:
        print(Translator.english_to_braille(input_text))


if __name__ == "__main__":
    main()
