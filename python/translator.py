import sys

# Mapping from Braille to English
BRAILLE_TO_ENG = {
    'O.....': 'a',    'O.O...': 'b',    'OO....': 'c',    'OO.O..': 'd',    'O..O..': 'e',
    'OOO...': 'f',    'OOOO..': 'g',    'O.OO..': 'h',    '.OO...': 'i',    '.OOO..': 'j',
    'O...O.': 'k',    'O.O.O.': 'l',    'OO..O.': 'm',    'OO.OO.': 'n',    'O..OO.': 'o',
    'OOO.O.': 'p',    'OOOOO.': 'q',    'O.OOO.': 'r',    '.OO.O.': 's',    '.OOOO.': 't',
    'O...OO': 'u',    'O.O.OO': 'v',    '.OOO.O': 'w',    'OO..OO': 'x',    'OO.OOO': 'y',
    'O..OOO': 'z',    '......': ' ',
    '.....O': 'capital next',   '.O.OOO': 'number next'
}

# Reverse mapping from English letters to Braille
ENG_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....',
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...',
    'j': '.OOO..', 'k': 'O...O.','l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.','o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.','r': 'O.OOO.',
    's': '.OO.O.','t': '.OOOO.', 'u': 'O...OO',
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO',' ': '......',
    'capital next': '.....O','number next': '.O.OOO'
}

# number mode mapping
NUM_MAPPING = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
    'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def translate_braille_to_english(braille_string):
    index = 0
    translated_text = []
    capitalize_next = False
    is_number_mode = False

    while index < len(braille_string):
        current_braille = braille_string[index:index + 6]

        # Check if the current Braille pattern is a special command
        if current_braille == ENG_TO_BRAILLE["capital next"]:
            capitalize_next = True
        elif current_braille == ENG_TO_BRAILLE['number next']:
            is_number_mode = True
        elif current_braille in BRAILLE_TO_ENG:
            character = BRAILLE_TO_ENG[current_braille]

            # Handle number mode
            if is_number_mode and character in NUM_MAPPING:
                translated_text.append(NUM_MAPPING[character])
            else:
                # Apply capitalization if needed
                if capitalize_next:
                    character = character.upper()
                    capitalize_next = False
                translated_text.append(character)

                # Reset number mode if the character is a space
                if character == ' ':
                    is_number_mode = False

        index += 6

    return ''.join(translated_text)


def convert_english_to_braille(english_text):
    braille_output = []  # List to accumulate Braille characters
    is_number_mode = False  # Indicates whether to interpret characters as numbers

    for character in english_text:
        if character.isupper():  # Handle uppercase letters
            braille_output.append(ENG_TO_BRAILLE['capital next'])
            character = character.lower()

        if character.isdigit():  # Handle digits
            if not is_number_mode:
                braille_output.append(ENG_TO_BRAILLE['number next'])
                is_number_mode = True
            # Find corresponding Braille letter for the digit
            character = next(key for key, value in NUM_MAPPING.items() if value == character)
        elif is_number_mode:
            # Exit number mode if the character is not a digit
            is_number_mode = False

        # Append the Braille representation of the character
        braille_output.append(ENG_TO_BRAILLE[character])

    return ''.join(braille_output)


def process_translation(input_text):
   
    braille_chars = {'O', '.'}
    
    # Determine if the input is Braille based on its characters
    if all(char in braille_chars for char in input_text):
        return translate_braille_to_english(input_text)
    else:
        return convert_english_to_braille(input_text)


def main():
    # Combine all command-line arguments into a single string
    command_line_input = ' '.join(sys.argv[1:])
    
    # Translate the input text based on its format
    translated_output = process_translation(command_line_input)

    # Output the translated result to the terminal
    sys.stdout.write(translated_output)
    

if __name__ == "__main__":
    main()
