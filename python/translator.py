#!/usr/bin/env python3

import sys

# Define the mapping for Braille positions
def positions_to_braille(positions):
    pos_order = [1, 4, 2, 5, 3, 6]
    braille = ''
    for pos in pos_order:
        if pos in positions:
            braille += 'O'
        else:
            braille += '.'
    return braille

def braille_to_positions(braille):
    pos_order = [1, 4, 2, 5, 3, 6]
    positions = []
    for idx, ch in enumerate(braille):
        if ch == 'O':
            positions.append(pos_order[idx])
    return positions

# Mapping letters to Braille positions
letter_to_positions = {
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

# Reverse mapping from Braille code to letters
positions_to_letter = {}

for letter, positions in letter_to_positions.items():
    braille = positions_to_braille(positions)
    positions_to_letter[braille] = letter

# Number sign and capital sign
number_sign_positions = [3,4,5,6]
number_sign = positions_to_braille(number_sign_positions)
capital_sign_positions = [6]
capital_sign = positions_to_braille(capital_sign_positions)

# Numbers mapping (after number sign)
number_mapping = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': '0',
}

# Prepare reverse mapping for numbers
positions_to_number = {}
for letter, num in number_mapping.items():
    positions = letter_to_positions[letter]
    braille = positions_to_braille(positions)
    positions_to_number[braille] = num

def is_braille(s):
    for ch in s:
        if ch not in 'O. ':
            return False
    return True

def translate_to_braille(text):
    result = ''
    idx = 0
    while idx < len(text):
        ch = text[idx]
        if ch.isupper():
            # Add capital sign
            result += capital_sign
            ch = ch.lower()
        if ch.isdigit():
            # Add number sign if previous character was not a digit
            if idx == 0 or not text[idx -1].isdigit():
                result += number_sign
            # Convert digit to corresponding letter a-j
            num_to_letter = {v: k for k, v in number_mapping.items()}
            letter = num_to_letter[ch]
            positions = letter_to_positions[letter]
            braille = positions_to_braille(positions)
            result += braille
        elif ch == ' ':
            # Represent space as empty Braille cell
            result += '......'
        elif ch.lower() in letter_to_positions:
            positions = letter_to_positions[ch.lower()]
            braille = positions_to_braille(positions)
            result += braille
        idx +=1
    return result

def translate_from_braille(braille_text):
    result = ''
    idx = 0
    capital_next = False
    number_mode = False
    # Remove spaces
    braille_text = braille_text.replace(' ', '')
    while idx < len(braille_text):
        cell = braille_text[idx:idx+6]
        if len(cell) <6:
            break
        if cell == capital_sign:
            capital_next = True
        elif cell == number_sign:
            number_mode = True
        elif cell == '......':
            result += ' '
            number_mode = False
        elif number_mode:
            if cell in positions_to_number:
                result += positions_to_number[cell]
            else:
                # Unknown Braille code
                result += '?'
        else:
            if cell in positions_to_letter:
                letter = positions_to_letter[cell]
                if capital_next:
                    letter = letter.upper()
                    capital_next = False
                result += letter
            else:
                # Unknown Braille code
                result += '?'
        idx +=6
    return result

def main():
    if len(sys.argv) >1:
        input_text = ' '.join(sys.argv[1:])
    else:
        input_text = sys.stdin.read().strip()
    if is_braille(input_text.replace(' ', '')):
        output = translate_from_braille(input_text)
    else:
        output = translate_to_braille(input_text)
    print(output)

if __name__ == '__main__':
    main()
