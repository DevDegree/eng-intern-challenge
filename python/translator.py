import sys
import json
from textwrap import wrap

BRAILLE_MAPPING = 'braille-ascii.json'

class BrailleReader():
    def __init__(self, inputs: str):
        self.inputs = inputs

        with open('braille-ascii.json', 'r') as file:
            self.decoder = json.load(file)   

    def translator(self, input: str):
        """Parses an input string and decodes it depending on whether or not it's a braille
        sequence or a string of words.

        Args:
            input (str): The string to decode.

        Raises:
            ValueError: if the string isn't formatted correctly

        Returns:
            str: The converted string 
        """
        if all(c in ('.', 'O') for c in input):
            if len(input) % 6 != 0:
                msg = "The braille sequence does not contain the correct amount of characters"
                raise ValueError(msg)
            return self.decode_braille(wrap(input,6))
        elif not all(c.isalnum() or c.isspace() for c in input):
            msg = "Do not include any special characters inside the string"
            raise ValueError(msg)
        return self.decode_alpha(input)

    def decoder_flip(self):
        """This function flips the dictionary with the english-braille translation so it can
        be used to decode bi-directionally.
        """
        self.decoder = {outer_key: {v: k for k, v in inner_dict.items()}
                        for outer_key, inner_dict in self.decoder.items()}

    def decode_braille(self, input: str):
        """Decodes braille sequences into english.

        Args:
            input (str): The string to decode.

        Returns:
            decoded (str): The converted string from braille to english.

        """
        self.decoder_flip()
        current_modifier = None
        decoded = []

        # Detects if the braille sequence is a modifier
        for text in input:
            if text in self.decoder["Modifier"].keys():
                current_modifier = self.decoder["Modifier"][text]
                continue

            if current_modifier:
                converted_text = self.decoder[current_modifier][text].upper()
                decoded.append(converted_text)
                current_modifier = None if not converted_text.isnumeric() else current_modifier
            else:
                decoded.append(self.decoder["Alpha"][text])

        return decoded
                
    def decode_alpha(self, input: str):
        """Decodes english sentences into braille sequences.

        Args:
            input (str): The string to decode.

        Returns:
            decoded (str): The converted string from english to braille.

        """
        decoded = []
        prev = None
        for index, text in enumerate(input):
            if not text.isnumeric():
                if text.isupper():
                    decoded.append(self.decoder['Modifier']['Alpha'])
                decoded.append(self.decoder['Alpha'][text.lower()])
            else:
                if index == 0 or not prev.isnumeric():
                    decoded.append(self.decoder['Modifier']['Numeric'])
                decoded.append(self.decoder['Numeric'][text])
            prev = text
        return decoded
    
    def decode(self):
        """Parses the input strings from the command line and sanitizes the input
        before decoding.
        """
        output = []
        # check if input is in braille or english
        for input in self.inputs:
            decoded_string = self.translator(input)
            output.append("".join(decoded_string))

        return "......".join(output)

if __name__ == "__main__":
    output = BrailleReader(sys.argv[1:])
    print(output.decode())

