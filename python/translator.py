import sys
from unittest import addModuleCleanup


class BrailleTranslator:
    BRAILLE_TO_LETTER = {
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
        "......": " ",
    }

    LETTER_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_LETTER.items()}

    BRAILLE_TO_NUM = {
        "O.....": "1",
        "O.O...": "2",
        "OO....": "3",
        "OO.O..": "4",
        "O..O..": "5",
        "OOO...": "6",
        "OOOO..": "7",
        "O.OO..": "8",
        ".OO...": "9",
        ".OOO..": "0",
        "......": " ",
    }

    NUM_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_NUM.items()}

    CAPITAL_FOLLOWS = ".....O"
    NUMBER_FOLLOWS = ".O.OOO"

    SPACE = "......"

    def _split_braille_into_words(self, line: str) -> list[str]:
        split_string = [line[i : i + 6] for i in range(0, len(line), 6)]
        return split_string

    def _translate_braille_to_english(self, words: str) -> str:
        translated = f""

        split_words = self._split_braille_into_words(words)

        reading_numbers = False
        capital = False
        for word in split_words:
            if word == self.NUMBER_FOLLOWS:
                reading_numbers = True
                continue
            elif word == self.CAPITAL_FOLLOWS:
                capital = True
                continue
            elif capital:
                translated += self.BRAILLE_TO_LETTER[word].upper()
                capital = False
            elif reading_numbers:
                if word == self.SPACE:
                    reading_numbers = False
                    translated += " "
                else:
                    translated += self.BRAILLE_TO_NUM[word]
            else:
                translated += self.BRAILLE_TO_LETTER[word]

        return translated

    def _translate_english_to_braille(self, words: str) -> str:
        translate = f""

        split_letter = list(words)

        inputting_numbers = False
        for letter in split_letter:
            if inputting_numbers:
                if letter.isalpha():
                    inputting_numbers = False
                else:
                    translate += self.NUM_TO_BRAILLE[letter]

            if not inputting_numbers:
                if letter.islower() or letter == " ":
                    translate += self.LETTER_TO_BRAILLE[letter]
                elif letter.isupper():
                    translate += self.CAPITAL_FOLLOWS
                    translate += self.LETTER_TO_BRAILLE[letter.lower()]
                elif letter.isnumeric():
                    translate += self.NUMBER_FOLLOWS
                    translate += self.NUM_TO_BRAILLE[letter]
                    inputting_numbers = True

        return translate

    def translate(self, sentence: str) -> str:
        if set(sentence).issubset({"O", "."}) and len(sentence) % 6 == 0:
            return self._translate_braille_to_english(sentence)
        else:
            return self._translate_english_to_braille(sentence)



def main():
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:]).strip()
    else:
        sys.exit(1)

    translator = BrailleTranslator()
    print(translator.translate(sentence), file=sys.stdout)

if __name__ == "__main__":
    main()  
