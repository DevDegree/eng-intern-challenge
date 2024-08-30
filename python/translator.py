import sys

alphabet_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

number_to_braille = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

upper_braille = '.....O'
number_braille = '.O.OOO'


braille_to_alphabet = {v: k for k, v in alphabet_to_braille.items()}
braille_to_number = {v: k for k, v in number_to_braille.items()}


def check_braille(string):
    # Check if the text contains only 'O' and '.'
    return all(char in 'O.' for char in string)


def translate_to_braille(text):
    result = []
    is_number = False

    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(upper_braille)
                char = char.lower()
            result.append(alphabet_to_braille[char])
            is_number = False  # Reset number flag when processing letters
        elif char.isdigit():
            if not is_number:
                result.append(number_braille)
                is_number = True  # Set number flag
            result.append(number_to_braille[char])
        elif char == " ":
            result.append(alphabet_to_braille[char])
            is_number = False  # Reset number flag when processing space

    return ''.join(result)


def braille_to_text(braille_string):
    """Translate Braille to English text."""
    text = []
    i = 0
    length = len(braille_string)
    is_number = False

    while i < length:
        braille_char = braille_string[i:i + 6]

        if braille_char == "......":
            is_number = False

        if braille_char == upper_braille:
            # Handle uppercase
            i += 6
            braille_char = braille_string[i:i + 6]
            if braille_char in braille_to_alphabet:
                text.append(braille_to_alphabet[braille_char].upper())
            elif braille_char in braille_to_number:
                text.append(braille_to_number[braille_char])
        elif braille_char == number_braille:
            is_number = True
            i += 6
            continue
        elif braille_char in braille_to_alphabet and is_number is False:
            text.append(braille_to_alphabet[braille_char])
            is_number = False
        elif braille_char in braille_to_number:
            if is_number:
                text.append(braille_to_number[braille_char])
            else:
                text.append('?')  # Unexpected number Braille
        elif braille_char == '......':  # Braille space
            text.append(' ')
        else:
            text.append('?')  # Unknown Braille pattern

        i += 6

    return ''.join(text)


def main():
    if len(sys.argv) < 2:
        return

    texts = sys.argv[1:]

    results = []

    for i, text in enumerate(texts):
        if check_braille(text):
            text_output = braille_to_text(text)
        else:
            text_output = translate_to_braille(text)
            if i > 0:
                results.append('......')  # Add Braille space between words



        results.append(text_output)

    print(''.join(results))


if __name__ == "__main__":
    main()