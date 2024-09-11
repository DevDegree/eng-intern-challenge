import sys

# Define the Braille encoding for alphabet characters, where 'O' represents a raised dot
# and '.' represents no dot.
ALPHABET_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Define the Braille encoding for numeric characters.
NUMS_BRAILLE = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Define additional symbols in Braille, such as space, capitalization, and numbers.
SYMBOLS_BRAILLE = {
    'SPACE': '......',       # Braille code for a space character
    'CAPITAL_FOLLOW': '.....O',  # Braille code indicating a capital letter follows
    'NUMBER_FOLLOW': '.O.OOO'    # Braille code indicating numeric characters follow
}

# Create reverse mappings from Braille code to alphabet and numeric characters.
BRAILLE_ALPHABET = {val: key for key, val in ALPHABET_BRAILLE.items()}
BRAILLE_NUMS = {val: key for key, val in NUMS_BRAILLE.items()}


def is_braille(sentence):
    """
    Determines if the given string represents valid Braille.
    Braille sentences are a multiple of 6 characters and can only contain '.' or 'O'.

    :param sentence: A string potentially in Braille format.
    :return: Boolean indicating whether the sentence is valid Braille.
    """
    braille = {'.', 'O'}
    return len(sentence) % 6 == 0 and all([char in braille for char in sentence])


def translate_english_braille(sentence):
    """
    Translates an English sentence into Braille. Handles alphabetic characters (lower and upper case),
    numeric characters, and spaces.

    :param sentence: The English sentence to be converted into Braille.
    :return: A string representing the sentence in Braille code.
    """
    res = []
    read_num = False  # Flag indicating whether the sentence is currently reading a numeric value.

    for char in sentence:
        if char.isalpha():
            if char.isupper():
                # Insert symbol for capitalization before adding the lowercase equivalent.
                res.append(SYMBOLS_BRAILLE['CAPITAL_FOLLOW'])
            res.append(ALPHABET_BRAILLE[char.lower()])
        elif char.isnumeric():
            if not read_num:
                # Insert the number-following indicator if a number is encountered.
                read_num = True
                res.append(SYMBOLS_BRAILLE['NUMBER_FOLLOW'])
            res.append(NUMS_BRAILLE[char])
        elif char == ' ':
            # Insert Braille code for space and reset the number flag.
            res.append(SYMBOLS_BRAILLE['SPACE'])
            read_num = False
        else:
            # If the character is unknown (punctuation, etc.), it's currently skipped.
            continue

    return ''.join(res)


def translate_braille_english(sentence):
    """
    Translates a Braille-encoded sentence back into English. Handles alphabetic characters
    (lower and upper case), numeric characters, and spaces.

    :param sentence: The Braille-encoded string.
    :return: A string representing the sentence in English.
    """
    result = []
    read_num = False  # Flag indicating that numbers are being read.
    read_cap = False  # Flag indicating the next letter is capitalized.

    # Process each character in chunks of 6 (the length of a single Braille character).
    for i in range(0, len(sentence), 6):
        symbol = sentence[i: i + 6]

        if symbol == SYMBOLS_BRAILLE['NUMBER_FOLLOW']:
            read_num = True  # Activate number-reading mode.
            continue
        elif symbol == SYMBOLS_BRAILLE['CAPITAL_FOLLOW']:
            read_cap = True  # The next letter is uppercase.
            continue
        elif symbol == SYMBOLS_BRAILLE['SPACE']:
            result.append(' ')  # Append a space and reset numeric mode.
            read_num = False
        elif symbol in BRAILLE_NUMS and read_num:
            result.append(BRAILLE_NUMS[symbol])  # Append a number.
        elif symbol in BRAILLE_ALPHABET and read_cap:
            result.append(BRAILLE_ALPHABET[symbol].upper())  # Append an uppercase letter.
        elif symbol in BRAILLE_ALPHABET and not read_cap:
            result.append(BRAILLE_ALPHABET[symbol])  # Append a lowercase letter.
        else:
            # Unknown symbol handling is currently skipped.
            continue

        read_cap = False  # Reset capitalization flag after processing.

    return ''.join(result)


def main():
    """
    Main entry point of the program. Processes command-line input to either translate English
    to Braille or Braille to English based on the input format.
    """
    if len(sys.argv) < 2:
        # No input provided.
        return
    else:
        # Non-empty input: concatenate all arguments into a single string.
        args = sys.argv[1:]
        sentence = " ".join(args)

        # Check if the input is Braille or English, and call the appropriate translation function.
        if is_braille(sentence):
            print(translate_braille_english(sentence))
        else:
            print(translate_english_braille(sentence))


if __name__ == "__main__":
    main()

