import sys

# Braille mapping
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ', '.....O': 'CAP', '.O.OOO': 'NUM'
}

# Additional mappings for numbers
numbers_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Functions will be defined here

def translate_braille_to_english(braille_text):
    result = []
    capitalize = False
    is_number = False

    # Split the input string into chunks of 6 characters (Braille characters)
    chars = [braille_text[i:i + 6] for i in range(0, len(braille_text), 6)]

    for char in chars:
        if char == '.....O':  # Capital sign
            capitalize = True
        elif char == '.O.OOO':  # Number sign
            is_number = True  # Start a number sequence
        elif char == '......':  # Handle space
            result.append(' ')
            is_number = False  # Reset number flag after space
        else:
            if is_number:
                # Process as a number if the number flag is set
                for key, value in numbers_braille.items():
                    if char == value:
                        result.append(key)
                # Do not reset is_number so that we can capture multiple digits
            else:
                letter = braille_to_english.get(char, '')
                if capitalize:
                    result.append(letter.upper())
                    capitalize = False
                else:
                    result.append(letter)

    return ''.join(result)

def main():
    # Main execution logic will go here
    pass  # Placeholder

if __name__ == '__main__':
    main()

