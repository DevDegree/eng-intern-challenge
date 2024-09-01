import argparse
from typing import Dict, List

# Constants
BRAILLE: str = "braille"
ENGLISH: str = "english"

# Mappings for Braille translation
letter_braille_dict: Dict[str, str] = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOOO..', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.O',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

number_braille_dict: Dict[str, str] = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

symbol_braille_dict: Dict[str, str] = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '.....OO', '/': '.O..O.', '(': 'O.O..', ')': '.O.O.O',
    '<': '.OO..', '>': '.O.O.O.', ' ': '......'
}

special_braille_dict: Dict[str, str] = {
    'CAPITAL': '.....O',  
    'DECIMAL': '.O...O',
    'NUMBER': '.O.OOO'}

# Reverse mappings for Braille-to-English translation
reverse_letter_braille_dict: Dict[str, str] = {v: k for k, v in letter_braille_dict.items()}
reverse_number_braille_dict: Dict[str, str] = {v: k for k, v in number_braille_dict.items()}
reverse_symbol_braille_dict: Dict[str, str] = {v: k for k, v in symbol_braille_dict.items()}
reverse_special_braille_dict: Dict[str, str] = {v: k for k, v in special_braille_dict.items()}

def detect_input_language(input_str: str) -> str:
    """Determine if the input string is Braille or English based on its characters."""
    return BRAILLE if set(input_str) <= {'O', '.'} else ENGLISH

def validate_input(input_str: str, input_type: str) -> bool:
    """
    Validate the input string based on the input type.
    
    Args:
    input_str (str): The input string to validate
    input_type (str): Either BRAILLE or ENGLISH
    
    Returns:
    bool: True if valid, False otherwise
    """
    if input_type == BRAILLE:
        return set(input_str) <= {'O', '.'} and len(input_str) % 6 == 0
    elif input_type == ENGLISH:
        valid_chars = set(letter_braille_dict.keys()) | set(number_braille_dict.keys()) | set(symbol_braille_dict.keys())
        return set(input_str.lower()) <= valid_chars
    return False

def english_to_braille(english_str: str) -> str:
    """
    Convert English text to Braille, handling capitalization, numbers, and punctuation.
    
    Args:
    english_str (str): The English string to convert
    
    Returns:
    str: The converted Braille string
    """
    
    braille_output: List[str] = []
    number_mode: bool = False
    was_upper: bool = False 

    for char in english_str:
        # Handle capitalization
        if char.isupper():
            if not was_upper:
                braille_output.append(special_braille_dict['CAPITAL'])
                was_upper = True
            char = char.lower()
        else:
            was_upper = False
        
        # Handle numbers and number mode
        if char.isdigit():
            if not number_mode:
                braille_output.append(special_braille_dict['NUMBER'])
                number_mode = True
            braille_output.append(number_braille_dict[char])
        else:
            if number_mode:
                number_mode = False
                
            # Translate alphabets and handle punctuation
            if char.isalpha():
                braille_output.append(letter_braille_dict[char])
            elif char == '.':
                braille_output.append(special_braille_dict['DECIMAL'] if number_mode else symbol_braille_dict[char])
            elif char in symbol_braille_dict:
                braille_output.append(symbol_braille_dict[char])
            else:
                raise ValueError(f"Invalid character: {char}")

    return ''.join(braille_output)


def braille_to_english(braille_str: str) -> str:
    """
    Convert Braille text to English.
    
    Args:
    braille_str (str): The Braille string to convert
    
    Returns:
    str: The converted English string
    
    Raises:
    ValueError: If an invalid Braille symbol is encountered
    """
    
    english_output: List[str] = []
    i: int = 0
    number_mode: bool = False
    capitalize_next: bool = False
    
    while i < len(braille_str):
        symbol = braille_str[i:i+6]
        i += 6
        
        if symbol == special_braille_dict['CAPITAL']:
            capitalize_next = True
            continue
        elif symbol == special_braille_dict['NUMBER']:
            number_mode = True
            continue
        elif symbol == special_braille_dict['DECIMAL']:
            english_output.append('.')
            continue
        
        if number_mode and symbol in reverse_number_braille_dict:
            english_output.append(reverse_number_braille_dict[symbol])
        elif symbol in reverse_letter_braille_dict:
            char = reverse_letter_braille_dict[symbol]
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english_output.append(char)
            number_mode = False
        elif symbol in reverse_symbol_braille_dict:
            english_output.append(reverse_symbol_braille_dict[symbol])
            if symbol == symbol_braille_dict[' ']:
                number_mode = False
        else:
            raise ValueError(f"Invalid Braille symbol: {symbol}")
    
    return ''.join(english_output)

def main() -> None:
    """
    Main function to handle command-line arguments and perform translation.
    """
    parser = argparse.ArgumentParser(description="Translate between English and Braille.")
    parser.add_argument('texts', nargs='+', help="Texts to translate")
    args = parser.parse_args()
    
    text_to_conv = ' '.join(args.texts)
    
    input_type = detect_input_language(text_to_conv)
    if not validate_input(text_to_conv, input_type):
        print(f"Invalid {input_type} input")
        return
    
    try:
        if input_type == BRAILLE:
            result = braille_to_english(text_to_conv)
        else:
            result = english_to_braille(text_to_conv)
        print(result)
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
