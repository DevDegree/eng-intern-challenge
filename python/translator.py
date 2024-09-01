import sys

braille_chars = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......'
}

braille_unique = {'capital': '.....O', 'number': '.O.OOO'}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
}

def english_to_braille(string):
    result = ''
    is_number = False

    for char in string:
        if char.isdigit():
            if not is_number:
                is_number = True
                result += braille_unique['number']
            result += braille_numbers[char]
        elif char == ' ':
            is_number = False
            result += braille_chars[' ']
        elif char.isalpha():
            if char == char.upper():
                result += braille_unique['capital']
            result += braille_chars[char.lower()]
        else:
            result += '......'  # Fallback for unmapped characters

    return result

def braille_to_english(string):
    # Create a dictionary that maps Braille characters to their corresponding English letters
    english_chars = {}
    for key, value in braille_chars.items():
        english_chars[value] = key
    
    # Create a dictionary that maps unique Braille patterns (like capital and number) to their meanings
    english_unique = {}
    for key, value in braille_unique.items():
        english_unique[value] = key
    
    # Create a dictionary that maps Braille number patterns to their corresponding digits
    english_numbers = {}
    for key, value in braille_numbers.items():
        english_numbers[value] = key

    result = ''
    is_upper = False
    is_number = False

    # Loop through the string, processing 6 characters at a time
    for i in range(0, len(string), 6):
        braille_char = string[i: i + 6]

        if braille_char in english_unique:
            if english_unique[braille_char] == 'capital':
                is_upper = True
            elif english_unique[braille_char] == 'number':
                is_number = True
            continue

        if is_number:
            if braille_char in english_numbers:
                result += english_numbers[braille_char]
            else:
                result += ' '
            is_number = False
        elif braille_char in english_chars:
            letter = english_chars[braille_char]
            if is_upper:
                result += letter.upper()
                is_upper = False
            else:
                result += letter
        else:
            result += ' '  # Fallback for unmapped characters

    return result


def is_string_braille(string):
    # Check if the length of the string is a multiple of 6
    if len(string) % 6 != 0:
        return False
    
    # Check each character in the string
    for char in string:
        # If the character is not 'O' or '.', return False
        if char != 'O' and char != '.':
            return False
    
    # If all characters are valid, return True
    return True

def main():
    message = ' '.join(sys.argv[1:])
    is_braille_string = is_string_braille(message)

    if is_braille_string:
        print(braille_to_english(message))
    else:
        print(english_to_braille(message))

if __name__ == "__main__":
    main()