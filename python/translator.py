# Braille representations using 'O' for raised dots and '.' for flat dots
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    'capital': '.....O', 'number': '.O.OOO'
}

# Reverse mapping from Braille to English
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# function to convert english to braille
def english_to_braille(text):
    braille_output = ""
    is_number = False
    for char in text:
        # checking and storing number follow indicator
        if char.isdigit() and not is_number:
            braille_output += braille_dict['number']
            is_number = True
        # checking and storing capital follow indicator
        elif char.isalpha() and char.isupper():
            braille_output += braille_dict['capital']  
            char = char.lower()
            is_number = False
        # checking and storing space
        elif char == ' ':
            is_number = False
        braille_output += braille_dict[char]
    return braille_output

# function to detect if input is Braille or English and translate accordingly
def detect_and_translate(input_string):
    # Detect if input is Braille or English based on presence of 'O' and '.' or normal letters/numbers
    if all(c in 'O.' for c in input_string):
        # translate input to English
        return "English"
    else:
        # translate input to Braille
        return english_to_braille(input_string)

if __name__ == "__main__":
    # Take the input from the command line arguments
    input_text = input("Enter the text you want to translate (English or Braille): ")
    output_text = detect_and_translate(input_text)
    print(output_text)