
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
    numberFound = False;
    
   
    for letter in wordsInput:
        if letter.isupper():    # Check for uppercase letter
            braille_translation += ".....O"  # Add capitalization indicator
            braille_translation += braille_dict[letter.lower()]  # Add lowercase letter Braille
            numberFound = False  # End number mode if applicable

        elif letter.isdigit():  # Check for numbers
            if not numberFound:
                braille_translation += ".O.OOO"  # Add number indicator
                numberFound = True  # Start number mode
            braille_translation += braille_dict[letter]  # Add the Braille digit

        elif letter == '.':  # Check for decimal point
            braille_translation += ".O...O"  # Add decimal indicator
            braille_translation += braille_dict[letter]  # Add the Braille decimal point
            numberFound = False  # End number mode after decimal point

        else:  # For lowercase letters, punctuation, or spaces
            braille_translation += braille_dict[letter]  # Add the Braille equivalent
            numberFound = False  # End number mode for non-numeric characters
    
    print(braille_translation)

wordsInput = input()

braille_translator(wordsInput)