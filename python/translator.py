#!/usr/bin/env python3
import sys

# Braille dictionary for lowercase letters, numbers, and symbols
braille_dict = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..", "f": "OOO...", "g": "OOOO..",
    "h": "O.OO..", "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.",
    "o": "O..OO.", "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.", "u": "O...OO",
    "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO", "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..", "6": "OOO...", "7": "OOOO..",
    "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    " ": "......"
}

# Special symbols for capitalization and numbers
capital_prefix = ".....O"
number_prefix = ".O.OOO"

# Reverse lookup for Braille to English
english_dict = {v: k for k, v in braille_dict.items()}

def translate_to_braille(text):
    result = []
    is_number_mode = False
    for char in text:
        if char.isdigit():
            if not is_number_mode:
                result.append(number_prefix)
                is_number_mode = True
            result.append(braille_dict[char])
        elif char.isalpha():
            if char.isupper():
                result.append(capital_prefix)
            result.append(braille_dict[char.lower()])
            is_number_mode = False
        elif char == ' ':
            result.append(braille_dict[' '])
            is_number_mode = False
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    is_capital = False
    is_number_mode = False
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == capital_prefix:
            is_capital = True
            i += 6
            continue
        if symbol == number_prefix:
            is_number_mode = True
            i += 6
            continue
        if symbol == "......":  # Handle space in Braille
            result.append(" ")
            is_number_mode = False  # Reset number mode after space
            i += 6
            continue
        if is_number_mode and symbol in english_dict:
            result.append(str(english_dict[symbol]))
            i += 6
            continue
        if symbol in english_dict:
            letter = english_dict[symbol]
            if is_capital:
                letter = letter.upper()
                is_capital = False
            result.append(letter)
        i += 6
    return ''.join(result)

def detect_input_type(input_string):
    """ Detect if the input is Braille or English """
    # If the input contains only "O" and ".", it's Braille
    if all(c in "O." for c in input_string):
        return "braille"
    # Otherwise, we assume it's English
    return "english"

def validate_braille_input(braille):
    """ Validates that the Braille input is well-formed (length is a multiple of 6) """
    if len(braille) % 6 != 0:
        raise ValueError("Invalid Braille input: Braille must be in groups of 6 characters.")

def main():
    # Check if arguments are provided
    if len(sys.argv) < 2:
        print("Error: No input provided.")
        print("Usage: translator.py <string>")
        return

    # Combine all command-line arguments into one string
    input_string = ' '.join(sys.argv[1:])
    
    # Detect if the input is Braille or English
    input_type = detect_input_type(input_string)
    
    try:
        if input_type == "braille":
            validate_braille_input(input_string)
            result = translate_to_english(input_string)
        else:
            result = translate_to_braille(input_string)
        
        # Output the result
        print(result)
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
