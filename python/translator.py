# Braille patterns for alphabet, numbers, and punctuation
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO"
}

# Braille numbers, same pattern as letters a-j, prefixed with a number indicator
braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Braille punctuation and special symbols
braille_punctuation = {
    ",": ".O....",  # Comma
    ".": ".O.O..",  # Period
    "?": ".O..O.",  # Question mark
    "!": "..O.O.",  # Exclamation mark
    "'": "....O.",  # Apostrophe
    "-": "....OO",  # Hyphen
    ";": ".O.O..",  # Semicolon
    ":": ".O..O.",  # Colon
    "/": ".O..O.",  # Slash
    "<": "OO....",  # Less than
    ">": "OO.O..",  # Greater than
    "(": "O.OOO.",  # Left parenthesis
    ")": ".OOO..",  # Right parenthesis
    " ": "......"   # Space
}

# Special Braille indicators
braille_capital = ".....O"  # Capital letter indicator
braille_number = ".O.OOO"   # Number mode indicator

# Reverse mappings for easy lookup
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}
reverse_braille_punctuation = {v: k for k, v in braille_punctuation.items()}

def is_braille(input_string):
    """Check if the input contains only valid Braille characters."""
    return all(char in "O. " for char in input_string)

def english_to_braille(text):
    """Convert English text to Braille."""
    braille = []
    for char in text:
        if char == " ":
            braille.append(braille_punctuation[" "])
        elif char.isupper():
            braille.append(braille_capital)
            braille.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            braille.append(braille_number)
            braille.append(braille_numbers[char])
        elif char in braille_punctuation:
            braille.append(braille_punctuation[char])
        else:
            braille.append(braille_alphabet.get(char, "......"))  # Handle unknown characters
    return " ".join(braille)

def braille_to_english(braille_text):
    """Convert Braille to English."""
    english = []
    i = 0
    is_number_mode = False
    while i < len(braille_text):
        symbol = braille_text[i:i+6]
        if symbol == braille_punctuation[" "]:
            english.append(" ")
            is_number_mode = False
        elif symbol == braille_capital:
            i += 6
            capital_letter = reverse_braille_alphabet.get(braille_text[i:i+6], "")
            english.append(capital_letter.upper())
        elif symbol == braille_number:
            is_number_mode = True
        elif is_number_mode:
            number = reverse_braille_numbers.get(symbol, "")
            english.append(number)
            is_number_mode = False
        elif symbol in reverse_braille_punctuation:
            punctuation = reverse_braille_punctuation[symbol]
            english.append(punctuation)
        else:
            letter = reverse_braille_alphabet.get(symbol, "")
            english.append(letter)
        i += 6
    return "".join(english)

def main():
    """Main function to handle user interaction."""
    print("Welcome to the Braille Translator!")
    mode = input("Choose mode: [1] English to Braille, [2] Braille to English: ")

    if mode == "1":
        input_text = input("Enter English text: ")
        translated_text = english_to_braille(input_text)
        print("\nTranslated to Braille:")
        # Print Braille in groups of 6 for clarity
        for i in range(0, len(translated_text), 6):
            print(translated_text[i:i+6], end=" ")
        print()
    elif mode == "2":
        input_text = input("Enter Braille (separate characters by space): ").replace(" ", "")
        translated_text = braille_to_english(input_text)
        print("\nTranslated to English:", translated_text)
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
