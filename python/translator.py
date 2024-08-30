import sys


class BrailleTranslator:
    TEXT_TO_BRAILLE = {
        "a": "O.....", "b": "O.O...",
        "c": "OO....", "d": "OO.O..",
        "e": "O..O..", "f": "OOO...",
        "g": "OOOO..", "h": "O.OO..",
        "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.",
        "m": "OO..O.", "n": "OO.OO.",
        "o": "O..OO.", "p": "OOO.O.",
        "q": "OOOOO.", "r": "O.OOO.",
        "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO",
        "w": ".OOO.O", "x": "OO..OO",
        "y": "OO.OOO", "z": "O..OOO",
        " ": "......", "0": ".OOO..",
        "1": "O.....", "2": "O.O...",
        "3": "OO....", "4": "OO.O..",
        "5": "O..O..", "6": "OOO...",
        "7": "OOOO..", "8": "O.OO..",
        "9": ".OO...", "capital_follows": ".....O",
        "number_follows": ".O.OOO",
    }

    BRAILLE_TO_TEXT = {
        # Exclude numeric keys to avoid mapping same key to multiple values (e.g "j" and "0")
        v: k for k, v in TEXT_TO_BRAILLE.items() if not k.isnumeric()
    }

    @staticmethod
    def translate(input_list) -> str:
        '''
            Translate input text (list of strings) to braille or braille to text
            accordingly and return converted text (str)
        '''
        input_str: str = " ".join(input_list)

        def determine_input_type(input_str: str) -> str:
            return "braille" if "." in input_str else "text"

        translations = {
            "braille": BrailleTranslator.braille_to_text,
            "text": BrailleTranslator.text_to_braille,
        }

        return translations[determine_input_type(input_str)](input_str)

    @classmethod
    def text_to_braille(cls, text: str) -> str:
        braille_result: str = ""
        number_follows = False

        for c in text:
            if c == " ":
                braille_result += cls.TEXT_TO_BRAILLE.get(c)
                # Set number follows flag to False
                number_follows = False
            elif c.isupper():
                braille_result += cls.TEXT_TO_BRAILLE.get("capital_follows", "*")
                braille_result += cls.TEXT_TO_BRAILLE.get(c.lower(), "*")
            elif c.isnumeric():
                if not number_follows:
                    # Add a number follows to the braille result first
                    braille_result += cls.TEXT_TO_BRAILLE.get("number_follows", "*")
                braille_result += cls.TEXT_TO_BRAILLE.get(c, "*")
                number_follows = True
            else:
                braille_result += cls.TEXT_TO_BRAILLE.get(c, "*")

        return braille_result

    @classmethod
    def braille_to_text(cls, braille: str) -> str:
        text_result: str = ""
        capital_follows, number_follows = False, False

        for i in range(0, len(braille), 6):
            braille_char = braille[i : i + 6]
            text_char: str = cls.BRAILLE_TO_TEXT.get(braille_char, "*")

            # Handle special cases (capital_follows and number_follows)
            if text_char == "capital_follows":
                capital_follows = True
                continue
            if text_char == "number_follows":
                number_follows = True
                continue

            # Handle space
            if text_char == " ":
                text_result += text_char
                # reset "number_follows" flag
                number_follows = False
                continue

            if text_char.isalpha():
                if capital_follows:
                    text_result += text_char.upper()
                    # reset "capital_follows" flag
                    capital_follows = False
                elif number_follows:
                    # (ord(text_char) - ord('a') + 1) % 10 will map the character to the corresponding number
                    # mod 10 to handle special case of j being equal to 0 in braille
                    text_result += str((ord(text_char) - ord("a") + 1) % 10)
                else:
                    text_result += text_char

        return text_result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage from CLI: python translator.py <text>")
        sys.exit(1)
    print(BrailleTranslator.translate(sys.argv[1:]))
