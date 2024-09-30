import sys

# Braille to English dictionary
braille_to_english = {
    "O.....": "a", 
    "O.O...": "b", 
    "OO....": "c", 
    "OO.O..": "d", 
    "O..O..": "e", 
    "OOO...": "f", 
    "OOOO..": "g", 
    "O.OO..": "h", 
    ".OO...": "i", 
    ".OOO..": "j",
    "O...O.": "k", 
    "O.O.O.": "l", 
    "OO..O.": "m", 
    "OO.OO.": "n", 
    "O..OO.": "o", 
    "OOO.O.": "p", 
    "OOOOO.": "q", 
    "O.OOO.": "r", 
    ".OO.O.": "s", 
    ".OOOO.": "t",
    "O...OO": "u", 
    "O.O.OO": "v", 
    ".OOO.OO": "w", 
    "OO..OO": "x", 
    "OO.OOO": "y", 
    "O..OOO": "z",
    "......": " ",  # Space
}


# English to Braille dictionary
english_to_braille = {
    "a": "O.....", 
    "b": "O.O...", 
    "c": "OO....", 
    "d": "OO.O..", 
    "e": "O..O..", 
    "f": "OOO...", 
    "g": "OOOO..", 
    "h": "O.OO..", 
    "i": ".OO...", 
    "j": ".OOO..",
    "k": "O...O.", 
    "l": "O.O.O.", 
    "m": "OO..O.", 
    "n": "OO.OO.", 
    "o": "O..OO.", 
    "p": "OOO.O.", 
    "q": "OOOOO.", 
    "r": "O.OOO.", 
    "s": ".OO.O.", 
    "t": ".OOOO.",
    "u": "O...OO", 
    "v": "O.O.OO", 
    "w": ".OOO.OO", 
    "x": "OO..OO", 
    "y": "OO.OOO", 
    "z": "O..OOO",
    " ": "......",  
}

# Correct Braille representation for numbers
number_to_braille = {
    "1": "O.....",  # Adjusted based on your notation for "1"
    "2": "O.O...",  # Correct for "2"
    "3": "OO....",  # Adjusted for "3"
    "4": "OO.O...",  # Correct for "4"
    "5": "O..O..",  # Correct for "5"
    "6": "OOO...",  # Correct for "6"
    "7": "OOOO..",  # Correct for "7"
    "8": "O.OO..",  # Correct for "8"
    "9": ".OO...",  # Correct for "9"
    "0": ".OOO.."   # Correct for "O"
}



def is_braille(input_str):
    # Check if input contains only O and .
    return all(char in ['O', '.'] for char in input_str)

def braille_to_english_converter(braille_str):
    result = ""
    # Split Braille string into 6-character blocks
    blocks = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    is_capital = False
    is_number = False
    
    for block in blocks:
        if block == ".....O":
            is_capital = True
        elif block == ".....OO":
            is_number = True
        elif block in braille_to_english:
            letter = braille_to_english[block]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            result += letter
    return result

def english_to_braille_converter(english_str):
    result = ""
    is_number = False  # Track if we're converting numbers

    for char in english_str:
        # Handle spaces explicitly
        if char == " ":
            result += "......"  # Space in Braille
            is_number = False  # Reset number mode after a space
            continue

        # Handle digits (numbers)
        if char.isdigit():
            if not is_number:
                result += ".O.OOO"  # Number follows symbol (once before the number sequence)
                is_number = True
            result += number_to_braille[char]  # Use the Braille number map
        else:
            # Reset number mode after switching back to letters
            if is_number:
                is_number = False

            # Handle uppercase letters
            if char.isupper():
                result += ".....O"  # Capital follows symbol
                result += english_to_braille[char.lower()]
            else:
                # Handle lowercase letters
                result += english_to_braille[char]

    return result


def main():
    # Get the input string
    input_str = " ".join(sys.argv[1:])
    
    # Determine if input is English or Braille
    if is_braille(input_str):
        print(braille_to_english_converter(input_str))
    else:
        print(english_to_braille_converter(input_str))

if __name__ == "__main__":
    main()

