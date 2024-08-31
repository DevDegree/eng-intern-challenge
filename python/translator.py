import sys
import subprocess

# Braille patterns dictionary remains the same
braille_patterns = {
    '0': '.OOO..', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..',
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...',
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......', 'NUM': '.O.OOO', 'CAP': '.....O', 'DEC': '.O...O',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.',
    '(': 'O.O..O', ')': '.O..O.'
}

def translate_to_braille(input_string):
    braille_output = ''
    num_mode = False
    for i, char in enumerate(input_string):
        if char.isdigit():
            if not num_mode:
                braille_output += braille_patterns['NUM']
                num_mode = True
            braille_output += braille_patterns[char]
        elif char.isalpha():
            if char.isupper():
                if num_mode:
                    num_mode = False
                braille_output += braille_patterns['CAP'] + braille_patterns[char]
            else:
                braille_output += braille_patterns[char.upper()]
        elif char == '.':
            if i + 1 < len(input_string) and input_string[i + 1].isdigit():
                braille_output += braille_patterns['DEC']
            else:
                braille_output += braille_patterns['.']
            num_mode = True
        else:
            if num_mode:
                num_mode = False
            braille_output += braille_patterns.get(char, '......')
    return braille_output

def braille_to_english_translation(braille_string):
    braille_to_english = {v: k for k, v in braille_patterns.items()}

    braille_chunks = [braille_string[i:i+6] for i in range(0, len(braille_string), 6)]
    english_output = ''
    num_mode = False
    capital_mode = False

    for chunk in braille_chunks:
        if chunk == braille_patterns['NUM']:
            num_mode = True
        elif chunk == braille_patterns['CAP']:
            capital_mode = True
            num_mode = False
        elif chunk == braille_patterns['DEC']:
            english_output += '.'
        elif chunk in braille_to_english:
            char = braille_to_english[chunk]
            if num_mode:
                if char.isdigit():
                    english_output += char
                    num_mode = False
                else:
                    english_output += '?'  
            else:
                if capital_mode and char.isalpha():
                    english_output += char
                    capital_mode = False
                else:
                    english_output += char.lower()
        else:
            english_output += '?'  

    return english_output

def identify_and_translate(input_string):
    if all(char in '.O' for char in input_string):
        return braille_to_english_translation(input_string)
    else:
        return translate_to_braille(input_string)

def main():
    input_strings = sys.argv[1:]
    results = [identify_and_translate(input_str) for input_str in input_strings]
    r= ""
    count = 0
    for result in results:

        r +=result
        if count<2:
            r+=braille_patterns[' ']
        count+=1
    print(r)
if __name__ == '__main__':
    main()
