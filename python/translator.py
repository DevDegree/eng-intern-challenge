import sys

### DICTIONARIES ###

# Maps letters and punctuation to Braille patterns
char_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...",
    "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOOOO.", "q": "OOOOOO", "r": "O.OOO.",
    "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..", ";": "..O.O.",
    "-": "....OO", "/": ".O..O.", "(": "O.O..O", ")": ".O.OO.", " ": "......"
}

# Maps numbers to Braille patterns
digit_map = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionaries for Braille to English conversion
reverse_char_map = {x: y for y, x in char_map.items()}
reverse_digit_map = {x: y for y, x in digit_map.items()}

### MODE INDICATORS ###

# indicator for capital letters
caps = ".....O"

# indicator for the beginning of number sequence
nums = ".O.OOO"

### FUNCTION TO CONVERT ENGLISH TO BRAILLE ###

def convert_to_braille(english_text):
    """
    Converts English text to braille
    """
    result = []
    number_mode = False
    
    for char in english_text:
        if char.isupper():
            result.append(caps)  # Add capital letter marker
            char = char.lower()  # Convert to lowercase for mapping
        if char.isdigit():
            if not number_mode:
                result.append(nums)  # Add number marker if not in number mode
            result.append(digit_map[char])  # Convert digit to Braille
            number_mode = True  # Set number mode to True
        else:
            result.append(char_map.get(char, "......"))  # Convert character to Braille
            if char == " ":  # Reset number mode after a space
                number_mode = False
    
    return ''.join(result)

### FUNCTION TO CONVERT BRAILLE TO ENGLISH ###

def convert_from_braille(braille_text):
    """
    Converts Braille text to English.
    """
    output = []
    capital_mode = False  # Tracks if next letter should be capital
    number_mode = False  # Tracks if number mode is active
    
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]  # Extracts Braille character (6 dots)
        
        if braille_char == caps:
            capital_mode = True  # Enable capital letter mode
            continue  # Go to the next Braille character
        if braille_char == nums:
            number_mode = True  # Enable number mode
            continue  # Go to the next Braille character
        if braille_char == "......":
            output.append(" ")  # Add space
            number_mode = False  # Reset number mode after space
        elif number_mode:
            number = reverse_digit_map.get(braille_char, "?")  # Convert Braille to digit
            output.append(number)
        else:
            letter = reverse_char_map.get(braille_char, "?")  # Convert Braille to letter
            if capital_mode:
                letter = letter.upper()  # Capitalize the letter
                capital_mode = False  # Reset capital mode
            output.append(letter)
    
    return ''.join(output)

### CHECK IF INPUT IS BRAILLE ###

def is_braille(input_text):
    """
    Checks if the given input is Braille  by ensuring it consists of only
    'O' and '.'. Also checks that its length is a multiple of 6.
    """
    return set(input_text) <= {"O", "."} and len(input_text) % 6 == 0

### MAIN FUNCTION ###

def main():
    """
    Main function that handles command-line input.
    Detects if the input is Braille or English, then converts accordingly.
    """
    user_input = " ".join(sys.argv[1:])  # Combines command-line arguments into a string
    
    if is_braille(user_input):
        print(convert_from_braille(user_input))
    else:
        print(convert_to_braille(user_input))

### SCRIPT ENTRY POINT ###

if __name__ == "__main__":
    main()

'''
Thanks for reviewing my submission! I’m excited about the opportunity and look forward to discussing more during the interview.

- Shayan :D
'''
