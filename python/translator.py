import sys

BRAILE_MAPPING = {
    # letters
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    # Special Char
    '.....O': 'CAPS', '.O.OOO': 'NUM', '......': ' '
}

ENGLISH_MAPPING = {v: k for k, v in BRAILE_MAPPING.items()} # inverting dict mapping using https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping

NUMBER_MAPPING = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

NUMBER_REV_MAPPING = {v: k for k, v in NUMBER_MAPPING.items()}

def is_braile(phrase):
    n = len(phrase)
    for i in range(n):
        if phrase[i] != 'O' and phrase[i] != '.':
            return False
    return True

def braile_to_eng(phrase):
    curr = 0
    capslock = False
    numSwitch = False
    english = []
    for i in range(int(len(phrase)/6)):
        segment = phrase[curr:curr+6]
        if segment in BRAILE_MAPPING:
            if BRAILE_MAPPING[segment] == 'CAPS':
                capslock = True
            elif BRAILE_MAPPING[segment] == 'NUM':
                numSwitch = True
            elif BRAILE_MAPPING[segment] == ' ':
                numSwitch = False
                english.append(' ')
            else:
                hashed = BRAILE_MAPPING[segment]
                if capslock:
                    english.append(hashed.upper())
                    capslock = False
                elif numSwitch:
                    english.append(NUMBER_MAPPING[segment])
                else:
                    english.append(hashed)
        curr = curr + 6
    return english

def eng_to_braile(phrase):
    braile = []
    isNum = False

    for char in phrase:
        if char.isnumeric() and char in NUMBER_REV_MAPPING:
            if not isNum:
                braile.append(ENGLISH_MAPPING['NUM'])
            isNum = True
            braile.append(NUMBER_REV_MAPPING[char])
        elif char in ENGLISH_MAPPING or char.lower() in ENGLISH_MAPPING:
            isNum = False
            if char.isupper():
                braile.append(ENGLISH_MAPPING['CAPS'])
                char = char.lower()
            braile.append(ENGLISH_MAPPING[char])
    return braile

def main():
    # print(ENGLISH_MAPPING)
    if len(sys.argv) > 1:
        phrase = ' '.join(sys.argv[1:]) # used: https://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
        # print(phrase)
        if is_braile(phrase):
            word = braile_to_eng(phrase)
            n = len(word)
            for i in range(n):
                print(word[i], end="")
            print()
        else:
            braile = eng_to_braile(phrase)
            n = len(braile)
            for i in range(n):
                print(braile[i], end="")
            print()
    else:
        print("")


if __name__ == "__main__":
    main()