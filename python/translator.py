import sys

# Hashmap for letters
BRAILLE_HASHMAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
    'capital': '.....O', 'number': '.O.OOO',
}

# Hashmap for numbers
B_HASHMAP_NUMBERS = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
}

# invert both of the dictionaries
INVERTED_HASHMAP = {v: k for k, v in BRAILLE_HASHMAP.items() if k not in B_HASHMAP_NUMBERS}
INVERTED_B_HASHMAP_NUMBERS = {v: k for k, v in B_HASHMAP_NUMBERS.items()}


# Function to check if the input is a braille or not
def valid_braille(input_text):
    
    return all(char in {'O', '.'} for char in input_text) and len(input_text) % 6 == 0

# Function to convert from English to Braille
def translate_english_to_braille(input_text):
    translation = []
    number = False

    # Iterate over the input text
    for char in input_text:
        if char.isupper():
            # If the char is upper case append the braille equivalent code
            translation.append(BRAILLE_HASHMAP['capital'])
            translation.append(BRAILLE_HASHMAP[char.lower()])
        # If the char is a number
        elif char.isdigit():
            # Append the number braille and turn on the number Flag, if flag is already on append the braille
            if not number:
                translation.append(BRAILLE_HASHMAP['number'])
                number = True
            translation.append(B_HASHMAP_NUMBERS[char])
        elif char.isalpha():
            if number:
                number = False
            translation.append(BRAILLE_HASHMAP[char.lower()])
        else:
            translation.append(BRAILLE_HASHMAP[char])
            number = False

    return ''.join(translation)

def translate_braille_to_english(input_text):
    translation = []
    number = False

    # Process braille input in groups of 6
    i = 0
    while i < len(input_text):
        char = input_text[i:i + 6]

        # if braille code for capital
        if char == BRAILLE_HASHMAP['capital']:
            i += 6
            # Grab the next letter, capitalize and append
            if i < len(input_text):
                next_char = input_text[i:i + 6]
                translated_char = INVERTED_HASHMAP.get(next_char, '')
                translation.append(translated_char.upper())
                i += 6  
                continue 
        # if its a number code, turn on the flag
        elif char == BRAILLE_HASHMAP['number']:
            number = True
            i += 6 
            continue
        # If its a space, we can append and turn off the number flag
        elif char == BRAILLE_HASHMAP[' ']:  
            translation.append(' ')
            number = False
            i += 6
            continue
        # Else check if its a number, append or if not append the letter
        else:
            if number:
                translated_char = INVERTED_B_HASHMAP_NUMBERS.get(char, '')
                if translated_char:
                    translation.append(translated_char)
            else:
                translated_char = INVERTED_HASHMAP.get(char, '')
                translation.append(translated_char)

        i += 6

    return ''.join(translation)


def main():
    if len(sys.argv) < 2:
        print("Error: Please provide at least one string for translation.")
        return
    

    input_text = ' '.join(sys.argv[1:])

    if valid_braille(input_text):
        translated_text = translate_braille_to_english(input_text)
    else:
        translated_text = translate_english_to_braille(input_text)

    print(translated_text)

if __name__ == '__main__':
    main()