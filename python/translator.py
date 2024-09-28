
class Translator:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    NUMBERS = "1234567890"

    BRAILLE_LETTERS = {
        'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
        'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
        'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
        'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
        'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
        'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
        'y': "OO.OOO", 'z': "O..OOO"
    }

    BRAILLE_NUMBERS = {
        '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
        '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
        '9': ".OO...", '0': ".OOO.."
    }

    SPACE_BRAILLE = "......"
    NUMBER_BRAILLE = ".O.OOO"
    UPPERCASE_BRAILLE = ".....O"

    # Reverse mappings so i can translate back to english
    BRAILLE_LETTERS_REVERSE = {v: k for k, v in BRAILLE_LETTERS.items()}
    BRAILLE_NUMBERS_REVERSE = {v: k for k, v in BRAILLE_NUMBERS.items()}

    def isBraille(self, text: str) -> bool:
        return "." in text

    def english_to_braille(self, englishText: str) -> str:
        toReturn = ""
        putNumberMark = True  # to reset number mode after space
        # Tracks previous character type: 'number', 'letter', or 'space'
        previousCharType = None

        for char in englishText:
            if char.isupper():
                toReturn += self.UPPERCASE_BRAILLE
                char = char.lower()

            if char.isnumeric():
                if putNumberMark:
                    toReturn += self.NUMBER_BRAILLE
                    putNumberMark = False
                brailleChar = self.BRAILLE_NUMBERS.get(char)
                if brailleChar:
                    toReturn += brailleChar
                else:
                    raise ValueError(f"invalid number: {char}")
                previousCharType = 'number'
            elif char.isspace():
                putNumberMark = True
                toReturn += self.SPACE_BRAILLE
                previousCharType = 'space'
            elif char.isalpha():
                # if prev character was a number, add a space to exit number mode
                if previousCharType == 'number':
                    toReturn += self.SPACE_BRAILLE
                    putNumberMark = True
                brailleChar = self.BRAILLE_LETTERS.get(char)
                if brailleChar:
                    toReturn += brailleChar
                else:
                    raise ValueError(f"invalid letter: {char}")
                previousCharType = 'letter'
            else:
                raise ValueError(f"invalid letter: {char}")

        # put space at the end if the last character was a number
        if previousCharType == 'number':
            toReturn += self.SPACE_BRAILLE

        return toReturn

    def braille_to_english(self, brailleText: str) -> str:
        toReturn = ""
        seenNumber = False
        capitalized = False

        i = 0
        while i < len(brailleText):
            brailleLetterString = brailleText[i:i + 6]

            if brailleLetterString == self.UPPERCASE_BRAILLE:
                capitalized = True
                i += 6
                continue

            if brailleLetterString == self.SPACE_BRAILLE:
                if seenNumber:
                    # Exiting number mode without adding a space
                    seenNumber = False
                else:
                    # It's an actual space between words
                    toReturn += " "
                i += 6
                continue

            if brailleLetterString == self.NUMBER_BRAILLE:
                seenNumber = True
                i += 6
                continue

            if seenNumber:
                # Numbers share the same Braille patterns as letters a-j
                number = self.BRAILLE_NUMBERS_REVERSE.get(brailleLetterString)
                if number:
                    toReturn += number
                else:
                    # if not a number, exit number mode and treat as letter
                    seenNumber = False
                    letter = self.BRAILLE_LETTERS_REVERSE.get(
                        brailleLetterString)
                    if letter:
                        if capitalized:
                            toReturn += letter.upper()
                            capitalized = False
                        else:
                            toReturn += letter
                    else:
                        raise ValueError(
                            f"invalid braille: {brailleLetterString}")
            else:
                letter = self.BRAILLE_LETTERS_REVERSE.get(brailleLetterString)
                if letter:
                    if capitalized:
                        toReturn += letter.upper()
                        capitalized = False
                    else:
                        toReturn += letter
                else:
                    raise ValueError(
                        f"invalid braille: {brailleLetterString}")

            i += 6

        return toReturn


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("please input valid text to translate")
        sys.exit(1)

    inputText = " ".join(sys.argv[1:])
    translator = Translator()

    try:
        if translator.isBraille(inputText):
            output = translator.braille_to_english(inputText)
        else:
            output = translator.english_to_braille(inputText)
        print(output)
    except ValueError as e:
        print(f"Error, {e}")
        sys.exit(1)
