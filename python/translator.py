import sys

# Braille mappings for letters and numbers
braille_letters = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",  # Space
}

braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

# Inverse dictionaries for Braille to English translation
alphabet = {v: k for k, v in braille_letters.items()}
numbers = {v: k for k, v in braille_numbers.items()}

# Upper and number indicators
upper_indicator = ".....O"
number_indicator = ".O.OOO"

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <string_to_translate>")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:])

    if is_braille(input_string):
        print(to_english(input_string))
    else:
        print(to_braille(input_string))

def is_braille(input_string):
    return all(char in ['O', '.', ' '] for char in input_string)

def to_braille(input_string):
    result = []
    for word in input_string.split():
        if result:
            result.append(braille_letters[' '])  # Add space between words
        number_mode = False  # Reset number mode for each word
        for char in word:
            if char.isupper():
                result.append(upper_indicator)
                result.append(braille_letters[char.lower()])
                number_mode = False  # Reset number mode after an uppercase letter
            elif char.isdigit():
                if not number_mode:
                    result.append(number_indicator)
                    number_mode = True
                result.append(braille_numbers[char])
            else:
                result.append(braille_letters[char])
                number_mode = False  # Reset number mode for letters

    return ''.join(result)

def to_english(braille_string):
    result = []
    i = 0
    number_mode = False  # Track if in number mode

    while i < len(braille_string):
        if braille_string[i:i + 6] == upper_indicator:
            i += 6  # Skip upper indicator
            if braille_string[i:i + 6] in alphabet:
                result.append(alphabet[braille_string[i:i + 6]].upper())
                i += 6
                continue
        
        if braille_string[i:i + 6] == number_indicator:
            number_mode = True  # Enter number mode
            i += 6
        
        # Handle numbers in number mode
        if number_mode:
            while i < len(braille_string) and braille_string[i:i + 6] != braille_letters[' ']:
                if braille_string[i:i + 6] in numbers:
                    result.append(numbers[braille_string[i:i + 6]])
                else:
                    print(f"Unknown number Braille: {braille_string[i:i + 6]}")  # Debug line
                i += 6
            number_mode = False  # Reset number mode after reading numbers
            continue

        if braille_string[i:i + 6] in alphabet:
            result.append(alphabet[braille_string[i:i + 6]])
        else:
            print(f"Unknown Braille: {braille_string[i:i + 6]}")  # Debug line
        i += 6

    return ''.join(result)

if __name__ == "__main__":
    main()
