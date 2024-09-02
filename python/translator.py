# Dictionary to map Braille to English and vice versa
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", ".O.OOO": "number",
    "..O...": ",", "..OO.O": ".", "..O.OO": "!", "..OO..": ":", "..O.O.": ";",
    "..O..O": "-", "..O.O.": "/", "..O.OO": "(", "..OOOO": ")",
    "......": " ", "..OO.O": "?"
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

# Adding numbers (1-9 and 0 are represented as letters a-j prefixed by number indicator)
numbers_mapping = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse mapping for numbers
braille_to_numbers = {v: k for k, v in numbers_mapping.items()}

def translate_to_braille(text):
    braille_text = ''
    for char in text:
        if char.isupper():
            braille_text += english_to_braille['capital'] + english_to_braille[char.lower()]
        elif char.isdigit():
            braille_text += english_to_braille['number'] + numbers_mapping[char]
        elif char == ' ':
            braille_text += '......'  # Space in Braille
        else:
            braille_text += english_to_braille.get(char, '')  # Default to empty string if char not found
    return braille_text

def translate_to_english(braille):
    english_text = ''
    i = 0
    while i < len(braille):
        char = braille[i:i+6]
        if char == ".....O":  # Capital follows
            i += 6
            next_char = braille[i:i+6]
            english_text += braille_to_english[next_char].upper()
        elif char == ".O.OOO":  # Number follows
            i += 6
            while i < len(braille) and braille[i:i+6] != "......":  # Continue until space
                num_char = braille[i:i+6]
                english_text += braille_to_numbers[num_char]
                i += 6
        elif char == "......":  # Space
            english_text += ' '
        else:
            english_text += braille_to_english.get(char, '')  # Default to empty string if char not found
        i += 6
    return english_text

if __name__ == "__main__":
    import sys
    # Translate each argument separately and concatenate the results
    translated_texts = []

    for input_text in sys.argv[1:]:
        if set(input_text).issubset({'O', '.'}):  # This implies input is Braille
            translated_texts.append(translate_to_english(input_text))
        else:
            translated_texts.append(translate_to_braille(input_text))
    
    # Join the translated parts with Braille spaces between them
    output = "......".join(translated_texts)
    
    # Ensure the correct spacing by stripping any excess dots that may be added inappropriately
    print(output.strip('.'))