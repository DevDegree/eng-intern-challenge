# Braille alphabet mapping for lowercase letters
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......'
}

# Special Braille symbols
braille_capital = '.....O'  # Capitalization symbol
braille_number = '.O.OOO'   # Number symbol

# Number mapping
braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse mappings (Braille to English)
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_string):
    # Check if the input string contains only 'O' and '.'
    return all(c in "O." for c in input_string)

def translate_english_to_braille(text):
    braille_output = []
    number_mode = False
    
    for char in text:
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_number)
                number_mode = True
            braille_output.append(braille_numbers[char])
        elif char.isalpha():
            if number_mode:
                number_mode = False
            if char.isupper():
                braille_output.append(braille_capital)
                braille_output.append(braille_alphabet[char.lower()])
            else:
                braille_output.append(braille_alphabet[char])
        elif char == ' ':
            braille_output.append(braille_alphabet[' '])
            number_mode = False  # reset number mode on space

    return ''.join(braille_output)

def translate_braille_to_english(braille_text):
    english_output = []
    i = 0
    number_mode = False
    capitalize_next = False
    
    while i < len(braille_text):
        braille_char = braille_text[i:i+6]
        
        if braille_char == braille_capital:
            capitalize_next = True
            i += 6
            continue
        elif braille_char == braille_number:
            number_mode = True
            i += 6
            continue
        elif braille_char == braille_alphabet[' ']:
            english_output.append(' ')
            number_mode = False
        elif number_mode:
            english_output.append(reverse_braille_numbers.get(braille_char, ''))
        else:
            letter = reverse_braille_alphabet.get(braille_char, '')
            if capitalize_next:
                letter = letter.upper()
                capitalize_next = False
            english_output.append(letter)
        
        i += 6

    return ''.join(english_output)

def main():
    # Prompt the user for input
    input_string = input("Enter text or braille to translate: ")

    if is_braille(input_string):
        print("Translating Braille to English:")
        print(translate_braille_to_english(input_string))
    else:
        print("Translating English to Braille:")
        print(translate_english_to_braille(input_string))

if __name__ == "__main__":
    main()

