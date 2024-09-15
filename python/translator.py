import string
import sys
import re


class Translator():
    braille_alpha_dict = {
        # dictionary with alphabets, indicators and special characters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',

        # Special Braille symbols
        'capital': '.....O',  # Indicates that the next letter should be capitalized
        'number': '.O.OOO',  # Indicates that the following characters are numbers
        'decimal': '.O...O',  # Indicates that the following characters are decimal
        'space': '......',  # Space
        ',': '..O...',  # Comma
        '.': '..OO.O',  # Period
        '?': '..OOO.',  # Question mark
        '!': '..OOO',  # Exclamation mark
        ':': '..OO..',  # Colon
        ';': '..O.O.',  # Semicolon
        '-': '..O.O.',  # Dash
        '/': '.O...O',  # Slash
        '<': 'O.OO.O',  # Greater than
        '>': 'OOO...',  # Less than
        '(': 'OO..O.',  # Left parenthesis
        ')': 'O..OOO',  # Right parenthesis
    }
    braille_num = {
        # dictionary with Numbers (to differentiate between letters a-j)
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'

    }

    """
    helper function to check if value is float
    :param self: ref to current instance of the class
    :param value: The value to check if it's a valid float.
    :return: True if the value can be converted to a float, False otherwise.
    """

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    """
    helper function to check if value is present in dictionary
    :param self:ref to current instance of the class
    :param dict:dictionary to search the value 
    :param val: value to search in dictionary
    :return: True if the value is found in dict, False otherwise.
    """
    def key_in(self, dict, val) -> bool:
        for key, value in dict.items():
            if val in value:
                return True
            else:
                False

    """
    helper function to get key from value from the provided dictionary
    :param self:ref to current instance of the class
    :param dict:dictionary to search the value 
    :param value:value to return the matching from dict
    :return:The key corresponding to the value, or None if the value is not found
    """
    def get_key(self, dict, value) -> string:

        for k, v in dict.items():
            if value in v:
                return k

    """
        function converts alpha numeric plain text to braille 
        :param self:ref to current instance of the class
        :param tokens:list of individual plain text characters 
        :param value:value to return the matching from dict
        :return:braille string is returned
        """
    def alphanum(self, tokens: list) -> string:
        output = ""
        is_number = False  # Track if we're in number mode

        for char in tokens:
            # Check if character is a space
            if char == ' ':
                output = output + self.braille_alpha_dict['space']
                is_number = False  # Reset number mode after space

            # Check if character is a digit
            elif char.isdigit():
                if not is_number:
                    output = output + self.braille_alpha_dict['number']  # Add number follows symbol once
                    is_number = True  # Now we are in number mode
                output = output + self.braille_num[char]

            # Check if character is a letter
            elif char.isalpha():
                if char.isupper():
                    output = output + self.braille_alpha_dict['capital']  # Add capital follows symbol
                output = output + self.braille_alpha_dict[char.lower()]
                is_number = False  # Exit number mode after letter

        return output

    """
     function converts plain text to braille 
    :param self:ref to current instance of the class
    :param tokens:list of individual plain text characters 
    :param value:value to return the matching from dict
    :return:braille string is returned
    """
    def alpha(self, tokens: list) -> string:
        output = ""
        regex = re.compile('!()<>?/:.,-/]')
        for token in tokens:
            if token.isupper():
                output = output + self.braille_alpha_dict['capital'] + self.braille_alpha_dict[token.lower()]
            elif token == ' ':
                output = output + self.braille_alpha_dict['space']
            elif regex.search(token) is not None:
                output = output + self.braille_alpha_dict[token]
            else:
                output = output + self.braille_alpha_dict[token.lower()]
        return output

    """
       function converts numeric plain text to braille 
      :param self:ref to current instance of the class
      :param tokens:list of individual plain text characters 
      :param value:value to return the matching from dict
      :return:braille string is returned
      """
    def num(self, tokens: list) -> string:
        output = ""
        if '.' in tokens:
            output = output + self.braille_alpha_dict['decimal']
            for token in tokens:
                output = output + self.braille_num[token]
        else:
            output = output + self.braille_alpha_dict['number']
            for token in tokens:
                output = output + self.braille_num[token]
        return output


    def translate(self):
        output = []
        capitalize_next = False
        alpha = False
        number_mode = False
        # Command to run translator.py script
        if len(sys.argv) > 1:
            command = ' '.join(sys.argv[1:])
        else:
            command = ''.join(sys.argv[1])
        s = set(command)
        if '.' in s and 'O' in s:
            chunks = [command[i:i + 6] for i in range(0, len(command), 6)]

            for chunk in chunks:
                # Check for special symbols
                alpha = True
                if chunk == '.....O':  # Capital follows
                    capitalize_next = True
                elif chunk == '.O.OOO':  # Number follows
                    number_mode = True
                elif chunk == '......':  # Space
                    output.append(' ')
                    number_mode = False  # Reset number mode after space
                elif number_mode or capitalize_next or alpha:
                    # If in number mode, translate using the number dictionary
                    if number_mode:
                        if self.key_in(self.braille_num, chunk):
                            char = self.get_key(self.braille_num, chunk)
                            if char.isdigit():
                                output.append(char)
                    # Otherwise, use the letter dictionary
                    else:
                        if self.key_in(self.braille_alpha_dict, chunk):
                            char = self.get_key(self.braille_alpha_dict, chunk)
                            if capitalize_next:
                                char = char.upper()
                                capitalize_next = False
                                output.append(char)

                            else:
                                output.append(char)
                                alpha = False

            print(''.join(output))

        else:
            out = ""
            tokens = list(command)
            if "".join([char for char in command if char.isalnum()]).isalnum():
                out = self.alphanum(tokens=tokens)
                print(out)
            elif command.isdigit() == False:
                out = self.alpha(tokens=tokens)
                print(out)
            elif command.isdigit() or self.is_float(command):
                out = self.num(tokens=tokens)
                print(out)


if __name__ == '__main__':
    test = Translator()
    test.translate()
