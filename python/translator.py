import sys

# Eng to Braille
english_to_braille = {
    # Lowercase Letters
    # First 10 chars have the same mapping to digits 1-0. 
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",

    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", 
    "z": "O..OOO",

    # Special Character Markers
    "CAP": ".....O",
    "NUM": ".O.OOO",

    # Space
    " ": "......"
}

# Braille to Eng
braille_to_english = {
    # Lowercase Letters
    # First 10 chars have the same mapping to digits 1-0.
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",

    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",

    # Special Character Markers
    ".....O": "CAP",
    ".O.OOO": "NUM",

    # Space
    "......": " "
}

# Function to split a string into chunks of 6 characters (for Braille)
def split_into_chunks_of_6(s: str):
    """Splits the input string into chunks of 6 characters (Braille cell size)."""
    return [s[i:i+6] for i in range(0, len(s), 6)]


def braille_to_text(braille_string: str) -> str:
    """
    Converts a Braille-encoded string into English text.
    
    Args:
        braille_string: The input Braille string to be translated.

    Returns:
        The translated English string.
    """
    chunks = split_into_chunks_of_6(braille_string)
    translated = []
    is_capital = False
    is_numbers = False

    for chunk in chunks:
        # Handle special Braille markers for capital letters and numbers
        if braille_to_english.get(chunk) == "CAP":
            is_capital = True
            continue
        elif braille_to_english.get(chunk) == "NUM":
            is_numbers = True
            continue
        
        # Handle numbers (a-j represent 1-0)
        if is_numbers:
            letter = braille_to_english.get(chunk)
            if letter in "abcdefghij":
                number = ord(letter) - ord('a') + 1
                if letter == "j":  # Special case for 0
                    number = 0
                translated.append(str(number))
            else:
                translated.append("?")  # Unknown Braille chunk
            is_numbers = False  # Reset after processing a number
        else:
            letter = braille_to_english.get(chunk, "?")
            if is_capital:
                letter = letter.upper()
                is_capital = False  # Reset capital flag
            translated.append(letter)

    return ''.join(translated)


def text_to_braille(text_string: str) -> str:
    """
    Converts an English text string into a Braille-encoded string.
    
    Args:
        text_string: The input English text to be translated.

    Returns:
        The translated Braille string.
    """
    translated = []
    is_numbers = False

    for char in text_string:
        # Handle numbers
        if char.isdigit():
            if not is_numbers:  # Only insert the number marker once
                translated.append(english_to_braille["NUM"])
                is_numbers = True
            if char == '0':  # Special case for 0, mapped to 'j' in Braille
                translated.append(english_to_braille['j'])
            else:  # Map digits 1-9 to 'a'-'i'
                number_letter = chr(ord('a') + int(char) - 1)
                translated.append(english_to_braille[number_letter])
        else:
            is_numbers = False  # Reset numbers flag after leaving number mode
            if char.isupper():  # Handle capital letters
                translated.append(english_to_braille["CAP"])
                translated.append(english_to_braille[char.lower()])
            else:  # Handle regular lowercase letters and space
                translated.append(english_to_braille.get(char, "......"))

    return ''.join(translated)



# Main translate function. Determines whether or not input is braille or english.
def translate(input_string:str):
    if all(c in ['O', '.'] for c in input_string):  # If the input consists of only Braille characters
        return braille_to_text(input_string)
    else:
        return text_to_braille(input_string)

# Main program execution
if __name__ == "__main__":
    # Join all arguments into a single input string so you don't have to add quotes for input.
    input_string = ' '.join(sys.argv[1:])
    print(translate(input_string))
