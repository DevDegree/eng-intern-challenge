import sys


#   Position 0: Dot 1
#   Position 1: Dot 4
#   Position 2: Dot 2
#   Position 3: Dot 5
#   Position 4: Dot 3
#   Position 5: Dot 6

# Visual representation of Braille cell 
# Dot 1  Dot 4
# Dot 2  Dot 5
# Dot 3  Dot 6

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

# Braille Special sign
number_follows = [3,4,5,6]
capital_follows = [6]

# Braille patterns for numbers (0-9), represented by letters a-j with number sign prefix
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

# Reverse mappings for Braille to English translation
reverse_braille_letters = {tuple(sorted(v)): k for k, v in braille_letters.items()}
reverse_braille_numbers = {tuple(sorted(v)): k for k, v in braille_numbers.items()}
reverse_braille_punctuation = {tuple(sorted(v)): k for k, v in braille_punctuation.items()}

# Mapping of dots to positions in the 6-character string
dot_to_index = {
    1: 0,  # Dot 1 -> Position 0
    4: 1,  # Dot 4 -> Position 1
    2: 2,  # Dot 2 -> Position 2
    5: 3,  # Dot 5 -> Position 3
    3: 4,  # Dot 3 -> Position 4
    6: 5,  # Dot 6 -> Position 5
}

index_to_dot = {v: k for k, v in dot_to_index.items()}

def dots_to_braille_pattern(dots):
    pattern = ['.'] * 6
    for dot in dots:
        index = dot_to_index[dot]
        pattern[index] = 'O'
    return ''.join(pattern)

def braille_pattern_to_dots(pattern):
    dots = []
    for i, c in enumerate(pattern):
        if c == 'O':
            dot = index_to_dot[i]
            dots.append(dot)
    return dots

def translate_eng_to_braille(input_text):
    output = []
    i = 0
    while i < len(input_text):
        char = input_text[i]
        if char == ' ':
            # Change: Represent space with an empty Braille cell ('......')
            output.append('......')
            i += 1
            continue
        if char.isupper():
            output.append(dots_to_braille_pattern(capital_follows))
            char = char.lower()
        if char.isdigit():
            output.append(dots_to_braille_pattern(number_follows))
            while i < len(input_text) and input_text[i].isdigit():
                digit = input_text[i]
                pattern = braille_numbers.get(digit)
                if pattern:
                    output.append(dots_to_braille_pattern(pattern))
                i += 1
            continue
        elif char in braille_punctuation:
            pattern = braille_punctuation[char]
            output.append(dots_to_braille_pattern(pattern))
        elif char.isalpha():
            pattern = braille_letters.get(char)
            if pattern:
                output.append(dots_to_braille_pattern(pattern))
        i += 1
    return ''.join(output)

def translate_braille_to_eng(input_text):
    output = []
    number_mode = False
    capitalize_next = False
    cells = []
    i = 0
    # Change: Process the input in chunks of 6 characters (Braille cells)
    while i + 6 <= len(input_text):
        cell = input_text[i:i+6]
        cells.append(cell)
        i += 6
    # Handle any remaining characters (if incomplete Braille cell)
    if i < len(input_text):
        cell = input_text[i:]
        if len(cell) == 6:
            cells.append(cell)
    for cell in cells:
        if cell == '......':
            # Change: Interpret '......' as a space in English output
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
                    char = reverse_braille_numbers.get(key)
                    if char:
                        output.append(char)
                    else:
                        # Check if it's a punctuation mark
                        punct = reverse_braille_punctuation.get(key)
                        if punct:
                            output.append(punct)
                    # Continue in number mode unless a space is encountered
                else:
                    punct = reverse_braille_punctuation.get(key)
                    if punct:
                        output.append(punct)
                    else:
                        char = reverse_braille_letters.get(key)
                        if char:
                            if capitalize_next:
                                char = char.upper()
                                capitalize_next = False
                            output.append(char)
    return ''.join(output)

def main():
    args = sys.argv[1:]
    if not args:
        return
    input_text = ''.join(args)
    # Change: Exclude spaces from the Braille detection check
    is_braille = all(c in ('O', '.') for c in input_text)
    if is_braille:
        output = translate_braille_to_eng(input_text)
    else:
        output = translate_eng_to_braille(input_text)
    print(output)

if __name__ == '__main__':
    main()