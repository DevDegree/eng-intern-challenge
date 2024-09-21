import sys

def is_braille(s):
    """
    Determines if the input string is Braille.
    Braille strings consist of 'O' and '.' characters,
    and the length should be a multiple of 6 (each Braille cell has 6 dots).
    """
    return all(c in ['O', '.'] for c in s) and len(s) % 6 == 0

def dots_to_braille_cell(raised_dots):
    """
    Converts a list of raised dot positions into a Braille cell string.
    The Braille cell is represented as a 6-character string,
    reading left to right, line by line, starting at the top left.
    Positions in the cell are mapped as follows:
    Positions: [1, 4, 2, 5, 3, 6]
    """
    # Positions in Braille cell: [1, 4, 2, 5, 3, 6]
    positions = [1, 4, 2, 5, 3, 6]
    cell = ''
    for pos in positions:
        # 'O' represents a raised dot, '.' represents no dot
        cell += 'O' if pos in raised_dots else '.'
    return cell

# Build the Braille mapping dictionaries

# Dictionary mapping letters to their corresponding raised dot positions
letters = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6],
    'capital': [6],
    'number': [3, 4, 5, 6],
    'space': []
}

# Dictionary mapping digits to their corresponding Braille letters (a-j)
numbers = {
    '1': letters['a'],
    '2': letters['b'],
    '3': letters['c'],
    '4': letters['d'],
    '5': letters['e'],
    '6': letters['f'],
    '7': letters['g'],
    '8': letters['h'],
    '9': letters['i'],
    '0': letters['j']
}

# Create Braille mapping from characters to Braille cells
braille_map = {}

# Map letters to Braille cells
for ch in letters:
    if ch not in ['capital', 'number', 'space']:
        braille_map[ch] = dots_to_braille_cell(letters[ch])

# Map digits to Braille cells
for digit in numbers:
    braille_map[digit] = dots_to_braille_cell(numbers[digit])

# Add capital sign, number sign, and space to Braille mapping
braille_map['capital'] = dots_to_braille_cell(letters['capital'])
braille_map['number'] = dots_to_braille_cell(letters['number'])
braille_map[' '] = dots_to_braille_cell(letters['space'])

# Create reverse mapping from Braille cells to characters
reverse_braille_map = {v: k for k, v in braille_map.items()}

def translate_english_to_braille(input_str):
    """
    Translates an English string into Braille representation.
    Handles capitalization and numbers according to the rules specified.
    """
    result = ''
    number_mode = False  # Flag indicating if we are in number mode
    for ch in input_str:
        if ch == ' ':
            # Add space Braille cell
            result += braille_map[' ']
            number_mode = False  # Reset number mode after space
        elif ch.isdigit():
            # If entering number mode, add number sign
            if not number_mode:
                result += braille_map['number']
                number_mode = True
            # Add Braille cell for digit
            result += braille_map[ch]
        elif ch.isalpha():
            number_mode = False  # Exit number mode when a letter is encountered
            if ch.isupper():
                # Add capital sign before uppercase letter
                result += braille_map['capital']
            # Add Braille cell for letter
            result += braille_map[ch.lower()]
        else:
            # Ignore any other characters (punctuation, etc.)
            pass
    return result

def translate_braille_to_english(input_str):
    """
    Translates a Braille string into English representation.
    Handles capitalization and numbers according to the rules specified.
    """
    result = ''
    number_mode = False  # Flag indicating if we are in number mode
    capital_flag = False  # Flag indicating the next letter should be capitalized
    i = 0
    while i < len(input_str):
        # Read the next Braille cell (6 characters)
        cell = input_str[i:i+6]
        if cell == braille_map['number']:
            number_mode = True  # Enter number mode
        elif cell == braille_map['capital']:
            capital_flag = True  # Next letter should be capitalized
        elif cell == braille_map[' ']:
            result += ' '
            number_mode = False  # Reset number mode after space
        else:
            if cell in reverse_braille_map:
                ch = reverse_braille_map[cell]
                if number_mode:
                    # Add digit to result
                    result += ch
                else:
                    # Add letter to result, capitalized if capital_flag is set
                    if capital_flag:
                        result += ch.upper()
                        capital_flag = False
                    else:
                        result += ch
            else:
                # Unrecognized Braille cell, ignore or handle as needed
                pass
        # Move to the next Braille cell
        i += 6
    return result

def main():
    """
    Main function to read input from command-line arguments,
    determine the input type, and perform the translation.
    """
    # Get input string from command-line arguments
    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        # Input is Braille, translate to English
        output = translate_braille_to_english(input_str)
    else:
        # Input is English, translate to Braille
        output = translate_english_to_braille(input_str)
    # Output the result
    print(output)

if __name__ == '__main__':
    main()