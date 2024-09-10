import sys

# Define the Braille alphabet, numbers and constants
BRAILLE_ALPHABET = {
    'a': "O.....", 'b': "O.O...", 
    'c': "OO....", 'd': "OO.O..", 
    'e': "O..O..", 'f': "OOO...", 
    'g': "OOOO..", 'h': "O.OO..", 
    'i': ".OO...", 'j': ".OOO..", 
    'k': "O...O.", 'l': "O.O.O.", 
    'm': "OO..O.", 'n': "OO.OO.", 
    'o': "O..OO.", 'p': "OOO.O.", 
    'q': "OOOOO.", 'r': "O.OOO.", 
    's': ".OO.O.", 't': ".OOOO.", 
    'u': "O...OO", 'v': "O.O.OO", 
    'w': ".OOO.O", 'x': "OO..OO", 
    'y': "OO.OOO", 'z': "O..OOO"
}

BRAILLE_NUMBERS = {
    '1': "O.....", '2': "O.O...", 
    '3': "OO....", '4': "OO.O..", 
    '5': "O..O..", '6': "OOO...", 
    '7': "OOOO..", '8': "O.OO..", 
    '9': ".OO...", '0': ".OOO.."
}

BRAILLE_CAPITAL_FOLLOWS = ".....O"
BRAILLE_NUMBER_FOLLOWS = ".O.OOO"
BRAILLE_SPACE = "......"


def is_braille(text: str) -> bool:
    """Checks if input is Braille."""
    for char in text:
        if char != '.' and char != 'O':
            return False
    
    return len(text) % 6 == 0


def text_to_braille(text: str) -> str:
    """Convert English text to Braille."""
    braille_output = []
    number_follows = False
    
    for char in text:
        if char.isdigit() and not number_follows:
            braille_output.append(BRAILLE_NUMBER_FOLLOWS)
            number_follows = True
        elif not char.isdigit() and number_follows:
            number_follows = False
        
        if char.isupper():
            braille_output.append(BRAILLE_CAPITAL_FOLLOWS)
            char = char.lower()
        
        if char.isdigit():
            braille_output.append(BRAILLE_NUMBERS[char])
        elif char == ' ':
            braille_output.append(BRAILLE_SPACE)
        elif char.isalpha():
            braille_output.append(BRAILLE_ALPHABET[char])
    
    return ''.join(braille_output)


def braille_to_text(braille: str) -> str:
    """Convert Braille to English text."""
    braille_input = []
    for i in range(0, len(braille), 6):
        braille_input.append(braille[i:i+6])

    text_output = []
    number_follows = False
    capitalize_follows = False
    
    for symbol in braille_input:
        if symbol == BRAILLE_CAPITAL_FOLLOWS:
            capitalize_follows = True
            continue
        elif symbol == BRAILLE_NUMBER_FOLLOWS:
            number_follows = True
            continue
        elif symbol == BRAILLE_SPACE:
            text_output.append(' ')
            number_follows = False
            continue
        
        if number_follows:
            for num, braille_num in BRAILLE_NUMBERS.items():
                if symbol == braille_num:
                    text_output.append(num)
                    break
        else:
            for letter, braille_letter in BRAILLE_ALPHABET.items():
                if symbol == braille_letter:
                    if capitalize_follows:
                        text_output.append(letter.upper())
                        capitalize_follows = False
                    else:
                        text_output.append(letter)
                    break

    return ''.join(text_output)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input>")
        sys.exit(1)

    input_string = sys.argv[1] if len(sys.argv) >= 2 else '' 
    for i in range(2, len(sys.argv)):
        input_string = f'{input_string} {sys.argv[i]}'
    
    if is_braille(input_string):
        print(braille_to_text(input_string).strip())
    else:
        print(text_to_braille(input_string).strip())
        

if __name__ == "__main__":
    main()
