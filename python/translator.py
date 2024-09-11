import sys

ALPHABET_BRAILLE = {
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
}

NUMS_BRAILLE = {
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
}

PREFIX_BRAILLE = {
    'SPACE': '......',
    'CAPITAL_FOLLOW': '.....O',
    'NUMBER_FOLLOW': '.O.OOO'
}

BRAILLE_ALPHABET = {val: key for key, val in ALPHABET_BRAILLE.items()}
BRAILLE_NUMS = {val: key for key, val in NUMS_BRAILLE.items()}

def translate_english_braille(sentence):
    result = ""
    numberFollows = False
    for char in sentence:
        if char.isnumeric():
            if not numberFollows:
                result += PREFIX_BRAILLE['NUMBER_FOLLOW'] + NUMS_BRAILLE[char]
                numberFollows = True
            else:
                result += NUMS_BRAILLE[char]
        elif char.isupper():
                result += PREFIX_BRAILLE['CAPITAL_FOLLOW'] + ALPHABET_BRAILLE[char.lower()]
        elif char == " ":
            result += PREFIX_BRAILLE['SPACE']
            numberFollows = False
        else:
            result += ALPHABET_BRAILLE[char.lower()]
    return result

def translate_braille_english(sentence):
    result = ""
    numberFollows = False
    capitalFollows = False

    for idx in range(0, len(sentence), 6):
        partition = sentence[idx: idx + 6]
        if partition == PREFIX_BRAILLE['NUMBER_FOLLOW']:
            numberFollows = True
            capitalFollows = False
            continue
        elif partition == PREFIX_BRAILLE['CAPITAL_FOLLOW']:
            capitalFollows = True
            continue
        elif partition == PREFIX_BRAILLE['SPACE']:
            result += " "
            capitalFollows = False
            numberFollows = False
        elif numberFollows:
            result += BRAILLE_NUMS[partition]
            capitalFollows = False
        elif capitalFollows:
            result += BRAILLE_ALPHABET[partition].upper()
            capitalFollows = False
        else:
            result += BRAILLE_ALPHABET[partition]
            capitalFollows = False
    return result

def is_braille(input):
    braille = [".","O"]
    if len(input) % 6 != 0:
        return False

    for char in input:
        if char not in braille:
            return False
    return True


def main():
    if len(sys.argv) < 2:
        raise Exception("Missing arguments")
    else:
        args = sys.argv[1:]
        sentence = " ".join(args)
        if is_braille(sentence):
            print(translate_braille_english(sentence))
        else:
            print(translate_english_braille(sentence))


if __name__ == "__main__":
    main()


