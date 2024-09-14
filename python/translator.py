import sys

# Dictionaries for Braille translation
alphabet_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

numbers_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

special_keys = {
    'space': '......',
    'capital': '.....O',
    'number': '.O.OOO'
}

# Reverse dictionaries for Braille-to-English translation
braille_to_alphabet = {v: k for k, v in alphabet_to_braille.items()}
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}

def is_braille_input(input_string):
    # Check if the input is Braille by ensuring:
    # - All characters are either 'O' or '.'
    # - The length of the input is a multiple of 6 (since Braille characters are 6 dots)
    # - The input contains at least one '.' to confirm it's not composed entirely of 'O's, ensuring a valid Braille pattern
    return all(char in 'O.' for char in input_string) and len(input_string) % 6 == 0 and any(char == '.' for char in input_string)

def braille_to_english(input_string):
    text = []
    i = 0
    capital_next = False
    number_next = False

    for i in range (0, len(input_string), 6):
        symbol = input_string[i:i+6]
        if symbol == special_keys['capital']:
            capital_next = True
        elif symbol == special_keys['number']:
            number_next = True
            capital_next = False
        elif symbol == special_keys['space']:
            text.append(' ')
            number_next = False
            capital_next = False
            # https://github.com/DevDegree/eng-intern-challenge/issues/1902
            # number_next = False if number_next else text.append(' ')
        else:
            if number_next and not capital_next:
                # Translate Braille to number
                text.append(braille_to_numbers.get(symbol, ''))
            else:
                # Translate Braille to alphabet
                char = braille_to_alphabet.get(symbol, '')
                if capital_next:
                    text.append(char.upper())
                else:
                    text.append(char)
            capital_next = False

    return ''.join(text)

def english_to_braille(input_string):
    braille = []
    number_mode = False

    for char in input_string:
        if char.isdigit():
            if not number_mode:
                number_mode = True
                braille.append(special_keys['number'])
            braille.append(numbers_to_braille[char]) 
        elif char == ' ':
            braille.append(special_keys['space'])
            number_mode = False
        else:
            # https://github.com/DevDegree/eng-intern-challenge/issues/1902
            # if number_mode:
            #     braille.append(special_keys['space'])
            if char.isupper():
                braille.append(special_keys['capital'])
                char = char.lower()
            braille.append(alphabet_to_braille.get(char, ''))
            number_mode = False
    return ''.join(braille)

def main():
    input_string = ' '.join(sys.argv[1:])
    output_string = braille_to_english(input_string) if is_braille_input(input_string) else english_to_braille(input_string)
    print(output_string)

if __name__ == "__main__":
    main()
