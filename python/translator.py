import sys
import json
import re


class translator:
    def __init__(self, translation_table: dict) -> None:
        """Initializes the translator with the provided translation table.

        Args:
            translation_table (dict): A dictionary containing mappings for alphabets, numbers,
            and special characters to their corresponding Braille representations.
        """
        self.alpha2braille = translation_table["alpha2braille"]
        self.num2braille = translation_table["num2braille"]
        self.specialchars2braille = translation_table["special chars"]

        flipdict = lambda dict2flip: {v: k for k, v in dict2flip.items()}

        self.braille2alpha = flipdict(self.alpha2braille)
        self.braille2num = flipdict(self.num2braille)
        self.braille2specialchars = flipdict(self.specialchars2braille)

    def checktext_valid(self, test_string: str) -> bool:
        """Checks if the input text string contains valid characters (alphabets, numbers, and common punctuation).

        Args:
            test_string (str): The input string to validate.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        valid_char_patten = re.compile(r"^[a-zA-Z0-9 ,.?!;:/<>()]")
        return bool(valid_char_patten.match(test_string))

    def checkbraille_valid(self, test_string: str) -> bool:
        """Checks if the input string contains only valid Braille characters (O or .)

        Args:
            test_string (str): The input string to validate.

        Returns:
            bool: True if the string is valid Braille, False otherwise.
        """
        braille_characters = {"O", "."}
        return set(test_string).issubset(braille_characters)

    def alphanum2braille(self, text_string: str) -> str:
        """Converts an alphanumeric text string to its corresponding Braille representation.

        Args:
            text_string (str): The alphanumeric string to be converted.

        Returns:
            str: The Braille representation of the input string.
        """
        translated_txt = []
        numeric_sequence = False

        for char in text_string:

            if char.isspace():
                translated_txt.append(self.specialchars2braille.get("space", ""))
                numeric_sequence = False

            elif char.isalpha():
                if char.isupper():
                    translated_txt.append(
                        self.specialchars2braille.get("capital follows", "")
                    )
                translated_txt.append(self.alpha2braille.get(char.lower(), ""))

            elif char.isnumeric():

                if not (numeric_sequence):
                    translated_txt.append(
                        self.specialchars2braille.get("number follows")
                    )
                    numeric_sequence = True

                translated_txt.append(self.num2braille.get(char, ""))

            elif char == ".":
                if numeric_sequence:
                    translated_txt.append(
                        self.specialchars2braille.get("decimal follows", "")
                    )
                translated_txt.append(self.specialchars2braille.get(".", ""))

            elif char in self.specialchars2braille:
                translated_txt.append(self.specialchars2braille.get(char, ""))

            else:
                translated_txt.append("")

        return "".join(translated_txt)

    def braille2alphanum(self, braille_string: str) -> str:
        """Converts a Braille string to its corresponding alphanumeric representation.

        Args:
            braille_string (str): The Braille string to be converted.

        Returns:
            str: The alphanumeric representation of the input Braille string.
        """

        translated_txt = []
        bstring_length = len(braille_string)
        idx_braille = 0
        numeric_sequence = False

        while idx_braille < bstring_length:
            try:
                bchar = braille_string[idx_braille : idx_braille + 6]

                if bchar == self.specialchars2braille.get("space", ""):
                    translated_txt.append(" ")
                    numeric_sequence = False

                elif not numeric_sequence:

                    if bchar == self.specialchars2braille.get("number follows", ""):
                        numeric_sequence = True

                    elif bchar == self.specialchars2braille.get("capital follows", ""):
                        if idx_braille + 12 <= bstring_length:
                            next_bchar = braille_string[
                                idx_braille + 6 : idx_braille + 12
                            ]
                            translated_txt.append(
                                self.braille2alpha.get(next_bchar, "").upper()
                            )
                            idx_braille += 6
                        else:
                            translated_txt.append(
                                ""
                            )  # no char or incomplete char after 'capital follows' char

                    elif bchar in self.braille2alpha:
                        translated_txt.append(self.braille2alpha.get(bchar, ""))

                    elif bchar in self.braille2specialchars:
                        translated_txt.append(self.braille2specialchars.get(bchar, ""))

                    else:

                        translated_txt.append(
                            ""
                        )  # invalid chars outside of non-numeric sequence

                elif numeric_sequence:
                    if bchar == self.specialchars2braille.get("decimal follows", ""):

                        if idx_braille + 12 <= bstring_length:

                            next_bchar = braille_string[
                                idx_braille + 6 : idx_braille + 12
                            ]
                            if self.braille2specialchars.get(next_bchar, "") == ".":
                                translated_txt.append(".")
                                idx_braille += 6
                        else:

                            translated_txt.append(
                                ""
                            )  # no decimal char after 'decimal follows' char

                    else:
                        translated_txt.append(self.braille2num.get(bchar, ""))

                else:
                    translated_txt.append("")  # unrecognized char

                idx_braille += 6
            except Exception as e:
                print(f"Error processing braille at index {idx_braille}: {e}")
                translated_txt.append("")
                idx_braille += 6

        return "".join(translated_txt)

    def translate(self, input_string: str) -> str:
        """Translates an input string between alphanumeric and Braille representations based on its content.

        Args:
            input_string (str): The string to be translated, either in alphanumeric or Braille format.

        Raises:
            ValueError: If the input string is neither valid Braille nor valid alphanumeric text.

        Returns:
            str: The translated string in the target format (Braille or alphanumeric).
        """

        if self.checkbraille_valid(input_string):
            return self.braille2alphanum(input_string)

        elif self.checktext_valid(input_string):
            return self.alphanum2braille(input_string)

        else:
            raise ValueError(
                "Inputs are not valid braille (O or .) or valid text characters."
            )


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 translator <strings to translate>")
        sys.exit(1)

    else:
        input_string = " ".join(sys.argv[1::])

        if input_string == "":
            raise ValueError("Empty string provided to translator.")
        else:

            # load translation table json to dictionary
            with open("translation_table.json", "r") as file:
                translation_table = json.load(file)

            # initialize translator
            translator = translator(translation_table)

            # translate text and print output to console
            try:
                translated_output = translator.translate(input_string)
                print(translated_output)
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(1)
            except Exception as e:
                print(f"Unexpected error: {e}")
                sys.exit(1)