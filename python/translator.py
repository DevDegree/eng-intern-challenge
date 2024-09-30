import sys

# Braille representations (6-character strings)
braille_dict = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
    'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
    'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO", 'z': "O..OOO",
    '0': ".OOO..", '1': "O.....", '2': "O.O...", '3': "OO....",
    '4': "OO.O..", '5': "O..O..", '6': "OOO...", '7': "OOOO..",
    '8': "O.OO..", '9': ".OOO."
}

number_sign = ".O.OOO"
space_sign = "......"
capital_sign = ".....O"

braille_to_english_dict = {v: k for k, v in braille_dict.items()}

# Function to translate a string to Braille
def translate_to_braille(input_string):
    braille_output = ""
    is_number_mode = False
    
    for char in input_string:
        if char == ' ':
            braille_output += space_sign
            is_number_mode = False
            continue
        
        if char.isdigit():
            if not is_number_mode:
                braille_output += number_sign
                is_number_mode = True
            braille_output += braille_dict[char]
        elif char.isalpha():
            if is_number_mode:
                is_number_mode = False

            if char.isupper():
                braille_output += capital_sign 
                braille_output += braille_dict[char.lower()]
            else:
                braille_output += braille_dict[char]
        else:
            continue
    
    return braille_output

def translate_to_english(braille_string):
    english_output = ""
    braille_chars = [braille_string[i:i + 6] for i in range(0, len(braille_string), 6)]

    is_number_mode = False
    for braille_char in braille_chars:
        if braille_char == space_sign:
            english_output += ' ' 
            is_number_mode = False
            continue

        if braille_char in braille_to_english_dict:
            translated_char = braille_to_english_dict[braille_char]
            if translated_char.isdigit():
                if not is_number_mode:
                    is_number_mode = True
            else:
                is_number_mode = False
            
            english_output += translated_char
        else:
            continue  

    return english_output

# Main execution
if __name__ == "__main__":

    input_string = " ".join(sys.argv[1:])  

    if all(char in "O." for char in input_string.replace(" ", "")):
        translated = translate_to_english(input_string).strip()
    else:
        translated = translate_to_braille(input_string).strip()

    print(translated)
