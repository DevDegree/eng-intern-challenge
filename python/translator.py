# English to Braille Alphabet Mapping
english_to_braille = {
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
    'z': 'O..OOO',
    ' ': '......'
}

# Number to Braille mapping
numbers_to_braille = {
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

# Braille to English Alphabet Mapping
braille_to_english = {v: k for k, v in english_to_braille.items()}
# Braille to Numbers Mapping
braille_to_numbers = {v: k for k, v in numbers_to_braille.items()}

def translate(input_string):
    # Determine if input is English or Braille
    if input_string[0].isalnum():
        output = ''
        number_initiated = False
        for char in input_string:
            # If the character is a number we need to add the number prefix
            if char.isdigit():
                if not number_initiated:
                    output += '.O.OOO'
                    number_initiated = True
                output += numbers_to_braille[char]
            else:
                # if the character is a space
                if char == ' ':
                    number_initiated = False
                # if the character is upper case
                if char.isupper():
                   output += '.....O'
                output += english_to_braille[char.lower()]
        return output
    else:
        cap = False
        number = False
        # Braille to English
        output = ''
        i = 0
        while i < len(input_string):
            # Check for numbers or letters, then translate
            braille_char = input_string[i:i+6]

            if cap:
                output += braille_to_english.get(braille_char, '').upper()
                cap = False
                i += 6
                continue

            # Check for capitalization
            if braille_char == '.....O':
                cap = True
                i += 6
                continue
            # Check for numbers
            elif braille_char == '.O.OOO':
                number = True
                i += 6
                continue
            elif braille_char == '......':
                output += ' '
                number = False
                i += 6
                continue

            if number:
                output += braille_to_numbers.get(braille_char, '')
            else:
                output += braille_to_english.get(braille_char, '')
            i += 6
        return output

if __name__ == "__main__":
    import sys
    # Get all the arguments passed to the script
    input_string = ''
    for arg in sys.argv[1:]:
        input_string += arg + ' '
    # Remvoe the last space
    result = translate(input_string[:-1])
    print(result)

