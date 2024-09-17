import sys

# Braille mappings for English letters and numbers
letter_braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......', 'capital_follows': '.....O', 'number_follows': '.O.OOO'
}

number_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Combine dictionaries for easy lookup
braille_dict = {**letter_braille_dict, **number_braille_dict}

# inversion so that it can be translated braille back to english
inverse_letter_braille_dict = {v: k for k, v in letter_braille_dict.items()}
inverse_number_braille_dict = {v: k for k, v in number_braille_dict.items()}


def is_braille(s):
    # checking if the input is a valid braille format
    return len(s) % 6 == 0 and all(c in "O." for c in s)


def english_to_braille(text):
    result = []  # stores the list of braille translation
    number_mode = False  # checks if number mode is active or not

    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_dict['number_follows'])
                number_mode = True
            result.append(number_braille_dict.get(char, ''))

            # If the character is a letter, it checks if it's uppercase.
            # it adds the "capital" indicator (.....O) if it is a capital letter
            # and converts the letter to lowercase before
            # adding the rest of the Braille code
        elif char.isalpha():
            if char.isupper():
                result.append(braille_dict['capital_follows'])
                char = char.lower()
            number_mode = False
            result.append(letter_braille_dict.get(char, ''))
        elif char == ' ':
            number_mode = False
            result.append(braille_dict[' '])

    return ''.join(result)


def braille_to_english(braille):
    """Translate Braille text to English."""
    result = []
    i = 0
    number_mode = False
    capital_mode = False

    while i < len(braille):
        chunk = braille[i:i + 6]

        # Handle special modes
        if chunk == braille_dict['capital_follows']:
            capital_mode = True
            i += 6
            continue
        elif chunk == braille_dict['number_follows']:
            number_mode = True
            i += 6
            continue

        # Translate Braille chunk to character
        if number_mode:
            char = inverse_number_braille_dict.get(chunk, '?')
            if char.isdigit():
                result.append(char)
                i += 6
                continue  # Stay in number mode for next chunk
            else:
                result.append('?')  # Handle error if non-digit found in number mode
                number_mode = False  # Reset number mode
        else:
            char = inverse_letter_braille_dict.get(chunk, '?')
            if capital_mode:
                char = char.upper()
                capital_mode = False
            result.append(char)

        i += 6

    return ''.join(result)


def main():
    while True:
        print("Braille Translator")
        print("Enter text to translate:")
        user_input = input(">>> ").strip()

        if is_braille(user_input):
            try:
                translation = braille_to_english(user_input)
            except ValueError as e:
                print(e)
                continue
        else:
            translation = english_to_braille(user_input)

        print(translation)
        print("\n")

        again = input("Do you want to translate another text? (yes/no): ").strip().lower()
        if again != 'yes':
            break


if __name__ == "__main__":
    main()

