import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
}

NUMBER_TO_BRAILLE = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

SYMBOL_TO_BRAILLE = {
    'capital': '.....O',
    'number': '.O.OOO',
    'space': '......'
}

# Inverts the dictionarys above. 
def invert_dict(dictionary):
    return {value: key for key, value in dictionary.items()}

# Determines if the input text is Braille based on the presence of 'O.' character.
def is_braille(text):
    return all(all(c in 'O.' for c in word) for word in text)

def remove_suffix(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string


# Converts English text to Braille. 
def to_braille(text):
    braille_output = []

    # Combile all Dictionaries
    braille_lookup = {**ENGLISH_TO_BRAILLE, **NUMBER_TO_BRAILLE, **SYMBOL_TO_BRAILLE}

    for word in text:
        number_follows = False

        for symbol in word:
            if symbol.isalpha() and symbol.isupper():
                braille_output.append(braille_lookup['capital'])
            if symbol.isdigit() and not number_follows:
                braille_output.append(braille_lookup['number'])
                number_follows = True

            braille_output.append(braille_lookup[symbol.lower()])

        # Add space after each word
        braille_output.append(braille_lookup['space']) 

    # Remove trailing space
    return remove_suffix(''.join(braille_output), braille_lookup['space'])
    

def to_english(text):

    # Converts Braille text to English.
    english_output = []
    english_lookup = invert_dict(ENGLISH_TO_BRAILLE)
    number_lookup = invert_dict(NUMBER_TO_BRAILLE)
    symbol_lookup = invert_dict(SYMBOL_TO_BRAILLE)

    flattened_text = ''.join(text)

    # Create list of Braille symbols
    braille = [flattened_text[i:i+6] for i in range(0, len(flattened_text), 6)]

    # Process Braille symbols
    capital_follows = False
    number_follows = False

    for symbol in braille:
        if symbol in symbol_lookup:
            if symbol_lookup[symbol] == 'space':
                english_output.append(' ')
                number_follows = False
            elif symbol_lookup[symbol] == 'capital':
                capital_follows = True
            elif symbol_lookup[symbol] == 'number':
                number_follows = True
            continue

        # Determine letter or number output
        if number_follows:
            english_output.append(number_lookup[symbol])
        elif capital_follows:
            english_output.append(english_lookup[symbol].upper())
            capital_follows = False
        else:
            english_output.append(english_lookup[symbol])

    return ''.join(english_output)

if __name__ == '__main__':
    input_words = sys.argv[1:]
    if is_braille(input_words):
        output = to_english(input_words)
    else:
        output = to_braille(input_words)
    print(output)