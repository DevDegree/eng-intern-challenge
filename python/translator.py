import sys  # a way to read command line arguments

class Translator:
    # Braille encoding for lowercase letters a-z
    braille_alphabet = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......',  # space is 6 dots empty
    }

    # Braille encoding for numbers 0-9
    braille_numbers = {
        '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
    }

    # Special symbols for capital letters and numbers
    braille_capital = '.....O'  # Precedes capital letters
    braille_number = '.O.OOO'   # Precedes numbers

    def __init__(self, args):
        # Store the arguments, ignoring the script name (args[0])
        self.args = args[1:]

    def translate(self):
        input_text = ' '.join(self.args)

        # Determine whether input is in English or Braille
        if all(c in 'O.o ' for c in input_text):
            return self.braille_to_english(input_text)
        else:
            return self.english_to_braille(input_text)

    def english_to_braille(self, text):
        braille_text = []
        number_mode = False
        for char in text:
            if char.isupper():
                braille_text.append(self.braille_capital)
                braille_text.append(self.braille_alphabet[char.lower()])
            elif char.isdigit() and not number_mode:
                braille_text.append(self.braille_number)
                braille_text.append(self.braille_numbers[char])
                number_mode = True
            elif char.isdigit() and number_mode:
                braille_text.append(self.braille_numbers[char])
            else:
                braille_text.append(self.braille_alphabet[char])
                number_mode = False  # Reset number mode on non-digit
        return ''.join(braille_text)

    
    def braille_to_english(self, braille):
        
        # Break Braille string into 6-character chunks
        braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
        english_text = []
        capital_mode = False
        number_mode = False

        for braille_char in braille_chars:
            if braille_char == self.braille_capital:
                capital_mode = True
                continue
            elif braille_char == self.braille_number:
                number_mode = True
                continue
            elif braille_char == '......':
                english_text.append(' ')
                number_mode = False  # Reset number mode after a space
                continue

            # First check the numbers dictionary
            for char, braille_code in self.braille_numbers.items():
                if braille_code == braille_char and number_mode: # the missing piece
                    english_text.append(char)  # Append digit
                    break
            else:
                # Then check the letters dictionary
                for char, braille_code in self.braille_alphabet.items():
                    if braille_code == braille_char:
                        if capital_mode:
                            english_text.append(char.upper())  # Capitalize letter
                            capital_mode = False  # Reset capital mode after using it
                        else:
                            english_text.append(char)  # Regular letter
                        break

        return ''.join(english_text)
    

        
if __name__ == "__main__":
    translator = Translator(sys.argv)
    translation_result = translator.translate()
    print(f"{translation_result}")

