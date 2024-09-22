import sys

# Braille dictionary mapping for letters, numbers, and special characters
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "cap": ".....O", "num": ".O.OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

# Reverse lookup for translating Braille back to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}


def is_braille(text):
    """
    Checks if the given input is Braille based on the presence of 'O' and '.' characters only.
    """
    return all(c in 'O.' for c in text)


def braille_to_english(braille):
    """
    Convert Braille to English text.
    This function handles capital letters, numbers, and spaces.
    """
    result = []
    i = 0
    length = len(braille)

    # Flags to handle capitalization and number mode
    capitalize = False
    number_mode = False

    while i < length:
        symbol = braille[i:i + 6]

        if symbol == braille_alphabet["cap"]:
            capitalize = True
        elif symbol == braille_alphabet["num"]:
            number_mode = True
        elif symbol in reverse_braille_alphabet:
            char = reverse_braille_alphabet[symbol]
            if number_mode and char.isalpha():
                # Convert to number (based on Braille letters 'a' -> '1', 'j' -> '0')
                char = str((ord(char) - ord('a') + 1) % 10)
            elif not number_mode and char.isdigit():
                # Convert digit to corresponding letter
                char = chr(((int(char) - 1) % 9) + ord('a'))

            if capitalize:
                char = char.upper()
                capitalize = False

            result.append(char)

            if char == " ":
                number_mode = False
        else:
            # Handle unknown symbol
            result.append(" ")
        i += 6

    return ''.join(result)


def english_to_braille(text):
    """
    Convert English text to Braille.
    This function handles capital letters, numbers, and spaces.
    """
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(braille_alphabet["cap"])
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                result.append(braille_alphabet["num"])
                number_mode = True
            # Convert digit to corresponding letter (1-9 -> a-i, 0 -> j)
            char = chr(((int(char) - 1) % 9) + ord('a'))
        elif char.isalpha() or char == ' ':
            if number_mode:
                number_mode = False

        if char in braille_alphabet:
            result.append(braille_alphabet[char])
        else:
            # Handle unknown character
            result.append(braille_alphabet[" "])

    return ''.join(result)


def main():
    # When there is no arg
    if len(sys.argv) <= 1:
       return ""

    text = " ".join(sys.argv[1:]);

    # Determine whether the input is Braille or English and convert accordingly
    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

    english_to_braille()
if __name__ == "__main__":
    main()
