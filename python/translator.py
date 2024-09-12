import sys

# Braille dictionary for translation
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "......": " ",  # space
}

numbers_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OOO..", "0": ".OO.O."
}

english_to_braille = {v: k for k, v in braille_to_english.items()}

# Special characters
braille_capital = ".....O"
braille_number = ".O.OOO"  # Braille number sign

def translate_braille_to_english(braille):
    i = 0
    result = []
    capitalize_next = False
    number_mode = False
    
    while i < len(braille):
        if braille[i:i + 6] == braille_capital:
            capitalize_next = True
            i += 6
        elif braille[i:i + 6] == braille_number:
            number_mode = True
            i += 6
        else:
            char = braille_to_english.get(braille[i:i + 6], "")
            if number_mode and char in "abcdefghij":
                num_char = "1234567890"[list(braille_to_english.keys()).index(braille[i:i + 6])]
                result.append(num_char)
            else:
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                result.append(char)
                number_mode = False
            i += 6
    
    return "".join(result)

def translate_english_to_braille(text):
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(braille_number)
                number_mode = True
            braille_char = numbers_to_braille[char]
            result.append(braille_char)
        elif char.isupper():
            result.append(braille_capital)
            braille_char = english_to_braille[char.lower()]
            result.append(braille_char)
            number_mode = False
        elif char == " ":
            result.append("......")
            number_mode = False
        else:
            braille_char = english_to_braille[char]
            result.append(braille_char)
            number_mode = False
    
    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    # Join all arguments to form the complete input text
    input_text = " ".join(sys.argv[1:])

    if all(c in "O." for c in input_text):
        # Braille to English
        output_text = translate_braille_to_english(input_text)
    else:
        # English to Braille
        output_text = translate_english_to_braille(input_text)
    
    print(output_text)

if __name__ == "__main__":
    main()
