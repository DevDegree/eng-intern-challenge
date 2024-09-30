
import sys

# Braille to English and vice versa mappings
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OOO...': 'd', 'O..O..': 'e',
    'OO.O..': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OOO.O.': 'n', 'O..OO.': 'o',
    'OO.OO.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OOO.OO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'CAP', '..OO.O': 'NUM'
}

# Reverse dictionary for English to Braille conversion
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Numbers in Braille (1-9 and 0)
number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OOO...', '5': 'O..O..',
    '6': 'OO.O..', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Function to detect if input is Braille or English
def is_braille(input_string):
    return all(c in ['O', '.', ' '] for c in input_string)

# Function to translate Braille to English
def braille_to_english_translator(braille_text):
    words = braille_text.split(' ')
    result = []
    capitalize_next = False
    is_number = False

    for word in words:
        for i in range(0, len(word), 6):
            braille_char = word[i:i + 6]
            if braille_char == '.....O':  # Capital letter indicator
                capitalize_next = True
                continue
            elif braille_char == '..OO.O':  # Number indicator
                is_number = True
                continue

            if is_number:
                result.append(braille_to_english[braille_char].upper())
            elif capitalize_next:
                result.append(braille_to_english[braille_char].upper())
                capitalize_next = False
            else:
                result.append(braille_to_english.get(braille_char, ' '))

        result.append(' ')  # Add a space between words

    return ''.join(result).strip()

# Function to translate English to Braille
def english_to_braille_translator(english_text):
    result = []
    for char in english_text:
        if char.isdigit():
            result.append('..OO.O')  # Number indicator
            result.append(number_to_braille[char])
        elif char.isupper():
            result.append('.....O')  # Capital letter indicator
            result.append(english_to_braille[char.lower()])
        elif char == ' ':
            result.append('......')  # Space
        elif char in english_to_braille:
            result.append(english_to_braille[char])
        else:
            # Ignore unsupported characters
            continue

        result.append(' ')  # Add a space between each Braille character

    return ''.join(result).strip()

# Main function to detect input type and translate accordingly
def main():
    # Get input string from command-line arguments
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return

    input_string = sys.argv[1]

    if is_braille(input_string):
        print(braille_to_english_translator(input_string))
    else:
        print(english_to_braille_translator(input_string))

if __name__ == "__main__":
    main()
