import sys

english_to_braille_map = {
    # TODO
}

# TODO Automatically create the Braille to English map by reversing the above map.
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}

def braille_to_english(braille_text: str) -> str:
    """Convert Braille text to English."""
    return "English translation not yet implemented."

# TODO Converts English text to Braille.
def english_to_braille(text: str) -> str:
    """Convert English text to Braille."""
    return "Braille translation not yet implemented."


# TODO Detect whether the input is Braille or English.
def is_braille(input_string: str) -> bool:
    """Detect if the input string is Braille"""
    return False #stub

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_or_braille_string>")
        return
    
    # Join all arguments (after script name) into a single string
    input_string = ' '.join(sys.argv[1:])
    
    # Decide whether the input is Braille or English
    if is_braille(input_string):
        # Convert Braille to English
        result = braille_to_english(input_string)
    else:
        # Convert English to Braille
        result = english_to_braille(input_string)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()
    