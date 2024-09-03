import sys


class Translator:
    ALPHANUM_ENG_TO_BRAILLE_MAP = {
        "a": "0.....",
        "b": "0.0...",
        "c": "00....",
        "d": "00.0..",
        "e": "0..0..",
        "f": "000...",
        "g": "0000..",
        "h": "0.00..",
        "i": ".00...",
        "j": ".000..",
        "k": "0...0.",
        "l": "0.0.0.",
        "m": "00..0.",
        "n": "00.00.",
        "o": "0..00.",
        "p": "000.0.",
        "q": "00000.",
        "r": "0.000.",
        "s": ".00.0.",
        "t": ".0000.",
        "u": "0...00",
        "v": "0.0.00",
        "w": ".000.0",
        "x": "00..00",
        "y": "00.000",
        "z": "0..000",
        "1": "0.....",
        "2": "0.0...",
        "3": "00....",
        "4": "00.0..",
        "5": "0..0..",
        "6": "000...",
        "7": "0000..",
        "8": "0.00..",
        "9": ".00...",
        "0": ".000..",
        " ": "......",
    }

    BRAILLE_CAPITALIZE_FOLLOWS = ".....0"
    BRAILLE_DECIMAL_FOLLOWS = ".0...0"
    BRAILLE_NUMBER_FOLLOWS = ".0.000"

    BRAILLE_SPACE = "......"

    def __init__(self) -> None:
        pass

    def is_braille(self, input_str: str) -> bool:
        return set(input_str) == set("0.")

    def translate(self, input_str: str) -> str:
        return (
            self.translate_braille_to_eng(input_str)
            if self.is_braille(input_str)
            else self.translate_eng_to_braille(input_str)
        )

    def translate_eng_to_braille(self, input_str: str) -> str:
        return input_str

    def translate_braille_to_eng(self, input_str: str) -> str:
        return input_str


def main():
    print(sys.argv[1:])


if __name__ == "__main__":
    main()
