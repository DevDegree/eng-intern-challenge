import sys
import yaml

def load_yaml_file(file_path):
    """Loads the YAML file and returns the contents"""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    
def find_input_type(input_string):
    """Determines if the input string is in English or Braille."""
    return 'braille' if all(c in ['O', '.'] for c in input_string) else 'english'

def english_to_braille(english_string, braille_map):
    """Translates from English to Braille."""
    result = ""
    is_number = False
    for char in english_string:
        if char.isupper():
            result += braille_map["CAPITAL"]
            char = char.lower()
            is_number = False
        if char.isdigit():
            if not(is_number):
                result += braille_map["NUMBER"]
            is_number = True

        # if char == '.' and is_number:
        #     result += braille_map["DECIMAL"]
        #     is_number = True # Continue number mode after a decimal point
        #     continue

        if char == ' ':
            char = "SPACE"
            is_number = False
        result += braille_map.get(char, '') 
    return result

def braille_to_english(braille_string, braille_map, reverse_braille_map):
    """Translates from Braille to English."""
    result = ""
    is_capital = False
    is_number = False

    # Split the Braille input into chunks of 6 characters (each Braille character)
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]

        # Check for control characters
        if braille_char == braille_map["CAPITAL"]:
            is_capital = True
            continue
        if braille_char == braille_map["NUMBER"]:
            is_number = True
            continue
        if braille_char == braille_map["SPACE"]:
            result += " "
            is_number = False  # Reset number state after space
            continue

        # if is_number and braille_char==braille_map["DECIMAL"]:
        #     result += "."
        #     is_number = True
        #     continue

        # Normal Braille characters
        if is_number:
            char = reverse_braille_map.get('numbers', {}).get(braille_char)
        else:
            char = reverse_braille_map.get(braille_char, '')
        if is_capital:
            char = char.upper()
            is_capital = False
        result += char
    return result


def main():
    # Load the mappings from YAML files
    braille_map = load_yaml_file('braille_map.yaml')['eng_to_braille']
    reverse_braille_map = load_yaml_file('braille_map.yaml')['braille_to_eng']

    # Read the input from the command line arguments
    input_string = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else ''

    # Determine input type and translate accordingly
    if find_input_type(input_string) == 'english':
        print(english_to_braille(input_string, braille_map))
    else:
        print(braille_to_english(input_string, braille_map, reverse_braille_map))

if __name__ == "__main__":
    main()