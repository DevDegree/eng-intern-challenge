import sys

# Define English - Braille mappings
BRAILLE_ALPHABET = {
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

# Mappings from Braille to English
ENGLISH_ALPHABET = {v: k for k, v in BRAILLE_ALPHABET.items()}
ENGLISH_LETTERS = {v: k for k, v in BRAILLE_ALPHABET.items() if k.isalpha() or k == ' '}
ENGLISH_NUMBERS = {v: str(i) for i, v in enumerate(['O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..'], start=1)}

# Function to determine if the input is braille/english
def is_braille(input_text):
    return all(c in ['O', '.'] for c in input_text)

# If it is Braille, then translate Braille text to English
def braille_to_english(braille):
    eng = ''
    index= 0 
    # keep track of capital letters
    capitalize_next_one = False

    # keep track of numbers indication
    numbers_next = False

    while index <len(braille):
        # process braille in chunks of size 6
        char_b = braille[index : index + 6]

        if char_b == BRAILLE_ALPHABET['capital']:
            capitalize_next_one = True
            index += 6 
            continue

        if char_b == BRAILLE_ALPHABET['number']:
            numbers_next = True
            index += 6 
            continue

        if numbers_next:
            char = ENGLISH_NUMBERS.get(char_b, '')
            if char == ' ':
                numbers_next = False
        else:
            char = ENGLISH_LETTERS.get(char_b, '')
            if capitalize_next_one:
                char = char.upper()
                capitalize_next_one = False
        

        eng += char
        index+=6

    return eng
        

# If it is English, then translate to Braille
def english_to_braille(text):
    braille = ''
    numbers_next =  False
    
    for char in text:

        if char.isdigit():
            if not numbers_next:
                braille += BRAILLE_ALPHABET['number']
                numbers_next = True
            braille += BRAILLE_ALPHABET[char]
        # if the charcater is capitalised, then add braille capital indicator before adding that character
        else:
            numbers_next = False
            if char.isupper():
                braille += BRAILLE_ALPHABET['capital']
                char = char.lower()
            # if the next char is a number, then add a number indicator before adding the number 
            braille += BRAILLE_ALPHABET.get(char, '')# return '' if key not found

    return braille


# Entry point
def main():
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
    else:
        input_text = input("Enter text to translate: ").strip()
    
    if not input_text:
        print("Please provide a string to translate.")
        return

    # Print the result without a newline at the end
    print(english_to_braille(input_text), end='')

if __name__ == "__main__":
    main()