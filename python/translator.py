import sys

# English to Braille mapping
english_to_braille = {
    # Letters a-z
  'a': 'O.....', 'b': 'O.O...',
  'c': 'OO....', 'd': 'OO.O..',
  'e': 'O..O..', 'f': 'OOO...',
  'g': 'OOOO..', 'h': 'O.OO..',
  'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.',
  'o': 'O..OO.', 'p': 'OOO.O.',
  'q': 'OOOOO.', 'r': 'O.OOO.',
  's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO',
  'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO',
}

space_to_braille = {
    ' ': '......'  # Space
}

special_symbols_to_braille = {
    'capital': '.....O',  # Capitalization marker
    'number': '.O.OOO',   # Number follows marker
    'decimal': '.O...O',  # Decimal follows marker
}

numbers_to_braille = {
# Numbers 0-9 (Braille numbers follow the letters a-j)
  '1': 'O.....', '2': 'O.O...',
  '3': 'OO....', '4': 'OO.O..',
  '5': 'O..O..', '6': 'OOO...',
  '7': 'OOOO..', '8': 'O.OO..',
  '9': '.OO...', '0': '.OOO..',
}

punctuation_to_braille = {
    
    # Punctuation
  ',': '..O...',  # Comma
  ';': '..O.O.',  # Semicolon
  ':': '..OO..',  # Colon
  '.': '..OO.O',  # Period
  '!': '..OOO.',  # Exclamation mark
  '?': '..O.OO',  # Question mark
  '-': '....OO',  # Hyphen
  '(': 'O.O..O',  # Opening parenthesis
  ')': '.O.OO.',  # Closing parenthesis
  "<": '.OO..O',  # Arrow Left
  '>': 'O..OO.',  # Arrow Right
  '/': '.O..O.',  # Slash
}
# Reverse mapping from above dictionaries
letters_from_braille = {v: k for k, v in english_to_braille.items()}
numbers_from_braille = {v: k for k, v in numbers_to_braille.items()}
punctuation_from_braille = {v: k for k, v in punctuation_to_braille.items()}
special_symbols_from_braille = {v: k for k, v in special_symbols_to_braille.items()}
space_from_braille = {v: k for k, v in space_to_braille.items()}

# Detect whether the input is Braille or English
def detect_input_type(input_str):
    if all(char in 'O.' for char in input_str):
        return 'braille'
    else:
        return 'english'

# Translate from English to Braille
def translate_to_braille(text):
    result = []
    number_mode = False  # Tracks if we are in a number sequence

    for char in text:
        if char.isupper():
            # Add the capitalization marker before the uppercase letter
            result.append(special_symbols_to_braille['capital'])
            char = char.lower()  # Convert to lowercase to find the correct mapping

        if char.isdigit():
            if not number_mode:
                # Add the number marker before the first digit
                result.append(special_symbols_to_braille['number'])
                number_mode = True
            result.append(numbers_to_braille[char])
        else:
            if char in punctuation_to_braille and number_mode == True:
                # Add decimal marker and decimal if number
                result.append(special_symbols_to_braille['decimal'])
                result.append(punctuation_to_braille['.'])
            
            elif char in english_to_braille:
                number_mode = False
                result.append(english_to_braille[char])
            elif char in punctuation_to_braille:
                number_mode = False
                result.append(punctuation_to_braille[char])
            elif char == ' ':
                number_mode = False
                result.append(space_to_braille[char])
            else:
                number_mode = False
                result.append('')  # Handle any unexpected input

    return ''.join(result)

# Translate from Braille to English
def translate_to_english(braille):
    result = []
    i = 0
    length = len(braille)
    capital_mode = False
    number_mode = False
    decimal_mode = False

    while i < length:
        braille_char = braille[i:i+6] # Chunk of characters representing one braille symbol

        if braille_char in special_symbols_from_braille:
            # Different modes depending on conditions
            if special_symbols_from_braille[braille_char] == 'capital':
                capital_mode = True
            elif special_symbols_from_braille[braille_char] == 'number':
                number_mode = True
            elif special_symbols_from_braille[braille_char] == 'decimal':
                decimal_mode = True
            i += 6
            continue

        if number_mode:
            # Prints number
            if braille_char in numbers_from_braille:
                char = numbers_from_braille[braille_char]
            elif braille_char == '..OO.O' and decimal_mode == True:
                # Prints decimal within number
                char = '.'
            elif braille_char  == '......':
                # Space; turns off number mode
                number_mode = False  # Exit number mode if the character isn't a number
                char = space_from_braille.get(braille_char, ' ')
        else:
            if braille_char in letters_from_braille:
                char = letters_from_braille[braille_char]
            elif braille_char in punctuation_from_braille:
                char = punctuation_from_braille[braille_char]
            elif braille_char in space_from_braille:
                char = space_from_braille[braille_char]
            else:
                char = ''  # Handle any unexpected input

        if capital_mode:
            char = char.upper()
            capital_mode = False

        result.append(char)
        i += 6

    return ''.join(result)

# Main function to run the translator
def main():
    if len(sys.argv) < 2:
        # Error handling
        print("Usage: python translator.py Enter text")
        sys.exit(1)

    args = sys.argv[1:]
    # Join the arguments with a space
    input_str = " ".join(args)

    
    if detect_input_type(input_str) == 'english':
        braille_translation = translate_to_braille(input_str)
        print(braille_translation, end='')
    else:
        english_translation = translate_to_english(input_str)
        print(english_translation, end='')

if __name__ == "__main__":
    main()
