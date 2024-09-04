class Translator:
    english_to_braille = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO', ' ': '......',
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
        '^': '.....O', '#': '.O.OOO', '.': '.O...O', ',': '..O...', '?': '..O.OO',
        '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.',
        '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.'
    }

    braille_to_english = {v: k for k, v in english_to_braille.items()}

    @staticmethod
    def is_braille(input_str):
        return all(c in 'O.' for c in input_str)

    @staticmethod
    def english_to_braille_translator(text):
        output = ''
        number_mode = False

        for ch in text:
            if ch.isdigit():
                if not number_mode:
                    output += Translator.english_to_braille['#']
                    number_mode = True
                output += Translator.english_to_braille[ch]
            elif ch.isalpha():
                if ch.isupper():
                    output += Translator.english_to_braille['^']
                    output += Translator.english_to_braille[ch.lower()]
                else:
                    output += Translator.english_to_braille[ch]
                number_mode = False
            elif ch == ' ':
                output += Translator.english_to_braille[ch]
                number_mode = False
            elif ch in Translator.english_to_braille:
                output += Translator.english_to_braille[ch]
                number_mode = False

        return output

    @staticmethod
    def braille_to_english_translator(braille):
        if len(braille) % 6 != 0:
            print('Error: Invalid Braille input length.')
            return ''

        output = ''
        capital_mode = False
        number_mode = False

        for i in range(0, len(braille), 6):
            symbol = braille[i:i+6]

            if symbol == '.....O':
                capital_mode = True
                continue

            if symbol == '.O.OOO':
                number_mode = True
                continue

            english_char = Translator.braille_to_english.get(symbol, None)
            if english_char is None:
                print(f"Error: No English mapping found for Braille symbol: {symbol}")
                return ''

            if number_mode and english_char in 'abcdefghij':
                english_char = str((ord(english_char) - ord('a') + 1) % 10)
                number_mode = False

            if capital_mode:
                output += english_char.upper()
                capital_mode = False
            else:
                output += english_char

        return output

# Test cases
print('Testing English to Braille: Hello world')
braille_output = Translator.english_to_braille_translator('Hello world')
print(f"Output: {braille_output}")

print('Testing Braille to English: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
english_output = Translator.braille_to_english_translator('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....')
print(f"Output: {english_output}")
