import sys

def braille_translator(wordsInput):
    braille_dict = {
        'a': "O.....",
        'b': "O.O...",
        'c': "OO....",
        'd': "OO.O..",
        'e': "O..O..",
        'f': "OOO...",
        'g': "OOOO..",
        'h': "O.OO..",
        'i': ".OO...",
        'j': ".OOO..",
        'k': "O...O.",
        'l': "O.O.O.",
        'm': "OO..O.",
        'n': "OO.OO.",
        'o': "O..OO.",
        'p': "OOO.O.",
        'q': "OOOOO.",
        'r': "O.OOO.",
        's': ".OO.O.",
        't': ".OOOO.",
        'u': "O...OO",
        'v': "O.O.OO",
        'w': ".OOO.O",
        'x': "OO..OO",
        'y': "OO.OOO",
        'z': "O..OOO",
        '1': "O.....",
        '2': "O.O...",
        '3': "OO....",
        '4': "OO.O..",
        '5': "O..O..",
        '6': "OOO...",
        '7': "OOOO..",
        '8': "O.OO..",
        '9': ".OO...",
        'O': ".OOO..",
        '.': "..OO.O",
        ',': "..O...",
        '?': "..O.OO",
        '!': "..OOO.",
        ':': "..OO..",
        ';': "..O.O.",
        '-': "....OO",
        '/': ".O..O.",
        '<': ".OO..O",
        '>': "O..OO.",
        '(': "O.O..O",
        ')': ".O.OO.",
        ' ': "......"
    }
    
    braille_translation = ""
    number_mode = False

    for letter in wordsInput:
        # Handle uppercase letters
        if letter.isupper() and not number_mode:
            braille_translation += ".....O"  # Add capital indicator
            braille_translation += braille_dict[letter.lower()]  # Add the lowercase letter Braille

        # Handle digits (in number mode)
        elif letter.isdigit():
            if not number_mode:
                braille_translation += ".O.OOO"  # Add number follows indicator
                number_mode = True  # Enter number mode
            braille_translation += braille_dict[letter]  # Add the digit's Braille

        # Handle decimal point (stay in number mode)
        elif letter == '.':
            braille_translation += ".O...O"  # Add decimal follows indicator
            braille_translation += braille_dict[letter]  # Add the Braille decimal point
            number_mode = True  # Stay in number mode

        # Handle spaces (reset number mode)
        elif letter == ' ':
            braille_translation += braille_dict[letter]  # Add space
            number_mode = False  # Reset number mode

        # Handle punctuation or lowercase letters (only if not in number mode)
        elif not number_mode:
            braille_translation += braille_dict[letter]  # Add Braille for punctuation or lowercase letters

    print(braille_translation, end='')

# Command-line interface to handle input from the command
if __name__ == "__main__":
    # Combine command-line arguments into a single string
    args = " ".join(sys.argv[1:])
    
    # Call the braille_translator function with the arguments
    braille_translator(args)