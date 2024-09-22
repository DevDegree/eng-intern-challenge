import sys

ENGLISH_TO_BRAILLE = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOOO.',
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
    'w': '.OOOOO',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO',
    'DECIMAL': '.O...O',
}
BRAILLE_TO_ENGLISH= {}
# reverse map of braille to enligsh
for char, braille in ENGLISH_TO_BRAILLE.items():
    BRAILLE_TO_ENGLISH[braille] = char

# the numbers are j repeats of alphabets
NUMBER_MAP = {
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


def is_braille(input_str):
    for c in input_str:
        if c not in ['O','.']:
            return False
    return True
    
def english_to_braille(text):
    braille = []
    number_mode = False
    for char in text:
        if char == ' ':
            braille.append(ENGLISH_TO_BRAILLE[' '])
            number_mode = False
            continue
        elif char == '.':
            braille.append(ENGLISH_TO_BRAILLE['DECIMAL'])
            number_mode = False
            continue
        elif char.isupper():
            braille.append(ENGLISH_TO_BRAILLE['CAPITAL'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille.append(ENGLISH_TO_BRAILLE['NUMBER'])
                number_mode = True
            if char == '0':
                braille.append(ENGLISH_TO_BRAILLE['j']) #0 same as j
            else:
                braille.append(ENGLISH_TO_BRAILLE[chr(ord('a') + int(char) - 1)])
        else:
            if number_mode:
                number_mode = False
            if char in ENGLISH_TO_BRAILLE:
                braille.append(ENGLISH_TO_BRAILLE[char])
            else:
                # unknown characters
                continue
    return ''.join(braille)

def braille_to_english(braille_str):
    #split into chunks of 6
    chunks = [] 
    for i in range(0, len(braille_str), 6):
        # split the string from index i to i+6 then store it
        chunk = braille_str[i:i+6]
        chunks.append(chunk)

    english = []
    i = 0
    number_mode = False
    while i < len(chunks):
        chunk = chunks[i]
        # print("Chunk", chunk)
        if chunk == ENGLISH_TO_BRAILLE['CAPITAL']:
            i += 1
            # print("hello")
            if i < len(chunks):
                next_char = BRAILLE_TO_ENGLISH.get(chunks[i], '')
                print(next_char)
                if next_char:
                    english.append(next_char.upper())
            i += 1
            continue
        elif chunk == ENGLISH_TO_BRAILLE['NUMBER']:
            number_mode = True
            i += 1
            continue
        elif chunk == ENGLISH_TO_BRAILLE['DECIMAL']:
            english.append('.')
            number_mode = False
            i += 1
            continue
        elif chunk == ENGLISH_TO_BRAILLE[' ']:
            english.append(' ')
            number_mode = False
            i += 1
            continue
        elif number_mode:
            char = BRAILLE_TO_ENGLISH.get(chunk, '')
            if char in NUMBER_MAP:
                english.append(NUMBER_MAP[char])
            i += 1
            continue
        else:
            char = BRAILLE_TO_ENGLISH.get(chunk, '')
            if char:
                english.append(char)
            i += 1
            continue
    return ''.join(english)

def main():
    # if there is no string input when running the program
    if len(sys.argv) < 2:
        print("")
        return
    # print(sys.argv)
    input_args = sys.argv[1:]
    # print(input_args)
    input_str = ' '.join(input_args)
    if is_braille(input_str):
        translated = braille_to_english(input_str)
    else:
        translated = english_to_braille(input_str)
    print(translated)

if __name__ == "__main__":
    main()
