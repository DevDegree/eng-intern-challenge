import sys

# Braille Dictionaries
char_to_brai = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 
    'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..', 'cap': '.....O', 'deci': '.O...O', 'num': '.O.OOO',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}

brai_to_char = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 
    'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z', 
    # 'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5', 'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0', 
    '.....O': 'cap', '.O...O': 'deci', '.O.OOO': 'num',
    '..OO.O': '.', '..O...': ',', '..O.OO': '?', '..OOO.': '!', '..OO..': ':', '..O.O.': ';', '....OO': '-', '.O..O.': '/', '.OO..O': '<', 'O..OO.': '>', 'O.O..O': '(', '.O.OO.': ')', '......': ' '
}

alph_to_digit = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
}

def is_braille(text):
    # Check the given string is English or Braille
    if len(text) % 6 != 0:
        return False
    chunks = [text[i:i+6] for i in range(0, len(text), 6)]
    return all(chunk in brai_to_char for chunk in chunks)

def eng_to_bari(text):
    result = ''
    # Record the number follows option
    num_follows = False
    for char in text:
        # Check the char type
        if char.isalpha():
            # If uppercase alphabet 
            if char.isupper():
                result += char_to_brai['cap'] + char_to_brai[char.lower()]
            # If lowercase alphabet
            else:
                result += char_to_brai[char]
        # If digit
        elif char.isdigit():
            if num_follows:
                result += char_to_brai[char]
            else: 
                result += char_to_brai['num'] + char_to_brai[char]
                num_follows = True
        # If punctuations
        else:
            if char == ' ':
                num_follows = False
            result += char_to_brai[char]
    return result

def bari_to_eng(text):
    result = ''
    chunks = [text[i:i+6] for i in range(0, len(text), 6)]
    num_follows = False
    cap_follows = False
    for c in chunks:
        curr_char = brai_to_char[c]
        # Chunck is cap
        if curr_char == 'cap':
            cap_follows = True
        # Chunck is digit
        elif num_follows == True and curr_char in alph_to_digit :
            result += alph_to_digit[curr_char]
        # Chunck is alphabet
        elif curr_char.isalpha() and len(curr_char) == 1: 
            if cap_follows:
                result += curr_char.upper()
                cap_follows = False
            else:
                result += curr_char
        # Chunck is num
        elif curr_char == 'num':
            num_follows = True
        # Chunck is puntuations
        elif curr_char == ' ':
            result += curr_char
            num_follows = False
        else:
            result += curr_char
    return result

def translate(input):
    if is_braille(input):
        return bari_to_eng(input)
    else:
        return eng_to_bari(input)
    
if __name__ == "__main__":
    # Check if any command-line arguments were provided
    if len(sys.argv) > 1:
        # Join all command-line arguments as the input string
        input_str = ' '.join(sys.argv[1:])
    else:
        # If no command-line arguments were given
        input_str = input()
    # Call the translate function with the input arguments
    result = translate(input_str)

    # Output the result
    print(result)