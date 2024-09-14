
import sys

# Braille mappings for letters, numbers, and special symbols
braille_alphabet = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"
}

braille_capital = ".....O"  # Braille prefix for capitalization
braille_number = ".O.OOO"   # Braille prefix for numbers

# Braille for numbers (0-9 correspond to a-j with the number prefix)
braille_numbers = {
    '0': ".OOO..", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO..."
}

def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            result.append(braille_numbers[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                result.append(braille_capital)
                char = char.lower()
            result.append(braille_alphabet[char])
        elif char == ' ':
            result.append(braille_alphabet[char])
            number_mode = False  # Reset number mode on spaces
    return ''.join(result)

def braille_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_capital:
            i += 6
            char_symbol = braille[i:i+6]
            for key, value in braille_alphabet.items():
                if value == char_symbol:
                    result.append(key.upper())
                    break
        elif symbol == braille_number:
            number_mode = True
        elif symbol in braille_alphabet.values():
            for key, value in braille_alphabet.items():
                if value == symbol:
                    if number_mode:
                        for num_key, num_value in braille_numbers.items():
                            if num_value == value:
                                result.append(num_key)
                                break
                    else:
                        result.append(key)
                    break
        i += 6
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return

    input_text = ' '.join(sys.argv[1:])
    
    # Detect if the input is Braille or English
    if all(c in "O. " for c in input_text):
        # Translate Braille to English
        print(braille_to_english(input_text))
    else:
        # Translate English to Braille
        print(english_to_braille(input_text))

if __name__ == "__main__":
    main()
