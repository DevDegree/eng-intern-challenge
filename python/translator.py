# Braille alphabet mappings for English letters
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "CAP", ".OOO..": "NUM", "......": " ", 
    
    ".O....": "-",  
    
}

english_to_braille = {v: k for k, v in braille_to_english.items()}  

# Number mappings (1-0 in Braille are the same as a-j but preceded by NUM symbol)
english_to_braille.update({"1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
                           "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..",
                           "9": ".OO...", "0": ".OOO.."})

def translate_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isdigit() and not is_number:
            result.append(english_to_braille["NUM"])
            is_number = True
        if char.isalpha() and char.isupper():
            result.append(english_to_braille["CAP"])
        if char == ' ':
            is_number = False
        #Case for unsupported characters
        braille_char = english_to_braille.get(char.lower(), "......")  # space for unsupported
        result.append(braille_char)
    return ''.join(result)

def translate_to_english(braille):
    result = []
    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    is_number = False
    is_capital = False
    for braille_char in braille_chars:
        if braille_char == "NUM":
            is_number = True
        elif braille_char == "CAP":
            is_capital = True
        else:
            if is_number:
                result.append(braille_to_english.get(braille_char, "?"))  # Use "?" for unknown Braille
                is_number = False
            elif is_capital:
                result.append(braille_to_english.get(braille_char, "?").upper())
                is_capital = False
            else:
                result.append(braille_to_english.get(braille_char, "?"))
    return ''.join(result)

def main(input_str):
    if "O" in input_str or "." in input_str:
        # Assume it's Braille
        print(translate_to_english(input_str))
    else:
        # Assuming it is in English
        print(translate_to_braille(input_str))

if __name__ == "__main__":
    import sys
    input_str = sys.argv[1] if len(sys.argv) > 1 else ""
    main(input_str)

def translate_to_braille(text):
    result = []
    is_number = False
    for char in text:
        if char.isdigit() and not is_number:
            result.append(english_to_braille["NUM"])
            is_number = True
        if char.isalpha() and char.isupper():
            result.append(english_to_braille["CAP"])
        if char == ' ':
            is_number = False  # Reset number flag after a space
        # Handle unsupported characters
        braille_char = english_to_braille.get(char.lower(), "......")
        result.append(braille_char)
    
    print("Braille output: ", ''.join(result))  # Add this for debugging
    return ''.join(result)
