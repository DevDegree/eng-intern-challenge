import sys

# Braille representation for English letters
letters_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......"
}

# Braille encoding for digits (0-9)
digits_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

capital_marker = ".....O"  # Marker for uppercase letters
number_marker = ".O.OOO"   # Marker for starting number sequence

# Reverse lookup: from Braille back to English (letters)
braille_to_letters = {v: k for k, v in letters_to_braille.items()}

# Reverse lookup: from Braille back to digits (0-9)
braille_to_digits = {v: k for k, v in digits_to_braille.items()}

# Determines whether the input string is Braille or not
def is_braille_input(input_str):
    return all(c in "O." for c in input_str.replace(" ", ""))

# Translates an English string into Braille
def english_to_braille(english_text):
    output = []
    in_number_mode = False

    for char in english_text:
        if char.isdigit():
            if not in_number_mode:
                output.append(number_marker)
                in_number_mode = True
            output.append(digits_to_braille[char])
        else:
            if in_number_mode:
                in_number_mode = False
            if char.isupper():
                output.append(capital_marker)
                char = char.lower()
            output.append(letters_to_braille.get(char, "......"))
    
    return "".join(output)

# Translates a Braille string into English
def braille_to_english(braille_text):
    result = []
    index = 0
    in_number_mode = False

    braille_text = braille_text.replace(" ", "")

    while index < len(braille_text):
        braille_char = braille_text[index:index+6]

        # Handle capital letter indicator
        if braille_char == capital_marker:
            index += 6
            braille_char = braille_text[index:index+6]
            result.append(braille_to_letters.get(braille_char, "").upper())
        
        # Handle number indicator
        elif braille_char == number_marker:
            in_number_mode = True
            index += 6
            continue
        
        # Translate regular letters or digits
        else:
            if braille_char == "......":
                result.append(" ")
                if in_number_mode:
                    in_number_mode = False
            else:
                if in_number_mode:
                    result.append(braille_to_digits.get(braille_char, ""))
                else:
                    result.append(braille_to_letters.get(braille_char, ""))
        
        index += 6 

    return "".join(result)

# Main function to handle input and output
def main():
    inputs = sys.argv[1:]
    if not inputs:
        print("No input provided")
        return
    
    input_string = ' '.join(inputs)

    if is_braille_input(input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()