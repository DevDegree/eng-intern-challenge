import sys
import re

braille_map = {
        'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
        'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
        'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
        'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
        'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
        'z': 'O..OOO',
        '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
        '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 'O': '.OOO..',
        ' ': '......'
    }

nextCapital = ".....O"
nextNumber = ".O.OOO"

def braille(input_strings):
    output = []
    valid_chars = r'^[a-zA-Z0-9 ]+$' # Check if the input string contains only valid characters using regex

    # If the input string contains invalid characters, raise an error
    for string in input_strings:
        if not re.match(valid_chars, string):
            raise ValueError(f"Invalid characters in input: {string}")
    
    for string in input_strings:
        currentDigit = False
        brailleParts = [] 
        # Using a list to store the braille parts of each character instead of a string because strings are immutable and lists are mutable
        for char in string:
            if char.isdigit():
                if not currentDigit: 
                    # Add the nextNumber symbol before the first digit in a series
                    brailleParts.append(nextNumber)
                    currentDigit = True
                brailleParts.append(braille_map[char])
            else:
                # Reset the currentDigit flag after processing the current character
                currentDigit = False
                if char.isupper():
                    # Add the nextCapital symbol before the braille representation of the lowercase character
                    brailleParts.append(nextCapital + braille_map[char.lower()])
                else:
                    brailleParts.append(braille_map[char.lower()])
        output.append("".join(brailleParts))
        # I append the translated string to the output list

    return braille_map[" "].join(output) # Join the translated strings with a space in braille

if __name__ == "__main__":
    inputs = sys.argv[1:]
    result = braille(inputs)
    print(result, end='')