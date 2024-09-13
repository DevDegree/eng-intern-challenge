import sys

# Braille to English dictionary
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    "......": " ",  # Space
    ".....O": "cap",  # Capital letter indicator
    ".O.OOO": "num"   # Number indicator
}

# English to Braille dictionary
english_to_braille = {v: k for k, v in braille_to_english.items() if v != "cap" and v != "num"}

# Number to Braille mapping (number starts with the 'num' sign)
number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Braille to number reverse mapping
braille_to_number = {v: k for k, v in number_to_braille.items()}

def translate_braille_to_english(braille_input):
    words = braille_input.strip().split(' ')
    output = ""
    is_capital = False
    is_number = False

    for word in words:
        if word == ".....O":  # Capitalization marker
            is_capital = True
        elif word == ".O.OOO":  # Number marker
            is_number = True
        elif is_number:
            output += braille_to_number.get(word, "")
            is_number = False
        else:
            letter = braille_to_english.get(word, "")
            if is_capital:
                letter = letter.upper()
                is_capital = False
            output += letter
    
    return output

def translate_english_to_braille(english_input):
    output = []
    for char in english_input:
        if char.isupper():
            output.append(".....O")  # Capital marker
            output.append(english_to_braille[char.lower()])
        elif char.isdigit():
            output.append(".O.OOO")  # Number marker
            output.append(number_to_braille[char])
        else:
            output.append(english_to_braille.get(char, "......"))  # Default to space if not found
    
    return ' '.join(output)

def is_braille(input_string):
    return all(c in 'O. ' for c in input_string)

def main():
    # Input provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        return
    
    input_string = sys.argv[1]
    
    if is_braille(input_string):
        # Translate from Braille to English
        print(translate_braille_to_english(input_string))
    else:
        # Translate from English to Braille
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()