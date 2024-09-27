import sys

# Braille dictionary
 
braille_dict = {'1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    '0': '.OOO..', 'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..',
    'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O.OOOO', '(': 'O.O..O', ')': '.O.OO.', 'cap': '.....O', 'decimal': '.O...O', 'num': '.O.OOO'
}

reverse_braille_dict = {v:k for k,v in braille_dict.items()}

def translate_to_braille(text):
    if text is None:
        return "Your input is null. Please enter a valid text."

    if not isinstance(text, str):
        return "Input text must be a string."

    braille_translation = []
    num_mode = False
    for char in text:
        if char.isdigit():
            if not num_mode:
                braille_translation.append(braille_dict["num"])
                num_mode = True
            braille_translation.append(braille_dict[char])
        elif char.isalpha():
            if char.isupper():
                braille_translation.append(braille_dict["cap"])
            braille_translation.append(braille_dict[char.lower()])
            num_mode = False
        elif char == " ":
            braille_translation.append(braille_dict[" "])
            num_mode = False
    return "".join(braille_translation)

def translate_to_english(braille):
    if braille is None:
        return "Your input is null. Please enter a valid text."

    if not isinstance(braille, str):
        return "Input text must be a string."

    english_translation = []
    i = 0
    cap_next = False
    num_mode = False

    while i < len(braille):
        symbol = braille[i:i + 6]  # Extract the next 6 characters representing a Braille cell

        # Capitalization indicator
        if symbol == braille_dict["cap"]:
            cap_next = True
            i += 6
            continue

        # Number indicator
        if symbol == braille_dict["num"]:
            num_mode = True
            i += 6
            continue

        if symbol in reverse_braille_dict:
            char = reverse_braille_dict[symbol]
            # Convert 'a'-'j' to '1'-'0' when in number mode
            if num_mode and char in "abcdefghij":
                char = str(ord(char) - ord('a') + 1)
                if char == "10":
                    char = "0"
            # Exit number mode if a space is encountered or after processing the number
            if char == " ":
                num_mode = False
            if cap_next:  # Apply capitalization
                char = char.upper()
                cap_next = False

            english_translation.append(char)
        i += 6

    return "".join(english_translation)

def is_braille(input_string):
    return all(c == 'O' or c == '.' for c in input_string)

def handle_input(*args):
    if len(args) == 1 and isinstance(args[0], str):
        # Single string input
        return args[0]
    else:
        # Multiple string inputs
        combined_string = ' '.join(args)
        return combined_string

def main():
    
    if len(sys.argv) > 1:
        input_string = handle_input(*sys.argv[1:])

    if is_braille(input_string):
        print(translate_to_english(input_string))
    else:
        print(translate_to_braille(input_string))

if __name__ == "__main__":
    main()
