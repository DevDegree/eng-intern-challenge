import sys

# Dictionary for Braille to English translation
braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd',
    'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h',
    '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p',
    'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z',
    '.....O': 'cap', '..OOO.': 'num', '......': ' ',  # Capitalization marker, number marker, space
}

# Numbers 0-9 using 'a' to 'j' in Braille after the number marker
braille_to_english_numbers = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4',
    'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8',
    '.OO...': '9', '.OOO..': '0'
}

# Dictionary for English to Braille translation
english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille.update({
    'A': '.....O' + 'O.....',  # Capital 'A' is capital marker + 'a' Braille
    'B': '.....O' + 'O.O...',
    'C': '.....O' + 'OO....',
    # Continue for other capital letters
    ' ': '......',  # Space
    '1': '..OOO.' + 'O.....',  # Number marker + 'a' for 1
    '2': '..OOO.' + 'O.O...',
    '3': '..OOO.' + 'OO....',
    '4': '..OOO.' + 'OO.O..',
    '5': '..OOO.' + 'O..O..',
    '6': '..OOO.' + 'OOO...',
    '7': '..OOO.' + 'OOOO..',
    '8': '..OOO.' + 'O.OO..',
    '9': '..OOO.' + '.OO...',
    '0': '..OOO.' + '.OOO..'
})

# Function to translate from English to Braille
def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(english_to_braille['cap'])  # Append capitalization marker
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            result.append(english_to_braille['num'])  # Append number marker
            result.append(english_to_braille[char])
        else:
            result.append(english_to_braille.get(char, ''))
    return ''.join(result)

# Function to translate from Braille to English
def translate_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == '.....O':  # Capitalization marker
            capitalize_next = True
        elif symbol == '..OOO.':  # Number marker
            number_mode = True
        else:
            if number_mode:
                char = braille_to_english_numbers.get(symbol, '')
                result.append(char)
                number_mode = False
            else:
                char = braille_to_english.get(symbol, '')
                if capitalize_next:
                    result.append(char.upper())
                    capitalize_next = False
                else:
                    result.append(char)
        i += 6
    return ''.join(result)

# Function to detect if input is Braille or English
def detect_and_translate(input_str):
    if set(input_str).issubset({'O', '.'}):  # Check if input consists only of "O" and "."
        return translate_to_english(input_str)
    else:
        return translate_to_braille(input_str)

# Main function to handle input from the command-line
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <input_text>")
        sys.exit(1)

    input_str = sys.argv[1]
    output = detect_and_translate(input_str)
    print(output)
