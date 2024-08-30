#Dictionary mapping for English to Braille translation
english_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',  #Space
    '.': '.O..OO', ',': '.O....', '?': '.OO.OO', '!': '.OOO.O', ':': '.O.OO.',
    ';': '.OO.O.', '-': '......O', '/': '......O.', '<': 'O..O..', '>': '.O...O',
    '(': 'O...OOO', ')': '.OO.OOO',
    'capital': '.....O',  #Capital letter
    'number': '.O.OOO'    #Number
}

#Braille to English translation
braille_to_english = {v: k for k, v in english_to_braille.items()}

def translate_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isupper():
            result.append(english_to_braille['capital'])
            char = char.lower()

        if char.isdigit() and not number_mode:
            result.append(english_to_braille['number'])
            number_mode = True
        elif not char.isdigit():
            number_mode = False

        braille_char = english_to_braille.get(char)
        if braille_char:
            result.append(braille_char)
        else:
            #Error if the character isn't supported
            raise ValueError(f"Character '{char}' is not in the Braille dictionary.")

    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        braille_char = braille[i:i+6]

        if braille_char == english_to_braille['capital']:
            capitalize_next = True
        elif braille_char == english_to_braille['number']:
            number_mode = True
        else:
            char = braille_to_english.get(braille_char, '')
            if capitalize_next:
                char = char.upper()
                capitalize_next = False

            if number_mode and char.isalpha():
                number_mode = False

            result.append(char)

        i += 6

    return ''.join(result)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]

    #Determine if the input is Braille or English
    if set(input_text).issubset({'O', '.'}):  #Braille to English
        print(translate_to_english(input_text))
    else:  #English to Braille
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()
