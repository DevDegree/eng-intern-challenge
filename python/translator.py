import sys

to_braille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',
}

nums_to_braille = {'0': '.OOO..',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'}

#reverse mapping
to_english = {v: k for k, v in to_braille.items()}

nums_to_english = {v: k for k, v in nums_to_braille.items()}

capital = '.....O'
number_follows = '.O.OOO'

def main():
    code = ' '.join(sys.argv[1:])
    
    if len(code) < 1:
        sys.exit(1)
        
    number = False

    if code[0].lower() in to_braille:
        braille = []
        for char in code:
            if char.isupper():
                braille.append(capital)
                char = char.lower()
            if char == ' ':
                number = False
            if char.isnumeric() and not number:
                braille.append(number_follows)
                braille.append(nums_to_braille[char])
                number = True
            elif char.isnumeric():
                braille.append(nums_to_braille[char])
            else:
                braille.append(to_braille[char])
        print(''.join(braille))
    else:
        english = []
        i = 0
        while i < len(code):
            if code[i:i+6] == capital:
                i += 6
                english.append(to_english[code[i:i+6]].upper())
            elif code[i:i+6] == to_braille[' ']:
                number = False
                english.append(to_english[code[i:i+6]])
            elif code[i:i+6] == number_follows:
                i += 6
                english.append(nums_to_english[code[i:i+6]])
                number = True
            elif number:
                english.append(nums_to_english[code[i:i+6]])
                number = True
            else:
                english.append(to_english[code[i:i+6]])
            i += 6
        print(''.join(english))

if __name__ == "__main__" and len(sys.argv) > 1:
    main()
