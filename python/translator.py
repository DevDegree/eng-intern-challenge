import sys

# Mapping of English letters to Braille
alpha_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
    ' ': "......"
}
braille_to_alpha = {v: k for k, v in alpha_to_braille.items()}

num_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
}
braille_to_num = {v: k for k, v in num_to_braille.items()}

special_braille = {
    "capital": ".....O",
    "number": ".O.OOO"
}

# Check if input string is braille
def is_braille(input_string):
    return all(c in {".", "O"} for c in input_string)

# Convert between text and braille based on input
def convert(input_string, is_braille_mode):
    output = []
    previous_mode = None

    if not is_braille_mode:
        # Conversion from English to Braille
        for char in input_string:
            if char.isdigit():
                if previous_mode != "number":
                    output.append(special_braille["number"])
                output.append(num_to_braille[char])
                previous_mode = "number"
            elif char.isalpha():
                if char.isupper():
                    output.append(special_braille["capital"])
                output.append(alpha_to_braille[char.lower()])
                previous_mode = "alphabet"
            else:
                output.append(alpha_to_braille[char])
                previous_mode = None
    else:
        # Conversion from Braille to English
        for i in range(0, len(input_string), 6):
            braille_char = input_string[i:i+6]
            if braille_char == special_braille["capital"]:
                previous_mode = "capital"
            elif braille_char == special_braille["number"]:
                previous_mode = "number"
            elif braille_char == alpha_to_braille[' ']:  # Handling space
                output.append(" ")
                previous_mode = None
            else:
                if previous_mode == "capital":
                    output.append(braille_to_alpha[braille_char].upper())
                    previous_mode = None
                elif previous_mode == "number":
                    output.append(braille_to_num[braille_char])
                else:
                    output.append(braille_to_alpha[braille_char])
                    previous_mode = None

    return "".join(output)

if __name__ == "__main__":
    # Combine into a single string
    string = " ".join(sys.argv[1:])
    # Print result
    print(convert(string, is_braille(string)))