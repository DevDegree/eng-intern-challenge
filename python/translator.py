
class BrailleTranslator:
    english_to_braille_letter = {
        'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...",
        'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
        'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.",
        's': ".OO.O.", 't': ".OOOO.", 'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
        'y': "OO.OOO", 'z': "O..OOO"
    }

    english_to_braille_number = {
        '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...",
        '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
    }

    braille_to_english_letter = {v: k for k, v in english_to_braille_letter.items()}
    braille_to_english_number = {v: k for k, v in english_to_braille_number.items()}

    CAPITAL_PREFIX = ".....O"
    NUMBER_PREFIX = ".O.OOO"
    SPACE = "......"
    BRAILLE_LENGTH = 6

    @staticmethod
    def translate_to_braille(input_str):
        result = []
        is_number = False

        for ch in input_str:
            if ch == ' ':
                result.append(BrailleTranslator.SPACE)
                is_number = False
                continue
            if ch.isupper():
                result.append(BrailleTranslator.CAPITAL_PREFIX)
                ch = ch.lower()
                is_number = False

            if ch.isdigit() and not is_number:
                result.append(BrailleTranslator.NUMBER_PREFIX)
                is_number = True
            elif not ch.isdigit() and is_number:
                is_number = False

            if is_number:
                result.append(BrailleTranslator.english_to_braille_number[ch])
            else:
                result.append(BrailleTranslator.english_to_braille_letter[ch])

        return ''.join(result)

    @staticmethod
    def translate_to_english(input_str):
        result = []
        is_capital = False
        number_mode = False

        for i in range(0, len(input_str), BrailleTranslator.BRAILLE_LENGTH):
            braille_char = input_str[i:i + BrailleTranslator.BRAILLE_LENGTH]

            if braille_char == BrailleTranslator.CAPITAL_PREFIX:
                is_capital = True
                number_mode = False
                continue
            elif braille_char == BrailleTranslator.NUMBER_PREFIX:
                is_capital = False
                number_mode = True
                continue
            elif braille_char == BrailleTranslator.SPACE:
                result.append(' ')
                is_capital = False
                number_mode = False
                continue

            if number_mode:
                english_char = BrailleTranslator.braille_to_english_number[braille_char]
            else:
                english_char = BrailleTranslator.braille_to_english_letter[braille_char]
                if is_capital:
                    english_char = english_char.upper()
                    is_capital = False

            result.append(english_char)

            if number_mode and not english_char.isdigit():
                number_mode = False

        return ''.join(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide input to translate.")
    else:
        final_output = ""

        # Iterate through all arguments passed except the script name
        for index, input_data in enumerate(sys.argv[1:], start=1):
            if input_data.startswith('O') or input_data.startswith('.'):
                final_output += BrailleTranslator.translate_to_english(input_data)
                if index != len(sys.argv) - 1:
                    final_output += ' '
            else:
                final_output += BrailleTranslator.translate_to_braille(input_data)
                if index != len(sys.argv) - 1:
                    final_output += BrailleTranslator.SPACE

        print(final_output)
