"""
Harshil Chudasama
Eng Intern Challenge - Shopify
"""
import sys

class TranslationError(Exception):
    """Custom exception for translation errors."""
    pass

# Dictionary mapping Braille to English
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital", ".O.OOO": "number", "......": " ",  # Capital, number, space
}

# Braille for numbers (same symbols as a-j with number indicator)
number_to_braille = {
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Reverse dictionary to map English to Braille
english_to_braille = {v: k for k, v in braille_to_english.items() if v not in ["capital", "number", " "]}
english_to_braille.update({
    " ": "......",  # Space
    "capital": ".....O",  # Capital Braille indicator
    "number": ".O.OOO"    # Number Braille indicator
})

def translate_to_braille(text: str) -> str:
    """
    Translates English text to Braille, handling capital letters and numbers.

    Args:
        text (str): The English input text.

    Returns:
        str: The corresponding Braille output.
    """
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(english_to_braille["capital"])
            char = char.lower()
        
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille["number"])  # Number indicator
                number_mode = True  # Stay in number mode until a non-number is found
            result.append(number_to_braille[char])
        else:
            if number_mode:
                number_mode = False  # Exit number mode for non-digit characters
            if char in english_to_braille:
                result.append(english_to_braille[char])
            else:
                raise TranslationError(f"Cannot translate character: {char}")
    
    return "".join(result)

def translate_to_english(braille: str) -> str:
    """
    Translates Braille text to English, handling capital letters and numbers.

    Args:
        braille (str): The Braille input string.

    Returns:
        str: The corresponding English text.
    """
    result = []
    current_mode = None  # Tracks whether we're in 'capital' or 'number' mode

    for i in range(0, len(braille), 6):
        symbol = braille[i:i+6]
        if symbol == braille_to_english["capital"]:
            current_mode = "capital"
        elif symbol == braille_to_english["number"]:
            current_mode = "number"
        elif current_mode == "number":
            for num, braille_digit in number_to_braille.items():
                if symbol == braille_digit:
                    result.append(num)
                    break
            current_mode = None  # Exit number mode after translating the number
        elif symbol in braille_to_english:
            char = braille_to_english[symbol]
            result.append(char.upper() if current_mode == "capital" else char)
            current_mode = None  # Reset capital mode
        else:
            raise TranslationError(f"Cannot translate Braille sequence: {symbol}")
    
    return "".join(result)

def detect_input_type(input_string: str) -> str:
    """
    Detects if the input string is Braille or English.

    Args:
        input_string (str): The input text to check.

    Returns:
        str: Either 'braille' or 'english', depending on the input.
    """
    return 'braille' if all(c in "O. " for c in input_string) else 'english'

def main():
    """
    Main function to handle command-line inputs and translate accordingly.
    """
    if len(sys.argv) < 2:
        print("Error: No input provided. Please provide a string to translate.")
        sys.exit(1)

    input_string = ' '.join(sys.argv[1:]).strip()

    try:
        input_type = detect_input_type(input_string)
        if input_type == 'braille':
            print(translate_to_english(input_string))
        else:
            print(translate_to_braille(input_string))
    except TranslationError as e:
        print(f"Translation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
