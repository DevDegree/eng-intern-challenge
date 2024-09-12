# Define Braille dictionary for letters, digits, and special symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', ' ': '......',
    'cap': '.....O', 'num': '.O.OOO',  # Capital and number prefix
    '0': '.OOOOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...' 
}

# Reverse dictionary for decoding Braille
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(input_str):
    """Determine if the input string is Braille (based on characters used)."""
    return all(c in 'O.' for c in input_str)

def braille_to_english(braille_str):
    """Convert Braille to English."""
    words = braille_str.split('......')  # split by space
    english = []
    number_mode = False
    for word in words:
        letters = [word[i:i+6] for i in range(0, len(word), 6)]
        word_result = []
        for letter in letters:
            if letter == '.....O':  # Capital letter mode
                word_result.append('CAP')
            elif letter == '.O.OOO':  # Number mode
                number_mode = True
            else:
                char = reverse_braille_dict.get(letter, '')
                if char == '':
                    continue
                if number_mode and char.isdigit():
                    word_result.append(char)
                elif 'CAP' in word_result:  # Capitalize next letter
                    word_result[-1] = reverse_braille_dict[letter].upper()
                    word_result.remove('CAP')
                else:
                    word_result.append(char)
                number_mode = False
        english.append(''.join(word_result))
    return ' '.join(english)

def english_to_braille(english_str):
    """Convert English to Braille."""
    braille = []
    for char in english_str:
        if char.isupper():  # Capitalize letter
            braille.append(braille_dict['cap'])
            braille.append(braille_dict[char.lower()])
        elif char.isdigit():  # Number handling
            braille.append(braille_dict['num'])
            braille.append(braille_dict[char])
        else:
            braille.append(braille_dict.get(char, ''))
    return ''.join(braille)

def translate(input_str):
    """Main function to determine the type of input and translate."""
    if is_braille(input_str):
        return braille_to_english(input_str)
    else:
        return english_to_braille(input_str)

