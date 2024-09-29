
import sys  # to read the command line arguments


class BrailleChallenge:
    english_to_braille = {
        # Letters
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',

        # Space character
        " ": '......',

        # Special indicators
        'capital': '.....O',  # Capital letter marker (dot 6)
        'number': '.O.OOO',  # Number follows marker (dots 3-4-5-6)
    }

    braille_to_english = {v: k for k, v in english_to_braille.items()}

    # Mapping digits to letters 'a' to 'j' for Braille representation
    digit_to_letter = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }

    # Mapping letters 'a' to 'j' to digits '1' to '0' for number mode
    letter_to_digit = {v: k for k, v in digit_to_letter.items()}

    def __init__(self, input_str: str):
        self.input_str = input_str

    def to_braille(self) -> str:
        result = ""
        i = 0
        while i < len(self.input_str):
            char = self.input_str[i]
            if char.isdigit():
                # Start number mode
                result += self.english_to_braille['number']
                while i < len(self.input_str) and self.input_str[i].isdigit():
                    digit = self.input_str[i]
                    # Map the digit to the corresponding letter
                    letter = self.digit_to_letter[digit]
                    result += self.english_to_braille[letter]
                    i += 1
                continue  # Skip incrementing i at the end of the loop
            elif char.isupper():
                # Capital letter indicator
                result += self.english_to_braille['capital']
                result += self.english_to_braille[char.lower()]
            else:
                result += self.english_to_braille[char]
            i += 1
        return result

    def to_text(self) -> str:
        result = ""
        idx = 0
        braille_chars = []

        # Split the Braille string into 6-character chunks
        while idx < len(self.input_str):
            br_str = self.input_str[idx: idx + 6]
            eng = self.braille_to_english[br_str]
            braille_chars.append(eng)
            idx += 6

        i = 0
        number_mode = False
        while i < len(braille_chars):
            char = braille_chars[i]
            if char == 'number':
                number_mode = True
                i += 1
                continue
            if char == 'capital':
                next_char = braille_chars[i + 1]
                result += next_char.upper()
                i += 2
                continue
            if char == ' ':
                result += ' '
                number_mode = False  # Reset number mode after a space
                i += 1
                continue
            else:
                if number_mode:
                    digit = self.letter_to_digit.get(char)
                    result += digit
                else:
                    result += char
                i += 1
        return result

    def is_braille(self) -> bool:
        # Check if the length is a multiple of 6
        if len(self.input_str) % 6 != 0:
            return False

        idx = 0
        while idx < len(self.input_str):
            braille_character = self.input_str[idx: idx + 6]
            if braille_character not in self.braille_to_english:
                return False
            idx += 6

        return True


def main():
    if len(sys.argv) < 2:
        return

    text = ' '.join(sys.argv[1:])
    braille = BrailleChallenge(text)

    # Determine if the input text is Braille or English
    if braille.is_braille():
        output = braille.to_text()
    else:
        output = braille.to_braille()

    print(output)


if __name__ == '__main__':
    main()
