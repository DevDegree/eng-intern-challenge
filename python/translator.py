#!/usr/bin/env python3
import sys

# Braille dictionary for letters
braille_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 'Z': 'O..OOO'
}
braille_numbers_dict = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
braille_special_dict = {
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.OO..O', '(': 'O.O..O', ')': '.O.OO.', ' ': '......'
}
braille_indication_dict = {
    'capital': '.....O',
    'number': '.O.OOO',
    'decimal': '.O...O'
}

# Detect whether the input is Braille or English
def is_braille(text):
    return all(c in 'O.' for c in text)
# Function to create a reverse dictionary
def reverse_dict(d):
    return {v: k for k, v in d.items()}

def english_to_braille(sentence):
    result = []
    words = sentence.split()
    for word in words:
        if word.isnumeric():
            result.append(braille_indication_dict['number'])
        for char in word:
            if char.isalpha():
                if char.isupper():
                    result.append(braille_indication_dict['capital'] + braille_dict[char])
                else:
                    result.append(braille_dict[char.upper()])
            if char.isnumeric():
                result.append(braille_numbers_dict[char])
            if char in braille_dict:
                result.append(braille_dict[char])
            elif char in braille_special_dict:
                result.append(braille_special_dict[char])
            else:
                continue

        if word != words[-1]:
            result.append(braille_special_dict[' '])
    return ''.join(result)


def braille_to_english(sentence):
    # Create reverse dictionaries
    reverse_braille_dict = reverse_dict(braille_dict)
    reverse_braille_numbers_dict = reverse_dict(braille_numbers_dict)
    reverse_braille_special_dict = reverse_dict(braille_special_dict)
    reverse_braille_indication_dict = reverse_dict(braille_indication_dict)
    
    result = []
    capital_mode = False
    number_mode = False
    words = [sentence[i:i+6] for i in range(0, len(sentence), 6)]
    print(words)

    for word in words:
        # Check for Braille special indicators
        if word == '.O.OOO':
            number_mode = True
            continue
        if word == '.....O':
            capital_mode = True
            continue
        if word == '......':
            result.append(' ')
            number_mode = False
            continue

        # Decode the Braille cell
        if number_mode:
            if word in reverse_braille_numbers_dict:
                result.append(reverse_braille_numbers_dict[word])
        elif word in reverse_braille_dict:
            char = reverse_braille_dict[word]
            if capital_mode:
                result.append(char)
                capital_mode = False
            else:
                result.append(char.lower())
        elif word in reverse_braille_special_dict:
            result.append(reverse_braille_special_dict[word])
    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <input>")
        return

    # make input text an array of strings
    input_text = ' '.join(sys.argv[1:])
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

if __name__ == '__main__':
    main()
