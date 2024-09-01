import sys

class Translator:
    def __init__(self):
        """
        Initializes the dictionaries for translation between English and Braille.
        """
        self.braille_alpha_dict = {
            "A": "O.....",
            "B": "O.O...",
            "C": "OO....",
            "D": "OO.O..",
            "E": "O..O..",
            "F": "OOO...",
            "G": "OOOO..",
            "H": "O.OO..",
            "I": ".OO...",
            "J": ".OOO..",
            "K": "O...O.",
            "L": "O.O.O.",
            "M": "OO..O.",
            "N": "OO.OO.",
            "O": "O..OO.",
            "P": "OOO.O.",
            "Q": "OOOOO.",
            "R": "O.OOO.",
            "S": ".OO.O.",
            "T": ".OOOO.",
            "U": "O...OO",
            "V": "O.O.OO",
            "W": ".OOO.O",
            "X": "OO..OO",
            "Y": "OO.OOO",
            "Z": "O..OOO",
        }
        self.braille_num_dict = {
            "1": "O.....",
            "2": "O.O...",
            "3": "OO....",
            "4": "OO.O..",
            "5": "O..O..",
            "6": "OOO...",
            "7": "OOOO..",
            "8": "O.OO..",
            "9": ".OO...",
            "0": ".OOO..",
        }
        self.braille_flag_dict = {
            "CAPITAL": ".....O",
            "DECIMAL": ".O...O",
            "NUMBER": ".O.OOO",
        }
        self.braille_symbol_dict = {
            ".": "..OO.O",
            ",": "..O..O",
            "?": "..O.OO",
            "!": "..OOO.",
            ":": "..OO..",
            ";": "..O.O.",
            "-": "....OO",
            "/": ".O..O.",
            "<": ".OO..O",
            ">": "O..OO.",
            "(": "O.O..O",
            ")": ".O.OO.",
            " ": "......",
        }

        # Create the reverse dictionaries for translation from Braille to English
        self.english_alpha_dict = {v: k for k, v in self.braille_alpha_dict.items()}
        self.english_num_dict = {v: k for k, v in self.braille_num_dict.items()}
        self.english_flag_dict = {v: k for k, v in self.braille_flag_dict.items()}
        self.english_symbol_dict = {v: k for k, v in self.braille_symbol_dict.items()}

    def translate(self, string):
        """
        Translates a string to Braille if it is in English, or to English if it is in Braille.

        :param string: The string to translate.
        :return: The translated string.
        """
        if self.is_braille(string):
            return self.braille_to_english(string)
        return self.english_to_braille(string)
    
    def is_braille(self, string):
        """
        Checks if a string is in Braille.

        :param string: The string to check.
        :return: True if the string is in Braille, False otherwise.
        """
        if len(string) % 6 == 0: # if the length of the string is a multiple of 6
            for c in string:
                if c != "O" and c != ".": # if the character is not a Braille dot
                    return False
            return True
        return False
    
    def english_to_braille(self, string):
        """
        Translates an English string to Braille.

        :param string: The English string to translate.
        :return: The translated Braille.
        """
        result = ""
        try:
            for i in range(len(string)):
                if ord("A") <= ord(string[i].upper()) <= ord("Z"): # if the character is a letter
                    if string[i].isupper(): # if the letter is uppercase
                        result += self.braille_flag_dict["CAPITAL"]
                    result += self.braille_alpha_dict[string[i].upper()]
                elif ord("0") <= ord(string[i]) <= ord("9"): # if the character is a number
                    # if the character is a number and is not preceded by a number or a decimal point
                    if i == 0 or (not string[i - 1].isdigit() and not (i > 1 and string[i - 2].isdigit() and string[i - 1] == ".")):
                        result += self.braille_flag_dict["NUMBER"]
                    result += self.braille_num_dict[string[i]]
                elif string[i] == ".": # if the character is a period or decimal point
                    # if the character is a period
                    if i == 0 or i == len(string) - 1 or not string[i - 1].isdigit() or not string[i + 1].isdigit():
                        result += self.braille_symbol_dict[string[i]]
                    else: # if the character is a decimal point
                        result += self.braille_flag_dict["DECIMAL"]
                elif string[i] in self.braille_symbol_dict: # if the character is a symbol
                    result += self.braille_symbol_dict[string[i]]
                else: # if the character is not a letter, number, period, or symbol
                    raise KeyError(string[i])
        except KeyError as e:
            return "" # return an empty string if the character is not recognized
        return result

    def braille_to_english(self, string):
        """
        Translates a Braille string to English.

        :param string: The Braille string to translate.
        :return: The translated English.
        """
        result = ""
        i = 0
        capital = False
        number = False
        try:
            while i < len(string):
                current = string[i:i + 6] # get the current Braille character
                if current in self.english_flag_dict: 
                    if self.english_flag_dict[current] == "CAPITAL": # if the next character is a capital letter
                        capital = True
                        number = False
                    elif self.english_flag_dict[current] == "NUMBER": # if the next character is a number
                        number = True
                    elif self.english_flag_dict[current] == "DECIMAL": # if the next character is a decimal point
                        result += "."
                elif capital: # if the current character is a capital letter
                    result += self.english_alpha_dict[current]
                    capital = False
                elif number: # if the current character is a number
                    if current in self.english_num_dict:
                        result += self.english_num_dict[current]
                    else:
                        result += self.english_symbol_dict[current]
                        number = False
                elif current in self.english_alpha_dict: # if the current character is a lowercase letter
                    result += self.english_alpha_dict[current].lower()
                    number = False
                elif current in self.english_symbol_dict: # if the current character is a symbol
                    result += self.english_symbol_dict[current]
                    number = False
                else: # if the current character is not recognized
                    raise KeyError(current)
                i += 6 # move to the next Braille character
        except KeyError as e:
            return "" # return an empty string if the character is not recognized
        return result
    
if __name__ == '__main__':
    translator = Translator()
    print(translator.translate(" ".join(sys.argv[1:])))