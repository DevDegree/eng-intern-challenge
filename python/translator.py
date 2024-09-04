import sys

# Braille to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ",  # Space
    ".O.OOO": "cap",  # Capital indicator
    ".OOOO": "num"   # Number indicator
}

# Number Braille mappings (same as letters a-j)
braille_numbers = {
    ".O....": "1", ".OO...": "2", ".O.O..": "3", ".O.OO.": "4", ".OOO..": "5",
    ".OOO.O": "6", ".OOOO.": "7", ".O.OO.": "8", ".OO.O.": "9", ".OOOOO": "0"
}

# Reverse mapping: English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}
english_to_braille.update({
    "1": ".O....", "2": ".OO...", "3": ".O.O..", "4": ".O.OO.", "5": ".OOO..",
    "6": ".OOO.O", "7": ".OOOO.", "8": ".O.OO.", "9": ".OO.O.", "0": ".OOOOO"
})

def is_braille(text):
    """Determine if the input text is Braille based on the characters."""
    return all(c in "O." for c in text)

def translate_braille_to_english(braille_text):
    """Translate Braille to English."""
    words = braille_text.split("......")  # Split by space (......)
    result = []
    
    for word in words:
        chars = [word[i:i+6] for i in range(0, len(word), 6)]
        translated_word = ""
        capitalize_next = False
        number_mode = False
        
        for char in chars:
            if char == ".O.OOO":  # Capital indicator
                capitalize_next = True
            elif char == ".OOOO":  # Number indicator
                number_mode = True
            else:
                if number_mode:
                    letter = braille_numbers.get(char, "")
                    number_mode = False  # Exit number mode after one digit
                else:
                    letter = braille_to_english.get(char, "")
                
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                
                translated_word += letter
        
        result.append(translated_word)

    return " ".join(result)

def translate_english_to_braille(english_text):
    """Translate English to Braille."""
    braille_text = []
    number_mode = False

    for char in english_text:
        if char.isupper():
            braille_text.append(english_to_braille['cap'])  # Capital indicator
            braille_text.append(english_to_braille[char.lower()])
        elif char.isdigit():
            if not number_mode:
                braille_text.append(english_to_braille['num'])  # Number indicator
                number_mode = True
            braille_text.append(english_to_braille[char])
        elif char == " ":
            braille_text.append("......")  # Space
            number_mode = False  # Reset number mode after space
        else:
            braille_text.append(english_to_braille[char])
            number_mode = False  # Reset number mode after any non-digit

    return "".join(braille_text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python braille_translator.py <text>")
        return

    input_text = sys.argv[1]

    if is_braille(input_text):
        print(translate_braille_to_english(input_text))
    else:
        print(translate_english_to_braille(input_text))

if __name__ == "__main__":
    main()

