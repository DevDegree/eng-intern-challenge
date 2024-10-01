import sys

# Braille alphabet
BRAILLE_ALPHABET = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Braille Number Mapping
BRAILLE_NUMBERS = {
    '1': 'O.....', 
    '2': 'O.O...', 
    '3': 'OO....', 
    '4': 'OO.O..', 
    '5': 'O..O..', 
    '6': 'OOO...', 
    '7': 'OOOO..', 
    '8': 'O.OO..', 
    '9': '.OO...', 
    '0': '.OOO..', 
}

BRAILLE_SPECIAL = {
    'capital_follows': '.....O',
    'number_follows': '.O.OOO',
    'space': '......',
    
    'period': '..OO.O',
    'comma': '..O...',
    'question_mark': '..O.OO',
    'exclamation_mark': '..OOO.',
    'colon': '..OO..',
    'semicolon': '..O.O.',
    'hyphen': '....OO',
    'slash': '.O..O.',
    'open_parenthesis': '..OOO.',
    'close_parenthesis': '..OOOO',
    
}

def english_to_braille(text):
    result = []
    number_mode = False  # Track whether we are in number mode

    for char in text:
        if char.isalpha():  # It's a letter
            if number_mode:
                result.append(BRAILLE_SPECIAL['space'])  # Reset with a space if we were in number mode
                number_mode = False

            if char.isupper():
                result.append(BRAILLE_SPECIAL['capital_follows'])
            result.append(BRAILLE_ALPHABET[char.lower()])

        elif char.isdigit():  # It's a number
            if not number_mode:
                result.append(BRAILLE_SPECIAL['number_follows'])
                number_mode = True
            result.append(BRAILLE_NUMBERS[char])

        elif char.isspace():  # It's a space
            result.append(BRAILLE_SPECIAL['space'])
            number_mode = False  # Reset number mode if there's a space

        # Handle punctuation
        elif char == '.':
            result.append(BRAILLE_SPECIAL['period'])
        elif char == ',':
            result.append(BRAILLE_SPECIAL['comma'])
        elif char == '?':
            result.append(BRAILLE_SPECIAL['question_mark'])
        elif char == '!':
            result.append(BRAILLE_SPECIAL['exclamation_mark'])
        elif char == ':':
            result.append(BRAILLE_SPECIAL['colon'])
        elif char == ';':
            result.append(BRAILLE_SPECIAL['semicolon'])
        elif char == '-':
            result.append(BRAILLE_SPECIAL['hyphen'])
        elif char == '/':
            result.append(BRAILLE_SPECIAL['slash'])
        elif char == '(':
            result.append(BRAILLE_SPECIAL['open_parenthesis'])
        elif char == ')':
            result.append(BRAILLE_SPECIAL['close_parenthesis'])

    return ''.join(result)


def braille_to_english(braille):
    result = []
    i = 0
    capitalize_next = False
    number_mode = False
    
    reverse_alphabet = {v: k for k, v in BRAILLE_ALPHABET.items()}
    reverse_numbers = {v: k for k, v in BRAILLE_NUMBERS.items()}
    reverse_special = {v: k for k, v in BRAILLE_SPECIAL.items() if k not in ['capital_follows', 'number_follows', 'space']}

    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == BRAILLE_SPECIAL['capital_follows']:
            capitalize_next = True
            i += 6
            continue
        
        if symbol == BRAILLE_SPECIAL['number_follows']:
            number_mode = True
            i += 6
            continue
        
        if symbol == BRAILLE_SPECIAL['space']:
            result.append(' ')
            number_mode = False
            i += 6
            continue
        
        # Handle punctuation
        if symbol in reverse_special:
            result.append(reverse_special[symbol])
            i += 6
            continue
        
        if number_mode:
            if symbol in reverse_numbers:
                result.append(reverse_numbers[symbol])
            number_mode = False  # Exit number mode after processing
        else:
            if symbol in reverse_alphabet:
                letter = reverse_alphabet[symbol]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
        
        i += 6

    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Correct Usage: python translator.py <input_string>")
        return
    
    input_string = ' '.join(sys.argv[1:])
    
    # Determine if input is English or Braille
    if all(c in 'O.' for c in input_string):
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)

if __name__ == "__main__":
    main()