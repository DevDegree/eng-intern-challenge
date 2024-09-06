import argparse
import sys

braille_capital_follows = '.....O'
braille_decimal_follows = '.O...O'
braille_number_follows = '.O.OOO'
brailled_space = '......'
braille_alpha_map = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z',
}
braille_num_map = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

def braille_to_english(braille_string):
    # Braille to English mapping
    
    number_mode = False
    capital_mode = False
    result = ''
    
    # Ensure the input string length is a multiple of 6
    if len(braille_string) % 6 != 0:
        raise ValueError("Input string length must be a multiple of 6")
    
    # Process the input string in chunks of 6 characters
    for i in range(0, len(braille_string), 6):
        braille_char = braille_string[i:i+6]
        
        if braille_char == braille_number_follows:
            number_mode = True
            continue
        
        if braille_char == braille_decimal_follows:
            result += '.'
            continue
        
        if braille_char == braille_capital_follows:
            capital_mode = True
            continue
        
        if braille_char == brailled_space:
            number_mode = False
            result += ' '
            continue
        
        if braille_char in braille_alpha_map:
            if number_mode:
                result += braille_num_map[braille_char]
            else:
                if capital_mode:
                    result += braille_alpha_map[braille_char].upper()
                    capital_mode = False
                else:
                    result += braille_alpha_map[braille_char]
        else:
            raise ValueError("Unknown Braille Sequence: " + braille_char)
    
    return result



def english_to_braille(text):
    # English to Braille mapping
    
    braille_capital_indicator = '.....O'
    braille_number_indicator = '.O.OOO'
    braille_decimal_indicator = '.O...O'

    alpha_to_braille = {v: k for k, v in braille_alpha_map.items()}
    num_to_braille = {v: k for k, v in braille_num_map.items()}

    result = ""
    number_mode = False

    for char in text:
        if char.isalpha():
            if number_mode:
                result += brailled_space
                number_mode = False
            
            braille_char = alpha_to_braille[char.lower()]
            if char.isupper():
                result += braille_capital_indicator
            result += braille_char

        elif char.isdigit():
            if not number_mode:
                result += braille_number_indicator
                number_mode = True
            result += num_to_braille[char]

        elif char == '.':
            result += braille_decimal_indicator
            
        elif char == ' ':
            result += brailled_space
            number_mode = False

        elif char in alpha_to_braille:
            if number_mode:
                result += brailled_space
                number_mode = False
            result += alpha_to_braille[char]

        else:
            raise ValueError("Character not supported: " + char)

    return result

def convert_braille_or_english(input_text):
    def is_braille(text):
        # Check if the input consists only of 'O' and '.' characters
        # and its length is a multiple of 6
        return all(char in 'O.' for char in text) and len(text) % 6 == 0

    if is_braille(input_text):
        return braille_to_english(input_text)
    else:
        return english_to_braille(input_text)
    
def main():
    parser = argparse.ArgumentParser(description="Convert between Braille and English text.")
    parser.add_argument("text", nargs="*", help="The text to convert. If not provided, the program will read from stdin.")
    parser.add_argument("-f", "--file", help="Input file containing the text to convert.")
    parser.add_argument("-o", "--output", help="Output file to write the converted text.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print additional information about the conversion.")

    args = parser.parse_args()

    # Get input text
    if args.file:
        with open(args.file, 'r') as file:
            input_text = file.read().strip()
    elif args.text:
        input_text = ' '.join(args.text)
    else:
        input_text = sys.stdin.read().strip()

    # Perform conversion
    output_text = convert_braille_or_english(input_text)

    # Print verbose information if requested
    if args.verbose:
        input_type = "Braille" if all(char in 'O.' for char in input_text) else "English"
        output_type = "English" if input_type == "Braille" else "Braille"
        print(f"Input type detected: {input_type}")
        print(f"Converting to: {output_type}")

    # Output result
    if args.output:
        with open(args.output, 'w') as file:
            file.write(output_text)
        if args.verbose:
            print(f"Conversion result written to {args.output}")
    else:
        print(output_text)

if __name__ == "__main__":
    main()