import sys

# Braille dictionaries for letters, numbers, and control symbols
braille_dict_mutex = {
    'CAPFLW': '.....O', 'DECFLW': '.O...O', 
    'NUMFLW': '.O.OOO', 'SPC': '......'
}

braille_dict_letters = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.',
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O....OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', ' ': '......', '.': '..O.O.',
    ',': '.O....', '?': '.O.O.O', '!': '..OO..', '-': '....O.'
}

braille_dict_numbers= {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..',
    '9': '.OO...', '0': '.OOO..',
}

# Helper function to split strings into Braille-size segments
def split_into_segments(text, n=6):
    return [text[i:i + n] for i in range(0, len(text), n)]

# Check if a string is valid Braille based on allowed characters
def is_braille(input_string):
    allowed_chars = {'O', '.'}
    segments = split_into_segments(input_string)
    return all(len(seg) == 6 and all(c in allowed_chars for c in seg) for seg in segments)

# Convert text to Braille
def text_to_braille(text):
    braille_text = ""
    using_numbers = False
    
    for char in text:
        if char.isdigit():
            if not using_numbers:
                braille_text += '.O.OOO'  # Number indicator
                using_numbers = True
        else:
            using_numbers = False

        if char.isupper():
            braille_text += '.....O'  # Uppercase indicator
            char = char.lower()  # Normalize to lowercase

        dictionary = braille_dict_numbers if using_numbers else braille_dict_letters
        braille_text += dictionary.get(char, '......')  # Get Braille or default to unknown pattern

    return braille_text

# Convert Braille to text
def braille_to_text(braille_sequence):
    text_output = ""
    using_numbers = False
    next_is_upper = False
    
    segments = split_into_segments(braille_sequence)
    
    for segment in segments:
        if segment == braille_dict_mutex['CAPFLW']:
            next_is_upper = True
            continue
        elif segment == braille_dict_mutex['NUMFLW']:
            using_numbers = True
            continue
        
        dictionary = braille_dict_numbers if using_numbers else braille_dict_letters
        for key, value in dictionary.items():
            if value == segment:
                text_output += key.upper() if next_is_upper else key
                next_is_upper = False
                break
    
    return text_output

def main():
    input_text = " ".join(sys.argv[1:])

    if not input_text:
        print("No text provided. Usage: python3 translator.py <text>")
        return

    if is_braille(input_text):
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))

if __name__ == "__main__":
    main()

