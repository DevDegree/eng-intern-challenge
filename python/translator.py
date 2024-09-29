import sys

"""
Note: The Braille mapping for 'o' and '>' is the same, so a way to differentiate between them is needed.
I was thinking of adding a special indicator, for example, a "special character follows" in Braille,
similar to "capital follows" or "decimal follows." 
"""

# Braille mapping dictionaries
char_to_braille_mapping = {
    # Letters
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
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",

    # Space
    " ": "......",

    # Punctuation
    ".": "..OO.O",  # Period
    ",": "..O...",  # Comma
    "?": "..O.OO",  # Question Mark
    "!": "..OOO.",  # Exclamation Mark
    ":": "..OO..",  # Colon
    ";": "..O.O.",  # Semicolon
    "-": "....OO",  # Hyphen
    "/": ".O..O.",  # Slash
    "<": ".OO..O",  # Less than
    # ">": "O..OO.",  # Greater than
    "(": "O.O..O",  # Open parenthesis
    ")": ".O.OO.",  # Close parenthesis

    # Special indicators
    "capital follows": ".....O",  # Capital follows indicator
    "decimal follows": ".O...O",  # Decimal follows indicator
    "number follows": ".O.OOO"    # Number follows indicator
}

digit_to_braille_mapping = {
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
}

def english_to_braille(text):
    braille = ""
    is_number = False
    is_decimal = False

    for i, char in enumerate(text):
        if char.isupper():
            # Add the capital follows indicator and convert to lowercase
            braille += char_to_braille_mapping["capital follows"]
            char = char.lower()

        if char.isdigit():
            if not is_number:
                # Add number follows indicator at the start of numbers
                braille += char_to_braille_mapping["number follows"]
                is_number = True

            # If we're in decimal mode, add the decimal follows indicator
            if is_decimal:
                braille += char_to_braille_mapping["decimal follows"]
                is_decimal = False

            braille += digit_to_braille_mapping[char]
        
        elif char == '.':
            # If a decimal point is found, set the decimal mode flag
            is_decimal = True
        
        else:
            # Exit number mode when a non-digit character is encountered
            if is_number:
                is_number = False

            # Handle space explicitly
            if char == " ":
                braille += char_to_braille_mapping[" "]
            # Add the Braille equivalent for other characters if they exist in the mapping
            elif char in char_to_braille_mapping:
                braille += char_to_braille_mapping[char]

    return braille

def braille_to_english(braille_text):
    # Inverse mapping of char_to_braille_mapping
    braille_to_char_mapping = {value: key for key, value in char_to_braille_mapping.items()}
    braille_to_digit_mapping = {value: key for key, value in digit_to_braille_mapping.items()}

    # Split the braille text into chunks of 6 characters
    braille_chunks = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]

    english = ""
    is_number = False
    capitalize_next = False

    for chunk in braille_chunks:
        if chunk == char_to_braille_mapping["number follows"]:
            # Set number mode
            is_number = True
            continue
        
        if chunk == char_to_braille_mapping["capital follows"]:
            # Capitalize the next character
            capitalize_next = True
            continue
        
        if chunk == char_to_braille_mapping[" "]:
            # Handle space explicitly
            english += " "
            is_number = False  # Exit number mode after space
            continue

        if is_number:
            if chunk in braille_to_digit_mapping:
                english += braille_to_digit_mapping[chunk]
            elif chunk == char_to_braille_mapping["decimal follows"]:
                english += "."
            else:
                is_number = False  # Exit number mode if non-number character is found
                if chunk in braille_to_char_mapping:
                    char = braille_to_char_mapping[chunk]
                    english += char.upper() if capitalize_next else char
                    capitalize_next = False
        else:
            if chunk in braille_to_char_mapping:
                char = braille_to_char_mapping[chunk]
                # Handle capitalization
                if capitalize_next:
                    char = char.upper()
                    capitalize_next = False
                english += char

    return english


def main():
    input_text = ' '.join(sys.argv[1:])
    
    if all(char in 'O.' for char in input_text) and len(input_text) % 6 == 0:
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()
