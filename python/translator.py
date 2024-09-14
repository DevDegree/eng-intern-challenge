import sys

# Dictionary to map english to braille
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
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    ' ': '......',
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
    'capital': '.....O',
    'number': '.O.OOO'
}

# Reversing the dictionary (didn't wanna rewrite it) 
braille_to_english = {value: key for key, value in english_to_braille.items()}

def is_braille(word):
    word = word.replace(' ', '')
    valid_characters = all(char in ".O" for char in word)
    valid_length = len(word) % 6 == 0
    return valid_characters and valid_length


def main():
    input_str = ' '.join(sys.argv[1:])

    # Braille to English
    if is_braille(input_str):
        english = ''
        isCapital = False
        isNumber = False
        # We have to remove spaces from the input string
        input_str = input_str.replace(' ', '') 

        for i in range(0, len(input_str), 6):
            curr = input_str[i:i+6]

            if curr not in braille_to_english:
                print(f"Braille is Invalid :( !!!: {curr}")
                return

            curr_engChar = braille_to_english[curr]

            if curr_engChar == 'capital':
                isCapital = True
                continue
            elif curr_engChar == 'number':
                isNumber = True
                continue

            if curr_engChar == ' ':
                english += ' '
                isNumber = False
                continue

            if isCapital:
                english += curr_engChar.upper()
                isCapital = False
            elif isNumber:
                english += curr_engChar
                isNumber = False
            else:
                english += curr_engChar

        print(english)

    else:
        # English to Braille
        braille = ''
        isNumber = False

        for char in input_str:
            if char.isupper():
                braille += english_to_braille['capital']
                char = char.lower()
                braille += english_to_braille[char]
            elif char.isdigit():
                if not isNumber:
                    isNumber = True
                    braille += english_to_braille['number']
                braille += english_to_braille[char]
            else:
                isNumber = False
                braille += english_to_braille[char]

        print(braille)


if __name__ == '__main__':
    main()
