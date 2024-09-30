import sys

# Mapping letters to Braille dots
letter_to_dots = {
    'a': [1], 'b': [1, 2], 'c': [1, 4], 'd': [1, 4, 5], 'e': [1, 5], 'f': [1, 2, 4], 'g': [1, 2, 4, 5], 'h': [1, 2, 5], 'i': [2, 4],
    'j': [2, 4, 5], 'k': [1, 3], 'l': [1, 2, 3], 'm': [1, 3, 4], 'n': [1, 3, 4, 5], 'o': [1, 3, 5], 'p': [1, 2, 3, 4], 'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5], 's': [2, 3, 4], 't': [2, 3, 4, 5], 'u': [1, 3, 6],'v': [1, 2, 3, 6], 'w': [2, 4, 5, 6], 'x': [1, 3, 4, 6], 
    'y': [1, 3, 4, 5, 6], 'z': [1, 3, 5, 6]
}

# Function to convert dots to Braille
def dots_to_braille(dots):
    braille = ['.' for _ in range(6)]
    for dot in dots:
        if dot == 1:
            braille[0] = 'O'
        elif dot == 2:
            braille[2] = 'O'
        elif dot == 3:
            braille[4] = 'O'
        elif dot == 4:
            braille[1] = 'O'
        elif dot == 5:
            braille[3] = 'O'
        elif dot == 6:
            braille[5] = 'O'
    return ''.join(braille)

# Create dictionary for English to Braille
eng_to_braille = {}
# Create dictionary for Braille to English
braille_to_eng = {}

# Loop through each letter and its corresponding dots
for letter, dots in letter_to_dots.items():
    braille = dots_to_braille(dots)
    eng_to_braille[letter] = braille
    braille_to_eng[braille] = letter

# Add numbers
for i in range(10):
    num = str(i)
    letter = chr(ord('a') + i - 1) if i > 0 else 'j'
    eng_to_braille[num] = eng_to_braille[letter]

# Add special characters
eng_to_braille['CAPITAL'] = dots_to_braille([6])
eng_to_braille['NUMBER'] = dots_to_braille([3, 4, 5, 6])
eng_to_braille['SPACE'] = '......'

braille_to_eng[eng_to_braille['CAPITAL']] = 'CAPITAL'
braille_to_eng[eng_to_braille['NUMBER']] = 'NUMBER'
braille_to_eng[eng_to_braille['SPACE']] = ' '

# Function to check if input is Braille
def is_braille(text):
    text = text.replace(' ', '')
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

# Function to translate English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char == ' ':
            result.append(eng_to_braille['SPACE'])
            number_mode = False
        elif char.isupper():
            result.append(eng_to_braille['CAPITAL'])
            result.append(eng_to_braille[char.lower()])
            number_mode = False
        elif char.isdigit():
            if not number_mode:
                result.append(eng_to_braille['NUMBER'])
                number_mode = True
            result.append(eng_to_braille[char])
        else:
            result.append(eng_to_braille.get(char.lower(), '......'))
            number_mode = False
    return ''.join(result)

# Function to translate Braille to English
def braille_to_english(braille):
    result = []
    braille = braille.replace(' ', '')
    i = 0
    capital_next = False
    number_mode = False

    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == eng_to_braille['SPACE']:
            result.append(' ')
            number_mode = False
        elif symbol == eng_to_braille['CAPITAL']:
            capital_next = True
        elif symbol == eng_to_braille['NUMBER']:
            number_mode = True
        else:
            char = braille_to_eng.get(symbol, '')
            if char:
                if number_mode:
                    char = str('1234567890'['abcdefghij'.index(char)])
                elif capital_next:
                    char = char.upper()
                    capital_next = False
                result.append(char)
        i += 6

    return ''.join(result)

# Main function
def main():
    if len(sys.argv) < 2:
        print("Please provide input text as a command-line argument.")
        return

    input_text = ' '.join(sys.argv[1:])

    if is_braille(input_text):
        output = braille_to_english(input_text)
    else:
        output = english_to_braille(input_text)

    print(output)

if __name__ == '__main__':
    main()

