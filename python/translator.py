import sys

class Braille:
    '''
    Braille class 
    '''

    char_to_braille: dict[str, str] = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',
        'capital': '.....O',
        'number': '.O.OOO',
        ' ': '......',
    }

    braille_to_char: dict[str, str] = {val: key for key, val in char_to_braille.items() if key.isalpha() or key.isspace()}
    braille_to_nums: dict[str, str] = {val: key for key, val in char_to_braille.items() if key.isdigit()}

    @staticmethod
    def isEncoded(text: str) -> bool:
        '''
        isEncoded(str) -> bool
        checks if the string argument is a braille or not
        returns True if text is braille, returns False if text is cleartext
        '''
        text = text.replace(' ', '')

        if 0 != len(text) % 6:
            return False

        for char in text:
            if char not in ('O', '.'):
                return False

        return True

    @staticmethod
    def encode(clear_text: str) -> str:
        '''
        encode(str) -> str
        encodes the string in clear_text to Braille
        raises Exception if unknown character encountered
        '''
        is_number_mode = False
        encoded: list[str] = []
        for char in clear_text:
            if char.isdigit():
                if not is_number_mode:
                    is_number_mode = True
                    encoded.append(Braille.char_to_braille['number'])
                encoded.append(Braille.char_to_braille[char])
            elif char.isupper():
                encoded.append(Braille.char_to_braille['capital'])
                encoded.append(Braille.char_to_braille[char.lower()])
                is_number_mode = False
            elif char.isspace():
                encoded.append(Braille.char_to_braille[' '])
                is_number_mode = False
            else:
                if char in Braille.char_to_braille:
                    encoded.append(Braille.char_to_braille[char])  # Default to space for unknown chars
                    is_number_mode = False
                else:
                    raise Exception(f'Unknown character encountered: {char}')

        return ''.join(encoded)

    @staticmethod
    def decode(encoded_text: str) -> str:
        '''
        decode(str) -> str
        decodes braille string to clear text
        raises Exception if unknown character encountered
        '''

        encoded_list: list[str] = [encoded_text[i:i+6] for i in range(0, len(encoded_text), 6)]
        decoded: list[str] = []
        skip_next = False
        is_number_mode = False

        for i, braille_char in enumerate(encoded_list):
            if skip_next:
                skip_next = False
                continue

            if braille_char == Braille.char_to_braille['number']:
                is_number_mode = True
                continue

            elif braille_char == Braille.char_to_braille['capital']:
                # The next character is treated as a capital letter
                next_char = Braille.braille_to_char.get(encoded_list[i + 1], ' ')
                if next_char:
                    decoded.append(next_char.upper())
                skip_next = True
                is_number_mode = False  # End number mode after capital
                continue

            elif is_number_mode and braille_char != Braille.char_to_braille[' ']:
                # If we are in number mode, treat the braille character as a digit
                decoded.append(Braille.braille_to_nums.get(braille_char, ' '))
                continue

            else:
                # Regular alphabetic decoding (not in number mode)
                if braille_char in Braille.braille_to_char:
                    decoded.append(Braille.braille_to_char[braille_char])
                    is_number_mode = False
                else:
                    raise Exception(f"Unknown braille character: {braille_char}")
            
        return ''.join(decoded)


def main() -> None:
    input_text: str = ' '.join(sys.argv[1:])
    if Braille.isEncoded(input_text):
        print( Braille.decode(input_text))
    else:
        print( Braille.encode(input_text))

if __name__ == '__main__':
    main()
