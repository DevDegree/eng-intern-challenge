import sys
from braille_map import braille_map, reverse_braille_map, braille_follows_symbols, special_symbols

def translate_to_braille(text):
    braille_output = []
    number_mode = False  # Track if we are in number mode

    for char in text:
        if char.isupper():
            # Capital letter: add capital sign and corresponding lowercase Braille character
            braille_output.append(braille_follows_symbols['capitalSign'])
            braille_output.append(braille_map[char.lower()])
            number_mode = False  # Exit number mode
        elif char.isdigit():
            if not number_mode:
                # Add number sign before the first number in sequence
                braille_output.append(braille_follows_symbols['numberSign'])
                number_mode = True  # Enter number mode
            braille_output.append(braille_map[char])
        elif char == '.':
            if number_mode:
                # Decimal point: add decimal sign if in number mode
                braille_output.append(braille_follows_symbols['decimalSign'])
            else:
                # Regular period (.)
                braille_output.append(braille_map[char])
        elif char in special_symbols:
            braille_output.append(braille_map[char])
            number_mode = False  # Reset number mode on space
        elif char in braille_map:
            # Regular lowercase letter or punctuation
            braille_output.append(braille_map[char])

    return ''.join(braille_output)


def translate_to_english(braille_text):
    english_output = []
    number_mode = False   # Flag to indicate if we are in number mode
    capital_mode = False  # Flag to indicate if the next letter should be capitalized

    # Process the input Braille text in chunks of six characters
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    for braille_char in braille_chars:
        if braille_char == braille_follows_symbols['numberSign']:
            # Enter number mode
            number_mode = True
        elif braille_char == braille_follows_symbols['capitalSign']:
            # Enter capital mode
            capital_mode = True
        elif braille_char == braille_follows_symbols['decimalSign']:
            if number_mode:
                # Append a decimal point if in number mode
                english_output.append('.')
        elif braille_char in reverse_braille_map:
            # Fetch the correct translation depending on number mode
            if number_mode:
                # Translate as a digit in number mode
                translated_char = reverse_braille_map[braille_char].get('digit', '')
                if not translated_char:
                    number_mode = False
                    # Translate as a letter in letter mode
                    translated_char = reverse_braille_map[braille_char].get('symbol', '')
            else:
                translated_char = reverse_braille_map[braille_char].get('letter', '')
                # If it's not a letter, check if it's a symbol
                        

            if capital_mode:
                english_output.append(translated_char.upper())  # Capitalize if needed
                capital_mode = False  # Reset capital mode
            else:
                english_output.append(translated_char)

            # # Exit number mode if we encounter a non-digit character (e.g., a letter or space)
            # if number_mode and not translated_char.isdigit():
            #     print("number end")
            #     number_mode = False

    return ''.join(english_output)



# Detect if input is Braille
def is_braille(input_str):
    return all(char in ['O', '.'] for char in input_str)


def translate(input_text):
    if is_braille(input_text):
        return translate_to_english(input_text)
    else:
        return translate_to_braille(input_text)


if __name__ == "__main__":
    result = ''
    for arg in sys.argv[1:]:
        result = result + translate(arg)
    print(result)