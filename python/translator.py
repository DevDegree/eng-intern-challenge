import sys

# Dictionaries
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

capital_follows = '.....O'
number_follows = '.O.OOO'

english_to_braille = {}

# Reverse the dictionary
for braille, english in braille_to_english.items():
    english_to_braille[english] = braille


# Add capital letters
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    english_to_braille[char] = capital_follows + \
        english_to_braille[char.lower()]

braille_to_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

numbers_to_braille = {}

# Reverse the dictionary
for braille, num in braille_to_numbers.items():
    numbers_to_braille[num] = braille


def braille_to_text(braille_string):
    text = ''
    reading_numbers = False
    capitalize_next = False

    # Split the input string into Braille symbols (each symbol is 6 characters long)
    if len(braille_string) % 6 != 0:
        print("Error: Invalid Braille input length")
        return ""

    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        if braille_char == capital_follows:
            capitalize_next = True
            continue

        if braille_char == number_follows:
            reading_numbers = True
            continue

        if reading_numbers:
            if braille_char == english_to_braille[' ']:
                text += ' '
                reading_numbers = False
                continue
            elif braille_char in braille_to_numbers:
                text += braille_to_numbers[braille_char]
            else:
                print(f"Error: Unrecognized number '{braille_char}'")
                return ""
        else:
            if braille_char in braille_to_english:
                letter = braille_to_english[braille_char]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                text += letter
            else:
                print(f"Error: Unrecognized Braille symbol '{braille_char}'")
                return ""

    return text


def text_to_braille(text):
    braille = ''
    reading_numbers = False

    for char in text:
        if char.isdigit():
            if not reading_numbers:
                braille += number_follows
                reading_numbers = True
            braille += numbers_to_braille.get(char, '......')
        elif char == ' ':
            # Reset number mode when we hit space
            reading_numbers = False
            braille += english_to_braille[' ']
        else:
            if reading_numbers:
                print(
                    f"Error: Number follows symbol read but found non-number character '{char}'")
                return ""
            if char.isupper():
                braille += capital_follows
            # Assume no other characters, but default to space if char not found
            braille += english_to_braille.get(char.lower(), "......")
    return braille


def is_braille(input_string):
    for char in input_string:
        if char not in 'O.':
            return False
    return True


def main():
    if len(sys.argv) < 2:
        print("No input string provided")
        return

    # Joins all arguments into a single string
    input_string = " ".join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))


if __name__ == '__main__':
    main()