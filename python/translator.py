def main(input_string):
    if "O" in input_string or "." in input_string:
        # Treat as Braille input
        result = braille_to_english(input_string)
    else:
        # Treat as English input
        result = english_to_braille(input_string)
    
    print(result)

def braille_to_english(braille_string):
    braille_to_english_map = {
        # Add the Braille-to-English mappings here
        "O.....": "a",
        "O.O...": "b",
        # Add more mappings
    }
    
    translation = []
    capitalize_next = False
    number_mode = False
    
    # Split the input string into 6-character chunks
    braille_chars = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    
    for braille_char in braille_chars:
        if braille_char == ".....O":  # Capital marker
            capitalize_next = True
        elif braille_char == ".O.OOO":  # Number marker
            number_mode = True
        elif braille_char in braille_to_english_map:
            char = braille_to_english_map[braille_char]
            if number_mode:
                char = convert_to_number(char)  # Handle number conversion
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            translation.append(char)
    
    return ''.join(translation)

def english_to_braille(english_string):
    english_to_braille_map = {
        # Add the English-to-Braille mappings here
        "a": "O.....",
        "b": "O.O...",
        # Add more mappings
        "capital": ".....O",
        "number": ".O.OOO"
    }
    
    translation = []
    for char in english_string:
        if char.isupper():
            translation.append(english_to_braille_map["capital"])
            char = char.lower()
        if char.isdigit():
            translation.append(english_to_braille_map["number"])
            char = convert_to_braille_digit(char)
        if char in english_to_braille_map:
            translation.append(english_to_braille_map[char])
    
    return ''.join(translation)

def convert_to_number(char):
    # Map letters to numbers (Braille digits mode)
    letter_to_number_map = {
        "a": "1",
        "b": "2",
        # Add more mappings
    }
    return letter_to_number_map.get(char, char)

def convert_to_braille_digit(digit):
    # Convert a digit to its Braille representation
    digit_to_braille_map = {
        "1": "O.....",
        "2": "O.O...",
        # Add more mappings
    }
    return digit_to_braille_map.get(digit, digit)

# Example usage (replace with any test input)
test_input = "python3"  # This is an example Braille input
main(test_input)

