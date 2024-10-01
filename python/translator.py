import sys

# Braille representation
BRAILLE_ALPHABET = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"
}

BRAILLE_NUMBERS = {
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"

def is_braille(text):
    # Check if the text consists only of 'O', '.', and ' ' (space)
    return all(c in 'O. ' for c in text)

def english_to_braille(text):
    translated_text = ""
    in_number_mode = False

    for char in text:
        if 'A' <= char <= 'Z':
            # Capital letter
            translated_text += BRAILLE_CAPITAL_FOLLOWS + BRAILLE_ALPHABET[char.lower()]
        elif 'a' <= char <= 'z':
            # Lowercase letter
            translated_text += BRAILLE_ALPHABET[char]
        elif '0' <= char <= '9':
            # Number
            if not in_number_mode:
                translated_text += BRAILLE_NUMBER_FOLLOWS
                in_number_mode = True
            translated_text += BRAILLE_NUMBERS[char]
        elif char == ' ':
            # Space
            translated_text += BRAILLE_ALPHABET[' ']
            in_number_mode = False
        else:
            raise ValueError(f"Unknown character: {char}")
    return translated_text

def braille_to_english(braille):
    translated_text = ""
    index = 0
    in_number_mode = False

    while index < len(braille):
        letter = braille[index:index + 6]

        if letter == BRAILLE_CAPITAL_FOLLOWS:
            # Next letter is capitalized
            next_letter = braille[index + 6:index + 12]
            for key, value in BRAILLE_ALPHABET.items():
                if value == next_letter:
                    translated_text += key.upper()
                    break
            index += 12  # Skip over capital follows and the capital letter
        elif letter == BRAILLE_NUMBER_FOLLOWS:
            in_number_mode = True
            index += 6
        elif letter == BRAILLE_ALPHABET[' ']:
            translated_text += ' '
            in_number_mode = False
            index += 6
        else:
            if in_number_mode:
                for num, braille_num in BRAILLE_NUMBERS.items():
                    if braille_num == letter:
                        translated_text += num
                        break
            else:
                for char, braille_char in BRAILLE_ALPHABET.items():
                    if braille_char == letter:
                        translated_text += char
                        break
            index += 6

    return translated_text

def main():
    # Get the command-line argument (the string to translate)
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    
    # Determine if the input is Braille or English and translate accordingly
    if is_braille(text):
        translated_text = braille_to_english(text)
    else:
        translated_text = english_to_braille(text)

    # Output the translated text
    print(translated_text)

if __name__ == "__main__":
    main()
