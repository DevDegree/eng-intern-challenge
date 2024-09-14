import sys

class BrailleConverter:
    def __init__(self):
        self._maps = self._initialize_maps()

    def _initialize_maps(self):
        punctuation_map = {
            '.': '.O..OO', ',': '.O....', '?': '.O.OO.', '!': '.OO.O.', 
            ':': 'OO....', ';': 'O.O...', '-': '......', '/': 'O.O...', 
            '<': 'O..OO.', '>': '.OOO.O', '(': 'OO.OO.', ')': '.OO.OO'
        }
        special_symbols_map = {
            'cap': '.....O', 'num': '.O.OOO', 'dec': '.O...O', 'space': '......'
        }
        numbers_map = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
            '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
            '9': '.OO...', '0': '.OOO..'
        }
        letters_map = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 
            'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 
            'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
            'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
            'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
            'y': 'OO.OOO', 'z': 'O..OOO'
        }
        return {
            'punctuation': punctuation_map,
            'special_symbols': special_symbols_map,
            'numbers': numbers_map,
            'letters': letters_map,
            'braille_to_letters': {v: k for k, v in letters_map.items()},
            'braille_to_numbers': {v: k for k, v in numbers_map.items()},
            'braille_to_punctuation': {v: k for k, v in punctuation_map.items()}
        }

    def _is_braille_code(self, code):
        brailleValues = ['O', '.']
        return all(char in brailleValues for char in code) and len(code) % 6 == 0

    def _decode_from_braille(self, code):
        decoded = []
        idx = 0
        cap_mode, num_mode = False, False

        while idx < len(code):
            chunk = code[idx:idx + 6]

            if chunk == self._maps['special_symbols']['cap']:
                cap_mode = True
            elif chunk == self._maps['special_symbols']['num']:
                num_mode = True
            elif chunk == self._maps['special_symbols']['space']:
                decoded.append(' ')
                cap_mode = num_mode = False
            elif num_mode and chunk in self._maps['braille_to_numbers']:
                decoded.append(self._maps['braille_to_numbers'][chunk])
                num_mode = False
            elif chunk in self._maps['braille_to_letters']:
                char = self._maps['braille_to_letters'][chunk].upper() if cap_mode else self._maps['braille_to_letters'][chunk]
                decoded.append(char)
                cap_mode = False
            elif chunk in self._maps['braille_to_punctuation']:
                decoded.append(self._maps['braille_to_punctuation'][chunk])
            else:
                raise ValueError(f"Invalid Braille sequence '{chunk}'.")

            idx += 6

        return ''.join(decoded)


    def _encode_to_braille(self, text):
        encoded = []
        num_mode = False

        for ch in text:
            if ch.isdigit() and not num_mode:
                encoded.append(self._maps['special_symbols']['num'])
                num_mode = True

            if ch == ' ':
                encoded.append(self._maps['special_symbols']['space'])
                num_mode = False
            elif ch.isupper():
                encoded.append(self._maps['special_symbols']['cap'])
                encoded.append(self._maps['letters'][ch.lower()])
            elif ch.isdigit():
                encoded.append(self._maps['numbers'][ch])
            elif ch in self._maps['letters']:
                encoded.append(self._maps['letters'][ch])
            elif ch in self._maps['punctuation']:
                encoded.append(self._maps['punctuation'][ch])
            else:
                raise ValueError(f"Character '{ch}' cannot be translated.")

        return ''.join(encoded)

    def convert(self, text):
      return self._decode_from_braille(text) if self._is_braille_code(text) else self._encode_to_braille(text)

def main():
    input_text = ' '.join(sys.argv[1:])
    converter = BrailleConverter()

    try:
        result = converter.convert(input_text)
        print(result)
    except ValueError as err:
        print(f"Conversion error: {err}")

if __name__ == '__main__':
    main()