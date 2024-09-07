import sys
import json

# Load the JSON file
with open('braille_mappings.json', 'r') as file:
    mappings = json.load(file)

# Extract the mappings
ENGLISH_TO_BRAILLE = mappings['ENGLISH_TO_BRAILLE']

# Dynamically create BRAILLE_TO_ENGLISH without digits to avoid repetitions
BRAILLE_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_BRAILLE.items() if not k.isdigit()}

def detect_input_type(input_str):
    # Detect if input is English or Braille
    if all(c in ['O', '.'] for c in input_str):
        return "braille"
    else:
        return "english"

def translate_to_braille(english_text):
    braille_translation = []
    capitalize_symbol = ENGLISH_TO_BRAILLE["cap"]
    number_symbol = ENGLISH_TO_BRAILLE["num"]
    previous_was_digit = False  # Flag to track if the previous character was a digit
    
    # Iterate through each character in the English text
    for char in english_text:
        if char.isalpha():
            # Reset the digit flag when encountering a letter
            previous_was_digit = False
            # Check if the character is uppercase and add the capitalize symbol if needed
            if char.isupper():
                braille_translation.append(capitalize_symbol)
                char = char.lower()
            braille_translation.append(ENGLISH_TO_BRAILLE[char])
        elif char.isdigit():
            # Add the number symbol only if the previous character wasn't a digit
            if not previous_was_digit:
                braille_translation.append(number_symbol)
                previous_was_digit = True  # Set the flag to true since current is a digit
            braille_translation.append(ENGLISH_TO_BRAILLE[char])
        elif char == ' ':
            # Reset the digit flag for spaces
            previous_was_digit = False
            # Translate spaces
            braille_translation.append(ENGLISH_TO_BRAILLE[' '])
        elif char in ENGLISH_TO_BRAILLE:
            # Handle punctuation and other special symbols
            previous_was_digit = False
            braille_translation.append(ENGLISH_TO_BRAILLE[char])
    
    # Join the list into a single string
    return ''.join(braille_translation)


def translate_to_english(braille_text):
    english_translation = []
    capitalize_next = False  # Flag to capitalize the next letter
    number_mode = False      # Flag to indicate if currently in number mode
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]  # Split into 6-char Braille cells

    for char in braille_chars:
        if char == ENGLISH_TO_BRAILLE['cap']:
            capitalize_next = True
        elif char == ENGLISH_TO_BRAILLE['num']:
            number_mode = True
        elif char == ENGLISH_TO_BRAILLE[' ']:
            english_translation.append(' ')
            number_mode = False  # Reset number mode on space
        else:
            if number_mode and char in BRAILLE_TO_ENGLISH:
                # Handle digit conversion
                letter = BRAILLE_TO_ENGLISH[char]
                digit = str(ord(letter) - ord('a') + 1) if letter != 'j' else '0'
                english_translation.append(digit)
            elif char in BRAILLE_TO_ENGLISH:
                letter = BRAILLE_TO_ENGLISH[char]
                # Capitalize if needed
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False  # Reset capitalize flag after using
                english_translation.append(letter)
                number_mode = False  # Reset number mode if a non-number char is encountered

    # Join the list into a single string
    return ''.join(english_translation)

def validate_input(input_str, dictionary, input_type):
    # Validate input based on dictionary keys
    valid_keys = set(dictionary.keys())
    if input_type == "english":
        # Check if each character is in the dictionary (including lowercase check)
        return all(char.lower() in valid_keys for char in input_str)
    # For Braille, split into 6-char segments and check each against the dictionary
    braille_chars = [input_str[i:i+6] for i in range(0, len(input_str), 6)]
    return all(char in valid_keys for char in braille_chars)

def main():
    # Check if an input string is provided
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        return

    # Combine all arguments into a single input string to ensure that the script 
    # behaves consistently whether run directly or via the test file.
    input_str = " ".join(sys.argv[1:])

    input_type = detect_input_type(input_str)

    if input_type == "english":
        dictionary = ENGLISH_TO_BRAILLE
        answer = translate_to_braille(input_str)
    else:
        dictionary = BRAILLE_TO_ENGLISH
        answer = translate_to_english(input_str)

    if not validate_input(input_str, dictionary, input_type):
        print("Invalid input: Only letters, numbers, and spaces are allowed.")
        return
    else:
        print(answer)
        
if __name__ == "__main__":
    main()
