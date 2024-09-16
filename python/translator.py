import sys

# Braille alphabet mappings using O for raised dots and . for flat areas
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOOOO', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'capital': '.....O',  # Capitalization indicator
    'number': '.O.OOO',   # Number indicator
}

# Reverse mappings for Braille to English
reverse_braille_dict = {
    braille_pattern: letter for letter,
    braille_pattern in braille_dict.items() if letter != 'capital' and letter != 'number'
}

# Number mappings
number_braille_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOOO..'
}

# Reverse mappings for Braille to Numbers
reverse_number_braille_dict = {
    braille: number for number,
    braille in number_braille_dict.items()
}

# Function to get input from command-line arguments
def get_input():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)
    return ' '.join(sys.argv[1:])  # Join arguments to handle multi-word inputs

# Function to determine if the input is Braille
def is_braille(input_text):
    return all(char in 'O. ' for char in input_text)

# Function to translate English to Braille
def translate_to_braille(text):
    braille_output = ''
    number_mode = False

    for char in text:
        if char.isdigit():  # Handle numbers
            if not number_mode:
                braille_output += braille_dict['number']  # Prefix for numbers
                number_mode = True
            braille_output += number_braille_dict[char]
        else:
            if char.isalpha():  # Handle letters
                if number_mode:
                    braille_output += braille_dict[' ']  # Reset after numbers
                    number_mode = False
                if char.isupper():  # Handle capitalization
                    braille_output += braille_dict['capital']
                braille_output += braille_dict[char.lower()]
            elif char == ' ':  # Handle spaces
                braille_output += braille_dict[' ']
                number_mode = False  # Reset number mode after space

    return braille_output

# Function to translate Braille to English
def translate_to_english(braille_text):
    english_output = ''
    braille_chars = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    number_mode = False
    capitalize_next = False

    for braille_char in braille_chars:
        if braille_char == braille_dict['capital']:  # Handle capital letter
            capitalize_next = True
        elif braille_char == braille_dict['number']:  # Handle number mode
            number_mode = True
        elif braille_char == '......':  # Space
            english_output += ' '
            number_mode = False
        else:
            if number_mode:
                english_output += reverse_number_braille_dict.get(braille_char, '')
                number_mode = False  # Reset after using number mode
            else:
                letter = reverse_braille_dict.get(braille_char, '')
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                english_output += letter

    return english_output

# Main function to handle input and perform translation
def main():
    input_text = get_input()
    if is_braille(input_text):
        translated_text = translate_to_english(input_text)
    else:
        translated_text = translate_to_braille(input_text)

    print(translated_text)

# Ensure main function runs when the script is executed
if __name__ == "__main__":
    main()