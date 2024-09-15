import sys

#  Braille to English mappings
braille_to_alpha = {
    'O.....': 'a', 'OO....': 'c', 'O.O...': 'b', 'OO.O..': 'd', 'O..O..': 'e',
    'OOOO..': 'g', 'OOO...': 'f', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'OO..O.': 'm', 'O.O.O.': 'l', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOOOO.': 'q', 'OOO.O.': 'p', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'OO..OO': 'x', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' ',
}

# Reverse mapping for English to Braille
alpha_to_braille = {v: k for k, v in braille_to_alpha.items()}

# Number mappings
braille_to_digit = {
    'O.....': '1', 'OO....': '3', 'O.O...': '2', 'OO.O..': '4', 'O..O..': '5',
    'OOOO..': '7', 'OOO...': '6', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

digit_to_braille = {v: k for k, v in braille_to_digit.items()}

# Punctuation mappings
braille_to_punct = {
    '..O...': ',', '..OO.O': '.', '..O.OO': '?', 
    'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')',
    '..O.O.': ';', '..OO..': ':', '....OO': '-',
    '.OO..O': '<',  '.O..O.': '/','..OOO.': '!'
}

punct_to_braille = {v: k for k, v in braille_to_punct.items()}

# Special indicators
capital_indicator = '.....O'
number_indicator = '.O.OOO'
punctuation_indicator = '.O...O'

def translate_braille_to_english(braille_input):
    result = []
    capitalize_next = False
    number_mode = False
    punctuation_mode = False

    braille_chars = [braille_input[i:i + 6] for i in range(0, len(braille_input), 6)]

    # Mapping for indicators for faster checks
    indicators = {
        capital_indicator: lambda: set_mode('capitalize'),
        number_indicator: lambda: set_mode('number'),
        punctuation_indicator: lambda: set_mode('punctuation'),
        '......': lambda: (result.append(' '), reset_modes())
    }

    # Function to set mode
    def set_mode(mode):
        nonlocal capitalize_next, number_mode, punctuation_mode
        if mode == 'capitalize':
            capitalize_next = True
        elif mode == 'number':
            number_mode = True
        elif mode == 'punctuation':
            punctuation_mode = True

    # Function to reset modes
    def reset_modes():
        nonlocal number_mode, punctuation_mode
        number_mode = False
        punctuation_mode = False

    for char in braille_chars:
        # Check if char is an indicator
        if char in indicators:
            indicators[char]()
            continue

        # Get the character based on current mode
        if punctuation_mode:
            character = braille_to_punct.get(char, '?')
            punctuation_mode = False  # reset after use
        elif number_mode:
            character = braille_to_digit.get(char, '?')
        else:
            character = braille_to_alpha.get(char, '?')

        # Capitalization logic
        if capitalize_next:
            character = character.upper()
            capitalize_next = False

        result.append(character)

    return ''.join(result).strip()

def translate_english_to_braille(english_input):
    result = []
    number_mode = False

    for char in english_input:
        if char.isdigit():
            if not number_mode:
                result.append(number_indicator)
                number_mode = True
            result.append(digit_to_braille[char])
        elif char.isupper():
            if number_mode:
                number_mode = False
            result.append(capital_indicator)
            result.append(alpha_to_braille[char.lower()])
        elif char in punct_to_braille:
            if number_mode:
                number_mode = False
            result.append(punctuation_indicator)
            result.append(punct_to_braille[char])
        else:
            if number_mode:
                number_mode = False
            result.append(alpha_to_braille.get(char, '......'))

    return ''.join(result)

def translate_input(input_string):
    if all(c in 'O. ' for c in input_string):
        return translate_braille_to_english(input_string)
    else:
        return translate_english_to_braille(input_string)

def main():
    input_data = " ".join(sys.argv[1:])
    translated_output = translate_input(input_data)
    print(translated_output)

if __name__ == "__main__":
    main()