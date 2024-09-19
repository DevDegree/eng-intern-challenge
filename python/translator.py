import sys

# Define mappings between letters and the Braille cells
braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse mapping for Braille to letters
reverse_braille_map = {v: k for k, v in braille_map.items()}

# Mapping digits to letters (numbers are represented using letters a-j after a number sign)
digit_to_letter = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
    '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
}

# Reverse mapping for letters to digits
letter_to_digit = {v: k for k, v in digit_to_letter.items()}

def is_braille(s):
    return all(c in ('O', '.') for c in s.replace(' ', '')) and len(s.replace(' ', '')) % 6 == 0

def main():
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str.replace(' ', '')):
        # Braille to English
        output = ''
        index = 0
        number_mode = False
        capitalize_next = False
        input_str = input_str.replace(' ', '')

        while index < len(input_str):
            chunk = input_str[index:index+6]
            index += 6

            if chunk == braille_map[' ']:
                output += ' '
                number_mode = False
                continue
            elif chunk == braille_map['number']:
                number_mode = True
                continue
            elif chunk == braille_map['capital']:
                capitalize_next = True
                continue
            else:
                if chunk not in reverse_braille_map:
                    # Handle unknown Braille pattern
                    output += '?'
                    continue
                letter = reverse_braille_map[chunk]
                if number_mode:
                    if letter in letter_to_digit:
                        digit = letter_to_digit[letter]
                        output += digit
                    else:
                        # Not a valid digit after number sign
                        output += '?'
                else:
                    if capitalize_next:
                        output += letter.upper()
                        capitalize_next = False
                    else:
                        output += letter
    else:
        # English to Braille
        output = ''
        number_mode = False

        for char in input_str:
            if char == ' ':
                output += braille_map[' ']
                number_mode = False
            elif char.isdigit():
                if not number_mode:
                    output += braille_map['number']
                    number_mode = True
                letter = digit_to_letter[char]
                output += braille_map[letter]
            elif char.isalpha():
                if char.isupper():
                    output += braille_map['capital']
                    output += braille_map[char.lower()]
                else:
                    output += braille_map[char]
                number_mode = False
            else:
                # Skip any non-alphanumeric characters
                pass

    print(output)

if __name__ == "__main__":
    main()
