import sys

map_braille_to_english = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.O....': 'i',
    '.OO...': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
    'OOO.O.': 'p',
    'OOOOO.': 'q',
    'O.OOO.': 'r',
    '.OO.O.': 's',
    '.OOOO.': 't',
    'O...OO': 'u',
    'O.O.OO': 'v',
    '.OO.OO': 'w',
    'OO..OO': 'x',
    'OO.OOO': 'y',
    'O..OOO': 'z',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.OO..O': '<',
    # 'O..OO.': '>',
    'O.O..O': '(',
    '.O.OO.': ')',
    '......': ' '
}

capital_follows = '.....O'
decimal_follows = '.O...O'
num_follows = '.O.OOO'
map_english_to_braille = {v: k for k, v in map_braille_to_english.items()}

def english_to_braille(english_string):
    braille_string = ""
    is_digit_set = False
    for char in english_string:
        if char == ' ':
            is_digit_set = False
            braille_string += map_english_to_braille[char]
        elif char.isdigit():
            if not is_digit_set:
                braille_string += num_follows
                is_digit_set = True
            num = int(char)
            if num == 0:
                num = 10
            char = chr(ord('a') + num - 1)
            braille_string += map_english_to_braille[char]
        elif char.isupper():
            braille_string += capital_follows
            braille_string += map_english_to_braille[char.lower()]
        elif char == '.' and is_digit_set:
            braille_string += decimal_follows
        else:
            is_digit_set = False
            braille_string += map_english_to_braille[char]
    return braille_string

def braille_to_english(braille_string):
    english_string = ""
    cap_follows = False
    digit_follows = False
    for i in range(0, len(braille_string), 6):
        braille = braille_string[i:i+6]
        if braille == capital_follows:
            cap_follows = True
        elif braille == num_follows:
            digit_follows = True
        elif braille == decimal_follows:
            english_string += '.'
        elif braille in map_braille_to_english:
            if braille == '......':
                digit_follows = False
                english_string += map_braille_to_english[braille]
            elif cap_follows:
                english_string += map_braille_to_english[braille].upper()
                cap_follows = False
            elif digit_follows:
                num = ord(map_braille_to_english[braille]) - ord('a') + 1
                if num == 10:
                    num = 0
                english_string += str(num)
            else:
                english_string += map_braille_to_english[braille]
    return english_string

def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <input_string>")
        sys.exit(1)
    input_string = " ".join(sys.argv[1:])
    if all(char in 'O.' for char in input_string):
        print(braille_to_english(input_string))
    else:
        print(english_to_braille(input_string))

if __name__ == "__main__":
    main()