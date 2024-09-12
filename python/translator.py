import sys

class Translator:


    ENGLISH_BRAILLE_DICT = {"a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", 
                            "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", 
                            "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO", "capital": ".....O", "decimal": ".O...O", "number": ".O.OOO", ".": "..OO.O", ",": "..O...", "?": "..O.OO", 
                            "!": "..OOO.", ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.", " ": "......"}

    NUMBER_BRAILLE_DICT = {"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..", " ": "......"}

    BRAILLE_NUMBER_DICT = {v: k for k, v in NUMBER_BRAILLE_DICT.items()}

    BRAILLE_ENGLISH_DICT = {v: k for k, v in ENGLISH_BRAILLE_DICT.items()}


    def is_braille(s: str) -> bool:
        '''
        Check if a string is braille or english

        Args:
            s: string
        
        Returns:
            True if the string is braille, False otherwise
        '''
        for i in s:
            if i not in ['.', 'O']:
                return False
        return True


    def braile_to_english(s: str) -> str:
        '''
        Translate braille to english

        Args:
            s: string
        
        Returns:
            English translation of the braille string
        '''

        if len(s) % 6 != 0:
            raise ValueError("Braille string length should be a multiple of 6")

        result = ""
        Capital = False
        Number = False
        for i in range(0, len(s), 6):
            letter = s[i:i+6]
            if letter not in Translator.BRAILLE_ENGLISH_DICT:
                raise ValueError(f"Braille pattern does not exist: {letter}")
            if letter in Translator.BRAILLE_ENGLISH_DICT:
                if Translator.BRAILLE_ENGLISH_DICT[letter] == "capital":
                    Capital = True
                    continue
                elif Translator.BRAILLE_ENGLISH_DICT[letter] == "number":
                    Number = True
                    continue
                if Capital:
                    result += Translator.BRAILLE_ENGLISH_DICT[letter].upper()
                    Capital = False
                elif Number and Translator.BRAILLE_ENGLISH_DICT[letter] == " ":
                    result += Translator.BRAILLE_ENGLISH_DICT[letter]
                    Number = False
                elif Number:
                    result += Translator.BRAILLE_NUMBER_DICT[letter]
                else:
                    if letter not in Translator.BRAILLE_ENGLISH_DICT:
                        raise ValueError(f"Unrecognized character in input: {letter}")
                    result += Translator.BRAILLE_ENGLISH_DICT[letter]
        
        return result

    def english_to_braille(s: str) -> str:
        '''
        Translate english to braille

        Args:
            s: string

        Returns:
            Braille translation of the english string
        '''
        result = ""
        number = False
        for i in s:
            if i.isupper():
                result += Translator.ENGLISH_BRAILLE_DICT["capital"]
                result += Translator.ENGLISH_BRAILLE_DICT[i.lower()]
            elif i.isdigit():
                if not number:
                    result += Translator.ENGLISH_BRAILLE_DICT["number"]
                    number = True
                result += Translator.NUMBER_BRAILLE_DICT[i]
            elif i == " ":
                result += Translator.ENGLISH_BRAILLE_DICT[i]
                number = False
            else:
                result += Translator.ENGLISH_BRAILLE_DICT[i]

        return result

# Test cases
# print(braile_to_english(".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.."))
# print(english_to_braille("Hello world") == ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")

def main():
    if len(sys.argv) < 2:
        print("Provide an input text in English or Braille to translate")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    # print(input_text)

    if Translator.is_braille(input_text):
        print(Translator.braile_to_english(input_text))
    else:
        print(Translator.english_to_braille(input_text))


if __name__ == '__main__':
    main()

