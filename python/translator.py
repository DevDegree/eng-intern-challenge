import sys

# English letters to Braille mapping
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", 
    " ": ".....",  # Space in Braille
    "cap": ".....O",  # Capitalization marker
}

# Numbers to Braille mapping
numbers_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}

# Reverse mappings
braille_to_english = {v: k for k, v in english_to_braille.items()}
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}

# Detect if input is Braille or English
def is_braille(input_str):
    return all(char in "O. " for char in input_str)

# Translate Braille to English or Numbers
def braille_to_eng(braille_input):
    words = braille_input.strip().split()
    translated = []
    capital = False
    number_mode = False

    for word in words:
        if word == ".....O":
            capital = True
            continue
        elif word == ".O.OOO":  # Number indicator
            number_mode = True
            continue

        if number_mode:
            if word in braille_to_numbers:
                translated.append(braille_to_numbers[word])
            else:
                number_mode = False  # Exit number mode if no match
        else:
            if word in braille_to_english:
                letter = braille_to_english[word]
                if capital:
                    letter = letter.upper()
                    capital = False  # Exit capital mode after one letter
                translated.append(letter)

    return ''.join(translated)

# Translate English or Numbers to Braille
def eng_to_braille(english_input):
    translated = []
    number_mode = False
    last_was_space = False

    for char in english_input:
        if char.isupper():
            translated.append(".....O")  # Capitalization symbol
            char = char.lower()

        if char.isdigit():
            if not number_mode:
                translated.append(".O.OOO")  # Number indicator
                number_mode = True
            translated.append(numbers_to_braille[char])
        elif char == " ":
            translated.append("......")  # Braille space for separation
        elif char in english_to_braille:
            number_mode = False  # Exit number mode when switching back to letters
            translated.append(english_to_braille[char])
    
    return ''.join(translated)

# Main function to detect and translate
def main():
    # Join all command-line arguments into one string (e.g., "Abc 123 xYz")
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        # Translate Braille to English or Numbers
        print(braille_to_eng(input_str), end="")
    else:
        # Translate English or Numbers to Braille
        print(eng_to_braille(input_str), end="")

if __name__ == "__main__":
    main()
