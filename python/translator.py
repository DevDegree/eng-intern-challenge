import sys

braille_chars = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOO.O', 'r': 'O.OO.O', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......', '!': '..OOO.', ':': '..OO..', ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.OO..O', '>': 'O..OO.', '(': 'O.O..O', ')': '.O.OO.',
    'capital follows': '.....O', 'decimal follows': '.O...O', 'number follows': '.O.OOO', '.': '..OO.O', ',': '..O...', '?': '..O.OO'
}

braille_nums = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 'O': '.OOO..'
}

def braille_to_english(input_string):
    output_string = ''
    i = 0
    
    # if all(c in 'O.' for c in input_string):
    while i < (len(input_string)-6):
        if input_string[i:i+6] == braille_chars['capital follows']:
            i += 6
            char = [k for k,v in braille_chars.items() if v == input_string[i:i+6]][0].upper()
        elif input_string[i:i+6] == braille_chars['number follows']:
            i += 6
            char = [k for k,v in braille_nums.items() if v == input_string[i:i+6]][0]
        else:
            char = [k for k,v in braille_chars.items() if v == input_string[i:i+6]][0]
        output_string += char
        i += 6

    return output_string

def english_to_braille(input_string):
    output_string = ''
    i = 0
    
    while i < len(input_string):
        if input_string[i].isupper():
            output_string += braille_chars['capital follows']
            output_string += braille_chars[input_string[i].lower()]
        elif input_string[i].isdigit():
            output_string += braille_chars['number follows']
            while input_string[i] != ' ':
                output_string += braille_nums[input_string[i]]
                i += 1
            output_string += braille_chars[' ']
        else:
            output_string += braille_chars[input_string[i]]
        i += 1
    
    return output_string
    

def main():
    input_string = ' '.join(sys.argv[1:])
    
    # Determine if the input is Braille or English
    if all(c in 'O.' for c in input_string):
        # Translate Braille to English
        output_string = braille_to_english(input_string)
    else:
        # Translate English to Braille
        output_string = english_to_braille(input_string)
    
    # Print the output string (this will be captured in the test case)
    print(output_string, end="")

if __name__ == "__main__":
    main()