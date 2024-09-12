import sys

class BrailleTranslator:
    # Braille dictionary mapping characters to Braille patterns
    BRAILLE_DICT = {
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
        '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
        '9': '.OO...', '0': '.OOO..', 
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
        ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
        '>': 'O.OOOO', '(': 'O.O..O', ')': '.O.OO.', 'capital': '.....O', 'decimal': '.O...O', 'number': '.O.OOO'
    }

    def __init__(self):
        pass

    def _is_valid_braille_length(self, text):
        return len(text) % 6 == 0

    def is_braille(self, text):
        if text is None:
            return "Your input is null. Please enter a valid text."
        return all(char in 'O.' for char in text.replace('\n', '').replace(' ', ''))

    def english_to_braille(self, text):
        # Wrap the input text in quotes if not already quoted
        if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
            text = text  # Already quoted
        else:
            text = f'"{text}"'  # Wrap in double quotes

        if text is None:
            return "Your input is null. Please enter a valid text."
        
        if not isinstance(text, str):
            return "Input text must be a string."

        # Remove the surrounding quotes for processing
        text = text.strip('"\'')
        
        if len(text) == 0:
            return "Input text is empty. Please enter some text."

        braille_text = ''
        is_number = False
        
        for char in text:
            if char.isupper():
                braille_text += self.BRAILLE_DICT.get('capital', '')
                braille_text += self.BRAILLE_DICT.get(char.lower(), '')
                is_number = False
            elif char.isdigit():
                if not is_number:
                    braille_text += self.BRAILLE_DICT.get('number', '')
                    is_number = True
                braille_text += self.BRAILLE_DICT.get(char, '')
            elif char == '.':
                braille_text += self.BRAILLE_DICT.get('decimal', '')
                is_number = False
            elif char == ' ':
                braille_text += self.BRAILLE_DICT.get(' ', '')
                is_number = False
            elif char in self.BRAILLE_DICT:
                braille_text += self.BRAILLE_DICT[char]
                is_number = False
            else:
                braille_text += f"Character '{char}' not found in Braille dictionary. Skipping."
        
        return braille_text.strip()

    def braille_to_english(self, text):
        if text is None:
            return "Your input is null. Please enter a valid text."

        if not isinstance(text, str):
            return "Input text must be a string."
        
        cleaned_text = text.replace('\n', '').replace(' ', '')
        if not self._is_valid_braille_length(cleaned_text):
            return "Braille text length must be a multiple of 6 characters."
        
        braille_chars = [cleaned_text[i:i+6] for i in range(0, len(cleaned_text), 6)]
        reversed_braille_dict = {v: k for k, v in self.BRAILLE_DICT.items()}
        
        english_text = ''
        skip_next = False
        
        for i, braille in enumerate(braille_chars):
            if skip_next:
                skip_next = False
                continue
            
            if braille == '.....O':
                if i + 1 < len(braille_chars):
                    next_braille = braille_chars[i + 1]
                    if next_braille in reversed_braille_dict:
                        english_text += reversed_braille_dict[next_braille].upper()
                        skip_next = True
                    else:
                        english_text += '?'
                continue
            
            if braille == '.O...O':
                if i + 1 < len(braille_chars):
                    next_braille = braille_chars[i + 1]
                    if next_braille in reversed_braille_dict:
                        english_text += '.'
                        skip_next = True
                    else:
                        english_text += '?'
                continue
            
            if braille == '.O.OOO':
                braille_to_number = {
                    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
                    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
                    '.OO...': '9', '.OOO..': '0'
                }
                reversed_braille_dict_number = {v: k for k, v in braille_to_number.items()}
                
                remaining_string = ''.join(braille_chars[i+1:])
                symbols = remaining_string.split('......')
                symbols_to_convert = symbols[0]
    
                numbers = []
                k = 0
                while k < len(symbols_to_convert):
                    symbol = symbols_to_convert[k:k+6]
                    if len(symbol) == 6 and symbol in braille_to_number:
                        numbers.append(braille_to_number[symbol])
                    k += 6
                
                english_text += ''.join(numbers)
                break

            if braille in reversed_braille_dict:
                english_text += reversed_braille_dict[braille]
            else:
                english_text += f"Braille pattern '{braille}' not found in dictionary. Skipping."
        
        return english_text.strip()

    def translate(self, text):
        if text is None:
            return "Your input is null. Please enter a valid text."
        
        if not isinstance(text, str):
            return "Input text must be a string."
        
        if len(text) == 0:
            return "Input text is empty. Please enter some text."
        
        if self.is_braille(text):
            return self.braille_to_english(text)
        else:
            return self.english_to_braille(text)

def list_to_string(input_value):
    if isinstance(input_value, list):
        return ' '.join(map(str, input_value))
    else:
        return "Error: Input is not a list"

def handle_input(*args):
    if len(args) == 1 and isinstance(args[0], str):
        # Single string input
        return args[0]
    else:
        # Multiple string inputs
        combined_string = ' '.join(args)
        return combined_string

def main():
    # Ensure you handle index errors if no arguments are provided
    if len(sys.argv) > 1:
        input_text = handle_input(*sys.argv[1:])
    else:
        input_text = ""  

    translator = BrailleTranslator()
    translated_text = translator.translate(input_text)
    print(translated_text)

if __name__ == "__main__":
    main()
