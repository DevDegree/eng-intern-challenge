import sys

# Braille alphabet mappings for letters and numbers
braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO", 'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO.."
}

# Special symbols for capital, number mode, and space
special_symbols = {
    'capital': ".....O",
    'number': ".O.OOO",
    'space': "......"
}

def text_to_braille(text):
    braille_output = []
    num_mode = False
    
    for char in text:
        if char.isdigit():
            if not num_mode:
                braille_output.append(special_symbols['number'])
                num_mode = True
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            if num_mode:
                num_mode = False
            if char.isupper():
                braille_output.append(special_symbols['capital'])
            braille_output.append(braille_dict[char.lower()])
        elif char == ' ':
            num_mode = False
            braille_output.append(special_symbols['space'])
    
    return ''.join(braille_output)

def braille_to_text(braille_str):
    text_output = []
    num_mode = False
    i = 0
    
    while i < len(braille_str):
        braille_char = braille_str[i:i+6]
        
        if braille_char == special_symbols['space']:
            text_output.append(' ')
            num_mode = False
        elif braille_char == special_symbols['number']:
            num_mode = True
        elif braille_char == special_symbols['capital']:
            i += 6
            letter = braille_str[i:i+6]
            if letter in braille_dict.values():
                text_output.append(get_key(braille_dict, letter).upper())
        elif num_mode and braille_char in braille_dict.values():
            text_output.append(get_key(braille_dict, braille_char))
        elif braille_char in braille_dict.values():
            text_output.append(get_key(braille_dict, braille_char))
        
        i += 6
    
    return ''.join(text_output)

def get_key(dictionary, value):
    """Helper function to get the key from a dictionary based on the value."""
    for k, v in dictionary.items():
        if v == value:
            return k
    return None

def main():
    # Capture arguments from command line
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 translator.py <text_or_braille>")
        return
    
    input_text = ' '.join(args)

    # Determine if input is Braille or text based on characters
    if all(c in "O." for c in input_text.replace(' ', '')):
        # Convert Braille to text
        result = braille_to_text(input_text)
    else:
        # Convert text to Braille
        result = text_to_braille(input_text)
    
    print(result)

if __name__ == "__main__":
    main()
