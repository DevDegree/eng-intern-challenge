import sys

# Braille mappings
letter_to_braille = {
    'a': 'O.....',  'b': 'O.O...',  'c': 'OO....',  'd': 'OO.O..',  'e': 'O..O..',
    'f': 'OOO...',  'g': 'OOOO..',  'h': 'O.OO..',  'i': '.OO...',  'j': '.OOO..',
    'k': 'O...O.',  'l': 'O.O.O.',  'm': 'OO..O.',  'n': 'OO.OO.',  'o': 'O..OO.',
    'p': 'OOO.O.',  'q': 'OOOOO.',  'r': 'O.OOO.',  's': '.OO.O.',  't': '.OOOO.',
    'u': 'O...OO',  'v': 'O.O.OO',  'w': '.OOO.O',  'x': 'OO..OO',  'y': 'OO.OOO',
    'z': 'O..OOO',  ' ': '......'
}

number_to_braille = {
    '1': 'O.....',  '2': 'O.O...',  '3': 'OO....',  '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...',  '7': 'OOOO..',  '8': 'O.OO..',  '9': '.OO...', '0': '.OOO..'
}

# Explicitly defined reverse mappings
braille_to_letter = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

braille_to_number = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

capital_symbol = '.....O'
number_symbol = '.O.OOO'

def text_to_braille(text):
    braille = []
    number_mode = False

    for char in text:
        if char.isalpha():
            if number_mode:
                braille.append('......')  # Space to end number mode
                number_mode = False
            if char.isupper():
                braille.append(capital_symbol)
                char = char.lower()
            braille.append(letter_to_braille[char])
        elif char.isdigit():
            if not number_mode:
                braille.append(number_symbol)
                number_mode = True
            braille.append(number_to_braille[char])
        elif char == ' ':
            braille.append('......')
            number_mode = False
        else:
            raise ValueError(f"Unsupported character: {char}")

    return ''.join(braille)

def braille_to_text(braille):
    text = []
    i = 0
    capitalize_next = False
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        
        if symbol == capital_symbol:
            capitalize_next = True
        elif symbol == number_symbol:
            number_mode = True
        elif number_mode and symbol in braille_to_number:
            text.append(braille_to_number[symbol])
        elif symbol in braille_to_letter:
            char = braille_to_letter[symbol]
            if char == ' ':
                number_mode = False
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            text.append(char)
        else:
            raise ValueError(f"Unknown Braille symbol: {symbol}")
        
        i += 6

    return ''.join(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py '<text or braille>'")
        return

    input_str = sys.argv[1]

    # Determine if input is Braille or text
    if all(c in 'O.' for c in input_str) and len(input_str) % 6 == 0:
        output = braille_to_text(input_str)
    else:
        output = text_to_braille(input_str)

    print(output)

if __name__ == "__main__":
    main()

