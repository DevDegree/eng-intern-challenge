import sys
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....','d': 'OO.O..','e': 'O..O..','f': 'OOO...','g': 'OOOO..','h': 'O.OO..',
    'i': '.OO...','j': '.OOO..','k': 'O...O.','l': 'O.O.O.','m': 'OO..O.','n': 'OO.OO.','o': 'O..OO.','p': 'OOO.O.',
    'q': 'OOOOO.','r': 'O.OOO.','s': '.OO.O.','t': '.OOOO.','u': 'O...OO','v': 'O.O.OO','w': '.OOO.O','x': 'OO..OO','y': 'OO.OOO',
    'z': 'O..OOO'
}
braille_special = {
    '.': '..OO.O',',': '..O...','?': '..O.OO','!': '..OOO.',
    ':': '..OO..',';': '..O.O.','-': '....OO','/': '.O..O.',
    '<': '.OO..O','>': 'O..OO.','(': 'O.O..O',')': '.O.OO.'
}
# numbers 0 to 9 replicate a to j
braille_numbers = {str(i): braille_alphabet[chr(96 + i)] for i in range(1, 10)}
braille_modifiers = {
    ' ': '......',
    'capital': '.....O',
    'number':'.O.OOO',
    '.':'.O...O'
}
def main():
    input_text = " ".join(sys.argv[1:])
    if set(input_text) in [{'O', '.'}, {'O'}, {'.'}] and len(input_text) % 6 == 0 and len(input_text) != 0:
        print(braille_to_english(input_text))
        return
    print(english_to_braille(input_text))
    return

# Checks for a decimal point
def is_decimal_point(text, index):
    if text[index] == '.' and 0 < index < len(text) - 1:
        return text[index - 1].isdigit() and text[index + 1].isdigit()
    return False

# Checks for a sequence of numbers
def sequence_numerical(text, index):
    return text[index].isnumeric() and index > 0 and text[index - 1].isdigit()

def get_braille_representation(char, text, index):
    # Clear modifiers first then proceed
    if char.isupper():
        return braille_modifiers['capital'] + braille_alphabet[char.lower()]
    elif char.isspace():
        return braille_modifiers[' ']
    elif char.isnumeric():
        return braille_numbers[char] if sequence_numerical(text, index) else braille_modifiers['number'] + braille_numbers[char]
    elif is_decimal_point(text, index):
        return braille_modifiers['.']
    if char in braille_special:
        return braille_special[char]
    elif char in braille_alphabet:
        return braille_alphabet[char]
    return None

# For braille to english translation
def find_key_by_value(dict, target_value):
    for key, value in dict.items():
        if value == target_value:
            return key
    return None

def english_to_braille(text):
    braille_string = ''
    for index, char in enumerate(text):
        braille_rep = get_braille_representation(char, text, index)
        if braille_rep is None:
            return "contains invalid character. Unable to translate"
        braille_string += braille_rep
    return braille_string

def braille_to_english(text):
    english_string = ''
    # Creates a list of braille characters
    braille_chunks = [text[i:i+6] for i in range(0, len(text), 6)]
    capitalized = False
    numeric = False
    for chunk in braille_chunks:
        # Clear modifiers first
        if chunk == braille_modifiers['capital']:
            capitalized = True
        elif chunk == braille_modifiers['number']:
            numeric = True
        elif chunk in braille_modifiers.values():
            key = find_key_by_value(braille_modifiers, chunk)
            if key == ' ':
                numeric = False
            english_string += key
        elif chunk in braille_alphabet.values():
            if numeric:
                key = find_key_by_value(braille_numbers, chunk)
                english_string += key
            else:
                key = find_key_by_value(braille_alphabet, chunk)
                english_string += key.upper() if capitalized else key
                capitalized = False
        elif chunk in braille_special.values():
            key = find_key_by_value(braille_special, chunk)
            english_string += key
        else:
            return "contains invalid character. Unable to translate"

if __name__ == "__main__": 
    main()