import sys


# Braille dictionary for translating English to Braille
braille_dict = {
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

# Reverse Braille dictionary for translating Braille to English (only for characters)
reverse_braille_dict_chars = {v: k for k, v in braille_dict.items() if not k.isdigit()}


# Reverse Braille dictionary for translating Braille to English (only for numbers)
reverse_braille_dict_numbers = {v: k for k, v in braille_dict.items() if k.isdigit()}

# Function to convert English text to Braille which get a string text and return a string as the result
def english_to_braille(text: str) -> str:
    braille_text = ''

    # For checking if we are reading numbers or characters
    number_mode = False

    for char in text:
        if char.isdigit() and not number_mode:
            braille_text += braille_dict['number']
            number_mode = True

        if char == ' ' and number_mode:
            number_mode = False

        if char.isupper():
            braille_text += braille_dict['capital']

        braille_text += braille_dict.get(char.lower(), '')

    return braille_text


def braille_to_english(braille: str) -> str: 
    english_text = ''

    i = 0
    while i < len(braille):

        symbol = braille[i:i+6]

        if symbol == braille_dict['capital']:
            
            # Get the next character which we know is capital
            i += 6

            symbol = braille[i:i+6]

            english_text += reverse_braille_dict_chars[symbol].upper()

        elif symbol == braille_dict['number']:

            i += 6

            # Read numbers until reached space
            while i < len(braille):

                number_symbol = braille[i:i+6]

                if number_symbol == '......':
                    break

                english_text += reverse_braille_dict_numbers[number_symbol]
                i += 6

            continue
        else:
            english_text += reverse_braille_dict_chars.get(symbol, '')

        i += 6

    return english_text


def is_braille(text: str) -> bool:
    return all(char in 'O.' for char in text)

def main():
    
    text = ' '.join(sys.argv[1:])
    
    if is_braille(text):
        print(braille_to_english(text))

    else:
        print(english_to_braille(text))



if __name__ == "__main__":
    main()
