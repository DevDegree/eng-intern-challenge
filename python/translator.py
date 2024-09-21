import sys

# Mapping Braille dot positions to indices in the 6-character string
dot_positions = {1: 0, 2: 2, 3: 4, 4: 1, 5: 3, 6: 5}

# Mapping letters to their corresponding Braille dot positions
letter_to_dots = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6],
}

# Mapping digits to corresponding letters in Braille
number_to_letter = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j',
}

# Function: Convert dot positions to a 6-character Braille pattern
def dots_to_pattern(dots):
    pattern = ['.'] * 6
    for dot in dots:
        index = dot_positions[dot]
        pattern[index] = 'O'
    return ''.join(pattern)

# Generate letter to pattern mapping
letter_to_pattern = {letter: dots_to_pattern(dots) for letter, dots in letter_to_dots.items()}

# Generate pattern to letter mapping
pattern_to_letter = {pattern: letter for letter, pattern in letter_to_pattern.items()}

# Generate number to pattern mapping
number_to_pattern = {digit: letter_to_pattern[letter] for digit, letter in number_to_letter.items()}

# Number and capitalization indicators
number_indicator = dots_to_pattern([3, 4, 5, 6])
capitalization_indicator = dots_to_pattern([6])

# Function: Determine if the input is Braille
def is_braille(s):
    s_no_space = s.replace(' ', '')
    return set(s_no_space) <= {'O', '.'} and len(s_no_space) % 6 == 0

# Function: Translate text to Braille
def text_to_braille(text):
    output = []
    number_mode = False
    for char in text:
        if char == ' ':
            output.append('......')  # Braille space
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                output.append(number_indicator)
                number_mode = True
            output.append(number_to_pattern[char])
        else:
            if number_mode:
                number_mode = False
            if char.isupper():
                output.append(capitalization_indicator)
                char = char.lower()
            pattern = letter_to_pattern.get(char)
            if pattern:
                output.append(pattern)
    return ''.join(output)

# Function- Translate Braille to text
def braille_to_text(braille_string):
    output = []
    number_mode = False
    capitalization_flag = False
    chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    for chunk in chunks:
        if chunk == '......':
            output.append(' ')
            number_mode = False
        elif chunk == capitalization_indicator:
            capitalization_flag = True
        elif chunk == number_indicator:
            number_mode = True
        else:
            if number_mode:
                letter = pattern_to_letter.get(chunk)
                if letter:
                    for digit, ltr in number_to_letter.items():
                        if ltr == letter:
                            output.append(digit)
                            break
                else:
                    continue
            else:
                letter = pattern_to_letter.get(chunk)
                if letter:
                    if capitalization_flag:
                        output.append(letter.upper())
                        capitalization_flag = False
                    else:
                        output.append(letter)
    return ''.join(output)

def main():
    if len(sys.argv) < 2:
        sys.exit("No input provided")
    input_string = ' '.join(sys.argv[1:])
    if is_braille(input_string):
        print(braille_to_text(input_string))
    else:
        print(text_to_braille(input_string))

if __name__ == "__main__":
    main()

