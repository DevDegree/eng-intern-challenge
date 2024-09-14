import sys

# Braille characters to alphabet mapping
BRAILLE_TO_ALPHABET = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OOO.O': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '......': ' ',
    '.....O': 'capital_next',
    '.O.OOO': 'number_next',
}

# Alphabet characters to braille mapping
ALPHABET_TO_BRAILLE = {alphabet: braille for braille, alphabet in BRAILLE_TO_ALPHABET.items()}

"""
Checks if a given string is written in braille.
Parameters:
    message (str): The given message to be translated.
Returns:
    boolean: True if message is in braille, else False.
"""
def is_braille(message):
    # Braille messages must be a multiple of 6
    if len(message) % 6 != 0:
        return False

    # Check if all characters are either 'O' or '.'
    valid_chars = {'O', '.'}
    for char in message:
        if char not in valid_chars:
            return False

    return True


"""
Converts a braille string to its corresponding alphanumeric message.
Parameters:
    braille_message (str): The given braille message to be translated.
Returns:
    translated_text (str): The translated alphanumeric message.
"""
def braille_to_alphabet_translator(braille_message):
    # Partition the braille string every 6 characters
    braille_characters = [braille_message[i:i + 6] for i in range(0, len(braille_message), 6)]
    translated_text = ''

    # Technical flags needed for special cases
    capitalize_next = False
    number_next = False

    # Loop through each braille character and perform the translation necessary
    for braille_character in braille_characters:
        character_as_alphabet = BRAILLE_TO_ALPHABET.get(braille_character)

        if character_as_alphabet == 'capital_next':
            capitalize_next = True
        elif character_as_alphabet == 'number_next':
            number_next = True
        elif character_as_alphabet == ' ':
            translated_text += ' '
            number_next = False
        else:
            if capitalize_next:
                character_as_alphabet = character_as_alphabet.upper()
                capitalize_next = False
            if number_next:
                character_as_alphabet = 0 if character_as_alphabet == 'j' else ord(character_as_alphabet.lower()) - ord('a') + 1

            translated_text += str(character_as_alphabet)

    return translated_text


"""
Converts an alphanumeric string to its corresponding braille message.
Parameters:
    alphanumeric_message (str): The given alphanumeric_message message to be translated.
Returns:
    translated_text (str): The translated braille string.
"""
def alphabet_to_braille_translator(alphanumeric_message):
    translated_text = ''

    # Technical flags needed for special cases
    is_prev_numerical = False

    # Loop through each alphanumeric character and perform the translation necessary
    for character in alphanumeric_message:
        if character.isupper():
            is_prev_numerical = False
            capital_next_braille = str(ALPHABET_TO_BRAILLE.get('capital_next'))
            character_as_braille = str(ALPHABET_TO_BRAILLE.get(character.lower()))

            translated_text += capital_next_braille + character_as_braille
        elif character.isnumeric():
            if not is_prev_numerical:
                number_next_braille = str(ALPHABET_TO_BRAILLE.get('number_next'))
                translated_text += number_next_braille

            is_prev_numerical = True
            number_as_character = 'j' if character == '0' else chr(int(character) + ord('a') - 1)
            translated_text += str(ALPHABET_TO_BRAILLE.get(number_as_character))
        else:
            if is_prev_numerical and character == ' ':
                is_prev_numerical = False
            translated_text += str(ALPHABET_TO_BRAILLE.get(character))

    return translated_text


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_string = ''

        for index in range(1, len(sys.argv)):
            input_string += sys.argv[index] + ' '
        input_string = input_string.strip()

        if is_braille(input_string):
            print(braille_to_alphabet_translator(input_string))
        else:
            print(alphabet_to_braille_translator(input_string))
    else:
        print("Please enter a valid argument.")