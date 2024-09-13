import sys

# Braille alphabet and numbers mapping
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "CAPITAL",  # Capital letter indicator
    ".O.OOO": "NUMBER",   # Number indicator
    "......": " "        # Space
}

braille_to_english_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"
}

# Reverse map from English letters and numbers to Braille
english_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",

    ' ': "......",  # Space
    
    'CAPITAL': ".....O",  # Capital indicator
    'NUMBER': ".O.OOO"    # Number indicator
}

def is_braille(input_string):
    """ Check if the input string is Braille or English by examining its structure. """
    return all(c in 'O.' for c in input_string)

def braille_to_text(braille):
    """ Convert Braille to English text. """
    result = []
    i = 0
    capital_next = False
    number_mode = False
    
    while i < len(braille):
        char = braille[i:i+6]
        if char == ".....O":  # Capital indicator
            capital_next = True
        elif char == ".O.OOO":  # Number indicator
            number_mode = True
        else:
            if number_mode:
                symbol = braille_to_english_num[char]
                result.append(symbol)
            elif char in braille_to_english:
                symbol = braille_to_english[char]
                if symbol == " ":
                    if not number_mode:
                        result.append(" ")
                    number_mode = False  # Exit number mode after a space
                elif capital_next:
                    result.append(symbol.upper())
                    capital_next = False
                else:
                    result.append(symbol.lower())
        i += 6
    
    return ''.join(result)

def text_to_braille(text):
    """ Convert English text to Braille. """
    result = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(english_to_braille["NUMBER"])
                number_mode = True
            result.append(english_to_braille[char])
        else:
            if char.isalpha() and char.isupper():
                result.append(english_to_braille["CAPITAL"])
                result.append(english_to_braille[char.lower()])
            else:
                result.append(english_to_braille[char])
            number_mode = False  # Exit number mode if a non-number is encountered
    
    return ''.join(result)

def main():
    input_string = ' '.join(sys.argv[1:])
    
    if is_braille(input_string):
        # Convert from Braille to English
        print(braille_to_text(input_string))
    else:
        # Convert from English to Braille
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main()
