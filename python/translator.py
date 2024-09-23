import sys

# Braille representations for numbers
number_to_braille = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Braille representations for letters
alphabet_to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO'
}

# Special symbols
special_to_braille = {
    'capital': '.....O',  # For capital letters
    'number': '.O.OOO',    # For numbers
    'space': '......' # For space
}

# Reverse mapping for Braille to English
braille_to_number = {value: key for key, value in number_to_braille.items()}
braille_to_alphabet = {value: key for key, value in alphabet_to_braille.items()}

# Function to determine if the input is Braille or English
def is_braille(input_str):
    # Modulo 6 because every braille character is of length 6
    # all characters are either 0 or . that is why the all(...) expression is used
    return len(input_str) % 6 == 0 and all(c in 'O.' for c in input_str) 
    
# Function to convert English to Braille
def english_to_braille(input_str):
    result = []
    is_number = False
    for char in input_str:
        if char.isupper():
            result.append(special_to_braille['capital'])  # Add capital symbol
            result.append(alphabet_to_braille[char.lower()])
        elif char.isdigit():
            if is_number == False:
                result.append(special_to_braille['number'])  # Add number symbol
                is_number = True
            result.append(number_to_braille[char])
        elif char == ' ':
            result.append(special_to_braille['space'])
            is_number = False
        else:
            result.append(alphabet_to_braille[char])

    return ''.join(result)

# Function to convert Braille to English
def braille_to_english_str(input_str):
    result = []
    braille_chars = [input_str[i:i + 6] for i in range(0, len(input_str), 6)] # each element in braille_chars is one braille character
    is_capital = False
    is_number = False
    
    for char in braille_chars:
        if char == special_to_braille['capital']:
            is_capital = True
            continue
        if char == special_to_braille['number']:
            is_number = True
            continue
        if char == special_to_braille['space']:
            is_number = False
            result.append(' ')
            continue

        translated_char = braille_to_alphabet.get(char, '~') # ~ serves as a unknown character, returned when char not found

        if is_capital:
            result.append(translated_char.upper())
            is_capital = False
        elif is_number:
            result.append(braille_to_number.get(char, '~')) 
        else:
            result.append(translated_char)
    
    return ''.join(result)

# Main function
def main():
    if len(sys.argv) < 2:
        print("Incorrect args, correct usage: python translator.py <string>")
        return

    input_str = ' '.join(sys.argv[1:])
    
    if is_braille(input_str):
        print(braille_to_english_str(input_str))
    else:
        print(english_to_braille(input_str))

if __name__ == "__main__":
    main()
