import sys


class Translator:
    capital_braille = ".....O"
    decimal_braille = ".O...O"
    numeric_braille = ".O.OOO"
    braille_text_pairs = [
        ["a", "O....."],
        ["b", "O.O..."],
        ["c", "OO...."],
        ["d", "OO.O.."],
        ["e", "O..O.."],
        ["f", "OOO..."],
        ["g", "OOOO.."],
        ["h", "O.OO.."],
        ["i", ".OO..."],
        ["j", ".OOO.."],
        ["k", "O...O."],
        ["l", "O.O.O."],
        ["m", "OO..O."],
        ["n", "OO.OO."],
        ["o", "O..OO."],
        ["p", "OOO.O."],
        ["q", "OOOOO."],
        ["r", "O.OOO."],
        ["s", ".OO.O."],
        ["t", ".OOOO."],
        ["u", "O...OO"],
        ["v", "O.O.OO"],
        ["w", ".OOO.O"],
        ["x", "OO..OO"],
        ["y", "OO.OOO"],
        ["z", "O..OOO"],
        ["1", "O....."],
        ["2", "O.O..."],
        ["3", "OO...."],
        ["4", "OO.O.."],
        ["5", "O..O.."],
        ["6", "OOO..."],
        ["7", "OOOO.."],
        ["8", "O.OO.."],
        ["9", ".OO..."],
        ["0", ".OOO.."],
        [".", "..OO.O"],
        [",", "..O..."],
        ["?", "..O.OO"],
        ["!", "..OOO."],
        [":", "..OO.."],
        [";", "..O.O."],
        ["-", "....OO"],
        ["/", ".O..O."],
        ["<", ".OO..O"],
        # [">", "O..OO."], Removed since it is the same braille as o
        ["(", "O.O..O"],
        [")", ".O.OO."],
        [" ", "......"],
    ]

    text_to_braille_dict = {}
    braille_to_text_dict = {}
    braille_to_number_dict = {}

    def translate(self):
        string = self.get_input_string()
        is_braille = self.check_if_braille(runtime_argument=string)

        self.setup_text_to_braille_dict()
        self.setup_braille_to_text_dict()

        output_string = ""
        if is_braille:
            output_string = self.convert_from_braille(string=string)
        else:
            output_string = self.convert_to_braille(string=string)

        self.output(string=output_string)

    def get_input_string(self):
        """
        Takes the runtime arguments and returns the string to be translated
        """

        input_string = ""
        argc = len(sys.argv)

        if argc > 1:
            for i in range(1, argc - 1):
                input_string += sys.argv[i] + " "

            input_string += sys.argv[-1]

        return input_string

    def setup_text_to_braille_dict(self):
        """
        Takes the braille-text pairs provided in the braille_text_pairs array and reformats the data
        into a dictionary for constant time lookup later in the code.
        """

        for letter, braille in self.braille_text_pairs:
            self.text_to_braille_dict[letter] = braille
            if letter.isalpha():
                self.text_to_braille_dict[letter.upper()] = (
                    self.capital_braille + braille
                )

    def setup_braille_to_text_dict(self):
        """
        Takes the braille-text pairs provided in the braille_text_pairs array and reformats the data
        into a dictionary for constant time lookup later in the code.
        """

        for letter, braille in self.braille_text_pairs:
            if letter.isnumeric():
                self.braille_to_number_dict[braille] = letter
            else:
                self.braille_to_text_dict[braille] = letter

    def check_if_braille(self, runtime_argument: str = None):
        """
        Takes the runtime argument as the input string and returns True if the string is braille.
        Otherwise the function will return False indicating it must be translated into braille.
        """

        # Checks if the string is exclusively consists of braille characters
        for character in runtime_argument:
            if character not in ["O", "."]:
                return False

        # Checks if the braille string is a multiple of 6 as should be expected of braille strings.
        return len(runtime_argument) % 6 == 0

    def convert_from_braille(self, string: str = None):
        """
        Takes a braille text and returns the non braille translation.
        """

        tokens = [string[i : i + 6] for i in range(0, len(string), 6)]
        numeric_flag = False
        capital_flag = False
        return_string = ""

        for token in tokens:
            if token == self.numeric_braille:
                numeric_flag = True
                continue
            if token == self.capital_braille:
                capital_flag = True
                continue
            if token == self.text_to_braille_dict[" "]:
                numeric_flag = False

            if capital_flag:
                return_string += chr(ord(self.braille_to_text_dict[token]) - 32)
                capital_flag = False
                continue

            if numeric_flag:
                return_string += self.braille_to_number_dict[token]
                continue

            return_string += self.braille_to_text_dict[token]

        return return_string

    def convert_to_braille(self, string: str = None):
        """
        Takes a non braille text and returns the braille translation.
        """

        return_string = ""
        numeric_flag = False

        for i in range(len(string)):
            character = string[i]
            if (
                self.text_to_braille_dict[character] == self.text_to_braille_dict["."]
                and i > 0
            ):
                if string[i - 1].isnumeric():
                    return_string += self.decimal_braille
                else:
                    return_string += self.text_to_braille_dict["."]
            else:
                if character.isnumeric() and not numeric_flag:
                    numeric_flag = True
                    return_string += self.numeric_braille

                if character == " " and numeric_flag:
                    numeric_flag = False

                return_string += self.text_to_braille_dict[character]

        return return_string

    def output(self, string: str = None):
        """
        Outputs the translated string. In this case to standard output.
        """

        print(string)


if __name__ == "__main__":
    Translator().translate()
