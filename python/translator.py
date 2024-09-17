import sys

# position of the dots in the Braille cell
# 1 4
# 2 5
# 3 6

# Braille patterns for letters (a-z)
braille_letters = {
    'a': [1],
    'b': [1,2],
    'c': [1,4],
    'd': [1,4,5],
    'e': [1,5],
    'f': [1,2,4],
    'g': [1,2,4,5],
    'h': [1,2,5],
    'i': [2,4],
    'j': [2,4,5],
    'k': [1,3],
    'l': [1,2,3],
    'm': [1,3,4],
    'n': [1,3,4,5],
    'o': [1,3,5],
    'p': [1,2,3,4],
    'q': [1,2,3,4,5],
    'r': [1,2,3,5],
    's': [2,3,4],
    't': [2,3,4,5],
    'u': [1,3,6],
    'v': [1,2,3,6],
    'w': [2,4,5,6],
    'x': [1,3,4,6],
    'y': [1,3,4,5,6],
    'z': [1,3,5,6],
}

# Braille patterns for numbers (0-9)
braille_numbers = {
    '1': [1],
    '2': [1,2],
    '3': [1,4],
    '4': [1,4,5],
    '5': [1,5],
    '6': [1,2,4],
    '7': [1,2,4,5],
    '8': [1,2,5],
    '9': [2,4],
    '0': [2,4,5],
}

# Special Sign
number_follows = [3,4,5,6]
capital_follows = [6]
decimal_follows = [3, 4, 5, 6]

# Braille patterns for punctuation
braille_punctuation = {
    '.': [2,5,6],
    ',': [2],
    '?': [2,3,6],
    '!': [2,3,5],
    ':': [2,5],
    ';': [2,3],
    '-': [3,6],
    '/': [3,4],
    '(': [1,2,6],
    ')': [3,4,5],
    '<': [2,4,6],
    '>': [1,3,5], 
}

# Braille pattern for space (empty cell)
space_cell = '......'

# Reverse mappings for Braille to English
reverse_braille_letters = {tuple(sorted(v)): k for k, v in braille_letters.items()}
reverse_braille_numbers = {tuple(sorted(v)): k for k, v in braille_numbers.items()}
reverse_braille_punctuation = {tuple(sorted(v)): k for k, v in braille_punctuation.items()}

# Function to convert dot positions to 'O' and '.' Braille representation
def dots_to_braille_pattern(dots):
    pattern = ['.'] * 6
    for dot in dots:
        if 1 <= dot <= 6:
            pattern[dot - 1] = 'O'
    return ''.join(pattern)

# Function to convert 'O' and '.' Braille representation to dot positions
def braille_pattern_to_dots(pattern):
    dots = []
    for i, c in enumerate(pattern):
        if c == 'O':
            dots.append(i + 1)
    return dots

# Translate English to Braille
def translate_eng_to_braille(input_text):
    output = []
    i = 0
    while i < len(input_text):
        char = input_text[i]
        if char == ' ':
            # Represent space with an empty Braille cell
            output.append(space_cell)
            i += 1
            continue

        if char.isupper():
            # Add capital sign
            output.append(dots_to_braille_pattern(capital_follows))
            char = char.lower()

        if char.isdigit():
            # Add number sign
            output.append(dots_to_braille_pattern(number_follows))
            # Process digits until a space or non-digit character
            while i < len(input_text) and input_text[i].isdigit():
                digit = input_text[i]
                pattern = braille_numbers.get(digit)
                if pattern:
                    output.append(dots_to_braille_pattern(pattern))
                i += 1
            continue
        elif char.isalpha():
            pattern = braille_letters.get(char)
            if pattern:
                output.append(dots_to_braille_pattern(pattern))
        # Ignore unsupported characters
        i += 1
    return ''.join(output)

# Translate Braille to English
def translate_braille_to_eng(input_text):
    output = []
    number_mode = False
    capitalize_next = False
    cells = []
    i = 0
    while i < len(input_text):
        if input_text[i] == ' ':
            # Space character
            cells.append(' ')
            i += 1
        else:
            if i + 6 <= len(input_text):
                cell = input_text[i:i+6]
                cells.append(cell)
                i +=6
            else:
                # Not enough characters for a Braille cell
                break
    # Process the cells
    for cell in cells:
        if cell == ' ':
            output.append(' ')
            number_mode = False  # Reset number mode after a space
        else:
            dots = braille_pattern_to_dots(cell)
            if dots == capital_follows:
                capitalize_next = True
            elif dots == number_follows:
                number_mode = True
            else:
                key = tuple(sorted(dots))
                if number_mode:
                    # Numbers
                    digit = reverse_braille_numbers.get(key)
                    if digit:
                        output.append(digit)
                    else:
                        # Invalid number character
                        pass
                else:
                    # Letters
                    letter = reverse_braille_letters.get(key)
                    if letter:
                        if capitalize_next:
                            letter = letter.upper()
                            capitalize_next = False
                        output.append(letter)
                    else:
                        # Invalid letter character
                        pass
    return ''.join(output)

# Main function to handle input and output
def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 translator.py [text to translate]")
        return
    input_text = ' '.join(args)
    # Determine if input is Braille or English
    is_braille = all(c in ('O', '.', ' ') for c in input_text)
    if is_braille:
        output = translate_braille_to_eng(input_text)
    else:
        output = translate_eng_to_braille(input_text)
    print(output)

if __name__ == '__main__':
    main()
