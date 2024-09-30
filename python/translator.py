import sys

# Braille letter mappings (using 'O' and '.' for raised dots)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OO.OO',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Braille digit mappings (using 'O' and '.' for raised dots)
braille_digits = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille special symbols
braille_special = {
    'capital': '.....O',  # Braille capital follows symbol
    'number': '.O.OOO',   # Braille number follows symbol
    'space': '......'     # Braille space
}

# Reverse mappings to translate Braille back to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_digits = {v: k for k, v in braille_digits.items()}


"""Check if the input is Braille by checking if input made up of only '0' and/or '.' ."""
def is_braille(input_str):
    str_no_spaces = input_str.replace(' ', '')
    return all(char in 'O.' for char in str_no_spaces)

"""Translates English to Braille."""
"""Capital follows symbol shows up before each braille equivalent of a capital letter"""
"""Number follows symbol shows up once before first instance of braille equivalent of a number (setting number mode to be true) 
until a space is reached, which resets number mode to be false so that another number follows symbol will show up 
before the next braille equivalent of a number"""
def translate_to_braille(english_text):
    result = []
    number_mode = False  # Indicates if we're in number mode

    for char in english_text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_special['number'])
                number_mode = True
            result.append(braille_digits[char])
        elif char.isalpha():
            if char.isupper():
                result.append(braille_special['capital'])
            result.append(braille_alphabet[char.lower()])
            number_mode = False  # Exit number mode after encountering a letter
        elif char == ' ':
            # Space resets everything (both number mode and normal mode)
            result.append(braille_special['space'])
            number_mode = False

    return ''.join(result)

"""Translates Braille to English, considering numbers and capital letters."""
"""When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol."""
def translate_to_english(braille_text):
    words = braille_text.split(' ')
    result = []
    number_mode = False  # Indicates whether we are in number mode
    capitalize_next = False  # Indicates if the next letter should be capitalized

    for word in words:
        translated_word = []
        for symbol in [word[i:i + 6] for i in range(0, len(word), 6)]:
            if symbol == braille_special['number']:
                number_mode = True
            elif symbol == braille_special['capital']:
                capitalize_next = True
            elif symbol == braille_special['space']:
                translated_word.append(' ')
                number_mode = False
            elif number_mode:
                if symbol in reverse_braille_digits:
                    translated_word.append(reverse_braille_digits[symbol])
                else:
                    number_mode = False
            else:
                if symbol in reverse_braille_alphabet:
                    letter = reverse_braille_alphabet[symbol]
                    if capitalize_next:
                        letter = letter.upper()
                        capitalize_next = False
                    translated_word.append(letter)
        
        result.append(''.join(translated_word))

    return ' '.join(result)

def main():
    # Get the input string from the command-line arguments
    if len(sys.argv) < 2:
        print("Missing arguments")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    
    # Determine if the input is Braille or English
    if is_braille(input_text):
        # Translate Braille to English
        translated_text = translate_to_english(input_text)
    else:
        # Translate English to Braille
        translated_text = translate_to_braille(input_text)
    
    # Output the translated text
    print(translated_text)

if __name__ == "__main__":
    main()