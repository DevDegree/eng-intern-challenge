import sys
import re

class Translator():
    # english characters to braille mapping
    __ENGLISH_TO_BRAILLE_ALPHABETS = {
        "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
        "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
        "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
        "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
        "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
        "z": "O..OOO",
    }
    __ENGLISH_TO_BRAILLE_NUMBERS = {
        "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
        "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    }
    __ENGLISH_TO_BRAILLE_CHARS = {
        ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
        ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O", ">": "O..OO.",
        "(": "O.O..O", ")": ".O.OO.", " ": "......"
    }
    __ENGLISH_SPECIAL_MAPPINGS = {
        "CAPITAL_FOLLOWS": ".....O", "NUMBER_FOLLOWS": ".O.OOO"
    }
    # braille to characters mapping
    __BRAILLE_TO_ENGLISH_ALPHABETS = {v: k for k, v in __ENGLISH_TO_BRAILLE_ALPHABETS.items()}
    __BRAILLE_TO_ENGLISH_NUMBERS = {v: k for k, v in __ENGLISH_TO_BRAILLE_NUMBERS.items()}
    __BRAILLE_TO_ENGLISH_CHARS = {v: k for k, v in __ENGLISH_TO_BRAILLE_CHARS.items()}
    __BRAILE_SPECIAL_MAPPINGS = {v: k for k, v in __ENGLISH_SPECIAL_MAPPINGS.items()}
    @staticmethod
    def __isBraille(string: str) -> bool:
        """
        Private function to determine if a given string is Braille or not
        Args: the string to translate
        Return: boolean value, True indicating the string is Braille, False for not
        """
        # braille shouldn't have spaces, the length should be divisible by 6, and should only contain "." and "O" (sol'n will account for the case for only "."'s, all spaces)
        if re.fullmatch(r'[O\.]+', string) and ' ' not in string and len(string) % 6 == 0:
            return True
        
        return False
    
    @staticmethod
    def __braileToEnglish(string: str) -> str:
        """
        Private function that converts a braille string to english
        Args: the string to translate
        Return: the english translated string
        """
        try:
            next_is_capital = False
            next_is_number = False
            translatedString = ""
            # use sliding window approach and iterate through 6's
            for index in range(0, len(string), 6):
                window = string[index:index+6]
                # if it's a special mapping to handle one of the "follows" conversions
                if window in Translator.__BRAILE_SPECIAL_MAPPINGS:
                    if Translator.__BRAILE_SPECIAL_MAPPINGS[window] == "CAPITAL_FOLLOWS":
                        next_is_capital = True
                    elif Translator.__BRAILE_SPECIAL_MAPPINGS[window] == "NUMBER_FOLLOWS":
                        next_is_number = True
                
                # it's a space
                elif window == "......":
                    translatedString += Translator.__BRAILLE_TO_ENGLISH_CHARS[window]
                    # space will stop any number follows being read
                    next_is_number = False
                # current letter should be a capital letter
                elif next_is_capital:
                    translatedString += Translator.__BRAILLE_TO_ENGLISH_ALPHABETS[window].upper()
                    next_is_capital = False
                # it's a number
                elif next_is_number:
                    translatedString += Translator.__BRAILLE_TO_ENGLISH_NUMBERS[window]
                # it's some other character
                # note: the only overlapping symbol character and letter character is ">" and "o", we'll prioritize outputting o
                else:
                    if window in Translator.__BRAILLE_TO_ENGLISH_ALPHABETS:
                        translatedString += Translator.__BRAILLE_TO_ENGLISH_ALPHABETS[window]
                    elif window in Translator.__BRAILLE_TO_ENGLISH_CHARS:
                        translatedString += Translator.__BRAILLE_TO_ENGLISH_CHARS[window]
            return translatedString
        except Exception as error:
            # return an error message or empty string
            return f"{error}" 
    @staticmethod
    def __englishToBraille(string: str) -> str:
        """
        Private function that converts an english string to braille
        Args: the string to translate
        Return: the braille translated string
        """
        try:
            translatedString = ""
            isNumber = False
            for c in string:
                # if it's an upper case letter
                if c.isupper():
                    # in case we have an input like "123Abc", give a braille output that maps to "123 abc"
                    # add a space in case the input doesn't account for the space after the number
                    if isNumber:
                        translatedString += Translator.__ENGLISH_TO_BRAILLE_CHARS[" "]
                        isNumber = False
                    translatedString += Translator.__ENGLISH_SPECIAL_MAPPINGS["CAPITAL_FOLLOWS"]
                    translatedString += Translator.__ENGLISH_TO_BRAILLE_ALPHABETS[c.lower()]
                
                # if it's a number
                elif c.isnumeric():
                    if not isNumber:
                        translatedString += Translator.__ENGLISH_SPECIAL_MAPPINGS["NUMBER_FOLLOWS"]
                        translatedString += Translator.__ENGLISH_TO_BRAILLE_NUMBERS[c]
                        isNumber = True
                    else:
                        translatedString += Translator.__ENGLISH_TO_BRAILLE_NUMBERS[c]
                
                # it's some other character, either special char or lower case
                else:
                    if c in Translator.__ENGLISH_TO_BRAILLE_ALPHABETS:
                        # in case we have an input like "123abc", give a braille output that maps to "123 abc"
                        # add a space in case the input doesn't account for the space after the number
                        if isNumber:
                            translatedString += Translator.__ENGLISH_TO_BRAILLE_CHARS[" "]
                            isNumber = False
                        translatedString += Translator.__ENGLISH_TO_BRAILLE_ALPHABETS[c]
                    elif c in Translator.__ENGLISH_TO_BRAILLE_CHARS:
                        translatedString += Translator.__ENGLISH_TO_BRAILLE_CHARS[c]
                        # space will stop any number follows being read
                        if c == " ":
                            isNumber = False
            return translatedString
        
        except Exception as error:
            print('error')
            return f"{str(error)}"
    @staticmethod
    def translate(joined_args: str) -> str:
        """
        Central function that handles translating a given string and returning the translated string
        Args: the string provided in the arguments of the file during runtime
        Return: the translated string
        """
        if Translator.__isBraille(joined_args):
            return Translator.__braileToEnglish(joined_args)
        
        return Translator.__englishToBraille(joined_args)
def main():
    argv = sys.argv[1:]
    if argv:
        translated_string = Translator.translate(" ".join(argv))
        print(translated_string)
    else:
        print("No arguments provided")
    
if __name__ == "__main__":
    main()
