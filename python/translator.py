import sys

# hashmap for eng -> braille
alphabets_chars_to_braille = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
    ".": "..OO.O",
    ",": "..O...",
    " ": "......",

    # NOT NEEDED FOR NOW
    # "?": "..O.OO",
    # "!": "..OOO.",
    # ":": "..OO..",
    # ";": "..O.O.",
    # "-": "....OO",
    # "/": ".O..O.",
    # "<": ".OO..O",
    # ">": "O..OO.",
    # "(": "O.O..O",
    # ")": ".O.OO.",
}

numbers_to_braille = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
}

# hashmap for braille -> eng
braille_to_alphabets = {v: k for k, v in alphabets_chars_to_braille.items()}
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}
braille_commands = {
    ".....O": "capital",
    ".O...O": "decimal",
    ".O.OOO": "number",
}


class BrailleEnglishTranslator:

    BRAILLE_MAX_LENGTH = 6

    def __init__(self, input_string: str):
        self.input_string = input_string

    def is_valid_braille(self) -> bool:
        return all(char in "O." for char in self.input_string)

    def braille_to_english(self) -> str:
        translation = []
        capital_flag = False
        number_flag = False
        
        for i in range(0, len(self.input_string), self.BRAILLE_MAX_LENGTH):
            char = self.input_string[i : i + self.BRAILLE_MAX_LENGTH]
            if char in braille_commands:
                command = braille_commands[char]
                if command == "capital":
                    capital_flag = True
                elif command == "number":
                    number_flag = True
                continue

            if braille_to_alphabets[char] == " ":
                number_flag = False
            if number_flag:
                translation.append(braille_to_numbers[char])
            elif char in braille_to_alphabets:
                if capital_flag:
                    translation.append(braille_to_alphabets[char].upper())
                    capital_flag = False
                else:
                    translation.append(braille_to_alphabets[char])

        return "".join(translation)

    def english_to_braille(self) -> str:
        translation = []
        number_flag = False

        for char in self.input_string:
            if char.isdigit():
                if not number_flag:
                    translation.append(alphabets_chars_to_braille["number"])
                    number_flag = True
                translation.append(numbers_to_braille[char])
            elif char.isalpha():
                if char.isupper():
                    translation.append(alphabets_chars_to_braille["capital"])
                translation.append(alphabets_chars_to_braille[char.lower()])
            elif char == " ":
                number_flag = False
                translation.append(alphabets_chars_to_braille[char])

        return "".join(translation)
    
    def translate(self) -> str:
        if self.is_valid_braille():
            return self.braille_to_english()
        else:
            return self.english_to_braille()


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        return

    input_string = " ".join(sys.argv[1:])
    res = BrailleEnglishTranslator(input_string)
    print(res.translate())


if __name__ == "__main__":
    main()
