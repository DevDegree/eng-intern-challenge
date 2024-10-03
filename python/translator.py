import sys
# Braille dictionary for letters, numbers, and special symbols
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "capital": ".....O", "number": ".O.OOO", " ": "......"
}

# Inverse dictionary for translation from Braille to English
inverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(text):
    return all(char in 'O.' for char in text)

def translate_braille_to_english(braille):
    result = []
    is_capital = False
    is_number = False
    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == braille_dict["capital"]:
            is_capital = True
        elif symbol == braille_dict["number"]:
            is_number = True
        else:
            translated = inverse_braille_dict.get(symbol, "")
            if is_number:
                result.append(translated)
                is_number = False
            elif is_capital:
                result.append(translated.upper())
                is_capital = False
            else:
                result.append(translated)
    return "".join(result)

def translate_english_to_braille(english):
    result = []
    is_number = False
    for char in english:
        if char.isdigit():
            if not is_number:
                result.append(braille_dict["number"])
                is_number = True
            result.append(braille_dict[char])
        elif char.isalpha():
            if char.isupper():
                result.append(braille_dict["capital"])
            result.append(braille_dict[char.lower()])
            is_number = False
        elif char == " ":
            result.append(braille_dict[" "])
            is_number = False
    return "".join(result)

def main():
    if len(sys.argv) > 1:
        # Combine all arguments into a single string
        input_string = " ".join(sys.argv[1:])
        
        if is_braille(input_string):
            print(translate_braille_to_english(input_string))
        else:
            print(translate_english_to_braille(input_string))
    else:
        print("Please provide a string to translate.")

# Ensure the script is run directly
if __name__ == "__main__":
    main()

