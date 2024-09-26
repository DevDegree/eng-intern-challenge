braille_dict = {
    'A': 'O.....',    'B': 'O.O...',    'C': 'OO....',    'D': 'OO.O..',    'E': 'O..O..',
    'F': 'OOO...',    'G': 'OOOO..',    'H': 'O.OO..',    'I': '.OO...',    'J': '.OOO..',
    'K': 'O...O.',    'L': 'O.O.O.',    'M': 'OO..O.',    'N': 'OO.OO.',    'O': 'O..OO.',
    'P': 'OOO.O.',    'Q': 'OOOOO.',    'R': 'O.OOO.',    'S': '.OO.O.',    'T': '.OOOO.',
    'U': 'O...OO',    'V': 'O.O.OO',    'W': '.OOO.O',    'X': 'OO..OO',    'Y': 'OO.OOO',
    'Z': 'O..OOO',    ' ': '......',
    '.': '.O.O.O',    ',': '.O....',    '?': '.O..O.',    '!': '.O.OO.',    ':': '.O.O..',
    ';': '.OO...',    '-': '.O..O.',    '/': '.O.O..',    '<': '.O..OO',    '>': '.OO.O.',
    '(': '.O.OO.',    ')': '.O.OO.',    '=': '.OO.OO',   '+': '.OOO..',   '*': '.OOO.O'
}

number_dict = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '0'
}

number_sign = '.O.OOO'
capital_sign = '.....O'

def text_to_braille(text):
    result = ''
    number_mode = False

    for char in text:
        if char.isdigit():  # If it's a number
            if not number_mode:
                result += number_sign  # Prepend the number sign if switching to number mode
                number_mode = True
            # Convert number to braille using letters A-J for 0-9
            result += braille_dict[next(key for key, value in number_dict.items() if value == char)]
        elif char.isalpha():  # If it's a letter
            if number_mode:
                number_mode = False  # Exit number mode if we're encountering a letter
            if char.isupper():
                result += capital_sign  # Prepend capital sign for uppercase letters
            result += braille_dict[char.upper()]
        elif char in braille_dict:  # For spaces and punctuation
            if number_mode:
                number_mode = False  # Exit number mode for non-letter characters
            result += braille_dict[char]
    
    return result

def braille_to_text(braille):
    inv_braille = {v: k for k, v in braille_dict.items()}
    result = ''
    i = 0
    capitalize_next = False
    number_mode = False
    while i < len(braille):
        cell = braille[i:i+6]
        if cell == capital_sign:
            capitalize_next = True
            i += 6
        elif cell == number_sign:
            number_mode = True
            i += 6
        elif cell in inv_braille:
            char = inv_braille[cell]
            if number_mode and char in number_dict:
                result += number_dict[char]
            else:
                if char == ' ':
                    number_mode = False  # Reset number mode when encountering a space
                if capitalize_next:
                    result += char.upper()
                    capitalize_next = False
                else:
                    result += char.lower()
            i += 6
        else:
            i += 6
    return result

def is_braille(text):
    return all(char in '.O' for char in text) and len(text) % 6 == 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        print(braille_to_text(input_text))
    else:
        print(text_to_braille(input_text))
