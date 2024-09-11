import sys

# Function to load the Braille mapping from a text file
def load_braille_mapping(file_path):
    mapping = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):  # Skip empty lines and comments
                key, value = line.split("|")  # Use the pipe separator
                mapping[key] = value
    return mapping

# Reverse Braille-to-English to get English-to-Braille mapping
def reverse_braille_mapping(braille_to_mapping):
    return {v: k for k, v in braille_to_mapping.items()}

# Special Braille signs
capital_follows = ".....O"
number_follows = ".O.OOO"
space_follows = "......"
decimal_follows = ".O...O"

# Function to detect if the input is Braille or English
def detect_input_type(input_string):

    # If all characters in the input string are 'O' or '.', it's likely Braille
    if all(char in ['O', '.'] for char in input_string) and len(input_string)%6==0:
        return 'braille'
    else:
        return 'english'

# Function to translate Braille to English
def translate_braille_to_english(braille_string, letters_mapping, numbers_mapping):
    # Split the Braille input into chunks of 6 characters (each Braille cell is 6 dots)
    braille_cells = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    
    result = []
    capital_mode = False  # Track if the next letter should be capitalized
    number_mode = False   # Track if we're in number mode
    
    for cell in braille_cells:
        # Handle the capital sign (directly check for the Braille pattern)
        if cell == capital_follows:  # Checking the Braille pattern for capital sign
            capital_mode = True
            continue  # Skip processing this cell, move to the next one
        
        # Handle the number sign (directly check for the Braille pattern)
        if cell == number_follows:  # Checking the Braille pattern for number sign
            number_mode = True
            continue
        
        # Handle the decimal sign (directly check for the Braille pattern)
        if cell == decimal_follows:  # Checking the Braille pattern for decimal sign
            result.append(".")
            continue
        
        # Handle the space (directly check for the Braille pattern)
        if cell == space_follows:  # Braille pattern for space
            result.append(" ")
            number_mode = False
            continue
        
        # Convert Braille cell to English
        if number_mode:
            # Translate Braille cell to a number (using the braille_to_numbers dictionary)
            number = numbers_mapping.get(cell, "?")  # Fallback to '?' for unknown characters
            result.append(number)
            continue  # Stay in number mode until space or non-number symbol is encountered
        else:
            letter = letters_mapping.get(cell, "?")
            
            # Capitalize the letter if capital mode is active
            if capital_mode:
                result.append(letter.upper())
                capital_mode = False  # Reset capital mode after applying it to one letter
            else:
                result.append(letter)
    
    return "".join(result)

# Function to translate English to Braille
def translate_english_to_braille(english_string, letters_mapping_reverse, numbers_mapping_reverse):
    result = []
    number_mode = False  # Track if we're in number mode
    
    for char in english_string:
        
        # Handle the decimal sign (directly check for the Braille pattern)
        if char == "." and number_mode:  # Checking the Braille pattern for decimal sign
            if number_mode:
                result.append(decimal_follows)
                continue

                    
        if char.isdigit():
            # Handle numbers (prepend the number sign if we're not in number mode)
            if not number_mode:
                result.append(number_follows)
                number_mode = True
            result.append(numbers_mapping_reverse[char])
        else:
            
            if char.isalpha():
                # Handle letters (prepend the capital sign if it's uppercase)
                if char.isupper():
                    result.append(capital_follows)
                result.append(letters_mapping_reverse[char.lower()])
            elif char == ' ':
                # Handle spaces
                result.append(space_follows)

                # If a non-number is encountered, exit number mode
                if number_mode:
                    number_mode = False

            else:
                # Handle punctuation or unknown characters
                if number_mode:
                    result.append(numbers_mapping_reverse.get(char, "?"))
                else:
                    result.append(letters_mapping_reverse.get(char, "?"))
    
    return "".join(result)

# Main entry point of the script
if __name__ == "__main__":

    if len(sys.argv)==1:
        print("No input provided, exiting.")
        sys.exit(0)  # Exit the script gracefully

    # Join all the arguments into a single string (handles multiple words)
    input_string = " ".join(sys.argv[1:])

    # Load the Letters mapping from a text file
    letters_mapping = load_braille_mapping("braille_mapping_letters.txt")
    
    # Reverse the mapping for Letters to Braille translation
    letters_mapping_reverse = reverse_braille_mapping(letters_mapping)

    # Load the Letters mapping from a text file
    numbers_mapping = load_braille_mapping("braille_mapping_numbers.txt")
    
    # Reverse the mapping for Letters to Braille translation
    numbers_mapping_reverse = reverse_braille_mapping(numbers_mapping)
    
    # Detect if the input is Braille or English
    input_type = detect_input_type(input_string)
    
    if input_type == 'braille':
        # Translate Braille to English
        translated_string = translate_braille_to_english(input_string, letters_mapping, numbers_mapping)
        print(translated_string)
    else:
        # Translate English to Braille
        translated_string = translate_english_to_braille(input_string, letters_mapping_reverse, numbers_mapping_reverse)
        print(translated_string)
