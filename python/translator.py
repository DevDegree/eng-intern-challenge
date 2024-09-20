import sys

#Dictionaires for Braille
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

braille_special = {
    'capital': '.....O',
    'number': '.O.OOO'
}

# Reverse dictionaires
english_alphabet = {v: k for k, v in braille_alphabet.items()}
english_numbers = {v: k for k, v in braille_numbers.items()}

# Function checks to see if input is Braille
def is_braille(input_str):
    return all(char in "O." for char in input_str)

#Translates Braille to English
def english_to_braille(input_str):
    braille_output = []
    in_number_mode = False
    for char in input_str:
        if char.isalpha():
            if char.isupper():
                braille_output.append(braille_special['capital'])
                char = char.lower()
            braille_output.append(braille_alphabet[char])
            in_number_mode = False
        elif char.isdigit():
            if not in_number_mode:
                braille_output.append(braille_special['number'])
                in_number_mode = True
            braille_output.append(braille_numbers[char])
        elif char == ' ':
            braille_output.append(braille_alphabet[' '])
            in_number_mode = False
    return ''.join(braille_output)

#Translates English to Braille
def braille_to_english(input_str):
    english_output = []
    i=0
    in_number_mode = False
    while i < len(input_str):
        if input_str[i:i + 6] == braille_special['capital']:
            next_char = input_str[i + 6:i + 12]
            english_output.append(english_alphabet[next_char].upper())
            i += 12
        elif input_str[i:i + 6] == braille_special['number']:
            in_number_mode = True
            i += 6
        else:
            current_char = input_str[i:i + 6]
            if in_number_mode:
                english_output.append(english_numbers[current_char])
            else:
                english_output.append(english_alphabet[current_char])
            in_number_mode = False
            i += 6
    return ''.join(english_output)

#Handling the command-line input and translation output

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])


    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()







