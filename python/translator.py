import sys

# Braille to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", 
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", ".....O": "CAPITAL", ".OO.O.": "NUMBER", "......": " "
}

# English to Braille mapping
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO", "A": ".....O O.....", "B": ".....O O.O...", " ": "......", 
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
    "9": ".OO...", "0": ".OOO.."
}

def translate_braille_to_english(braille_text):
    result = ""
    capitalize_next = False
    number_mode = False
    
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        if braille_char == ".....O":  # Capital indicator
            capitalize_next = True
            continue
        elif braille_char == ".O.OOO":  # Number indicator
            number_mode = True
            continue
        elif braille_char == "......":  # Space
            result += " "
            continue
        
        if number_mode:
            for key, value in english_to_braille.items():
                if braille_char == value:
                    result += key
                    break
            number_mode = False
        elif capitalize_next:
            result += braille_to_english[braille_char].upper()
            capitalize_next = False
        else:
            result += braille_to_english[braille_char]
    
    return result

def translate_english_to_braille(english_text):
    result = ""
    number_mode = False  # Track whether we are in number mode

    for char in english_text:
        if char.isupper():  # Handle uppercase letters with capitalization indicator
            result += ".....O"  # Capitalization indicator (no extra space)
            result += english_to_braille[char.lower()]
        elif char.isdigit():  # Handle digits
            if not number_mode:
                result += ".O.OOO"  # Apply the number indicator once before the number sequence
                number_mode = True  # Enter number mode
            result += english_to_braille[char]  # Translate the digit directly
        else:
            if number_mode:
                number_mode = False  # Exit number mode after encountering a non-digit
            result += english_to_braille[char]  # Translate normal letters or spaces
    return result



if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    
    # Determine if the input is Braille or English
    if all(c in "O." for c in input_text.replace(" ", "")):
        output = translate_braille_to_english(input_text)
    else:
        output = translate_english_to_braille(input_text)
    
    print(output)
