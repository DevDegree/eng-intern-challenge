import sys

characters = {
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
    ' ': '......',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.'
}

numbers = {
    "1": "O.....",
    "2": "O.O...", 
    "3": "OO....", 
    "4": "OO.O..", 
    "5": "O..O..",
    "6": "OOO...", 
    "7": "OOOO..", 
    "8": "O.OO..", 
    "9": ".OO...",
    "0": ".OOO..",
}

special = {
    "cap": ".....O",
    "num": ".O.OOO",
    "dec": ".O...O",
}

reverse_braille_letters = {v: k for k, v in {**characters}.items()}
reverse_braille_numbers = {v: k for k, v in {**numbers}.items()}

def english_to_braille(text):
    inNum = True
    canDec = False
    braille_translation = ""
    for char in text:
        if char.isupper():
            inNum = True
            braille_translation += special["cap"]
            char = char.lower()
        if char.isdigit():
            if inNum:
                braille_translation += special["num"]
                inNum = False
                canDec = True
            braille_translation += numbers[char]
        else:
            inNum = True
            if canDec and char == '.':
                braille_translation += special["dec"]
                canDec = False
                inNum = False
            braille_translation += characters.get(char, "")
    return braille_translation

def braille_to_english(braille):
    english_translation = ""
    index = 0
    while index < len(braille):
        char = braille[index:index + 6]
        if char == special["cap"]:
            next_char = braille[index + 6:index + 12]
            english_translation += reverse_braille_letters[next_char].upper()
            index += 12
        elif char == special["num"]:
            index += 6
            while True:
                next_char = braille[index:index + 6]
                if next_char == ("......") or next_char == (''):
                    break
                english_translation += reverse_braille_numbers[next_char]
                index += 6
        else:
            english_translation += reverse_braille_letters.get(char, "")
            index += 6
    return english_translation

def is_braille(text):
    return all(char in "O. " for char in text)

def main():
    text = " ".join(sys.argv[1:])

    if is_braille(text):
        print(braille_to_english(text))
    else:
        print(english_to_braille(text))

if __name__ == "__main__":
    main()