import sys  # get args from command line

# solution reasoning
# Use a dict to map from braille to english and vice versa as well as the numbers
# use flags to indicate capital, and number mode
# loop over input

class BrailleTranslator:
    def __init__(self):
        self.is_number_mode = False
        self.braille_to_english_mapping = {
            'O.....': 'A', 'O.O...': 'B', 'OO....': 'C', 'OO.O..': 'D', 'O..O..': 'E',
            'OOO...': 'F', 'OOOO..': 'G', 'O.OO..': 'H', '.OO...': 'I', '.OOO..': 'J',
            'O...O.': 'K', 'O.O.O.': 'L', 'OO..O.': 'M', 'OO.OO.': 'N', 'O..OO.': 'O',
            'OOO.O.': 'P', 'OOOOO.': 'Q', 'O.OOO.': 'R', '.OO.O.': 'S', '.OOOO.': 'T',
            'O...OO': 'U', 'O.O.OO': 'V', '.OOO.O': 'W', 'OO..OO': 'X', 'OO.OOO': 'Y',
            'O..OOO': 'Z', '......': ' ', '.....O': 'capital_follows', '.O.OOO': 'number_follows'
        }

        self.english_to_braille_mapping = {v: k for k, v in self.braille_to_english_mapping.items()}
        self.letter_to_number = {
            'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
            'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
        }
        self.number_to_letter = {v: k for k, v in self.letter_to_number.items()}

    def braille_to_english(self, input_string: str) -> str:
        english_string = []
        i = 0
        capital_next = False

        while i < len(input_string):
            braille_char = input_string[i:i+6]
            # check for special cases first: capital next, number follows and space
            if braille_char == '.....O':
                capital_next = True
            elif braille_char == '.O.OOO':
                self.is_number_mode = True
            elif braille_char == '......':
                english_string.append(' ')
                self.is_number_mode = False
            else:
                c = self.braille_to_english_mapping[braille_char]
                if self.is_number_mode:
                    english_string.append(self.letter_to_number[c])
                else:  # character is alpha
                    if not capital_next:
                        c = c.lower()
                    english_string.append(c)
                    capital_next = False
                    self.is_number_mode = False
            i += 6

        return "".join(english_string)

    def english_to_braille(self, input_string: str) -> str:
        braille_string = []
        for c in input_string:
            if c.isalpha():
                if self.is_number_mode:  # was number mode, clear it
                    braille_string.append(self.english_to_braille_mapping[' '])
                    self.is_number_mode = False
                if c.isupper():
                    braille_string.append(self.english_to_braille_mapping["capital_follows"])
                braille_string.append(self.english_to_braille_mapping[c.upper()])
            elif c.isdigit():
                if not self.is_number_mode:
                    braille_string.append(self.english_to_braille_mapping["number_follows"])
                    self.is_number_mode = True
                braille_string.append(self.english_to_braille_mapping[self.number_to_letter[c]])
            elif c == ' ':
                self.is_number_mode = False  # reset number mode
                braille_string.append('......')
        return "".join(braille_string)
            


    def translate(self, input_string: str) -> str:
        # input_string must be braille if only contains '.' and/or 'O'
        if set(input_string).issubset({'.', 'O'}):
            return self.braille_to_english(input_string)
        else:
            # is english text
            return self.english_to_braille(input_string)

if __name__ == "__main__":
    translator = BrailleTranslator()
    if len(sys.argv) > 1:
        # join all arguments to form sentence
        input_string = ' '.join(sys.argv[1:])
        print(translator.translate(input_string))
    else:
        print("Nothing to translate! Please provide at least 1 string.")
