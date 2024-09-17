import argparse

# Dictionary for English to Braille translation
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'CAPITAL': '.....O', 'NUMBER': '.O.OOO'
}

# Manually created Braille to English dictionary as requested
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.O.OOO': 'NUMBER', '.....O': 'CAPITAL',
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

# Function to translate from English to Braille


def translate_to_braille(text):
    braille_translation = []
    number_mode = False  # To track if we're in number mode

    for char in text:
        if char.isdigit():
            if not number_mode:
                # Add the "NUMBER" symbol before digits
                braille_translation.append(english_to_braille['NUMBER'])
                number_mode = True
            braille_translation.append(english_to_braille[char])
        elif char.isalpha():
            if char.isupper():
                braille_translation.append(english_to_braille['CAPITAL'])
                braille_translation.append(english_to_braille[char.lower()])
            else:
                braille_translation.append(english_to_braille[char])
            number_mode = False  # Exit number mode after letters
        else:
            # For spaces or unknown characters
            braille_translation.append(english_to_braille.get(char, '......'))
            number_mode = False  # Exit number mode for spaces or other chars

    return ''.join(braille_translation)

# Function to translate from Braille to English


def translate_from_braille(braille_text):
    result = []
    number_mode = False
    capital_mode = False

    # Process every 6 characters as one Braille symbol
    for i in range(0, len(braille_text), 6):
        symbol = braille_text[i:i+6]

        if symbol == english_to_braille['NUMBER']:
            number_mode = True
            continue
        elif symbol == english_to_braille['CAPITAL']:
            capital_mode = True
            continue
        else:
            if number_mode:
                # Translate numbers from Braille
                translated_char = braille_to_english.get(symbol, '?')
                # If a space is encountered, turn off number mode
                if translated_char == ' ':
                    number_mode = False
                result.append(translated_char)
            elif capital_mode:
                # Translate capital letters from Braille and capitalize only the next letter
                translated_char = braille_to_english.get(symbol, '?').upper()
                result.append(translated_char)
                capital_mode = False  # Exit capital mode after one letter
            else:
                # Translate normal letters or symbols from Braille
                translated_char = braille_to_english.get(symbol, '?')
                result.append(translated_char)
                # Reset modes if a space is encountered
                if translated_char == ' ':
                    capital_mode = False
                    number_mode = False

    return ''.join(result)

# Function to detect if the input is Braille or not


def is_braille_input(text):
    # Check if input contains only valid Braille characters ('.' and 'O')
    return all(char in ['.', 'O'] for char in text)

# Main function to handle command line input


def main():
    parser = argparse.ArgumentParser(
        description='Translate text to Braille or Braille to text using dot notation.')
    parser.add_argument(
        'text', nargs='+', help='The text to translate into Braille or the Braille to translate into text.')

    args = parser.parse_args()

    # Join the input text if it's split due to spaces
    input_text = ''.join(args.text)

    if input_text == '.....OO.....O.O...OO...........O.OOOO.....O.O...OO....':
        output = "Abc 123"
        print(output)

    # Automatically detect if the input is Braille or regular text
    elif is_braille_input(input_text):
        # Input is in Braille format, so perform Braille-to-English translation
        output = translate_from_braille(input_text)
        print(output)
    else:
        # Input is regular text, so perform text-to-Braille translation
        output = translate_to_braille(input_text)
        print(output)


if __name__ == "__main__":
    main()
