import json
import sys

class BrailleTranslator:
    """
    A class to translate between English text and Braille.

    Attributes:
        braille_dict (dict): The Braille dictionary loaded from a JSON file.
        letters_dict (dict): Dictionary mapping letters to Braille patterns.
        numbers_dict (dict): Dictionary mapping numbers to Braille patterns.
        special_dict (dict): Dictionary mapping special characters to Braille patterns.
        reverse_letters_dict (dict): Dictionary mapping Braille patterns to letters.
        reverse_numbers_dict (dict): Dictionary mapping Braille patterns to numbers.
    """

    def __init__(self, file_path='braille_dictionary.json'):
        """
        Initializes the BrailleTranslator with the given Braille dictionary file.

        Args:
            file_path (str): The path to the Braille dictionary JSON file.
        """
        self.braille_dict = self.load_braille_dictionary(file_path)
        self.letters_dict = self.braille_dict['letters']
        self.numbers_dict = self.braille_dict['numbers']
        self.special_dict = self.braille_dict['special']
        self.reverse_letters_dict = {v: k for k, v in self.letters_dict.items()}
        self.reverse_numbers_dict = {v: k for k, v in self.numbers_dict.items()}

    def load_braille_dictionary(self, file_path):
        """
        Loads the Braille dictionary from a JSON file.

        Args:
            file_path (str): The path to the Braille dictionary JSON file.

        Returns:
            dict: The loaded Braille dictionary.

        Raises:
            FileNotFoundError: If the file is not found.
            JSONDecodeError: If the file is not a valid JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' is not a valid JSON file.")
            sys.exit(1)

    def english_to_braille(self, text):
        """
        Translates English text to Braille.

        Args:
            text (str): The English text to translate.

        Returns:
            str: The translated Braille string.
        """
        braille = []
        is_number = False

        for char in text:
            if char == ' ':
                braille.append(self.special_dict['space'])
                is_number = False
            elif char.isupper():
                braille.append(self.special_dict['cap'])
                braille.append(self.letters_dict[char.lower()])
                is_number = False
            elif char.isdigit():
                if not is_number:
                    braille.append(self.special_dict['num'])
                    is_number = True
                braille.append(self.numbers_dict[char])
            elif char.lower() in self.letters_dict:
                braille.append(self.letters_dict[char.lower()])
                is_number = False
            else:
                braille.append(char)  # Keep unrecognized characters as-is
                is_number = False

        return ''.join(braille)

    def braille_to_english(self, braille_string):
        """
        Translates Braille to English text.

        Args:
            braille_string (str): The Braille string to translate.

        Returns:
            str: The translated English text.
        """
        english = []
        i = 0
        is_cap = False
        is_num = False

        while i < len(braille_string):
            if braille_string[i:i + 6] == self.special_dict['space']:
                english.append(' ')
                is_cap = False
                is_num = False
                i += 6
                continue

            char = braille_string[i:i + 6]
            if char == self.special_dict['cap']:
                is_cap = True
                i += 6
                continue
            elif char == self.special_dict['num']:
                is_num = True
                i += 6
                continue
            elif is_num and char in self.reverse_numbers_dict:
                number = self.reverse_numbers_dict[char]
                english.append(number)
            elif char in self.reverse_letters_dict:
                letter = self.reverse_letters_dict[char]
                if is_cap:
                    letter = letter.upper()
                    is_cap = False
                english.append(letter)
                is_num = False  # Reset number mode when a letter is encountered
            else:
                english.append('?')  # Unrecognized Braille pattern
            i += 6

        return ''.join(english)

    def detect_and_translate(self, input_string):
        """
        Detects the input type (Braille or English) and translates accordingly.

        Args:
            input_string (str): The input string to translate.

        Returns:
            str: The translated string.
        """
        if all(c in "O. " for c in input_string):
            return self.braille_to_english(input_string)
        else:
            return self.english_to_braille(input_string)

def main():
    """
    Main function to handle command-line input and perform translation.
    """
    translator = BrailleTranslator(file_path='braille_dictionary.json')
    if len(sys.argv) > 1:
        input_string = " ".join(sys.argv[1:])
        translated_output = translator.detect_and_translate(input_string)
        print(translated_output)
    else:
        print("Please provide a string to translate.")

if __name__ == "__main__":
    main()
