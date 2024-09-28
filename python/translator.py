# Define Braille alphabet to English mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z"
}

# English to Braille mapping, reverse of above
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Special symbols for capitalization and numbers
capital_follows = ".....O"
number_follows = ".O.OOO"

def translate_braille_to_english(braille_input):
    output = []
    i = 0
    is_capital = False
    is_number = False
    
    # Split input into chunks of 6
    while i < len(braille_input):
        # Handle capital or number flags
        if braille_input[i:i+6] == capital_follows:
            is_capital = True
            i += 6
            continue
        elif braille_input[i:i+6] == number_follows:
            is_number = True
            i += 6
            continue
        
        # Read the next 6 characters for a Braille symbol
        braille_char = braille_input[i:i+6]
        i += 6
        
        # Lookup translation
        if braille_char in braille_to_english:
            char = braille_to_english[braille_char]
            if is_number:
                output.append(str(ord(char) - ord('a') + 1))  # Convert letters 'a' to 'j' to numbers
                is_number = False  # Numbers continue till a space is encountered
            else:
                if is_capital:
                    output.append(char.upper())
                    is_capital = False
                else:
                    output.append(char)
        else:
            output.append(' ')  # Handle spaces
    
    return ''.join(output)

def translate_english_to_braille(english_input):
    output = []
    for char in english_input:
        if char.isupper():
            output.append(capital_follows)
            char = char.lower()
        if char.isdigit():
            output.append(number_follows)
            # Map digit back to braille 'a' to 'j'
            output.append(english_to_braille[chr(ord('a') + int(char) - 1)])
        elif char in english_to_braille:
            output.append(english_to_braille[char])
        elif char == ' ':
            output.append('......')  # Space symbol
    return ''.join(output)

# Command-line execution logic
if __name__ == "__main__":
    import sys
    input_string = sys.argv[1]  # Get input from command-line
    
    # Determine if the input is Braille or English
    if input_string.startswith("O") or input_string.startswith("."):
        # Assuming Braille input
        print(translate_braille_to_english(input_string))
    else:
        # Assuming English input
        print(translate_english_to_braille(input_string))
