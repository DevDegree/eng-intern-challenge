# Braille patterns for alphabet, numbers, and punctuation
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    ",": ".O....", ".": ".O.O..", "?": ".O..O.", "!": ".OO.O.", "'": "....O.", "-": "....OO"
}

braille_numbers = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Special Braille patterns
braille_capital = ".....O"
braille_number = ".O.OOO"
braille_space = "......"

# Reverse dictionary for quick lookup
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

# Enhanced feature: Additional symbols and punctuation
braille_punctuation = {",": ".O....", ".": ".O.O..", "?": ".O..O.", "!": ".OO.O.", "'": "....O.", "-": "....OO"}

reverse_braille_punctuation = {v: k for k, v in braille_punctuation.items()}

def is_braille(input_string):
    # Check if the input is braille (contains only O, ., and possibly spaces)
    return all(char in "O. " for char in input_string)

def english_to_braille(text):
    braille = []
    for char in text:
        if char == " ":
            braille.append(braille_space)
        elif char.isupper():
            braille.append(braille_capital)
            braille.append(braille_alphabet[char.lower()])
        elif char.isdigit():
            braille.append(braille_number)
            braille.append(braille_numbers[char])
        elif char in braille_punctuation:
            braille.append(braille_punctuation[char])
        else:
            braille.append(braille_alphabet.get(char, "......"))  # Handle unknown characters gracefully
    return " ".join(braille)

def braille_to_english(braille_text):
    english = []
    i = 0
    is_number_mode = False
    while i < len(braille_text):
        # Extract 6-character braille pattern
        symbol = braille_text[i:i+6]
        
        if symbol == braille_space:
            english.append(" ")
            is_number_mode = False
        elif symbol == braille_capital:
            # Capital letter follows
            i += 6
            capital_letter = reverse_braille_alphabet.get(braille_text[i:i+6], "")
            english.append(capital_letter.upper())
        elif symbol == braille_number:
            # Number mode
            is_number_mode = True
        elif is_number_mode:
            number = reverse_braille_numbers.get(symbol, "")
            english.append(number)
        elif symbol in reverse_braille_punctuation:
            punctuation = reverse_braille_punctuation[symbol]
            english.append(punctuation)
        else:
            letter = reverse_braille_alphabet.get(symbol, "")
            english.append(letter)
        
        i += 6
    
    return "".join(english)

def main():
    # Enhanced: Allow the user to choose translation direction
    print("Welcome to the Braille Translator!")
    mode = input("Choose mode: [1] English to Braille, [2] Braille to English: ")

    if mode == "1":
        input_text = input("Enter English text: ")
        translated_text = english_to_braille(input_text)
        print("\nTranslated to Braille:")
        # Enhanced: Better formatted output
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
