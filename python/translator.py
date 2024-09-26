class BrailleTranslator:
    
    braille_dict = {
        'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
        'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
        'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
        'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
        'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
        'z': "O..OOO", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
        '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...",
        '0': ".OOO..", ' ': "......"
    }
    
    capital_braille = ".....O"
    number_braille = ".O.OOO"

    english_dict = {v: k for k, v in braille_dict.items()}

    @staticmethod
    def translate_to_braille(text):
        braille_translation = []
        is_number = False

        for char in text:
            if char.isupper():
                braille_translation.append(BrailleTranslator.capital_braille)
                char = char.lower()

            if char.isdigit() and not is_number:
                braille_translation.append(BrailleTranslator.number_braille)
                is_number = True

            if char.isalpha() and is_number:
                is_number = False

            if char in BrailleTranslator.braille_dict:
                braille_translation.append(BrailleTranslator.braille_dict[char])

        return ''.join(braille_translation)

    @staticmethod
    def translate_to_english(braille):
        english_translation = []
        is_capital = False
        is_number = False

        for i in range(0, len(braille), 6):
            braille_char = braille[i:i + 6]

            if braille_char == BrailleTranslator.capital_braille:
                is_capital = True
                continue

            if braille_char == BrailleTranslator.number_braille:
                is_number = True
                continue

            if braille_char in BrailleTranslator.english_dict:
                translated_char = BrailleTranslator.english_dict[braille_char]

                if is_number:
                    number_mapping = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
                                      'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'}
                    translated_char = number_mapping.get(translated_char, translated_char)

                if is_capital:
                    translated_char = translated_char.upper()
                    is_capital = False

                english_translation.append(translated_char)

                if is_number and translated_char == ' ':
                    is_number = False

        return ''.join(english_translation)

    @staticmethod
    def main():
        import sys
        if len(sys.argv) < 2:
            print("Please provide input to translate.")
            return

        input_text = ' '.join(sys.argv[1:])

        if all(c in "O." for c in input_text):
            print(BrailleTranslator.translate_to_english(input_text))
        else:
            print(BrailleTranslator.translate_to_braille(input_text))

if __name__ == '__main__':
    BrailleTranslator.main()

