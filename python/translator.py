import sys

# Dictionary for English to Braille
alpha_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 
    'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 
    'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 
    'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO',
}

# Dictionary for Special Braille Characters
special_braille = {
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
}

# Dictionary for Numbers to Braille
num_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', 
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...',
    '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..',
}

# Dictionnary for Symbols to Braille
symbol_to_braille = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OOO.', ':': '..OO..', ';': '..O.O.',
    '-': '....OO', '/': '.O..O.', '<': '.OO..O',
    '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    ' ': '......',
}

# List of Braille Characters
braille_chars = [".", "O"]

def is_braille(input_str):
    if len(input_str) % 6 != 0:
        return False 
    for i in range(0, len(input_str), 6):
        if not all(c in braille_chars for c in input_str[i:i+6]):
            return False
    return True

def get_english_char(braille_char, braille_dict):
    for char, braille in braille_dict.items():
        if braille_char == braille:
            return char
    return ""

def braille_to_english(input_str):
    letter = ""
    command = ""
    result = ""

    left = 0
    right = 6

    while right <= len(input_str):
        while left < right:
            letter += input_str[left]
            left += 1

        if letter in special_braille.values():
            for cmd, braille in special_braille.items():
                if letter == braille:
                    command = cmd

        elif ((command == "" or command == "capital") and (letter in alpha_to_braille.values())):
            if command == "capital":
                result += get_english_char(letter, alpha_to_braille).capitalize()
                command = ""
            else: 
                result += get_english_char(letter, alpha_to_braille)  

        elif ((command == "" or command == "decimal" or command == "number") and (letter in symbol_to_braille.values())):
            result += get_english_char(letter, symbol_to_braille)

        elif command == "number" and letter in num_to_braille.values():
            result += get_english_char(letter, num_to_braille)

        right += 6
        letter = ""

    return result

def english_to_braille(input_str):
    result = ""
    command = ""

    for char in input_str:
        if char.isupper() or char in alpha_to_braille:
            if char.isupper():
                result += special_braille.get("capital")
                result += alpha_to_braille.get(char.lower())
            else:
                result += alpha_to_braille.get(char)

        elif char in num_to_braille:
            if command == "":
                command = "number"
                result += special_braille.get("number")
            result += num_to_braille.get(char)

        elif char in symbol_to_braille:
            result += symbol_to_braille.get(char)

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py '<string>'")
        sys.exit(1)

    input_str = ' '.join(sys.argv[1:])

    if is_braille(input_str):
        print(braille_to_english(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == '__main__':
    main()
