import json
import sys
import re

# Load the Braille mappings from a JSON configuration file
def load_config(config_file='braille_config.json'):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# Braille Translator class
class translator:
    def __init__(self, config):
        self.alphabet_to_braille = config.get('alphabet', {})
        self.numbers = config.get('numbers', {})
        self.special = config.get('special', {})

        # Reverse mapping for braille to text translation
        self.braille_to_alphabet = {v: k for k, v in self.alphabet_to_braille.items()}
        self.braille_to_numbers = {v: k for k, v in self.numbers.items()}
        self.braille_to_special = {v: k for k, v in self.special.items()}

    def is_valid_braille(self, input_string):
        return all(c in {'O', '.'} for c in input_string) and len(input_string) % 6 == 0

    def is_valid_text(self, input_string):
        # Define a regular expression pattern to match valid text characters including additional symbols
        pattern = re.compile(r'^[a-zA-Z0-9 ,.?!><:;/()\-]+$')
        return bool(pattern.match(input_string))

    def translate(self, input_string):
        if self.is_valid_braille(input_string):
            return self.braille_to_text(input_string)
        elif self.is_valid_text(input_string):
            return self.text_to_braille(input_string)
        else:
            raise ValueError("Invalid input format. Input should be either valid Braille (0 and .) or valid text with allowed special characters.")

    def braille_to_text(self, braille_string):
        output = []
        i = 0
        in_number_sequence = False

        while i < len(braille_string):
            braille_char = braille_string[i:i+6]
            if braille_char == self.special.get('space'):
                output.append(' ')
                in_number_sequence = False
                i += 6
            elif not in_number_sequence:
                if braille_char == self.special.get('number_indicator'):
                    in_number_sequence = True
                    i += 6
                elif braille_char == self.special.get('capital'):
                    if i + 6 < len(braille_string):
                        next_braille_char = braille_string[i+6:i+12]
                        letter = self.braille_to_alphabet.get(next_braille_char, '')
                        output.append(letter.upper())
                        i += 12
                    else:
                        i += 6  # Skip the capital symbol if no following character
                elif braille_char in self.braille_to_alphabet:
                    if in_number_sequence:
                        output.append(self.braille_to_numbers.get(braille_char, ''))
                    else:
                        output.append(self.braille_to_alphabet[braille_char])
                    i += 6
            elif braille_char in self.braille_to_numbers or in_number_sequence:
                if braille_char == self.special.get('decimal_indicator'):
                    output.append(".")
                    i+=12
                else:
                    output.append(self.braille_to_numbers[braille_char])
                    in_number_sequence = True
                    i += 6
            else:
                output.append('')  # Unknown Braille character
                i += 6
        return ''.join(output)

    def text_to_braille(self, text_string):
        output = []
        number_indicator = self.special.get('number_indicator', '') 
        pattern = re.compile(r'^[a-zA-Z0-9 ,.?!><:;/()\-]+$')
        in_number_sequence = False
        for char in text_string:
            if char.isspace():
                output.append(self.special.get('space', ''))
                in_number_sequence = False
            elif char.isdigit() or in_number_sequence:
                # Add number indicator before the digit
                if char == ".":
                    output.append(self.special.get('decimal_indicator', ''))
                    output.append(self.special.get(char, ''))
                    continue
                elif not in_number_sequence:
                    output.append(number_indicator)
                    in_number_sequence=True
                output.append(self.numbers.get(char, ''))
            elif not in_number_sequence and char.isalpha():
                if char.isupper():
                    output.append(self.special.get('capital', ''))  # Capitalization indicator
                output.append(self.alphabet_to_braille.get(char.lower(), ''))
            elif not in_number_sequence and bool(pattern.match(char)):
                output.append(self.special.get(char, ''))
            else:
                output.append('')  # Unknown character
        return ''.join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input_string>")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    try:
        # Load configuration
        config = load_config()

        # Create BrailleTranslator instance with the loaded config
        translator = translator(config)

        # Translate the input string
        translation = translator.translate(input_string)
        print(translation)
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    
    except ValueError as e:
        print(e)
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
